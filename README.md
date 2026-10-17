# four-eyes

An agent skill that orders non-trivial development work into four roles, each filled by the strongest model available to it at the time, never by a named required model:

1. **Designer**: the strongest model on the host writes a specification with pre-registered acceptance criteria and precise interfaces.
2. **Verifier**: other models review the specification adversarially before anything is built, through [review-panel](https://github.com/ivan-avramov/review-panel), with at least one member from a different vendor than the designer. The operator approves the verified specification before dispatch.
3. **Worker**: a capable model in a fresh, isolated copy implements from the approved specification only, and commits nothing; its result is a complete candidate diff.
4. **Reviewer**: a capable model distinct from the worker writes adversarial tests from the specification alone, then receives the candidate, runs everything in isolation and reviews for security and quality; the panel then reviews the candidate read-only.

The skill records the runtime, vendor and observed model that filled each role, with its evidence, and stops to ask the operator, with a recommendation, when a role cannot be filled as intended: a missing CLI, an authentication failure, a usage limit, a session model below the host's strongest, or the cross-vendor verifier returning nothing. That keeps it usable across vendors and across model releases.

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
