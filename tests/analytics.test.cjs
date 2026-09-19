const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source=fs.readFileSync('site/analytics.js','utf8');

function run({saved=null, hostname='airr.science', storageError=false}={}) {
  const requests=[], elements=[], stored=[], listeners={};
  const preview={dataset:{pdfEvent:'/papers/X/versions/v1/pdf/'}, open:false, events:{},
    addEventListener(name, fn){this.events[name]=fn;}};
  function element(tag) {
    const e={tag, dataset:{}, events:{}, children:[], hidden:false,
      setAttribute(){}, addEventListener(name, fn){this.events[name]=fn;},
      appendChild(child){this.children.push(child);},
      querySelectorAll(){return this.buttons;}, click(){this.events.click?.();}};
    if(tag==='section') e.buttons=['allow','decline'].map(value=>Object.assign(element('button'),{dataset:{value}}));
    elements.push(e); return e;
  }
  const footer=element('footer'), body=element('body');
  const context={location:{hostname, search:'?email=private@example.test', hash:'#secret'},
    document:{currentScript:{dataset:{page:'/papers/'}}, body,
      createElement:element, querySelector:()=>footer,
      querySelectorAll:selector=>selector==='details[data-pdf-event]'?[preview]:[],
      addEventListener(name, fn){listeners[name]=fn;}},
    localStorage:{getItem(){if(storageError)throw Error();return JSON.stringify(saved);},
      setItem(k,v){if(storageError)throw Error();stored.push([k,JSON.parse(v)]);}},
    fetch:(url,opts)=>{requests.push({url,opts});return Promise.resolve();},Date};
  vm.runInNewContext(source,context);
  return {requests,stored,panel:elements.find(e=>e.tag==='section'),settings:footer.children[0],listeners,preview};
}
const pdfLink=label=>({closest:selector=>selector==='a[data-pdf-event]'?{dataset:{pdfEvent:label}}:null});
const sentPaths=requests=>requests.map(r=>JSON.parse(r.opts.body).path);
const saved=value=>({value,expires:Date.now()+100000});
test('no request before choice; equally available decline persists',()=>{
  const a=run();assert.equal(a.requests.length,0);assert.equal(a.panel.hidden,false);
  a.panel.buttons[1].click();assert.equal(a.requests.length,0);assert.equal(a.stored[0][1].value,'decline');
  assert.equal(run({saved:saved('decline')}).requests.length,0);
});
test('allow sends one canonical aggregate event without identifiers or credentials',()=>{
  const a=run();a.panel.buttons[0].click();a.panel.buttons[0].click();assert.equal(a.requests.length,1);
  const {url,opts}=a.requests[0];assert.equal(url,'https://submit.airr.science/api/v1/pageviews');
  assert.deepEqual(JSON.parse(opts.body),{path:'/papers/',consent:'aggregate-v1'});
  assert.equal(opts.credentials,'omit');assert.equal(opts.referrerPolicy,'no-referrer');
  assert.equal(run({saved:saved('allow')}).requests.length,1);
});
test('withdrawal is available and prevents subsequent page collection',()=>{
  const a=run({saved:saved('allow')});assert.equal(a.panel.hidden,true);
  a.settings.click();assert.equal(a.panel.hidden,false);a.panel.buttons[1].click();
  assert.equal(a.requests.length,1);assert.equal(run({saved:a.stored[0][1]}).requests.length,0);
});
test('PDF opens send their per-version label once per page load, only with consent',()=>{
  const a=run({saved:saved('allow')});
  a.listeners.click({type:'click',target:pdfLink('/papers/X/versions/v1/pdf/')});
  a.listeners.auxclick({type:'auxclick',button:1,target:pdfLink('/papers/X/versions/v1/pdf/')});
  a.preview.open=true;a.preview.events.toggle();
  a.listeners.auxclick({type:'auxclick',button:2,target:pdfLink('/papers/X/versions/v2/pdf/')});
  a.listeners.click({type:'click',target:{closest:()=>null}});
  assert.deepEqual(sentPaths(a.requests),['/papers/','/papers/X/versions/v1/pdf/']);
  const b=run({saved:saved('decline')});
  b.listeners.click({type:'click',target:pdfLink('/papers/X/versions/v1/pdf/')});
  b.preview.open=true;b.preview.events.toggle();
  assert.equal(b.requests.length,0);
  const c=run();
  c.listeners.click({type:'click',target:pdfLink('/papers/X/versions/v1/pdf/')});
  assert.equal(c.requests.length,0);
});
test('expired consent, unavailable storage and private host fail closed',()=>{
  assert.equal(run({saved:{value:'allow',expires:1}}).requests.length,0);
  const a=run({storageError:true});assert.equal(a.requests.length,0);
  a.panel.buttons[0].click();assert.equal(a.requests.length,1);
  const b=run({hostname:'submit.airr.science',saved:saved('allow')});
  assert.equal(b.requests.length,0);assert.equal(b.panel,undefined);
});
