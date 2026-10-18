# four-eyes 0.5.0

An agent skill that orders non-trivial development work into separated roles, each filled by the models available at the time. The skill captures a principle: independent review across separated roles in fresh contexts. It never requires a vendor or a model. It runs on whatever you have, down to one subscription offering two models that pull double duty, and tells you plainly, before anything is built, what that configuration does not check.

1. **Designer**: a top-tier model, the session's, writes a specification with pre-registered acceptance criteria and precise interfaces; if the session's model is not top-tier, the operator is asked first.
2. **Verifier**: independent models, with at least one top-tier member, review the specification adversarially before anything is built, through [review-panel](https://github.com/ivan-avramov/review-panel) 0.3.0 or later. The operator approves the verified specification, the planned assignment and every degradation in one gate message before anything write-capable is dispatched.
3. **Worker**: a capable (cheaper) model in a fresh isolated copy implements from the approved specification only, commits nothing, and returns a complete candidate against a recorded baseline.
4. **Reviewer**: a capable model writes adversarial tests from the specification alone, then receives the candidate, runs everything in isolation and reviews for security and quality; the panel, also drawn from capable models, then reviews the frozen candidate read-only.

Expensive models go to design and verification; cheaper capable ones go to implementation and routine review.

## Modes

- **Light** (default): the specification is verified in one round; the candidate panel is one invocation; one remediation.
- **Strict**: for security, authentication, permissions, secrets, a data boundary or architecture: the specification converges over up to three rounds. A trigger found at design, at the gate or after build escalates a light run to strict and asks you again.

## Independence levels

Independence is a property of a pair of roles, evidenced per member. Fresh context is a prerequisite of every level; vendor and model distinctness add to it. Each pair has a preferred and a minimum level; a pair that cannot reach L1 stops the run. A level describes which correlated risks a configuration reduces, never that an error was caught.

## What a degraded run does not check

Each run prints, per distinct level present, which member pairs sit at that level and what that level does not reduce, using these fixed wordings:

| Level | Meaning | Reduces correlated risk from | Does not reduce (fixed disclosure wording) |
|---|---|---|---|
| L3 | fresh context, different vendor (maker of the model) | transcript anchoring, model-specific errors, vendor-wide habits | blind spots shared across the industry's training data and conventions |
| L2 | fresh context, same vendor, different model | transcript anchoring, model-specific errors | vendor-wide training habits, shared tuning, shared data blind spots |
| L1 | fresh context, same model | transcript anchoring | anything the model gets wrong consistently, including its own code and reasoning habits |
| none | fresh context not established | nothing established | may share the driver's context; independence not established |
| L0 | shared context | nothing | forbidden for any required pair |

A run-level line follows:

`verified distinct models across all roles: m (identity unresolved: k); verified distinct vendors: v`

When k is zero and m is two: `Every check in this run was made by two models; an error both make consistently is not reduced, and on L1 pairs an error that model makes consistently is not reduced.` When k is zero and m is one: `Every check in this run was made by one model; any error it makes consistently is not reduced.` When k is not zero, no total is asserted; the line stands alone.

On one vendor with two models, at least one required pair is always at L1; the method still runs, and these lines say what it cannot catch.

## Cost and its units

Every run ends with a ledger, a timestamped event sequence and a totals block. Nothing is estimated; every figure is what the runtime itself returned, or `unreported`.

- An **execution** is one runtime invocation: one panel member in one round, the worker, each of the reviewer's two deliveries, each re-run of phase B (resuming the same reviewer session), each remediation dispatch. The ledger counts executions.
- A **panel invocation** is one round of one panel; a **verification cycle** is one converge call of one to three rounds. The run criteria count invocations and cycles (R3 counts per cycle).
- Each execution records its tokens (uncached input, cache read, cache creation, output, or one unsplit `total-only` figure), its money with currency, its wall seconds, and its model, vendor, tier and session. The driver's own session is always a record too: the run-scoped delta where the host exposes one, else `unreported`.
- Tokens are bucketed by runtime and vendor and never summed across buckets. Money is bucketed by runtime and the billing basis you declare (`api` or `subscription`, dated) and never summed across runtimes, currencies or bases; an undeclared basis is labelled `basis unknown`.
- Every subtotal states its coverage, `over n of e` executions. Elapsed time is reported apart from summed execution seconds.
- A resumed session's usage and a host subagent's usage are `unreported`.

## What 0.4.0 guaranteed, and where the report shows it

| Guarantee (S6) | Report field |
|---|---|
| Isolation of write-capable roles in a fresh copy | the isolation probes |
| Disclosure scanning before anything leaves the host | the disclosure scan per dispatch |
| Evidence of what ran per role | the roles block, and the ledger's execution records (observed model, session id, freshness evidence) |
| The approval gate before dispatch | the gate field of the roles block, the questions section, and the event sequence showing no write-capable dispatch before the answer |
| The reviewer's tests frozen before the candidate is revealed | the frozen test hash and freeze time, earlier than the candidate reveal time |
| Commit of the candidate's files only | the baseline, the authorised candidate delta and the commit delta, equal; the committed tree hash equal to the final candidate hash bound to the last panel verdict |
| Push only on the operator's explicit word | `push: none`, or the operator's words |

## Why, and its limits

The method rests on an assumption: a model anchored on its own design or its own code misses defects that a fresh context, and a model trained elsewhere, is more likely to catch. Fresh contexts and model diversity reduce anchoring and correlated blind spots; they do not remove them. Models from different vendors share training data and habits, so panel findings are evidence for the driver to weigh, never a guarantee. The operator sees the findings, the dispositions and the evidence of what ran, and can overrule any of it.

## Gates

One question per run is folded into the approval gate: nothing write-capable is dispatched until your recorded answer accepts the run's levels and tier substitutions. No acceptance persists between runs. Beyond the gate, questions arise **only** from escalation, lost coverage or an evidence mismatch, or from the procedure's named decisions (an unresolved converge, a held change revised, a changed operator tree at acceptance, an unresolved blocker after remediation, a second remediation round, an out-of-scope build hit, a found or non-excludable secret with the cause `found secret`, a context no available runtime can provide with the cause `unsupported context`), each recorded with its cause; declining it stops the run with no commit. A `found secret` decision is put to you, folded into the gate message when it arises before the gate. Sanitising touches only disposable material outside the hashed candidate tree (briefs, scratch), redactions recorded; a secret in any tracked file of that tree, found before the baseline, waits for you to remove it; a secret found at or after step 4, in the baseline or the candidate, stops the run with a report, or on your answer rebuilds from step 4 with every derived artifact invalidated; a secret in the candidate is also a candidate finding and is never dispatched for remediation. You may answer `not a secret` with the pattern, path and reason, recorded in the report; the run continues on that answer. A pre-baseline removal is committed in your repository before step 4 records the state; the specification is committed before step 4 as well; other authorised untracked files are listed and excluded from the step 10 delta and tree comparisons. Secret-bearing material is never dispatched. Commits happen only when every finding is dispositioned and the committed tree matches the reviewed candidate; pushes only on your explicit word. Evidence of identity has limits the skill discloses rather than hides: a host subagent reports no model id or session id, such a role has no level and is admitted only by your answer at the gate, and some CLIs echo the requested selector or list several models per run.

## Install

Requires review-panel 0.3.0 or later. Copy `four-eyes/` into a skills directory:

- user-wide: `~/.claude/skills/` (Claude Code) and `~/.agents/skills/` (Codex and other clients that load skills from there)
- per repository: `<repo>/.claude/skills/`, `<repo>/.agents/skills/`

Add the standing trigger so qualifying work invokes the skill rather than relying on automatic selection: append `claude/CLAUDE.snippet.md` to `~/.claude/CLAUDE.md` and `codex/AGENTS.snippet.md` to `~/.codex/AGENTS.md`. Declare each panel member's `vendor` and `tier` (`top` or `capable`), and each runtime's `billing`, with dates, in `~/.config/review-panel/panel.toml` so tiers, levels and cost buckets rest on your declarations rather than a model's memory. review-panel's own `panel.example.toml` (0.3.0 or later) ships these fields as commented examples; copy it by hand. Migration: 0.4.0's operator file `tiers.toml` is replaced by the per-member `tier` in the panel file; four-eyes reads no `tiers.toml`, and a 0.2.0 panel file stays valid, with warnings for the absent fields. Consequence for cursor-agent: a 0.2.0 roster with cursor-agent members (no session id, so level `none`) is asked before dispatch every run, or stops non-interactively. Run `sandbox/probes.md` once per machine before trusting the write guard.

## Files

- `four-eyes/SKILL.md`: the skill, terse and directive.
- `four-eyes/briefs/`: what the verifier's review-panel brief must carry; worker and reviewer templates.
- `review-panel-0.2.0/`: review-panel 0.3.0 as a patch for its own repository (the directory name is unchanged).
- `sandbox/`: the macOS profiles (`macos-write-guard.sb` for the CLI, `macos-test-guard.sb` for the tests) and the probes that qualify it.
- `codex/AGENTS.snippet.md`, `claude/CLAUDE.snippet.md`: standing triggers for Codex and Claude Code.
