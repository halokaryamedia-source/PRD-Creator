# Voice Requirement Extraction

Status: active Flow 5 policy

## Purpose

Convert one accepted Flow 4 handoff into the minimal traceable Voice scope that Flow 6 can author without inventing project meaning.

Detailed field/state procedure lives in `kits/prd-creator/voice/EXTRACTION.md`; this page owns durable boundaries only.

## Canonical owners

```text
work/voice-requirements.md
→ Voice scope + communication intent + Owner ID + Moment ID

state/voice-state.yaml
→ one Voice lifecycle status + canonical refs + exact accepted PRD source identity
```

## Entry

Flow 5 starts only from a **currently valid** `handoff_ready` state. Before extraction run `validator/validate_handoff.py`.

Voice source identity is two-part:

```text
source_prd_revision
+ source_prd_sha256
```

The version identifies the accepted PRD revision family; the SHA binds the exact accepted `work/render-data.json` bytes. A same-version PRD/04 revision therefore invalidates stale Voice state unless the current handoff is revalidated and Flow 5 is refreshed as needed.

If accepted PRD/04 meaning changes, reopen only affected Voice requirements.

## Stable placement identity

Flow 5 defines placement because it is project meaning, not performance craft:

```text
Owner ID
  ↓
Moment ID
  ↓
Voice ID
```

Owner IDs are `package:<id>` for package-owned meaning and `journey:<id>` only for non-package journey nodes. `Moment ID` uses stable `MOM-...` identity. Display section/moment titles may change without changing those IDs.

## Flow 5 → Flow 6 interface

Every included requirement defines:

```text
Owner ID
Moment ID + Moment
Type
Function
Necessity
Speaker
Channel
Trigger
Purpose
Must communicate
Must not add/repeat
Source refs
Timing Constraint   # optional authoritative truth only
```

Flow 6 still owns final wording, performance tags, punctuation/CAPS, Estimated Duration, voice/profile selection, Stability, Surface, and other production interpretation.

## Candidate/readiness rule

Keep a Voice moment only when it is player-facing, supported by accepted meaning, tied to approved Speaker/Channel/Trigger, useful at that point, and non-duplicative without a distinct reason. A package may legitimately have zero Voice moments.

Return upstream when a material Speaker, Channel, Trigger, Purpose, Owner/Moment identity, required fact, result/reward, sequence, or authoritative timing rule is unresolved.

## One Voice lifecycle schema

All Voice flows use the schema owned by `shared/lifecycle.py`:

```yaml
status: voice_requirements_ready
source_handoff: state/handoff-state.yaml
source_prd_revision: <accepted document.version>
source_prd_sha256: <sha256 of exact accepted work/render-data.json bytes>
canonical_prd: work/content.md
requirements: work/voice-requirements.md
production: work/voice-production.md
project_html: output/v<accepted document.version>/prd.html
```

Persisted refs are normalized project-relative POSIX paths. Unknown/retired lifecycle fields are invalid.

## Mechanical boundary

`validator/validate_voice.py` is lifecycle-aware. At every validatable Voice state it reruns canonical PRD handoff validation, checks exact PRD source SHA + revision identity, and then applies the stage-specific Voice checks. `voice_requirements_ready` does not require a production script yet.

`no_voice_required` is also revision-bound; it cannot remain valid after the accepted PRD bytes change merely because `document.version` stayed the same.

## Completion

Flow 5 completes as either:

- `voice_requirements_ready`; or
- `no_voice_required` when accepted upstream meaning justifies no Voice.

Stop before performance writing.
