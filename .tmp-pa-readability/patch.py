from pathlib import Path
import re

ROOT = Path('.')
renderer = ROOT / 'kits/project-document-generator/renderer/production_assets_objective.py'
text = renderer.read_text(encoding='utf-8')

# Remove whole-flow copy aggregation: individual exact-copy controls are sufficient.
text, n = re.subn(
    r'\n\ndef _flow_copy_text\(.*?\n\ndef _pages_and_nav\(',
    '\n\ndef _pages_and_nav(',
    text,
    count=1,
    flags=re.S,
)
if n != 1:
    raise SystemExit('could not remove _flow_copy_text')

old_asset = '''def _asset_html(entry: AssetEntry, number: int, page_id: str) -> str:\n    copy_id = f"{page_id}-asset-copy-{number}"\n    context = (\n        f'<p class="pa-usage"><span>{i18n(bi("Trigger / Placement", "Trigger / Penempatan"))}</span>'\n        f'{esc(entry.usage)}</p>'\n        if entry.usage\n        else ""\n    )\n    content = ""\n    if entry.content:\n        content = (\n            '<div class="pa-content-head">'\n            f'<span>{i18n(bi("Developer Copy", "Developer Copy"))}</span>'\n            f'{_copy_button(copy_id, "Copy Text")}</div>'\n            f'<pre class="pa-content" id="{copy_id}">{esc(entry.content)}</pre>'\n        )\n    return (\n        '<article class="pa-card">'\n        '<div class="pa-card-head">'\n        f'<div class="pa-card-number">{number:02d}</div>'\n        '<div class="pa-card-title">'\n        f'<span class="pa-type-badge">{esc(entry.category)}</span>'\n        f'<h4>{esc(entry.title)}</h4></div></div>'\n        '<div class="pa-card-body">'\n        f'<p class="pa-requirement"><span>{i18n(bi("Implementation", "Implementasi"))}</span>'\n        f'{esc(entry.requirement)}</p>'\n        f'{context}{content}</div></article>'\n    )\n'''
new_asset = '''def _asset_html(entry: AssetEntry, number: int, page_id: str) -> str:\n    copy_id = f"{page_id}-asset-copy-{number}"\n    usage = (\n        '<div class="pa-work-row">'\n        f'<span>{i18n(bi("When / Where", "Kapan / Di Mana"))}</span>'\n        f'<p>{esc(entry.usage)}</p></div>'\n        if entry.usage\n        else ""\n    )\n    content = ""\n    if entry.content:\n        copy_label = "Player Text" if entry.category == "UI & Information" else "Copy-ready Text"\n        content = (\n            '<div class="pa-content-block">'\n            '<div class="pa-content-head">'\n            f'<span>{esc(copy_label)}</span>'\n            f'{_copy_button(copy_id, "Copy Text")}</div>'\n            f'<pre class="pa-content" id="{copy_id}">{esc(entry.content)}</pre>'\n            '</div>'\n        )\n    return (\n        '<article class="pa-card">'\n        '<div class="pa-card-head">'\n        f'<div class="pa-card-number">{number:02d}</div>'\n        '<div class="pa-card-title">'\n        f'<span class="pa-type-badge">{esc(entry.category)}</span>'\n        f'<h4>{esc(entry.title)}</h4></div></div>'\n        '<div class="pa-card-body">'\n        '<div class="pa-work-row">'\n        f'<span>{i18n(bi("What to Build", "Yang Dibuat"))}</span>'\n        f'<p>{esc(entry.requirement)}</p></div>'\n        f'{usage}{content}</div></article>'\n    )\n'''
if old_asset not in text:
    raise SystemExit('asset renderer block changed unexpectedly')
text = text.replace(old_asset, new_asset, 1)

old_note = '''            '<p class="pa-use-note">Follow the gameplay flows below. Each flow combines every implementation need '\n            'for that beat—player text, Voice, audio, visual presentation, and models. Use the Copy buttons for '\n            'exact production text.</p>'\n'''
new_note = '''            '<p class="pa-use-note">Choose the gameplay flow you are implementing. Every relevant model, player text, Voice, audio cue, and visual requirement for that beat is kept together below. Copy only the exact text or Voice prompt you need.</p>'\n'''
if old_note not in text:
    raise SystemExit('use-note block changed unexpectedly')
text = text.replace(old_note, new_note, 1)

old_flow = '''            flow_copy = _flow_copy_text(flow_title, flow_assets, flow_voices)\n            body += (\n                f'<div class="pa-flow" id="{flow_id}">'\n                '<div class="pa-flow-head"><div>'\n                f'<span>{i18n(bi("Gameplay Flow", "Flow Gameplay"))}</span>'\n                f'<h3>{esc(flow_title)}</h3></div>'\n            )\n            if flow_copy:\n                flow_copy_id = f"{flow_id}-copy"\n                body += _copy_button(flow_copy_id, "Copy Flow Text")\n            body += '</div>'\n            if flow_copy:\n                body += f'<pre class="pa-flow-copy-source" id="{flow_copy_id}">{esc(flow_copy)}</pre>'\n            body += '<div class="pa-flow-items">'\n'''
new_flow = '''            body += (\n                f'<div class="pa-flow" id="{flow_id}">'\n                '<div class="pa-flow-head"><div>'\n                f'<span>{i18n(bi("Gameplay Flow", "Flow Gameplay"))}</span>'\n                f'<h3>{esc(flow_title)}</h3></div></div>'\n                '<div class="pa-flow-items">'\n            )\n'''
if old_flow not in text:
    raise SystemExit('flow-copy block changed unexpectedly')
