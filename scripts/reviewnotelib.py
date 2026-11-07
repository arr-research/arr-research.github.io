# SPDX-License-Identifier: AGPL-3.0-or-later
"""Exact-PDF narrative reviews, without inventing ARR-ASSESS criterion stars."""
import hashlib
import json
import math
from datetime import datetime
from pathlib import Path


def load_review_note(paper):
    path = paper.path/'MODEL-REVIEW-CONTEXT.json'
    if not path.exists():
        return None
    if path.stat().st_size > 50000:
        raise ValueError('Narrative review metadata exceeds 50 KB.')
    note = json.loads(path.read_text(encoding='utf-8'))
    required = {'schema_version', 'version_id', 'canonical_sha256', 'provider',
                'ui_label', 'backend_identity', 'recorded_at', 'score', 'scale',
                'recommendation', 'context', 'summary', 'report_files'}
    if not isinstance(note, dict) or set(note) != required or note['schema_version'] not in {'1.0', '1.1'}:
        raise ValueError('Narrative exact-PDF review fields do not match the contract.')
    if note['version_id'] != paper.metadata['version_id'] or note['canonical_sha256'] != paper.metadata['integrity']['canonical_sha256']:
        raise ValueError('Narrative review must identify this exact version and PDF hash.')
    if note['backend_identity'] is not None:
        raise ValueError('This narrative adapter is for unexposed backend identities; do not fabricate one.')
    if note['score'] is None and note['schema_version'] != '1.1':
        raise ValueError('Qualitative reports without a numerical score require narrative format 1.1.')
    if note['score'] is not None and (type(note['score']) not in (int, float) or not math.isfinite(note['score']) or not 0 <= note['score'] <= 10):
        raise ValueError('Original AI-only score must be null or lie within 0–10.')
    for key in ('provider', 'ui_label', 'scale', 'recommendation', 'context', 'summary'):
        if not isinstance(note[key], str) or not 3 <= len(note[key].strip()) <= 4000:
            raise ValueError('Explicit original review identity, scope and context are required.')
    if datetime.fromisoformat(note['recorded_at'].replace('Z', '+00:00')).tzinfo is None:
        raise ValueError('Original review time must be offset-aware.')
    if not isinstance(note['report_files'], list) or not 2 <= len(note['report_files']) <= 16:
        raise ValueError('Original report and context files must be retained.')
    for source in note['report_files']:
        if not isinstance(source, dict) or set(source) != {'label', 'path', 'sha256'}:
            raise ValueError('Review source fields do not match the contract.')
        if not isinstance(source['label'], str) or not 3 <= len(source['label']) <= 200 or not isinstance(source['path'], str):
            raise ValueError('Explicit bounded review source label/path required.')
        target = (paper.path/source['path']).resolve()
        if not target.is_relative_to(paper.path.resolve()) or not target.is_file() or target.is_symlink():
            raise ValueError('Review source must be a retained file within this exact version.')
        if hashlib.sha256(target.read_bytes()).hexdigest() != source['sha256']:
            raise ValueError('Retained original narrative review source hash mismatch.')
    return note


def review_note_score_text(note):
    """Preserve an absent grade rather than manufacturing one for display."""
    if note['score'] is None:
        return 'No numerical score assigned by the model.'
    return f"Original AI-only score: {note['score']:g} / 10"
