# Reviewer briefs (templates): one fresh session, two deliveries

Start the session without the driver's transcript. Paste the constraint block from SKILL.md verbatim into both deliveries.

## Commands for a CLI reviewer

Both deliveries start without any ephemeral flag, so the session can be resumed. Run both under the guard in the isolated copy, with the runtime's flags recorded for freshness (memory disabled, no resume flag in phase A). Record the session id each delivery reports; the unverified templates below are checked by probe 6 in `sandbox/probes.md`.

- claude, phase A: `CLAUDE_CONFIG_DIR=<runtime-state> claude -p --model <model> --setting-sources "project,local" --strict-mcp-config --output-format json --tools "<tools>" < <phase-A-brief>`; phase B: `CLAUDE_CONFIG_DIR=<runtime-state> claude -p --resume <phase-A-session-id> --model <model> --setting-sources "project,local" --strict-mcp-config --output-format json --tools "<tools>" < <phase-B-brief>`. With `CLAUDE_CONFIG_DIR` set to the run-scoped `<runtime-state>`, the CLI's memory is empty and run-scoped.
- codex, phase A: `CODEX_HOME=<runtime-state> codex exec --sandbox workspace-write --skip-git-repo-check -c model_reasoning_effort=<effort> [-m <model>] < <phase-A-brief>` (the isolated copy is its workspace; no ephemeral flag); phase B: `CODEX_HOME=<runtime-state> codex exec resume <phase-A-session-id> --skip-git-repo-check -c model_reasoning_effort=<effort> < <phase-B-brief>`, with the same environment as phase A.

## Phase A (receives the specification and the baseline only)

Write adversarial tests against the specification's acceptance criteria and interfaces into `<test directory>`. Attack boundaries, failure paths, injection, path handling, permissions and the data boundary the specification names. No implementation is given; do not guess at one. For each test state its class: reproduces a failure the specification fixes, preserves an invariant that must hold before and after, or exercises new behaviour. Run them on the baseline and report the outcomes truthfully; no outcome is "expected".

## Phase B (same session; receives the candidate and the worker's report)

A replaced reviewer session never receives phase B alone: it starts at a new candidate-blind phase A with newly frozen tests, recorded `replaced (lost session | escalation)`. A lost session is replaced at most once per run; a second loss goes to the operator. Where a runtime documents id rotation on resume, the recorded chain of ids stands in for equality.

Apply the candidate in your isolated copy. Run the phase A tests, then the full suite, under the isolation the brief states. Then review the candidate for security (secrets, injection, paths, permissions, data boundary) and quality (correctness, clarity, dead code, unhandled errors) against the specification. Do not fix; report.

## Report
1. Phase A tests: names, class, what each attacks, baseline outcome, candidate outcome.
2. Full suite result, verbatim summary.
3. Security findings, severity-ordered, with file:line.
4. Quality findings, with file:line.
5. Specification deviations.
6. Verdict: merge, fix-then-merge (list every required fix), or reject (why).
