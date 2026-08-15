from pathlib import Path
import re

ROOT = Path('.')
VALIDATOR = ROOT / 'kits/voice-production-kit/validator/validate.py'
TESTS = ROOT / 'tests/test_voice_contracts.py'
RENDERER = ROOT / 'kits/project-document-generator/renderer/production_assets_objective.py'


def replace_between(text: str, start: str, end: str, replacement: str) -> str:
    a = text.index(start)
    b = text.index(end, a)
    return text[:a] + replacement + text[b:]


def patch_validator() -> None:
    text = VALIDATOR.read_text(encoding='utf-8')
    fn = '''def validate_project_html(\n    path: Path,\n    sections: list[str],\n    script: dict[str, ScriptEntry],\n    requirements: dict[str, Requirement],\n) -> list[str]:\n    source = path.read_text(encoding="utf-8")\n    issues=[]\n    if 'id="production-assets-style"' not in source:\n        issues.append("Project HTML missing Production Assets presentation")\n    if "Production Assets" not in source or "production-assets-nav" not in source:\n        issues.append("Project HTML missing Production Assets Voice navigation")\n    if source.count('class="pa-row pa-row-voice"') != len(script):\n        issues.append("Project HTML compact Voice row count differs from canonical script")\n\n    for section in sections:\n        plain = re.sub(r"^\\s*\\d+\\.\\s*", "", section).strip()\n        if plain and html.escape(plain, quote=True) not in source:\n            issues.append(f"Project HTML missing Voice gameplay section: {plain}")\n\n    for vid,e in script.items():\n        prompt_id=f"voice-prompt-{vid.lower()}"\n        pattern=re.compile(rf'<pre class="voice-script-text" id="{re.escape(prompt_id)}">(.*?)</pre>', re.S)\n        matches=pattern.findall(source)\n        if len(matches)!=1:\n            issues.append(f"Project HTML must contain exact Voice prompt panel once for {vid}")\n            continue\n        actual=html.unescape(matches[0])\n        if actual != e.performance:\n            issues.append(f"Project HTML performance text differs from canonical script for {vid}")\n        identity = html.escape(f"{e.speaker} — {e.title}", quote=True)\n        if identity not in source:\n            issues.append(f"Project HTML missing compact Voice identity for {vid}")\n    return issues\n\n\n'''
    text = replace_between(text, 'def validate_project_html(', 'def validate_docx(', fn)
    VALIDATOR.write_text(text, encoding='utf-8')


def patch_tests() -> None:
    text = TESTS.read_text(encoding='utf-8')
    fixture = '''def project_html(*, omit_intro_prompt: bool = False) -> str:\n    intro = "" if omit_intro_prompt else '<div class="pa-row pa-row-voice"><h4>Narrator — Welcome</h4><pre class="voice-script-text" id="voice-prompt-vo-intro-01">[calm]\\nBegin the trial.</pre></div>'\n    return f"""<!doctype html>\n<html><head><style id="production-assets-style"></style></head><body>\n<div class="nav-group production-assets-nav">Production Assets</div>\n<section data-page-role="production-assets"><h2>Intro</h2>{intro}</section>\n<section data-page-role="production-assets"><h2>Ending</h2>\n<div class="pa-row pa-row-voice"><h4>Guide — Complete</h4><pre class="voice-script-text" id="voice-prompt-vo-end-01">[clear]\\nThe trial is complete.</pre></div></section>\n</body></html>"""\n\n\n'''
    text = replace_between(text, 'def project_html(', 'class VoiceProductionContracts', fixture)
    old = '''    def test_validator_rejects_missing_flow5_trigger_context_in_project_html(self) -> None:\n        project = self.make_project()\n        (project / "output/v1.0.0/prd.html").write_text(\n            project_html(omit_intro_context=True),\n            encoding="utf-8",\n        )\n\n        validated = run_cli(VALIDATOR, project)\n        self.assertEqual(validated.returncode, 1)\n        self.assertIn(\n            "Project HTML missing Flow 5 Trigger context for VO-INTRO-01",\n            validated.stdout,\n        )\n\n'''
    new = '''    def test_validator_rejects_missing_voice_prompt_in_project_html(self) -> None:\n        project = self.make_project()\n        (project / "output/v1.0.0/prd.html").write_text(\n            project_html(omit_intro_prompt=True),\n            encoding="utf-8",\n        )\n\n        validated = run_cli(VALIDATOR, project)\n        self.assertEqual(validated.returncode, 1)\n        self.assertIn(\n            "Project HTML must contain exact Voice prompt panel once for VO-INTRO-01",\n            validated.stdout,\n        )\n\n'''
    if old not in text:
        raise SystemExit('old trigger-context test not found')
    text = text.replace(old, new, 1)
    TESTS.write_text(text, encoding='utf-8')


def patch_renderer_overrides() -> None:
    text = RENDERER.read_text(encoding='utf-8')
    marker = '        "Repair Markers": "PRESENTATION",\n'
    if marker in text:
        text = text.replace(marker, '', 1)
    insert_after = '        "Orrery Ring": "MODEL / ANIMATION",\n'
    additions = (
        '        "Pillar Lamp Feedback": "VFX",\n'
        '        "Warden Hit Effects": "VFX",\n'
        '        "Repair Gap Markers": "PRESENTATION",\n'
        '        "Gremlin Path Collapse": "PRESENTATION",\n'
        '        "Gremlin Route Swap": "PRESENTATION",\n'
        '        "Gremlin First Rollback": "PRESENTATION",\n'
        '        "Gremlin Second Rollback": "PRESENTATION",\n'
    )
    if additions not in text:
        if insert_after not in text:
            raise SystemExit('renderer override insertion point missing')
        text = text.replace(insert_after, insert_after + additions, 1)
    RENDERER.write_text(text, encoding='utf-8')


patch_validator()
patch_tests()
patch_renderer_overrides()
print('compact Voice contract prepared')
