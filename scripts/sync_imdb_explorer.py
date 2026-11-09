"""Keep the case page's embedded snapshot aligned with its aggregate data file."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def main():
    data = json.loads((ROOT / 'data/imdb-vote-floors.json').read_text())
    payload = json.dumps(data, separators=(',', ':')).replace('<', '\\u003c')
    page = ROOT / 'case-studies/imdb-catalogue.html'
    source, count = re.subn(
        r'(<script id="vote-floor-data" type="application/json">).*?(</script>)',
        lambda match: match[1] + payload + match[2],
        page.read_text(), flags=re.S,
    )
    if count != 1:
        raise ValueError('Expected one embedded IMDb snapshot')
    page.write_text(source)


if __name__ == '__main__':
    main()
