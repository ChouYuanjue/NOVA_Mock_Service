#!/usr/bin/env python3
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString
from pathlib import Path
import re
import sys

p = Path(sys.argv[1]) if len(sys.argv)>1 else Path('contracts/openapi.yaml')
if not p.exists():
    print('File not found:', p)
    sys.exit(2)

bak = p.with_suffix('.yaml.autobak')
bak.write_bytes(p.read_bytes())
print('Backup written to', bak)

Y = YAML()
Y.preserve_quotes = True
Y.indent(mapping=2, sequence=4, offset=2)

doc = Y.load(p)
changed = False

# Collect tags used in operations
used_tags = set()
paths = doc.get('paths', {}) or {}
for path, ops in paths.items():
    if not isinstance(ops, dict):
        continue
    for method, op in ops.items():
        if isinstance(op, dict):
            tags = op.get('tags')
            if isinstance(tags, list):
                for t in tags:
                    if isinstance(t, str):
                        used_tags.add(t)

# Add top-level tags if missing
if used_tags:
    if 'tags' not in doc or not isinstance(doc['tags'], list):
        doc['tags'] = []
        changed = True
    existing = {t.get('name') for t in doc['tags'] if isinstance(t, dict) and 'name' in t}
    for t in sorted(used_tags):
        if t not in existing:
            doc['tags'].append({'name': t, 'description': f'Auto-generated tag for {t}'})
            changed = True

# Helper to decide if string needs quoting
date_like = re.compile(r'^\d{4}-\d{2}-\d{2}')
url_like = re.compile(r'^[a-zA-Z][a-zA-Z0-9+.-]*://')

def ensure_quoted(val):
    if not isinstance(val, str):
        return val, False
    if val.startswith('"') or val.startswith("'"):
        return val, False
    if ':' in val or ',' in val or '//' in val or url_like.match(val) or date_like.match(val):
        return DoubleQuotedScalarString(val), True
    # also quote true/false/yes/no/numeric-like
    if val.lower() in ('true','false','yes','no','on','off'):
        return DoubleQuotedScalarString(val), True
    if re.fullmatch(r'[-+]?\d+(\.\d+)?', val):
        return DoubleQuotedScalarString(val), True
    return val, False

# Walk document to find 'example' keys
def walk(node):
    global changed
    if isinstance(node, dict):
        for k,v in list(node.items()):
            if k == 'example':
                newv, did = ensure_quoted(v)
                if did:
                    node[k] = newv
                    changed = True
            else:
                walk(v)
    elif isinstance(node, list):
        for item in node:
            walk(item)

walk(doc)

if changed:
    with p.open('w', encoding='utf-8') as f:
        Y.dump(doc, f)
    print('File updated:', p)
else:
    print('No changes needed')
