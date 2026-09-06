// SPDX-License-Identifier: AGPL-3.0-or-later
"use strict";
const copyButton = document.getElementById("copy-reference");
const reference = document.getElementById("donation-reference");
const copyStatus = document.getElementById("copy-status");
if (copyButton && reference && copyStatus) {
  copyButton.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(reference.value);
      copyStatus.textContent = "Reference copied.";
    } catch {
      reference.focus();
      reference.select();
      copyStatus.textContent = "Reference selected. Copy it using your browser or keyboard.";
    }
  });
}
