# PRD Creator

**Version:** 3.1.3

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

Package 3.1.2 restores Audio Tags as first-class Eleven v3 acting controls through Expression Coverage without returning to boilerplate tags.

Package 3.1.3 completes the pre-audio Voice preparation model with **Actor/Character Continuity, Language & Pronunciation Control, and controlled Candidate Iteration**. Existing `VO-...` / `AST-...` formats and lifecycle state remain backward-compatible.

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
   ├─ Actor Baseline / Voice Fit
   ├─ natural spoken wording
   ├─ Expression Coverage / Audio Tags
   ├─ pronunciation/language strategy
   ├─ continuity planning
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
│     ├─ v3-voice-casting-continuity.md
│     ├─ v3-pronunciation-language.md
│     ├─ v3-candidate-iteration.md
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

### Actor / Character Continuity

For recurring Speakers, SoundMaker establishes an internal actor baseline:

```text
Identity / Timbre
Native Cadence
Baseline Energy / Projection
Emotional / Projection Range
Language / Accent
Persona / Social Stance
No-Drift Boundary
Pronunciation Risk
```

Each Moment is treated as a local performance **delta from that actor**, not permission to reinvent the character.

Voice selection should cover the broadest required project envelope. Expression-heavy lines do not justify forcing an unsuitable voice with tag stacks.

When actual generation begins, use the actual ElevenLabs `voice_id` as reproducibility evidence when material. Current ElevenLabs Default voices are scheduled to expire on **2026-12-31**; a suggested replacement is not assumed to be an equivalent actor.

### Naturalness foundation

```text
actor fit
→ natural spoken wording
→ thought-group prosody
```

This removes document-like stiffness without forcing all speakers into casual dialogue.

### Expression Coverage

SoundMaker preserves material acting:

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
no material acting state beyond actor/text baseline
→ zero-tag payload may be correct

material emotion/subtext/projection/pacing/reaction/transition
→ explicit direction must be sufficient
→ use precise Audio Tag(s) when needed
```

The quality goal is **complete expression coverage without redundant direction**.

### Language & Pronunciation

Before generation, detect only critical spoken-form risks: names, fictional/project terms, acronyms, numbers/dates/symbols, foreign/code-switched terms, and repeated technical vocabulary.

Use the smallest reliable control:

```text
normal text
→ explicit spoken form/alias when ambiguous
→ IPA/phoneme when needed
→ pronunciation dictionary for repeated critical terms
```

Prefer a voice compatible with the target language/accent. Website TTS auto-detects language from text context; API `language_code` may be used when short/ambiguous input or normalization needs an explicit language.

### Generation boundaries

Connected same-speaker narration may use `previous_text` / `next_text` or neighboring request IDs for prosodic continuity. Each new TTS request can reset acting state; when a specific expression must continue, re-anchor that state at the new clip opening when necessary.

Conversationally dependent multi-speaker Voice IDs in one approved Moment use Text to Dialogue. Each turn keeps its own `VO-...` identity, actor baseline, and local expression direction.

### Candidate iteration

ElevenLabs output is nondeterministic. A single weak take does not prove the canonical prompt is wrong.

```text
reviewed prompt + same voice/settings/context
→ compare same-content candidate/regeneration
→ repeated defect?
   no  → select best acceptable take
   yes → diagnose first wrong owner
```

After a repeated defect is established, change one variable class at a time: wording, expression direction, voice, settings, pronunciation/language, or surface/context.

Do not require a fixed number of takes. `seed` is best-effort consistency only.

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
Expression Conservation
Character Continuity Conservation when applicable
Pronunciation Conservation
Voice Script Readiness
```

These remain semantic/craft gates, not new persisted schema fields.

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
- preserve actor identity and material expression;
- use explicit acting direction when performance would otherwise be ambiguous;
- protect critical pronunciation before generation;
- distinguish candidate variance from real prompt/voice/settings defects;
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

Mechanical PASS does not establish semantic, visual, naturalness, expression, pronunciation, or audio-quality proof.

## Derived delivery

```text
output/README.md
output/v<document.version>/prd.html
output/v<document.version>/context.md
output/v<document.version>/index.json
```

Derived files never outrank canonical `work/` / `state/` sources.

For production use start from `SKILL.md`. For implementation defects start from `AGENTS.md` and the smallest exact technical owner.
