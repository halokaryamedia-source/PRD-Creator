# ElevenLabs Source Register

Last verified: 2026-08-13

Purpose: keep reusable production rules tied to evidence and prevent old v3 Alpha guidance or creator folklore from silently becoming repository policy.

## Authority order

```text
A — current official ElevenLabs documentation
B — official ElevenLabs product/help/blog material that is useful but may contain legacy/Alpha wording or product-specific behavior
C — creator/community material; heuristic only
P — project-calibrated approved prompt/audio evidence
```

For technical/product claims: **A > B > C**.  
For a voice-specific production behavior already proved by approved audio: **P** can be more useful than generic guidance, but P never changes upstream project facts.

## A — Current official documentation

| Source | URL | Use |
|---|---|---|
| Text to Speech Best Practices | https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices | voice selection, Stability, punctuation, CAPS, Audio Tags, v3 SSML break limitation, text structure, IPA |
| Text to Speech Product Guide | https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech | model/voice influence, nondeterminism, text formatting, numbers/symbols, current web TTS behavior, model limits |
| Models | https://elevenlabs.io/docs/overview/models | v3/v2 positioning, languages, character limits, long-form stability |
| Text to Speech Capability | https://elevenlabs.io/docs/overview/capabilities/text-to-speech | current TTS overview/model positioning |
| Voices | https://elevenlabs.io/docs/overview/capabilities/voices | Voice Library/cloning/design boundaries and language/accent context |
| Voiceover Studio | https://elevenlabs.io/docs/voiceover-studio/overview | Dynamic Duration vs Fixed Duration and timing trade-off |
| Pronunciation Dictionaries | https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/pronunciation-dictionaries | IPA/CMU dictionary support and v3 pronunciation control |
| Create Speech API | https://elevenlabs.io/docs/api-reference/text-to-speech/convert | seed, previous/next context, normalization, request continuity |
| Create Speech with Timing | https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps | seed + previous/next text/request continuity with timing output |
| Credits terminology | https://elevenlabs.io/docs/help-center/account/general/have-characters-changed | website TTS credit-per-character behavior and shared-voice multipliers |
| Quota / generation behavior | https://elevenlabs.io/docs/help-center/account/general/do-i-use-quota-on-every-generation | current Generate/Regenerate charging behavior including v3 alternatives |
| Maximum text | https://elevenlabs.io/docs/help-center/product/speech-synthesis/text-to-speech/whats-the-maximum-amount-of-characters-and-text-i-can-generate | web/API input limits and Studio recommendation for longer content |
| Number/symbol normalization | https://elevenlabs.io/docs/help-center/product/speech-synthesis/text-to-speech/why-are-numbers-dates-symbols-and-acronyms-not-properly-pronounced-or-spoken-in-the-correct-language | explicit spoken forms and normalization behavior |

## B — Official product/news/directing material

| Source | URL | Use / caveat |
|---|---|---|
| Eleven v3 GA announcement | https://elevenlabs.io/blog/eleven-v3-is-now-generally-available | v3 is GA since 2026-02-02; use to override stale `Alpha` labels |
| Emotional Context | https://elevenlabs.io/blog/eleven-v3-audio-tags-expressing-emotional-context-in-speech | emotional beats, long-form evolving performance, reaction sequencing |
| Precision Delivery Control | https://elevenlabs.io/blog/eleven-v3-audio-tags-precision-delivery-control-for-ai-speech | pacing/rhythm/emphasis tags and combinations |
| Narrative Intelligence | https://elevenlabs.io/blog/eleven-v3-audio-tags-enabling-narrative-intelligence-in-speech | long-form narration/story beat directing |
| Character Direction | https://elevenlabs.io/blog/eleven-v3-character-direction | character/accent/archetype directing; article can retain legacy Alpha wording |
| Situational Awareness | https://elevenlabs.io/blog/eleven-v3-situational-awareness | mid-line context/performance changes; article can retain legacy Alpha wording |
| V3 Audio Tags overview | https://elevenlabs.io/blog/v3-audiotags | conceptual Audio Tag categories/directing |
| Voice Design help | https://help.elevenlabs.io/hc/en-us/articles/29314862567313-What-is-Voice-Design | designed-voice compatibility, experimental status, PVC caveat |
| Expressive Mode (Agents) | https://elevenlabs.io/docs/eleven-agents/customization/voice/expressive-mode | product-specific 4–5-word tag scope; **do not transfer this number to normal Speech Synthesis** |

## Legacy source warning

`https://elevenlabs.io/docs/best-practices/prompting` still contains older Alpha-era guidance such as encouraging prompts over 250 characters. Current v3 is GA and the consolidated current Best Practices page does not establish 250 characters as a production minimum.

Treat the old page as historical context only when current documentation does not already answer the question.

## C — Creator/community material

Creator sources are useful for discovering patterns worth checking, not for establishing product truth.

| Source | URL | Useful observation | Authority limit |
|---|---|---|---|
| Versely v3 Creator Guide 2026 | https://www.versely.studio/blog/elevenlabs-v3-voice-cloning-complete-guide-2026 | avoid over-tagging; punctuation and tags reinforce each other; preserve emotional peaks | third-party; do not treat percentages or universal behavior claims as fact |
| Greg Preece v3 tutorial | https://gregpreece.com/articles/11-labs-tutorial-elevenlabs-v3 | practical creator workflow and v3-optimized voice emphasis | may include creator-specific SFX practices outside this Voice lane |
| OmniArt v3 tags guide | https://omniart.studio/blog/articles-tips/eleven-v3-audio-tags-guide | framing Audio Tags as voice-director cues | product/platform-specific vocabulary may differ |

Community reports about inconsistent takes/tag responsiveness are consistent with ElevenLabs' official nondeterminism warning, but do not independently prove a platform regression. Do not store a `v3 tags are broken` rule from anecdotal reports.

## P — Project-calibrated evidence

When an actual project audio is approved, record only evidence that improves later production:

```text
project / Voice ID
exact prompt actually generated
voice
model
visible settings
actual duration
approved pronunciation
what performance behavior worked
what repeatedly failed
```

Do not promote one project's specific tag/voice behavior into a universal rule without additional evidence.

## Documentation conflicts currently known

### Speed

One current TTS product-guide section states Speed is not available for v3, while a current FAQ says Speed 0.7–1.2 is available for all models.

Repository policy: **UNKNOWN / UI-DEPENDENT**. Do not rely on Speed as a mandatory v3 control.

### Language controls

Some help text says web TTS auto-detects language without manual selection, while the current product UI observed by the user can expose a Language Override control.

Repository policy: current UI owns control availability; text/voice language-accent principles remain authoritative.

### PVC + v3

Current official material warns that PVC compatibility/optimization with v3 is limited, while the product UI may allow a PVC with a warning.

Repository policy: treat as compatibility risk requiring actual output evidence, not as a silent prohibition or silent approval.

## Freshness rule

Re-check official sources when:

- ElevenLabs changes v3 model status/settings/UI;
- Director's Mode launches;
- a new production rule depends on Speed, language override, PVC compatibility, or tag semantics;
- a documented current rule conflicts with observed UI behavior.

Do not refresh this register merely for ceremony when the active task does not depend on a changing claim.
