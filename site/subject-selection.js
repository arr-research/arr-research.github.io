// SPDX-License-Identifier: AGPL-3.0-or-later
(function () {
  "use strict";
  const root = document.querySelector("[data-selected-subject]");
  const id = new URL(location.href).searchParams.get("subject");
  if (!root || !id) return;
  root.hidden = false;
  root.textContent = "Loading your selected subject…";
  fetch(root.dataset.vocabularyUrl, {credentials: "omit"}).then(response => {
    if (!response.ok) throw Error("vocabulary"); return response.json();
  }).then(data => {
    const term = data.terms.find(t => t.id === id);
    if (!term) {root.textContent = "That subject is not in the current catalogue. Choose a subject to continue.";return;}
    root.textContent = `Selected subject: ${term.path}. `;
    const intake = root.dataset.intakeUrl;
    if (intake) {
      const link = document.querySelector(".intake-link");
      if (link) {const url = new URL(link.href);url.searchParams.set("subject", id);link.href = url.href;}
      root.append("The private form will keep this selection. Registration remains subject to approval.");
    } else root.append("Private uploads are not open yet. Keep this page to carry the subject into the form when intake opens. No manuscript has been registered.");
  }).catch(() => {root.textContent = "The subject could not be loaded. You can choose it again from the subject directory.";});
})();
