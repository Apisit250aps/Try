# Measurement and experiment judgment

P05/P06/P10/P11 in [notes](../research/notes.md). Definitions below reflect
consulted documentation on 2026-11-26, not perpetual definitions. Recheck the
actual product/export. Missing or ambiguous definitions block dependent ratios,
not the entire strategy. Do not impute missing data as zero.

## Build the dictionary before diagnosing

| Measure | Definition / denominator / limits |
| --- | --- |
| Impressions / reach | Impressions count eligible displays under a particular surface rule; reach is generally a unique-account/person estimate only where the product defines it so. Never assume every display is eligible or that reach sums across posts. YouTube registered-thumbnail rules and exclusions are in S02. Instagram Help reach definition was inaccessible in this development pass; require native tooltip/export evidence. |
| YouTube views / engaged views | S01 distinguishes Shorts starts/replays from engaged views after its dated 2025 change. S02's currently inspected text also describes starts across formats. Preserve definition era; never merge an older view series without a break note. S01's engagement threshold is not numerically specified: don't invent seconds. |
| YouTube CTR | Views originating from registered thumbnail impressions / those registered impressions × 100 (S04). Total views / impressions is incorrect when other traffic exists. Not a universal Shorts feed swipe metric. |
| Retention / AVD / APV | Retention needs native eligible viewing base at each point. AVD uses corresponding watch time / the documented view base; inspected S03 uses engaged views. APV needs the native percent-viewed definition, eligible base and duration treatment, or a clearly labeled derived calculation. Only derive AVD / duration × 100 for a fixed-duration, compatible base; not a cross-platform native APV claim. |
| Completion | Completed eligible plays / eligible starts × 100 only when those events share counting/session rules. TikTok Ads S10 defines paid in-feed play/quartile metrics, **not** organic Studio metrics. An “at least 6 seconds OR interaction” metric is not pure six-second viewing. |
| Rewatch | Use the reported replay rule or a declared proxy; never infer unique rewatchers from views minus reach. Views/reach is exposure frequency only under compatible coverage and is not a replay count. APV over 100 can reflect repeats under some definitions; don't clamp blindly. |
| Shares / saves | Keep native counts, whether events or unique accounts, attribution and window. Derived shares per 100 eligible views = shares / that view base × 100, labeled as a local rate; shares / reach is a different rate. Availability/definitions vary; don't invent a saves field. |
| Subscriber/follower conversion | Attributed new subscribers / specified eligible viewers or views, with attribution window and scope. Net follower change / views is a different proxy influenced by unfollows and other posts. Without attribution, don't call it episode conversion. |
| Business conversion | Observed defined actions / eligible exposures or sessions under a declared attribution method/window, with privacy limits. Correlation or last-click credit is not incremental causal return. |

Record each metric's platform/surface/format, native label/definition version,
unit, counting and replay rules, numerator/denominator, source/export time,
window/timezone, post age, paid/organic, traffic source, cohort/locale/region,
estimated/observed status, missingness and uncertainty. No computed rate for an
unknown denominator or zero exposure: use undefined/insufficient evidence.
Missing per-view distributions prevents trustworthy AVD uncertainty estimates.

Instagram S13's 2023 watch-time formula and S14's changed plays definition are
historical evidence of definition drift, not a current 2026 denominator contract.
TikTok organic definitions were not established by the accessible Studio launch
article S11. Preserve supplied native tooltips/screenshots/date; where absent,
report counts as supplied and suspend the affected calculation. Never substitute
Ads Manager or Creator Rewards “qualified views” for organic public views.

## Compare like with like

Compare within platform, format/duration band, goal, post-age window, audience
and traffic source first. Use cohorts (new/returning, subscriber/non, locale) when
available and privacy-safe. A broader distribution can lower CTR while increasing
total valuable viewing. Stratify before diagnosing a packaging decline; pooled
averages can reverse segment-level direction. Do not average percentages without
eligible denominators; pool counts only if events, definitions, windows and
non-overlap permit it. Unique reach usually cannot be summed without deduplication.

Across TikTok/Reels/YouTube, compare goal attainment and within-platform change
against a comparable baseline, retaining separate definitions. Do not rank raw
view counts, add them as unique audience, or label one platform “best” from one
post. Report “definition unresolved” where necessary. Platform claims about
distribution are guidance, not an independently measured causal model.

## Diagnose before prescribing

Read actual content and segment curves alongside metrics: promise mismatch,
context burden, poor intelligibility, source change, novelty, seasonality and
measurement drift can explain the same pattern. S03 explicitly allows a spike
to mean confusion. Pair curve locations with comments/interviews and exact
episode/cut/version; do not invent a dip location without a curve. Use “consistent
with,” alternatives and a distinguishing next test. A viral one-off may have
little return or economic fit; assess series cohorts and repeatable production.

## Experiment plan, not fictional A/B result

Write the falsifiable hypothesis, mechanism, baseline/source, smallest worthwhile
effect (MDE), variants, one primary outcome plus guardrail and data-quality metrics,
analysis unit, allocation/exposure rules, window/post-age, stop rule and analysis
before execution (S22, S26, S28). A minimum sample depends on baseline rate or
variance, MDE, alpha, power, independent units and design; no universal “1,000
views is enough.” If these are missing, propose a pilot to estimate them and mark
power/precision unknown. Repeated views are not independent people.

Choose a design you can actually implement:

- Native concurrent test: verify supported account/format/features and record
  the platform's outcome definition and limitations. S27 currently excludes
  Shorts and selects on watch time; don't claim it runs on Reels or Shorts.
- Recruited randomized prototype study: define recruitment/assignment/consent,
  comprehension or choice task, sample plan and external-validity limits. The
  outcome is prototype response, not real feed retention or algorithm lift.
- Organic sequential/matched releases: keep comparable format, post age and
  audience as feasible; log time/topic/source/season/other changes. Call this
  exploratory observational comparison. Without defensible assignment and
  assumptions, do not attribute the difference to the hook or claim an A/B win.

Inspect logging/coverage and assignment balance before results. Treat dropouts,
repeat users, missing exports and simultaneous title/music changes explicitly.
Report effect magnitude/intervals when estimable, practical relevance and design
limits; no invented p-values. Predefine duration/sample and account for peeking
and multiple comparisons (S26). Monitor harm/rights/data failures without using
early noisy gains as a winner rule. Inconclusive is valid; decide whether further
learning is worth its cost instead of asserting equality.
