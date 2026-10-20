# Light rewrite of four-eyes (0.6.0) and review-panel (0.4.0): panel round (2026-10-20)

Operator's instruction (2026-10-20): rework the skills to be lighter, about 40% of their size, descriptive rather than imperative, keeping the use of multiple models for more effective work and dropping isolation and sandboxing; run the rewrite by the panel. The heavy work of run fe-run2 stays on branches `fe-run2-per-session-resolution` and `review-panel-0.3.0`.

Roster: review-panel (light rules): codex, runtime codex, model gpt-6-astra (header `model: gpt-6-astra`, `provider: openai`), session 01a157e2-d5d1-70c3-9a4c-7710b707d3bc, briefed, user instructions loaded (~/.codex/AGENTS.md), returned, 73 s, tokens used 56,324; opus, runtime claude, model claude-opus-5-5 (modelUsage), session b424a6a9-2b7b-4ece-921d-af0cc6f7a917, briefed, returned, 264 s, USD 0.82. Both fresh sessions under the operator's normal CLI configuration, read-only tools. Shared with the driver (claude-fable-5-1): opus shares the vendor; codex shares neither. Mode converge, one round; the revision below is not re-reviewed.

Brief: /private/tmp/fe-light/brief.md (removed after the run); material: the eight new files; the 0.5.0 and 0.3.0 versions staged for comparison only.

## Ledger (driver's dispositions)

- Constraint block versus "contract last" (codex 1, opus 1): adopted. The block ends implementer and test-writer briefs only; panel briefs end with review-panel's contract.
- No write-capable launch forms; cursor-agent and subagent cannot be the test-writer (codex 2, opus 3): adopted; a "Starting a write-capable helper" section in briefs.md.
- Frozen tests have no path into the clean copy or the commit (codex 3): adopted; the second delivery rebuilds the copy with the frozen tests; the commit carries implementation, tests and the specification.
- Acceptance can bypass required fixes or a reject (codex 4): adopted as an acceptance condition.
- Fresh-session definition in the wrong skill and conflicting with `checkout`; `user instructions` marker (codex 5, opus 7, opus 8): adopted; defined once in review-panel; the level keeps what the member could read and carries `user instructions loaded | unconfirmed`.
- Required `web` without a supported member (codex 6): adopted; a member that cannot support the tools its task needs is unavailable for that task.
- Consent: "asks once" versus the commit and push (codex 7, opus 2): adopted; Go authorises dispatch; Accept shows the final diff and that answer is the commit word; push and release separately; `commit word` in the report.
- Test-writer replacement undefined (codex 8, opus 9): adopted; a replacement starts blind and makes the first delivery before seeing the candidate.
- Caller-selected members (codex 9): adopted as an Inputs sentence.
- Disclosure: compare design review with the designer and change review with the implementer; the test-writer's relation; a `not covered` line; the two-model allocation explained and the second model added to the change review; the single-model case (codex 10, opus 4): adopted.
- Unused hash, duplicate timestamps, secret scan in both skills, subagent enforcement wording (codex 11, opus 9): adopted; the frozen copy and the two timestamps stay; the scan lives in review-panel with "a hit stops the dispatch and goes to the operator"; subagent "read-only by its tool list".
- README paths and snippet asymmetry (codex 12, opus 16): the staged copies were renamed for the brief; the repository paths are as the README says; both snippets now carry the not-installed sentence.
- Invalid frozen test (opus 5): adopted; the designer may judge one invalid with the reason shown; only the test-writer amends it.
- Export rule and applying the diff to the operator's tree (opus 6): adopted.
- Round marker in the brief (opus 10): adopted; "never marked as a revision or a round".
- Light mode wording and the declined second fix (opus 11): adopted; declined gives `rejected`.
- Roster shown and proceed (opus 12): adopted.
- Order rule and where strength comes from (opus 13): adopted; the file's order and names, shown at Go.
- Restatement (opus 14): adopted in part; strict triggers now appear in the description (the skill's trigger) and once in Modes; the test-writer detail lives in briefs.md; flags only in runtimes.md; model and vendor buys only in review-panel.
- review-panel trims (opus 15, codex 11): applied in part; the fresh-session definition moved in from four-eyes, so SKILL.md stands at 50% of 0.3.0 (8.7 KB), with the two return contracts (0.75 KB) verbatim. A further trim is the operator's call.

Sizes after the revision: four-eyes SKILL.md 10.5 KB (29% of 0.5.0), briefs.md 3.7 KB, README 3.0 KB; review-panel SKILL.md 8.7 KB (50%), runtimes.md 3.1 KB (50%), panel.example.toml 0.8 KB.
