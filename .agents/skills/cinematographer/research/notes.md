# Claim ledger and research synthesis

Research precedes the skill's first implementation, 2026-11-25. C IDs resolve to
the [source registry](sources.md). P IDs identify bounded claims; H applications
and S choices are local synthesis. This is a provenance map, not a claim that all
sources agree, nor that every worked exercise was published by those sources.

## Evidence classes

- **P (physical/technical):** optical/capture relationships, scoped to assumptions
  and device/model. Check with measurements when implementing.
- **C (industry convention):** learned vocabulary and practice; may be violated
  deliberately, and job boundaries vary.
- **H (craft heuristic):** useful hypothesis/diagnostic, including this package's
  decision tables and original examples. Test effect; no guaranteed emotion.
- **I (cultural/contextual interpretation):** a reading supported by a particular
  story/genre/audience context; not a universal causal mechanism.
- **S (system design):** local ownership, schema, review, iteration and budget
  choices. Sources inform these; they do not prescribe this agent architecture.

## Claim to inspected source map

| Claim | Class / bounded proposition | Source IDs | Runtime use |
| --- | --- | --- | --- |
| P01 | C: distinguish scale, framing, POV, focus and movement; meanings depend on context | C01 | Strategy, camera |
| P02 | H: detail selection and reaction order can construct inference; Hitchcock offers one account | C20 | Strategy, examples |
| P03 | C: establishing, shot/reverse-shot and matches connect views | C02 | Strategy, coverage |
| P04 | H: organize frame information/hierarchy; composition offers choices, not only rules | C04 | Strategy |
| P05 | C/I: lighting/color/space participate in interpretation; hue/angle associations are not exclusive | C01, C03 | Strategy, light |
| P06 | C: continuity aligns spatial/temporal/action relations; axis is one convention, rhythm involves multiple elements | C02 | Continuity, timing |
| P07 | P: sensor dimension/focal length define approximate rectilinear FOV; viewpoint comparisons require a stated model | C05 | Optics and pinhole deduction |
| P08 | P: sensor crop changes recorded view; matched framing may change distance/lens | C06 | Camera |
| P09 | P: useful DOF needs a sharpness criterion; aperture/distance and diffraction interact | C07 | Camera |
| P10 | P/C: quality differs from intensity; effective source size/spill and key/fill functions matter | C08, C03 | Light; exposure trade-offs |
| P11 | P: WB/tint, ISO/latitude and recording/viewing choices are device-specific | C09 | Camera/light |
| P12 | P/C: shutter interval and frame rate govern blur sampling; 180° is conventional | C10 | Camera/time |
| P13 | P: source flicker and shutter/frame rate require capture tests | C11 | Technical diagnosis |
| P14 | C/H: pan baseline is conditional on playback/settings/content | C12 | Motion |
| P15 | C: shot-light treatment can work from visual-development keys | C13 | Light/look boundary |
| P16 | C: visualization communicates composition/action/timing/transitions/camera/sound within constraints | C14 | Boards/previs workflow |
| P17 | C: storyboard panels translate script/vision and prepare continuity/editorial work | C15 | Artist handoff |
| P18 | C: layout iterates camera/staging/rough action with adjacent shots | C16 | Animation/previs |
| P19 | Technical/H: Gen-4 guide favors simple motion and incremental iteration | C17 | AI adapter; not universal syntax |
| P20 | Technical: listed models support first/last conditioning | C18 | Capability checking |
| P21 | Technical: subject references are a distinct provider capability | C19 | Reference-role separation |
| P22 | H/I: Morano's quoted strategy used unseen areas in one film | C21 | Withholding counterexample |
| P23 | C: 30-degree guideline warns against near-duplicate angles | C22 | Continuity; narrow use only |

## S01 — Project ownership

Artist's current production contract at inspected commit `d13dc0f` assigns
camera/framing/screen direction/shot light to Cinematographer and assets/look to
Artist. Storyteller/Screenwriter drafts inspected during parallel work also
preserve IDs, versions, knowledge and owner decisions. This package adopts those
semantics without requiring sibling files at runtime. Director approval,
performance, canon, screenplay, final cut and sound treatment are not silently
absorbed. This is project design, not a universal DP job description.

## S02 — Interchange and validation

The versioned semantic packet, explicit narrative vs script beat types,
normalized safe region, primary sequence vs alternate coverage, panel IDs,
state comparison and local static checker are design choices. They prevent
information loss during parallel development; they do not establish a shared
application schema. Missing files, provider support, real timing and aesthetic
quality remain outside a JSON checker. The conditional 30-degree practice maps
to P23, not a new physical law.

## S03 — Generation iteration

One main action/simple motion as a starting hypothesis and two failed corrective
attempts as a stop/replan rule are local budget/diagnostic choices. They are not
universal model limits. Separate a desired shot from actual API controls, keep
identity/style/geometry/endpoints distinct and inspect intermediate states.
Vendor capability claims are not a success-rate benchmark.

## S04 — Review and practice

The eight-dimension 0–2 rubric and hard-failure gate are local, observable planning
criteria. A possible 4/5 viewer pilot threshold is an experiment design, not a
reported result. Same-author walkthroughs, deterministic packet checks and real
image/video/receiver trials must retain separate evidence labels.

## Tensions and decisions from research

1. **Optical shorthand vs a controlled comparison.** Yale/Brown/Canon-style
   descriptions sometimes bundle lens choice and distance. The skill records both
   and derives its zoom/dolly example using an explicit ideal camera. It does not
   claim a lens changes perspective while viewpoint stays fixed.
2. **Emotional recipes vs interpretation.** Historical angle/genre associations
   are examples; C01 explicitly allows contrary readings. Use audience-task
   hypotheses with counterexamples and tests, not blue/sad or low/power rules.
3. **Craft authority vs scope.** C16 describes layout artists proposing new beats;
   this skill can propose a story change but cannot silently authorize it. Project
   ownership supersedes a copied studio workflow.
4. **Control vs expressive flexibility.** Continuity supports inference, yet
   discontinuity/long takes can be intentional. Record purpose and recovery, not
   an automatic penalty or a fixed duration threshold.
5. **Model documentation vs real evidence.** Runway syntax guidance and Google's
   reference controls are separate cases; inspect the actual current tool. Exact
   lens numbers, identity, endpoint interpolation and negative prompts are never
   assumed to work identically across providers.
6. **Source quality is granular.** Adobe is useful for a narrow taught convention;
   its loose jump-cut examples are excluded. ASC access was partial/intermittent;
   only seen material supports claims. Source prestige does not fill unread pages.

## Research still needed when relevant

Specialized lens distortion/anamorphic behavior, stereoscopy/VR, VFX tracking,
calibrated color management, high-speed capture and real lighting hardware need
their own current manuals/measurements. Cultural readings need project/audience
context and appropriate consultation. The skill can plan a scoped test; it does
not claim specialist engineering or universal cultural authority.