text = text.replace(old_flow, new_flow, 1)

# Replace the card-specific style block with a cleaner work-spec layout.
style_replacements = {
'''.pa-card-body{margin:8px 0 0 35px}\n.pa-requirement,.pa-usage{max-width:84ch;margin:0;color:var(--ink);font-size:.79rem;line-height:1.55}\n.pa-usage{margin-top:7px;color:#52616a;font-size:.74rem}\n.pa-requirement>span,.pa-usage>span{display:block;margin-bottom:2px;color:var(--muted);font-size:.57rem;font-weight:850;letter-spacing:.06em;text-transform:uppercase}\n.pa-content-head{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-top:10px}\n.pa-content-head>span{color:var(--muted);font-size:.58rem;font-weight:850;letter-spacing:.06em;text-transform:uppercase}\n.pa-content{margin:5px 0 0;padding:11px 12px;border-left:3px solid var(--blue);background:#f8fafb;color:var(--navy);font:700 .78rem/1.52 var(--font);white-space:pre-wrap;overflow-wrap:anywhere}\n''':
'''.pa-card-body{display:grid;gap:0;margin:10px 0 0 35px;border-top:1px solid var(--line)}\n.pa-work-row{display:grid;grid-template-columns:112px minmax(0,1fr);gap:14px;padding:10px 0;border-bottom:1px solid var(--line)}\n.pa-work-row>span{padding-top:1px;color:var(--muted);font-size:.57rem;font-weight:850;letter-spacing:.06em;text-transform:uppercase}\n.pa-work-row p{max-width:76ch;margin:0;color:var(--ink);font-size:.79rem;line-height:1.55}\n.pa-work-row+ .pa-work-row p{color:#52616a;font-size:.75rem}\n.pa-content-block{padding-top:10px}\n.pa-content-head{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:5px}\n.pa-content-head>span{color:var(--blue);font-size:.58rem;font-weight:850;letter-spacing:.06em;text-transform:uppercase}\n.pa-content{margin:0;padding:12px 13px;border:1px solid var(--line);border-left:3px solid var(--blue);border-radius:2px;background:#f8fafb;color:var(--navy);font:700 .8rem/1.55 var(--font);white-space:pre-wrap;overflow-wrap:anywhere}\n''',
'''.pa-flow-copy-source{display:none}\n''': '',
'''body.theme-dark .pa-context,body.theme-dark .pa-usage{color:#c8d7dc}\n''': '''body.theme-dark .pa-context,body.theme-dark .pa-work-row p{color:#c8d7dc}\n''',
'''@media(max-width:760px){\n.pa-flow-head{align-items:stretch;flex-direction:column}\n.pa-card-body{margin-left:0}\n.pa-content-head{align-items:flex-start}\n}\n''': '''@media(max-width:760px){\n.pa-flow-head{align-items:stretch;flex-direction:column}\n.pa-card-body{margin-left:0}\n.pa-work-row{grid-template-columns:1fr;gap:3px}\n.pa-content-head{align-items:flex-start}\n}\n''',
}
for old, new in style_replacements.items():
    if old not in text:
        raise SystemExit('style block changed unexpectedly: ' + old[:50])
    text = text.replace(old, new, 1)

renderer.write_text(text, encoding='utf-8')

# Record the user's refinement as current authority without creating a parallel requirement.
source_path = ROOT / 'workspace/active/the-clockwork-vault/state/source-inventory.yaml'
source = source_path.read_text(encoding='utf-8')
if 'id: SRC-010' not in source:
    source += '''\n  - id: SRC-010\n    type: instruction\n    role: authoritative\n    status: current\n    origin: user\n    inspection: full\n    summary: User refined the Production Assets developer UX: remove Copy Flow Text, keep fast gameplay-flow navigation, and make each Asset Requirement easier to scan and use. Each item should clearly separate What to Build, When/Where context when available, and exact per-item player text or Voice prompt with its own Copy action.\n'''
    source_path.write_text(source, encoding='utf-8')

req_path = ROOT / 'workspace/active/the-clockwork-vault/state/requirement-register.yaml'
req = req_path.read_text(encoding='utf-8')
old_req = '''  - id: REQ-017\n    area: production-assets\n    statement: Production Assets must be organized by gameplay flow within each objective/section, not by asset category. Each flow presents all implementation needs together; UI/player-facing strings and Voice prompts provide exact copy-ready text with Copy actions, while audio, visual/presentation, and model requirements show their implementation context/trigger in the same flow. Category names remain secondary badges. Pages provide quick-jump navigation to gameplay flows and may provide Copy Flow Text for all copy-ready content in that flow.\n    provenance: [SRC-009]\n'''
new_req = '''  - id: REQ-017\n    area: production-assets\n    statement: Production Assets must be organized by gameplay flow within each objective/section, not by asset category. Each flow presents all implementation needs together. Every Asset Requirement must be scan-friendly: show the secondary asset-type badge, a clear What to Build block, When/Where context when available, and exact per-item player-facing text or Voice prompt with its own Copy action. Pages retain quick-jump navigation between flows. Do not provide Copy Flow Text aggregation.\n    provenance: [SRC-009, SRC-010]\n'''
if old_req not in req:
    raise SystemExit('REQ-017 text changed unexpectedly')
req_path.write_text(req.replace(old_req, new_req, 1), encoding='utf-8')

print('Production Assets readability refinement applied')
