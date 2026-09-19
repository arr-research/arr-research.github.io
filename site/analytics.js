/* Optional aggregate measurement. No request is sent before an affirmative choice. */
(() => {
  'use strict';
  const script = document.currentScript;
  if (!script || !['airr.science', 'www.airr.science'].includes(location.hostname)) return;
  const path = script.dataset.page;
  if (!path) return;
  const key = 'airr-statistics-choice-v1';
  let choice = null;
  try {
    const saved = JSON.parse(localStorage.getItem(key));
    if (saved && saved.expires > Date.now() && ['allow','decline'].includes(saved.value)) choice = saved.value;
  } catch (_) { /* No storage means no default consent. */ }
  const counted = new Set();
  const panel = document.createElement('section');
  panel.className = 'statistics-choice';
  panel.setAttribute('aria-label', 'Anonymous statistics preference');
  panel.innerHTML = '<p><strong>Allow anonymous statistics?</strong> Help AIRR count visits to public pages and PDF opens. No visitor profiles. <a href="/privacy/">Privacy details</a></p><div><button type="button" data-value="allow">Allow</button><button type="button" data-value="decline">Decline</button></div>';
  panel.hidden = choice !== null;
  const controls = document.createElement('button');
  controls.type = 'button'; controls.className = 'statistics-settings';
  controls.textContent = 'Statistics preferences';
  controls.addEventListener('click', () => {panel.hidden = !panel.hidden;});
  document.body.appendChild(panel);
  document.querySelector('footer')?.appendChild(controls);
  // Each label (this page, or one version's PDF) counts at most once per page load.
  function count(label = path) {
    if (counted.has(label) || choice !== 'allow') return;
    counted.add(label);
    fetch('https://submit.airr.science/api/v1/pageviews', {
      method: 'POST', mode: 'cors', credentials: 'omit', referrerPolicy: 'no-referrer',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({path: label, consent: 'aggregate-v1'}), keepalive: true
    }).catch(() => {});
  }
  panel.querySelectorAll('button').forEach(button => button.addEventListener('click', () => {
    choice = button.dataset.value;
    try {localStorage.setItem(key, JSON.stringify({value:choice, expires:Date.now()+180*86400000}));} catch (_) {}
    panel.hidden = true;
    count();
  }));
  // PDF links carry a build-time label; opening one sends that label instead of the file URL.
  function pdfOpen(event) {
    if (event.type === 'auxclick' && event.button !== 1) return;
    const link = event.target?.closest?.('a[data-pdf-event]');
    if (link) count(link.dataset.pdfEvent);
  }
  document.addEventListener('click', pdfOpen);
  document.addEventListener('auxclick', pdfOpen);
  document.querySelectorAll('details[data-pdf-event]').forEach(preview => preview.addEventListener('toggle', () => {
    if (preview.open) count(preview.dataset.pdfEvent);
  }));
  count();
})();
