#!/usr/bin/env python3
"""Small Jira REST helper for operations ACLI does not cover.

Credentials are read from environment and never passed in process arguments.
"""
from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
from pathlib import Path
import secrets
import sys
import urllib.error
import urllib.request


def config() -> tuple[str, str]:
    email = os.environ.get('ACLI_EMAIL')
    token = os.environ.get('ACLI_TOKEN')
    if not email or not token:
        raise SystemExit('jira_rest: ACLI_EMAIL and ACLI_TOKEN must be set')
    site = os.environ.get('ACLI_SITE')
    if not site:
        raise SystemExit('jira_rest: ACLI_SITE must be set, e.g. yourorg.atlassian.net')
    base = site if site.startswith('http') else f'https://{site}'
    auth = base64.b64encode(f'{email}:{token}'.encode()).decode()
    return base.rstrip('/'), f'Basic {auth}'


def request(method: str, url: str, auth: str, data: bytes | None = None, headers: dict[str, str] | None = None):
    h = {'Authorization': auth, 'Accept': 'application/json'}
    h.update(headers or {})
    req = urllib.request.Request(url, data=data, headers=h, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read()
            return resp.status, json.loads(body) if body else None
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode('utf-8', errors='replace')
        raise SystemExit(f'jira_rest: HTTP {exc.code}: {detail[:2000]}') from exc


def attach(issue: str, file: Path) -> None:
    if not file.is_file():
        raise SystemExit(f'jira_rest: attachment not found: {file}')
    base, auth = config()
    boundary = '----toolbox-' + secrets.token_hex(16)
    ctype = mimetypes.guess_type(file.name)[0] or 'application/octet-stream'
    payload = b''.join([
        f'--{boundary}\r\n'.encode(),
        f'Content-Disposition: form-data; name="file"; filename="{file.name}"\r\n'.encode(),
        f'Content-Type: {ctype}\r\n\r\n'.encode(),
        file.read_bytes(), b'\r\n', f'--{boundary}--\r\n'.encode(),
    ])
    _, result = request('POST', f'{base}/rest/api/3/issue/{issue}/attachments', auth, payload, {
        'X-Atlassian-Token': 'no-check',
        'Content-Type': f'multipart/form-data; boundary={boundary}',
    })
    if not isinstance(result, list) or not result or not any(x.get('filename') == file.name for x in result if isinstance(x, dict)):
        raise SystemExit('jira_rest: upload response did not confirm requested filename')
    print(json.dumps(result, indent=2))



def add_label(issue: str, label: str) -> None:
    base, auth = config()
    _, item = request('GET', f'{base}/rest/api/3/issue/{issue}?fields=labels', auth)
    if not isinstance(item, dict):
        raise SystemExit('jira_rest: unexpected issue response while reading labels')
    fields = item.get('fields') or {}
    labels = fields.get('labels') or []
    if not isinstance(labels, list) or not all(isinstance(x, str) for x in labels):
        raise SystemExit('jira_rest: unexpected labels shape')
    intended = labels if label in labels else [*labels, label]
    payload = json.dumps({'fields': {'labels': intended}}).encode()
    status, _ = request('PUT', f'{base}/rest/api/3/issue/{issue}', auth, payload, {'Content-Type': 'application/json'})
    if status != 204:
        raise SystemExit(f'jira_rest: expected HTTP 204, got {status}')
    print(json.dumps({'issue': issue, 'labels': intended}, indent=2))


def set_parent(issue: str, parent: str) -> None:
    base, auth = config()
    payload = json.dumps({'fields': {'parent': {'key': parent}}}).encode()
    status, _ = request('PUT', f'{base}/rest/api/3/issue/{issue}', auth, payload, {'Content-Type': 'application/json'})
    if status != 204:
        raise SystemExit(f'jira_rest: expected HTTP 204, got {status}')
    print(f'{issue} parent -> {parent}')


def create_link(blocker: str, blocked: str, link_type: str) -> None:
    """Create a dependency link where `blocker` blocks `blocked`, then verify the direction.

    Uses Jira's REST model directly, which is unambiguous: the outward issue performs the
    type's outward action, so for `Blocks` the outward issue blocks the inward issue. acli's
    `--out`/`--in` flags are empirically inverted relative to this, so they are not used here.
    """
    base, auth = config()
    payload = json.dumps({
        'type': {'name': link_type},
        'outwardIssue': {'key': blocker},
        'inwardIssue': {'key': blocked},
    }).encode()
    status, _ = request('POST', f'{base}/rest/api/3/issueLink', auth, payload, {'Content-Type': 'application/json'})
    if status not in (200, 201):
        raise SystemExit(f'jira_rest: expected HTTP 201 creating link, got {status}')
    _assert_blocks(base, auth, blocker, blocked, link_type)
    print(f'{blocker} {link_type.lower()} {blocked} (verified: {blocker} is the blocker)')


def _assert_blocks(base: str, auth: str, blocker: str, blocked: str, link_type: str) -> None:
    _, item = request('GET', f'{base}/rest/api/3/issue/{blocker}?fields=issuelinks', auth)
    links = ((item or {}).get('fields') or {}).get('issuelinks') or []
    for link in links:
        if not isinstance(link, dict) or (link.get('type') or {}).get('name') != link_type:
            continue
        if (link.get('outwardIssue') or {}).get('key') == blocked:
            return
    raise SystemExit(
        f'jira_rest: direction NOT confirmed after create — {blocker} shows no outward '
        f'{link_type} link to {blocked}. Refusing to assert the dependency; check and fix by hand.'
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest='cmd', required=True)
    a = sub.add_parser('attach')
    a.add_argument('issue')
    a.add_argument('file', type=Path)
    l = sub.add_parser('add-label')
    l.add_argument('issue')
    l.add_argument('label')
    p = sub.add_parser('set-parent')
    p.add_argument('issue')
    p.add_argument('parent')
    k = sub.add_parser('link', help='create a verified dependency link (blocker blocks blocked)')
    k.add_argument('--blocker', required=True, help='the issue that blocks')
    k.add_argument('--blocked', required=True, help='the issue that is blocked')
    k.add_argument('--type', default='Blocks')
    args = parser.parse_args()
    if args.cmd == 'attach':
        attach(args.issue, args.file)
    elif args.cmd == 'add-label':
        add_label(args.issue, args.label)
    elif args.cmd == 'set-parent':
        set_parent(args.issue, args.parent)
    else:
        create_link(args.blocker, args.blocked, args.type)


if __name__ == '__main__':
    main()
