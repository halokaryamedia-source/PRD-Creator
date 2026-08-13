# PRD-Creator

PRD-Creator produces a development-ready PRD plus optional objective-first Production Assets in the same project HTML.

Current versions: Project Document Generator **v1.13.0**; Voice Production Kit **v1.11.2**; Voice scope **Eleven v3**. Development continues on `Local`.

## Output

```text
output/final.html
├── 01 Overview
├── 02 Gameplay Flow
├── 03 Development
│   └── gameplay/objective sections
└── 04 Production Assets      # only when downstream assets exist
    ├── Global / Shared Assets   # only when needed
    └── <gameplay section> → <accepted PRD label>
```

Production Assets pages show only non-zero categories: `3D Models`, `UI & Information`, `Audio`, and `Cinematic & Presentation`.

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
