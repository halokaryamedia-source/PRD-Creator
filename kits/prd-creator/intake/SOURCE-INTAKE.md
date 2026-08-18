# Source Intake & Requirement Recovery

Flow 2 turns uneven project material into a **complete reviewable project model** before Flow 3 writes the PRD. It recovers supported meaning, notices material gaps/conflicts, forms practical AI proposals when authority does not settle an answer, propagates the chosen model across production roles, preserves real Production Asset needs, and obtains user approval through the Simple Chat Preview.

Source-backed meaning and AI-proposed meaning remain distinguishable internally until approval. A Proposal may be concrete; it must never be presented as if it came from the source.

## Outcome

Keep only state needed for continuity and current truth:

```text
state/source-inventory.yaml
state/requirement-register.yaml
state/intake-state.yaml
work/review.md                 # only when a readable decision summary materially helps
```

The Simple Chat Preview is **chat output, not another artifact**. Do not create topology maps, coverage spreadsheets, dependency graphs, preview HTML, asset-inventory previews, or extra approval files.

## 1. Bootstrap, authority, and source retention

```text
user project name OR strongest authoritative title
→ derive/reuse stable project workspace
→ inventory current evidence
→ inspect by authority/relevance
```

Do not ask the user for internal slugs, folders, IDs, YAML shapes, or renderer files.

Every material source/instruction gets one stable `SRC-###` entry. Roles are:

- `authoritative` — defines current project facts/requirements;
- `supporting` — supplements authoritative evidence;
- `reference` — demonstrates structure/quality only unless explicitly adopted;
- `generated` — prior generated output for continuity/conflict evidence only.

### Retention rule

Repository source copies are **useful evidence, not a ceremonial requirement**.

- Keep a supplied original under `source/originals/` when later direct inspection/reproduction materially benefits from having the bytes in-repo.
- A large/static source may remain externally retained when duplicating it adds no production value. Record enough exact identity/provenance in `source-inventory.yaml` to avoid ambiguity; for a file source, normally include filename and SHA-256 when available, plus `retention: external`.
- External retention is valid only after relevant source meaning has been inspected to sufficient depth and current production meaning is persisted through requirement/canonical state. It is not permission to discard unread authority.
- Never replace source identity with a generated review artifact.

### Reading depth

Read by **material relevance**, not by file count or bytes consumed.

```yaml
inspection: full
```

means no uninspected portion is expected to materially change current scope.

```yaml
inspection: targeted
inspection_scope: Objective 2 timing and reset behavior
```

is valid for bounded work.

A material user instruction is authoritative even without a file. Persist coherent instruction sets as source entries instead of relying on chat history or creating fake source files.

Use source-level `status: superseded` only when the whole source is no longer current. Partial changes are resolved at requirement/claim level.

## 2. Recover requirement truth

Recover explicit facts, rules, exclusions, removals, topology, terminology, and necessary production implications before filling gaps.

Negative statements are first-class requirements:

```text
remove
no longer use
do not use
only
must not
replaced by
```

Do not broaden them beyond their actual scope.

Create one `REQ-###` per meaningful production rule/constraint/conflict/exclusion/topology rule/proposed decision that must survive into project documentation/acceptance. Do not mirror every source sentence.

Normal source-backed requirement:

```yaml
id: REQ-001
area: gameplay
statement: Player must cross the bridge before collapse.
provenance: [SRC-001]
impact: high
```

Material AI proposal before approval:

```yaml
id: REQ-014
area: gameplay
statement: The first target appears after 90 seconds of free experimentation.
recovery_class: proposal
approval_status: pending
resolution: Recommended preview default; preserves experiment-before-explanation.
provenance: [SRC-002, SRC-003]
impact: high
```

Sparse defaults stay implicit unless a non-default condition matters. Use `affects` only when it materially helps cross-role propagation.

### Requirement meaning vs implementation evidence

Apply the durable PRD-scope boundary from `docs/foundation/02-source-intake-recovery.md` while recovering technical or completed-map sources. Do not assume that a detail belongs in the PRD merely because it is precise, executable, or present in authoritative implementation output.

Use this judgment:

```text
Does the detail define required gameplay, build, production, or observable system behavior?
→ recover the requirement.

Is it an explicit approved technical constraint that production must obey?
→ recover it at PRD abstraction level.

Does it only show how one finished implementation happened to realize the requirement?
→ retain it as source evidence; recover the underlying production meaning when material;
  do not promote the incidental identifier/setup itself.

Is it an exact world coordinate or map-instance locator?
→ do not create a canonical PRD requirement for the locator;
  preserve the supported spatial intent instead.
```

Spatial intent is still production meaning. Keep approved dimensions, area relationships, route/boundary requirements, relative or functional placement, visibility/readability, checkpoint role, and gameplay function. `30×30 block arena`, `control machine centered in the chamber`, or `exit visible from the objective area` may be legitimate requirements. A final `X/Y/Z` spawn, teleport, trigger, checkpoint, ticking-area, or authored bounding coordinate is not canonical PRD content.

