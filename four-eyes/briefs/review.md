# Reviewer briefs (templates): two phases, two deliveries

Paste the constraint block from SKILL.md verbatim into both.

## Phase A (fresh context; receives the specification and the baseline tree only)

Write adversarial tests against the specification's acceptance criteria and interfaces into `<test directory>`. Attack boundaries, failure paths, injection, path handling, permissions and the data boundary the specification names. No implementation is given; do not guess at one. Report the test names and what each attacks. They are expected to fail on the baseline tree.

## Phase B (same reviewer; receives the candidate and the worker's report)

Apply the candidate in your isolated copy. Run the phase A tests, then the full suite, with the scrubbed credentials and network settings the brief states. Then review the candidate for security (secrets, injection, paths, permissions, data boundary) and quality (correctness, clarity, dead code, unhandled errors) against the specification. Do not fix; report.

## Report
1. Phase A tests: names, what each attacks, result on the candidate.
2. Full suite result, verbatim summary.
3. Security findings, severity-ordered, with file:line.
4. Quality findings, with file:line.
5. Specification deviations.
6. Verdict: merge, fix-then-merge (list), or reject (why).
