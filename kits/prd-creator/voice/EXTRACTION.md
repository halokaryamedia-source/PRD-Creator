# Voice Requirement Extraction

Flow 5 converts one accepted `handoff_ready` PRD revision into justified player-facing Voice requirements. It owns Voice scope, stable placement identity, communication intent, and source timing truth. It does **not** write final performance text.

## Entry gate

Before extraction run:

```bash
python kits/prd-creator/validator/validate_handoff.py \
  workspace/active/<project>/
```

Start only when the current handoff, exact accepted render-data revision, canonical PRD, and versioned delivery agree.

## Authority

```text
accepted work/content.md
→ approved requirement state when traceability is needed
→ current versioned delivery as navigation/presentation aid
→ Voice reference material for structure/craft only
```

Reference projects never supply new project facts, speakers, channels, triggers, owners, or Voice moments.

## Stable Owner ID

Flow 5 owns the placement identity for every Voice section. It is project topology, not Flow 6 craft.

Use exactly one:

```text
Owner ID: journey:<gameplay-flow-id>   # only for non-package journey nodes
Owner ID: package:<package-id>         # package and its matching gameplay-flow meaning
```

Do not use `journey:<package-id>` for a package. Display titles are presentation only and may change without changing identity.

## Extraction sequence

```text
current handoff guard PASS
→ identify player-facing communication system
→ identify justified Voice moments
→ remove UI-only / redundant / unsupported moments
→ assign stable Owner ID
→ define Function / Necessity / Speaker / Channel / Trigger / Purpose / Moment
→ preserve required communication / exclusions / source refs
→ record authoritative Timing Constraint only when one exists
→ mechanically validate voice_requirements_ready
→ Flow 6
```

## Candidate rule

Keep a candidate only when it is player-facing, source-supported, tied to an approved Speaker/Channel/Trigger, useful at that moment, and non-duplicative without a distinct gameplay reason. A package may legitimately have zero Voice moments.

Reject developer telemetry, hidden implementation state, decorative unsupported narration, duplicate UI reading, invented lore/mechanics/rewards/triggers, and symmetry added merely because another package has Voice.

## Canonical Flow 5 interface

Every included Voice ID must define:

- **Owner ID** — stable accepted topology owner for 04 placement;
- **Type** — `Main Story`, `Radio Communication`, or another explicit supported type;
- **Function** — communication job such as `briefing`, `warning`, `transition`, `completion`;
- **Necessity** — `required` or `supporting`;
- **Speaker** — approved speaker identity;
- **Channel** — approved communication channel;
- **Trigger** — concrete project event/state including listener state when material;
- **Purpose** — what the listener must know/do/understand after hearing it;
- **Moment** — natural reader-facing Production Assets moment where this resource belongs;
- **Must communicate** — one or more material facts/actions;
- **Must not add/repeat** — one or more scope/continuity guardrails;
- **Source refs** — one or more accepted requirement/content references;
- **Timing Constraint** — optional; authoritative hard window/sync truth only.

`Moment` is not a script title. It is the stable reader-facing grouping used by `04 Production Assets`.

`Timing Constraint` is not Flow 6 `Estimated Duration`. Omit it when no hard upstream timing truth exists.

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
- Moment: <natural Production Assets moment>
- Timing Constraint: <authoritative constraint only; omit when none>
- Must communicate:
  - <material fact/action>
- Must not add/repeat:
  - <scope/continuity guardrail>
- Source refs:
  - <accepted requirement/content reference>
```

Do not include final wording, performance tags, Estimated Duration, commercial voice selection, Stability, Surface, or other Flow 6 craft.

## Canonical Voice state

`state/voice-state.yaml` uses one schema across Flow 5–7. Do not add lifecycle aliases or helper fields.

```yaml
status: voice_requirements_ready
source_handoff: state/handoff-state.yaml
source_prd_revision: <accepted document.version>
canonical_prd: work/content.md
requirements: work/voice-requirements.md
production: work/voice-production.md
project_html: output/v<accepted document.version>/prd.html
```

`production` names the canonical downstream path even before the file exists. `project_html` names the current consolidated delivery path when that delivery already exists.

Lifecycle statuses are:

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

Unknown/retired state fields are invalid; do not reintroduce `source_revision`, `flow`, `next_step`, `unresolved_upstream`, or `delivery_scope` as parallel lifecycle vocabulary.

## Flow 5 mechanical gate

After requirements are written and before Flow 6:

```bash
python kits/prd-creator/validator/validate_voice.py \
  workspace/active/<project>/
```

At `voice_requirements_ready`, this validates current handoff/revision identity, the strict Flow 5 field contract, and every Owner ID against accepted PRD topology. It does not require `voice-production.md` yet.

`no_voice_required` is valid only when accepted upstream meaning supports no Voice production for the current scope.

## Upstream return rule

Use `needs_upstream_decision` when Speaker, Channel, Trigger, Purpose, Moment ownership, required communication, result/reward, terminology/sequence, or authoritative timing truth remains materially unresolved.

Do not hide those decisions inside Flow 6 wording.

## Completion

Flow 5 is complete only when `voice_requirements_ready` mechanically passes, or accepted evidence supports `no_voice_required`. Stop before performance writing.
