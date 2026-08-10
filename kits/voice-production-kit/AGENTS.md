# Voice Production Kit Agent Rules

Read `SKILL.md` first.

Flow routing:

- Flow 5: `VOICE-EXTRACTION.md` — accepted PRD → voice requirements.
- Flow 6: `SCRIPT-PRODUCTION.md` + `DOCX-FORMAT.md` — voice requirements → performance script/DOCX.
- Flow 7: downstream validation/delivery; do not self-approve it during Flow 6.

For Flow 6:

- require `state/voice-state.yaml: voice_requirements_ready`;
- preserve the exact Flow 5 Voice ID set and type;
- `work/voice-production.md` owns spoken wording/performance notation;
- build the DOCX from canonical Markdown; do not use the DOCX as the editable source of truth;
- use the Aftershock DOCX only as a demonstrated quality/layout reference;
- return unresolved project facts upstream rather than improvising them.
