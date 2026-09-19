// SPDX-License-Identifier: AGPL-3.0-or-later
// Typeset inline TeX in titles and abstracts with the self-hosted KaTeX build.
// Citation text, permalinks and code stay verbatim so copied references are unchanged.
(function () {
  "use strict";
  const targets = [
    "main h1", ".paper-card h3", ".paper-summary", ".abstract p", ".rank-paper-main h3",
    ".assessment-rank-row h3", ".related-records a", "td a", ".search-result-title", ".search-results .paper-summary",
  ].join(",");
  const options = {
    delimiters: [
      {left: "$$", right: "$$", display: false},
      {left: "$", right: "$", display: false},
      {left: "\\(", right: "\\)", display: false},
    ],
    throwOnError: false,
    ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code", "input", "option"],
  };
  function render(root) {
    if (typeof window.renderMathInElement !== "function") return;
    (root || document).querySelectorAll(targets).forEach(element => {
      if (element.dataset.mathRendered || !/\$|\\\(/.test(element.textContent)) return;
      element.dataset.mathRendered = "1";
      window.renderMathInElement(element, options);
    });
  }
  window.airrRenderMath = render;
  render(document);
}());
