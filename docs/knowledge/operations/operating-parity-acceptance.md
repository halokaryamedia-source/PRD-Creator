# Operating Parity Acceptance — Phase 3

Updated: 2026-08-10
Status: `ACCEPTANCE_IN_PROGRESS`

## Purpose

Exercise the Phase 1–2 operating architecture as a real repository workflow rather than accepting documentation existence as proof.

This acceptance does not re-run product Flow 2–7. It validates agent routing, Maintenance ownership, local-owner rules, navigation/ownership consistency, and whether a small automated engineering gate is justified.

## Representative Routing Runs

### Scenario A — New project from incomplete source

Result: **PASS — routing contract**.

Route exercised:

```text
boot owners already current
→ development-brief
→ activation matrix
→ project-document-production
→ Flow 2 SOURCE-INTAKE + project originals/state
```

Observed:

- semantic owner identified without scanning Voice/reference/history;
- exactly one specialist is sufficient;
- project facts still originate upstream, not from rendering;
- no user-context reconstruction is required.

### Scenario B — PRD content / rendering change

Result: **PASS — routing contract**.

```text
Developing change
→ development-brief
→ project-document-production
→ canonical content first
→ RENDERING/template only when projection/presentation is affected
```

A renderer/file-format mention does not create another specialist.

### Scenario C — Voice scope / script change

Result: **PASS — routing contract**.

```text
Developing change
→ development-brief
→ voice-production
→ current accepted PRD / voice-state
→ Flow 5, 6, or 7 owner only
```

The route preserves the distinction between Voice scope, performance wording, derived DOCX, and optional audio evidence.

### Scenario D — Maintenance / routing defect

Result: **REAL DEFECT FOUND + ROOT FIX PREPARED**.

Observed defect:

`kits/project-document-generator/SKILL.md` required a broad fixed reading sequence (`GLOSSARY → RULES → SOURCE-INTAKE → CONTENT-CONTRACT → RENDERING → VALIDATION → WORKFLOW`) even when only one Flow was active.

Why this is a defect:

- contradicts root minimal-navigation policy;
- conflicts with `project-document-production`, which says to read only the smallest relevant kit procedure/source;
- increases context without improving correctness;
- makes Flow 2/3/4 boundaries less explicit.

Root correction:

- add nearest `kits/project-document-generator/AGENTS.md` with Flow-local routing;
- change Project Document `SKILL.md` to Flow-first reading;
- preserve every production semantic/authority rule.

This is the required real Maintenance exercise for Phase 3.

## Nearest `AGENTS.md` Decision

**Project Document Generator: ADD.**

Reason: it contains three materially different Flow boundaries plus renderer/template/validator implementation surfaces. A nearest agent file provides local routing/edit discipline even when a root specialist is not loaded.

**Voice Production Kit: KEEP.**

Its existing nearest `AGENTS.md` already provides concise Flow 5/6/7 routing and acceptance boundaries. No additional local layer is needed.

Nearest `AGENTS.md` is not required for every directory. Add it only where scoped rules materially reduce ambiguity or unsafe broad reading.

## Navigation / Ownership Audit

Current owner graph is coherent:

```text
AGENTS
→ CONTEXT
→ next-action
→ module/source/implementation owner when needed
→ activation matrix only for skill selection
→ affected kit/project
```

Phase 3 adds automated relative-link verification so future stale navigation fails closed instead of depending only on manual review.

## Engineering Gate Decision

**Decision: a small automated gate is justified.**

Evidence:

1. the repository now depends on a frozen root-skill inventory and canonical owner paths;
2. Phase 3 found a real routing inconsistency after architecture changes;
3. production contains executable Python renderer/validator/builder code;
4. retired architecture must not silently return;
5. relative navigation is part of repository continuity.

Canonical gate:

```text
tools/verify_repository.py
.github/workflows/repository-verify.yml
```

The gate checks only stable, cheap invariants:

- required operating owners exist;
- canonical root skill set is exact;
- no nested duplicate repository skill root;
- retired `Production Document Builder/` stays absent;
- `next-action.md` keeps exactly one Next Step;
- relative Markdown navigation resolves;
- Python production sources are syntax-valid.

## Explicit Non-Claims

Repository Verify does **not** prove:

- PRD semantic correctness;
- HTML browser appearance;
- DOCX visual correctness;
- ElevenLabs/generated-audio quality;
- current-project Flow readiness.

Those retain their existing production-specific proof requirements.

## Final Acceptance Gate

Phase 3 can become `OPERATING_PARITY_ACCEPTED` when:

- representative routing scenarios are recorded;
- the real Maintenance defect is corrected;
- nearest-owner decision is recorded;
- navigation/ownership audit passes;
- Repository Verify is committed and its first `Local` workflow run passes.

Until that workflow result is observed, current status remains acceptance in progress.