Likewise, do not treat technical vocabulary as automatically invalid. `Must run in Minecraft Education Edition` or `must reuse the existing shared state interface because another approved system depends on it` can be legitimate constraints. By contrast, a scoreboard name, tag, function path, runtime ID, UUID, or pack/file identifier observed only in an existing implementation stays evidence rather than becoming product meaning.

Do not add a requirement-state taxonomy, keyword blacklist, coordinate detector, or compatibility framework for this distinction. The decision follows authority and meaning. If the user explicitly requests a separate as-built/technical setup artifact, handle that as a different requested deliverable rather than expanding the canonical PRD silently.

### Topology and terminology

Before preview, the model must be able to explain as applicable:

```text
project experience
├── shared/global rules
├── ordered gameplay packages/stages
├── dependencies/transitions
└── ending/final result or handoff
```

Store material topology as normal requirements; do not create another topology artifact.

Normalize names when variants may refer to the same concept. Preserve distinctions when they are real; when ambiguity is material and authority cannot settle it, choose a coherent Proposal for preview instead of synonym-cycling.

## 3. One integrated production-completeness pass

After explicit recovery, run **one reasoning pass**, not separate forms/reviews.

| Concern | Must be clear when applicable |
|---|---|
| Topology | package order, shared/local ownership, dependencies, transitions, ending/final result |
| Gameplay | purpose/objective, start, player action/feedback, completion/end, fail/retry/recovery, result |
| Level Design | required areas/objects/routes, relationships, readability, known spatial constraints, gameplay function |
| Developer | activation, state/progression, timing/quantities, validation, data/result, interruption/reset, handoff |
| Production Assets | concrete `MODEL`, `ITEM`, `UI / TEXT`, standalone `AUDIO`, and standalone `PARTICLE` resources that the approved experience actually requires; shared vs local ownership; exact player-facing copy when known |
| Lifecycle | precondition → trigger → active behavior → success/fail/interruption → result → retry/reset |
| Quantitative coherence | related timings/counts/capacities/scoring inputs/weights agree |
| Global/local coherence | shared defaults remain shared; local exceptions are explicit |
| Known constraints | authoritative platform/production limits do not silently conflict with required behavior |
| Operational clarity | competent roles should not reasonably build materially different behavior from the approved model |

Only inspect concerns that apply. Optional/decorative detail is not a reason to inflate scope.

The Production Assets concern is a **meaning check, not a new Flow or artifact**. If accepted gameplay necessarily needs a concrete resource, the model should not leave that production need invisible merely because the source did not name an asset file. Do not invent visual style, lore, dimensions, animations, VFX, sound, or presentation beats simply to fill 04.

If choosing a particular asset form/name/content would materially change gameplay, lore, communication, or scope, use the existing Completion/Proposal rules. Obvious production implications do not require another approval framework. `../production-assets/CONTRACT.md` later materializes the approved resource needs into the compact reader-first 04 source.

### Golden-guided completeness

Use the **Reverse-derived Golden fill map** in `../document/CONTENT-CONTRACT.md` as the finite guide for what the final PRD core must be able to answer.

Golden supplies **questions, placement, hierarchy, and presentation behavior**. It never supplies project mechanics, counts, lore, timings, scoring values, implementation facts, or asset style for another project.

When authority does not answer a material Golden-required question, do not leave the future slot empty merely because source is incomplete. Resolve it through authority, Completion, concrete Proposal, Explicit No / Not Applicable where truthful, or Blocked as the last resort.

### Mature-source consistency

A polished or `FINAL` source can still contradict itself. Compare only repeated **material** claims across relevant Gameplay Flow / Gameplay Overview / Level Design / Developer surfaces: progression count, triggers/timing, state change, fail/retry/recovery, scoring/result, reward/handoff, interruption/reset, and similarly consequential rules.

If same-authority surfaces materially disagree:

1. record the conflict internally;
2. preserve constraints/user direction that still hold;
3. select one coherent recommended preview resolution;
4. mark it Proposal + pending;
5. propagate it across the preview model.

Do not silently call the selected side source truth.

## 4. Resolution ladder

For every material gap/conflict:

```text
1. Existing authority resolves it
   → recover.

2. One necessary evidence-backed result exists
   → Completion.

3. AI must choose among plausible product/design/development answers
   → one concrete Proposal that best fits project intent/constraints.

4. Options are genuinely balanced
   → still choose one reasonable preview default as Proposal;
      mention an alternative only when it materially helps review.

5. Golden requires a material answer but source is silent
   → practical project-consistent Proposal at PRD abstraction level.

6. No responsible proposal can be formed
   → Blocked/direct decision.
```

### Completion vs Proposal

Use Completion only when the result follows from evidence/necessary implication and does not select among plausible product/design options.

