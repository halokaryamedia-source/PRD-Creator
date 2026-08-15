from pathlib import Path

p = Path('workspace/active/the-clockwork-vault/work/asset-requirements.md')
text = p.read_text(encoding='utf-8')
start = text.index('## The Resonance Engine\n')
end = text.index('## The Broken Gallery\n', start)
section = text[start:end]
old = '04 — Enter the Workshop'
assert section.count(old) == 2, section.count(old)
section = section.replace(old, '04 — Engine Restored')
text = text[:start] + section + text[end:]
text = text.replace('Valid Placement Markers', 'Repair Markers')
p.write_text(text, encoding='utf-8')
print('scoped 04 label fix applied')
