# SPDX-License-Identifier: AGPL-3.0-or-later
from __future__ import annotations

from pathlib import Path
import re
import unittest

CSS = (Path(__file__).resolve().parents[1] / "site" / "style.css").read_text(encoding="utf-8")


def palette(block: str) -> dict[str, str]:
    return dict(re.findall(r"--([a-z-]+):\s*([^;]+);", block))


def luminance(hex_colour: str) -> float:
    channels = [int(hex_colour[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(a: str, b: str) -> float:
    high, low = sorted((luminance(a), luminance(b)), reverse=True)
    return (high + 0.05) / (low + 0.05)


class ThemeTests(unittest.TestCase):
    def setUp(self):
        light_start = CSS.index(":root {")
        self.light = palette(CSS[light_start:CSS.index("\n}", light_start)])
        dark_start = CSS.index("@media (prefers-color-scheme: dark) {")
        self.dark = palette(CSS[dark_start:CSS.index("\n}", dark_start)])

    def test_both_palettes_define_the_same_colours_without_self_reference(self):
        self.assertEqual(set(self.light) - {"max"}, set(self.dark) | {"white"})
        for name, value in {**self.light, **self.dark}.items():
            self.assertNotIn(f"var(--{name})", value, name)

    def test_reading_text_meets_wcag_aa_in_both_themes(self):
        for theme in (self.light, self.dark):
            for ink in ("ink", "ink-soft", "muted", "blue", "gold", "green", "red"):
                for ground in ("paper", "surface"):
                    with self.subTest(ink=ink, ground=ground, paper=theme["paper"]):
                        self.assertGreaterEqual(contrast(theme[ink], theme[ground]), 4.5)

    def test_rules_use_palette_variables_not_fixed_dark_colours(self):
        rules = re.sub(r":root \{.*?\n\}", "", CSS, count=1, flags=re.S)
        rules = re.sub(r"@media \(prefers-color-scheme: dark\) \{.*?\n\}\n", "", rules, count=1, flags=re.S)
        self.assertEqual(sorted(set(re.findall(r"#[0-9a-fA-F]{3,8}\b", rules))), ["#fff"])

    def test_content_blocks_fill_the_column_without_fixed_width_caps(self):
        # Owner rule: no empty bands beside intros, forms or record sections.
        allowed = ("footer p", ".home-hero .lede", ".hero h1", ".author-header {")
        caps = [line.strip()[:60] for line in CSS.splitlines()
                if re.search(r"max-width: ?\d+(px|ch)", line) and not line.lstrip().startswith("@media")
                and not line.lstrip().startswith(allowed)]
        self.assertEqual(caps, [])


if __name__ == "__main__":
    unittest.main()
