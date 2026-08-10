# Workflow

Project Document Generator uses three macro steps. Internal artifacts/checks support them; they are not user-facing approval stages.

```text
1. UNDERSTAND   — Flow 2
2. BUILD PRD    — Flow 3
3. REVIEW       — Flow 4
```

Normal user experience:

```text
project source
→ automatic project bootstrap
→ inspect/recover
→ one grouped decision review only if needed
→ build Golden-Sample PRD
→ review/fix
→ final accepted PRD
```

Normal PRD production is **Production Execution**, not repository Developing. `development-brief` is only for changing PRD-Creator itself.

## Automatic bootstrap

The agent derives/reuses the project workspace, preserves originals, creates only current-Flow state/work artifacts, and assigns internal IDs. Do not ask the user to manage slugs, folder names, source IDs, requirement IDs, or renderer files unless project identity is genuinely ambiguous.

---

## 1. UNDERSTAND — Flow 2

Follow `SOURCE-INTAKE.md`.

```text
inspect all available source
→ reconcile authority / duplicates
→ recover production-relevant requirements
→ apply safe Clarification / Completion
→ collect remaining high-impact Proposal / Blocked decisions
→ one grouped decision review when needed
```

When a decision needs approval, provide:

```text
Decision N — <topic>
Recommended: <option>
Reason: <short evidence-based reason>
Impact: <what changes>
```

The user may approve all recommendations or override only named exceptions. Recommendations remain Proposal until approved.

Do not force a human review artifact when no material decision/recovery summary is useful.

**Exit:** `ready_for_prd`, `needs_decision`, or `blocked` is truthful.

---

## 2. BUILD PRD — Flow 3

Read `CONTENT-CONTRACT.md` and produce canonical `work/content.md` from authoritative source, supported recovery, and approved decisions.

### Golden fidelity is part of BUILD

The approved Golden Sample defines **both hierarchy and page composition**.

Hierarchy:

```text
Overview
→ Gameplay Flow
→ Global Development
→ Gameplay Package(s)
     → Gameplay Overview
     → Level Design
     → Developer
```

Reusable composition:

```text
Gameplay Flow
→ narrative sequence / transition

Global Development
→ shared tabs
→ context block
→ flow cards
→ grouped requirements table
→ note cards

Gameplay Overview
→ title/subtitle + 1/2/3 tabs
→ Gameplay Context / Main Objective / Result
→ Gameplay Information table
→ role-sequence

Level Design
→ title/subtitle + tabs
→ context block
→ Design Flow cards
→ 5-column Golden Build Requirements table
→ note cards

Developer
→ title/subtitle + tabs
→ context block
→ Development Flow cards
→ grouped Golden Development Requirements table
   with scoring/completion/reset inside the hierarchy
→ note cards
```

A document that uses Golden CSS/JS but replaces these page families with generic cards/tables has **not** completed BUILD correctly.

Use minimum sufficient project detail inside this fixed composition. Do not invent content to fill visual space.

Internal rendering remains one BUILD operation:

```text
work/content.md
→ derive Golden-oriented work/render-data.json
→ renderer emits Golden component composition
→ approved Golden Sample template
→ output/final.html
```

If canonical drafting exposes a real unresolved product decision, return it to UNDERSTAND instead of guessing.

**Exit:** canonical meaning is complete and the current generated HTML represents the Golden composition without unresolved placeholders.

---

## 3. REVIEW — Flow 4

Read `VALIDATION.md`.

Run the current mechanical validator once for the finished revision. It checks normal artifact/navigation contracts **plus a small Golden composition marker set** so generic renderer output cannot silently pass.

Then perform one integrated review:

```text
mechanical + Golden composition markers
+ visual sanity when actual page/browser inspection is available
+ New Reader / Level Designer / Developer / Consistency
→ fix real findings
→ re-review only invalidated scope
```

Visual sanity checks the actual Golden result for broken composition/tabs, wrong footer identity, table overflow, broken grouped rows, score/completion placement, note/Terms behavior, density, and inspected responsive/print issues.

Do not add another Flow, visual score, pixel diff, screenshot baseline, AI-quality detector, or generic HTML schema.

**Exit:** mechanical/Golden composition checks pass, all semantic lenses pass, Critical=0, Major=0, and no material Proposal/Blocked item affects delivered scope. Visual claims require actual visual evidence.

## Revision fast path

For a bounded approved revision:

```text
approved change
→ affected requirement/content only
→ necessary cross-references
→ regenerate Golden projection / HTML
→ one current mechanical check
→ targeted semantic/visual re-review
→ updated final PRD
```

Do not replay unchanged source intake, resolved decisions, unrelated packages, or unaffected review evidence.

## Team handoff

Under the current canonical sequence, `output/team-handoff.md` remains a concise navigation aid and `handoff_ready` remains the downstream boundary. Do not copy the PRD into the handoff file.

## Default user-facing delivery

Show only:

```text
Final PRD: <output/final.html>

Main adjustments / recovered decisions:
- material items only

Needs attention:
- none OR real remaining decision/blocker
```

Internal state/YAML/IDs/render data/validator JSON/CI logs stay internal unless requested or needed to explain a blocker.

## Stop gate

Do not claim client sign-off, implementation completion, QA completion, release approval, Voice readiness, or Golden visual fidelity beyond actual evidence.
