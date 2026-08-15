from pathlib import Path
import json,re
R=Path('.')
P=R/'workspace/active/the-clockwork-vault'
A=P/'work/asset-requirements.md'
RR=R/'kits/project-document-generator/renderer/production_assets_objective.py'
S=P/'state/source-inventory.yaml'; Q=P/'state/requirement-register.yaml'
B=json.loads((R/'.tmp-clockwork-04-reader-first/briefs.json').read_text(encoding='utf-8'))
REMOVE={'Resonance Engine Seal Opening','Resonance Engine Restoration','Gremlin Path Collapse','Gremlin Route Swap','First Rollback Sabotage','Second Rollback Sabotage','Great Orrery Restoration','Vault Awakening Sequence'}

def setf(body,label,value):
    p=re.compile(rf'(?m)^{re.escape(label)}:.*$'); line=f'{label}: {value}'
    if p.search(body): return p.sub(line,body,count=1)
    m=re.search(r'(?m)^Flow:.*$',body)
    if m: return body[:m.end()]+'\n'+line+body[m.end():]
    return line+'\n'+body

def migrate_assets():
    t=A.read_text(encoding='utf-8').replace('#### Gremlin Wager Cue\n','#### Gallery Challenge Warning Sound\n')
    for name in REMOVE:
        t,n=re.subn(rf'(?ms)^#### {re.escape(name)}\n.*?(?=^#### |^### |^## |\Z)','',t)
        if n not in (0,1): raise SystemExit(f'duplicate {name}')
    pat=re.compile(r'(?ms)^#### (.+?)\n(.*?)(?=^#### |^### |^## |\Z)')
    out=[]; pos=0
    for m in pat.finditer(t):
        name=m.group(1).strip(); body=m.group(2)
        out.append(t[pos:m.start()])
        if name not in B: raise SystemExit(f'missing brief: {name}')
        typ,fun,brief=B[name]
        body=setf(body,'Type',typ); body=setf(body,'Function',fun)
        if brief: body=setf(body,'Asset Brief',brief)
        else: body=re.sub(r'(?m)^Asset Brief:.*\n?','',body)
        out.append(f'#### {name}\n{body}'); pos=m.end()
    out.append(t[pos:]); A.write_text(''.join(out),encoding='utf-8')

def repl_block(t,start,end,new):
    p=re.compile(rf'(?ms)^{re.escape(start)}.*?(?=^{re.escape(end)})')
    m=p.search(t)
    if not m: raise SystemExit(f'block not found: {start}')
    return t[:m.start()]+new+'\n\n'+t[m.end():]

