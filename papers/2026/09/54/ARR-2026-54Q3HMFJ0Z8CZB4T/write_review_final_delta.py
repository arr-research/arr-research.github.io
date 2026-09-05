"""Seal the final internal review against the inspected source/PDF hashes."""
from pathlib import Path
import hashlib
import json
from datetime import datetime,timezone

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PDF = HERE.parent/"pdfs/commutator.pdf"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
read = lambda name: json.loads((HERE/name).read_text(encoding="utf-8"))
source_hash = sha(HERE/"paper.md")
pdf_hash = sha(PDF)
assert source_hash == "6262600d0d33eff5045bdc97ae3ce016f9818535e11106a3b1b5adac1cfabcf6"
assert pdf_hash == "c4e21f587ecaafe4aa01e7b638e3f23b90263bfe77970a924b48625afbc52901"
independent = read("review_final_delta_check.json")
contact = read("contact_certificate.json")
primaldual = read("algorithm_certificate_replay.json")
pdf = read("review_pdf_correspondence.json")
assert independent["status"] == contact["status"] == pdf["status"] == "PASS"
assert independent["source_hashes"]["paper.md"] == source_hash
assert primaldual["status"] == "EXACT_INDEPENDENT_REPLAY_PASS"
assert pdf["source_sha256"] == source_hash and pdf["pdf_sha256"] == pdf_hash
files = [
    "paper.md","review_final_delta.md","review_final_delta_check.py","review_final_delta_check.json",
    "review_pdf_correspondence.py","review_pdf_correspondence.json","review_pdf_text.txt",
    "verify_contacts.py","contact_certificate.json","contact_midpoint.json",
    "optimal_constant_N4_d8.json","algorithm_certificate_replay.py","algorithm_certificate_replay.json",
    "independent_lr_geometry_review.py","independent_lr_geometry_review.json",
    "verify_balanced_four.py","balanced_four_certificate.json","geometry.py","horn_8.json",
    "certified_constant.py","requirements.txt","write_review_final_delta.py",
]
predecessor = ROOT/"work/arr-publish-approved/papers/2026/09/24/ARR-2026-24M24KDPZK8HDBQ9/paper.md"
result = {
    "reviewed_utc":datetime.now(timezone.utc).isoformat(),
    "status":"PASS_AFTER_RESOLVED_REPRODUCTION_CORRECTION",
    "screening_outcome":"pass",
    "record_id_public":"ARR-2026-54Q3HMFJ0Z8CZB4T",
    "intended_public_version":"v1",
    "canonical_pdf_sha256":pdf_hash,
    "canonical_pdf_bytes":PDF.stat().st_size,
    "canonical_pdf_pages":pdf["pages"],
    "manuscript_source_sha256":source_hash,
    "previous_reviewed_manuscript_sha256":"26869d8b74fc4ce32ae1ba93620235792bdfc095474f68960066e17423f2b26e",
    "review_role":"Separate internal audit agent in the producing model family",
    "independence":"involved_in_manuscript",
    "independent_human_review":False,
    "statistical_independence_claimed":False,
    "numerical_arr_assessment_round":False,
    "no_millennium_score_or_stars_assigned":True,
    "runtime_identity_note":"Use separately evidenced session runtime identity; reasoning tier is not inferred from this review.",
    "scope":{
        "complete_final_source_read":True,
        "delta_against_previous_reviewed_source_inspected":True,
        "Theorem_A_all_quantifiers_and_rationality":True,
        "Theorem_B_fixed_ambient_sharpness_and_reverse_attribution":True,
        "Theorem_C_complete_contact_set_and_strictness":True,
        "Lemma1_alpha_beta_faces_vertices_edges":True,
        "Lemma2_cut_geometry_completeness":True,
        "Lemma3_actual_and_normalized_eigenvalues":True,
        "ordered_chamber_polyhedral_continuity":True,
        "concavity_and_cellwise_contact_hulls":True,
        "midpoint_global_Horn_feasibility_and_gap":True,
        "all_dimension_extension":True,
        "reproduction_dependencies_and_actual_environment":True,
        "all_eight_pdf_pages_visually_inspected":True,
        "pdf_source_correspondence":True,
    },
    "new_executed_checks":{
        "author_contact_replay":{"status":contact["status"],"exact_Horn_checks":contact["exact_Horn_checks"]},
        "separate_LR_contact_replay":{
            "status":independent["status"],"exact_Horn_checks":independent["exact_Horn_checks"],
            "vertices":independent["vertices"],"LR_triples":independent["LR_triples"],
            "positive_vertex_count":independent["strict_positive_vertex_count"],
            "minimum_positive_slack":independent["minimum_positive_vertex_slack"],
            "cell_contact_count_histogram":independent["cell_contact_count_histogram"],
            "midpoint_gap_lower":independent["midpoint"]["gap_lower"],
        },
        "stored_primal_dual_replay":{
            "status":primaldual["status"],"certificates":primaldual["certificates_checked"],
            "Horn_checks":primaldual["full_dimension_Horn_checks"],
            "dual_terms":primaldual["dual_terms_reconstructed"],
        },
        "pdf":{
            "status":pdf["status"],"display_equations":pdf["display_equations"],
            "equation_tags":pdf["tag_sequence"],
            "extractable_prose_characters":pdf["prose_characters"],
            "prose_exact_after_documented_normalization":True,
            "independent_rerender_matches_eight_inspected_images":True,
        },
    },
    "resolved_findings":[{
        "id":"reproduction_dependency_description",
        "severity":"nonmaterial_to_mathematical_theorems_but_requires_reproduction_correction",
        "original":"Section8 said certified_constant.py uses SymPy; actual imports were NumPy/SciPy, and requirements.txt was absent.",
        "correction":"Source now describes NumPy/SciPy proposals and exact rational primal/dual acceptance; requirements.txt pins NumPy 2.5.1 and SciPy 1.18.0.",
        "resolution_verified_in_source_code_and_runtime":True,
    }],
    "unresolved_material_objections":[],
    "unresolved_nonmaterial_findings":[],
    "inherited_evidence":{
        "prior_review":"work/cycle3/commutator/independent_review.md",
        "prior_review_sha256":sha(ROOT/"work/cycle3/commutator/independent_review.md"),
        "original_89_vertex_bound_and_general_geometry":"Previously reviewed exact evidence retained; no unnecessary regeneration.",
        "Horn_primary_source_check":"Prior targeted Fulton equations8-10/Theorem1 and Knutson-Tao checks retained.",
    },
    "predecessor_dependency_reading":{
        "id":"ARR-2026-24M24KDPZK8HDBQ9","version":"v1",
        "canonical_pdf_sha256":"15b54435c01a4972af77db0277c7f99fc21afb43be3bbc56b1884b76bb53bf30",
        "local_source_sha256":sha(predecessor),
        "read_in_this_review":["Section2 including one-spike proof","Theorem3","Sections5.3 and5.4"],
        "full_predecessor_reaudited_in_this_subtask":False,
    },
    "limitations":[
        "Classical Horn sufficiency imported, not proved by finite checks.",
        "Internal same-family agent review; no human editorial signature or formal verification.",
        "No new exhaustive priority or novelty search.",
        "General O(N5) counts LPs, not overall computational complexity.",
        "Optional floating-point proposal generator was inspected but not rerun.",
        "PDF math is rasterized; complete paper.md is required alongside extracted paper.txt.",
        "No publication, remote modification or ARR numeric score was performed here.",
        "Finality applies only to the pinned source and PDF; later changes require additional review.",
    ],
    "files_sha256":{name:sha(HERE/name) for name in files},
}
(HERE/"review_final_delta.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":result["status"],"paper_id":result["record_id_public"],
                  "source_sha256":source_hash,"pdf_sha256":pdf_hash,
                  "review_md_sha256":sha(HERE/"review_final_delta.md"),
                  "review_json_sha256":sha(HERE/"review_final_delta.json")},indent=2))
