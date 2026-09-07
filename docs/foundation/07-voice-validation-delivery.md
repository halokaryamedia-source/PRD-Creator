# Voice Validation & Delivery

Status: active Flow 7 policy

## Purpose

Flow 7 decides whether the current Voice chain is safe to deliver. Default non-audio delivery is the same versioned project HTML containing PRD core + `04 Production Assets → Owner ID → Moment ID → AUDIO`.

Detailed operational validation lives in `kits/prd-creator/voice/VALIDATION.md`; this page owns durable boundaries.

## Canonical sequence

```text
voice_script_ready
→ revalidate current Flow 4 handoff
→ verify exact Voice source PRD revision + SHA
→ lifecycle-aware Voice mechanical validation
→ Communication Conservation
→ integrated Voice Script Readiness
→ current consolidated HTML
→ visual evidence when claimed
→ optional generated-audio evidence
→ exact Voice acceptance
→ voice_delivery_ready | needs_revision | blocked
```

## Mechanical chain

`validator/voice_validation.py` owns the Flow 5–7 domain checks and first reruns canonical `validate_handoff.py`. `validator/validate_voice.py` is the thin CLI/public entrypoint. Shared acceptance label/SHA parsing is owned by `shared/acceptance.py`.

The domain validator proves, as applicable:

```text
accepted PRD revision
= voice-state source_prd_revision
= render-data document.version
= voice-requirements Source PRD revision
= voice-production Source Voice Requirements revision

voice-state source_prd_sha256
= exact current accepted render-data bytes

voice-production Source Voice Requirements SHA
= exact current requirements bytes

Flow 5 Owner ID / Type / Speaker
= Flow 6 Owner ID / Type / Speaker

Flow 5 Owner ID + Moment ID
= current 04 page + stable moment grouping

HTML Voice requirement/production SHA bindings
= exact current canonical bytes
```

At `voice_delivery_ready`, it additionally proves Voice acceptance binds exact current `voice-production.md` bytes and every represented speaker has a non-empty Voice Cast selection/profile. The renderer enforces the same final-state cast boundary so a delivery-ready render cannot truthfully publish a pending selection.

Mechanical PASS does not establish semantic or visual quality.

## One Voice state schema

Flow 7 continues the same state owned by `shared/lifecycle.py`:

```yaml
status: voice_validation
source_handoff: state/handoff-state.yaml
source_prd_revision: <accepted document.version>
source_prd_sha256: <sha256 of exact accepted work/render-data.json bytes>
canonical_prd: work/content.md
requirements: work/voice-requirements.md
production: work/voice-production.md
project_html: output/v<accepted document.version>/prd.html
```

All refs are safe project-relative POSIX paths. Current state does not accept lifecycle aliases.

## Communication Conservation

PASS only when all `Must communicate` meaning survives, `Must not add/repeat` remains respected, authoritative timing truth remains honored, and Flow 6 polish adds/deletes no project meaning.

```text
Communication Conservation: PASS | FAIL
```

## Integrated Voice Script Readiness

Review Communication, Listener, Character, Performance, Timing, Continuity, and Operator concerns once:

```text
Voice Script Readiness: PASS | FAIL
```

Do not persist per-lens scorecards.

## Production Assets HTML

When visual readiness is claimed, verify:

- accepted 01–03 page/navigation identity remains unchanged;
- 04 is additive;
- each Voice resource is on its accepted Owner page and `Moment ID` group;
- resource title is `<Character> — <Line Title>`;
- Function, Voice selection/profile, Eleven v3, Estimated Duration, and Prompt are readable;
- Flow 5 internal fields/reasoning do not leak into reader-facing 04;
- copied Prompt remains canonical;
- claimed browser widths are readable.

```text
Project HTML Visual: PASS | FAIL | NOT PROVEN
```

Static validation cannot claim visual PASS.

## Voice selection

Preparation may use a clear target profile. `voice_delivery_ready` requires a non-empty Voice Cast selection/profile for every represented speaker. Actual Generation Mode requires the intended generation voice.

## Audio evidence

```text
Audio Evidence: not_provided | partial_review | reviewed_passed | reviewed_with_findings
```

Do not infer audio quality or measured duration from script/HTML appearance.

## Exact Voice acceptance

`work/voice-acceptance.md` authorizes the exact reviewed production source:

```text
# Voice Acceptance
Status: needs_revision | voice_delivery_ready
Mechanical: PASS | FAIL
Voice Script Readiness: PASS | FAIL
Communication Conservation: PASS | FAIL
Project HTML Visual: PASS | FAIL | NOT PROVEN
Audio Evidence: not_provided | partial_review | reviewed_passed | reviewed_with_findings
Findings: <only when findings exist>
Critical: N
Major: N
Accepted Voice Production SHA256: <exact current work/voice-production.md SHA-256>
```

The SHA binding is required for `voice_delivery_ready`. Editing wording, duration, Speaker metadata, section ownership, or Voice Cast after review invalidates the prior acceptance even when the PRD revision is unchanged.

The production source already binds exact Flow 5 requirement bytes, while Voice state binds exact accepted PRD bytes, so the chain has no version-only freshness gap.

## First wrong owner

```text
stale/changed PRD handoff or project/gameplay/story fact
→ PRD / Flow 4 authority

Voice Owner/Moment identity, scope, Speaker, Channel, Trigger, Purpose, required communication, source timing
→ Flow 5

wording, performance, Estimated Duration, Voice Cast selection
→ Flow 6

correct canonical Voice but stale/wrong 04 HTML
→ renderer/compositor

generated-audio-only issue
→ Generation Mode evidence/settings
```

## Delivery gate

`voice_delivery_ready` requires:

- current upstream handoff Mechanical PASS;
- exact current PRD revision + render-data SHA identity;
- Mechanical PASS across Voice lifecycle/identity/HTML freshness;
- exact current Voice Acceptance SHA;
- Voice Cast selection/profile for every represented speaker;
- Communication Conservation PASS;
- Voice Script Readiness PASS;
- current consolidated project HTML;
- Project HTML Visual PASS when visual readiness is claimed;
- Critical = 0 and Major = 0;
- truthful optional audio evidence.

It does not imply audio approval, client sign-off, implementation completion, or release.
