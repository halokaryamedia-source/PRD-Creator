# Next Action

## Current Status

`ASTRA_DEVELOP_CANDIDATE_READY`

The Astra optimization candidate is complete on `develop` and remains behavior/output preserving.

Completed high-value changes:

1. compact agent/context routing with the same authority and first-wrong-owner boundaries;
2. compact GitHub execution rules without weakening branch/write/verification safety;
3. repository verification owns durable machine invariants instead of duplicated prose wording;
4. one tracked canonical Golden/runtime source; the redundant runtime-template alias is retired;
5. default render is regression-proven byte-identical to explicit canonical Golden rendering;
6. GitHub Actions use current Node-24-capable v7 releases pinned by immutable commit SHA;
7. the verifier enforces immutable external Action refs;
8. Repository Verify runs on every `develop`/`Local` push and owns the repository-health contract;
9. changes to the repository verifier automatically trigger the full Local Promotion regression on `develop`;
10. one adaptive scope-proportional routing system now keeps bounded Maintenance and Production work on the smallest relevant owner/proof path without creating separate fast/full modes or weaker quality paths.

Baseline commit `40f50bf72ef9be03c2ec058552670f3ee8b24325` passed Repository Verify and Local Promotion Verify, including repository contracts, Ruff, Mypy, the complete `test_*.py` suite, coverage threshold enforcement, and browser proof.

Routing commit `b3efc93836a24c1b63dfcf9aacf781965f9b3b3a` passed Repository Verify. It changes routing/procedure only: PRD/Voice semantic contracts, render-data schema, machine identity, Golden bytes/design grammar, renderer/validator behavior, Production Assets, Voice output contracts, and promotion gates remain unchanged.

No branch promotion was performed.

## Active Boundary

Keep all current work on `develop`.

- Use one system and one quality standard; never introduce parallel fast/full workflows.
- Minor or bounded work must touch only the context, owner, downstream scope, tools, and proof that can affect the requested result.
- Expand context or verification only when evidence shows the bounded path is insufficient.
- `status` and `impact` are conditional routing aids, not mandatory ceremony.
- PRD/Voice semantic contracts remain unchanged.
- Render-data schema and machine identity contracts remain unchanged.
- Golden approved bytes/design grammar remain unchanged.
- Production Assets and Voice output contracts remain unchanged.
- Full regression/browser proof remains mandatory before any eventual `develop → Local` promotion.
- Do not add more abstraction, duplicate routing, compatibility layers, caches, or model-specific ceremony without a reproduced defect.

## Next Step

Use this `develop` candidate for a real PRD-Creator production task with GPT-6 Astra Extra High and record only concrete defects or friction that actually appear. Keep fixes bounded to the first wrong owner and avoid unrelated work. Do not promote to `Local` until the user explicitly requests promotion after the pilot.
