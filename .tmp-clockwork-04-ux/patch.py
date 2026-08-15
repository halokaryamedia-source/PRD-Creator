from pathlib import Path
import re

ROOT = Path('.')
PROJECT = ROOT / 'workspace/active/the-clockwork-vault'
RENDERER = ROOT / 'kits/project-document-generator/renderer/production_assets_objective.py'
ASSET = PROJECT / 'work/asset-requirements.md'
SOURCE = PROJECT / 'state/source-inventory.yaml'
REQ = PROJECT / 'state/requirement-register.yaml'


def replace_between(text: str, start_marker: str, end_marker: str, replacement: str) -> str:
    start = text.index(start_marker)
    end = text.index(end_marker, start)
    return text[:start] + replacement + text[end:]


def patch_renderer() -> None:
    text = RENDERER.read_text(encoding='utf-8')

    asset_and_voice = r'''def _asset_html(entry: AssetEntry, page_id: str) -> str:
    copy_id = f"{page_id}-asset-copy-{slug(entry.title)}"
    type_label = _category_label(entry.category, entry.title)
    actions = ""
    detail = ""
    if entry.content:
        actions = _copy_button(copy_id, "Copy Text")
        short_copy = len(entry.content) <= 320 and entry.content.count("\n") <= 7
        if short_copy:
            detail = (
                '<div class="pa-row-copy pa-row-copy-open">'
                f'<pre class="pa-content" id="{copy_id}">{esc(entry.content)}</pre>'
                '</div>'
            )
        else:
            detail = (
                '<details class="pa-row-details">'
                '<summary>View Text</summary>'
                f'<pre class="pa-content" id="{copy_id}">{esc(entry.content)}</pre>'
                '</details>'
            )
    return (
        '<article class="pa-row">'
        '<div class="pa-row-main">'
        f'<span class="pa-type">{esc(type_label)}</span>'
        '<div class="pa-row-info">'
        f'<h4>{esc(entry.title)}</h4>'
        f'<p>{esc(entry.for_text)}</p>'
        '</div>'
        f'<div class="pa-row-actions">{actions}</div>'
        '</div>'
        f'{detail}'
        '</article>'
    )


def _voice_html(
    entry: voice.VoiceEntry,
    doc: voice.VoiceProduction,
    for_text: str,
) -> str:
    prompt_id = f"voice-prompt-{slug(entry.voice_id)}"
    selected_voice = voice._voice_for(doc.cast, entry.speaker)
    return (
        '<article class="pa-row pa-row-voice">'
        '<div class="pa-row-main">'
        '<span class="pa-type pa-type-voice">VOICE</span>'
        '<div class="pa-row-info">'
        f'<h4>{esc(entry.speaker)} — {esc(entry.title)}</h4>'
        f'<p>{esc(for_text)}</p>'
        f'<small>{esc(selected_voice)} · {esc(entry.duration)}</small>'
        '</div>'
        '<div class="pa-row-actions">'
        f'<button class="voice-copy-button" data-voice-copy="{esc(prompt_id)}" type="button">'
        '<span class="voice-copy-label">Copy Prompt</span></button>'
        '</div>'
        '</div>'
        '<details class="pa-row-details pa-voice-details">'
        '<summary>View Prompt</summary>'
        f'<pre class="voice-script-text" id="{esc(prompt_id)}">{esc(entry.performance)}</pre>'
        f'<div class="voice-script-display">{voice._performance_html(entry.performance)}</div>'
        '</details>'
        '</article>'
    )


def _shared_voice_cast_html(doc: voice.VoiceProduction | None) -> str:
    if doc is None or not doc.cast:
        return ""
    rows = []
    for speaker, selected in doc.cast.items():
        rows.append(
            '<div class="pa-cast-row">'
            f'<strong>{esc(speaker)}</strong>'
            f'<span>{esc(selected)}</span>'
            '<small>Eleven v3</small>'
            '</div>'
        )
    return (
        '<div class="pa-cast">'
        '<div class="pa-cast-head"><span>Voice Cast</span><p>Shared voice assignments for all Production Assets.</p></div>'
        '<div class="pa-cast-rows">' + ''.join(rows) + '</div>'
        '</div>'
    )


'''
    text = replace_between(text, 'def _asset_html(', 'def _pages_and_nav(', asset_and_voice)

    pages_function = r'''def _pages_and_nav(
    render_data: dict[str, Any],
    assets: AssetRequirements | None,
    voice_doc: voice.VoiceProduction | None,
    triggers: dict[str, str],
    voice_flows: dict[str, str],
    voice_for: dict[str, str],
) -> tuple[str, str]:
    asset_map = {
        voice._title_key(section.title): section
        for section in (assets.sections if assets else [])
    }
    voice_map = {
        voice._title_key(section.title): section
        for section in (voice_doc.sections if voice_doc else [])
    }
    brand = render_data["document"].get("brand") or render_data["document"]["title"]
    pages: list[str] = []
    links: list[str] = []

    for title in _ordered_titles(render_data, assets, voice_doc):
        key = voice._title_key(title)
        asset_section = asset_map.get(key)
        voice_section = voice_map.get(key)
        asset_entries = _asset_entries(asset_section)
        voice_entries = list(voice_section.entries) if voice_section else []
        if not asset_entries and not voice_entries:
            continue

        meta = _presentation(render_data, title)
        grouped_assets: dict[str, list[AssetEntry]] = {}
        for entry in asset_entries:
            grouped_assets.setdefault(entry.flow, []).append(entry)

        grouped_voices: dict[str, list[voice.VoiceEntry]] = {}
        for entry in voice_entries:
            flow = voice_flows.get(entry.voice_id)
            if not flow:
                raise ValueError(f"Voice requirement Flow missing for canonical production entry: {entry.voice_id}")
            grouped_voices.setdefault(flow, []).append(entry)

        flow_defs = dict(asset_section.flows) if asset_section else {}
        flow_titles = sorted(
            set(flow_defs) | set(grouped_assets) | set(grouped_voices),
            key=_flow_sort_key,
        )
        for flow_title in flow_titles:
            if flow_title not in flow_defs:
                raise ValueError(
                    f"Gameplay Flow metadata missing for Production Assets section: {title} / {flow_title}"
                )

        body = (
            '<header class="pa-shell">'
            '<small>Production Assets</small>'
            f'<h2>{esc(meta.title)}</h2><strong>{i18n(meta.package_label)}</strong>'
            '<p class="pa-section-note">Production-ready assets and exact in-game copy. Mechanics stay in 03 Development.</p>'
            '</header>'
        )
        if key == voice._title_key(SHARED_SECTION):
            body += _shared_voice_cast_html(voice_doc)

        body += f'<div class="pa-tabs" data-pa-tabs="{esc(meta.page_id)}">'
        body += '<div class="pa-tab-list" role="tablist" aria-label="Production flow">'
        for pos, flow_title in enumerate(flow_titles):
            panel_id = f"{meta.page_id}-flow-{slug(flow_title)}"
            selected = 'true' if pos == 0 else 'false'
            active = ' is-active' if pos == 0 else ''
            body += (
                f'<button class="pa-tab{active}" type="button" role="tab" '
                f'aria-selected="{selected}" aria-controls="{esc(panel_id)}" '
                f'data-pa-tab="{esc(panel_id)}">{esc(flow_title)}</button>'
            )
        body += '</div>'

        for pos, flow_title in enumerate(flow_titles):
            flow_assets = grouped_assets.get(flow_title, [])
            flow_voices = grouped_voices.get(flow_title, [])
            panel_id = f"{meta.page_id}-flow-{slug(flow_title)}"
            hidden = '' if pos == 0 else ' hidden'
            body += (
                f'<div class="pa-panel" id="{esc(panel_id)}" role="tabpanel"{hidden}>'
                f'<div class="pa-panel-head"><h3>{esc(flow_title)}</h3>'
                f'<span>{len(flow_assets) + len(flow_voices)} production items</span></div>'
                '<div class="pa-rows">'
            )
            for entry in flow_assets:
                body += _asset_html(entry, meta.page_id)
            for entry in flow_voices:
                for_text = voice_for.get(entry.voice_id)
                if not for_text:
                    raise ValueError(f"Voice requirement For missing for canonical production entry: {entry.voice_id}")
                if voice_doc is None:
                    raise ValueError("Voice entry exists without Voice Production document.")
                body += _voice_html(entry, voice_doc, for_text)
            body += '</div></div>'
        body += '</div>'

        index = len(pages)
        pid = meta.page_id
        pages.append(
            page(
                pid,
                f"PA-{index + 1:02d}",
                bi("Production Assets", "Aset Produksi"),
                body,
                context=meta.title,
                header=bi("Production Assets", "Aset Produksi"),
                footer_title=bi("Production Assets", "Aset Produksi"),
                brand=brand,
                role="production-assets",
                classes="sheet professional-only production-assets-page",
            )
        )
        links.append(
            f'<a data-target="{pid}" href="#{pid}">'
            f'<span class="production-assets-objective-name">{esc(meta.title)}</span>'
            f'<small>{i18n(meta.package_label)}</small></a>'
        )

    if not pages:
        raise ValueError("Production Assets contain no renderable accepted sections.")

    nav = (
        '<div class="nav-group is-open professional-nav production-assets-nav">'
        '<button aria-expanded="true" class="nav-group-toggle" type="button">'
        '<span class="nav-index" data-full-index="04" data-overview-index="">04</span>'
        f'<span class="nav-copy">{i18n(bi("Production Assets", "Aset Produksi"))}</span>'
        '<span aria-hidden="true" class="group-chevron"></span></button>'
        '<div class="nav-submenu">' + "".join(links) + "</div></div>"
    )
    return "".join(pages), nav


'''
    text = replace_between(text, 'def _pages_and_nav(', 'OBJECTIVE_STYLE =', pages_function)

    style = r'''OBJECTIVE_STYLE = r'''<style id="production-assets-objective-style">
