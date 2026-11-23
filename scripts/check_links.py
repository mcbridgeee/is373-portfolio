"""Fail if index.html points at a local file or #anchor that doesn't exist."""
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text(encoding="utf-8")
ids = set(re.findall(r'\sid="([^"]+)"', html))
problems = []
for ref in re.findall(r'(?:href|src)="([^"]+)"', html):
    if ref.startswith(("http://", "https://", "mailto:")):
        continue
    if ref.startswith("#"):
        if ref[1:] not in ids:
            problems.append(f"missing anchor {ref}")
    elif not (root / ref).is_file():
        problems.append(f"missing file {ref}")
for p in problems:
    print(p)
print(f"checked local links: {len(problems)} problem(s)")
sys.exit(1 if problems else 0)
