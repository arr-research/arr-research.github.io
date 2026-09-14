for z in 0 1 2; do for m in 3 4 5 6 7 8 9; do d=$((m+z+3)); if [ $d -le 14 ]; then python coverage_vertices.py $m $z; fi; done; done
