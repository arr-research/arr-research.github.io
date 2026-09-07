// SPDX-License-Identifier: AGPL-3.0-or-later
(function () {
  "use strict";
  const root = document.querySelector("[data-subject-pickers]");
  if (!root || !window.AIRRSubjects) return;
  fetch(root.dataset.catalogueUrl, {credentials: "same-origin"}).then(response => {
    if (!response.ok) throw Error("vocabulary");return response.json();
  }).then(data => {
    root.querySelectorAll(".subject-picker").forEach(picker => {
      const input = picker.querySelector("[data-picker-search]");
      const select = picker.querySelector("select");
      const status = picker.querySelector("[data-picker-status]");
      const originals = [...select.children].map(child => child.cloneNode(true));
      picker.querySelector("[data-picker-search-label]").hidden = false;
      const optionLabel = term => term.label + (term.parent ? " — " + term.path.split(" › ").slice(0,-1).join(" › ") : "");
      const selectionMessage = () => select.value ? `Selected: ${data.terms.find(t => t.id === select.value)?.label || select.selectedOptions[0].textContent}` : "No subject selected.";
      if (select.value) status.textContent = selectionMessage();
      function update() {
        const selected = select.value;
        if (!input.value.trim()) {
          select.replaceChildren(...originals.map(child => child.cloneNode(true)));
          select.value = selected;
          status.textContent = "All fields available. Select a field below, or type to narrow the list.";
          return;
        }
        const matches = window.AIRRSubjects.findSubjects(data.terms, input.value);
        const choices = matches.slice(0, 100);
        const current = data.terms.find(t => t.id === selected);
        if (current && !choices.some(t => t.id === selected)) choices.unshift(current);
        select.replaceChildren(new Option(select.required ? "Choose a subject" : "None", ""));
        choices.forEach(t => select.add(new Option(optionLabel(t), t.id)));
        select.value = selected;
        status.textContent = `${matches.length} matching fields${matches.length > 100 ? "; showing the first 100 — type more to narrow" : ""}. Your current selection is kept until you choose another.`;
      }
      let timer;
      input.addEventListener("input", () => {clearTimeout(timer);timer = setTimeout(update, 120);});
      select.addEventListener("change", () => {status.textContent = selectionMessage();});
    });
  }).catch(() => {root.querySelectorAll("[data-picker-status]").forEach(el => {el.textContent = "Search could not load. All fields remain available in the list.";});});
})();
