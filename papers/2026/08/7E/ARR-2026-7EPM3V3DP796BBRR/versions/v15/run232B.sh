#!/bin/sh
set -u
export GOOGLE_APPLICATION_CREDENTIALS=/mnt/c/Users/lluis/AppData/Roaming/gcloud/application_default_credentials.json
OUT=/mnt/d/Entregas/the-eriksson-programme/2026-11-10_manuscript232/attempt-b
CLI=/home/lluis/.local/bin/colab
CFG=/home/lluis/.config/colab-cli/tep232-b-sessions.json
mkdir -p "$OUT"
record_exit() { case "$2" in ''|*[!0-9]*) exit 92;; esac; printf '%s\n' "$2" > "$OUT/$1.tmp"; mv "$OUT/$1.tmp" "$OUT/$1"; }
date -u +%FT%TZ > "$OUT/runtime232-open-requested.txt"
"$CLI" --auth adc --config "$CFG" new -s tep232-b-own-cpu --high-mem > "$OUT/allocation232.log" 2>&1
allocation=$?
record_exit allocation232.exit "$allocation"
if [ "$allocation" -ne 0 ]; then cat "$OUT/allocation232.log"; exit "$allocation"; fi
"$CLI" --auth adc --config "$CFG" exec -s tep232-b-own-cpu -f /mnt/c/Trabajo/the-eriksson-programme/perron-spec-210-20261108/_tmp/render232B.py --timeout 1200 > "$OUT/execution232.log" 2>&1
execution=$?
record_exit execution232.exit "$execution"
"$CLI" --auth adc --config "$CFG" download -s tep232-b-own-cpu /content/tep232B-review.zip "$OUT/tep232B-review.zip" > "$OUT/download232.log" 2>&1
download=$?
record_exit download232.exit "$download"
"$CLI" --auth adc --config "$CFG" stop -s tep232-b-own-cpu > "$OUT/release232.log" 2>&1
release=$?
record_exit release232.exit "$release"
date -u +%FT%TZ > "$OUT/runtime232-release-finished.txt"
printf 'ALLOCATION=%s EXECUTION=%s DOWNLOAD=%s RELEASE=%s\n' "$allocation" "$execution" "$download" "$release"
if [ "$execution" -ne 0 ] || [ "$download" -ne 0 ] || [ "$release" -ne 0 ]; then exit 1; fi
