# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from texlib import plain_text, summary


class PlainTextTests(unittest.TestCase):
    def test_catalogue_notation_becomes_readable_unicode(self):
        cases = {
            "inertia $(m,n)$": "inertia (m,n)",
            "$\\kappa_d(F)=\\tfrac12\\min\\{\\|C\\|_{HS}^2:CC^*-C^*C=2F\\}$": "κ_d(F)=½min{‖C‖_HS²:CC*-C*C=2F}",
            "$F\\in M_d(\\mathbb C)$": "F ∈ M_d(ℂ)",
            "$1\\le k\\le m-n+1$": "1 ≤ k ≤ m-n+1",
            "$\\operatorname{cost}(L_k)$": "cost(L_k)",
            "$W_{(a,b)}$ on $\\mathbb{C}^d$": "W_(a,b) on ℂ^d",
            "$\\mathbb{CP}^{d-1}$": "ℂℙ^(d-1)",
            "$\\kappa^{2j}$ and $\\gamma_{N,d}$": "κ^(2j) and γ_(N,d)",
            "$L_q=q(q-1)/8$": "L_q=q(q-1)/8",
            "$\\frac{a+b}{2}$, $\\sqrt{n}$, $\\binom{n}{k}$": "(a+b)/2, √n, C(n,k)",
            "$m\\equiv1,2\\pmod3$": "m ≡ 1,2 (mod 3)",
            "$\\mathbb{Z}_2$ slice and $SU(2)$": "ℤ₂ slice and SU(2)",
            "cost \\$5 and 3×3-block": "cost $5 and 3×3-block",
            "Unknown $\\foo{x}$ macro": "Unknown foox macro",
        }
        for source, expected in cases.items():
            with self.subTest(source=source):
                self.assertEqual(plain_text(source), expected)

    def test_plain_text_is_unchanged_and_whitespace_is_normalised(self):
        self.assertEqual(plain_text('A < B & "C"'), 'A < B & "C"')
        self.assertEqual(plain_text("  One\n  line  "), "One line")

    def test_summary_prefers_sentence_then_word_boundaries(self):
        self.assertEqual(summary("Short abstract."), "Short abstract.")
        sentence = "First sentence is here. " + "x" * 200
        self.assertEqual(summary(sentence, limit=40), "First sentence is here.")
        words = "word " * 60
        result = summary(words, limit=50)
        self.assertTrue(result.endswith("word…"), result)
        self.assertLessEqual(len(result), 50)
        self.assertLessEqual(len(summary("y" * 300)), 160)


if __name__ == "__main__":
    unittest.main()
