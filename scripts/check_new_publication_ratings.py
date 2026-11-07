# SPDX-License-Identifier: AGPL-3.0-or-later
"""Require real exact-PDF numerical assessments for newly added public versions."""
import argparse
import json
import re
import subprocess

from arrlib import ROOT, discover_papers, select_paper
from assessmentlib import assessments_for, load_assessment_registry, validate_assessment


def publication_rating_errors(papers, reports):
    errors = []
    for paper in papers:
        valid = [r for r in assessments_for(reports, paper)
                 if not validate_assessment(r, [paper])]
        if not valid:
            errors.append(f'{paper.id} {paper.version}: new public versions require a genuine '
                          'numerical exact-PDF assessment with overall and five criterion stars; '
                          'a qualitative report or predecessor score does not satisfy this gate.')
    return errors


def added_metadata(base, root=ROOT):
    if not re.fullmatch(r'[0-9a-f]{40}', base):
        raise ValueError('Publication comparison requires a complete Git commit SHA.')
    if base == '0' * 40:
        command = ['git', 'ls-files', '-z', '--', 'papers/**/metadata.json']
    else:
        command = ['git', 'diff', '--name-only', '-z', '--diff-filter=AM', base,
                   'HEAD', '--', 'papers/**/metadata.json']
    raw = subprocess.check_output(command, cwd=root).decode('utf-8')
    candidates = [p for p in raw.split('\0') if p]
    changed = set()
    for path in candidates:
        current = json.loads((root / path).read_text(encoding='utf-8'))
        old = subprocess.run(['git', 'show', f'{base}:{path}'], cwd=root,
                             capture_output=True, check=False)
        if old.returncode:
            changed.add((root / path).resolve())
            continue
        previous = json.loads(old.stdout)
        def identity(metadata):
            integrity = metadata.get('integrity', {})
            return (metadata.get('id'), metadata.get('version'), metadata.get('version_id'),
                    integrity.get('canonical_sha256'), integrity.get('pdf_sha256'))
        if identity(current) != identity(previous):
            changed.add((root / path).resolve())
    return changed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument('--base')
    scope.add_argument('--paper-id')
    parser.add_argument('--version', default='')
    args = parser.parse_args()
    all_papers = discover_papers()
    if args.paper_id:
        papers = [select_paper(all_papers, args.paper_id, args.version or None)]
    else:
        added = added_metadata(args.base)
        papers = [p for p in all_papers if (p.path / 'metadata.json').resolve() in added]
        if len(papers) != len(added):
            raise ValueError('Every added public metadata file must resolve to a discovered version.')
    errors = publication_rating_errors(papers, load_assessment_registry()['assessments'])
    for error in errors:
        print(error)
    if errors:
        return 1
    print(f'New-publication rating gate: {len(papers)} versions checked.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
