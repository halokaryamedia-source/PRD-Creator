# Anti-Overdevelopment Simplification Decision

Date: 2026-08-10
Status: current

## Context

The BuildIT-parity remediation began adding revision fingerprints/checksums and deeper derived-artifact integrity machinery to PRD and Voice production. The user identified that this was making the repository harder to use and was no longer aligned with the repository's anti-overdevelopment rules.

## Decision

Prefer the simplest production chain that protects real failures without creating a second revision-management system.

```text
Source / canonical work
→ generate derived artifact
→ run focused validation
→ human/semantic/visual review where required
```

Do **not** require operators or canonical project files to carry SHA/checksum metadata for normal PRD or Voice production.

### Keep

- PRD structural validation and exact generated page-set checks;
- PRD script-safe glossary serialization and required shell-marker checks;
- Voice ID/Type parity;
- basic DOCX content/section/duration/performance presence checks;
- the real DOCX blank-page regression;
- focused CI that exercises actual renderer/builder/validator paths;
- controlled failure for concrete malformed input.

### Remove / do not continue

- PRD render-data SHA/fingerprint metadata;
- Voice Requirements SHA in canonical script;
- script SHA / DOCX revision identifier;
- separate derived-artifact revision registry;
- P1.5 test-discovery work without a demonstrated missed-test failure;
- P1.6 atomic-write work without a demonstrated partial-write failure;
- additional hardening phases merely because an audit listed theoretical possibilities.

## Empty Voice sections

A zero-entry `##` Voice section is invalid canonical Flow 6 input. The builder may reject it with a clear controlled error. No general Markdown parser framework is needed.

## Proof rule

Use the cheapest check that can falsify the changed boundary. Once the current production flow has enough evidence, stop.

A passing CI gate does not justify adding more machinery. `No change required` is a valid and preferred result when the remaining risk is theoretical or cheaper to handle procedurally.
