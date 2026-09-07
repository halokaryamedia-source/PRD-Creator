# Voice Requirement Extraction

Status: active Flow 5 policy

## Purpose

Convert one Flow 4 `handoff_ready` PRD revision into a minimal, traceable set of justified Voice moments that Flow 6 can author without inventing project meaning.

## Canonical owners

```text
work/voice-requirements.md
→ Voice scope + communication intent + stable Owner ID + natural production Moment

state/voice-state.yaml
→ lifecycle status + current source/delivery paths + source PRD revision
```

Detailed procedure is `kits/prd-creator/voice/EXTRACTION.md`.

## Entry

Flow 5 starts only from current `handoff_ready` meaning. Before extraction:

```bash
python kits/prd-creator/validator/validate_handoff.py \
  workspace/active/<project>/
```

If accepted PRD meaning changes, only affected Voice requirements become stale.

## Stable placement identity

Flow 5 assigns the 04 owner because placement is project topology, not performance craft:

```text
journey:<gameplay-flow-id>  → non-package journey node only
package:<package-id>        → package plus its matching gameplay-flow meaning
```

A package must not also use `journey:<package-id>`. Human-readable section titles are not machine identity.

## Flow 5 → Flow 6 contract

Every included requirement defines:

```text
Owner ID
Type
Function
Necessity
Speaker
Channel
Trigger
Purpose
Moment
Must communicate
Must not add/repeat
Source refs
Timing Constraint   # optional authoritative truth only
```

Meaning:

- **Owner ID** — stable PRD topology owner for Production Assets placement;
- **Function** — primary communication job;
- **Necessity** — `required` or `supporting`;
- **Trigger** — concrete gameplay/story state, including listener state when material;
- **Purpose** — what the listener should know/do/understand after the line;
- **Moment** — natural 04 Production Assets grouping where the Voice resource belongs;
- **Must communicate** — independently actionable communication payload;
- **Must not add/repeat** — scope/continuity guards;
- **Source refs** — enough accepted traceability to verify meaning;
- **Timing Constraint** — optional hard upstream timing/sync truth, never a production estimate.

Flow 6 still owns final wording, performance tags, punctuation/CAPS, Estimated Duration, actual voice/profile selection, Stability, Surface, and other production interpretation.

## Candidate/readiness rule

Keep a Voice moment only when it is player-facing, supported by accepted meaning, tied to approved Speaker/Channel/Trigger, useful at that moment, and non-duplicative without a distinct reason. A gameplay package may legitimately have zero Voice moments.

Return upstream when a material Speaker, Channel, Trigger, Purpose, Moment ownership, required fact, result/reward, terminology/sequence, or authoritative timing rule is unresolved.

## Canonical Voice state

All Voice flows use one state vocabulary:

```yaml
status: voice_requirements_ready
source_handoff: state/handoff-state.yaml
source_prd_revision: <accepted document.version>
canonical_prd: work/content.md
requirements: work/voice-requirements.md
production: work/voice-production.md
project_html: output/v<accepted document.version>/prd.html
```

Supported lifecycle statuses:

```text
pending_extraction
needs_upstream_decision
voice_requirements_ready
no_voice_required
blocked
voice_script_ready
voice_validation
needs_revision
voice_delivery_ready
```

Unknown or retired lifecycle fields are invalid. Do not maintain parallel aliases such as `source_revision`, `flow`, `next_step`, `unresolved_upstream`, or `delivery_scope`.

## Mechanical boundary

At `voice_requirements_ready`, run:

```bash
python kits/prd-creator/validator/validate_voice.py \
  workspace/active/<project>/
```

The same lifecycle-aware validator is reused later for Flow 6/7. At Flow 5 it validates handoff/revision identity, strict requirement fields, and Owner IDs without requiring `voice-production.md` yet.

## Completion

Flow 5 completes as either:

- `voice_requirements_ready` — requirements mechanically and semantically ready for Flow 6; or
- `no_voice_required` — accepted upstream meaning supports no Voice for the current scope.

Stop before performance writing.
