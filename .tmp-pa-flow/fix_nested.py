from pathlib import Path

path = Path('kits/project-document-generator/renderer/production_assets_objective.py')
text = path.read_text(encoding='utf-8')
old_open = "f'<section class=\"pa-flow\" id=\"{flow_id}\">'"
new_open = "f'<div class=\"pa-flow\" id=\"{flow_id}\">'"
old_close = "body += '</div></section>'"
new_close = "body += '</div></div>'"
if old_open not in text or old_close not in text:
    raise SystemExit('expected nested flow container markers not found')
text = text.replace(old_open, new_open, 1).replace(old_close, new_close, 1)
path.write_text(text, encoding='utf-8')
print('nested Production Assets flow container fixed')
