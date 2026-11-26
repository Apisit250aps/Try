# Validation and evidence

Before exploration specify model, initial state, domains/bounds, transitions,
priority/fallback, invariants, termination criteria, stochastic treatment and
version. Check duplicate/missing IDs, missing targets, malformed guards/effects,
type/range violations and unowned facts. For each reachable (node,state), enumerate
eligible transitions, apply the defined ordering and invariants, and record the
predecessor trace. Check all ending guards for overlap and uncovered *reachable*
states; report unreachable endings/nodes with a witness or explain bounds. Detect
unintended dead ends and invalid transitions. Examine joins for impossible or
contradictory knowledge/inventory/relationship states. A topologically reachable
node can still be unreachable with guards.

Cycle detection alone does not prove nontermination. Identify intentional loops,
progress measure, exit and fairness assumptions. A reachable closed cycle with no
exit is nonterminating; a cycle with an exit still permits infinite execution if
nothing forces exit. For stochastic systems, distinguish possible infinite traces,
almost-sure termination and proof of a fixed limit; do not infer any from samples.
Report intended infinite experiences separately. Track depth and state bounds; if
truncated, list unexplored frontier and label reachability/coverage partial. Abstract
states or sample paths for scale, document what abstraction loses. Path, branch,
node, transition, guard truth/false and ending coverage are distinct metrics;
100% of one is not total narrative correctness. Record tools, model version,
commands, inputs, expected and observed results and failures/retests.

A graph check cannot establish thematic quality, character believability, UI
legibility or perceived agency. Separately run fresh-context model tasks with
blind rubric where feasible, real receiver/production trials and human audience or
player studies when authorized and available. Give creative interpretations as
hypotheses, track sampling bias and do not invent playtest results.
