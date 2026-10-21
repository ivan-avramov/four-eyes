# Churn patch: four-eyes 0.6.1 and review-panel 0.4.1, panel round (2026-10-20)

Operator's instruction (2026-10-20): two projects (Limitaur, Premisa) ran strict four-eyes under 0.5.0 and 0.6.0 and did not converge; two GPT-Sol sessions wrote a proposal of skill changes (`/tmp/four-eyes-review-panel-churn-proposal.md`, preserved under `~/ws/premisa/docs/reviews/workflow-churn-p531/`). The operator asked for an analysis of whether the skills themselves were at fault and what, if anything, to adopt; then: proceed, check additions for literal and semantic duplicates against the existing text, agent-facing register.

Skill-side causes identified (the rest is driver judgement and project governance inherited from 0.4/0.5): the converge stop rule continuing whenever a major was adopted while "major" was unanchored; findings adopted as a unit, problem and mechanism together; the design-review question asking for gaps and never for excess; "strict" read as a mandate to maximize assurance; Go silent on retries; Accept imposing a commit gate against the operator's standing rule; no path for specification changes after Go; fix-round implementers seeing frozen tests with no rule against coding to them; a sentinel rule too literal; change reviewers informed by the test-writer's report without disclosure. Declined from the proposal: classification and origin fields in the contract, a scenario validation harness, feasibility probes, same-session completion rules, cross-run finding lineage.

Roster: review-panel 0.4.1 draft (the revised contract ran on its own review): codex, runtime codex, gpt-6-astra, effort high, session 01a15ca1-2e74-71d0-bc81-c58efbd98f3b, briefed, user instructions loaded (~/.codex/AGENTS.md), returned, exit 0, tokens used 24,548; opus, runtime claude, claude-opus-5-5 (modelUsage), session 9d4e77fc-4283-48ee-88e7-5e205b7acfa0, briefed, returned, exit 0, 116 s, USD 0.34. Dispatched 04:03:49Z, collected 04:05:46Z. Shared with the driver (claude-fable-5-1): opus the vendor; codex neither. Mode converge, one round; the revision below is not re-reviewed.

Brief: `/private/tmp/fe-061-panel/brief.md` (789 words; raw outputs under `out/` there, not durable). Material: the four changed files, their 0.6.0 and 0.4.0 versions for comparison, and the two diffs.

## Ledger (driver's dispositions, grouped by underlying issue)

- "A finding whose severity rests on a guarantee the material does not claim ... never applied" suppresses real defects and hazards (codex P1, opus 2, opus 3): adopted. The clause is gone; "major" and the scope request are anchored to "the request it serves" instead of the material's stated purpose; the contract says a hazard the material introduces is a defect.
- The scope-request label's owner is unstated (opus 4): adopted; severity and the label are the driver's.
- A member reporting the specification's excess over the request would be labelled a scope request and protected from removal (opus 1): adopted; the contract says "a requirement you would add".
- The implementer-side test rule is not in the brief and leaves a failing test at Accept (codex P2, opus 5): adopted; the rule moved to the Implementer section of `briefs.md` for fix rounds, and Fix routes an unsupported test to the invalid-test path of step 5.
- Post-Go specification changes: "adds" too narrow, "shown" not an ask, "asks named here" and "round beyond the mode" ambiguous or duplicate (codex P3, opus 6): adopted; a change after Go is an ask, architecture as Modes defines it gets one design-review round before the ask, the round clause dropped.
- The strict qualifier binds the designer while members get "mode: strict" first in the brief (opus 7): adopted; the mode is no longer in the design-review brief.
- "Smallest" unanchored and the two-part sentence restating "adapted" (opus 8): adapted; the sentence now defines adapting as keeping the problem and replacing the change with the smallest one that resolves it.
- Sentinel still literal (opus 9): adopted; case, punctuation and formatting around it ignored.
- Accept "under standing instructions" ambiguous with none or with a stricter rule (opus 10): adopted; "as the operator's standing instructions allow, or asks when there are none".
- Success and failure path addition traces to no named cause (opus 11): declined removal; it addresses interface closure, which the brief's assumption list omitted; "one" replaced by "a" to remove the per-interface reading.
- Recorded-for-operator items have no showing point in four-eyes (opus 12): adopted; Go shows them.

Net size after the revision: review-panel SKILL.md +92 words over 0.4.0; four-eyes SKILL.md, briefs.md and README +177 words over 0.6.0.
