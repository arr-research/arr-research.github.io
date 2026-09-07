// SPDX-License-Identifier: AGPL-3.0-or-later
const {test} = require('node:test');
const assert = require('node:assert/strict');
const {findSubjects} = require('../site/subjects.js');
const terms = [
  {id:'ai', label:'Artificial intelligence', path:'Natural sciences › Computing › Artificial intelligence', family:'natural', labels:{es:'inteligencia artificial'}, aliases:['AI','IA'], count:0},
  {id:'agents', label:'AI agents and multi-agent systems', path:'Natural sciences › Computing › Artificial intelligence › AI agents', family:'natural', labels:{}, aliases:['sistemas agénticos'], count:1},
  {id:'pain', label:'Pain medicine', path:'Medicine › Pain medicine', family:'health', labels:{}, aliases:[], count:0},
  {id:'history', label:'History', path:'Humanities › History', family:'humanities', labels:{es:'historia'}, aliases:[], count:0},
];
test('exact aliases rank first and AI does not match inside pain', () => {
  assert.deepEqual(findSubjects(terms,'AI').map(t=>t.id), ['ai','agents']);
});
test('Spanish, accents and multiword synonyms are searchable', () => {
  assert.equal(findSubjects(terms,'sistemas agenticos')[0].id, 'agents');
  assert.equal(findSubjects(terms,'historia')[0].id, 'history');
  assert.equal(findSubjects(terms,'inteligencia artificial')[0].id, 'ai');
});
test('family, populated-only and query combine without losing zero-paper fields by default', () => {
  assert.equal(findSubjects(terms,'').length,4);
  assert.deepEqual(findSubjects(terms,'','natural',true).map(t=>t.id), ['agents']);
  assert.deepEqual(findSubjects(terms,'AI','health'), []);
  assert.deepEqual(findSubjects(terms,'history','',true), []);
});
test('a parent query includes nested fields and unknown queries remain empty', () => {
  assert.equal(findSubjects(terms,'computing').length,2);
  assert.deepEqual(findSubjects(terms,'unlisted field'), []);
});
