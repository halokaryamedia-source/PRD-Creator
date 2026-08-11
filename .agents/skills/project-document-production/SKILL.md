---
name: project-document-production
description: Semantic/product-contract owner for PRD-Creator Flow 2–4. Use for source recovery, canonical PRD meaning, Golden representation requirements, PRD readiness, and handoff semantics. Do not use as a generic HTML/Python wrapper when semantics are already correct.
---

# Project Document Production

Own Flow 2–4 semantic judgment. Detailed production procedure/mechanics stay in `kits/project-document-generator/`.

## Use when

- uneven source must become reliable production requirements;
- missing project meaning must be safely recovered before drafting;
- canonical `work/content.md` meaning is created/corrected;
- Golden hierarchy/page-composition requirements are defined/corrected;
- PRD development-readiness or handoff meaning is decided.

If semantics are already correct and the defect is renderer/template/validator mechanics, route directly to the nearest kit implementation owner.

## Authority chain

```text
originals + persisted user instructions + approved decisions
→ requirement state
→ content.md (canonical)
→ render-data.json (derived)
→ final.html (derived)
→ acceptance/handoff evidence
```

Generated output never becomes project authority. Rendering/prose may organize approved meaning but may not invent mechanics, quantities, lore, scoring, triggers, architecture, or unresolved decisions.

## Smallest semantic owner

- Flow 2 recovery/readiness/problem-solving → `SOURCE-INTAKE.md`
- Flow 3 content meaning → `CONTENT-CONTRACT.md`
- Flow 3 projection meaning → `RENDERING.md` only when projection/HTML behavior is actually in scope
- Flow 4 readiness → `VALIDATION.md`

`WORKFLOW.md` is sequencing reference only. Read the smallest owner required by the active problem.

## Flow 2 judgment

Flow 2 is not just provenance/extraction. Before `ready_for_prd`, it must recover enough production meaning that Flow 3 does not have to invent project structure or required role behavior, and it should help resolve material gaps before pushing decisions back to the user.

Apply this order:

```text
source authority + inspection
→ explicit facts/rules/exclusions
→ project topology + terminology
→ cross-role implications
→ production coverage
→ lifecycle + quantitative + operational clarity
→ global/local coherence + known-constraint feasibility
→ problem framing
→ Resolution Ladder
→ impact propagation
→ humanized grouped decision package only if needed
```

Key boundaries:

- material user instructions are persisted even without a file;
- source-level supersession is used only when the whole source is replaced;
- negative constraints/removals are first-class requirements;
- **do not over-broaden a negative statement**: `do not display score`, `do not export score`, and `this package has no Objective Score` are three different requirements unless authority explicitly connects them;
- for every gameplay package, recover the **Scoring / Result contract** that authority actually defines: internal Objective Score when one exists, or explicit `No Objective Score` when it does not; also recover player-facing display behavior, telemetry/export behavior, completion result, and relationship to final result when those concerns are material;
- never infer `No Objective Score` merely because player-facing scores/results are hidden or raw telemetry excludes scores;
- when current approved project decisions and an older/source-labelled `FINAL` artifact disagree, resolve through the normal authority chain; a filename/status label alone does not silently override a higher-authority current decision;
- Completion requires one reliable evidence-backed result at the needed abstraction;
- a missing detail is material only when a downstream role would otherwise have to choose product behavior/scope;
- relevant Gameplay / Level Design / Developer implications are recovered when logically required, without inventing implementation choices;
- related numbers/timings/counts/scoring facts are checked for direct contradictions before drafting;
- vague wording is resolved only when it would create materially different production outcomes; qualitative intent is not forced into fake metrics;
- shared/global defaults and local exceptions must be explicit and mutually coherent;
- authoritative known platform/project constraints are checked without turning generic best practice into authority;
- each material issue is framed and taken through the least-assumptive Resolution Ladder before asking the user;
- use `Recommended` only when evidence/goals/constraints genuinely favor one option; balanced tradeoffs must be presented honestly;
- one recovered/approved resolution is propagated to all actually affected requirements instead of being fixed in only one section;
- related decisions are grouped only when one root resolution genuinely controls them;
- irrelevant/optional detail remains open instead of being filled for completeness;
- once production-ready, stop generating optional redesign ideas.

### Humanized user communication

Flow 2 user-facing decision/recovery explanations should use clear plain production language, normally:

```text
Masalah → Saran → Kenapa → Dampak → Alternatif (only if useful)
```

When there is no clear recommended default, use a concise `Pilihan` + tradeoff explanation instead of inventing confidence.

This Humanize behavior changes presentation only. It must not change official terminology, numbers, timing, formulas, mechanics, triggers, uncertainty, provenance, or approval state. Do not expose internal `SRC/REQ`/YAML/recovery jargon unless requested or needed to explain a blocker.

## Flow 3 judgment

Use **minimum complete production detail**, not minimum-looking output. Preserve every material fact a production role needs while removing only useless repetition, filler, and duplicate wording.

