#!/usr/bin/env python3
"""Build the completed exact finite-frontier research manuscript."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "output" / "pdf" / "Exact_Rank_Transitions_through_p32_and_p53_Optimum.pdf"

NAVY = colors.HexColor("#10243E")
BLUE = colors.HexColor("#245A92")
PALE_BLUE = colors.HexColor("#EAF1F8")
PALE_GREEN = colors.HexColor("#EAF5EF")
PALE_RED = colors.HexColor("#F9ECEC")
INK = colors.HexColor("#17212B")
MUTED = colors.HexColor("#536272")
GREEN = colors.HexColor("#246B4B")
RED = colors.HexColor("#8F2F2F")
LINE = colors.HexColor("#C9D4DF")


class NoteDoc(BaseDocTemplate):
    def __init__(self, path: Path):
        super().__init__(
            str(path),
            pagesize=A4,
            leftMargin=19 * mm,
            rightMargin=19 * mm,
            topMargin=18 * mm,
            bottomMargin=18 * mm,
            title="Exact Cost-and-Rank Theorems at p=28 and p=53",
            author="Lluis Eriksson",
            subject="Exact Horn certificates for inverse Hilbert-Schmidt self-commutator optimization",
            keywords="self-commutator, Horn inequalities, Littlewood-Richardson, hive, Farkas certificate",
        )
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="body")
        self.addPageTemplates(PageTemplate(id="main", frames=[frame], onPage=self._page))

    @staticmethod
    def _page(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.45)
        canvas.line(doc.leftMargin, 13 * mm, A4[0] - doc.rightMargin, 13 * mm)
        canvas.setFont("Helvetica", 7.8)
        canvas.setFillColor(MUTED)
        canvas.drawString(doc.leftMargin, 8.5 * mm, "RESEARCH MANUSCRIPT - COMPLETE IN SCOPE - NOT PEER REVIEWED")
        canvas.drawRightString(A4[0] - doc.rightMargin, 8.5 * mm, f"Page {doc.page}")
        canvas.restoreState()


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    "TitleCustom", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=22, leading=26, textColor=NAVY, alignment=TA_LEFT, spaceAfter=7 * mm,
))
styles.add(ParagraphStyle(
    "Deck", parent=styles["Normal"], fontName="Helvetica", fontSize=11.2,
    leading=16, textColor=MUTED, spaceAfter=5 * mm,
))
styles.add(ParagraphStyle(
    "H1Custom", parent=styles["Heading1"], fontName="Helvetica-Bold",
    fontSize=16, leading=20, textColor=NAVY, spaceBefore=4 * mm, spaceAfter=2.8 * mm,
))
styles.add(ParagraphStyle(
    "H2Custom", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=11.8, leading=15, textColor=BLUE, spaceBefore=3 * mm, spaceAfter=1.8 * mm,
))
styles.add(ParagraphStyle(
    "BodyCustom", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.3,
    leading=13.6, textColor=INK, spaceAfter=2.5 * mm,
))
styles.add(ParagraphStyle(
    "SmallCustom", parent=styles["BodyText"], fontName="Helvetica", fontSize=7.8,
    leading=10.8, textColor=MUTED, spaceAfter=1.5 * mm,
))
styles.add(ParagraphStyle(
    "Equation", parent=styles["BodyText"], fontName="Courier-Bold", fontSize=9.2,
    leading=13.4, alignment=TA_CENTER, textColor=NAVY, leftIndent=4 * mm,
    rightIndent=4 * mm, spaceBefore=2.2 * mm, spaceAfter=3.2 * mm,
))
styles.add(ParagraphStyle(
    "BulletCustom", parent=styles["BodyText"], fontName="Helvetica", fontSize=9,
    leading=13, leftIndent=5 * mm, firstLineIndent=-3 * mm, bulletIndent=1 * mm,
    textColor=INK, spaceAfter=1.2 * mm,
))


def p(text: str, style: str = "BodyCustom") -> Paragraph:
    return Paragraph(text, styles[style])


def bullet(text: str) -> Paragraph:
    return Paragraph(text, styles["BulletCustom"], bulletText="-")


def box(text: str, color=BLUE, background=PALE_BLUE) -> Table:
    item = p(text)
    table = Table([[item]], colWidths=[155 * mm], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.9, color),
        ("BACKGROUND", (0, 0), (-1, -1), background),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return table


def data_table(data, widths, font_size=7.8, repeat=True):
    table = Table(data, colWidths=widths, repeatRows=1 if repeat else 0, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), font_size),
        ("LEADING", (0, 0), (-1, -1), font_size + 2.7),
        ("TEXTCOLOR", (0, 0), (-1, -1), INK),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("GRID", (0, 0), (-1, -1), 0.35, LINE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F6F8FA")]),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ]))
    return table


def build() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = NoteDoc(OUTPUT)
    story = [
        Spacer(1, 7 * mm),
        p("Exact Rank Transitions through p=32 and a Half-Integral Optimum at p=53", "TitleCustom"),
        p(
            "Inverse Hilbert-Schmidt self-commutator optimization on the ray "
            "F_(p,2p+1), with exact rational hive, dual, and Farkas certificates",
            "Deck",
        ),
        p("Lluis Eriksson", "H2Custom"),
        p("2 September 2026", "SmallCustom"),
        Spacer(1, 4 * mm),
        box(
            "STATUS. Completed manuscript. Exact costs and least attaining ranks are certified "
            "for every 4<=p<=32 on q=2p+1, proving rank transitions at p=8, 15, 27, and 28 "
            "and a cost-slope transition at p=29. An additional exact theorem at p=53 identifies "
            "a half-integral optimum and refutes the old integer candidate. No all-p theorem is claimed.",
            GREEN,
            PALE_GREEN,
        ),
        p("Abstract", "H1Custom"),
        p(
            "For the traceless Hermitian target F_(p,q)=diag(q repeated p times, -p repeated "
            "q times), let kappa(F) be one half of the least squared Hilbert-Schmidt norm of "
            "a factor C satisfying CC* - C*C = 2F, and let r_*(F) be the least rank among "
            "minimizers. On q=2p+1 we certify the complete finite frontier for 4<=p<=32. "
            "The minimum-rank excess r_*-q equals 0 on 4<=p<=7, 1 on 8<=p<=14, 2 on "
            "15<=p<=26, 3 at p=27, and 4 on 28<=p<=32. Thus p=27 and p=28 are two "
            "consecutive, rigorously separated rank transitions. Writing M_p=kappa(F_(p,2p+1))"
            "-(3p^2+2p), the exact data also prove M_p=6p-30 for 15<=p<=28 and "
            "M_p=7p-58 for 29<=p<=32, so the cost slope changes at p=29 rather than at "
            "the rank transition. Separately, kappa(F_(53,107))=8847 and r_*=115. Its "
            "optimum is half-integral; the earlier integer candidate of trace 8843 is refuted by "
            "an integral Farkas certificate. Every new assertion is replayed in exact rational arithmetic.",
        ),
        p("1. Problem and spectral reduction", "H1Custom"),
        p(
            "For a traceless Hermitian matrix F, define",
        ),
        p(
            "kappa(F) = (1/2) min { ||C||_HS^2 : CC* - C*C = 2F },    "
            "r_*(F) = min { rank(C) : C attains kappa(F) }.",
            "Equation",
        ),
        p(
            "Set P=(1/2)CC* and Q=(1/2)C*C. Then P and Q are positive and isospectral, "
            "P-Q=F, tr(P)=(1/2)||C||_HS^2=kappa(F), and rank(P)=rank(C). Conversely, "
            "positive isospectral P,Q with P-Q=F determine such a factor C by the polar "
            "construction. Thus the inverse problem is exactly a minimum-trace problem for "
            "positive isospectral matrices. At an optimum their common least eigenvalue is "
            "zero. The possible common spectra are governed by the Horn-Klyachko inequalities, "
            "equivalently by honeycombs or hives. A rank cap fixes the tail of this scaled "
            "spectrum to zero, turning both kappa and r_* into linear optimization questions "
            "over nested Horn faces [1-4].",
        ),
        PageBreak(),
        p("2. Exact finite frontier", "H1Custom"),
        p(
            "For every row below, a feasible primal spectrum and hive attain the displayed "
            "cost, an unrestricted rational dual matches it, and a second dual on the "
            "rank-at-most-(r_*-1) face has strictly larger value. The first block was the "
            "original exact frontier; the second block is the new exact closure.",
        ),
    ]

    frontier = [
        ["p", "q", "kappa", "r_*", "r_*-q", "status"],
        [4, 9, 65, 9, 0, "exact"], [5, 11, 98, 11, 0, "exact"],
        [6, 13, 137, 13, 0, "exact"], [7, 15, 182, 15, 0, "exact"],
        [8, 17, 233, 18, 1, "exact"], [9, 19, 291, 20, 1, "exact"],
        [10, 21, 355, 22, 1, "exact"], [11, 23, 425, 24, 1, "exact"],
        [12, 25, 501, 26, 1, "exact"], [13, 27, 583, 28, 1, "exact"],
        [14, 29, 671, 30, 1, "exact"], [15, 31, 765, 33, 2, "exact"],
        [16, 33, 866, 35, 2, "exact"], [17, 35, 973, 37, 2, "exact"],
        [18, 37, 1086, 39, 2, "exact"], [19, 39, 1205, 41, 2, "exact"],
        [20, 41, 1330, 43, 2, "exact"],
    ]
    story.extend([
        data_table(frontier, [13 * mm, 17 * mm, 23 * mm, 18 * mm, 20 * mm, 39 * mm]),
        Spacer(1, 3 * mm),
        p(
            "On 4<=p<=20 the certified rank excess is 0, 1, and 2 on the three indicated "
            "intervals. The continuation below is proved by newly frozen primal-dual objects, "
            "not by extrapolation.",
        ),
        PageBreak(),
        p("The new exact closure, 21<=p<=32", "H2Custom"),
        data_table([
            ["p", "q", "kappa", "r_*", "r_*-q", "rank <= r_*-1 value"],
            [21, 43, 1461, 45, 2, 1462], [22, 45, 1598, 47, 2, 1599],
            [23, 47, 1741, 49, 2, 1742], [24, 49, 1890, 51, 2, 1891],
            [25, 51, 2045, 53, 2, 2047], [26, 53, 2206, 55, 2, 2209],
            [27, 55, 2373, 58, 3, 2374], [28, 57, 2546, 61, 4, 2547],
            [29, 59, 2726, 63, 4, 2727], [30, 61, 2912, 65, 4, 2913],
            [31, 63, 3104, 67, 4, 3105], [32, 65, 3302, 69, 4, 3303],
        ], [14 * mm, 16 * mm, 25 * mm, 20 * mm, 22 * mm, 59 * mm], font_size=7.2),
        Spacer(1, 3 * mm),
        box(
            "THEOREM 2.1 (finite phase diagram). On q=2p+1 and 4<=p<=32, the exact "
            "minimum-rank excess is 0 for 4<=p<=7, 1 for 8<=p<=14, 2 for 15<=p<=26, "
            "3 for p=27, and 4 for 28<=p<=32. Hence the exact rank transitions in this "
            "range are p=8, 15, 27, and 28.",
            GREEN,
            PALE_GREEN,
        ),
        p(
            "The cost and rank transitions do not coincide. Define M_p=kappa(F_(p,2p+1))"
            "-(3p^2+2p). Exact subtraction gives M_p=6p-30 on 15<=p<=28 and "
            "M_p=7p-58 on 29<=p<=32. Thus the cost correction changes slope at p=29, "
            "one step after the consecutive rank jumps at p=27 and p=28.",
        ),
        p("Candidate state suggested by the exact spectra", "H2Custom"),
        p(
            "Every selected minimum-rank spectrum in the exact range admits a block "
            "decomposition",
        ),
        p("s_p = (2p+A_p, 2p, p+B_p, C_p, 0^(p-|C_p|)).", "Equation"),
        p(
            "At the selected parameters E_m=3*2^m+m+1, the blocks suggested "
            "explicit integer partitions A_m, B_m, and C_m. This formula reproduces the "
            "first three transition parameters and predicted the frozen p=28 spectrum before "
            "its exact certificates were constructed. The complete exact closure now proves that "
            "p=27 and p=28 are the actual consecutive rank transitions. The selected parameter "
            "p=53 remains an out-of-sample falsifier of the stronger integer-spectrum claim.",
        ),
        data_table([
            ["m", "p=E_m", "final kappa", "final r_*", "final status"],
            [0, 4, 65, 9, "exact feasible"],
            [1, 8, 233, 18, "exact feasible"],
            [2, 15, 765, 33, "exact feasible"],
            [3, 28, 2546, 61, "exact optimum"],
            [4, 53, 8847, 115, "exact; old state NO-GO"],
        ], [18 * mm, 23 * mm, 34 * mm, 32 * mm, 49 * mm], font_size=7.7),
        PageBreak(),
        p("3. Exact cost and rank at p=28", "H1Custom"),
        box(
            "THEOREM 3.1. For F_(28,57)=diag(57 repeated 28 times, -28 repeated "
            "57 times), kappa(F_(28,57))=2546. There exists an optimum of rank 61, "
            "and no optimum has smaller rank.",
            GREEN,
            PALE_GREEN,
        ),
        p("Upper certificate", "H2Custom"),
        p(
            "The common positive spectrum is recorded below in run-length notation; a^b "
            "means b repetitions of a.",
        ),
        p(
            "(84, 71, 64^2, 60^4, 58^7, 57^13, 56, 36, 32^2, 30^3, "
            "29^6, 28^16, 4, 2, 1^2, 0^24).",
            "Equation",
        ),
        p(
            "Its trace is 2546 and its rank is 61. The frozen Littlewood-Richardson "
            "tableau has 85 rows and 2,380 cells in the required skew shape, with content "
            "(85 repeated 28 times). The replay checks the complete shape, weak row order, "
            "strict column order, exact content, and every prefix lattice inequality. Hence "
            "the spectrum is Horn feasible and gives kappa<=2546 at rank 61.",
        ),
        p("Matching lower certificates", "H2Custom"),
        p(
            "An exact unrestricted hive dual has value 2546. A second exact dual on the "
            "rank-at-most-60 face has value 2547. Both use only integral or half-integral "
            "multipliers. Their supports are 3,126 and 3,210 rows. The first excludes any "
            "value below 2546; the second excludes every rank at most 60 at the optimum. "
            "Together with the LR construction, they prove Theorem 3.1.",
        ),
        p("Certificate logic", "H2Custom"),
        data_table([
            ["Object", "Exact statement", "Consequence"],
            ["LR tableau", "feasible, trace 2546, rank 61", "kappa<=2546 and r_*<=61"],
            ["unrestricted dual", "dual value 2546", "kappa>=2546"],
            ["rank-60 dual", "dual value 2547", "no optimum has rank<=60"],
        ], [38 * mm, 61 * mm, 57 * mm], font_size=7.5),
        p(
            "Combined with the exact p=27 predecessor, Theorem 2.1 establishes that p=28 is "
            "a genuine rank transition. It does not imply a formula for arbitrary p.",
            "SmallCustom",
        ),
        PageBreak(),
        p("4. Exact cost and rank at p=53", "H1Custom"),
        p(
            "THEOREM 4.1. kappa(F_(53,107))=8847, and the minimum attaining rank is 115.",
            "Equation",
        ),
        p(
            "Here F_(53,107)=diag(107 repeated 53 times, -53 repeated 107 times). "
            "Equivalently, there exists an optimum of rank 115 and none has smaller rank.",
        ),
        p("Exact upper certificate", "H2Custom"),
        p(
            "A common spectrum of dimension 160, trace 8847, and rank 115 is given in "
            "run-length notation by",
        ),
        p(
            "(159, 134, 243/2, 121, 229/2, 114^3, (221/2)^2, 110^5, "
            "217/2, 108^12, 215/2, 107^24, 106, 137/2, 123/2, 61, 115/2, "
            "57^2, 55^6, 109/2, 54^10, 107/2, 53^29, 17/2, 4, 2^2, 1^4, 0^45).",
            "Equation",
        ),
        p(
            "The frozen rational hive has 13,200 coordinates and denominator at most two. "
            "Exact replay checks all 481 boundary equalities and 38,319 hive, order, and "
            "nonnegativity inequalities; 34,589 inequalities are tight. This supplies "
            "kappa<=8847 at rank 115.",
        ),
        p("Matching lower certificates", "H2Custom"),
        p(
            "An unrestricted exact hive dual has value 8847 and support 10,837. A second "
            "exact dual on the rank-at-most-114 face has value 8848 and support 10,949. "
            "Every stored multiplier is integral or half-integral. Stationarity is checked "
            "on all 13,200 coordinates. The first dual matches the upper construction; the "
            "second proves the strict predecessor-rank gap. Therefore the least rank among "
            "all norm minimizers is exactly 115.",
        ),
        data_table([
            ["Object", "Exact statement", "Consequence"],
            ["rational hive", "trace 8847, rank 115", "kappa<=8847 and r_*<=115"],
            ["unrestricted dual", "dual value 8847", "kappa>=8847"],
            ["rank-114 dual", "dual value 8848", "no optimum has rank<=114"],
        ], [38 * mm, 61 * mm, 57 * mm], font_size=7.5),
        p("Why the old candidate state still matters", "H2Custom"),
        p(
            "The previous integer recursion predicted a different rank-115 spectrum of trace "
            "8843. Substitution leaves 13,041 free hive nodes. A 636-row integral Farkas "
            "combination cancels every free coefficient while its right side equals one, "
            "giving the contradiction 0 >= 1. Thus the old spectrum and cost prediction are "
            "false, even though the minimum-rank prediction 115 survives through a new "
            "half-integral Horn face.",
        ),
        p("Why a half-integral optimum is structurally possible", "H2Custom"),
        p(
            "The saturation theorem concerns integral boundary triples after dilation; it does "
            "not say that every vertex obtained by allowing the common spectrum itself to vary "
            "is integral. Here the optimization projects the hive cone onto one shared boundary, "
            "intersects it with positivity and a rank face, and minimizes trace. Such a projected "
            "rational polyhedron may have fractional exposed vertices. At p=53 the denominator-two "
            "primal and denominator-two matching dual identify the same exposed face, while the "
            "integral trace-8843 candidate is separated by an integral Farkas certificate. Thus "
            "half-integrality is a property of the optimum face, not a numerical artifact.",
        ),
        PageBreak(),
        p("5. Reproducibility and independent replay", "H1Custom"),
        p(
            "The discovery path and the proof replay are deliberately separated. HiGHS and "
            "SciPy were used to locate primal spectra, tableaux, active rows, and a normalized "
            "Farkas combination. The frozen proof objects are then checked by scripts that use "
            "only the Python standard library and exact Fraction arithmetic.",
        ),
        data_table([
            ["Replay", "Checks", "Result"],
            ["verify_lr_frontier_bundle.py", "original exact frontier and p=28 LR objects", "PASS"],
            ["verify_p28_exact_duals.py", "full and rank-60 dual stationarity/objectives", "PASS"],
            ["verify_exact_frontier_p21_p32.py", "12 primals and 24 duals; exact phase diagram", "PASS"],
            ["verify_p53_exact_endpoint.py", "hive plus full/rank-114 duals; 13,200 coordinates", "PASS"],
            ["verify_p53_independent.py", "independent row/index reconstruction", "PASS"],
            ["verify_p53_endpoint_nogo.py", "636 multipliers; 13,041 cancellations; RHS=1", "PASS"],
            ["python -O verifier", "optimized execution must be refused", "REFUSED"],
        ], [45 * mm, 83 * mm, 28 * mm], font_size=7.2),
        p("Canonical certificate identifiers", "H2Custom"),
        p(
            "p=28 unrestricted dual: "
            "72357c66fb80a75b5a28f221b2bc172b62dcefbbaccdc7131d5fdb257860646b",
            "SmallCustom",
        ),
        p(
            "p=28 rank-60 dual: "
            "f1333e9fd9bb73c6faf05cf763c07800d93da1b8d5e6f55b28ac0fad0ef7e0ae",
            "SmallCustom",
        ),
        p(
            "p=53 Farkas certificate: "
            "2968b7c01103fb70bc3d0c57138b098f7995584a9b13b40f684df7627204367d",
            "SmallCustom",
        ),
        p(
            "p=53 rank-115 primal: "
            "1a85bbed330ac8115c3a817ee25b0d95a6314363c1ab79c0e11dd61617ad7dfd",
            "SmallCustom",
        ),
        p(
            "p=53 unrestricted dual: "
            "a32442334b45bf11fdb00cd7e826399e19dca0fdaeb3ab95319f899f7cbb9d66",
            "SmallCustom",
        ),
        p(
            "p=53 rank-114 dual: "
            "4a1b24dffdf8a7a394a2c9395155887af75e86a82f192d86309c1bcda88d54de",
            "SmallCustom",
        ),
        p("Proof boundary", "H2Custom"),
        p(
            "The replay is conditional on the classical Horn-Klyachko theorem and its hive "
            "model. It is not a proof-assistant formalization. Independent peer review and an "
            "exhaustive priority search have not been performed. No numerical solution is used "
            "as a final proof object.",
        ),
        p("6. Consequences and remaining boundary", "H1Custom"),
        p(
            "The complete frontier establishes two consecutive rank transitions at p=27 and "
            "p=28, followed by a distinct cost-slope transition at p=29. The p=53 theorem raises the exact excess to "
            "eight: 115-107=8. More importantly, it separates three notions that the original "
            "recursion conflated. The predicted integer spectrum fails, its cost 8843 fails, "
            "but its rank 115 survives through a different half-integral optimum. A long exact "
            "fit can therefore identify a rank transition while missing the supporting Horn "
            "face and objective value.",
        ),
        box(
            "FINAL CLAIM BOUNDARY. Exact theorems: the full cost-and-rank phase diagram for "
            "4<=p<=32, including rank transitions at 8, 15, 27, 28 and the cost-slope change "
            "at 29; and kappa(F_(53,107))=8847 with r_*=115. Exact negative result: the old "
            "p=53 integer spectrum is infeasible. Open: every all-p recurrence and a "
            "classification of the optimal Horn faces between or beyond these parameters.",
            BLUE,
            PALE_BLUE,
        ),
        PageBreak(),
        p("References", "H1Custom"),
        p(
            "[1] A. Horn, Eigenvalues of sums of Hermitian matrices, Pacific Journal of "
            "Mathematics 12 (1962), 225-241. DOI: 10.2140/pjm.1962.12.225.",
            "SmallCustom",
        ),
        p(
            "[2] A. A. Klyachko, Stable bundles, representation theory and Hermitian "
            "operators, Selecta Mathematica 4 (1998), 419-445. DOI: 10.1007/s000290050037.",
            "SmallCustom",
        ),
        p(
            "[3] A. Knutson and T. Tao, The honeycomb model of GL(n) tensor products I: "
            "Proof of the saturation conjecture, Journal of the American Mathematical Society "
            "12 (1999), 1055-1090. arXiv:math/9807160.",
            "SmallCustom",
        ),
        p(
            "[4] W. Fulton, Eigenvalues, invariant factors, highest weights, and Schubert "
            "calculus, Bulletin of the American Mathematical Society 37 (2000), 209-249. "
            "DOI: 10.1090/S0273-0979-00-00865-X.",
            "SmallCustom",
        ),
        p(
            "[5] S. Fomin, W. Fulton, C.-K. Li, and Y.-T. Poon, Eigenvalues, singular "
            "values, and Littlewood-Richardson coefficients, arXiv:math/0301307.",
            "SmallCustom",
        ),
        p("Related exact result", "H2Custom"),
        p(
            "L. Eriksson, Optimal-rank onset for inverse self-commutators, "
            "ARR-2026-5QQF95VHTC9GABH8. The present manuscript does not alter that archived record.",
            "SmallCustom",
        ),
        p("Authorship, computational assistance, and conflicts", "H2Custom"),
        p(
            "Lluis Eriksson is the author and is responsible for the claims and proof "
            "boundary. Generative AI assisted corpus exploration, conjecture testing, code "
            "review, and drafting under author direction. Floating-point optimization was used "
            "only during discovery; every claim stated as exact has an exact replay. No external "
            "peer review or model evaluation is claimed. No conflict of interest is declared.",
            "SmallCustom",
        ),
        p("Scope and limitations", "H2Custom"),
        bullet("Complete in scope for the exact 4<=p<=32 phase diagram and the p=53 theorem."),
        bullet("No claim of a uniform p>=4 recurrence."),
        bullet("No classification of all minimizers or of every p=53 optimal spectrum."),
        bullet("Archive metadata and model assessments are not claims of peer review."),
    ])

    doc.build(story)
    print(OUTPUT.resolve())


if __name__ == "__main__":
    build()
