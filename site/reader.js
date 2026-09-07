// SPDX-License-Identifier: AGPL-3.0-or-later
(function () {
  "use strict";
  const status = document.querySelector("[data-copy-status]");
  document.querySelectorAll("[data-copy-target]").forEach(button => {
    button.hidden = false;
    button.addEventListener("click", async () => {
      const target = document.getElementById(button.dataset.copyTarget);
      if (!target) return;
      try {
        await navigator.clipboard.writeText(target.value || target.textContent.trim());
        if (status) status.textContent = button.dataset.copyLabel + " copied.";
      } catch (_) {
        if (status) status.textContent = "Copy is unavailable in this browser. Select the reference below or download a citation file.";
        target.focus();
        if (typeof target.select === "function") target.select();
      }
    });
  });
  const preview = document.querySelector("[data-pdf-preview]");
  if (!preview) return;
  preview.addEventListener("toggle", () => {
    if (!preview.open || preview.querySelector("iframe")) return;
    const source = new URL(preview.dataset.pdfPreview, location.href);
    // Only render an archive-hosted, version-specific PDF. No remote viewer.
    if (source.origin !== location.origin || !source.pathname.endsWith(".pdf")) return;
    const frame = document.createElement("iframe");
    frame.title = preview.dataset.pdfTitle;
    frame.src = source.href;
    frame.className = "pdf-frame";
    preview.querySelector(".pdf-preview-body").append(frame);
  });
}());
