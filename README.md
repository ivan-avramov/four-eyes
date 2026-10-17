# four-eyes

An agent skill that orders non-trivial development work into four roles, each filled by the model available to it at the time, never by a named required model:

1. **Designer**: the strongest model available on the host writes a specification with pre-registered acceptance criteria and precise interfaces; if the session's model is not the strongest, the operator is asked first.
2. **Verifier**: other models review the specification adversarially before anything is built, through [review-panel](https://github.com/ivan-avramov/review-panel), with at least one member from a different vendor than the designer at that vendor's strongest tier. The operator approves the verified specification before dispatch.
3. **Worker**: a capable model, not necessarily the strongest, in a fresh isolated copy implements from the approved specification only, commits nothing, and returns a complete candidate against a recorded baseline.
4. **Reviewer**: a capable model distinct from the worker writes adversarial tests from the specification alone, then receives the candidate, runs everything in isolation and reviews for security and quality; the panel then reviews the frozen candidate read-only.

The skill records the runtime, vendor and observed model that filled each role, with its evidence, and discloses where evidence is unavailable: a host subagent reports no model id, so a worker run that way is marked unverified, and roles whose identity matters (the verifier, the reviewer, any pair that must differ) are gated rather than assumed. It stops to ask the operator, with a recommendation, when a role cannot be filled as intended: a missing CLI, an authentication failure, a usage limit, a session model below the host's strongest, a cross-vendor member returning nothing, or isolation that cannot be enforced.

## Why, and its limits

The method rests on an assumption: a model anchored on its own design or its own code misses defects that a fresh context, and a model trained elsewhere, is more likely to catch. Fresh contexts and vendor diversity reduce anchoring and correlated blind spots; they do not remove them. Models from different vendors share training data and habits, so panel findings are evidence for the driver to weigh, never a guarantee. The operator sees the findings, the dispositions and the evidence of what ran, and can overrule any of it.

## Install

Requires review-panel. Copy `four-eyes/` into a skills directory:

- user-wide: `~/.claude/skills/` (Claude Code), `~/.agents/skills/` (Codex and other clients that load skills from there)
- per repository: `<repo>/.claude/skills/`, `<repo>/.agents/skills/`

For Codex, also append `codex/AGENTS.snippet.md` to `~/.codex/AGENTS.md` so qualifying work triggers the skill. Configure the panel per review-panel's instructions (`~/.config/review-panel/panel.toml`).

## Files

- `four-eyes/SKILL.md`: the skill, terse and directive.
- `four-eyes/briefs/`: what the verifier's review-panel brief must carry; worker and reviewer templates.
- `codex/AGENTS.snippet.md`: the global instruction that points Codex at the skill.
