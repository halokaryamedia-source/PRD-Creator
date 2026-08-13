#!/usr/bin/env python3
from __future__ import annotations
import argparse, re, sys
from dataclasses import dataclass, field
from pathlib import Path
from docx import Document

PLACEHOLDER_RE = re.compile(r"\b(?:TBD|TODO|FIXME)\b|\[OPEN\]", re.I)
ENTRY_RE = re.compile(r"^###\s+([A-Za-z0-9][A-Za-z0-9-]*)\s+[—-]\s+(.+?)\s*$")
VOICE_ID_RE = re.compile(r"\bVO-[A-Z0-9][A-Z0-9-]*\b")
STATUS_RE = re.compile(r"^\s*status:\s*([A-Za-z0-9_-]+)\s*$", re.M)

@dataclass
class Requirement:
    voice_id: str
    title: str
    voice_type: str = ""
    speaker: str = ""
    channel: str = ""
    trigger: str = ""
    must_communicate: list[str] = field(default_factory=list)

@dataclass
class ScriptEntry:
    voice_id: str
    title: str
    voice_type: str = ""
    speaker: str = ""
    duration: str = ""
    performance: str = ""
    section: str = ""


def norm(s: str) -> str:
    return " ".join(s.split())


def parse_requirements(path: Path) -> dict[str, Requirement]:
    text = path.read_text(encoding="utf-8")
    if PLACEHOLDER_RE.search(text):
        raise ValueError("Voice requirements contain unresolved placeholders")
    lines = text.splitlines()
    out: dict[str, Requirement] = {}
    current: Requirement | None = None
    list_mode: str | None = None
    for raw in lines:
        line = raw.rstrip()
        m = ENTRY_RE.match(line)
        if m:
            vid = m.group(1)
            if vid in out:
                raise ValueError(f"Duplicate Voice ID in requirements: {vid}")
            current = Requirement(vid, m.group(2).strip())
            out[vid] = current
            list_mode = None
            continue
        if current is None:
            continue
        if line.startswith("- Type:"):
            current.voice_type = line.split(":",1)[1].strip(); list_mode=None
        elif line.startswith("- Speaker:"):
            current.speaker = line.split(":",1)[1].strip(); list_mode=None
        elif line.startswith("- Channel:"):
            current.channel = line.split(":",1)[1].strip(); list_mode=None
        elif line.startswith("- Trigger:"):
            current.trigger = line.split(":",1)[1].strip(); list_mode=None
        elif line.startswith("- Must communicate:"):
            list_mode = "must"
        elif line.startswith("- Must not add/repeat:") or line.startswith("- Source refs:"):
            list_mode = None
        elif list_mode == "must" and re.match(r"^\s{2,}-\s+", line):
            current.must_communicate.append(re.sub(r"^\s{2,}-\s+", "", line).strip())
    if not out:
        raise ValueError("No Voice IDs found in requirements")
    for r in out.values():
        missing = [k for k,v in {"Type":r.voice_type,"Speaker":r.speaker,"Channel":r.channel,"Trigger":r.trigger}.items() if not v]
        if missing:
            raise ValueError(f"{r.voice_id} missing requirement metadata: {', '.join(missing)}")
    return out


def parse_script(path: Path) -> tuple[list[str], dict[str, ScriptEntry]]:
    text = path.read_text(encoding="utf-8")
    if PLACEHOLDER_RE.search(text):
        raise ValueError("Voice script contains unresolved placeholders")
    lines = text.splitlines()
    sections: list[str] = []
    current_section = ""
    out: dict[str, ScriptEntry] = {}
    i=0
    while i < len(lines):
        line = lines[i].rstrip()
        if line.startswith("## "):
            current_section = line[3:].strip()
            sections.append(current_section)
            i += 1; continue
        m = ENTRY_RE.match(line)
        if not m:
            i += 1; continue
        vid=m.group(1)
        if vid in out: raise ValueError(f"Duplicate Voice ID in script: {vid}")
        e=ScriptEntry(vid,m.group(2).strip(),section=current_section)
        i += 1
        while i < len(lines):
            meta=lines[i].rstrip()
            if meta.startswith("Type:"):
                e.voice_type=meta.split(":",1)[1].strip(); i+=1; continue
            if meta.startswith("Speaker:"):
                e.speaker=meta.split(":",1)[1].strip(); i+=1; continue
            if meta.startswith("Estimated Duration:"):
                e.duration=meta.split(":",1)[1].strip(); i+=1; continue
            if meta.strip()=="```performance":
                i+=1; body=[]
                while i<len(lines) and lines[i].strip()!="```":
                    body.append(lines[i].rstrip()); i+=1
                if i>=len(lines): raise ValueError(f"Unclosed performance block for {vid}")
                e.performance="\n".join(body).strip(); i+=1; break
            if meta.startswith("### ") or meta.startswith("## "):
                break
            i+=1
        if not current_section: raise ValueError(f"{vid} appears before a section")
        for k,v in {
            "Type":e.voice_type,
            "Speaker":e.speaker,
            "Estimated Duration":e.duration,
            "Performance Script":e.performance,
        }.items():
            if not v: raise ValueError(f"{vid} missing {k}")
        out[vid]=e
    if not out: raise ValueError("No Voice IDs found in script")
    return sections,out


