# Closure patch: four-eyes 0.6.2 (2026-10-21)

Operator's observation, from a strict run on the juno-ai repository the same day and from three or four earlier sessions on other projects with the same symptom: the design review ratholes through review rounds that bloat the solution, up to five times the work the request intended in some cases, and drift from the original goal. The 0.6.1 churn patch had anchored severity to the request and let members report excess; the symptom recurred. The operator's inline correction that ended it: step back to the framing of the problem, consider cutting, dropping, rolling back or rewriting work for quality, converge on a solution that reasonably rather than perfectly biases to maximize quality. The operator rejected a first proposal that gated extra rounds on the operator's word and carried examples from the day's work: the skill must drive to closure by itself and stay general.

Causes in the 0.6.1 text: no statement of the goal that every round and member is held to, so each round starts from the previous round's findings; findings adopted with their mechanisms, and each mechanism seeding the next round's hazards; convergence measured by the absence of new majors, which members briefed to disconfirm always supply on new text; no sanction to cut or roll back.

Changes, applied without a panel round (the operator's wording, settled in conversation):

- SKILL.md step 1: the goal is one paragraph stating the problem as posed and what solving it means, carried verbatim into every later brief and the measure of every finding.
- SKILL.md step 2: each round begins from the goal paragraph; the designer cuts, rewrites or rolls back before adopting; the bias is quality of outcome, reasonable rather than perfect, a rewrite or rollback preferred to a patch when it yields the better solution, an addition not made unless it raises the outcome against the goal; a finding is adopted for its problem, never its mechanism; a finding whose failure needs conditions the goal does not cover is a residual; a hazard in a mechanism an earlier round added weighs first against that mechanism; the review converges when the acceptance criteria are unchanged across a round, every open finding is a residual or a recorded decline, and no change the designer can name would raise the outcome; the round count is a ceiling and this rule, not review-panel's, decides a further round.
- briefs.md, design review: the goal paragraph verbatim after the request; the question asks what could be dropped or simplified while still meeting the goal.
- README step 2 restated. Modes unchanged.

Sample case for an evaluation: the juno-ai run of 2026-10-21 (specification `docs/design/uv-log-userinfo-and-host-widening.md`, three strict rounds, 79 findings, the specification from about 2,300 to 4,800 words before the operator's cut back to 4,500), mirrored with every brief, review and ledger under the evidence repository's `sessions/2026-10-21-session-E/`.

## 0.6.3, the same day

The 0.6.2 rule sat in step 2 alone; at the change review of the same run the designer adopted five cosmetic minors beside the one defect, the same reflex at a step the rule did not name, caught by a side agent. 0.6.3 states the rule at the change review (step 6) and lets only findings adopted under it reach the fix (step 7). Evidence that an instruction stated once does not generalize across steps in practice; the evaluation harness should measure each judging point.

## 0.6.4, the same run

After the first fix round, each strict change review found the next instance of one class (shell string operations quadratic on a crafted line of hundreds of kilobytes), the designer adopted each as real and cheap, and step 7 left it only two exits, the operator's word for another round or rejection, so the operator was asked for a round three times. The operator: "you keep asking me to run extra rounds. It starts to look again like a problem with the skill." 0.6.4 lets the designer record a finding of a bounded or residual class, or one needing an input outside the goal's operating conditions, and proceed to Accept; a further round is asked for only when the goal fails on an input it covers.
