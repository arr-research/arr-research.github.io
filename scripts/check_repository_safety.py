"""Reject operational private files and interpolated workflow input in shell code.

Checks names and workflow structure, never prints file contents or secrets.
This supplements secret scanning; it cannot detect all credentials or personal data.
"""
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ENV_EXAMPLES = {'.env.example', '.env.sample', '.env.template'}
PRIVATE_NAME = re.compile(
    r'^(?:intake\.env(?:\..*)?|id_rsa|id_ed25519|'
    r'.*\.(?:sqlite3?|db)(?:-(?:wal|shm))?|.*\.(?:key|pem|p12|pfx|age))$'
)
EXPRESSION = re.compile(r'\$\{\{\s*(?:inputs\.|github\.event\.)')


def private_file(path):
    name = PurePosixPath(path).name.lower()
    if name in ENV_EXAMPLES:
        return False
    return name == '.env' or name.startswith('.env.') or bool(PRIVATE_NAME.fullmatch(name))


def shell_input_lines(contents):
    """Yield input interpolation inside YAML run scalars, not env bindings."""
    block_indent = None
    for number, line in enumerate(contents.splitlines(), 1):
        indent = len(line) - len(line.lstrip())
        stripped = line.strip()
        if block_indent is not None:
            if not stripped:
                continue
            if indent > block_indent:
                if EXPRESSION.search(line):
                    yield number
                continue
            block_indent = None
        match = re.match(r'^(?:-\s+)?run:\s*(.*)$', stripped)
        if match:
            value = match.group(1)
            if value.startswith(('|', '>')):
                block_indent = indent + (2 if stripped.startswith('- ') else 0)
            elif EXPRESSION.search(value):
                yield number


def main():
    paths = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
    problems = []
    for path in filter(None, paths):
        if private_file(path):
            problems.append(f'Operational/private file must not be tracked: {path}')
        if path.startswith('.github/workflows/') and path.endswith(('.yml', '.yaml')):
            for line in shell_input_lines((ROOT / path).read_text(encoding='utf-8')):
                problems.append(f'Bind workflow input through env, not shell source: {path}:{line}')
    if problems:
        print('\n'.join(problems), file=sys.stderr)
        return 1
    print('Public repository boundary checks passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
