# Eleven v3 Naturalness & Narration Craft

Last verified: **2026-09-09**

Purpose: reduce stiff, synthetic, document-like Voice output **without flattening expression**. Naturalness craft and expression direction are complementary: this file owns speakability/prosody; `v3-expression-direction.md` owns explicit acting coverage.

## Core order

```text
approved meaning
→ suitable voice
→ natural spoken-language rewrite
→ thought-group / prosody design
→ Expression Coverage
→ continuity context
→ final punctuation/tag placement
→ generation
```

A line can be natural but under-expressive. A line can also be expressive but synthetic because it is over-directed. SoundMaker must avoid both.

# 1. Common causes of stiffness

- PRD/specification prose carried directly into speech;
- uniform sentence length and stress;
- several facts packed into one clause chain;
- repeated exposition the listener already knows;
- no listener relationship or point of view;
- mismatched voice cadence/projection/accent/emotional range;
- redundant Audio Tags, CAPS, punctuation, and settings all pushing the same state;
- connected narration generated as contextless fragments;
- Speed/Stability used to repair bad writing;
- fake-human filler or hesitations added mechanically.

Do **not** diagnose all stiffness as `too many tags`. Missing expression direction can also produce a flat, generic reading.

# 2. Speechification pass

Preserve required facts, then remove written-language scaffolding that does not help the listener.

Prefer:

- direct spoken verbs;
- familiar word order;
- context-aware references when unambiguous;
- contractions when appropriate;
- sentence-length variation driven by thought complexity;
- one dominant listener-facing purpose per thought group;
- a clear landing.

Avoid document phrases such as `the player must`, `in order to`, `upon completion of`, or `the objective is to` unless the speaker genuinely talks that way.

Example:

```text
written
Proceed to the central console in order to activate the sequence. Upon activation, remain within the marked area until calibration is complete.

spoken
Head to the central console and start the sequence.
Stay inside the marked area until calibration finishes.
```

This is not automatically casual; it is easier to speak and hear.

## 2A. Spoken economy and listener load

Treat every Voice line as an **auditory interface**, not a spoken copy of the design document.

Preserve every `Must communicate` fact, but communicate only what the listener needs **at this Moment**. Do not verbalize the entire mechanic tree merely because the PRD contains it.

Warning signs that exposition is still too document-like:

- several consecutive sentences repeat the same subject (`Kopi...`, `Kayu manis...`, `Sawit...`) with parallel specification syntax;
- a character explains implementation detail that is already visible or belongs to a later Moment;
- the same reward, instruction, or premise is restated in multiple ways;
- a simple invitation or tutorial becomes a checklist read aloud;
- the script reaches the top of its Estimated Duration range before expressive pauses/reactions are considered.

Rewrite in this order:

```text
required facts
→ listener-relevant grouping
→ remove duplicated framing
→ compress repeated syntax
→ keep character point of view
→ preserve a clear final landing
```

For tutorial/expository NPC dialogue, prefer a short setup plus grouped rules over one sentence per database field. When the accepted project already provides multiple Moments, distribute information to the correct Moment rather than front-loading everything into the first line.

Do not delete required gameplay truth merely to make a script shorter. If all facts genuinely belong in one Moment, keep them and use an honest longer Estimated Duration.

# 3. Register-correct naturalness

| Voice job | Natural baseline |
|---|---|
| Direct NPC dialogue | relational, context-aware, responsive |
| Narration | coherent thought flow, sentence contrast, controlled point of view |
| Radio / mission comms | concise, intelligible, structured |
| Tutorial / guidance | direct, calm when appropriate, one action per beat |
| Warning | front-loaded risk/action, little unnecessary explanation |
| Completion / success | acknowledge result without replaying briefing |

Do not force tutorial speech into casual banter or solemn narration into slang.

## 3A. Speaker register continuity

For recurring direct dialogue, keep a small internal register baseline so the same character does not drift randomly between speech identities.

For Indonesian material, pay particular attention to:

```text
self-reference   → saya | aku | gue | other established form
listener address → Anda | kamu | elu/lu | Kak | other established form
negation         → tidak | enggak | nggak
softener         → saja | aja
social stance    → formal | everyday | intimate | sales-like | authoritative | regional/character-specific
```

