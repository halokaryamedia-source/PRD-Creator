# PRD-Creator

PRD-Creator turns project discussion + source material into a development-ready PRD and, when needed, 04 Production Assets in the same project HTML.

Current package: **PRD Creator v1.14.0**. Voice scope remains **Eleven v3**. Development continues on `Local`.

## Output

```text
output/
├── README.md                  # navigator / resume entry point
└── v<document.version>/
    ├── prd.html               # human review
    ├── context.md             # AI semantic/development context
    └── index.json             # compact AI navigation + context line ranges
```

`prd.html` keeps the approved 01–03 PRD-core presentation. `context.md` and `index.json` are derived side documents from the same accepted project truth; they are not a second PRD authority.

04 Production Assets is planned from the same approved project model as 01–03 and is presented objective/moment-first. Visible resource types are `MODEL`, `ITEM`, `UI / TEXT`, `AUDIO`, and `PARTICLE`; only real required resources are included.

Optional non-Voice requirements use `work/asset-requirements.md` and are governed by `kits/prd-creator/production-assets/CONTRACT.md`. Voice keeps its Flow 5–7 canonical sources and is merged into the matching 04 moment as `AUDIO`.

The accepted 01–03 hierarchy, PRD page identities, Golden template bytes, and PRD-core style remain unchanged by 04 composition.

## Package map

```text
kits/prd-creator/
├─ README.md
├─ AGENTS.md
├─ SKILL.md
├─ intake/
├─ document/
├─ production-assets/
├─ voice/
├─ renderer/
├─ validator/
└─ template/
```

Project/PRD and Voice remain separate semantic domains inside this one product package.

Current ownership and continuation:

```text
kits/prd-creator/README.md
kits/prd-creator/AGENTS.md
kits/prd-creator/SKILL.md
docs/knowledge/ownership.md
docs/knowledge/next-action.md
workspace/README.md
```
