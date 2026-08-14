from pathlib import Path

path = Path("CONTEXT.md")
text = path.read_text(encoding="utf-8")
current = "PRD core, non-Voice asset requirements, and Voice Production retain separate canonical owners even though humans see one consolidated HTML.\n\n"
expected = "PRD core and downstream asset production retain separate canonical owners and acceptance evidence even though humans see one consolidated HTML.\n\n"
if current in text:
    text = text.replace(current, expected, 1)
elif expected in text:
    pass
else:
    raise SystemExit("CONTEXT.md: canonical ownership paragraph not found")
path.write_text(text, encoding="utf-8")
