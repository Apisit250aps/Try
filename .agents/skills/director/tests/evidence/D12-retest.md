# D12 — Keep the answer behind the search

Creative review D12-DIR@v1. Evidence inspected: supplied packet descriptions only. No note image, shots, audio or timeline media were attached. PROP12@v1 is **produced-uninspected**; CUT12@v1 is an Editor-reported assembly, unviewed. This is a specification review.

## Located review and decision

**N12-01: cinematographer package, SH1 at SCR12@v2 S070 B1.** The supplied description says SH1 shows the entire note clearly while the object is discovered missing. CAN12@v1 N7 requires suspicion of theft until the hidden note is read. Exposing its explanation at B1 risks answering the question before B2's search and B3's reading. The contradiction exists in the described shot strategy; actual legibility and audience inference have not been tested.

Preserve N7's mystery. The intended progression is missing object → search for a possible theft → note discovered and read → reinterpretation as safekeeping. Actor direction should pursue the missing object and react to newly acquired information at B3; do not perform knowledge of the explanation during B1–B2.

## Adapter mapping

Incoming contract is `cinematographer-shot-package/0.1`. This outgoing record uses the provisional local `director-packet/0.1`; compatibility or receipt has not been demonstrated.

| Incoming field/source | Director record / preservation |
| --- | --- |
| upstream CAN12@v1 / SCR12@v2 | Separate canon and script sources, unchanged versions; N7 is the governing requirement. |
| scene.id=S070 | Scene identity S070. |
| narrative_beat_ids=[N7] | Narrative link N7; not merged with script IDs. |
| script_beat_ids=[B1,B2,B3] | Script links B1 missing object, B2 search, B3 explanatory note reading. |
| shots SH1/SH2/SH3 | Retain distinct shot identities; source versions were not supplied. Only SH1's content is described. |
| Editor statement CUT12@v1 uses SH1→SH2→SH3 | Reported cut order, not evidence that shot order equals beat coverage or that reveal timing passes. |
| Artist return PROP12@v1 | Asset identity and produced-uninspected state; appearance, placement and legibility remain unknown. |

No supplied values establish `checks`, `handoff`, proposed duration, alternates, shot paths or SH2/SH3 content. Request those from the relevant owners; preserve the original description and any later unknown fields rather than inventing defaults or claiming schema validation.

## Smallest coherent revision

Cinematographer: revise SH1 so it establishes the absence while the note and its explanatory contents remain concealed until B3. Prefer local framing/occlusion that leaves PROP12 unchanged. Label the replacement explicitly and retain the original SH1; version naming is for the owner to confirm. Review SH2/SH3 descriptions before accepting their reveal behavior.

Editor: substitute the corrected SH1 in a new CUT12 version and check B1–B3 for early readable glimpses, transitions and continuity. Keep SH2/SH3 and their ordering if compatible. Artist need only supply PROP12 for inspection unless the local framing solution fails; no global prop redesign or script/canon rewrite is justified yet.

## Acceptance handoff

Return the revised package with exact shot versions, PROP12 locator and playable cut. Director checks complete playback at intended delivery size: before B3 the explanation is inaccessible; at B3 it becomes readable and supports safekeeping; search remains motivated. A fresh-viewer question before and after B3 can test the inference hypothesis without universal-response claims.

Specification disposition: revise SH1; downstream assembly acceptance pending. Actual note/shot inspection and cut verification are blocked by absent media, while this review is complete. All briefs are not-dispatched; no receiver acceptance, creative approval of media or release approval is claimed.
