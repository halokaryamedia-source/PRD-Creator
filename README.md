# PRD-Creator

PRD-Creator turns project discussion + source material into a development-ready PRD and, when needed, 04 Production Assets plus downstream Voice Production in the same project delivery.

## Branch Model

```text
Local  → active development / working authority
main   → stable / release branch
```

Routine development happens directly on `Local`; routine task branches and PRs are not required. `main` changes only through an explicit stable/release promotion. A release promotion may use a dedicated `Local` → `main` pull request and must pass the full `Release Verify` gate.

Repository behavior is routed by [AGENTS.md](AGENTS.md); GitHub execution is governed by [GITHUB_RULES.md](GITHUB_RULES.md). Stable product orientation lives in [CONTEXT.md](CONTEXT.md).

## Developer Quick Start

Prerequisite: **Python 3.11**. The current verification environment has no third-party Python dependencies.

Repository contract check:

```bash
python tools/verify_repository.py
```

PRD regression suite:

```bash
python -m unittest \
  tests.test_prd_contracts \
  tests.test_prd_content_purity \
  tests.test_prd_delivery \
  tests.test_prd_voice_assets \
  tests.test_prd_handoff_contracts \
  tests.test_prd_flow2_state_contracts \
  tests.test_prd_hierarchy_contracts \
  tests.test_prd_golden_reference
```

Voice regression suite:

```bash
python -m unittest tests.test_voice_contracts
```

Generate the current versioned delivery for a project:

```bash
python kits/prd-creator/renderer/delivery.py \
  workspace/active/<project>/
```

Validate a project revision:

```bash
python kits/prd-creator/validator/validate.py \
  workspace/active/<project>/
```

Use `validate_handoff.py` only when crossing the PRD handoff boundary and `validate_voice.py` only for current Voice scope. Current package version is owned by [kits/prd-creator/README.md](kits/prd-creator/README.md), not duplicated here.

## Output

```text
output/
├── README.md                  # stable handoff / resume navigator
└── v<document.version>/
    ├── prd.html               # human-facing project document
    ├── context.md             # AI semantic/development context
    └── index.json             # compact AI navigation + context ranges
```

`prd.html` keeps the approved PRD-core 01–03 presentation. `04 Production Assets` is additive and is planned from the same approved project model, not from a second design pass over generated 01–03. Voice remains downstream from accepted PRD meaning and is presented as `AUDIO` inside the matching 04 gameplay moment when required.

## Repository Map

```text
.agents/skills/      reusable semantic judgment
docs/foundation/     durable Flow policy
docs/knowledge/      continuation, ownership, decisions, evidence
kits/prd-creator/    Flow 2–7 procedure + implementation
tests/               executable regression contracts
tools/               repository verification
workspace/active/    current project packages
workspace/archive/   inactive retained project packages
```

Open only the owner required for the current task. Do not broad-read the repository, regenerate unrelated artifacts, or reopen completed workflow stages for ceremony.

## Working Principle

```text
identify mode
→ find first changed owner
→ read affected context only
→ change canonical source
→ regenerate only invalidated output
→ run the cheapest relevant proof
→ stop
```

Generated delivery is never a source of truth. Fix canonical state first, then regenerate.

## License

This repository is **not open source**. It is publicly accessible for development convenience, but use is restricted to personal/internal use by the copyright holder and explicitly authorized collaborators. See [LICENSE](LICENSE).
