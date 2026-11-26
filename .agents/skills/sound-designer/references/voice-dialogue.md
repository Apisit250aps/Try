# Voice, dialogue and localization

P03/P04/P07/P08 in [notes](../research/notes.md) ground collaboration,
restoration and provider-specific timing controls. Performance instructions and
the following production choices are local heuristics, not measured guarantees.

## Direct a performance

Use a [voice profile](../templates/voice-profile.md): identity/locale/register,
objective, addressee, subtext, thought changes, pace/breath/energy, range and
continuity constraints. Translate Director intent into a playable action:
“keep your sister from hearing the fear” gives behavior; “sound emotional” does
not. Do not force accent stereotypes or impersonate a named performer as a shortcut.

Keep approved text separate from performance annotations. Mark exact line ID,
pronunciation variants, pauses and alternate takes. Suggest a wording change to
Screenwriter when speech cannot fit naturally; do not silently delete a negation
or speed the whole voice until the dramatic beat is lost.

## Dialogue edit and ADR

Preserve originals, production metadata, take IDs and selects. Check actual
recordings for intelligibility, clipping, plosives, sibilance, breath, noise,
reverb and perspective changes. Audition edits in context; room tone and short
crossfades can preserve continuity, but don't smear consonants or create comb
filtering by overlapping correlated takes. Avoid a hard gate that chops endings.

Try a better take or local repair before aggressive denoising. Compare at matched
level, inspect the removed-signal monitor if available, and listen for watery
modulation, lost consonants or altered identity. “Denoised” is an operation, not
proof of clarity. Unrecoverable lines become ADR candidates with rationale.

ADR brief: line/scene/cut/take IDs, exact text, available sync window, lips/impact
anchors, objective, vocal effort, distance/axis/mic/room reference and requested
handles. Record guide/playback availability. Match performance and acoustic space;
clean studio sound alone may fail against a location take. Never claim repaired
lip sync without checking the actual picture and returned audio.

## TTS and multilingual delivery

Use a licensed stock voice or a documented authorized custom voice. Confirm
scope for synthesis, training, languages, distribution, term and revocation
handling in [rights guidance](ai-rights-accessibility.md). A recording supplied
for editing is not automatically permission to clone its speaker.

Record provider/voice/model/version, locale, text/SSML revision, parameters,
request/result ID and actual output locator. Recheck current provider support for
SSML, phonetic alphabets, lexicons, rate/style and language combinations. An SSML
tag unsupported by one voice must not be promised because another supports it.

Keep a pronunciation table: written form, locale, intended spoken form, optional
supported phoneme notation, reference/approver and listening status. Include
names, numbers, dates, abbreviations and code-switches. Do not invent confident
IPA for an unfamiliar name; request a spoken reference or native-speaker check.
Protect semantic meaning and natural phrasing before fitting duration. Separate
source script, localized adaptation, spoken take and captions by line/locale IDs.

For lip sync, align the chosen audio take first, then send phoneme/viseme events
with provider units and timeline offset to animation/Editor. Azure documents
100 ns audio-offset ticks; convert units explicitly, then account for trimming,
resampling and retiming. Visemes are language/feature dependent and are not
one-to-one phonemes. Provider events are guides, not visual acceptance. Check
plosive closures, phrase starts/ends and drift in the actual muxed cut with a
receiver-agreed tolerance; native pronunciation and lip sync remain unverified
without the appropriate listener and media.
