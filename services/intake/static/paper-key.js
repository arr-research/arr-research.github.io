'use strict';
const secret = document.getElementById('paper-secret');
const feedback = document.getElementById('key-feedback');
document.getElementById('copy-paper-key').addEventListener('click', async () => {
  try { await navigator.clipboard.writeText(secret.value); feedback.textContent = 'Key copied. Save it somewhere private.'; }
  catch { secret.select(); feedback.textContent = 'Select and copy the key above.'; }
});
document.getElementById('download-paper-key').addEventListener('click', () => {
  const text = `AIRR paper management key\n\n${secret.value}\n\nOpen ${location.origin}/manage\nKeep this file private. Anyone with this key can manage this paper.\n`;
  const url = URL.createObjectURL(new Blob([text], {type: 'text/plain'}));
  const link = document.createElement('a'); link.href = url; link.download = 'airr-paper-key.txt'; link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000); feedback.textContent = 'Keep the downloaded key file in a safe place.';
});
