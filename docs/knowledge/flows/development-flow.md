# Development Flow

Updated: 2026-08-10

This is the end-to-end path for **repository/system Developing** work in PRD-Creator.

Normal project Production Execution (for example creating or revising a PRD from project source) does **not** use this flow. It routes directly to the matching production owner/kit.

```text
User asks to change PRD-Creator itself
→ development-brief
→ goal/method/reference/authority grounded
→ development needed?
   ├─ no → explain/reuse + minimum proof
   └─ yes
      → at most one semantic specialist when useful
      → smallest complete implementation
      → minimum useful proof
      → Acceptance POV check
      → evidence-status check if material uncertainty remains
      → update repository state
```

## Development Brief

`development-brief` is mandatory before non-trivial repository/system implementation. Its canonical procedure lives in `.agents/skills/development-brief/SKILL.md`.

The user does not need to provide an expert prompt. The brief establishes:

- real goal;
- suggested method vs actual requirement;
- sample/reference vs generic requirement;
- authoritative input;
- expected output;
- execution channel;
- Build POV;
- Acceptance POV;
- minimal scope and out-of-scope boundary;
- 2–5 acceptance criteria;
- proof budget.

A proposed method is not automatically a requirement. Reject or redirect it when current evidence shows it is unsupported, contradicts accepted project meaning, repeats a failed approach, reduces downstream usability, or adds unnecessary parallel architecture.

## Development Necessity

Inspect existing behavior before inventing work.

`No change required` is a valid result when current behavior already satisfies the goal.

Do not create a new skill, schema, compatibility layer, renderer abstraction, validation report, or project state file merely because it could be useful later.

## Specialist Boundary

Use `development-brief` alone when another skill adds no material domain value.

Otherwise choose exactly one semantic specialist for the **system contract being changed**:

```text
Project Document Flow 2–4 system/policy
→ project-document-production

Voice Production Flow 5–7 system/policy
→ voice-production
```

Do not stack both because the final project pipeline contains both. Select the owner of the active system change.

If a PRD system change later invalidates Voice behavior, finish the upstream correction and explicitly mark downstream behavior for revalidation rather than keeping both specialists active at once.

## Execution Channel

### ChatGPT → GitHub

Prepare repository/source/artifact changes as far as static evidence allows.

Do not claim:

- browser interaction success without browser proof;
- generated-audio quality without actual audio;
- local runtime success without the corresponding runtime check.

When a material claim remains unproven, leave the exact local proof required.

### Local / Codex-style

Use the same brief and acceptance criteria. Run the smallest local check that can prove/disprove the remaining claim. Do not restart planning or run broad suites merely because a shell is available.

## Implementation

Before editing:

1. inspect the canonical owner;
2. inspect directly affected state/contract/caller/artifact path;
3. establish root cause when correcting behavior;
4. confirm the change remains inside the brief.

Then:

- make the smallest complete change;
- preserve valid behavior outside scope;
- never promote a project/reference-specific detail to generic policy without an explicit requirement;
- update derived artifacts only from their canonical owners.

## Dual Validation

### Build Pass

Check whether the semantic owner produced the intended system change correctly.

Examples:

- Flow 2 requirement/provenance recovery contract is internally consistent;
- Flow 3 canonical content/render projection contract agrees materially;
- Flow 6 exact Voice ID/Type parity remains intact;
- builder/validator changes pass the targeted mechanical check.

### Acceptance Pass

Re-check the original `development-brief` from the downstream Acceptance POV:

- does the result solve the actual user/team need?
- is the output usable without hidden assumptions?
- did scope remain inside the brief?
- does the claimed status match actual evidence?

Build PASS without Acceptance PASS is not completion.

## Evidence Escalation

Use root evidence labels only when a material claim remains uncertain:

- `CURRENT-PROJECT VERIFIED`;
- `AUTHORITATIVE-SOURCE VERIFIED`;
- `LOCAL PROOF REQUIRED`;
- `UNSUPPORTED`;
- `UNKNOWN`.

Routine edits with clear proof do not need ceremonial labeling.

## Repository Continuity

Do not create a planning note per task.

Update only the canonical owner:

- active goal/status/blocker/proof/next step → `docs/knowledge/next-action.md`;
- durable decision/reason → `docs/knowledge/decision-log.md`;
- stable production policy → `docs/foundation/` only when policy itself changes;
- skill inventory/routing → `docs/knowledge/skills/` only when skill architecture changes;
- detailed Flow procedure → affected kit/foundation owner.

## User Reporting

For material repository/system implementation:

```text
Status:
Hasil:
Bukti:
Batasan:
Next step:
```

Distinguish implemented from verified when material proof is still pending.

## Parent

- [Agent Routing Flow](../flow.md)
- [Skill Activation Matrix](../skills/activation-matrix.md)
- [Knowledge Dashboard](../index.md)