Use Proposal whenever the AI actually chooses a material default, including gameplay behavior, quantities, timings, recovery, scoring behavior, names, objects, build expectations, runtime behavior, implementation rules, or a Production Asset choice that changes project meaning.

The objective is **not to minimize AI decisions**. The objective is to give the user a coherent complete model to approve/correct without pretending unsupported choices are source facts.

### Materiality

A gap is material when leaving it unresolved would force production to choose product behavior/scope or would change player experience, build scope, runtime behavior, scoring/result, timing, transition/handoff, interruption, reset, or another approved project fact.

Optional advisory improvements remain out of the preview by default.

## 5. Propagate meaning once

Every recovered Completion or Proposal must update all actually affected model surfaces:

```text
requirement
→ topology / shared-vs-local ownership
→ Gameplay
→ Level Design
→ Developer
→ Production Asset implications
→ timing / quantities / scoring
→ transition / handoff
→ retry / interruption / reset
```

Production Asset implications remain resource meaning only. Do not move runtime logic from Developer into 04 and do not turn logic into fake SEQUENCE assets.

Reuse existing REQs + `affects` where useful. Do not build a dependency-graph artifact.

Before approval, Proposal stays pending. After the user approves the relevant preview, promote represented pending proposals to approved project decisions/requirement state unless explicitly corrected/rejected.

## 6. Simple Chat Preview and user approval

After the model is complete enough to review coherently, show one objective-based preview before initial readiness.

Default form:

```text
Project Overview
<short project/session/journey summary>

Objective N — <Name>

Tujuan
<what the player must accomplish>

Apa yang Player Lakukan
- chronological player actions / visible responses

Hasil
<completion/result/transition>

Level Design
- material build-owned meaning

Developer
- material runtime/data/reset meaning

Saran AI                 # required when material AI-chosen Proposals exist
- each material AI-chosen default once; omit only when none exist
```

Use one short Global Rules block only when shared rules materially affect all objectives.

Do not expose `SRC-###`, `REQ-###`, YAML, provenance jargon, Golden DOM terms, validator detail, or a long Production Asset inventory by default. **do not turn the preview into a second PRD**; it should remain a compact checkpoint over the complete underlying model.

Every **material AI-chosen Proposal** must be disclosed once in `Saran AI` before approval. This includes chosen timing, quantity, progression, scoring, fail/recovery, reward, build-scope, runtime-behavior defaults, or material Production Asset choices. Source-backed recovery and non-material production implications do not need individual labels. Keep one compact disclosure list rather than a multi-question decision dialog.

`Perlu Konfirmasi` is the exception for a genuinely user/external-only blocker, not the normal response to incomplete design.

### Approval behavior

Before approval:

```yaml
status: audit_in_progress
ready_for_prd: false
preview_approved: false
next_step: Present/resolve the complete Simple Chat Preview.
```

After approval and proposal promotion:

```yaml
status: ready_for_prd
ready_for_prd: true
preview_approved: true
```

A Flow-2-specific `next_step` may be omitted once another persisted owner (`content.md`, handoff state, or repository `next-action.md`) clearly owns later continuation; do not preserve stale instructions such as “Build canonical PRD content” after handoff is already complete.

Natural-language user approval is sufficient. A material Proposal counts as represented by the preview only when its chosen default appears once in `Saran AI`; do not promote a hidden material AI choice through blanket approval. If the user corrects the preview, persist the correction as higher authority, update only affected proposal/requirements, rerun only invalidated reasoning, and re-preview only the affected slice when needed.

## 7. Readiness

Statuses remain:

```text
collecting_sources
audit_in_progress
needs_decision
blocked
ready_for_prd
```

`ready_for_prd` requires:

- materially relevant authority inspected to sufficient depth;
- material user instructions persisted;
- facts/exclusions/topology/terminology recovered;
- applicable Gameplay / Level Design / Developer / Production Assets / lifecycle / quantitative / global-local / known-constraint implications resolved;
- each material issue passed through the Resolution Ladder;
- every Proposal represented in the approved preview has been promoted/corrected;
- no current `approval_status: pending`, `recovery_class: blocked`, or current source `inspection: blocked` affecting scope;
- the complete initial Simple Chat Preview (or bounded affected slice) is approved.

`state/source-inventory.yaml` and `state/requirement-register.yaml` must contain real stable evidence entries before repository-backed validation can trust positive readiness.

## 8. Bounded revision

```text
approved change
→ update affected authority/requirement meaning
→ completeness check only on invalidated slice
→ new Proposal only if the change opens a material gap
→ affected preview only when interpretation changed
→ approval/correction
→ continue downstream revision
```

If the current user instruction already states the complete bounded result unambiguously, it may serve as approval for that slice. Do not manufacture another confirmation step.

## Stop rule

Stop Flow 2 when the approved model is production-complete for current scope. Do not continue generating optional redesign ideas, extra artifacts, additional proof layers, or speculative hardening after readiness is established.