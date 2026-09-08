# Eleven v3 Language & Pronunciation Control

Last verified: **2026-09-09**

Purpose: prevent pronunciation, accent, normalization, and language-detection errors from being misdiagnosed as acting problems. This is a production reference for `../PERFORMANCE-WRITING.md`, not a pronunciation manifest or new canonical schema.

## Core principle

```text
correct language/accent voice fit
→ production-ready spoken text
→ detect critical pronunciation risks
→ apply the smallest reliable control
→ verify only when audio exists
```

Do not use emotional tags to repair pronunciation.

## 1. Pre-generation Spoken Form Pass

Before generation, inspect only terms that can materially fail:

```text
proper names
fictional locations
project/game terminology
acronyms / initialisms
numbers / dates / coordinates / symbols
foreign words
code-switched phrases
brand/product names
repeated technical terms
```

Ordinary low-risk vocabulary needs no special treatment.

## 2. Control ladder

Use the smallest intervention that solves the risk:

```text
normal word
→ normal text

ambiguous number/date/symbol/acronym
→ explicit spoken wording / alias

isolated unusual proper noun
→ IPA/phoneme control when needed

repeated critical project term
→ pronunciation dictionary

heard + approved pronunciation
→ project calibration
```

Do not create phonetic spellings everywhere by default.

## 3. Pronunciation dictionaries

Current ElevenLabs pronunciation dictionaries are useful for names, places, technical terms, and repeated vocabulary that must remain consistent.

Current official guidance:

- phoneme dictionary entries support Eleven v3;
- IPA and CMU alphabets are supported;
- Eleven v3 is required for IPA/CMU pronunciation in non-English languages;
- PLS entries are case-sensitive;
- focus dictionaries on terms that are frequently mispronounced or critical to the use case.

Repository rule:

```text
one-off low-risk term
→ avoid dictionary overhead

repeated critical term / consistency requirement
→ dictionary is preferred production setup
```

Dictionary identity/version belongs to generation evidence only when materially used; do not add it as a mandatory field to every VO entry.

## 4. Language and accent fit

Current ElevenLabs guidance says language is driven largely by text while accent/pronunciation are strongly influenced by the selected voice.

Prefer a voice trained in the target language and desired accent when that distinction matters.

A pronunciation problem caused by a mismatched actor should first route to **voice fit**, not progressively more phonetic hacks.

## 5. Website vs API language behavior

Current product behavior:

```text
website TTS
→ language auto-detected from prompt context

API
→ optional language_code (ISO 639-1)
```

Use `language_code` when short/ambiguous input, numbers, normalization, or language ambiguity makes the intended language unclear.

Do not assume `language_code` can turn an unsuitable voice into a native accent.

## 6. Code-switching / multilingual lines

Mixed-language prompts can confuse automatic language detection on the website.

When code-switching is genuinely required:

1. keep the primary language clear from context;
2. minimize unnecessary language switching inside one tiny line;
3. use an actor with compatible multilingual performance when possible;
4. use API `language_code` only when one dominant language should own normalization;
5. explicitly protect critical foreign names/terms with pronunciation control when needed.

Do not rewrite approved multilingual meaning simply to avoid a production challenge.

## 7. Numbers, dates, acronyms, and symbols

For production-critical content, prefer the exact spoken form you want heard rather than relying on normalization to guess intent.

Examples:

```text
2026
→ "twenty twenty-six" or project-required form

3/4
→ "three quarters" / "three slash four" according to meaning

NPC
→ "N-P-C" or established spoken form
```

The semantic owner decides what the value means; SoundMaker decides the safe spoken representation.

## 8. Pronunciation Conservation

A script passes when:

- every critical name/term has an intentional spoken strategy;
- the selected voice is compatible with target language/accent;
- code-switching is deliberate rather than accidental;
- numbers/dates/acronyms/symbols are not materially ambiguous;
- pronunciation control does not alter project meaning;
- unverified pronunciation is never claimed as approved before audio evidence exists.

This is part of Voice Script Readiness, not a new persisted acceptance field.

## Current official sources

- `https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/pronunciation-dictionaries`
- `https://elevenlabs.io/docs/eleven-agents/customization/voice/pronunciation-dictionary`
- `https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-do-i-select-the-language-and-accent`
- `https://elevenlabs.io/docs/api-reference/text-to-speech/convert`