def patch_renderer():
    t=RR.read_text(encoding='utf-8')
    t=re.sub(r'(?ms)^TYPE_PRIORITY = \{.*?^\}\n','TYPE_PRIORITY = {\n    "MODEL": 10,\n    "ITEM": 20,\n    "UI / TEXT": 30,\n    "AUDIO": 40,\n    "PARTICLE": 50,\n}\n',t,count=1)
    t=t.replace('    includes: str = ""\n    moment: str = ""','    includes: str = ""\n    function_text: str = ""\n    asset_brief: str = ""\n    moment: str = ""',1)
    t=t.replace('    includes: str\n    moment: str','    includes: str\n    function_text: str\n    asset_brief: str\n    moment: str',1)
    t=re.sub(r'(?ms)^def _default_type\(category: str\) -> str:\n.*?\n\n','''def _default_type(category: str) -> str:\n    return {\n        "3D Models": "MODEL",\n        "UI & Information": "UI / TEXT",\n        "Audio": "AUDIO",\n        "Visual Effects & Presentation": "PARTICLE",\n    }.get(category, category.upper())\n\n''',t,count=1)
    old='''                elif meta.startswith("Includes:"):\n                    entry.includes = meta.split(":", 1)[1].strip()\n                elif meta.startswith("Moment:"):'''
    new='''                elif meta.startswith("Includes:"):\n                    entry.includes = meta.split(":", 1)[1].strip()\n                elif meta.startswith("Function:"):\n                    entry.function_text = meta.split(":", 1)[1].strip()\n                elif meta.startswith("Asset Brief:"):\n                    entry.asset_brief = meta.split(":", 1)[1].strip()\n                elif meta.startswith("Moment:"):'''
    if old not in t: raise SystemExit('parse point missing')
    t=t.replace(old,new,1)
    t=t.replace('''        includes=entry.includes,\n        moment=entry.moment,''','''        includes=entry.includes,\n        function_text=entry.function_text or entry.for_text,\n        asset_brief=entry.asset_brief,\n        moment=entry.moment,''',1)
    voice_fn='''def _voice_to_item(\n    entry: voice.VoiceEntry, doc: voice.VoiceProduction, section: AssetSection | None,\n    page_id: str, flow: str, moment: str, function_text: str, order: int,\n) -> ProductionItem:\n    return ProductionItem(\n        item_id=f"{page_id}-build-{slug(entry.voice_id)}", title=f"{entry.speaker} — {entry.title}",\n        type_label="AUDIO", create_text="", used="", includes="",\n        function_text=function_text or "Story or character audio for this gameplay moment.", asset_brief="",\n        moment=moment or _plain_flow(flow) or "Gameplay Use", flow=flow, flow_order=_flow_order(section, flow),\n        sort_order=order, content=entry.performance, speaker=entry.speaker,\n        selected_voice=voice._voice_for(doc.cast, entry.speaker), duration=entry.duration, is_voice=True,\n    )'''
    t=re.sub(r'(?ms)^def _voice_to_item\(.*?\n\n(?=def _item_sort_key)',voice_fn+'\n\n',t,count=1)
    render='''def _build_item_html(item: ProductionItem) -> str:\n    exact = ""\n    if item.content:\n        if item.is_voice:\n            target = "voice-prompt-" + item.item_id.split("-build-")[-1]; head="Prompt"; label="Copy Prompt"; cls="voice-script-text"\n        else:\n            target = f"{item.item_id}-copy"; head="Player Text"; label="Copy Text"; cls="pa-content"\n        exact = ('<div class="pa-exact"><div class="pa-exact-head">'\n                 f'<span>{esc(head)}</span>{_copy_button(target,label)}</div>'\n                 f'<pre class="{cls}" id="{esc(target)}">{esc(item.content)}</pre></div>')\n    meta = '<div class="pa-build-meta-row"><b>Function</b><span>'+esc(item.function_text)+'</span></div>'\n    if item.is_voice:\n        meta += '<div class="pa-build-meta-row"><b>Voice Setup</b><span>'+esc(item.selected_voice)+' · Eleven v3</span></div>'\n        meta += '<div class="pa-build-meta-row"><b>Expected</b><span>'+esc(item.duration)+'</span></div>'\n    elif item.asset_brief:\n        meta += '<div class="pa-build-meta-row"><b>Asset Brief</b><span>'+esc(item.asset_brief)+'</span></div>'\n    cls = "pa-row pa-row-voice" if item.is_voice else "pa-build-row pa-row"\n    return (f'<article class="{cls}" id="{esc(item.item_id)}"><div class="pa-build-head">'\n            f'<span class="pa-type">{esc(item.type_label)}</span><h4>{esc(item.title)}</h4></div>'\n            f'<div class="pa-build-meta">{meta}</div>{exact}</article>')\n\ndef _moment_html(items: list[ProductionItem]) -> str:\n    grouped={}\n    for item in items: grouped.setdefault(item.moment,[]).append(item)\n    moments=sorted(grouped,key=lambda m:_moment_sort_key(m,grouped[m])); out=[]\n    for i,m in enumerate(moments,1):\n        out.append('<div class="pa-moment"><div class="pa-moment-head">'\n                   f'<span>{i:02d}</span><h3>{esc(m)}</h3></div><div class="pa-build-list">'\n                   +''.join(_build_item_html(x) for x in sorted(grouped[m],key=_item_sort_key))+'</div></div>')\n    return ''.join(out)'''
    t=re.sub(r'(?ms)^def _build_item_html\(.*?\n\n(?=def _pages_and_nav)',render+'\n\n',t,count=1)
    t=t.replace('''    voice_used = _voice_requirement_meta(requirements_path, "Used")\n    voice_moments = _voice_requirement_meta(requirements_path, "Moment")\n    voice_create = _voice_requirement_meta(requirements_path, "Create")''','''    voice_moments = _voice_requirement_meta(requirements_path, "Moment")\n    voice_function = _voice_requirement_meta(requirements_path, "For")''')
    t=t.replace('''                        flow,\n                        voice_used.get(entry.voice_id, ""),\n                        voice_moments.get(entry.voice_id, ""),\n                        voice_create.get(entry.voice_id, ""),\n                        order,''','''                        flow,\n                        voice_moments.get(entry.voice_id, ""),\n                        voice_function.get(entry.voice_id, ""),\n                        order,''',1)
    body=re.compile(r'(?ms)        body = \(\n            \'<header class="pa-shell">\'.*?\n        \)\n\n        index = len\(pages\)')
    m=body.search(t)
    if not m: raise SystemExit('body block missing')
    nb='''        body = (\n            '<header class="pa-shell"><small>Production Assets</small>'\n            f'<h2>{esc(meta.title)}</h2><strong>{i18n(meta.package_label)}</strong></header>'\n            '<div class="pa-moments">' + _moment_html(items) + '</div>'\n        )\n\n        index = len(pages)'''
    t=t[:m.start()]+nb+t[m.end():]
    css='''OBJECTIVE_STYLE = r'''<style id="production-assets-objective-style">\n.pa-shell{margin:0 0 18px}.pa-shell>small{display:block;margin-bottom:5px;color:var(--blue);font-size:.61rem;font-weight:850;letter-spacing:.09em;text-transform:uppercase}.pa-shell h2{margin:0;color:var(--navy);font-size:1.9rem;line-height:1.12}.pa-shell>strong{display:block;margin-top:5px;color:var(--amber);font-size:.68rem;letter-spacing:.06em;text-transform:uppercase}.pa-moments{display:grid;gap:22px}.pa-moment+.pa-moment{padding-top:20px;border-top:1px solid var(--line)}.pa-moment-head{display:flex;align-items:baseline;gap:9px;margin-bottom:8px}.pa-moment-head>span{color:var(--amber);font-size:.61rem;font-weight:900}.pa-moment-head h3{margin:0;color:var(--navy);font-size:1.05rem;text-transform:none}.pa-build-list{border-top:1px solid #cbd7dd}.pa-build-row,.pa-row-voice{padding:12px 10px;border-bottom:1px solid #cbd7dd;background:var(--paper);break-inside:avoid}.pa-build-head{display:flex;align-items:center;gap:9px}.pa-type{padding:3px 7px;border-radius:3px;background:var(--soft);color:var(--blue);font-size:.58rem;font-weight:900;letter-spacing:.055em;text-transform:uppercase}.pa-build-head h4{margin:0;color:var(--navy);font-size:.88rem;text-transform:none}.pa-build-meta{display:grid;gap:4px;margin-top:8px}.pa-build-meta-row{display:grid;grid-template-columns:82px minmax(0,1fr);gap:9px;color:#52616a;font-size:.72rem;line-height:1.45}.pa-build-meta-row b{color:var(--navy);font-size:.61rem;font-weight:850;text-transform:uppercase}.pa-exact{margin-top:9px}.pa-exact-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:5px}.pa-exact-head>span{color:var(--blue);font-size:.59rem;font-weight:850;text-transform:uppercase}.pa-copy-button{min-height:27px;padding:5px 8px;border:1px solid var(--navy);border-radius:3px;background:var(--navy);color:#fff;font:800 .56rem/1 var(--font);text-transform:uppercase}.pa-content,.pa-row-voice .voice-script-text{display:block!important;margin:0;padding:10px 12px;border:1px solid var(--line);border-left:3px solid var(--blue);border-radius:3px;background:#f8fafb;color:var(--navy);font:700 .76rem/1.52 var(--font);white-space:pre-wrap}.pa-row-voice .voice-script-text{border-left-color:var(--amber)}body.theme-dark .pa-build-row,body.theme-dark .pa-row-voice{background:#17262d}body.theme-dark .pa-build-meta-row{color:#c8d7dc}@media(max-width:760px){.pa-build-meta-row{grid-template-columns:1fr;gap:1px}}@media print{.pa-copy-button{display:none!important}}\n</style>'''\n'''
    t=re.sub(r"(?ms)^OBJECTIVE_STYLE = r'''<style.*?</style>'''\n",css,t,count=1)
    RR.write_text(t,encoding='utf-8')

def authority():
    s=S.read_text(encoding='utf-8')
    if 'id: SRC-017' not in s:
        s+='''\n\n  - id: SRC-017\n    type: instruction\n    role: authoritative\n    status: current\n    origin: user\n    inspection: full\n    summary: User superseded the two-part WHAT TO BUILD / WHERE IT IS USED design. Section 04 must use one universal moment-first production brief for every objective. A moment heading supplies timing/context; each resource directly explains its Function and the production information needed to create it. MODEL, ITEM, UI / TEXT, AUDIO, and standalone PARTICLE are the only primary resource types. MODEL/ITEM/PARTICLE use Function + Asset Brief; UI / TEXT uses Function + exact player copy; AUDIO dialogue uses Function + selected ElevenLabs voice, Eleven v3, expected duration, and exact prompt; non-dialogue AUDIO uses Function + Asset Brief and must explicitly say there is no spoken dialogue when relevant. Attached animation/sound/particle/state work stays inside its parent model/item. Gameplay-behavior SEQUENCE entries are not Production Assets. Section 03 Development is frozen and must not be edited by this 04 revision.\n'''
        S.write_text(s,encoding='utf-8')
    q=Q.read_text(encoding='utf-8')
    if 'id: REQ-023' not in q:
        q+='''\n\n  - id: REQ-023\n    area: production-assets\n    statement: Section 04 uses one generic reader-first, moment-first production brief for every objective. Moment headings answer when the resource is needed, so resource rows do not repeat Used/Trigger context. The only primary resource types are MODEL, ITEM, UI / TEXT, AUDIO, and standalone PARTICLE. Every resource must be a concrete thing that actually needs to be prepared. MODEL/ITEM/PARTICLE show Function plus a concise Asset Brief specific enough to start production; UI / TEXT shows Function plus exact copy-ready player text; AUDIO dialogue shows Function, selected ElevenLabs voice, Eleven v3, expected duration, and exact prompt; non-dialogue AUDIO shows Function plus Asset Brief and clearly states when there is no spoken dialogue. Animation, sound, particle, and state work belonging to a parent MODEL/ITEM remains inside that setup. Gameplay behavior and SEQUENCE entries are not Production Assets. Do not display internal document/process guidance, Used at, Create, Includes, For, Group, Speaker, separate WHAT TO BUILD / WHERE IT IS USED sections, or VoiceLab/provider labels. Section 03 Development remains unchanged.\n    provenance: [SRC-017]\n    evidence_status: approved\n    recovery_class: none\n    approval_status: not_required\n    impact: high\n'''
        Q.write_text(q,encoding='utf-8')

migrate_assets(); patch_renderer(); authority(); print('reader-first migration prepared')
