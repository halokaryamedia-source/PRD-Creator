# PRD Creator

**Version:** 3.1.2

PRD Creator turns project evidence/discussion into one revision-bound project model, canonical PRD, required Production Assets, and optional Voice Production in one versioned delivery.

## Version rule

```text
PATCH  backward-compatible fix
MINOR  additive backward-compatible capability
MAJOR  incompatible product/machine contract change
NO BUMP project-only revision, clarification, CI/repository hygiene, test-only work
```

Package 3.1 adds current ElevenLabs TTS/Text-to-Dialogue routing and non-dialogue Sound Effects production while preserving existing Asset/Voice machine formats.

Package 3.1.1 removes stiff document-like Voice writing and the repository-only mandatory opening-tag syntax rule.

Package 3.1.2 corrects the opposite risk: **Audio Tags remain first-class Eleven v3 acting controls**. SoundMaker now requires Expression Coverage for material emotion, subtext, projection, pacing, reactions, and state transitions while still allowing true baseline lines to remain zero-tag. Existing `VO-...` / `AST-...` formats and lifecycle state remain backward-compatible.

## Product flow

```text
sources
→ strict provenance + material requirement recovery
→ integrated cross-role model
→ conditional Proposal approval
→ exact requirement-revision binding
→ canonical content.md
→ strict render projection
→ deterministic PRD core
→ non-Voice 04 when required
   └─ AUDIO may use ElevenLabs SFX production
→ exact-byte PRD/04 acceptance
→ minimal handoff state
→ Flow 5 Voice requirements when justified
→ Flow 6 Voice production
   ├─ natural spoken wording
   ├─ Expression Coverage / Audio Tag direction
   └─ TTS | contextual TTS | Text to Dialogue | Studio
→ exact-byte Flow 7 acceptance
→ one current project HTML
```

## Package 3 engineering shape

```text
single truth
→ stable identity
→ strict schema
→ exact revision binding
→ deterministic projection
→ transactional publication
```

## Key contracts

```text
Flow 2
requirement-register bytes → approved_requirement_sha256

PRD projection
requirement SHA + content.md bytes → render-data bindings

PRD acceptance
Accepted Render Data SHA256
Accepted Asset Requirements SHA256

04 identity
Owner ID → Moment ID → AST/VO ID

Voice production
voice-production → exact Voice Requirements SHA

Voice acceptance
Accepted Voice Production SHA256
```

## Package map

```text
kits/prd-creator/
├─ SKILL.md
├─ AGENTS.md
├─ README.md
├─ intake/
├─ document/
├─ production-assets/
│  ├─ CONTRACT.md
│  └─ SOUND-EFFECTS.md
├─ voice/
│  ├─ EXTRACTION.md
│  ├─ PERFORMANCE-WRITING.md
│  ├─ VALIDATION.md
│  └─ references/elevenlabs/
│     ├─ v3-naturalness.md
│     ├─ v3-expression-direction.md
│     ├─ v3-performance-writing.md
│     ├─ v3-duration-planning.md
│     ├─ v3-dialogue-generation.md
│     ├─ v3-production-reference.md
│     └─ source-register.md
├─ shared/
├─ renderer/
├─ validator/
└─ template/
   └─ golden-reference.html
```

## Canonical owners

| Meaning | Artifact | Owner |
|---|---|---|
| source / requirement revision | `state/source-inventory.yaml`, `requirement-register.yaml`, `intake-state.yaml` | `intake/SOURCE-INTAKE.md` |
| PRD semantic meaning | `work/content.md` | `document/CONTENT-CONTRACT.md` |
| strict render projection | `work/render-data.json` | `shared/render_schema.py` + `renderer/CONTRACT.md` |
| Golden grammar | `template/golden-reference.html` | `document/DESIGN-CONTRACT.md` |
| non-Voice 04 | `work/asset-requirements.md` | `production-assets/CONTRACT.md` |
| ElevenLabs non-dialogue SFX | derived production context | `production-assets/SOUND-EFFECTS.md` |
| PRD acceptance/handoff | `work/acceptance.md`, `state/handoff-state.yaml` | `document/VALIDATION.md` |
| Voice requirements | `work/voice-requirements.md` | `voice/EXTRACTION.md` |
| Voice wording/performance | `work/voice-production.md` | `voice/PERFORMANCE-WRITING.md` |
| Voice acceptance | `work/voice-acceptance.md`, `state/voice-state.yaml` | `voice/VALIDATION.md` |

Do not create parallel schemas for these owners.

## ElevenLabs Voice model

### Naturalness foundation

```text
voice fit
→ natural spoken wording
→ thought-group prosody
```

This removes document-like stiffness without forcing all speakers into casual dialogue.

### Expression Coverage

SoundMaker then preserves material acting:

```text
Baseline State
Emotion
Attitude / Subtext
Projection
Pace / Rhythm
Intensity / Energy
Cognitive State
Reaction Event
Transition Points
Landing
```

Policy:

```text
no material acting state beyond voice/text baseline
→ zero-tag payload may be correct

material emotion/subtext/projection/pacing/reaction/transition
→ explicit direction must be sufficient
→ use precise Audio Tag(s) when needed
```

The quality goal is **complete expression coverage without redundant direction**, not `minimum tags` or `maximum tags`.

### Generation boundaries

Connected same-speaker narration may use `previous_text` / `next_text` or neighboring request IDs for prosodic continuity. Each new TTS request can reset acting state; when a specific expression must continue, re-anchor that state at the new clip opening when necessary.

### Dialogue

Conversationally dependent multi-speaker Voice IDs in one approved Moment use Text to Dialogue. Each turn keeps its own `VO-...` identity and its own expression tags where required.

### Settings

```text
Stability: Natural baseline
Creative: when greater expressive range is intentionally needed
Robust: when consistency outweighs directional responsiveness
Enhance: OFF on SoundMaker-reviewed prompts by default
```

## Voice readiness

Preparation establishes:

```text
Communication Conservation
Naturalness
Expression Conservation
Voice Script Readiness
```

Expression Conservation is a semantic/craft gate inside Voice Script Readiness, not a new persisted schema field.

Actual generated-audio quality still requires heard evidence.

## Renderer boundaries

- one strict render-data vocabulary;
- renderer does not invent missing semantics;
- Golden template remains protected;
- 04 joins only through stable Owner/Moment/Resource identity;
- delivery publishes complete version directories transactionally.

## Model behavior

- start from the smallest authoritative owner;
- preserve approved meaning, not accidental PRD syntax;
- preserve material expression, not arbitrary tag count;
- use explicit acting direction when performance would otherwise be ambiguous;
- do not invent personality/lore merely to make Voice more dramatic;
- fix the first wrong owner;
- stop when requested scope is correct and sufficiently proven.

## Operator CLI

```bash
python tools/prd.py status workspace/active/<project>/
python tools/prd.py build workspace/active/<project>/
python tools/prd.py validate workspace/active/<project>/
python tools/prd.py handoff workspace/active/<project>/
python tools/prd.py voice workspace/active/<project>/
```

Mechanical PASS does not establish semantic, visual, naturalness, expression, or audio-quality proof.

## Derived delivery

```text
output/README.md
output/v<document.version>/prd.html
output/v<document.version>/context.md
output/v<document.version>/index.json
```

Derived files never outrank canonical `work/` / `state/` sources.

For production use start from `SKILL.md`. For implementation defects start from `AGENTS.md` and the smallest exact technical owner.