The approved Golden Sample is a **functional quality floor**, not only a section skeleton. A new PRD does not copy Golden project facts, counts, or wording, but each corresponding surface must do the same job for its reader:

- Gameplay Flow makes the chronological player experience understandable in context;
- Gameplay Overview explains the package before implementation detail;
- Level Design carries the complete build-relevant meaning for the package;
- Developer carries the complete runtime/state/scoring-or-result/data/interruption/reset/handoff meaning that applies;
- Global Development keeps shared ownership visible instead of compressing important cross-package behavior into vague references.

### Gameplay Flow is the player story

Gameplay Flow is not a developer checklist or a three-step task summary. Write it as concise production narrative following the player through the experience:

```text
where the player comes from / current context
→ what the player sees or understands
→ instruction / NPC / system cue when relevant
→ what the player does
→ how the world/system responds
→ what changes because of that action
→ what the player carries/knows into the next beat
→ result and forward transition
```

Use enough beats to preserve the actual experience. Keep it production-readable rather than novelistic; do not invent dialogue, lore, animation, feedback, or mechanics that authority does not support.

### Development completeness

Do not compress a detailed source into a few generic rows merely because a Golden table exists. For each package, preserve all material role-owned meaning:

- **Level Design** — required spaces, objects, routes/relationships, readability/sightlines, known size constraints, safe/recovery areas, interaction placement, boundaries, visual requirements, gameplay function, and important build notes when supported/relevant;
- **Developer** — activation/preconditions, progression/state, interaction rules, quantities/timing, completion, Objective Score or explicit `No Objective Score`, score/result relationship, player-facing display rules, data/export rules, interruption/disconnect, retry/reset, transition/handoff, and important implementation notes when supported/relevant.

A shared/global rule may be referenced rather than repeated, but the local page must still make clear **which shared rule applies and what local behavior depends on it**. “See global rules” is not sufficient when a role would have to search the source to know what to implement.

### Scoring / Result is always explicit

Every gameplay package must state its result model:

```text
Scored package
→ Objective Score + applicable scale/components/weights/timer/no-score condition/result relationship

Non-scored package
→ No Objective Score + valid completion/result + relationship to final result
```

Keep separate when source distinguishes them:

```text
internal scoring/result
player-facing score/result display
telemetry/export payload
```

Hiding a score from the player or excluding score from telemetry does not erase the internal score.

### Humanize the PRD, not the facts

After meaning is complete and before projection, apply one bounded Humanize pass to narrative/explanatory prose:

- prefer natural production sentences over comma-stacked database prose;
- explain cause → action → response → consequence in readable order;
- give context before technical detail;
- keep paragraphs short enough to scan but complete enough to understand;
- keep official terms stable;
- leave tables, formulas, IDs, coordinates, timings, weights, state names, and exact technical values precise;
- do not make prose promotional, theatrical, vague, or longer merely to sound human.

If drafting discovers a material topology, terminology, exclusion, lifecycle, quantitative, operational-clarity, global/local, feasibility, cross-role, scoring/result, or product-decision gap that Flow 2 should have resolved, return that requirement upstream rather than hiding it with polished wording or HTML.

## Context economy

Normal production should not load the full Golden template or generated HTML source into model context. Use canonical content for meaning, validator/runtime for full-file mechanics, and actual rendered/browser inspection for visual claims. Inspect HTML source only for a concrete bounded defect. Do not reread unchanged source/packages during bounded revisions.

Context economy applies to **reading work**, not to deleting material production meaning from the final PRD.

## Acceptance judgment

Assess the current revision once through these lenses:

- New Reader / Player Context;
- Level Designer;
- Developer;
- Project Consistency.

A single reading slice may satisfy several lenses; do not reread the same package four times. Critical/Major findings block readiness.

The semantic review must also perform a bounded **source/requirement → PRD coverage check** for material/high-impact meaning. It is not a new matrix artifact or mechanical validator. Ask whether the PRD carries the important source meaning into the correct reader surface, not merely whether each page looks plausible.

Before reporting ready, confirm:

- a new reader can understand the chronological player journey without reopening the original source;
- Level Design can build the package from its page + clearly referenced shared rules without inventing material behavior;
- Developer can implement lifecycle/state, scoring or explicit `No Objective Score`, data/display/export distinctions, interruption/reset, and result/handoff without reopening the original source for missing material rules;
- material project meaning is supported and traceable;
- no unresolved material decision is hidden;
- canonical meaning and derived representation materially agree;
- Golden structure **and functional depth** are preserved without copying Golden-specific project facts;
- prose is human-readable production language rather than compressed database-like text;
- visual/runtime claims do not exceed evidence.

If a production role must reopen the source to discover a material requirement that should have been in the PRD, treat that as a **Major** completeness finding, not acceptable concision.

## Boundary

This skill owns PRD Flow 2–4 semantic/product contract only. Voice remains downstream. Never patch `final.html` as source of truth.
