# Sound spotting and cue sheet

Use [timing rules](../references/production-contract.md#timing-rules).
An empty production row does not represent existing audio.

## Header

- Contract: `sound-packet/0.1`; project / episode / packet ID / version / status:
- Story/script/shot/bible/cut IDs / versions / locators / authority:
- Inspected media/ranges/tools; missing materials and assumptions:
- Sequence origin / start TC / rational fps / DF or NDF / CFR or PTS mapping:
- Timeline duration / sample rate / channel layout; source-time mapping:
- Interval convention: `[in,out)`; unit (frames/samples/seconds) and rounding:
- Narrative locks / delivery profile / acceptance owner:

## Spotting rows

| Cue ID / version | Scene / typed beats / shot IDs | Category / asset or take IDs | Narrative function / inference | Diegesis / listener / world source | Entry → exit / units / timing basis | Sync anchor IDs | Priority / silence / overlap / tails | Rights / consent | Caption note | Owner / acceptance test / evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Categories can be DX, VO, ADR, Foley, ambience/room tone, SFX, MX or intentional
silence; silence is a design record, not an asset to generate or normalize.
Bridge rows name both scenes. Preserve typed upstream IDs and many-to-many links.

## Sync anchors and source edits

| Anchor ID | Cut / scene / shot / line / version | Observable event | Time domain / position / units | Estimated or verified / basis / uncertainty | Allowed tolerance / receiver |
| --- | --- | --- | --- | --- | --- |

| Cue / asset / take | Source in/out / offset and rate | Sequence placement | Handles / tail / stretch / processing | Stale dependencies / recheck |
| --- | --- | --- | --- | --- |

## Music rights reporting extension

For the recipient's actual reporting form add composition title, composer,
publisher, recording/performer, usage type and duration, ISWC/ISRC if known,
rights evidence and status. An internal spotting sheet is not a filed rights report.

## Revision and handoff

- Old/new cut and packet / authorization / changed cue IDs / split/merge map:
- Actual paths or absent assets; planned vs performed checks/logs:
- Field mapping / unresolved references / stale captions, stems and visemes:
- Receiver / requested check / actual receipt and scoped acceptance, if any:
