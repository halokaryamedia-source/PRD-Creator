# PRD Validation & Team Handoff

Flow 4 decides whether a generated PRD is actually usable by the production team. Rendering success is necessary but not sufficient.

## Status model

Use exactly one current PRD status in `state/handoff-state.yaml`:

- `pending_review` — Flow 3 output exists but Flow 4 audit is incomplete;
- `needs_revision` — one or more Critical/Major findings remain;
- `development_ready` — mechanical checks pass and all four semantic perspectives pass with Critical=0 and Major=0;
- `handoff_ready` — `development_ready` plus `output/team-handoff.md` exists and points the team to the accepted PRD;
- `blocked` — required artifacts/evidence are unavailable or a required upstream decision must return to Flow 2.

`handoff_ready` means the documentation is ready for production use. It does **not** mean client sign-off, release approval, or implementation completion.

## Required inputs

Audit the same current revision of:

- `state/requirement-register.yaml` — traceability / unresolved requirement state;
- `work/content.md` — canonical PRD meaning;
- `work/render-data.json` — derived rendering projection;
- `output/final.html` — rendered presentation.

Do not audit an old HTML file against newer canonical content.

## Step 1 — Mechanical validation

Run:

```bash
python kits/project-document-generator/validator/validate.py \
  workspace/active/<project>/
```

This check covers file presence, visible placeholders, render-data invariants, package role objects, scoring/completion exclusivity, numeric scoring weights, expected generated pages, duplicate HTML IDs, navigation reachability, and project browser title.

Mechanical `pass` is structural evidence only. It cannot issue `development_ready` by itself.

## Step 2 — Four-perspective semantic audit

### A. New Reader / Player Context

Assume the reviewer reads Overview + Gameplay Flow + the relevant Gameplay Overview page only.

They must be able to answer without guessing:

- What is this project / experience?
- What is the player/user role?
- What happens in what order?
- What starts this package?
- What counts as valid completion?
- What can fail, block, or retry?
- What result/handoff continues forward?
- Are project-specific terms understandable where first needed?

### B. Level Designer

Assume the level designer reads Gameplay Overview → Level Design for an assigned package.

They must be able to begin blockout/build work without inventing the main production requirements:

- required areas, objects, landmarks, routes, or relationships;
- entry, exit, return, or handoff path where relevant;
- build order / level-design flow;
- material dimensions and quantities where gameplay depends on them;
- visual/build requirement separated from gameplay function;
- interaction space/readability needed by the mechanic;
- package-local constraints that differ from global rules.

Do not require cosmetic dimensions that do not affect production.

### C. Developer

Assume the developer reads Gameplay Overview → Level Design → Developer plus relevant Global Development pages.

They must be able to form an implementation plan without inventing product rules:

- activation/start trigger;
- progression/state transitions;
- valid completion validation;
- quantities/items/resources/state ownership;
- timer start/stop/excluded time when applicable;
- scoring **or** completion-data behavior;
- recorded/persistent data where applicable;
- duplicate prevention;
- interruption/disconnect behavior when relevant;
- reset behavior;
- handoff/result to the next package;
- verification/acceptance behavior.

Implementation architecture, class names, file names, or APIs are required only when explicitly part of the approved project scope.

### D. Project Consistency

Compare Overview, Gameplay Flow, Global Development, all package pages, scoring/completion, reset, and handoffs.

Different wording is allowed. Different meaning is not.

Check especially:

- official names and terminology;
- package order / progression;
- player/session/arena counts;
- quantities and important dimensions;
- start/end/fail/retry conditions;
- timer boundaries;
- score components/weights/inputs;
- recorded data and ownership;
- handoff items/state/results;
- interruption/disconnect/reset behavior;
- final-result relationship.

## Severity

- **Critical** — can produce incorrect gameplay, scoring, data, build, ownership, reset, or implementation behavior.
- **Major** — required information is missing/contradictory enough that the role would need to invent a product decision.
- **Minor** — meaning is implementable but local clarity/consistency can improve without changing the product rule.
- **Suggestion** — optional polish; never blocks readiness.

Critical and Major always block `development_ready`.

A Minor may remain only when it does not change meaning, its owner/location is recorded, and leaving it open is intentional.

## Finding ownership

Classify the root owner before fixing:

- project meaning / requirement defect → fix `work/content.md` (and upstream requirement/decision state when needed), regenerate render-data, rerender;
- derived projection defect → regenerate/fix `work/render-data.json` from canonical content;
- renderer/template presentation defect → fix active renderer/template, then rerender;
- unresolved product decision → return the requirement to Flow 2; do not solve it during audit.

Never patch `final.html` as the source of truth.

## Acceptance record

Create/update `work/acceptance.md` with:

```text
# PRD Acceptance

Status: needs_revision | development_ready | handoff_ready
Reviewed revision: <content/html version or commit/reference>

## Mechanical Validation
PASS / FAIL + concise evidence

## New Reader
PASS / FAIL + findings

## Level Designer
PASS / FAIL + findings

## Developer
PASS / FAIL + findings

## Project Consistency
PASS / FAIL + findings

## Findings
ID | Severity | Owner | Location | Finding | Resolution Status

## Gate
Critical: N
Major: N
Minor: N
Result: ...
```

Keep this report concise. Do not duplicate the PRD inside the audit.

## Handoff state

Maintain `state/handoff-state.yaml`:

```yaml
flow: 4
status: handoff_ready
content: work/content.md
render_data: work/render-data.json
html: output/final.html
acceptance: work/acceptance.md
handoff: output/team-handoff.md
mechanical: passed
perspectives:
  new_reader: passed
  level_designer: passed
  developer: passed
  project_consistency: passed
findings:
  critical: 0
  major: 0
  minor: 0
next_step: flow_5_voice_requirement_extraction
```

Use project-relative paths. Do not store chat-only claims in the state.

## Team handoff

After the gate passes, create `output/team-handoff.md` as a navigation aid, not a second PRD.

It should contain only:

- project / accepted PRD version or revision;
- canonical PRD path and rendered HTML path;
- short project purpose / current production scope;
- recommended reading route for Level Designer and Developer;
- package/stage inventory;
- genuinely global systems that affect multiple packages;
- accepted Minor findings or explicit non-blocking caveats, if any;
- statement that Critical=0 / Major=0 at the accepted revision.

Do not copy every requirement into the handoff file.

## Development-ready gate

Set `development_ready` only when:

- mechanical validation passes;
- New Reader perspective passes;
- Level Designer perspective passes;
- Developer perspective passes;
- Project Consistency passes;
- Critical findings = 0;
- Major findings = 0;
- no unresolved Proposal/Blocked requirement affects the handed-off scope;
- scoring/completion and handoff/reset behavior are implementable where relevant;
- requested language coverage is usable for the intended team.

Then create the concise team handoff and set `handoff_ready`.

## Revisions after handoff

If canonical meaning changes after `handoff_ready`:

```text
change approved
→ update requirement/decision owner when needed
→ update content.md
→ regenerate render-data.json
→ rerender final.html
→ reopen Flow 4 status to pending_review
→ re-audit affected dependencies
→ issue updated handoff
```

Do not silently keep an old `handoff_ready` status against a newer PRD revision.
