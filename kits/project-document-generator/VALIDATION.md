# PRD Validation & Team Handoff

`CONTENT-CONTRACT.md` owns PRD meaning and Golden composition. This file owns the minimum proof needed to accept the current revision.

## Default sequence

```text
current PRD revision
→ one mechanical validation
→ one integrated semantic-readiness review
→ targeted desktop visual sanity when needed
→ fix the first wrong owner
→ development_ready | handoff_ready
```

Do not create separate review passes for New Reader, Level Design, Developer, Content Purity, Project Consistency, Acceptance, or Golden Fidelity. They are lenses inside one review, not independent workflow gates.

## 1. Mechanical validation

Run once after the current projection/render is complete:

```bash
python kits/project-document-generator/validator/validate.py \
  workspace/active/<project>/
```

Mechanical validation owns deterministic facts: Flow 2 readiness, required current artifacts, canonical/projection/render bindings, page order/IDs/navigation, scoring arithmetic, required Golden markers, and the narrow observed content-purity regression set.

Mechanical PASS does not prove source fidelity, semantic completeness, material conservation, or visual readability.

Content-purity checks stay narrow. They may reject concrete observed leakage such as generator/template/page narration, generic `Global Rule N`, or plain note strings that would render as generic `Important Note N`. Do not grow this into a prose score, word-count gate, or broad keyword blacklist.

## 2. Integrated semantic readiness

Review the current revision once. During that pass ask the relevant questions below; do not persist a PASS field for every lens.

| Lens | Ready when... |
|---|---|
| New Reader | journey, objective, result, setback/recovery, and transition are understandable without reopening source |
| Level Designer | build-owned areas, objects, relationships, constraints, and gameplay functions are sufficient |
| Developer | trigger/state/progression/timing/scoring/reset/handoff behavior is sufficient |
| Content Purity | visible project copy explains the project, not PRD-Creator or document-production mechanics |
| Project Consistency | terminology, timing, scoring, reset, and package handoff agree across the revision |
| Golden Placement | project meaning is placed in the matching approved Golden component family without unapproved presentation invention |

Record one result: `Semantic Readiness: PASS | FAIL`.

Return to Flow 2 only for a real unresolved project/design decision or authority conflict. Wording, placement, decomposition, and terminology corrections stay in the current semantic owner.

## 3. Material conservation

Material conservation remains a separate gate because a document can be clear yet accidentally omit an independent rule.

For changed or regenerated scope, verify that material conditions, values, exceptions, recovery rules, result behavior, and role-owned requirements still have an explicit readable representation. Do not use word count or row count as a proxy.

Record one result: `Material Conservation: PASS | FAIL`.

## 4. Golden reference economy

The approved Golden is already locked by `CONTENT-CONTRACT.md` and focused static regression coverage. Normal project production does **not** reread/re-prove the entire reference from scratch when the Golden/template/renderer composition is unchanged.

Re-run the reverse reference → contract proof only when the Golden artifact, template, visible page composition, or its semantic slot contract changes.

For ordinary content-only production, prove the forward direction only: current project meaning fills the existing approved contract correctly.

## 5. Targeted desktop visual sanity

Visual PASS requires actual rendered/browser evidence. Static HTML inspection cannot claim visual PASS.

For ordinary content-only work, inspect only representative/high-risk pages, normally:

```text
Overview
+ one Gameplay Flow
+ one Gameplay Overview
+ one Level Design
+ one dense Developer page
```

Check readable summary density, wrapping/overflow, component order, semantic note titles, table/list readability, and obvious material thinning.

Escalate to every-page or broader browser testing only when the template/CSS/JS/page-composition changed, a targeted finding suggests a global defect, a new component was approved, or the user explicitly asks for broader proof.

Do not routinely retest mobile, theme, localStorage, every link, or unrelated Voice behavior for a content-only revision.

## 6. Acceptance record

Keep `work/acceptance.md` compact:

```text
# PRD Acceptance
Status: needs_revision | development_ready | handoff_ready
Mechanical: PASS | FAIL
Semantic Readiness: PASS | FAIL
Material Conservation: PASS | FAIL
Visual sanity: PASS | FAIL | NOT PROVEN
Findings: <only when findings exist>
Critical: N
Major: N
```

`Semantic Readiness` replaces duplicated persisted fields for reader, role, consistency, acceptance, content-purity semantics, and Golden placement. The review still considers those lenses; it simply records one integrated decision.

`Material Conservation` stays explicit because omission risk is independent from readability. `Visual sanity` stays explicit because browser evidence is a different proof channel.

## 7. Handoff

Before Flow 5, run:

```bash
python kits/project-document-generator/validator/validate_handoff.py \
  workspace/active/<project>/
```

Handoff must point to the current canonical content/projection, acceptance record, `output/README.md`, and the matching versioned `prd.html` / `context.md` / `index.json` bundle. The accepted PRD version must use semantic `X.Y.Z` and match `render-data.document.version` plus the version declared by the side documents.

`output/README.md` is the human/AI resume navigator, not a second project-status database. It identifies the current artifact set and reading route; implementation progress remains owned by the implementation repository. Do not duplicate checksum tables or internal validation transcripts when Git state and the validators already own those checks.

## Bounded revision

```text
approved change
→ affected truth/content only
→ affected projection
→ one full-file rerender
→ one mechanical check
→ one integrated review of invalidated scope
→ visual check only where changed/high-risk
→ stop
```

Do not replay unchanged intake, source review, packages, proof, mobile QA, every-page visual QA, or downstream Voice work for ceremony.
