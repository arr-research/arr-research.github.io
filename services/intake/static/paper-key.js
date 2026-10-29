'use strict';
(() => {
  const secret = document.getElementById('paper-secret');
  if (!secret) return;
  const feedback = document.getElementById('key-feedback');
  document.getElementById('copy-paper-key').addEventListener('click', async () => {
    if (!secret.value) return;
    try { await navigator.clipboard.writeText(secret.value); feedback.textContent = 'Key copied. Save it somewhere private so you can return.'; }
    catch { secret.select(); feedback.textContent = 'Select and copy the key above.'; }
  });
  document.getElementById('download-paper-key').addEventListener('click', () => {
    if (!secret.value) return;
    const title = document.getElementById('paper-draft')?.elements.title.value.trim();
    const text = `AIRR paper management key\n${title ? 'Paper: ' + title + '\n' : ''}\n${secret.value}\n\nOpen ${location.origin}/manage\nKeep this file private. Anyone with this key can manage this paper. Lost keys cannot be recovered.\n`;
    const url = URL.createObjectURL(new Blob([text], {type: 'text/plain'}));
    const link = document.createElement('a'); link.href = url; link.download = 'airr-paper-key.txt'; link.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000); feedback.textContent = 'Keep the downloaded key file somewhere private. Use it at “Manage my paper”.';
  });
})();
