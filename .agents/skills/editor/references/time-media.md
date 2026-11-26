# Time, media and technical interpretation

Read [timeline contract](timeline-contract.md) before machine-readable work.
Technical claims P06–P12 are traced in [notes](../research/notes.md).

## Three clocks, not one

- **Source:** each asset's native frame/sample/PTS coordinates, rate, available
  range and original timecode origin. File-relative frame 0 need not mean
  timecode 00:00:00:00; multiple reels can share the same labels.
- **Record:** position in the sequence; choose a sequence origin separately from
  displayed start timecode. Record in/out belong to its rational frame rate.
- **Presentation:** actual stream timestamps and playback. Codec timebase
  (seconds per timestamp tick) may differ from frame duration. `1/90000` ticks
  does not mean 90,000 fps. VFR has nonuniform frame timestamps. [P06, P07, P11]

Use half-open intervals `[in,out)` everywhere locally: duration = out − in,
last included frame = out − 1. Some external formats display inclusive out;
convert explicitly at their boundary, never add one throughout the packet.
Use integer positions with a rational **units-per-second** rate `{num,den}`;
for fps `24000/1001`, one frame lasts `1001/24000` seconds. Keep the reciprocal
timebase `{num:1001,den:24000}` separate. No decimal 23.98 arithmetic. [P06, P15]

For constant forward speed `s` (source seconds per record second):

```text
source_seconds = (source_out - source_in) / source_rate
record_seconds = (record_out - record_in) / record_rate
record_seconds = source_seconds / s
source_at_record(r) = source_in + (r-record_in) * source_rate/record_rate * s
```

Example: 100 frames at 25 fps is 4 seconds; at normal speed in 24 fps it needs
96 record frames. Reinterpreting those same 100 frames as 24 fps is instead
25/6 seconds, a deliberate speed of 24/25. Do not confuse resampling cadence
with slowing the performance. A 240-frame source at `24000/1001` is 10.01 s,
not 10 s. At 48 kHz that is 480,480 samples. For a single such frame the sample
length is 2,002; other rate/sample combinations need explicit rounding. [P06–P09]

When an exact duration is not a whole number of record frames, select and record
a rounding/conform policy and residual; inspect drift over long scenes and at
the end. The local validator requires exact integral record allocation; it
rejects unrepresented residuals rather than making a hidden rounding choice.
Nonlinear/reverse/freeze/optical-flow/VFR edits need an explicit mapping/baked
version and separate checks; the validator does not support those mappings.

## Timecode labels

Frame rate and timecode counting mode are independent metadata. NDF advances
labels without the DF compensation; at `30000/1001` a nominal 30-frame NDF hour
is not one wall-clock hour. DF omits **numbers**, not image frames. SMPTE
ST 12-1:2014 §5.2.2 specifies omitting 00/01 each minute except each tenth minute
in the 30-count convention. This does not license DF at 24/25 fps. [P06]

For 59.94/high-frame-rate, interlaced/frame-pair labels, midnight rollover or
external EDL requirements, inspect the applicable representation and importer;
do not extrapolate punctuation into a specification. This package neither parses
nor emits SMPTE timecode. Its validator merely restricts a DF declaration to the
two rate families it recognizes. Consult current delivery specifications before
compliance claims; the accessed 2014 standard is a versioned source, not a claim
to have checked all later revisions.

## Handles, retiming and sync

Available range describes actual media; used range describes the selection.
Pre/post handles are unused media before/after it, in source units. An estimate
of 12 spare frames is not an observed handle count. Dissolves require sufficient
media on each side of the cut; at mixed rates/speeds convert record-side
transition offsets to source units, including rounding if needed. A tail can
extend audio beyond picture without extending narrative runtime. [P09, P10]

For J/L cuts retain original link/sync-group IDs. Map an identifiable mouth,
clap/contact or shared source timestamp to sequence position and compare against
its sound sample. Report expected/measured offset and agreed tolerance. Check
start, middle and end for drift; aligning only the first syllable is insufficient.
Audio retiming, pitch preservation and sample-rate conversion need explicit
methods and audition, owned with Sound Designer. `48 kHz` labels alone do not
guarantee sync; clock drift and wrong interpretations remain possible. [P08, P15]

## Media choices

Record dimensions, pixel aspect ratio, display aspect ratio, orientation and
interlace/progressive state. A 1080×1920 square-pixel frame is 9:16, but a source
rotation flag or nonsquare pixels changes the interpretation. Safe-area values
are project/destination constraints; a provisional rectangle is not a platform
certificate. Check subject and caption readability in the actual output. [P12]

A **container** (e.g. MOV/MP4/MXF) holds streams; a **codec** (e.g. ProRes/H.264)
encodes them. Resolution does not specify codec, bit depth, chroma, transfer
function, range or quality. An edit-friendly transcode/proxy can improve response
but must preserve source identity, duration, sync/channel layout and relink
mapping. Never replace the original to save an extra record. [P07, P12]

Separate input color interpretation, working/timeline space, viewing transform
and output space. Verify missing/wrong metadata with the responsible colorist;
assigning a tag is not the same as transforming pixels. Track LUT/CDL/version,
RAW/debayer settings, alpha handling and whether a look is baked. Avoid applying
the display transform twice. A codec tag or small preview does not establish
calibrated color accuracy. [P12]
