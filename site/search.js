// SPDX-License-Identifier: AGPL-3.0-or-later
(function () {
  "use strict";

  const weights = { title: 12, keywords: 8, subjects: 6, authors: 5, id: 15, abstract: 2 };
  const stopWords = new Set("a an the of for on in and or to with by about paper papers de del la las el los en y sobre un una".split(" "));

  function normalize(value) {
    return String(value || "").normalize("NFKD").replace(/\p{M}/gu, "").toLowerCase()
      .replace(/\\(?:mathrm|mathbf|mathsf|operatorname|text)\s*\{([^{}]*)\}/g, "$1")
      .replace(/\\(?:left|right|quad|qquad)\b|\\[,;!]/g, " ")
      // Keep Lie-group dimensions attached: SU(2), SU 2 and SU₂ match,
      // while SU(3), SU(20) and an unrelated number 2 stay distinct.
      .replace(/\b(su|so|sp|u|o)\s*(?:\(\s*(\d+|n)\s*\)|\[\s*(\d+|n)\s*\]|(\d+))(?=$|[^\p{L}\p{N}])/gu,
        (_, group, round, square, bare) => group + (round || square || bare))
      .replace(/[^\p{L}\p{N}]+/gu, " ").trim();
  }

  function queryTokens(query) {
    const all = normalize(query).split(/\s+/).filter(Boolean);
    const meaningful = all.filter(term => !stopWords.has(term));
    return [...new Set(meaningful.length ? meaningful : all)];
  }

  function makeIndex(records) {
    return records.map(record => {
      const fields = {};
      const all = new Set();
      for (const name of Object.keys(weights)) {
        const value = record[name];
        const text = normalize(Array.isArray(value) ? value.join(" ") : value);
        const tokens = text.split(/\s+/).filter(Boolean);
        fields[name] = { text, tokens };
        tokens.forEach(token => all.add(token));
      }
      return { record, fields, all };
    });
  }

  function tokenMatch(token, term) {
    if (token === term) return 1;
    // Prefixes help ordinary words; never broaden numeric scientific symbols.
    return term.length >= 4 && !/\p{N}/u.test(term) && token.startsWith(term) ? 0.45 : 0;
  }

  function search(index, query) {
    const terms = queryTokens(query);
    if (!terms.length) return [];
    const phrase = normalize(query);
    const rarity = new Map(terms.map(term => {
      const count = index.filter(entry => [...entry.all].some(token => tokenMatch(token, term))).length;
      return [term, 1 + Math.log(1 + index.length / (1 + count))];
    }));
    const results = [];
    for (const entry of index) {
      let score = 0;
      let matchedAll = true;
      const matchedFields = new Set();
      for (const term of terms) {
        let best = 0;
        let extra = 0;
        for (const [name, weight] of Object.entries(weights)) {
          const hits = entry.fields[name].tokens.map(token => tokenMatch(token, term)).filter(Boolean);
          if (!hits.length) continue;
          matchedFields.add(name);
          // Saturation prevents a long abstract repeating a term from burying
          // a paper whose title or keywords explicitly name the topic.
          const contribution = weight * Math.max(...hits) * (1 + 0.15 * Math.min(hits.length - 1, 3));
          best = Math.max(best, contribution);
          extra += contribution * 0.05;
        }
        if (!best) { matchedAll = false; break; }
        score += (best + extra) * rarity.get(term);
      }
      if (!matchedAll) continue;
      for (const [name, weight] of Object.entries(weights)) {
        if ((" " + entry.fields[name].text + " ").includes(" " + phrase + " ")) score += weight * 2;
      }
      if (entry.fields.id.text === phrase) score += 1000;
      results.push({ record: entry.record, score, matchedFields: [...matchedFields] });
    }
    // Stable alphabetical ties; activity, donations and assessment scores are
    // deliberately absent from the relevance calculation.
    return results.sort((a, b) => b.score - a.score ||
      a.record.title.localeCompare(b.record.title, "en") || a.record.id.localeCompare(b.record.id));
  }

  function excerpt(text, query, limit = 400) {
    const sentences = String(text || "").split(/(?<=[.!?])\s+/);
    const terms = queryTokens(query);
    let best = 0;
    let bestCount = -1;
    sentences.forEach((sentence, position) => {
      const tokens = normalize(sentence).split(" ");
      const count = terms.filter(term => tokens.some(token => tokenMatch(token, term))).length;
      if (count > bestCount) { best = position; bestCount = count; }
    });
    const selected = sentences.slice(best).join(" ");
    return (best ? "… " : "") + selected.slice(0, limit) + (selected.length > limit ? "…" : "");
  }

  function filterResults(index, query, filters = {}) {
    let hits = query.trim() ? search(index, query) : index.map(entry => ({ record: entry.record, score: 0, matchedFields: [] }));
    hits = hits.filter(({ record }) =>
      (!filters.subject || (record.subject_ids || []).includes(filters.subject) || (record.subjects || []).some(subject => normalize(subject) === normalize(filters.subject))) &&
      (!filters.status || record.status === filters.status) &&
      (!filters.year || String(record.date || "").slice(0, 4) === filters.year));
    const sort = filters.sort === "relevance" || !filters.sort ? (query.trim() ? "relevance" : "newest") : filters.sort;
    const byTitle = (a, b) => a.record.title.localeCompare(b.record.title, "en") || a.record.id.localeCompare(b.record.id);
    if (sort === "newest" || sort === "oldest") hits.sort((a, b) => {
      const dates = String(a.record.date || "").localeCompare(String(b.record.date || ""));
      return (sort === "newest" ? -dates : dates) || byTitle(a, b);
    });
    if (sort === "title") hits.sort(byTitle);
    return hits;
  }

  // Export the same implementation for deterministic, dependency-free tests.
  if (typeof module !== "undefined" && module.exports) module.exports = { normalize, queryTokens, makeIndex, search, excerpt, filterResults };
  if (typeof document === "undefined") return;
  const root = document.querySelector("[data-paper-search]");
  if (!root) return;
  const form = root.querySelector("form");
  const input = form.elements.q;
  const status = root.querySelector(".search-status");
  const list = root.querySelector(".search-results");
  const more = root.querySelector(".search-more");
  let indexPromise;
  let requestNumber = 0;
  let results = [];
  let shown = 0;
  let activeQuery = "";
  let activeFilters = {};
  let timer;

  function element(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  }

  function appendResults() {
    const start = shown;
    const end = Math.min(shown + 25, results.length);
    const fragment = document.createDocumentFragment();
    const labels = { accepted: "Accepted", corrected: "Corrected", archived: "Historical import", withdrawn: "Withdrawn" };
    for (let i = shown; i < end; i++) {
      const record = results[i].record;
      const item = element("li", "paper-card");
      const meta = element("div", "paper-meta");
      meta.append(element("span", "badge badge-" + record.status, labels[record.status] || record.status));
      meta.append(element("span", "", record.id + " · " + record.version));
      const header = element("div", "paper-card-header");
      header.append(meta, element("span", "paper-date", record.date));
      const title = element("h2", "search-result-title");
      const link = element("a", "", record.title);
      const target = new URL(record.url, location.origin);
      // Public metadata is text, never HTML; result links stay on this archive.
      if (target.origin === location.origin && /^https?:$/.test(target.protocol)) link.href = target.href;
      title.append(link);
      const cite = element("a", "paper-card-cite", "Cite this version");
      if (link.href && /^v[1-9]\d*$/.test(record.version)) {
        cite.href = new URL(`versions/${record.version}/#cite`, target).href;
      }
      const byline = element("div", "paper-byline");
      byline.append(element("p", "authors", record.authors.join(", ")), cite);
      item.append(header, title, byline,
        element("p", "paper-summary search-excerpt", excerpt(record.abstract, activeQuery)));
      const topics = [...new Set([...record.keywords, ...record.subjects])];
      if (topics.length) item.append(element("div", "search-topics", topics.slice(0, 6).join(" · ")));
      fragment.append(item);
    }
    list.append(fragment);
    shown = end;
    more.hidden = shown >= results.length;
    const labelsBySort = { relevance: activeQuery ? "By relevance" : "Newest first", newest: "Newest first", oldest: "Oldest first", title: "Title A–Z" };
    const scope = activeQuery ? ` for “${activeQuery}”` : " in the catalogue";
    const filtered = [activeFilters.subject, activeFilters.status, activeFilters.year].filter(Boolean).length;
    status.textContent = `${results.length} ${results.length === 1 ? "record" : "records"}${scope} · ${labelsBySort[activeFilters.sort]}${filtered ? " · Filters applied" : ""} · Showing ${shown}`;
    return start;
  }

  function loadIndex() {
    if (!indexPromise) {
      indexPromise = (async () => {
        const controller = new AbortController();
        const timeout = setTimeout(() => controller.abort(), 15000);
        try {
          const response = await fetch(root.dataset.indexUrl, { signal: controller.signal });
          if (!response.ok) throw new Error("Catalogue unavailable");
          const records = await response.json();
          if (!Array.isArray(records)) throw new Error("Invalid catalogue");
          return makeIndex(records);
        } finally { clearTimeout(timeout); }
      })().catch(error => { indexPromise = undefined; throw error; });
    }
    return indexPromise;
  }

  async function runSearch() {
    const request = ++requestNumber;
    const query = input.value.trim().slice(0, 300);
    list.replaceChildren();
    results = [];
    shown = 0;
    more.hidden = true;
    root.removeAttribute("aria-busy");
    const filters = Object.fromEntries(["subject", "status", "year", "sort"].map(name => [name, form.elements[name].value]));
    status.textContent = "Searching the complete catalogue…";
    root.setAttribute("aria-busy", "true");
    try {
      const index = await loadIndex();
      if (request !== requestNumber) return;
      activeQuery = query;
      activeFilters = filters;
      results = filterResults(index, query, filters);
      if (!results.length) {
        status.textContent = `No records match${query ? ` “${query}”` : " these filters"}. Try fewer words or clear the filters.`;
      } else { appendResults(); }
    } catch (_) {
      if (request === requestNumber) status.textContent = "The catalogue could not be loaded. Please press Search to try again, or browse Papers above.";
    } finally {
      if (request === requestNumber) root.removeAttribute("aria-busy");
    }
  }

  function updateURL(push) {
    const url = new URL(location.href);
    const query = input.value.trim().slice(0, 300);
    if (query) url.searchParams.set("q", query); else url.searchParams.delete("q");
    ["subject", "status", "year", "sort"].forEach(name => {
      const value = form.elements[name].value;
      if (value && !(name === "sort" && value === "relevance")) url.searchParams.set(name, value);
      else url.searchParams.delete(name);
    });
    if (url.href !== location.href) history[push ? "pushState" : "replaceState"](null, "", url);
  }

  form.addEventListener("submit", event => {
    event.preventDefault();
    clearTimeout(timer);
    updateURL(true);
    runSearch();
  });
  input.addEventListener("input", () => {
    clearTimeout(timer);
    // Invalidate pending work immediately, before the typing debounce elapses.
    requestNumber++;
    timer = setTimeout(() => { updateURL(false); runSearch(); }, 180);
  });
  root.querySelectorAll("select").forEach(select => select.addEventListener("change", () => {
    clearTimeout(timer);
    updateURL(true);
    runSearch();
  }));
  root.querySelector("[data-reset-filters]").addEventListener("click", () => {
    clearTimeout(timer);
    ["subject", "status", "year"].forEach(name => { form.elements[name].value = ""; });
    form.elements.sort.value = "relevance";
    updateURL(true);
    runSearch();
  });
  more.addEventListener("click", () => {
    const firstNew = appendResults();
    list.children[firstNew]?.querySelector("h2 a")?.focus();
  });
  function restoreQuery() {
    clearTimeout(timer);
    input.value = (new URL(location.href).searchParams.get("q") || "").slice(0, 300);
    const params = new URL(location.href).searchParams;
    ["subject", "status", "year", "sort"].forEach(name => {
      const select = form.elements[name];
      const value = (params.get(name) || (name === "sort" ? "relevance" : "")).slice(0, 160);
      // An obsolete subject/year must yield zero matches, not silently broaden a saved search.
      if (value && (name === "subject" || name === "year") && ![...select.options].some(option => option.value === value)) {
        const option = element("option", "", value);
        option.value = value;
        select.append(option);
      }
      select.value = value;
      if (select.selectedIndex < 0) select.value = name === "sort" ? "relevance" : "";
    });
    runSearch();
  }
  window.addEventListener("popstate", restoreQuery);
  restoreQuery();
}());
