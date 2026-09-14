#!/bin/bash
# Fast reruns for the manuscript (author scripts run in author/, reviewer scripts in reviewer/, exact_oq1.py in repro/);
# logs in logs/, wall-clock times in logs/timings.txt.  forms_mn.py is NOT rerun here: it overwrites the data files
# forms_m*_n*_z*.json (the computed sets S(m,n,z)); run it in a scratch copy if you want to regenerate them.
cd "$(dirname "$0")"; : > logs/timings.txt
run() { local dir=$1 name=$2; shift 2; local log="$PWD/logs/$name.log"; local t0=$(date +%s); (cd $dir && python "$@" > "$log" 2>&1); echo "$name: $(( $(date +%s) - t0 )) s  ($dir: python $*)" >> logs/timings.txt; }
run author ol_test_small ol_test.py "3,2,0;4,2,1;3,3,0;3,3,1;4,3,0" 300 1
run author ol_test_mid ol_test.py "4,4,0;5,4,0;5,3,0;6,3,1;5,5,0" 400 2
run author interlace_test interlace_test.py "4,2,0;5,2,1;4,3,0;5,3,0;5,3,1;4,4,0;5,4,0;6,4,1;5,5,0" 60 3
run author region_coverage region_coverage.py "4,2;6,2;4,3;6,3;5,4;7,4;6,5" 400 3
run author pure_chain_n2 pure_chain.py 2 6 400 1
run author pure_chain_n3 pure_chain.py 3 6 400 1
run author pure_chain_n4 pure_chain.py 4 8 300 1
run author inv_rule inv_rule.py "3,3,0;3,3,1;4,3,0;4,3,1;5,3,0;6,3,0;5,3,1;4,4,0;4,4,1;5,4,0;5,4,1;4,5,0;6,4,0;5,5,0"
run author d8_example d8_example.py
run author chain_lp chain_lp.py "3,3,0;3,3,2;4,3,0;5,3,0;6,3,0;5,3,1;4,4,0;4,4,1;5,4,0;5,4,1;4,5,0;6,4,0;5,5,0" 300 7
run author form_boxes_330 form_boxes.py 3 3 0
run author form_boxes_430 form_boxes.py 4 3 0
run author form_boxes_530 form_boxes.py 5 3 0
run author form_boxes_440 form_boxes.py 4 4 0
run author form_boxes_540 form_boxes.py 5 4 0
run author horn_boxes_d8 horn_boxes.py "3,2,0;4,2,1;3,3,0;3,3,1;4,3,0;4,4,0" 60 1
run reviewer rev_test_thm1 test_thm1.py
run reviewer rev_test_thm2AB test_thm2AB.py
run reviewer rev_test_oq1 test_oq1.py
run . exact_oq1 exact_oq1.py
echo DONE >> logs/timings.txt
