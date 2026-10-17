# four-eyes

An agent skill that orders non-trivial development work into four roles, each filled by the strongest model available to it at the time, never by a named required model:

1. **Designer**: the session's own model writes a specification with pre-registered acceptance criteria.
2. **Verifier**: other models review the specification adversarially before anything is built, through [review-panel](https://github.com/ivan-avramov/review-panel), with at least one member from a different provider than the designer.
3. **Worker**: a capable model in a fresh context implements from the approved specification only, and commits nothing.
4. **Reviewer**: a capable model distinct from the worker writes adversarial tests first, runs the suite, reviews for security and quality; the panel then reviews the diff read-only.

The skill reports the provider and model that actually filled each role, and stops to ask the operator, with a recommendation, when a role cannot be filled as intended: a missing CLI, an authentication failure, a usage limit, or the only available model being one already used in another role. That keeps it usable across providers (Anthropic, OpenAI, Cursor and whatever comes next) and across model releases.

## Why

Strong models design well and review their own work badly. Separating the roles, and putting a different provider on the review side, catches the errors a single context cannot see. Naming roles rather than models keeps the method alive when a model is rate-limited, retired or superseded.

## Install

Requires review-panel. Copy `four-eyes/` into a skills directory:

- user-wide: `~/.claude/skills/` (Claude Code), `~/.agents/skills/` (other clients)
- per repository: `<repo>/.claude/skills/`, `<repo>/.agents/skills/`

For Codex, append `codex/AGENTS.snippet.md` to `~/.codex/AGENTS.md` (Codex loads instructions, not skills).

Configure the panel per review-panel's instructions (`~/.config/review-panel/panel.toml`).

## Files

- `four-eyes/SKILL.md`: the skill, terse and directive.
- `four-eyes/briefs/`: templates for the verifier, worker and reviewer briefs.
- `codex/AGENTS.snippet.md`: the same method as a Codex global instruction.
