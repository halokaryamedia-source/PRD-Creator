# PRD-Creator

PRD-Creator produces a development-ready PRD plus optional objective-first Production Assets in the same project HTML.

Current versions: Project Document Generator **v1.14.0**; Voice Production Kit **v1.11.2**; Voice scope **Eleven v3**. Development continues on `Local`.

## Output

```text
output/
├── README.md                  # navigator / resume entry point
└── v<document.version>/
    ├── prd.html               # human review
    ├── context.md             # AI semantic/development context
    └── index.json             # compact AI navigation + context line ranges
```

`prd.html` keeps the approved human-facing PRD presentation. `context.md` and `index.json` are derived side documents from the same accepted project truth; they are not a second PRD authority.

Production Assets pages show only non-zero categories: `3D Models`, `UI & Information`, `Audio`, and `Visual Effects & Presentation`.

Optional non-Voice requirements use `work/asset-requirements.md` and are governed by `kits/project-document-generator/PRODUCTION-ASSETS.md`. Voice keeps its existing Flow 5–7 canonical sources and appears inside the matching gameplay page under `Audio → Voice Production`.

The accepted PRD hierarchy, PRD page identities, and Golden template bytes remain unchanged by downstream composition.

Current ownership and continuation:

```text
kits/project-document-generator/CONTENT-CONTRACT.md
kits/project-document-generator/PRODUCTION-ASSETS.md
kits/project-document-generator/RENDERING.md
kits/voice-production-kit/
docs/knowledge/ownership.md
docs/knowledge/next-action.md
workspace/README.md
```
