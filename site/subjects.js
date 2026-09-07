// SPDX-License-Identifier: AGPL-3.0-or-later
(function () {
  "use strict";
  const normalize = value => String(value || "").normalize("NFKD").replace(/\p{M}/gu, "").toLowerCase().replace(/[^\p{L}\p{N}]+/gu, " ").trim();
  function findSubjects(terms, query, family = "", populated = false) {
    const q = normalize(query);
    const words = q.split(/\s+/).filter(Boolean);
    return terms.map(term => {
      const label = normalize(term.label);
      const aliases = [...Object.values(term.labels || {}), ...(term.aliases || [])].map(normalize);
      const text = [label, normalize(term.path), ...aliases].join(" ");
      const tokens = text.split(/\s+/);
      const matches = words.every(w => tokens.some(t => t === w || (w.length >= 3 && t.startsWith(w))));
      const score = label === q ? 100 : aliases.includes(q) ? 80 : label.startsWith(q) ? 60 : 0;
      return {term, matches, score};
    }).filter(({term, matches}) => matches && (!family || term.family === family) && (!populated || term.count > 0))
      .sort((a, b) => b.score - a.score || a.term.path.localeCompare(b.term.path, "en"))
      .map(({term}) => term);
  }
  if (typeof module !== "undefined" && module.exports) module.exports = {normalize, findSubjects};
  if (typeof document === "undefined") return;
  window.AIRRSubjects = {normalize, findSubjects};
  const root = document.querySelector("[data-subject-browser]");
  if (!root) return;
  const filters = root.querySelector(".subject-filters");
  const query = root.querySelector("[data-subject-query]");
  const family = root.querySelector("[data-subject-family]");
  const populated = root.querySelector("[data-subject-published]");
  const tree = root.querySelector(".subject-tree");
  const list = root.querySelector(".subject-matches");
  const status = root.querySelector(".subject-result-status");
  const more = root.querySelector("[data-subject-more]");
  const base = root.dataset.base;
  let terms = [], hits = [], shown = 0;
  function element(tag, cls, value) {
    const el = document.createElement(tag);
    el.className = cls;
    if (value) el.textContent = value;
    return el;
  }
  function append() {
    const start = shown;
    const batch = hits.slice(shown, shown + 48);
    for (const term of batch) {
      const card = element("article", "subject-match");
      card.append(element("h2", "", term.label), element("p", "subject-path", term.path));
      const actions = element("div", "subject-actions");
      if (term.count) {
        const link = element("a", "", `${term.count} paper${term.count === 1 ? "" : "s"} →`);
        link.href = `${base}/search/?subject=${encodeURIComponent(term.id)}`;
        actions.append(link);
      } else actions.append(element("span", "subject-empty", "No papers yet"));
      const use = element("a", "", "Use subject");
      use.href = `${base}/submit/?subject=${encodeURIComponent(term.id)}`;
      use.setAttribute("aria-label", `Submission information for ${term.label}`);
      actions.append(use); card.append(actions); list.append(card);
    }
    shown += batch.length;
    more.hidden = shown >= hits.length;
    status.textContent = `${hits.length} matching fields · showing ${shown}.`;
    return start;
  }
  function update(save = true) {
    const active = query.value.trim() || family.value || populated.checked;
    tree.hidden = !!active; list.hidden = !active;
    list.replaceChildren(); shown = 0; more.hidden = true;
    if (active) {
      hits = findSubjects(terms, query.value, family.value, populated.checked); append();
      if (!hits.length) {
        status.textContent = populated.checked ? "No fields with papers match these filters. Clear ‘With papers only’ to include fields available for future submissions." : "No matching field. Try a broader term, change the filters, or describe an emerging topic in the submission form.";
        if (!populated.checked) {
          const link = element("a", "text-link", "Use Other or emerging research areas →");
          link.href = `${base}/submit/?subject=airr-other-or-emerging-research-areas`;list.append(link);
        }
      }
    } else status.textContent = `${terms.length.toLocaleString("en")} fields · expand a family or search in English, Spanish, French, German, Italian or Polish.`;
    if (save) {
      const url = new URL(location.href);
      for (const [key, value] of [["q", query.value], ["family", family.value], ["populated", populated.checked ? "1" : ""]]) {
        if (value) url.searchParams.set(key, value); else url.searchParams.delete(key);
      }
      history.replaceState(null, "", url);
    }
  }
  function restore() {
    const params = new URL(location.href).searchParams;
    query.value = (params.get("q") || "").slice(0,160);
    family.value = params.get("family") || ""; populated.checked = params.get("populated") === "1"; update(false);
  }
  fetch(root.dataset.vocabularyUrl, {credentials: "omit"}).then(response => {
    if (!response.ok) throw Error("vocabulary"); return response.json();
  }).then(data => {
    terms = data.terms; filters.hidden = false; restore();
    let timer;
    query.addEventListener("input", () => {clearTimeout(timer); timer = setTimeout(update, 120);});
    family.addEventListener("change", () => update()); populated.addEventListener("change", () => update());
    more.addEventListener("click", () => {const first = append(); list.children[first]?.querySelector("a")?.focus();});
    window.addEventListener("popstate", restore);
  }).catch(() => {status.textContent = "Search is temporarily unavailable. Expand the families below to browse every field.";});
})();
