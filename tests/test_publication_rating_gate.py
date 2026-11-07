# SPDX-License-Identifier: AGPL-3.0-or-later
import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from arrlib import discover_papers, group_paper_versions
from assessmentlib import normalize_model_response
from check_new_publication_ratings import publication_rating_errors


class NewPublicationRatingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.paper = next(iter(group_paper_versions(discover_papers()).values()))[-1]

    def report(self):
        p = self.paper
        return normalize_model_response({
            'paper_id': p.id, 'version': p.version, 'version_id': p.metadata['version_id'],
            'canonical_sha256': p.metadata['integrity']['canonical_sha256'],
            'provider': 'Fixture Provider', 'model_id': 'Fixture model',
            'assessed_at': '2026-11-07T10:00:00+00:00', 'prompt_version': 'ARR-ASSESS-1.0',
            'independence': 'unknown', 'recommendation': 'major_revision',
            'millennium_score': 2.0, 'overall_stars': 2,
            'criteria': {n: {'stars': 2, 'basis': 'Fixture finding with an explicit evidentiary limitation.'}
                         for n in ('correctness_confidence', 'rigor', 'novelty', 'significance', 'reproducibility')},
            'summary': 'A fixture numerical assessment with substantial concerns retained instead of selecting only favourable reports.',
            'strengths': [], 'weaknesses': ['A fixture concern needs substantial correction.'],
            'potential_errors': [], 'strong_novelty_candidates': [],
            'unresolved_material_objections': ['A fixture main theorem has an unresolved material objection.']})

    def test_no_new_versions_does_not_invent_ratings_for_historical_records(self):
        self.assertEqual(publication_rating_errors([], []), [])

    def test_missing_or_qualitative_evidence_does_not_supply_stars(self):
        self.assertTrue(publication_rating_errors([self.paper], []))

    def test_low_score_and_adverse_findings_are_not_suppressed(self):
        self.assertEqual(publication_rating_errors([self.paper], [self.report()]), [])

    def test_predecessor_and_wrong_hash_cannot_cover_a_new_version(self):
        for field, bad in [('version_id', 'arr:version:predecessor'), ('canonical_sha256', 'f' * 64)]:
            report = self.report()
            report[field] = bad
            self.assertTrue(publication_rating_errors([self.paper], [report]))

    def test_transcribed_score_or_missing_criterion_is_rejected(self):
        original = self.report()
        for mutation in ('score', 'criterion'):
            report = copy.deepcopy(original)
            if mutation == 'score':
                report['millennium_score'] = 9
            else:
                del report['criteria']['novelty']
            self.assertTrue(publication_rating_errors([self.paper], [report]))
