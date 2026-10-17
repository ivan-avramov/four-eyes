# four-eyes

An agent skill that orders non-trivial development work into four roles, each filled by the model available to it at the time, never by a named required model:

1. **Designer**: the strongest model available on the host writes a specification with pre-registered acceptance criteria and precise interfaces; if the session's model is not the strongest, the operator is asked first.
2. **Verifier**: other models review the specification adversarially before anything is built, through [review-panel](https://github.com/ivan-avramov/review-panel), with at least one member from a different vendor than the designer at that vendor's strongest tier. The operator approves the verified specification before dispatch.
3. **Worker**: a capable model, not necessarily the strongest, in a fresh isolated copy implements from the approved specification only, commits nothing, and returns a complete candidate against a recorded baseline.
4. **Reviewer**: a capable model distinct from the worker writes adversarial tests from the specification alone, then receives the candidate, runs everything in isolation and reviews for security and quality; the panel then reviews the frozen candidate read-only.

The skill records the runtime, vendor and observed model that filled each role, with its evidence, and discloses where evidence is unavailable: a host subagent reports no model id, so a worker run that way is marked unverified, and roles whose identity matters (the verifier, the reviewer, any pair that must differ) are gated rather than assumed. It stops to ask the operator, with a recommendation, when a role cannot be filled as intended: a missing CLI, an authentication failure, a usage limit, a session model below the host's strongest, a cross-vendor member returning nothing, or isolation that cannot be enforced.

## Why, and its limits

The method rests on an assumption: a model anchored on its own design or its own code misses defects that a fresh context, and a model trained elsewhere, is more likely to catch. Fresh contexts and vendor diversity reduce anchoring and correlated blind spots; they do not remove them. Models from different vendors share training data and habits, so panel findings are evidence for the driver to weigh, never a guarantee. The operator sees the findings, the dispositions and the evidence of what ran, and can overrule any of it.

## What differs, and what may coincide

The cross-vendor requirement applies to the verifier against the designer and to the final panel against the worker and reviewer. The reviewer must differ from the worker by model; the designer and the worker may be the same model. Two operator gates are built in: approval of the verified specification before anything is built, and a second remediation round. Commits happen only when every finding is dispositioned and the committed tree matches the reviewed candidate; pushes only on the operator's explicit word. Evidence of identity has limits the skill discloses rather than hides: a host subagent reports no model id, Codex echoes the requested selector, and the Claude CLI may list several models per run.

## Install

Requires review-panel. Copy `four-eyes/` into a skills directory:

- user-wide: `~/.claude/skills/` (Claude Code) and `~/.agents/skills/` (Codex and other clients that load skills from there)
- per repository: `<repo>/.claude/skills/`, `<repo>/.agents/skills/`

Add the standing trigger so qualifying work invokes the skill rather than relying on automatic selection: append `claude/CLAUDE.snippet.md` to `~/.claude/CLAUDE.md` and `codex/AGENTS.snippet.md` to `~/.codex/AGENTS.md`. Optionally maintain `~/.config/review-panel/tiers.toml` (vendor → ordered model selectors, dated) so "strongest available" rests on your list rather than a model's memory. Configure the panel per review-panel's instructions. Run `sandbox/probes.md` once per machine before trusting the write guard.

## Files

- `four-eyes/SKILL.md`: the skill, terse and directive.
- `four-eyes/briefs/`: what the verifier's review-panel brief must carry; worker and reviewer templates.
- `sandbox/`: the macOS write-guard profile and the probes that qualify it.
- `codex/AGENTS.snippet.md`, `claude/CLAUDE.snippet.md`: standing triggers for Codex and Claude Code.
