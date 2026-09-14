#!/bin/bash
# Fast reruns for the manuscript (author scripts run in author/, reviewer scripts in reviewer/); logs and timings in logs/.
cd "$(dirname "$0")"; : > logs/timings.txt
run() { local dir=$1 name=$2; shift 2; local t0=$(date +%s); (cd $dir && python "$@" > ../logs/$name.log 2>&1); echo "$name: $(( $(date +%s) - t0 )) s  ($dir: python $*)" >> logs/timings.txt; }
run author verify_formula2_9_9_2000_2 verify_formula2.py 9 9 2000 2 2026
run author certs_4_1 certs.py 4 1
run author familyA_cert_12_4 familyA_cert.py 12 4
run author families2_3_9 families2.py 3 9
run author coverage_vertices_4_1 coverage_vertices.py 4 1
run author test_pred_10_1_300 test_pred.py 10 1 300
run reviewer rev_tiles_check tiles_check.py
run reviewer rev_m2_reduction m2_reduction.py
run reviewer rev_padding_check padding_check.py
run reviewer rev_chain_own_5 chain_own.py 5
run reviewer rev_pred_m11 pred_m11.py
run reviewer rev_complete_m11 complete_m11.py
run reviewer rev_exposed_m5 exposed_m5.py
echo DONE >> logs/timings.txt
