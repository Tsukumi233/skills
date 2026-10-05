"""Validate skill layout and metadata using the Python standard library."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
errors = []
skills = sorted((root / "skills").iterdir())
for skill in skills:
    if not skill.is_dir():
        errors.append(f"{skill.name}: expected a directory")
        continue
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill.name) or len(skill.name) > 64:
        errors.append(f"{skill.name}: invalid skill name")
    source = skill / "SKILL.md"
    if not source.is_file():
        errors.append(f"{skill.name}: missing SKILL.md")
        continue
    text = source.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
    if not match:
        errors.append(f"{skill.name}: missing YAML front matter")
        continue
    # Repository convention: required fields are single-line YAML scalars.
    fields = {}
    for key in ("name", "description"):
        value = re.search(rf"^{key}:\s*(.+)$", match[1], re.M)
        if not value:
            errors.append(f"{skill.name}: missing {key}")
            continue
        raw = value[1].strip()
        if raw.startswith('"'):
            try:
                raw = json.loads(raw)
            except ValueError:
                errors.append(f"{skill.name}: invalid quoted {key}")
                continue
        elif raw.startswith("'") and raw.endswith("'"):
            raw = raw[1:-1].replace("''", "'")
        if not isinstance(raw, str) or not raw.strip() or raw in ("|", ">"):
            errors.append(f"{skill.name}: {key} must be a nonempty single-line scalar")
        fields[key] = raw
    if fields.get("name") != skill.name:
        errors.append(f"{skill.name}: name must match directory")
    if not text[match.end():].strip():
        errors.append(f"{skill.name}: empty body")
if not skills:
    errors.append("No skills found")
if errors:
    raise SystemExit("\n".join(errors))
print(f"Validated {len(skills)} skill(s)")
