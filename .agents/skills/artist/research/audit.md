# Artist audit and competency map

Baseline: clean repository at **f95b842**, inspected 2026-11-25. This checkout is
`wayu-arts`, used here as the specialist-skill package for the user's The Stories
initiative. No separate The Stories application, runtime, API or hidden project
conventions were found or modified. English documentation, one self-contained
Artist folder, relative references, preserved presets/assets and implicit skill
discovery are the existing conventions. No AGENTS.md was found in the checkout
or its ancestor chain.

## Scope update

The user subsequently removed SVG production from Artist. Its guide, template,
mode, validator logic and T01/T08 evidence were removed. The baseline inventory
below records what was inspected before that scope change; retained behavioral
evidence is identified in the current evaluation. Raster/pixel guidance remains.

## Inventory actually inspected

Read SKILL.md; all eight baseline references (`production-contract`, `consistency`,
`style-guide`, `pixel-style`, `pixel-examples`, `image-guidelines`, `svg-guidelines`,
`stock-guidelines`); both Markdown templates and base.svg; agents/openai.yaml;
both asset READMEs and pixel prompt history; README and all four original docs.
Viewed all eight supplied PNGs in a labeled contact sheet and measured their
format/dimensions/mode. Thumbnail review is not pixel-level validation.

Strong baseline: practical short-request workflow, artifact/spec distinction,
scoped reference edits, authority/version rules, asymmetric identity, retry budget,
self-contained format modes, honest pixel target/export distinction and retained
examples. No baseline executable validation/scenario suite was present; historical
validation narratives are evidence of past work, not a rerun for this revision.

## Gaps, competencies and implementation

“Added” means guidance exists, not observed mastery. Evidence status and actual
trials are in [evaluation](../tests/evaluation.md).

| Competency / observable task | Baseline gap | Revision and evidence source | Remaining proof |
| --- | --- | --- | --- |
| Visual development: convert intent to competing visual hypotheses | Named exploration; no decision process or source basis | Added intent → hypothesis → cheap tests → selection vs production (A01/A02) | Test against diverse actual briefs and owner choices |
| Design fundamentals: diagnose hierarchy at use size | Checklist, little reasoning/trade-off | Added value/space/edge/depth tests and counterexamples (A05/A06) | Actual raster readability tests |
| Shape and silhouette: distinguish cast beyond palette | Brief mentions only | Added contextual shape/cast tests, stereotype limits (A07) | Blind cast recognition at target size |
| Anatomy/stylization: keep action and connected forms | “Check anatomy” without method | Added construction/support/contact tests (A08/A09) | Species/complex action research per brief; drawing trials |
| Expression/pose: change performance, preserve identity | Continuity locks; no diagnostics | Added landmark/action separation and focused/angry example (A09/A10) | Subtle-expression visual comparisons |
| Costume/turnaround: usable multi-view construction | Views and asymmetry, limited construction guidance | Added garment/strap/reach, volume/landmark checks, hidden-detail proposals (A03/A11) | Generated/editable turnaround checked across views |
| Environment/props: support geography and interaction | One short mode row | Added route/scale/functional states and receiver packet (A04/A12/A13) | Multi-angle set and grip tests |
| Composition/color/light/material | Listed categories, no decision tests | Added framing/value, projection, base vs illuminated color, profiles (A06/A12–A16) | Controlled export/viewing and lighting-variant trials |
| Art/style bible and continuity | Strong records; limited “why” and dependency review | Retained source of truth; added rule rationale, dependency impact and use-size fields | Validate revisions across real downstream assets |
| Image generation/editing/iteration | Good mode/tool rules; weak comparative review | Added region/preservation tests, evidence rubric and native-source distinction | Live model generate → edit → cross-view trial pending |
| Deliverables/handoff/revision | Director absorbs camera/audio/edit duties | Split specialty interfaces, receiver expectations, provenance/source metadata (A03/A04/A15 + local design) | Future-role interoperability |
| Rights/provenance | Stock originality only | Added source-use ledger, license limits and provenance distinctions (A19–A21) | External inputs still need project-specific checks |
| Accessibility | SVG title/desc mention only | Added purpose-based alternatives, non-color cues and scoped contrast (A17/A18/A22/A23) | Publishing-host integration not tested |
| Judgment and review | Unweighted checks, no repeatable gate | Added evidence/severity/correction/retest rubric | Generalization beyond the small trial batch |

## Boundaries and redundancy

Keep format mechanics in image/pixel references, canon/version facts in
consistency and the production contract, design decisions in the new craft guides,
and evaluation in review-rubric. Templates record decisions; they do not define
a competing method. Cross-links replace duplicated procedures.

Artist self-review checks visual craft. Future Critic will independently assess
intent/effect and cross-role evidence; it should not become a second image producer.
Artist composes stills and creates color/material keys; Cinematographer handles
shot/camera/light systems with Director. Artist does not own narrative structure,
screenplay, sound, timeline assembly or audience strategy. The proposed nine roles
are skills describing responsibilities, not nine spawned processes.

Asset finding: basic-style imagery includes technology names/logo-like details
that conflict with generic-stock rules. Kept images byte-for-byte, documented
reference roles and excluded those incidental details from the style contract.
Pixel examples remain generated visual references with unverified native grids;
no new claim of technical sprite compliance was introduced.

## Acceptance state

This batch improves Artist only. Completion requires source traceability, useful
progressive routing, intact packaging, meaningful scenario behavior and honest
capability limits. Passing structure/spec/review trials permits a scoped
pilot, not a blanket professional-production claim. Raster edit/identity and
multi-view visual tests remain a separate gate. Do not create the next role merely
to increase the skill count; follow the repository roadmap at `docs/SPECIALIST_ROADMAP.md` (maintainer document,
not an installed-skill dependency).
