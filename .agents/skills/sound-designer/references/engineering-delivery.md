# Engineering, mix and delivery

Scope: ordinary file-based production and handoff; a spec is not a calibrated
studio or measured mix. P04–P06/P09/P11 in [notes](../research/notes.md) provide
evidence and limits. Resolve the receiver's current spec before mastering.

## Diagnose before processing

| Issue | Decision and actual check |
| --- | --- |
| Gain / headroom | Inspect sources, clip gain, inserts, buses and output for overload. Leave room appropriate to the chain; floating-point internal headroom does not repair clipped capture or guarantee unclipped export. Peak-normalization is not loudness normalization. |
| EQ | Identify rumble, resonance or competing bands by listening in context. Apply the smallest useful change, level-match bypass, check lost body/consonants; no default high-pass frequency or “cinematic EQ” for every voice. |
| Dynamics | Use clip automation for phrase balance, compression for a defined envelope problem and limiting for a required ceiling. Listen for pumping, flattened accents, noise lift, harshness and lost transients. Gate/expander settings must preserve tails and breath. |
| Masking | Choose which layer carries information at each beat. Try timing/density/level before spectral or keyed processing. A louder master cannot restore a masked word's relative prominence. |
| Phase / polarity | Check aligned microphones, stereo wideners and layered correlated sources. Polarity inversion and time/phase alignment are different operations. Test actual mono fold-down and image stability, not only a correlation meter; fix the cause rather than randomly flipping channels. |
| Perspective | Match direct/room balance, obstruction and distance across edits. Long reverb should not move an exterior source into a hall accidentally. Effects processing must respect protected clue intelligibility. |

Keep source masters, reversible edits and processing notes. Listen at comfortable,
known monitoring settings; don't describe a room or headphones as calibrated
without calibration evidence. Small-speaker simulation is a preview, not a real
phone test. Stereo spread and sub-bass must not be the sole carrier of an essential
clue. Ask whether a separate near-field version is required rather than flattening
all intended cinema dynamics by default.

## Delivery profiles, not one loudness number

Record destination/spec URL or supplied brief, version/access date, programme
range, full-programme vs dialogue-gated method, integrated target/tolerance,
short-term/momentary constraints if any, true-peak ceiling, LRA constraints if any,
channel map, sample rate/bit depth/codec, metadata and acceptance authority.
LUFS/LKFS describe loudness; dBFS sample peaks and dBTP reconstructed true peaks
are different measurements. BS.1770 names a measurement method, not a universal
delivery target. Whole-programme and dialogue-anchor readings are not interchangeable.

| Context | Evidence-backed boundary / action |
| --- | --- |
| EBU R128 v5 linear broadcast profile | R128 recommends programme −23 LUFS, generally entire-programme measurement, and maximum −1 dBTP for linear production. Its live/practical exception permits ±1 LU; QC measurement tolerance is ±0.2 LU. Do not import the older ±0.5 LU history as a blanket current requirement. Receiver-specific distribution limits may be lower. [EBU v5](https://tech.ebu.ch/files/live/sites/tech/files/shared/r/r128.pdf), clauses h–m. |
| Internet audio-only distribution | AES TD1008 explicitly excludes sound-with-picture. Its audio-only target tables are not film/OTT mastering rules; consult the actual recipient rather than copying a music-streaming value. [AES TD1008](https://aes.org/wp-content/uploads/2026/10/20210924_TD1008_v3.13.pdf), introduction. |
| YouTube upload | The opened official page recommends 48 kHz with AAC-LC, Opus or Eclipsa Audio options and channel-dependent encoding guidance; it does not establish a universal −14 LUFS delivery requirement. Verify the relevant upload path/profile. [YouTube settings](https://support.google.com/youtube/answer/1722171?hl=en). |
| OTT, broadcaster, festival or cinema | Obtain that recipient's current specification. Cinema monitor/reference level, dynamic intent and delivery format cannot be replaced by an invented LUFS target. Unknown destination leaves mastering acceptance pending. |
| Client says −16 LUFS / −2 dBTP | Treat as a supplied project requirement with declared measurement method/tolerance, not a platform fact. Keep a separate profile from the broadcast export; remeasure each final deliverable. |

Silence-only or very sparse cues may yield undefined/nonfinite integrated results;
don't substitute zero LUFS or boost silence to hit a target. Stems generally retain
mix balance; do not independently normalize every stem to the master target.
Short-form may have additional receiver limits: duration alone doesn't imply
the correct short-term/momentary specification.

## Measure and export when files and tools exist

1. Confirm actual file, intended stream/channel map and complete measurement
   range. Inspect actual rate/layout/duration; attach a hash when useful. Record
   tool/build, filter/meter settings and logs, including no-result/error states.
2. Measure input, make a reversible mix/master adjustment, then measure the
   exported file separately. A target setting is not an output result. Decode
   lossy delivery for a post-encode peak/listening check; sample conversion and
   encoding may change peaks. Retain both master and decoded-delivery evidence.
3. Verify sync at start, middle, end and critical anchors; check delay/drift, channel
   order, truncation, clicks, tails, clipping, missing content and exact timeline
   start. Inspect full programme where feasible; disclose sampled coverage.
4. Audition full mix, dialogue/speech, effects and music in context; test mono,
   headphones and intended speakers/device. Name actual devices and ranges.
   A meter cannot prove intelligibility, dramatic effect or artifact absence.

Optional FFmpeg measurement recipe, **only if installed** and compatible with
the receiver's metering method. Replace the file with an actual inspected input
and select the correct audio stream. This is analysis to a null output; it does
not create a delivery master:

```bash
ffmpeg -hide_banner -nostdin -i "actual-mix.wav" -map 0:a:0 -af "ebur128=peak=true" -f null -
```

Check local `ffmpeg -h filter=ebur128` and the
[official filters manual](https://ffmpeg.org/ffmpeg-filters.html#ebur128).
No installed filter or media means leave this unexecuted. For `loudnorm`, read
its current documented two-pass controls before using it: supplying measurements
does not guarantee linear mode; unsupported target/headroom conditions can cause
dynamic fallback. Confirm mode, output sample rate and final measurements; don't
apply a copied default target to every project. [FFmpeg loudnorm](https://ffmpeg.org/ffmpeg-filters.html#loudnorm).

## Mix, stems and archive

Use the [mix/stems plan](../templates/mix-stems-plan.md). Declare DX (dialogue),
MX (music), FX (effects), and optionally split Foley/ambience/VO; their sum/rebuild
behavior must be agreed. Keep common origin, duration, sample rate, channel order,
tail/handle policy and version. State wet/dry, shared returns, bus processing,
sidechain dependencies and master limiting. Nonlinear bus processing may prevent
a simple sum from matching the master; provide reconstruction instructions and
a real comparison/tolerance rather than claiming an unperformed null test.

M&E (music and effects for localization) must remove original dialogue while
retaining required nonverbal action/effort under the agreed scope. Shared baked
dialogue reverb, source music with speech or dialogue baked into generated FX
requires explicit handling; muting the DX stem alone may be insufficient.
Deliver approved language versions, captions/transcripts, registry, cue sheet,
QC logs and unresolved exceptions together. Archive source/project links and
plugin/version dependencies; stems alone may not reconstruct an editable session.
