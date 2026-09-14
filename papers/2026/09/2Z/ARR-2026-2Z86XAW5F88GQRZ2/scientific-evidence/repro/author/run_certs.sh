for m in 3 4 5 6 7 8 9; do for z in 0 1 2 3; do d=$((m+z+3)); if [ $d -le 12 ]; then python certs.py $m $z; fi; done; done
