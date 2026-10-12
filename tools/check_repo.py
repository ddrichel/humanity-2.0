import json
import re
from pathlib import Path
from validate_alignment import validate_record
ROOT=Path(__file__).resolve().parents[1]
for path in ROOT.rglob("*.json"): json.loads(path.read_text())
for path in ROOT.rglob("*.md"):
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)",path.read_text()):
        if target.startswith(("https:","http:","#","mailto:")): continue
        target=target.split("#")[0]
        if target and not (path.parent/target).exists(): raise ValueError(f"Broken link: {path.relative_to(ROOT)} -> {target}")
validate_record(json.loads((ROOT/"examples/synthetic-human-alignment.json").read_text()))
print("JSON, local links and synthetic alignment example checked")
