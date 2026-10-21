# Briefs

Panel briefs follow review-panel's rules and end with its return contract. Implementer and test-writer briefs end with the constraint block from `SKILL.md`, verbatim. The material is delimited from the instructions in every brief.

## Design review (review-panel `converge`)

In this order: the operator's original request in their words or a faithful paraphrase; the settled constraints, each marked by whom; the designer's assumptions, marked as such; the specification as the delimited material; a neutral question asking for disconfirming cases against the acceptance criteria, the constraints and the request, where a helper following the text literally would fail, what the specification requires beyond the request, and what is ambiguous, with a request to flag any sensitive area; and the converge return contract, last. The brief does not say which round it is.

## Implementer

The specification (or its path inside the copy), the files in scope, the test directory named as read-only, the copy's path, the test command, what is stubbed, what "done" means, and what to report: every file added, changed or deleted, one line each; the exact commands run and their results; anything in the specification it could not satisfy and why. Facts only. No commit. In a fix round it also gets the candidate, the findings as adopted or adapted, and the frozen tests, read-only; it satisfies the specification, not the tests, and reports a test the specification does not support instead of satisfying it.

## Test-writer

First delivery: the specification and the baseline only. It writes adversarial tests against the acceptance criteria and interfaces into the named directory, attacking boundaries, failure paths, injection, path handling and permissions, and states for each test whether it reproduces a failure the specification fixes, preserves an invariant, or exercises new behaviour. It runs them on the baseline and reports the outcomes as they are. No implementation is given and none is guessed at.

Second delivery, the same session continued: the candidate and the implementer's report. It applies the candidate to a clean copy with the frozen tests in place, runs its tests and then the full suite, checks that the same named tests ran, reviews the candidate for security (secrets, injection, paths, permissions, data boundary) and quality (correctness, clarity, dead code, unhandled errors) against the specification, and reports: the tests with class and outcomes on baseline and candidate; the suite result verbatim; findings with file and line; specification deviations; a verdict of merge, fix then merge with the required fixes listed, or reject with the reason. It does not fix.

## Change review (review-panel `opinion`)

The candidate diff, the frozen tests, the implementer's and test-writer's reports, the specification, and in strict mode the hunks that make the run strict, with a question asking what the tests miss, what the candidate does beyond the specification, and what would fail in use.

## Starting a write-capable helper

Review members use the read-only forms in review-panel's `runtimes.md`. The implementer and the test-writer need to edit files and run the test command, from the copy, with its project instructions loaded:

- Claude CLI: `claude -p --model <model> --setting-sources "project,local" --strict-mcp-config --tools "Read,Edit,Write,Grep,Glob,Bash" --permission-mode acceptEdits --allowedTools "Bash(<test command>:*)" --output-format json < <brief-file>`; the test-writer's second delivery adds `--resume <session_id>`.
- Codex: `codex exec --skip-git-repo-check --sandbox workspace-write -c model_reasoning_effort=<effort> [-m <model>] < <brief-file>`, without `--ephemeral` for the test-writer, whose second delivery is `codex exec resume <session id>`.
- cursor-agent and a host subagent expose no session to continue, so they can implement but cannot be the test-writer.

The model and session id come from the runtime's output as `runtimes.md` describes.