.pa-shell{margin:0 0 14px}
.pa-shell>small{display:block;margin-bottom:6px;color:var(--blue);font-size:.62rem;font-weight:800;letter-spacing:.09em;text-transform:uppercase}
.pa-shell h2{margin:0;color:var(--navy);font-size:1.9rem;line-height:1.12;letter-spacing:-.025em}
.pa-shell>strong{display:block;margin:5px 0 7px;color:var(--amber);font-size:.69rem;letter-spacing:.06em;text-transform:uppercase}
.pa-section-note{max-width:78ch;margin:0;color:var(--muted);font-size:.72rem;line-height:1.45}
.pa-cast{margin:14px 0 18px;border:1px solid var(--line);border-radius:5px;overflow:hidden}
.pa-cast-head{display:flex;align-items:baseline;gap:10px;padding:9px 12px;background:var(--soft);border-bottom:1px solid var(--line)}
.pa-cast-head span{color:var(--navy);font-size:.72rem;font-weight:850;text-transform:uppercase;letter-spacing:.06em}
.pa-cast-head p{margin:0;color:var(--muted);font-size:.69rem}
.pa-cast-row{display:grid;grid-template-columns:minmax(120px,.8fr) minmax(0,2fr) auto;gap:12px;align-items:center;padding:9px 12px;border-top:1px solid var(--line);font-size:.72rem}
.pa-cast-row:first-child{border-top:0}.pa-cast-row strong{color:var(--navy)}.pa-cast-row small{color:var(--muted)}
.pa-tabs{margin-top:14px}
.pa-tab-list{display:flex;gap:5px;overflow-x:auto;padding:0 0 8px;border-bottom:1px solid var(--line);scrollbar-width:thin}
.pa-tab{flex:0 0 auto;min-height:34px;padding:7px 10px;border:1px solid transparent;border-radius:4px 4px 0 0;background:transparent;color:#52616a;font:750 .68rem/1.2 var(--font);cursor:pointer;text-align:left}
.pa-tab:hover,.pa-tab:focus-visible{color:var(--blue);outline:0;background:var(--soft)}
.pa-tab.is-active{border-color:var(--line);border-bottom-color:var(--paper);background:var(--paper);color:var(--navy);box-shadow:inset 0 3px 0 var(--blue)}
.pa-panel{padding-top:15px}.pa-panel[hidden]{display:none!important}
.pa-panel-head{display:flex;align-items:baseline;justify-content:space-between;gap:12px;margin-bottom:8px}
.pa-panel-head h3{margin:0;color:var(--navy);font-size:1.08rem;line-height:1.25;text-transform:none}
.pa-panel-head span{color:var(--muted);font-size:.62rem;white-space:nowrap}
.pa-rows{border-top:1px solid #cbd7dd}
.pa-row{border-bottom:1px solid #cbd7dd;background:var(--paper)}
.pa-row-main{display:grid;grid-template-columns:118px minmax(0,1fr) auto;gap:13px;align-items:center;padding:11px 8px}
.pa-type{display:inline-flex;align-items:center;width:max-content;max-width:112px;padding:4px 7px;border-radius:3px;background:var(--soft);color:var(--blue);font-size:.59rem;font-weight:900;letter-spacing:.055em;line-height:1.25;text-transform:uppercase}
.pa-type-voice{color:#9a5a0a;background:#fff5df}
.pa-row-info h4{margin:0;color:var(--navy);font-size:.86rem;line-height:1.3;text-transform:none}
.pa-row-info p{margin:3px 0 0;color:#52616a;font-size:.71rem;line-height:1.42}
.pa-row-info small{display:block;margin-top:4px;color:var(--muted);font-size:.62rem}
.pa-row-actions{display:flex;align-items:center;gap:6px;justify-content:flex-end}
.pa-copy-button,.pa-row .voice-copy-button{display:inline-flex;align-items:center;justify-content:center;min-height:28px;padding:6px 8px;border:1px solid var(--navy);border-radius:3px;background:var(--navy);color:#fff;font:800 .57rem/1 var(--font);letter-spacing:.04em;text-transform:uppercase;cursor:pointer;white-space:nowrap}
.pa-copy-button:hover,.pa-copy-button:focus-visible,.pa-row .voice-copy-button:hover,.pa-row .voice-copy-button:focus-visible{background:var(--blue);border-color:var(--blue);outline:0}
.pa-row-copy,.pa-row-details{margin:0 8px 10px 139px}
.pa-row-details{padding-top:0}
.pa-row-details summary{display:inline-flex;cursor:pointer;color:var(--blue);font-size:.66rem;font-weight:800;margin:0 0 7px;user-select:none}
.pa-content,.pa-row .voice-script-text{margin:0;padding:10px 12px;border:1px solid var(--line);border-left:3px solid var(--blue);border-radius:3px;background:#f8fafb;color:var(--navy);font:700 .76rem/1.52 var(--font);white-space:pre-wrap;overflow-wrap:anywhere}
.pa-row .voice-script-text{display:block!important;border-left-color:var(--amber)}
.pa-row .voice-script-display{margin-top:7px;padding:8px 0 0;border-top:1px solid var(--line)}
.pa-row .voice-performance-tag{font-size:.57rem}.pa-row .voice-script-line{font-size:.75rem;line-height:1.5}.pa-row .voice-script-gap{height:6px}
body.theme-dark .pa-tab.is-active,body.theme-dark .pa-row{background:#17262d}
body.theme-dark .pa-tab.is-active{border-bottom-color:#17262d}
body.theme-dark .pa-type{background:#1d2f37}.theme-dark .pa-type-voice{background:#3a2c14;color:#ffd488}
body.theme-dark .pa-row-info p,body.theme-dark .pa-section-note{color:#c8d7dc}
body.theme-dark .pa-content,body.theme-dark .pa-row .voice-script-text{background:#1d2f37;color:#e8eff3}
@media(max-width:760px){.pa-row-main{grid-template-columns:1fr auto}.pa-type{grid-column:1}.pa-row-info{grid-column:1/-1;grid-row:2}.pa-row-actions{grid-column:2;grid-row:1}.pa-row-copy,.pa-row-details{margin-left:8px}.pa-cast-row{grid-template-columns:1fr}.pa-panel-head{align-items:flex-start;flex-direction:column;gap:3px}}
@media print{.pa-tab-list{display:none!important}.pa-panel[hidden]{display:block!important}.pa-row{break-inside:avoid}.pa-copy-button,.pa-row .voice-copy-button{display:none!important}}
</style>''' '''
    style = style.strip()
    text = replace_between(text, 'OBJECTIVE_STYLE =', 'OBJECTIVE_COPY_SCRIPT =', style + '\n\n')

    scripts = r'''OBJECTIVE_COPY_SCRIPT = r'''<script id="production-assets-flow-copy-script">(function(){
  function fallbackCopy(text){
    var area=document.createElement('textarea');area.value=text;area.setAttribute('readonly','');area.style.position='fixed';area.style.opacity='0';document.body.appendChild(area);area.select();try{document.execCommand('copy');}finally{document.body.removeChild(area);}
  }
  document.addEventListener('click',function(event){
    var tab=event.target.closest('[data-pa-tab]');
    if(tab){
      var tabs=tab.closest('[data-pa-tabs]');if(!tabs)return;
      var id=tab.getAttribute('data-pa-tab');
      tabs.querySelectorAll('[data-pa-tab]').forEach(function(btn){var active=btn===tab;btn.classList.toggle('is-active',active);btn.setAttribute('aria-selected',active?'true':'false');});
      tabs.querySelectorAll('.pa-panel').forEach(function(panel){panel.hidden=panel.id!==id;});
      return;
    }
    var button=event.target.closest('[data-pa-copy]');if(!button)return;
    var source=document.getElementById(button.getAttribute('data-pa-copy'));if(!source)return;
    var text=source.textContent||'';var label=button.querySelector('.pa-copy-label');var original=label?label.textContent:'Copy';
    var done=function(){button.classList.add('is-copied');if(label)label.textContent='Copied ✓';else button.textContent='Copied ✓';setTimeout(function(){button.classList.remove('is-copied');if(label)label.textContent=original;else button.textContent=original;},1400);};
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(text).then(done,function(){fallbackCopy(text);done();});}else{fallbackCopy(text);done();}
  });
})();</script>''' '''
    scripts = scripts.strip()
    text = replace_between(text, 'OBJECTIVE_COPY_SCRIPT =', '\n\ndef _insert(', scripts + '\n')

    RENDERER.write_text(text, encoding='utf-8')


def remove_asset_block(text: str, title: str) -> str:
    pattern = re.compile(rf'\n#### {re.escape(title)}\n.*?(?=\n#### |\n### |\n## |\Z)', re.S)
    text2, count = pattern.subn('', text, count=1)
    if count != 1:
        raise SystemExit(f'expected one asset block for removal: {title} ({count})')
    return text2


def patch_asset_source() -> None:
    text = ASSET.read_text(encoding='utf-8')
    for title in ['Pillar Readability', 'Level Retry Reset', 'Trap Readability', 'Checkpoint Recovery']:
        text = remove_asset_block(text, title)

    replacements = {
        '#### First Objective Prompt': '#### Custodian Key Prompt',
        '#### Pillar Interaction Feedback': '#### Pillar Lamp Feedback',
        '#### Objective 2 Instruction Panel': '#### Broken Gallery Entrance Message',
        '#### Level 1 Brief': '#### First Crossing Message',
        '#### Level 2 Brief': '#### Second Crossing Message',
        '#### Level 3 Time-Challenge Brief': "#### Gremlin's Wager Message",
        '#### Route Failure Message': '#### Crossing Failure Messages',
        '#### Repair Markers': '#### Repair Gap Markers',
        '#### Gremlin Route-Closed Event': '#### Gremlin Path Collapse',
        '#### Objective 3 Instruction Panel': '#### Warden Halls Entrance Message',
        '#### Echo Pebble Cooldown Indicator': '#### Echo Pebble HUD',
        '#### Trap Hit Feedback': '#### Warden Hit Effects',
        '#### Objective 4 Instruction Panel': '#### Workshop Entrance Message',
        '#### Ring Progress Display': '#### Orrery Ring Status',
        '#### First Sabotage Message': '#### Route Swap Message',
        '#### 50% Sabotage Message': '#### Ring One Power Loss Message',
        '#### 80% Sabotage Message': '#### Ring Two Power Loss Message',
        '#### Ring 2 Route-Swap Sabotage': '#### Gremlin Route Swap',
        '#### 50% Rotator Sabotage': '#### Gremlin First Rollback',
        '#### 80% Rotator Sabotage': '#### Gremlin Second Rollback',
        '#### Completion Message': '#### Vault Restored Message',
        '#### Vault Awakening and Exit Reveal': '#### Vault Awakening Sequence',
    }
    for old, new in replacements.items():
        if old in text:
            text = text.replace(old, new, 1)

    simple_refs = {
        'First Objective Prompt': 'Custodian Key Prompt',
        'Pillar Interaction Feedback': 'Pillar Lamp Feedback',
        'Objective 2 Instruction Panel': 'Broken Gallery Entrance Message',
        'Level 1 Brief': 'First Crossing Message',
        'Level 2 Brief': 'Second Crossing Message',
        'Level 3 Time-Challenge Brief': "Gremlin's Wager Message",
        'Route Failure Message': 'Crossing Failure Messages',
        'Repair Markers': 'Repair Gap Markers',
        'Gremlin Route-Closed Event': 'Gremlin Path Collapse',
        'Objective 3 Instruction Panel': 'Warden Halls Entrance Message',
        'Echo Pebble Cooldown Indicator': 'Echo Pebble HUD',
        'Trap Hit Feedback': 'Warden Hit Effects',
        'Objective 4 Instruction Panel': 'Workshop Entrance Message',
        'Ring Progress Display': 'Orrery Ring Status',
        'First Sabotage Message': 'Route Swap Message',
        '50% Sabotage Message': 'Ring One Power Loss Message',
        '80% Sabotage Message': 'Ring Two Power Loss Message',
        'Ring 2 Route-Swap Sabotage': 'Gremlin Route Swap',
        '50% Rotator Sabotage': 'Gremlin First Rollback',
        '80% Rotator Sabotage': 'Gremlin Second Rollback',
        'Completion Message': 'Vault Restored Message',
        'Vault Awakening and Exit Reveal': 'Vault Awakening Sequence',
    }
    for old, new in simple_refs.items():
        text = text.replace(old, new)

    ASSET.write_text(text, encoding='utf-8')


def append_authority() -> None:
    source = SOURCE.read_text(encoding='utf-8')
    if 'id: SRC-014' not in source:
        source += '''\n  - id: SRC-014\n    type: instruction\n    role: authoritative\n    status: current\n    origin: user\n    inspection: full\n    summary: User approved the Production Assets information-architecture audit. Section 04 must match the usability quality of sections 01-03: gameplay flows are interactive tabs, only the active flow is shown by default, assets use compact production rows rather than large repeated cards, per-flow For text is not repeated, Voice prompts are collapsed by default, Voice Cast is shown once in Shared Assets, exact UI/Text remains directly copyable, and non-deliverable design requirements belong in Development rather than Production Assets.\n'''
        SOURCE.write_text(source, encoding='utf-8')

    req = REQ.read_text(encoding='utf-8')
    if 'id: REQ-020' not in req:
        req += '''\n  - id: REQ-020\n    area: production-assets\n    statement: Section 04 must use a low-density production reference architecture comparable in clarity to sections 01-03. Each objective page uses interactive gameplay-flow tabs with only one flow visible by default. Inside a flow, each concrete production deliverable is a compact row showing literal asset type, asset name, one short purpose sentence, and Copy/View actions only when exact text or Voice exists. Do not repeat flow-level For descriptions. Voice prompts are collapsed by default and Voice Cast appears once in Global / Shared Assets. Remove abstract design/readability/reset requirements from 04 when they do not represent a concrete production deliverable; those remain owned by Development.\n    provenance: [SRC-014]\n    evidence_status: approved\n    recovery_class: none\n    approval_status: not_required\n    impact: high\n'''
        REQ.write_text(req, encoding='utf-8')


patch_renderer()
patch_asset_source()
append_authority()
print('04 tabbed compact UX prepared')
