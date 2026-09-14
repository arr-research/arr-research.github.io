#!/bin/bash
# Fast reruns for the manuscript. Runs on scratch copies so that author/ and reviewer/ stay verbatim;
# stdout of every script goes to logs/<name>.log, wall-clock times to logs/timings.txt.
set -u
cd "$(dirname "$0")"
mkdir -p logs; rm -rf logs/_work; mkdir -p logs/_work
cp -r author logs/_work/author; cp -r reviewer logs/_work/reviewer
: > logs/timings.txt
run() {  # run <dir> <logname> <command...>
  local d=$1 name=$2; shift 2
  local t0=$(date +%s)
  ( cd "logs/_work/$d" && "$@" ) > "logs/$name.log" 2>&1
  local rc=$?
  echo "$name  rc=$rc  $(( $(date +%s) - t0 )) s   ($*)" >> logs/timings.txt
}
run author   sym_reduction      python sym_reduction.py
run author   verify_lyapunov    python verify_lyapunov.py
run author   num_phi_4_5_6_10   python num_phi.py 4 5 6 10
run author   certify_neg_4_5_6  python certify_neg.py 4 5 6
run author   lemma_c_check      python lemma_c_check.py
run author   t_signchange       python t_signchange.py
run author   margins_4_10       python margins.py 4 10
run reviewer rev_sym            python rev_sym.py
run reviewer rev_fast           python rev_fast.py
run reviewer rev_num_4_5_6      python rev_num.py 4 5 6
run reviewer rev_spot           python rev_spot.py
run reviewer certify_neg_copy_4 python certify_neg_copy.py 4
rm -rf logs/_work
echo ALL DONE >> logs/timings.txt
