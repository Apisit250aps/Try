# Art review, revision and acceptance

Use for creation self-review and requested critique. This is a local evaluation
rubric, not a credential or an external industry standard. It operationalizes
[design fundamentals](../research/sources.md#a06),
[pose review](../research/sources.md#a09), and the project's existing contracts.

## Inspect before judging

Read the brief and reference roles. Look at the actual artifact, at delivery size
and a suitable enlarged view. For sheets/related frames compare the views side
by side. Separate source inspection, file measurements and visual inspection;
record which occurred. A prompt supports intent only. An image preview cannot
prove alpha, native pixel grid, editable source layers or a measured color profile.

For every finding, give location/view, observable evidence, effect on the brief,
severity, targeted correction and a retest. Distinguish defect from preference.
“Looks bad” is unactionable. “The notebook merges with the torso at thumbnail
size, hiding the requested grip; separate its value or hand placement within
locked blocking and retest at 160 px” is actionable.

## Scoring

Score applicable dimensions 0–3: **0** absent/contradicts task; **1** major defect;
**2** usable with a stated minor issue; **3** meets the brief with observed evidence.
Use **U** for uninspected and **N/A** when irrelevant. A specification may score
for specification quality; it cannot receive an observed-image score. Never
average U away or use a total score to excuse a hard failure.

| Dimension | Questions / evidence |
| --- | --- |
| Intent | Does the intended action/emotion read without invented story facts? |
| Design / hierarchy | Is the focal read clear at use size? Are shape, spacing and value serving it? |
| Construction / performance | Are volume, support, joints, contact, expression and gaze coherent for the chosen stylization? |
| Space / surface | Do scale, projection, light direction and material cues agree with the selected look? |
| Identity / continuity | Do face/proportions, anatomical sides, costume/prop IDs and persistent state match approved references? |
| Production / access | Is the actual artifact usable in the requested format/size, background, editability, crop and accessible context? |
| Evidence / provenance | Are actual inputs, changes, checks and unresolved source-use constraints traceable? |

Hard failures for the requested use: wrong mode/artifact (prompt passed off as
image), missing required input, unauthorized identity/story revision, broken
critical continuity, falsely claimed verification, or an unresolved asset-use
restriction that blocks the intended release. Treat that release issue as pending;
do not stop unrelated design work. A requested strict grid/alpha/source-layer contract
also fails until verified, even if the image is attractive.

A **reviewed deliverable** has no hard failure, no applicable 0/1, and an explicit
list of U/minor issues for owner assessment. A strict production requirement
cannot remain U. This marks review scope, not owner approval. A **draft** may
contain 0/1 with useful next steps. “Approved” needs recorded owner selection;
an ordinary one-off does not acquire a new approval ceremony.

## Revision loop

Rank fixes: brief/canon and action → silhouette/value/space → construction/contact
→ light/material → typography/edges/export. A failing export may need immediate
repair; the ordering prevents polishing an unusable underlying design.

For each attempt record the observed problem, proposed cause, allowed change,
reference used and resulting evidence. Change one main cause when diagnostic
isolation helps. A complete redesign can be justified by failed structure but
must remain inside the authorized change scope. Reinspect the affected area and
nearby identity/alpha/scene state; edits can repair a hand while damaging a face.
Do not rewrite canon to make the failed image pass. Follow the retry budget in
SKILL.md and preserve versions.

Example: if two expressions read as anger, first soften brow compression and
mouth tension while keeping facial construction. Counterexample: enlarging all
features and replacing the hairstyle makes a more cheerful character but fails
an identity-preserving expression edit.

## Skill evaluation is a different gate

Run the [scenarios](../tests/scenarios.md) after changes. Require evidence of
correct routing, meaningful design choices, boundary preservation, production
contracts and honest limitations. Compare overlapping tasks by decision and
artifact, not how many reference files were loaded. A prose-only pass establishes
reasoning behavior; actual raster generation, edit preservation and multi-view
identity need separate visual trials. Report partial acceptance by capability
rather than declaring professional mastery from one test batch.
