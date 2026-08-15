# Workflow

Project Document Generator has three numbered PRD production steps plus one bounded 04 Production Assets completion capability. This file owns **sequence only**; detailed behavior stays in each owner.

```text
Flow 2  UNDERSTAND + COMPLETE
Flow 3  BUILD PRD CORE 01–03
Flow 4  REVIEW & HANDOFF
        ↓
        COMPLETE 04 PRODUCTION ASSETS when justified
        # bounded capability, not another numbered Flow
```

Normal project creation/revision is Production Execution, not repository Developing.

## Flow 2 — UNDERSTAND + COMPLETE

Owner: `SOURCE-INTAKE.md`.

```text
source evidence + current instruction
→ authority/relevance triage
→ recover facts/rules/exclusions/topology/terminology
→ one integrated production-completeness pass
   including real Production Asset needs
→ Completion or concrete Proposal for material missing/conflicting meaning
→ propagate affected Gameplay / Level Design / Developer / Production Asset / timing / scoring / reset meaning
→ complete objective-based Simple Chat Preview
→ user correction / approval
→ promote represented pending proposals
→ ready_for_prd
```

Flow 2 must produce a **complete reviewable project model**, not a list of gaps. Golden supplies the finite questions/slot responsibilities for 01–03; it does not supply project facts or asset style.

Use `Blocked` only when no responsible proposal can be formed. Do not enter Flow 3 until the relevant preview meaning is approved. For a bounded revision, preview only the invalidated objective/global slice when interpretation changed; an unambiguous current user instruction may itself approve that slice.

Once ready, stop Flow 2. Optional redesign ideas are not part of intake.

## Flow 3 — BUILD PRD CORE 01–03

Semantic owner: `CONTENT-CONTRACT.md`.
Projection mechanics: `RENDERING.md` only when needed.

```text
preview-approved requirement state
→ one Content Purity + Humanize pass
→ work/content.md
→ direct work/render-data.json projection from the same approved model
→ exact approved Golden template + deterministic renderer
→ output/v<document.version>/prd.html → 01–03
```

`content.md` owns PRD-core meaning. Projection and HTML are derived.

Do not use HTML generation as the drafting loop and do not perform a second AI rewrite merely to create render data. If authoring exposes a new material product/design decision, return only that affected slice to Flow 2.

## Flow 4 — REVIEW & HANDOFF

Owner: `VALIDATION.md`.

```text
one mechanical validation
+ one integrated Semantic Readiness review
  including Production Assets readiness when 04 exists
+ Material Conservation
+ targeted desktop visual sanity when the claim requires it
→ fix first wrong owner
→ development_ready | handoff_ready
```

Mechanical PASS is not semantic or visual approval. New Reader, Level Designer, Developer, Production Assets when applicable, Content Purity, Project Consistency, and Golden Placement are lenses inside one semantic review, not separate persisted gates.

Normal content-only production does not re-prove the full Golden reference when the template/composition contract is unchanged.

## 04 Production Assets — bounded completion, no new Flow

Owner: `PRODUCTION-ASSETS.md`.

Production Asset needs come from the **same approved project model** recovered in Flow 2.

```text
approved project model
→ real non-Voice resource needs
→ work/asset-requirements.md
→ optional canonical Voice data from existing Voice owners
→ deterministic compositor
→ same output/v<document.version>/prd.html → 04 Production Assets
```

Do not discover 04 by rereading generated 01–03 and brainstorming extra assets. Do not modify 01–03 merely to make 04 easier to author or render.

## Bounded revision

```text
approved change
→ affected Flow 2 truth only
→ affected canonical PRD-core content/projection and/or 04 source
→ one full deterministic rerender
→ one mechanical check
→ targeted semantic/material/visual review of invalidated scope
→ stop
```

Do not replay unchanged intake, packages, evidence, mobile QA, Golden reverse proof, or downstream Voice work.

## Delivery

Default user delivery is the requested project document plus material changes/attention items. Internal source inventory, requirement state, render projection, and validator details stay internal unless needed.

Do not add workflow stages, template profiles, quality scores, screenshot systems, checksum registries, asset frameworks, or HTML frameworks merely to make the process look more rigorous.
