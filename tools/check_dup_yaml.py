from ruamel.yaml import YAML
from ruamel.yaml.constructor import DuplicateKeyError
import sys
from pathlib import Path

p = Path(sys.argv[1]) if len(sys.argv)>1 else Path('contracts/openapi.yaml')
Y=YAML()
Y.allow_duplicate_keys=False
try:
    with p.open('r',encoding='utf-8') as f:
        Y.load(f)
    print('No duplicate keys found (ruamel.yaml).')
except DuplicateKeyError as e:
    print('DuplicateKeyError:',e)
except Exception as e:
    print('YAML parse error:',e)
