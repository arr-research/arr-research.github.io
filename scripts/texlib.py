# SPDX-License-Identifier: AGPL-3.0-or-later
"""Readable plain-text renderings of TeX-bearing titles and abstracts.

Only discovery metadata (<title>, meta descriptions, social cards, structured
data) uses these renderings. Visible abstracts and citation exports stay verbatim.
"""
from __future__ import annotations

import re

SYMBOLS = {
    "alpha": "α", "beta": "β", "gamma": "γ", "Gamma": "Γ", "delta": "δ", "Delta": "Δ",
    "epsilon": "ε", "varepsilon": "ε", "zeta": "ζ", "eta": "η", "theta": "θ", "Theta": "Θ",
    "vartheta": "ϑ", "iota": "ι", "kappa": "κ", "lambda": "λ", "Lambda": "Λ", "mu": "μ",
    "nu": "ν", "xi": "ξ", "Xi": "Ξ", "pi": "π", "Pi": "Π", "rho": "ρ", "sigma": "σ",
    "Sigma": "Σ", "tau": "τ", "upsilon": "υ", "Upsilon": "Υ", "phi": "φ", "varphi": "φ",
    "Phi": "Φ", "chi": "χ", "psi": "ψ", "Psi": "Ψ", "omega": "ω", "Omega": "Ω",
    "ell": "ℓ", "hbar": "ℏ", "infty": "∞", "partial": "∂", "nabla": "∇", "emptyset": "∅",
    "forall": "∀", "exists": "∃", "dagger": "†", "star": "⋆", "circ": "∘", "cdot": "·",
    "times": "×", "otimes": "⊗", "oplus": "⊕", "pm": "±", "mp": "∓", "setminus": "∖",
    "cup": "∪", "cap": "∩", "wedge": "∧", "vee": "∨", "sum": "∑", "prod": "∏", "int": "∫",
    "dots": "…", "ldots": "…", "cdots": "⋯", "lfloor": "⌊", "rfloor": "⌋", "lceil": "⌈",
    "rceil": "⌉", "langle": "⟨", "rangle": "⟩", "lvert": "|", "rvert": "|", "lVert": "‖",
    "rVert": "‖", "vert": "|", "Vert": "‖", "|": "‖", "{": "{", "}": "}", "%": "%", "&": "&",
    "#": "#", "_": "_", "$": "$",
}
# Relations read better with surrounding spaces: "1 ≤ k ≤ m".
RELATIONS = {
    "le": "≤", "leq": "≤", "ge": "≥", "geq": "≥", "ne": "≠", "neq": "≠", "in": "∈",
    "notin": "∉", "to": "→", "mapsto": "↦", "rightarrow": "→", "Rightarrow": "⇒",
    "iff": "⇔", "sim": "~", "simeq": "≃", "cong": "≅", "approx": "≈", "equiv": "≡",
    "subset": "⊂", "subseteq": "⊆", "supset": "⊃", "supseteq": "⊇", "perp": "⊥", "mid": "|",
    "ll": "≪", "gg": "≫", "propto": "∝",
}
FUNCTIONS = {
    "max", "min", "inf", "sup", "lim", "liminf", "limsup", "log", "ln", "exp", "deg", "dim",
    "ker", "det", "tr", "rank", "sin", "cos", "tan", "sinh", "cosh", "tanh", "gcd", "arg",
    "Re", "Im", "Pr", "hom",
}
BLACKBOARD = {"C": "ℂ", "R": "ℝ", "Z": "ℤ", "N": "ℕ", "Q": "ℚ", "P": "ℙ", "H": "ℍ", "F": "𝔽", "E": "𝔼"}
TEXT_WRAPPERS = {
    "text", "textrm", "textit", "textbf", "mathrm", "mathit", "mathbf", "mathsf", "mathtt",
    "mathcal", "mathscr", "mathfrak", "operatorname", "boldsymbol", "bm", "emph", "mbox",
    "hat", "tilde", "bar", "overline", "widehat", "widetilde", "vec", "dot", "ddot",
}
IGNORED = {
    "left", "right", "big", "Big", "bigg", "Bigg", "bigl", "bigr", "Bigl", "Bigr", "biggl",
    "biggr", "displaystyle", "textstyle", "limits", "nolimits", "!",
}
SPACES = {",", ";", ":", " ", "quad", "qquad", "enspace", "thinspace", "medspace", "thickspace"}
SUPERSCRIPT = str.maketrans("0123456789+-=()ni*", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿⁱ*")
SUBSCRIPT = str.maketrans("0123456789+-=()", "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎")
SUPERSCRIPT_SOURCE = set("0123456789+-=()ni*")
SUBSCRIPT_SOURCE = set("0123456789+-=()")
MATH = re.compile(r"(?<!\\)\$\$(.+?)(?<!\\)\$\$|(?<!\\)\$(.+?)(?<!\\)\$|\\\((.+?)\\\)", re.S)


def _argument(source: str, index: int) -> tuple[str, int]:
    """Return one TeX argument starting at index: a braced group or one token."""
    while index < len(source) and source[index] == " ":
        index += 1
    if index >= len(source):
        return "", index
    if source[index] == "{":
        depth = 0
        for position in range(index, len(source)):
            if source[position] == "{" and (position == 0 or source[position - 1] != "\\"):
                depth += 1
            elif source[position] == "}" and source[position - 1] != "\\":
                depth -= 1
                if depth == 0:
                    return source[index + 1:position], position + 1
        return source[index + 1:], len(source)
    if source[index] == "\\":
        match = re.match(r"\\([A-Za-z]+|.)", source[index:])
        return match.group(0), index + len(match.group(0))
    return source[index], index + 1


def _script(value: str, table: dict, allowed: set, marker: str) -> str:
    rendered = _math(value).strip()
    if rendered and set(rendered) <= allowed:
        return rendered.translate(table)
    if len(rendered) == 1 or (rendered.startswith("(") and rendered.endswith(")")):
        return marker + rendered
    # Letter-only subscripts stay readable (‖C‖_HS); exponents and operators need grouping.
    if marker == "_" and rendered.isalnum():
        return marker + rendered
    return f"{marker}({rendered})"


def _math(source: str) -> str:
    output: list[str] = []
    index = 0
    while index < len(source):
        char = source[index]
        if char == "\\":
            match = re.match(r"\\([A-Za-z]+|.)", source[index:])
            name = match.group(1)
            index += len(match.group(0))
            if name in {"frac", "tfrac", "dfrac", "binom", "tbinom", "dbinom"}:
                top, index = _argument(source, index)
                bottom, index = _argument(source, index)
                top, bottom = _math(top).strip(), _math(bottom).strip()
                if name.endswith("binom"):
                    output.append(f"C({top},{bottom})")
                elif (top, bottom) == ("1", "2"):
                    output.append("½")
                else:
                    wrap = lambda part: f"({part})" if re.search(r"[\s+\-=,]", part) else part
                    output.append(f"{wrap(top)}/{wrap(bottom)}")
            elif name == "sqrt":
                value, index = _argument(source, index)
                value = _math(value).strip()
                output.append(f"√{value}" if len(value) == 1 else f"√({value})")
            elif name in {"mathbb", "mathbbm", "Bbb"}:
                value, index = _argument(source, index)
                output.append("".join(BLACKBOARD.get(letter, letter) for letter in value.strip()))
            elif name == "pmod":
                value, index = _argument(source, index)
                output.append(f" (mod {_math(value).strip()})")
            elif name in {"bmod", "mod"}:
                output.append(" mod ")
            elif name in TEXT_WRAPPERS:
                value, index = _argument(source, index)
                output.append(_math(value))
            elif name in IGNORED:
                continue
            elif name in SPACES:
                output.append(" ")
            elif name == "\\":
                output.append(" ")
            elif name in RELATIONS:
                output.append(f" {RELATIONS[name]} ")
            elif name in SYMBOLS:
                output.append(SYMBOLS[name])
            elif name in FUNCTIONS:
                output.append(name)
            else:
                output.append(name)
            continue
        if char in "^_":
            value, index = _argument(source, index + 1)
            if char == "^":
                output.append(_script(value, SUPERSCRIPT, SUPERSCRIPT_SOURCE, "^"))
            else:
                output.append(_script(value, SUBSCRIPT, SUBSCRIPT_SOURCE, "_"))
            continue
        if char in "{}":
            index += 1
            continue
        output.append(" " if char == "~" else char)
        index += 1
    return "".join(output)


def plain_text(value: str) -> str:
    """Render inline TeX as readable Unicode text and normalise whitespace."""
    def replace(match: re.Match) -> str:
        return _math(next(group for group in match.groups() if group is not None))

    text = MATH.sub(replace, value)
    text = text.replace("\\$", "$").replace("\\&", "&").replace("\\%", "%")
    text = re.sub(r"\s+", " ", text).strip()
    return re.sub(r"\s+([,.;:)])", r"\1", text).replace("( ", "(")


def summary(value: str, limit: int = 160) -> str:
    """A search-snippet-length plain summary that ends on a sentence or word boundary."""
    text = plain_text(value)
    if len(text) <= limit:
        return text
    window = text[: limit - 1]
    sentence_end = max(window.rfind(". "), window.rfind("? "), window.rfind("! "))
    if sentence_end >= limit // 2:
        return window[: sentence_end + 1]
    word_end = window.rfind(" ")
    cut = window[:word_end] if word_end >= limit // 2 else window
    return cut.rstrip(" ,;:–—-(") + "…"
