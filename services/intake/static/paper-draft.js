'use strict';
const form = document.getElementById('paper-draft');
const feedback = document.getElementById('draft-feedback');
let timer, saving = false, dirty = false, leaving = false;
async function saveDraft() {
  if (saving || leaving) return;
  saving = true; dirty = false;
  const data = new FormData(form); data.delete('manuscript'); data.set('action', 'save');
  feedback.textContent = 'Saving draft…';
  try {
    const result = await fetch(location.pathname, {method: 'POST', body: data, headers: {'X-Draft-Save': '1'}});
    if (!result.ok || !(await result.json()).saved) throw new Error('save');
    feedback.textContent = 'Draft saved. The PDF uploads only when you send.';
  } catch { feedback.textContent = 'Draft could not be saved. Keep this page open and try Save draft.'; }
  finally { saving = false; if (dirty && !leaving) timer = setTimeout(saveDraft, 800); }
}
form.addEventListener('input', event => {
  if (event.target.type === 'file' || event.target.type === 'checkbox') return;
  dirty = true; clearTimeout(timer); timer = setTimeout(saveDraft, 1200);
});
form.addEventListener('change', event => {
  if (event.target.tagName === 'SELECT' || event.target.name === 'operator_conflict') {
    dirty = true; clearTimeout(timer); timer = setTimeout(saveDraft, 200);
  }
});
form.addEventListener('submit', () => { leaving = true; clearTimeout(timer); });

const extract = document.getElementById('extract-details');
extract.addEventListener('click', async () => {
  const message = document.getElementById('extract-feedback');
  const file = form.elements.manuscript.files[0];
  if (!file) { message.textContent = 'Choose a PDF first.'; return; }
  if (file.size > 25 * 1024 * 1024) { message.textContent = 'The PDF must be no larger than 25 MiB.'; return; }
  extract.disabled = true; message.textContent = 'Scanning and reading your PDF…';
  const data = new FormData(); data.set('manuscript', file); data.set('csrf_token', form.elements.csrf_token.value);
  try {
    const result = await fetch(extract.dataset.url, {method: 'POST', body: data});
    const value = await result.json();
    if (!result.ok) throw new Error(value.error || 'Extraction is unavailable. Enter details manually.');
    for (const field of ['title', 'abstract']) {
      if (!form.elements[field].value.trim() && value[field]) form.elements[field].value = value[field];
    }
    message.textContent = value.notice + ' Existing text has been kept.';
    dirty = true; clearTimeout(timer); timer = setTimeout(saveDraft, 200);
  } catch (error) { message.textContent = error.message || 'Enter the title and abstract manually.'; }
  finally { extract.disabled = false; }
});
