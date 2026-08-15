from pathlib import Path

p = Path('.tmp-pa-minimal/patch.py')
text = p.read_text(encoding='utf-8')
old_a = "    style = r'''OBJECTIVE_STYLE = r'''<style id=\"production-assets-objective-style\">"
new_a = "    style = \"\"\"OBJECTIVE_STYLE = r'''<style id=\"production-assets-objective-style\">"
old_b = "</style>''' '''\n    # strip accidental outer spaces from raw construction"
new_b = "</style>'''\"\"\"\n    # strip accidental outer spaces from raw construction"
if old_a not in text or old_b not in text:
    raise SystemExit('expected quoting markers not found')
text = text.replace(old_a, new_a, 1).replace(old_b, new_b, 1)
p.write_text(text, encoding='utf-8')
print('patch quoting fixed')
