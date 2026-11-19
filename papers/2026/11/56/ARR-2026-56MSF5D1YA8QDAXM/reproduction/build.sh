#!/usr/bin/env bash
set -euo pipefail
export TZ=UTC LC_ALL=C FORCE_SOURCE_DATE=1
SOURCE_DATE_EPOCH=$(git show -s --format=%ct 4184d9cf423f974101af1fa1059218c04025cc64)
export SOURCE_DATE_EPOCH
source_path='papers/stationary-weighting354/research/2026-11-18-small-support/rank-defects-and-stability.tex'
source_sha256=aec662773a7c8e53bdda3039785204ea9bc2e771ad66bf5c19aae686b975feb1
root=$(mktemp -d)
out="$root/proof"
mkdir "$out"
for n in 1 2; do
  build="$root/build$n"
  mkdir "$build"
  git show "4184d9cf423f974101af1fa1059218c04025cc64:$source_path" > "$build/manuscript.tex"
  (
    cd "$build"
    echo "$source_sha256  manuscript.tex" | sha256sum -c -
    printf '%s\n' '\pdfinfoomitdate=1\relax' '\pdftrailerid{}' '\pdfsuppressptexinfo=15\relax' '\input{manuscript.tex}' > driver.tex
    for pass in 1 2 3; do
      pdflatex -no-shell-escape -halt-on-error -interaction=nonstopmode driver.tex > "pass$pass.log" || { tail -40 "pass$pass.log"; exit 1; }
    done
    if grep -E 'There were undefined references|Citation .*undefined|Reference .*undefined|multiply defined|Rerun to get cross-references right' driver.log; then exit 2; fi
    cp driver.log "$out/build$n.log"
    sha256sum driver.pdf > "$out/build$n.sha256"
  )
done
cmp "$root/build1/driver.pdf" "$root/build2/driver.pdf"
cp "$root/build1/driver.pdf" "$out/manuscript.pdf"
pdfinfo "$out/manuscript.pdf" > "$out/pdfinfo.txt"
pdftotext -layout "$out/manuscript.pdf" "$out/text.txt"
mkdir "$out/pages"
pdftoppm -scale-to 1400 -jpeg -jpegopt quality=85 "$out/manuscript.pdf" "$out/pages/page"
printf '%s\n' '4184d9cf423f974101af1fa1059218c04025cc64' > "$out/source-commit.txt"
pdflatex --version > "$out/toolchain.txt"
dest="$PWD/rank-stability-proof.zip"
(cd "$out" && zip -q -r "$dest" .)
test "$(wc -c < "$dest")" -le 52428800
sha256sum "$dest" "$out/manuscript.pdf"
