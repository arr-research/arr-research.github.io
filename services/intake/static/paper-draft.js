'use strict';
(() => {
  const form = document.getElementById('paper-draft');
  if (!form) return;
  const feedback = document.getElementById('draft-feedback');
  const fileInput = form.elements.manuscript;
  const fileFeedback = document.getElementById('pdf-feedback');
  const retry = document.getElementById('retry-paper-start');
  const starting = Boolean(form.dataset.startUrl);
  let ready = !starting, creating = false, timer, saving = false, dirty = false, leaving = false;

  async function saveDraft() {
    if (!ready || saving || leaving) return;
    saving = true; dirty = false;
    // Autosave contains details only: neither the PDF nor the paper key.
    const data = new FormData(form); data.delete('manuscript'); data.set('action', 'save');
    feedback.textContent = 'Saving your details…';
    try {
      const result = await fetch(form.action, {method: 'POST', body: data, headers: {'X-Draft-Save': '1'}});
      if (!result.ok || !(await result.json()).saved) throw new Error('save');
      feedback.textContent = 'Details saved. You can return with your key; select the PDF again if you leave.';
    } catch { feedback.textContent = 'Your details could not be saved. Keep this page open and try Save draft for later.'; }
    finally { saving = false; if (dirty && !leaving) timer = setTimeout(saveDraft, 800); }
  }
  function queueSave(delay = 900) { dirty = true; clearTimeout(timer); timer = setTimeout(saveDraft, delay); }

  async function choosePDF() {
    const file = fileInput.files[0];
    fileInput.setCustomValidity('');
    if (!file) { fileFeedback.textContent = 'Choose a PDF when you are ready.'; return; }
    const problem = file.size > 25 * 1024 * 1024 ? 'Choose a PDF no larger than 25 MiB.' : !/\.pdf$/i.test(file.name) ? 'Choose a file ending in .pdf.' : '';
    if (problem) { fileInput.setCustomValidity(problem); fileFeedback.textContent = problem; return; }
    fileFeedback.textContent = `${file.name} · ${(file.size / 1024 / 1024).toFixed(1)} MiB · selected on this device`;
    if (ready || creating) return;
    creating = true; retry.hidden = true;
    fileFeedback.textContent = 'Opening your private draft… Your PDF stays on this device.';
    const data = new FormData(); data.set('csrf_token', form.elements.csrf_token.value);
    data.set('subject', form.elements.primary_subject.value);
    try {
      const result = await fetch(form.dataset.startUrl, {method: 'POST', body: data, headers: {'X-Paper-Start': '1'}});
      if (!result.ok) throw new Error('start');
      const value = await result.json();
      if (!/^AIRR-[A-Za-z0-9_-]{43}$/.test(value.key) || !/^\/paper\/draft\/[a-f0-9]{32}$/.test(value.draft_url)) throw new Error('response');
      // Keep the same file input and document: choosing a file never loses it to a redirect.
      form.action = value.draft_url;
      document.getElementById('paper-secret').value = value.key;
      document.getElementById('paper-details').hidden = false;
      ready = true;
      history.replaceState(null, '', value.draft_url);
      fileFeedback.textContent = `${fileInput.files[0]?.name || file.name} is ready. Check the details below, save your key and send.`;
      form.elements.title.focus({preventScroll: true});
    } catch {
      fileFeedback.textContent = 'We could not open a draft. Your selected PDF is still here. Try again, or return later.';
      retry.hidden = false;
    } finally { creating = false; }
  }
  fileInput.addEventListener('change', choosePDF);
  retry?.addEventListener('click', choosePDF);
  const drop = document.getElementById('pdf-drop');
  for (const event of ['dragenter', 'dragover']) drop.addEventListener(event, e => { e.preventDefault(); drop.classList.add('is-dragging'); });
  for (const event of ['dragleave', 'drop']) drop.addEventListener(event, e => { e.preventDefault(); drop.classList.remove('is-dragging'); });
  drop.addEventListener('drop', e => {
    if (e.dataTransfer.files.length !== 1) { fileFeedback.textContent = 'Choose one PDF for this paper.'; return; }
    fileInput.files = e.dataTransfer.files; choosePDF();
  });
  form.addEventListener('input', e => { if (!['file', 'checkbox'].includes(e.target.type)) queueSave(); });
  form.addEventListener('change', e => { if (e.target.tagName === 'SELECT' || e.target.name === 'operator_conflict') queueSave(200); });
  form.addEventListener('submit', e => {
    if (!ready || leaving || (starting && !form.elements.key_saved.checked)) {
      e.preventDefault();
      if (ready && !leaving) { document.getElementById('key-feedback').textContent = 'Save your key and tick “I have saved my secret paper key” before leaving this page.'; document.getElementById('paper-secret').focus(); }
      return;
    }
    leaving = true; clearTimeout(timer);
    if (e.submitter?.value === 'save') fileInput.disabled = true;
    feedback.textContent = e.submitter?.value === 'save' ? 'Saving your draft…' : 'Sending your paper securely… Please keep this page open for the receipt.';
  });
  window.addEventListener('beforeunload', e => {
    if (starting && ready && !leaving && !form.elements.key_saved.checked) { e.preventDefault(); e.returnValue = ''; }
  });

  const extract = document.getElementById('extract-details');
  extract.addEventListener('click', async () => {
    const message = document.getElementById('extract-feedback');
    const file = fileInput.files[0];
    if (!file) { message.textContent = 'Choose a PDF first, or enter the details below.'; return; }
    if (!fileInput.checkValidity()) { message.textContent = fileInput.validationMessage; return; }
    extract.disabled = true; message.textContent = 'Scanning and reading your PDF…';
    const data = new FormData(); data.set('manuscript', file); data.set('csrf_token', form.elements.csrf_token.value);
    try {
      const result = await fetch(extract.dataset.url, {method: 'POST', body: data});
      const value = await result.json();
      if (!result.ok) throw new Error(value.error || 'Enter the title and abstract below; you can still submit.');
      if (fileInput.files[0] !== file || leaving) return;
      let filled = 0;
      for (const field of ['title', 'abstract']) {
        if (!form.elements[field].value.trim() && value[field]) { form.elements[field].value = value[field]; filled++; }
      }
      message.textContent = filled ? 'Suggested text added. Check it against your PDF. Anything you already wrote was kept.' : 'No empty fields could be filled. Your existing text is unchanged; you can enter the details yourself.';
      queueSave(200);
    } catch (error) { message.textContent = error.message || 'Enter the title and abstract manually.'; }
    finally { extract.disabled = false; }
  });
  if (starting) {
    document.getElementById('paper-start-enhanced').hidden = false;
    document.getElementById('paper-start-fallback').hidden = true;
  }
})();
