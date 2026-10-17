# Reviewer briefs (templates): one fresh session, two deliveries

Start the session without the driver's transcript. Paste the constraint block from SKILL.md verbatim into both deliveries.

## Phase A (receives the specification and the baseline only)

Write adversarial tests against the specification's acceptance criteria and interfaces into `<test directory>`. Attack boundaries, failure paths, injection, path handling, permissions and the data boundary the specification names. No implementation is given; do not guess at one. For each test state its class: reproduces a failure the specification fixes, preserves an invariant that must hold before and after, or exercises new behaviour. Run them on the baseline and report the outcomes truthfully; no outcome is "expected".

## Phase B (same session; receives the candidate and the worker's report)

Apply the candidate in your isolated copy. Run the phase A tests, then the full suite, under the isolation the brief states. Then review the candidate for security (secrets, injection, paths, permissions, data boundary) and quality (correctness, clarity, dead code, unhandled errors) against the specification. Do not fix; report.

## Report
1. Phase A tests: names, class, what each attacks, baseline outcome, candidate outcome.
2. Full suite result, verbatim summary.
3. Security findings, severity-ordered, with file:line.
4. Quality findings, with file:line.
5. Specification deviations.
6. Verdict: merge, fix-then-merge (list every required fix), or reject (why).
