from ruamel.yaml import YAML
from pathlib import Path
import sys

p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('contracts/openapi.yaml')
Y = YAML()
Y.preserve_quotes = True

from ruamel.yaml import YAML
from pathlib import Path
import sys

p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('contracts/openapi.yaml')
Y = YAML()
Y.preserve_quotes = True

def sanitize_path(path):
    s = path.strip('/').replace('/', '_')
    s = s.replace('{', '').replace('}', '')
    s = s.replace('-', '_')
    return s or 'root'

print(f'Loading {p}')
doc = None
with p.open(encoding='utf-8') as f:
    doc = Y.load(f)

paths = doc.get('paths', {})
count = 0
for path, ops in paths.items():
    if not isinstance(ops, dict):
        continue
    tag = None
    # derive tag from first path segment after /api/v1
    parts = path.strip('/').split('/')
    if len(parts) >= 2 and parts[0] == 'api' and parts[1] == 'v1':
        if len(parts) >= 3:
            tag = parts[2].capitalize()
    else:
        tag = parts[0].capitalize() if parts else 'Default'

    for method, op in list(ops.items()):
        if method.lower() not in ('get','post','put','delete','patch','options','head'):
            continue
        if not isinstance(op, dict):
            continue
        changed = False
        if 'operationId' not in op:
            op['operationId'] = f"{method.lower()}_{sanitize_path(path)}"
            changed = True
        if 'description' not in op:
            op['description'] = 'TODO: add description.'
            changed = True
        if 'tags' not in op:
            op['tags'] = [tag or 'Default']
            changed = True
        if changed:
            count += 1

if count:
    backup = p.with_suffix('.yaml.bak')
    print(f'Backing up original to {backup}')
    p.replace(backup)
    # write updated doc back
    with p.open('w', encoding='utf-8') as f:
        Y.dump(doc, f)
    print(f'Updated {count} operations and wrote file {p}')
else:
    print('No changes needed')
