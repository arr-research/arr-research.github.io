#!/usr/bin/env bash
set -euo pipefail
export TZ=UTC FORCE_SOURCE_DATE=1 DEBIAN_FRONTEND=noninteractive
repo=https://github.com/lluiseriksson/THE-ERIKSSON-PROGRAMME.git
rev=e5927d659a142f33a658eecc7f187657925c0090
sourcepath=papers/stationary-weighting354/research/2026-11-18-small-support/metastable-shell.tex
hash=da0a8281ef1b0dd37285138fef856c545936bc89dc389720664ecbf4f5c65cd0
work=$(mktemp -d /content/metastable-shell.XXXXXX)
cd "$work"
mkdir proof
trap 'echo "WORK=$PWD / $work"' EXIT
date -u > proof/start-utc.txt
if ! command -v pdflatex >/dev/null || ! kpsewhich lmodern.sty >/dev/null || ! command -v pdftoppm >/dev/null; then
 apt-get -qq update >proof/apt-update.log 2>&1
 apt-get -qq install -y --no-install-recommends texlive-latex-recommended lmodern poppler-utils >proof/apt-install.log 2>&1
fi
for n in 1 2; do
 git init -q "repo$n"
 git -C "repo$n" fetch -q --depth=1 --filter=blob:none "$repo" "$rev"
 test "$(git -C "repo$n" rev-parse FETCH_HEAD)" = "$rev"
 git -C "repo$n" remote add origin "$repo"
 git -C "repo$n" config remote.origin.promisor true
 git -C "repo$n" checkout FETCH_HEAD -- "$sourcepath"
 mkdir "proof/build$n"
 cp "repo$n/$sourcepath" "proof/build$n/manuscript.tex"
 (cd "proof/build$n"
 echo "$hash  manuscript.tex" | sha256sum -c -
 export SOURCE_DATE_EPOCH=$(git -C "../../repo$n" show -s --format=%ct FETCH_HEAD)
 printf '%s\n' '\pdfinfoomitdate=1\relax' '\pdftrailerid{}' '\pdfsuppressptexinfo=15\relax' '\input{manuscript.tex}' > driver.tex
 for i in 1 2 3; do pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error driver.tex > "pass$i.log" || { tail -25 "pass$i.log"; exit 1; }; done
 if grep -E 'There were undefined references|Citation .*undefined|Reference .*undefined|multiply defined|Rerun to get cross-references right' driver.log; then exit 2; fi
 sha256sum driver.pdf manuscript.tex > SHA256
 )
done
cmp proof/build1/driver.pdf proof/build2/driver.pdf
pdfinfo proof/build1/driver.pdf > proof/pdfinfo.txt
pdftotext -layout proof/build1/driver.pdf proof/text.txt
mkdir proof/pages
pdftoppm -scale-to 1250 -jpeg -jpegopt quality=83 proof/build1/driver.pdf proof/pages/page
pdflatex --version > proof/toolchain.txt
printf '%s\n' "$rev" > proof/source-commit.txt
date -u > proof/end-utc.txt
(cd proof; zip -qr /content/metastable-shell-proof.zip .)
cat proof/build1/SHA256
cat proof/pdfinfo.txt | grep -E 'Pages|File size'
sha256sum /content/metastable-shell-proof.zip
echo PRODUCTION_COMPLETE
