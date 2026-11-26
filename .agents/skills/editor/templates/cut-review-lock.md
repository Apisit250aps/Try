# Cut review, change request and picture lock

Review ID/version; reviewer relationship; unchanged brief/criteria version;
cut/sequence ID/version/hash; rate/timecode mode/start/count; actual files and
inspected modalities/ranges/tool/method; unassessed checks and reason.

| Note ID | Base cut / event / range | Expected / source | Observed / evidence | Interpretation / impact | Severity / confidence | Remedy / trade-off / owner | Authority / disposition | Retest / evidence / state |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CR-01 | Exact base | Protected intent or technical requirement | Fact, not a claimed feeling | Conditional if untested | Record both | Trim, hold, alternate, request | Pending / accepted / declined / accepted-risk | Open / implemented-unverified / verified |

## Change request

Request ID, author/source/date; base cut and affected locks; desired effect;
old→new order/ranges/media versions; canon/disclosure/performance consequence;
protected invariants; cost/coverage needs; approving authority and actual source;
new cut/version; invalidated color/audio/caption/VFX/export checks; unaffected
areas with reason; next owner and concrete acceptance test. Retain old cut.

## Picture lock record

- Exact cut/sequence version/hash, duration_frames, rational fps/timebase,
  record origin, displayed start timecode/mode; real reference locator/hash.
- Frozen scope: events/order/trims/retimes/graphics; permitted exceptions.
- Approval: who, source/date, version, delegated scope and conditions; pending
  if absent. Evidence inspected and blockers. No invented Director sign-off.
- Downstream recipients, current cut ID, handles and open work; actual receipt
  status. Final audio/color/captions/QC/release acceptance remains separate.
- Later authorized changes create a new cut and impact record; do not mutate
  the locked artifact in place.
