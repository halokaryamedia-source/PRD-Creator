# ElevenLabs contracts and source register

Read for a surface/parameter dispute or before the first paid batch. Checked: **2026-09-09**. These are documented capabilities, not live-account or heard-audio verification.

## Evidence classes

**Official fact** is scoped to its cited surface. **Repository policy** is our production recommendation, not a model guarantee. **Calibration** requires an identified same-project audio file and review. Unsupported controls remain unknown/unsupported; a marketing statement does not establish an API parameter.

## API contract

Source: [Create sound effect](https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert).

| Location | Field | Documented contract |
|---|---|---|
| Endpoint | POST | `/v1/sound-generation` |
| Body | `text` | Required description |
| Body | `model_id` | Default `eleven_text_to_sound_v2` |
| Body | `duration_seconds` | null/auto or 0.5–30 seconds |
| Body | `loop` | Boolean; default false; v2 only |
| Body | `prompt_influence` | 0–1; default 0.3 |
| Query | `output_format` | Verify supported enum and account entitlement |

Higher influence requests closer adherence with less variation, not guaranteed higher quality. The documented request has no `seed`, `voice_id`, `negative_prompt`, reference-audio input, event-timestamp control, or candidate-count field. Do not borrow these from speech/music endpoints. Unsupported does not mean technically impossible forever; re-check before changing policy.

The response may expose `character-cost`; retain its raw unit when useful. Do not silently convert it to currency. Read returned file metadata rather than assuming the response-description label overrides the requested codec.

## Surface differences and conflicts

| Source | Supported finding | Policy consequence |
|---|---|---|
| [Website guide](https://elevenlabs.io/docs/eleven-creative/playground/sound-effects) | Four effects per Generate; History review/download | A website candidate group is not four independent API requests; inspect candidates before another Generate. |
| [Website FAQ](https://elevenlabs.io/docs/help-center/product/core-capabilities/sound-effects/what-is-sound-effects) | Website prompt limit 450 characters | This is not an established API maximum. Portable examples stay below it. |
| [Overview](https://elevenlabs.io/docs/overview/capabilities/sound-effects) | Mentions 0.1-second minimum, 30-second maximum and WAV for non-looping effects | API execution uses the endpoint's 0.5-second minimum. Do not assume identical download choices across surfaces. |
| [Prompting help](https://help.elevenlabs.io/hc/en-us/articles/25735604945041-How-do-I-prompt-for-sound-effects) | Natural language/audio terms; concise detail; individual generation plus editing for complex effects | Archetype recipes are craft proposals, not official per-category presets. |
| [Current cost FAQ](https://elevenlabs.io/docs/help-center/product/core-capabilities/sound-effects/how-much-does-it-cost-to-generate-sound-effects) | Refers to current ElevenCreative/ElevenAPI rates; input text does not determine price | Do not use historical credit figures or equate shorter wording with lower SFX charges. |
| [Current API pricing](https://elevenlabs.io/pricing/api) | Live commercial reference; verify billing basis on the active account | No fixed numeric rate is stored in this skill. Conflicting units require reconciliation before a hard-money-capped request. |
| [Studio](https://elevenlabs.io/docs/eleven-creative/products/studio) | Timeline SFX placement/editing; SFX excluded from ElevenReader exports and Studio API project streaming | Studio is an editorial option, not assumed SFX API parity. Narration regeneration offers do not establish free SFX retries. |

Studio also documents plan-dependent WAV export from a compressed source and separately billed Studio Agent chat. Policy: a WAV extension does not prove a lossless origin; do not route a simple SFX request through a billable co-editor unnecessarily. Verify whether playback/export will generate other unconverted media before using it.

## Official tooling boundary

The [official sound-effects skill](https://github.com/elevenlabs/skills/blob/main/sound-effects/SKILL.md) contains execution instructions, not credentials or a callable tool. Read the installed executor's actual schema and defaults; prose examples can lag an SDK.

The [local MCP README](https://github.com/elevenlabs/elevenlabs-mcp/blob/main/README.md) marks that server deprecated in favor of hosted MCP. [Agent tooling](https://elevenlabs.io/docs/eleven-api/resources/agent-tooling) describes supported integration options. Do not infer that any connected/hosted MCP exposes the required SFX tool. Verify it once per execution environment; do not install a legacy server or copy an SDK into core PRD-Creator.

## Rights and privacy preflight

Sources: [Publishing guidance](https://help.elevenlabs.io/hc/en-us/articles/13313564601361-Can-I-publish-the-content-I-generate-on-the-platform), [Sound Effects Terms](https://elevenlabs.io/sound-effects-terms).

Check generation-time commercial eligibility, beta restrictions, source rights, and applicable client terms before using an asset commercially. A later paid subscription does not by itself relicense earlier free-plan output. The SFX terms dated 12 February 2026 describe a sublicensing opt-out; it does not retract already-granted uses. For restricted client work, resolve required settings before generation. Do not change account/privacy settings without authorization or upload private project prose merely to enrich a prompt.

## Update discipline

Re-check only the affected source when the model, executor, account terms, billing unit, observed controls, or documented contract changes. Preserve the observation date and scope. If sources disagree, record the conflict and use endpoint authority for API fields, active account evidence for billing, and heard files for acoustics. Do not resolve unknowns by paid probing. Never promote an untested prompt, language preference, loop claim, or cost-saving percentage into a fact.
