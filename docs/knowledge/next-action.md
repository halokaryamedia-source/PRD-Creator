# Next Action

Updated: 2026-08-13

## Current Status

`SOUNDMAKER_V3_OUTPUT_CONTRACT_READY`

Working branch: **`Local` only**.

## Current state

Project Document Generator remains **v1.13.0**. The approved Clockwork production package remains at `workspace/active/the-clockwork-vault/`; its accepted PRD meaning/rendered HTML were not changed.

Voice Production Kit is now **v1.7.0**.

SoundMaker remains **Eleven v3 only**. Preparation Mode still requires no audio generation/testing; Generation Mode remains optional and one active Voice ID at a time.

The static Voice output contract is now explicit and minimal.

### Canonical `work/voice-production.md`

Each entry contains only:

```text
Voice ID — Title
Type
Speaker
Estimated Duration
exact Eleven v3 performance block
```

`Voice ID`, `Type`, and **Speaker** are fail-closed against Flow 5. Speaker was added because an ElevenLabs operator must never infer which character owns a line.

Planning metadata stays in its owner rather than being duplicated into every script entry:

- Channel / Trigger / Purpose;
- Must communicate / Must not add;
- source refs;
- WPM math / performance-map reasoning;
- voice-fit ratings;
- QA notes.

### Operator handoff

No new handoff artifact is created by default.

Shared setup is stated once when useful:

```text
Speaker / selected voice or target voice profile
Model: Eleven v3
Stability
Surface
```

Each active line then shows only Voice ID/Title, Speaker, Estimated Duration, and the exact prompt. Additional production notes appear only when an operator action is required, such as pronunciation setup, Fixed Duration, or Studio routing.

### Derived DOCX

The DOCX now exposes:

```text
Type · Speaker
Voice ID — Title
Estimated Duration
Performance Script
```

It remains presentation only and does not become a settings database or duplicated Voice Requirements document.

## Non-audio workflow retained

Preparation Mode still supports:

- full-project/batch script preparation;
- context recovery before asking the user;
- Target Voice Profile before actual voice selection;
- duration planning without measured audio;
- pronunciation risk planning without false verification;
- recurring-speaker continuity / information progression;
- cross-line anti-template review;
- no audio generation/listening requirement.

## Next Step

**Continue only with another concrete non-audio workflow/content defect or use Preparation Mode on a real project package when requested. Do not require audio testing until the user explicitly enters Generation Mode.**
