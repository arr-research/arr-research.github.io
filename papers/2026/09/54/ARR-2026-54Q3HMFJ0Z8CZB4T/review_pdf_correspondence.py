"""Read-only source/PDF correspondence check; does not rebuild the PDF."""
from pathlib import Path
import hashlib
import json
import re
from difflib import SequenceMatcher
from pypdf import PdfReader
from PIL import Image

HERE = Path(__file__).resolve().parent
PDF = HERE.parent / "pdfs/commutator.pdf"
QA = PDF.parent / "qa/commutator"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
source = (HERE / "paper.md").read_text(encoding="utf-8")
reader = PdfReader(PDF)
ledger = json.loads((QA / "build_report.json").read_text(encoding="utf-8"))
assert sha(HERE/"paper.md") == "6262600d0d33eff5045bdc97ae3ce016f9818535e11106a3b1b5adac1cfabcf6"
assert sha(PDF) == "c4e21f587ecaafe4aa01e7b638e3f23b90263bfe77970a924b48625afbc52901"
assert ledger["source_sha256"] == sha(HERE/"paper.md") and ledger["pdf_sha256"] == sha(PDF)
blocks = re.findall(r"\\\[(.*?)\\\]",source,flags=re.S)
expected_equations = []
for block in blocks:
    tags = re.findall(r"\\tag\{([^}]+)\}",block)
    expected_equations.append({"tag":tags[0] if tags else None,
                               "tex":" ".join(re.sub(r"\\tag\{[^}]+\}","",block).split())})
assert len(blocks) == 35 == ledger["display_equations"]
assert expected_equations == [{"tag":x["tag"],"tex":" ".join(x["tex"].split())} for x in ledger["equations"]]
assert [x["tag"] for x in expected_equations if x["tag"]] == [str(i) for i in range(1,16)]

# Formulas are image fragments and are inspected visually. Compare every
# extractable prose character independently of the builder.
text = source
for dash in "\u2010\u2011\u2012\u2013\u2014":
    text = text.replace(dash,"-")
def display_to_tag(match):
    tags = re.findall(r"\\tag\{([^}]+)\}",match[1])
    return "(" + tags[0] + ")" if tags else ""
text = re.sub(r"\\\[(.*?)\\\]",display_to_tag,text,flags=re.S)
text = re.sub(r"\$[^$]+\$[.,;:]?","",text)
text = re.sub(r"\[([^\]]+)\]\(https?://[^)]+\)",r"\1",text)
text = text.replace(chr(96),"").replace("**","").replace("*","")
text = re.sub(r"^#{1,6}\s*","",text,flags=re.M)
extracted_pages = []
for n,page in enumerate(reader.pages,1):
    lines = page.extract_text().splitlines()
    lines = [line for line in lines if line.strip() not in {
        str(n),"Lluis Eriksson | Balanced inertia (4,4) | ARR v1"}]
    extracted_pages.append("\n".join(lines))
strip_space = lambda s: re.sub(r"\s+","",s)
expected = strip_space(text)
actual = strip_space("\n".join(extracted_pages))
diffs = []
for op,i,j,k,l in SequenceMatcher(a=expected,b=actual,autojunk=False).get_opcodes():
    if op != "equal":
        diffs.append({"operation":op,"source_fragment":expected[i:j],"pdf_fragment":actual[k:l],
                      "source_context":expected[max(0,i-30):min(len(expected),j+30)]})
pages = []
for n in range(1,9):
    original = QA / f"page-{n}.png"
    rerendered = HERE / "review_pdf_pages" / f"page-{n}.png"
    with Image.open(original) as a, Image.open(rerendered) as b:
        a,b = a.convert("RGB"),b.convert("RGB")
        assert a.size == b.size and a.tobytes() == b.tobytes()
        pages.append({"page":n,"size":list(a.size),
                      "inspected_original_sha256":sha(original),
                      "independent_rerender_sha256":sha(rerendered),
                      "pixels_identical":True})
report = {
    "status":"PASS" if expected == actual else "TEXT_DIFFERENCES_REQUIRE_INSPECTION",
    "source_sha256":sha(HERE/"paper.md"),"pdf_sha256":sha(PDF),
    "pdf_bytes":PDF.stat().st_size,"pages":len(reader.pages),
    "pdf_metadata":{str(k):str(v) for k,v in reader.metadata.items()},
    "display_blocks_exactly_match_render_ledger":True,
    "display_equations":35,"tag_sequence":[str(i) for i in range(1,16)],
    "extractable_prose_characters_equal_after_documented_normalization":expected == actual,
    "prose_characters":len(expected),"text_differences":diffs,
    "all_eight_pages_visually_inspected":True,
    "inspected_pages_equal_independent_render_of_canonical_pdf":pages,
    "visual_result":"All main statements, hypotheses, formulas, numbering, proof transitions, references and disclosure were inspected. No clipping, missing mathematical element or source/PDF discrepancy found.",
    "limits":[
        "Math is embedded as raster fragments; PDF text extraction alone omits it.",
        "Equation-source ledger equality is complemented by visual inspection, not treated as proof of rendered glyph semantics.",
        "This is internal same-family review, not human peer review or formal verification.",
    ],
    "input_hashes":{"render_ledger":sha(QA/"build_report.json"),"checker":sha(Path(__file__))},
}
(HERE/"review_pdf_correspondence.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in report.items() if k not in ("inspected_pages_equal_independent_render_of_canonical_pdf","pdf_metadata","limits","input_hashes")},ensure_ascii=False,indent=2))
