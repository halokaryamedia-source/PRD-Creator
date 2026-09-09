# Families and variation

Read for multiple sounds that must represent one recurring source. This is repository production policy. Product limits are in [contracts](elevenlabs-contracts-and-sources.md); approval evidence is in [validation](validation-and-delivery.md).

## Baseline, not a new identity system

Use the existing **SFX Family Baseline** concept. Do not create a second Sonic DNA schema. Keep a small set of audible invariants: physical source, core/secondary timbre, resonance, characteristic movement or breath, compatible perspective, intensity envelope and no-drift boundary. State changes are deltas, not unrelated descriptions.

Same text is not an identity lock. The documented SFX endpoint lacks voice casting/reference-audio conditioning controls. An approved audio file is a listening comparator, not an unsupported input parameter. Never promise that descriptors alone guarantee identical timbre across generations.

## Design assets from audible requirements

For each approved state/event, decide whether its audible information actually differs:

| Need | Cheapest quality-preserving route to consider |
|---|---|
| Same event in another moment | Reuse accepted asset when rights/context allow |
| Small loudness/presentation difference | Playback setting or non-destructive edit |
| Different cadence of the same contacts | Reuse contacts with target-supported timing |
| Noticeably repetitive performance | Add a genuinely distinct take only when repetition is a demonstrated problem |
| Different mechanism, vocal action or material | New sound or independently controlled layer |
| No justified audible difference | No additional asset; do not fill a state checklist for symmetry |

Reuse cannot erase a required distinction. Pitch shifts may change perceived size/identity and timing; do not use them to disguise a wrong mechanism or replace a required performance. Runtime randomization is an implementation option only when supported by the target; random selection is not automatically no-repeat/shuffle behavior.

## Representative-state gate

```text
approved family scope
→ select the state that best exposes identity and range
→ inspect existing approved files before new generation
→ bounded representative-state generation/review
→ approve identity using a retained file
→ expand only approved dependent states
→ compare each against the anchor and intended delta
```

The representative state need not be idle. For an attack-focused creature, a warning or action may expose identity better. For a machine, sustained load may reveal the core tone. Use one sufficient representative, not a mandatory audition suite. Preparation can recommend an anchor strategy; it cannot approve unheard identity.

With no accepted anchor, do not bulk-generate the family speculatively. Reuse an already accepted same-project anchor without asking the user to reconfirm it. Expansion must still fit the approved batch scope and remaining budget; approving sound quality does not reset either.

## State transitions and intensity

For an approved machine startup → run → shutdown, decide whether states are independently triggered. A combined clip is suitable only when the sequence is fixed. A variable-duration run usually needs separately managed onset, sustain and release; the playback owner must implement transitions rather than assume generation supplies them.

Keep identity-related descriptors stable across states. Vary the action, load, onset, modulation or breath appropriate to that state. When intensity matters, compare a small relative ladder in context: resting, attentive, warning, peak action. These are internal review positions, not mandatory states or asset counts. A warning must not accidentally overpower the peak action unless the project intends that distinction.

## Example family comparison

For an approved electric motor family, retain electric whine plus low rotor character. Idle may have steady light vibration; working load may intensify rotation; shutdown may descend and release. Do not introduce combustion exhaust in one state merely because it sounds impressive. Do not require identical pitch at different loads when a pitch change is the correct state delta.

For creature footsteps, the useful asset may be a contact family rather than a file named for a full walk cycle. Contact material and gait timing are separate decisions. A different floor does not automatically justify regenerating the creature's vocalizations.

## Variation budget and approval lock

Sample count follows exposure, identity needs and observed repetition, not a fixed 4/6/20-take recipe. Compare the group actually returned by the selected surface. Preserve multiple usable results from the same authorized generation when needed instead of discarding them and paying again.

Approved anchor + selected states + minimal exact prompt/settings/file references belong in existing project execution notes. Do not add family metadata to the strict asset-requirements grammar. Preserve originals and record edits as derivatives. After a baseline change, reopen only states whose accepted identity is invalidated; do not regenerate every sound in the project.
