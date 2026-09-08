# Voice Requirements

Voice Requirements converts one accepted `handoff_ready` PRD state into justified player-facing Voice requirements. It owns Voice scope, stable placement identity, communication intent, and authoritative timing truth. It does **not** write final performance text.

## Entry gate

Run:

```bash
python kits/prd-creator/validator/validate_handoff.py workspace/active/<project>/
```

Start only when PRD Handoff, exact accepted Render Data / Production Assets revision, canonical PRD, and versioned delivery agree.

Capture:

```text
source_prd_revision
source_prd_sha256
```

Both must remain current for every downstream Voice status, including `no_voice_required`.

## Authority

```text
accepted work/content.md
→ approved requirement state when traceability is needed
→ current versioned delivery as navigation/presentation aid
→ Voice reference material for structure/craft only
```

Reference projects never supply new project facts, speakers, channels, triggers, owners, moments, or Voice scope.

## Stable placement identity

Voice Requirements owns placement keys used by Production Assets presentation:

```text
Owner ID
→ Moment ID
→ Voice ID
```

### Owner ID

```text
Owner ID: journey:<gameplay-flow-id>   # non-package journey node only
Owner ID: package:<package-id>         # package + matching gameplay meaning
```

### Moment ID

```text
Moment ID: MOM-<STABLE-ID>
Moment: <reader-facing moment title>
```

`Moment ID` is machine identity; `Moment` is presentation. Multiple Voice/non-Voice resources may share one Owner + Moment ID.

## Extraction sequence

```text
current PRD Handoff PASS
→ capture accepted Render Data SHA
→ identify player-facing communication system
→ identify justified Voice moments
→ remove UI-only / redundant / unsupported moments
→ assign Owner ID + Moment ID
→ define Function / Necessity / Speaker / Channel / Trigger / Purpose
→ preserve required communication / exclusions / source refs
→ record authoritative Timing Constraint only when one exists
→ mechanically validate voice_requirements_ready
→ Voice Production
```

## Candidate rule

Keep a candidate only when it is player-facing, source-supported, tied to an approved Speaker/Channel/Trigger, useful at that moment, and non-duplicative without a distinct gameplay reason. A package may legitimately have zero Voice moments.

Reject telemetry, hidden implementation state, decorative unsupported narration, duplicate UI reading, invented lore/mechanics/rewards/triggers, and symmetry added merely because another package has Voice.

## Canonical interface

Every included Voice ID defines:

- **Owner ID** — accepted topology owner;
- **Moment ID** — stable production-moment identity;
- **Moment** — reader-facing moment title;
- **Type** — `Main Story`, `Radio Communication`, or another explicit supported type;
- **Function** — communication job such as `briefing`, `warning`, `transition`, `completion`;
- **Necessity** — `required` or `supporting`;
- **Speaker** — approved identity;
- **Channel** — approved communication channel;
- **Trigger** — concrete event/state including listener state when material;
- **Purpose** — what the listener must know/do/understand afterward;
- **Must communicate** — one or more material facts/actions;
- **Must not add/repeat** — one or more scope/continuity guardrails;
- **Source refs** — accepted requirement/content references;
- **Timing Constraint** — optional authoritative hard window/sync truth only.

`Timing Constraint` is not Voice Production `Estimated Duration`.

## Canonical output

```text
# Voice Requirements

Source PRD revision: <accepted document.version>
Voice system: <speaker/channel summary>

## <Gameplay Section>
Owner ID: package:<id> | journey:<id>

### VO-<SECTION>-01 — <Functional title>
- Type: Main Story | Radio Communication | <explicit supported type>
- Function: briefing | warning | ...
- Necessity: required | supporting
- Speaker: <approved speaker>
- Channel: <approved channel>
- Trigger: <approved event/state + relevant listener state>
- Purpose: <listener-facing outcome>
- Moment ID: MOM-<STABLE-ID>
- Moment: <natural Production Assets moment>
- Timing Constraint: <authoritative constraint only; omit when none>
- Must communicate:
  - <material fact/action>
- Must not add/repeat:
  - <scope/continuity guardrail>
- Source refs:
  - <accepted requirement/content reference>
```

Do not include final wording, performance tags, Estimated Duration, commercial voice selection, Stability, Surface, or other Voice Production craft.

## Canonical Voice state

`state/voice-state.yaml` uses one schema across Voice Requirements, Voice Production, and Voice Delivery:

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

Lifecycle statuses remain unchanged:

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

These are machine state names, not alternate workflow-stage names.

## Mechanical gate

After requirements are written:

```bash
python kits/prd-creator/validator/validate_voice.py workspace/active/<project>/
```

At `voice_requirements_ready`, validation checks current PRD Handoff, source PRD identity, strict Voice Requirements fields, and Owner topology without requiring `voice-production.md` yet.

## Upstream return rule

Use `needs_upstream_decision` when Speaker, Channel, Trigger, Purpose, Owner/Moment identity, required communication, result/reward, terminology/sequence, or authoritative timing truth remains materially unresolved.

Do not hide those decisions inside Voice Production wording.

## Completion

Voice Requirements is complete only when `voice_requirements_ready` mechanically passes, or accepted evidence supports `no_voice_required`. Stop before Voice Production.