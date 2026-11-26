# Finishing, handoff and QC

Technical P07–P13 and local workflow P16 are traced in [notes](../research/notes.md).
Use the [handoff template](../templates/finishing-handoff.md) at the relevant stage.

## Ingest, organization and conform

Retain original media and supplied folder/card structure. Inventory stable
asset/version/take IDs, locator/hash, reel/camera metadata, original timecode,
rate/PTS, dimensions/PAR, color interpretation and audio channels/sample rate.
Check files are readable; checksum equality verifies copying, not image quality.
Organize bins by project/episode/scene/take and label selects/rejects without
deleting the original. Keep project files/autosaves and versioned exports separate.

Use proxies only when performance needs them. Preserve source-to-proxy identity,
duration/start, rate, audio/channel mapping and relink criteria. Before online,
reconnect originals and inspect edit boundaries, orientation, retimes, effects,
levels and grades against the offline reference. A proxy can hide subtle focus/
image defects; check the intended viewing scale. Do not assume an application
always exports originals: some offer an explicit proxy-export setting. [P03, P07]

For a conform hand off: cut/version/hash, clean and burn-in references, source
manifest, record origin/rate/counting mode, event mapping and handles; retime/
stabilization/reframe/effect list and baked/unbaked status; missing media and
accepted exceptions. Verify returned picture against the locked reference at
every join and effect range, plus start/end/duration. Interchange losses need
explicit workarounds and a recheck, not “should import.” [P10, P16]

## Color, audio and captions

**Colorist:** provide originals/relink map, cut and reference versions, color
metadata, viewing transforms, LUT/CDL versions and intended look; distinguish
temp correction from baked transforms. Agree managed working/output space and
delivery range. On return compare sources, reframes, retimes, identity/detail
and continuity; scopes/metadata alone do not establish calibrated appearance.
Resolve/Adobe docs document workflows, not proof this project was graded. [P12]

**Sound Designer/mixer:** provide frame-accurate reference with cut ID, fps and
timecode burn-in where supported; sample/channel map, sync anchors, source
audio, cue placement, handles/tails, guide/temp status and change list. Request
stems only to the receiver's actual specification. Confirm common start and
duration, silence/padding convention, channel labels, rights and loudness/peak
target *with its source*. Do not impose one web/broadcast loudness target on
every destination. Listen/measure returned mix at appropriate scope; Editor
can verify placement without claiming authorship of the mix. [P08, P16]

**Captions/accessibility:** use the final cut/audio, correct names/meaning,
speaker identification and significant non-speech sound. Review automatic text;
test timing, line breaks, spelling, collisions with graphics/UI, reveal leakage
and target-player rendering. Language subtitles may omit sounds needed for
accessibility. A silent video's visual information may need a description/
transcript alternative; do not fabricate speech captions for it. Check whether
the requested player needs sidecar, embedded or burned-in captions and retain
a clean master where appropriate. WAI describes needs; this package is not a
legal-compliance certificate or player compatibility test. [P13]

## Delivery profile

Before final export, record destination specification URL/document/version/access
date, delivery owner, raster/PAR/orientation, exact rational rate, progressive/
interlace state, codec/container/profile, bit depth/chroma/bitrate constraints,
color primaries/transfer/matrix/range and HDR metadata if required; audio codec,
sample rate/channels/map/loudness/true-peak limits; captions, slate/leader/tail,
naming, checksum and acceptance test. Unknown requirements stay unresolved.
For an unspecified review file, propose a clearly local review profile, not a
platform-certified master. Do not extrapolate SMPTE timecode into a codec spec.

Render only with supported tools/codecs/filters and actual media. Keep settings,
tool/version, input manifest and command/project locator; capture stderr/logs
and exit status. In FFmpeg, verify stream mapping, timestamp resets after trims,
normalized stream properties and output cadence. A successful process exit is
one check, not final QC. Transcoding may create new cadence/color/artifacts and
must be checked. [P11, P12]

## Inspect the delivered file

| Pass | Evidence to record | Failure response |
| --- | --- | --- |
| Identity / metadata | File/hash, cut and profile versions; readable streams, exact frame count/rate, dimensions/PAR, audio channels/rate, duration. | Wrong cut/profile → new export and invalidate prior export checks. |
| Full decode | Actual decoder/version/log and complete range; truncation/corruption/missing-stream results. | Fix/relink/re-render; don't waive because the thumbnail plays. |
| Picture | Full-speed viewing plus frame checks at joins, reveals, retimes, AI defects, titles, black/freeze/flash or missing slates. | Distinguish intentional black/holds from defects; log ranges. |
| Sound / sync | Actual listening setup/range and measurements; start/mid/end sync, dropouts/clipping/phase or channel errors. | Reconform only affected cues/stems, then recheck actual returned mix. |
| Color / graphics | Intended display and transforms, legal-range method if required, output tag/pixel consistency, safe-area/readability evidence. | Incorrect tag vs incorrect pixels require different repair; consult colorist. |
| Captions / access | Actual timed file/player/device, language review, spoiler/readability/overlap checks; description alternative if requested. | Correct/re-time and inspect in the target player again. |
| Acceptance | Director/user creative decision, technical acceptance owner, rights/release scope and source. | Report ready-for-decision or blocked checks; no invented acceptance. |

Automated black/freeze/silence detection produces candidates; long takes,
intentional black and designed silence can be correct. Watch/listen and compare
to brief. Sparse frame extraction proves only the extracted images. If full
playback or hearing is unavailable, report technical decode results and the
unassessed perceptual checks separately. Preserve QC logs, exceptions and prior
exports; a revision invalidates results for the changed artifact.
