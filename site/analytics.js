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
  let counted = false;
  const panel = document.createElement('section');
  panel.className = 'statistics-choice';
  panel.setAttribute('aria-label', 'Anonymous statistics preference');
  panel.innerHTML = '<p><strong>Allow anonymous statistics?</strong> Help AIRR count visits to public pages. No visitor profiles. <a href="/privacy/">Privacy details</a></p><div><button type="button" data-value="allow">Allow</button><button type="button" data-value="decline">Decline</button></div>';
  panel.hidden = choice !== null;
  const controls = document.createElement('button');
  controls.type = 'button'; controls.className = 'statistics-settings';
  controls.textContent = 'Statistics preferences';
  controls.addEventListener('click', () => {panel.hidden = !panel.hidden;});
  document.body.appendChild(panel);
  document.querySelector('footer')?.appendChild(controls);
  function count() {
    if (counted || choice !== 'allow') return;
    counted = true;
    fetch('https://submit.airr.science/api/v1/pageviews', {
      method: 'POST', mode: 'cors', credentials: 'omit', referrerPolicy: 'no-referrer',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({path, consent: 'aggregate-v1'}), keepalive: true
    }).catch(() => {});
  }
  panel.querySelectorAll('button').forEach(button => button.addEventListener('click', () => {
    choice = button.dataset.value;
    try {localStorage.setItem(key, JSON.stringify({value:choice, expires:Date.now()+180*86400000}));} catch (_) {}
    panel.hidden = true;
    count();
  }));
  count();
})();
