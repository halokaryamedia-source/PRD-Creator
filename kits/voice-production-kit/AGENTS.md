# Voice Production Kit Agent Rules

Read `SKILL.md` first.

Flow routing:

- Flow 5: `VOICE-EXTRACTION.md` — accepted PRD → voice requirements.
- Flow 6: `SCRIPT-PRODUCTION.md` + `DOCX-FORMAT.md` — voice requirements → canonical performance script/DOCX.
- Flow 7: `VOICE-VALIDATION.md` — current script/DOCX → final script/DOCX delivery acceptance.

For Flow 7:

- require the current voice state to originate from `voice_script_ready`;
- run `validator/validate.py` before semantic acceptance;
- compare every Voice ID to Flow 5 requirements;
- review terminology/pronunciation risk, speaker/channel/trigger consistency, and whole-project performance continuity;
- render the DOCX and inspect every page before visual acceptance;
- treat actual audio as optional evidence unless the task explicitly includes audio delivery;
- fix the canonical/root owner rather than patching the DOCX or audit report;
- do not claim generated-audio quality without actually reviewing audio.
