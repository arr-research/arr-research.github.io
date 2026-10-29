const {test} = require('node:test');
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');

function setup({failStart = false} = {}) {
  const nodes = new Map(), calls = [], timers = [], history = [];
  function node(id) {
    if (!nodes.has(id)) nodes.set(id, {value:'', hidden:true, files:[], dataset:{}, listeners:{}, checked:false,
      addEventListener(type, fn) {(this.listeners[type] ||= []).push(fn);},
      async fire(type, event={}) {for (const fn of this.listeners[type] || []) await fn({target:this,...event});},
      setCustomValidity(value) {this.validationMessage=value;}, checkValidity() {return !this.validationMessage;},
      focus() {}, classList:{add() {},remove() {}}});
    return nodes.get(id);
  }
  const form = node('paper-draft'); form.dataset.startUrl='/paper/new'; form.action='/paper/new';
  form.elements = Object.fromEntries(['manuscript','csrf_token','primary_subject','title','abstract','authors','key_saved','agreement'].map(k=>[k,node(k)]));
  form.elements.csrf_token.value='test-csrf'; form.elements.primary_subject.value='airr-quantum-information';
  node('extract-details').dataset.url='/paper/extract';
  class Data extends Map {
    constructor(source) {super(); if (source) for (const [k,v] of Object.entries(source.elements)) this.set(k,k==='manuscript'?v.files[0]:v.value);}
  }
  let failures = failStart ? 1 : 0;
  const context={document:{getElementById:node},window:node('window'),FormData:Data,
    setTimeout(fn){timers.push(fn);return timers.length;},clearTimeout(){},
    history:{replaceState(...args){history.push(args);}},
    async fetch(url, options){calls.push({url,options}); if (url==='/paper/new' && failures-- > 0) throw Error('network');
      return {ok:true,async json(){return url==='/paper/new'?{key:'AIRR-'+'a'.repeat(43),draft_url:'/paper/draft/'+'b'.repeat(32)}:{saved:true};}};}};
  vm.runInNewContext(fs.readFileSync('services/intake/static/paper-draft.js','utf8'),context);
  return {node,form,calls,timers,history};
}

test('choosing a PDF opens an empty draft on the same page without uploading the file or key', async()=>{
  const s=setup(), file={name:'paper.pdf',size:1234};
  s.form.elements.manuscript.files=[file]; await s.form.elements.manuscript.fire('change');
  assert.equal(s.calls.length,1); assert.equal(s.calls[0].url,'/paper/new');
  assert.deepEqual([...s.calls[0].options.body.keys()],['csrf_token','subject']);
  assert.equal(s.form.elements.manuscript.files[0],file);
  assert.equal(s.form.action,'/paper/draft/'+'b'.repeat(32));
  assert.equal(s.node('paper-details').hidden,false);
  assert.equal(s.node('paper-secret').value,'AIRR-'+'a'.repeat(43));
  assert.equal(s.history[0][2],s.form.action);
  s.form.elements.title.value='An edited title'; await s.form.fire('input',{target:{type:'text'}}); await s.timers.at(-1)();
  const saved=s.calls[1]; assert.equal(saved.url,s.form.action); assert.equal(saved.options.body.has('manuscript'),false);
  assert.equal([...saved.options.body.values()].includes(s.node('paper-secret').value),false);
});

test('changing the selected file keeps the same paper and key', async()=>{
  const s=setup(); s.form.elements.manuscript.files=[{name:'one.pdf',size:12}]; await s.form.elements.manuscript.fire('change');
  const replacement={name:'two.pdf',size:18}; s.form.elements.manuscript.files=[replacement]; await s.form.elements.manuscript.fire('change');
  assert.equal(s.calls.length,1); assert.equal(s.form.elements.manuscript.files[0],replacement);
});

test('a failed start keeps the selected PDF and offers a retry', async()=>{
  const s=setup({failStart:true}),file={name:'paper.pdf',size:123}; s.form.elements.manuscript.files=[file];
  await s.form.elements.manuscript.fire('change'); assert.equal(s.node('retry-paper-start').hidden,false);
  assert.equal(s.form.elements.manuscript.files[0],file); assert.equal(s.node('paper-details').hidden,true);
  await s.node('retry-paper-start').fire('click'); assert.equal(s.node('paper-details').hidden,false);
  assert.equal(s.form.elements.manuscript.files[0],file);
});

test('unsupported and oversized selections do not create drafts', async()=>{
  for(const file of [{name:'paper.docx',size:10},{name:'huge.pdf',size:26*1024*1024}]){
    const s=setup(); s.form.elements.manuscript.files=[file]; await s.form.elements.manuscript.fire('change');
    assert.equal(s.calls.length,0); assert.ok(s.form.elements.manuscript.validationMessage);
  }
});

test('save-for-later cannot discard an unconfirmed new paper key',async()=>{
  const s=setup(); s.form.elements.manuscript.files=[{name:'paper.pdf',size:12}]; await s.form.elements.manuscript.fire('change');
  let prevented=false; await s.form.fire('submit',{preventDefault(){prevented=true;},submitter:{value:'save'}});
  assert.equal(prevented,true);
  s.form.elements.key_saved.checked=true; prevented=false;
  await s.form.fire('submit',{preventDefault(){prevented=true;},submitter:{value:'save'}}); assert.equal(prevented,false);
  assert.equal(s.form.elements.manuscript.disabled,true, 'saving for later does not transfer the PDF');
});