Natural variation is allowed. The goal is not rigid vocabulary uniformity; the goal is **recognizable social voice**.

A shift is valid when the approved character or Moment motivates it—for example, a controlled speaker becoming briefly blunt under pressure. Randomly mixing formal and highly colloquial forms without a character reason weakens actor continuity even when each sentence sounds natural in isolation.

Do not normalize every character into the same Indonesian register. Distinct characters may intentionally use different pronouns, slang density, cadence, or politeness.

# 4. Thought groups

A thought group is one breath-like unit with one dominant idea, image, action, or reaction.

```text
setup
→ important fact
→ implication / reaction
→ landing
```

Not every line needs every phase.

Good thought-group design:

- important information is not buried;
- new thoughts earn real boundaries;
- related words stay together;
- the final important phrase is not followed by unnecessary explanation;
- adjacent beats do not all share one cadence.

Grammar does not own performance segmentation.

# 5. Prosody through text

Use punctuation semantically:

```text
.  complete thought / reset
,  related continuation
?  questioning contour
!  textual intensity
—  pivot / interruption
…  hesitation / suspense / trailing weight
```

Use CAPS only for real contrast. Do not use punctuation as arbitrary timing code.

Natural rhythmic variation should come from thought shape before manufactured fillers, stutters, or ellipses.

# 6. Naturalness and Audio Tags

Audio Tags are **not a naturalness enemy**. They are Eleven v3 acting controls.

Correct relationship:

```text
spoken wording + thought groups
→ make speech natural

Audio Tags
→ make material acting direction explicit
```

Do not remove a tag that carries required emotion, subtext, projection, pacing, or reaction merely because the line already sounds conversational on the page.

Do remove:

- redundant synonyms;
- generic boilerplate with no audible job;
- directions that contradict the chosen voice;
- repeated state labels with no transition/generation-boundary reason.

Use `v3-expression-direction.md` for Expression Coverage.

# 7. Short lines: context, expression, no filler

A legitimate short line may remain short.

For connected same-speaker narration:

```text
short canonical line
+ previous_text / next_text or neighboring request context
→ better contextual prosody
```

If that short line must begin with a particular acting state, also anchor the state explicitly. Context and acting direction solve different problems.

For response-dependent dialogue, prefer Text to Dialogue.

# 8. Narration continuity

When narration is split across generation requests:

- split at semantic/emotional boundaries;
- pass relevant adjacent context;
- preserve the narrative emotional arc;
- treat the new request as a possible acting reset;
- re-anchor the opening state when that state materially matters;
- do not repeat tags just because files are adjacent.

For example:

```text
VO-01: [reflective] setup
VO-02: [uneasy] reveal
VO-03: [urgent] action
```

If VO-02 continues the same reflective state rather than changing, it may still need `[reflective]` at its own opening when generated independently and that state is performance-critical.

# 9. Anti-flatness check

A line may be natural yet still too neutral.

Before finalizing, ask:

- Is there approved/necessary subtext?
- Does emotion materially change how the line should land?
- Is projection important (whisper, shout, intimate, projected)?
- Is pacing important (hesitant, rushed, measured)?
- Is there a reaction or state transition?

If yes, route the need to Expression Coverage rather than relying on natural wording alone.

# 10. Anti-overacting check

If a prompt feels synthetic on the page, inspect:

```text
synonymous tags
→ too many state changes
→ CAPS / punctuation overload
→ fake filler/reactions
→ voice mismatch
```

Do not solve overacting by deleting every tag. Preserve the smallest set that still carries material expression.

# 11. Preparation gate

Naturalness passes when:

- wording is plausibly spoken for the speaker/register;
- thought groups follow meaning rather than document syntax;
- listener load is appropriate to the current Moment and required facts are not expanded into checklist-like exposition;
- speaker register remains coherent unless an intentional character/moment shift explains the change;
- cadence is not mechanically uniform;
- filler/hesitation/reactions are justified rather than decorative;
- continuity planning prevents detached narration;
- naturalness edits have not removed required meaning;
- Expression Coverage remains intact.

Naturalness PASS is a text/craft judgment, not heard-audio proof.