def validate_state(path: Path) -> str:
    text=path.read_text(encoding="utf-8")
    m=STATUS_RE.search(text)
    if not m: raise ValueError("voice-state.yaml missing status")
    status=m.group(1)
    allowed = {"voice_script_ready", "voice_validation", "needs_revision", "voice_delivery_ready"}
    if status not in allowed:
        raise ValueError(f"Flow 7 cannot validate status {status}; expected one of: {', '.join(sorted(allowed))}")
    return status


def validate_docx(path: Path, sections: list[str], script: dict[str, ScriptEntry]) -> list[str]:
    doc=Document(path)
    paras=[p.text for p in doc.paragraphs]
    full="\n".join(paras)
    flat=norm(full)
    issues=[]
    for section in sections:
        if section and norm(section) not in flat:
            issues.append(f"DOCX missing section heading: {section}")
    expected=set(script)
    actual=set(VOICE_ID_RE.findall(full))
    if actual != expected:
        missing=sorted(expected-actual); extra=sorted(actual-expected)
        if missing: issues.append("DOCX missing Voice IDs: "+", ".join(missing))
        if extra: issues.append("DOCX has extra Voice IDs: "+", ".join(extra))
    for vid,e in script.items():
        if full.count(vid) != 1:
            issues.append(f"DOCX must contain {vid} exactly once")
        if f"Speaker: {e.speaker}" not in full:
            issues.append(f"DOCX missing speaker for {vid}: {e.speaker}")
        if e.duration not in full:
            issues.append(f"DOCX missing duration for {vid}: {e.duration}")
        if norm(e.performance) not in flat:
            issues.append(f"DOCX performance text differs/missing for {vid}")
    sec=doc.sections[0]
    w=round(sec.page_width.inches,2); h=round(sec.page_height.inches,2)
    if (w,h)!=(8.5,11.0): issues.append(f"DOCX page size expected Letter 8.5x11, got {w}x{h}")
    if not doc.paragraphs: issues.append("DOCX contains no paragraphs")
    return issues


def main() -> int:
    ap=argparse.ArgumentParser(description="Mechanically validate the current Flow 7 Voice requirements/script/DOCX package.")
    ap.add_argument("project",type=Path, help="workspace/active/<project> directory")
    args=ap.parse_args(); p=args.project
    req=p/"work/voice-requirements.md"; scr=p/"work/voice-production.md"; docx=p/"output/Voice Production.docx"; state=p/"state/voice-state.yaml"
    missing=[str(x.relative_to(p)) for x in (req,scr,docx,state) if not x.is_file()]
    if missing:
        print("VOICE VALIDATION FAILED: missing files: "+", ".join(missing),file=sys.stderr); return 2
    try:
        validate_state(state)
        requirements=parse_requirements(req)
        sections,script=parse_script(scr)
        issues=[]
        if set(requirements)!=set(script):
            mi=sorted(set(requirements)-set(script)); ex=sorted(set(script)-set(requirements))
            if mi: issues.append("Script missing Voice IDs: "+", ".join(mi))
            if ex: issues.append("Script has extra Voice IDs: "+", ".join(ex))
        for vid in sorted(set(requirements)&set(script)):
            if requirements[vid].voice_type.casefold()!=script[vid].voice_type.casefold():
                issues.append(f"Type mismatch for {vid}")
            if requirements[vid].speaker.casefold()!=script[vid].speaker.casefold():
                issues.append(f"Speaker mismatch for {vid}")
        issues.extend(validate_docx(docx,sections,script))
        if issues:
            print("VOICE VALIDATION FAILED")
            for x in issues: print("- "+x)
            return 1
        print("VOICE VALIDATION PASS")
        print(f"requirements={len(requirements)} script_entries={len(script)} sections={len(sections)}")
        print("docx_structure=passed")
        print("semantic_and_visual_review=required")
        return 0
    except (OSError,ValueError) as e:
        print(f"VOICE VALIDATION FAILED: {e}",file=sys.stderr); return 2
if __name__=="__main__": raise SystemExit(main())
