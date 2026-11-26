# Model-agnostic timeline record

Local `editor-timeline/0.1`, system design P15. JSON example:
[silent-30s.timeline.json](../examples/silent-30s.timeline.json).
It represents editorial intent independently of generation model/NLE. It is
neither OTIO JSON nor CMX EDL nor FCPXML. The narrow offline validator below
does not certify this entire semantic contract or external applications.

## Identity, status and provenance

| Record | Required meaning |
| --- | --- |
| Header | `contract`, packet/cut ID/version, project/episode, upstream locators/hash/version/status, assumptions, tools and material gaps. |
| Sequence | `id`, `version`, rational `rate` in frames/s, reciprocal `timebase`, `start_timecode` string or null, `timecode_mode` NDF/DF/unknown, record origin (local 0), `duration_frames`, lock state and approval source. |
| Scene/shot/beats | Stable typed IDs and versions; shot→scene, narrative and script beat links, purpose, protected information/state and order dependencies. A shot may span beats; several events may select one shot. |
| Asset | `id`, `version`, `shot_id`, locator/hash or null, native rate, source-timecode origin, timing mode CFR/VFR/unknown, estimated/observed availability, used proxy/original mapping, generation provenance, inspection/rights. |
| Track | `id`, kind video/audio/caption, explicit role/order; audio channel/sample map when present. Gaps are explicit events, not missing media disguised as black. |
| Event | Stable ID/version, shot/scene/beat and asset/version refs; source and record ranges; speed/mapping, transition, handles, sync group/anchors, narrative purpose, dependencies, lock and evidence states. |
| Outputs | Planned profile distinct from actual rendered locator/hash/log, verified checks (range/modality/method/result), acceptance and unassessed checks. |

In machine records source `in/out` units follow the asset's declared rate; record
`in/out` are sequence frames. Audio source can be integer samples with its
samples/s rate; frame positions may be supplemented by an exact sample anchor.
Do not call samples frames. All intervals are half-open. Availability can be null
when missing, but used ranges then remain estimates and cannot prove exportability.

## Deterministic linear validation subset

`scripts/validate_timeline.py` validates **CFR forward constant-speed video** and
**constant-speed sample-domain audio** event arithmetic. Core fields are shown in
the example. It checks unique/referential IDs, typed beat membership, scene/shot
mapping, positive rational rates, reciprocal timebase, positive integral ranges,
speed relation, media bounds/handles when known, record bounds, video-track
coverage, transition handle needs, beat-order constraints and evidence state.
It checks sync anchor math when supplied. It does not open media or adjudicate
performance, causality, approval authenticity, color, captions or mix quality.

Video events on one track use adjacent nonoverlapping **nominal** record ranges.
An event's incoming `transition` is `cut` or `dissolve`; a dissolve has `before`
and `after` sequence-frame offsets around the nominal boundary. It consumes
incoming pre-handle for `before`, outgoing post-handle for `after`; it does not
add duration. Both offsets convert through rate and speed. Other models may
represent overlap differently; convert, do not copy numbers blindly. Audio
overlap uses separate tracks. A gap event has no asset, but a purpose and record
range; the validator supports gaps on video tracks. [P10, P15]

`handles.pre/post` are **available** unused source units, not requested margins;
null is unknown. Positive handle claims require known availability and cannot
exceed it. A planned source may have an estimated available range but it remains
unobserved; an observed range requires an evidence locator. Audio and video
must each satisfy their own duration relation. Linked clips may have different
record boundaries for J/L cuts without shifting their original sync anchors.

`sync_anchors[]` contain event ID, source position, record frame position and
agreed tolerance in record frames. Positions may be rational `{num,den}` when
audio samples do not fall on frame boundaries. The validator accepts integer
anchor positions for this subset and compares the mapped position exactly to
the supplied tolerance; fractional positioning remains a manual check.

`order_constraints[]` specify typed beat `before/after` IDs. The checker compares
earliest event starts; this is a limited disclosure-order guard, **not** proof
that the required action is visible or that a clue is readable. A beat that
must finish before another begins needs an additional manual interval check.
Missing required beats fail rather than quietly removing the constraint.

If nonlinear retiming, reverse/freeze, VFR/PTS, nesting, compositing, captions,
transition types or effects exceed this subset, keep the semantic record and
declare validation unsupported. Use a separately validated adapter or baked
asset/version. Never call an ignored field successfully executed. [P15]

Run from any directory with Python's standard library:

```bash
python3 scripts/validate_timeline.py examples/silent-30s.timeline.json
```

The paths above are relative to the installed Editor folder. No tools are
downloaded and no media is rendered by that command.

## Interchange capability gate

| Format | Requirement before claiming support | Current package status |
| --- | --- | --- |
| Paper CSV | Explicit units/IDs/versions; verify arithmetic and human interpretation. | Template provided; no external importer claimed. |
| OTIO | Installed version/adapters, actual serialized file, read-back equality for used properties and intended receiver check. | A bounded core `.otio` smoke test can be run with the test harness; see actual evaluation. OTIO carries edit metadata, not a rendering engine or embedded codec. |
| CMX EDL | Concrete exporter/importer, timecode/reel conventions, transition/track limits and round trip. | Not implemented/validated. Do not rename the CSV `.edl`. |
| FCPXML | Exact version/schema and receiver, audio lanes/roles, retimes/compound clips/media IDs round trip. | Not implemented/validated. Legacy FCP XML and FCPXML are not interchangeable names. |

OTIO's native adapters and optional plugins have different installation/support
scope. Core serialization success cannot establish CMX, AAF or FCPXML support.
Effect interpretation and missing/extended ranges can differ by consumer; check
actual media and rendered conform independently. [P10]
