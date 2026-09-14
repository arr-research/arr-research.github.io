#!/bin/bash
# Fast reruns for the manuscript (run from repro/). Writes logs/*.log and logs/timings.txt.
cd "$(dirname "$0")"; LOG="$(pwd)/logs"; mkdir -p "$LOG"; : > "$LOG/timings.txt"
run() { local name=$1; shift; local t0=$(date +%s); "$@" > "$LOG/$name.log" 2>&1; local rc=$?; echo "$name  $(( $(date +%s) - t0 )) s  rc=$rc" >> "$LOG/timings.txt"; }
export PYTHONIOENCODING=utf-8
cd author
run s1_exact_simplex_spectra          python s1_exact_simplex_spectra.py 400
run s2_zonal_integral_identity        python s2_zonal_integral_identity.py 40
run s4int_bipyramid_test              python s4int_d3_exact_certificate.py
run s4int_certificate_B               python s4int_d3_exact_certificate.py s6_refined_B_exact_den100000000.json 600
run s6_tie_refine_B                   python s6_tie_refine_mp.py s3_best_seed0.json 4,8,9,12,16 s6_refined_B_rerun.json
run s5_rationalise_and_certify_B      python s5_rationalise_and_certify.py s6_refined_B_rerun.json 600 100000000
run s7_rank_and_identify_B            python s7_identify_and_rank.py s6_refined_B.json 4,8,9,12,16
run s6_tie_refine_A                   python s6_tie_refine_mp.py s3_best_seed2.json 5,6,8,12,18 s6_refined_A_rerun.json
cd ../reviewer
run r1_exact                          python r1_exact.py
run r3_exactframe                     python r3_exactframe.py
run r5_kkt                            python r5_kkt.py
run r2_lemmaT                         python r2_lemmaT.py
run r2b_lemmaT                        python r2b_lemmaT.py
cd ..
python - <<'PY' >> "$LOG/timings.txt"
import json
a=json.load(open('author/s6_refined_B_exact_den100000000.json')); b=json.load(open('author/s6_refined_B_rerun_exact_den100000000.json'))
print('rerun exact spec identical to original:', a['n123']==b['n123'] and a['w']==b['w'])
PY
echo DONE >> "$LOG/timings.txt"
