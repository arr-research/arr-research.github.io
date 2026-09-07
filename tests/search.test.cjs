// SPDX-License-Identifier: AGPL-3.0-or-later
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { normalize, makeIndex, search, excerpt, filterResults } = require('../site/search.js');

function record(id, title, rest = {}) {
  return { id, title, abstract: '', keywords: [], subjects: [], authors: [], ...rest };
}

const records = [
  record('title', 'Exact SU(2) Yang–Mills theory'),
  record('keyword', 'Unitary oracles', { keywords: ['SU(2) conjugacy class'] }),
  record('abstract', 'Lattice models', { abstract: 'SU(2) '.repeat(50) }),
  record('su3', 'Exact SU(3) Yang–Mills theory'),
  record('su20', 'Exact SU(20) Yang–Mills theory'),
  record('irrelevant', 'Bounds for two passive networks', { abstract: '2 cases of saturation' }),
];

test('scientific notation variants return the same relevance order', () => {
  const index = makeIndex(records);
  for (const query of ['SU(2)', 'su2', 'SU ( 2 )', 'SU 2', 'SU₂', '$\\mathrm{SU}\\left(2\\right)$']) {
    assert.deepEqual(search(index, query).map(hit => hit.record.id), ['title', 'keyword', 'abstract'], query);
  }
});

test('group dimensions and nearby numbers remain distinct', () => {
  const index = makeIndex(records);
  assert.deepEqual(search(index, 'SU(3)').map(hit => hit.record.id), ['su3']);
  assert.deepEqual(search(index, 'SU(20)').map(hit => hit.record.id), ['su20']);
  assert.deepEqual(search(index, '2').map(hit => hit.record.id), ['irrelevant']);
});

test('all query terms must match, including terms spread across fields', () => {
  const index = makeIndex(records);
  assert.deepEqual(search(index, 'SU(2) oracles').map(hit => hit.record.id), ['keyword']);
  assert.deepEqual(search(index, 'SU(2) passive'), []);
  assert.deepEqual(search(index, 'papers about SU(2)').map(hit => hit.record.id), ['title', 'keyword', 'abstract']);
});

test('a complete title phrase outranks scattered terms', () => {
  const index = makeIndex([
    record('scattered', 'Kernel methods for heat equations'),
    record('phrase', 'Heat kernel methods for equations'),
  ]);
  assert.equal(search(index, 'heat kernel')[0].record.id, 'phrase');
});

test('accents and case do not prevent an author match', () => {
  const index = makeIndex([record('author', 'An unrelated title', { authors: ['Lluís Eriksson'] })]);
  assert.equal(search(index, 'lluis ERIKSSON')[0].record.id, 'author');
});

test('full ARR identifiers are preferred to incidental mentions', () => {
  const id = 'ARR-2026-6WX2JF38WE87GB2M';
  const index = makeIndex([record('other', id), record(id, 'Unitary oracles')]);
  assert.equal(search(index, id)[0].record.id, id);
});

test('word prefixes work without broadening short mathematical terms', () => {
  const index = makeIndex([record('quantum', 'Quantum information'), record('prefix', 'SU(21)')]);
  assert.equal(search(index, 'quant')[0].record.id, 'quantum');
  assert.deepEqual(search(index, 'SU2'), []);
});

test('empty, punctuation-only and unmatched queries are well defined', () => {
  const index = makeIndex(records);
  for (const query of ['', '  ', '()[]$', 'unfindabletopic']) assert.deepEqual(search(index, query), []);
  assert.equal(normalize('SU(2) × SO(3)'), 'su2 so3');
});

test('abstract excerpts include a later matching sentence', () => {
  const summary = 'An introductory result. We establish SU(2) invariance. The construction is exact.';
  assert.ok(excerpt(summary, 'SU2').startsWith('… We establish SU(2) invariance.'));
});

test('relevance is independent of downloads and assessment scores', () => {
  const before = search(makeIndex(records), 'SU2').map(hit => hit.record.id);
  const changed = records.map((item, i) => ({ ...item, downloads: i * 100000, score: i * 2 }));
  assert.deepEqual(search(makeIndex(changed), 'SU2').map(hit => hit.record.id), before);
});

test('the whole index is searched, including records beyond the first page', () => {
  const many = Array.from({ length: 170 }, (_, i) => record(`paper-${i}`, 'Unrelated topic'));
  many[169] = record('last', 'A finite SU(2) Ward identity');
  assert.equal(search(makeIndex(many), 'SU(2)')[0].record.id, 'last');
});

test('subject, status and year intersect without changing scientific relevance', () => {
  const index = makeIndex([
    record('title', 'Exact SU(2) result', { subjects: ['Mathematical Physics'], status: 'accepted', date: '2026-02-01' }),
    record('abstract', 'A quantum result', { abstract: 'SU(2)', subjects: ['Mathematical physics'], status: 'archived', date: '2025-06-01' }),
    record('su3', 'Exact SU(3) result', { subjects: ['Mathematical Physics'], status: 'accepted', date: '2026-09-01' }),
  ]);
  assert.deepEqual(filterResults(index, 'SU(2)', { subject: 'mathematical physics', sort: 'relevance' }).map(x => x.record.id), ['title', 'abstract']);
  assert.deepEqual(filterResults(index, 'SU(2)', { status: 'archived', year: '2025' }).map(x => x.record.id), ['abstract']);
  assert.deepEqual(filterResults(index, 'SU(2)', { status: 'accepted', year: '2025' }), []);
  assert.deepEqual(filterResults(index, '', { subject: 'unknown subject' }), []);
});

test('browsing without a query supports stable date and title sorting', () => {
  const index = makeIndex([
    record('old', 'Zulu', { date: '2025-01-01' }),
    record('new', 'Alpha', { date: '2026-01-01' }),
  ]);
  assert.deepEqual(filterResults(index, '', { sort: 'relevance' }).map(x => x.record.id), ['new', 'old']);
  assert.deepEqual(filterResults(index, '', { sort: 'oldest' }).map(x => x.record.id), ['old', 'new']);
  assert.deepEqual(filterResults(index, '', { sort: 'title' }).map(x => x.record.id), ['new', 'old']);
});
