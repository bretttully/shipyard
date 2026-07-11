#!/usr/bin/env python3
"""Convert CommonMark Markdown to Jira Atlassian Document Format JSON.

The wrapper always converts inside a dedicated virtual environment at
~/.claude/shipyard/adf. Exact converter dependencies are installed with hashes from
adf-requirements.lock, so ambient Python packages cannot silently change output.

Usage:
    python md_to_adf.py input.md > output.adf.json
    cat input.md | python md_to_adf.py > output.adf.json
    python md_to_adf.py --setup
"""
from __future__ import annotations

import argparse
import contextlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import venv

_ENV_DIR = Path.home() / '.claude/shipyard/adf'
_ENV_PYTHON = _ENV_DIR / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
_LOCK = _ENV_DIR.parent / 'adf.setup.lock'
_THIS = Path(__file__).resolve()
_REQUIREMENTS = _THIS.with_name('adf-requirements.lock')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', nargs='?', type=Path, help='Markdown file; stdin when omitted')
    parser.add_argument('--setup', action='store_true', help='provision the isolated converter environment')
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.setup:
        _ensure_env()
        print(f'md_to_adf: ADF env ready at {_ENV_DIR}', file=sys.stderr)
        return

    if Path(sys.executable).resolve() != _ENV_PYTHON.resolve():
        _ensure_env()
        os.execv(str(_ENV_PYTHON), [str(_ENV_PYTHON), str(_THIS), *sys.argv[1:]])

    from marklas import to_adf  # type: ignore[import-not-found]

    raw = args.input.read_text(encoding='utf-8') if args.input else sys.stdin.read()
    doc = to_adf(raw)
    if isinstance(doc, str):
        doc = json.loads(doc)
    _validate_adf(doc)
    json.dump(doc, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write('\n')


def _validate_adf(doc: object) -> None:
    if not isinstance(doc, dict):
        raise SystemExit('md_to_adf: converter returned non-object ADF')
    if doc.get('type') != 'doc' or doc.get('version') != 1 or not isinstance(doc.get('content'), list):
        raise SystemExit("md_to_adf: converter returned invalid top-level ADF shape")


def _ensure_env() -> None:
    if _health_ok():
        return
    if not _REQUIREMENTS.exists():
        raise SystemExit(f'md_to_adf: missing lock file: {_REQUIREMENTS}')

    _ENV_DIR.parent.mkdir(parents=True, exist_ok=True)
    with _setup_lock():
        if _health_ok():
            return
        print(f'md_to_adf: provisioning isolated env at {_ENV_DIR} …', file=sys.stderr)
        if not _ENV_PYTHON.exists():
            venv.EnvBuilder(with_pip=True, clear=False).create(_ENV_DIR)
        _run([
            str(_ENV_PYTHON), '-m', 'pip', 'install', '--disable-pip-version-check',
            '--require-hashes', '-r', str(_REQUIREMENTS),
        ])
        if not _health_ok():
            raise SystemExit('md_to_adf: setup completed but converter health check failed')
        print('md_to_adf: ADF env ready.', file=sys.stderr)


def _locked_versions() -> dict[str, str]:
    pins: dict[str, str] = {}
    for line in _REQUIREMENTS.read_text(encoding='utf-8').splitlines():
        spec = line.split()[0] if line.split() else ''
        if '==' in spec:
            name, _, version = spec.partition('==')
            pins[name] = version
    if not pins:
        raise SystemExit(f'md_to_adf: no pinned requirements found in {_REQUIREMENTS}')
    return pins


def _health_ok() -> bool:
    if not _ENV_PYTHON.exists() or not _REQUIREMENTS.exists():
        return False
    checks = '; '.join(
        f'assert m.version({name!r}) == {version!r}'
        for name, version in sorted(_locked_versions().items())
    )
    probe = (
        'import importlib.metadata as m; '
        'from marklas import to_adf; '
        f'{checks}; '
        "d=to_adf('# ok'); "
        "import json; d=json.loads(d) if isinstance(d,str) else d; "
        "assert d.get('type')=='doc' and d.get('version')==1"
    )
    return subprocess.run([str(_ENV_PYTHON), '-c', probe], capture_output=True, check=False).returncode == 0


@contextlib.contextmanager
def _setup_lock(timeout_seconds: int = 180):
    """Portable lock using atomic file creation with stale-lock recovery."""
    start = time.monotonic()
    while True:
        try:
            fd = os.open(_LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            os.write(fd, f'{os.getpid()}\n'.encode())
            os.close(fd)
            break
        except FileExistsError:
            if time.monotonic() - start > timeout_seconds:
                try:
                    age = time.time() - _LOCK.stat().st_mtime
                except FileNotFoundError:
                    continue
                if age > timeout_seconds:
                    _LOCK.unlink(missing_ok=True)
                    continue
                raise SystemExit(f'md_to_adf: timed out waiting for setup lock {_LOCK}')
            time.sleep(0.25)
    try:
        yield
    finally:
        _LOCK.unlink(missing_ok=True)


def _run(cmd: list[str]) -> None:
    try:
        subprocess.run(cmd, check=True, stdout=sys.stderr, stderr=sys.stderr)
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f'md_to_adf: setup command failed with exit {exc.returncode}') from exc


if __name__ == '__main__':
    main()
