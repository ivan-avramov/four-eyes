# four-eyes 0.6.0

An agent skill that puts the stages of a non-trivial change into separate hands: the session you talk to designs the change and judges the findings; other models, each in a fresh session, review the design, write the tests before they see the implementation, and review the finished change; a cheaper capable model implements from the approved specification. It runs on whatever models you have, down to one subscription with two models, and its report says which roles shared a model or a vendor, so you know what the configuration could not have caught.

The method is cooperative, not enforced. Helpers work in a copy of the repository with your normal CLI configuration; review members get read-only tools; nothing is committed without your word and nothing is pushed unless you say so in that turn. It is built for your own work on your own machine.

## What a run looks like

1. The session writes a specification with acceptance criteria.
2. A panel of other models reviews it (one round by default, up to three for security and architecture); the session adopts or declines each finding and says why.
3. You see the reviewed design, the planned cast and what pairs share a model or vendor, and say go.
4. A cheaper model implements it in a copy.
5. A different model writes tests from the specification alone, then runs them on the candidate and reviews it.
6. The panel reviews the change.
7. One fix round, then you see the final diff and give the commit word; a push only when you say so.

## Install

Requires [review-panel](https://github.com/ivan-avramov/review-panel) 0.4.0 or later. Copy the `four-eyes/` directory (`SKILL.md`, `briefs.md`) into a skills directory:

- user-wide: `~/.claude/skills/` (Claude Code) and `~/.agents/skills/` (Codex and other clients)
- per repository: `<repo>/.claude/skills/`, `<repo>/.agents/skills/`

To make qualifying work invoke the skill rather than rely on automatic selection, append `claude/CLAUDE.snippet.md` to `~/.claude/CLAUDE.md` and `codex/AGENTS.snippet.md` to `~/.codex/AGENTS.md` (the Codex snippet then loads into Codex helpers too, which is harmless: it tells them to do their one job). The models come from review-panel's `~/.config/review-panel/panel.toml`, in its order.

## Files

- `four-eyes/SKILL.md`: the skill.
- `four-eyes/briefs.md`: what each helper's brief carries.
- `claude/CLAUDE.snippet.md`, `codex/AGENTS.snippet.md`: standing triggers.
- `docs/`: proposals and run records, including the 0.5.0 design (`principle-over-models.md`) that this version replaces.

## History

0.4.0 and 0.5.0 enforced isolation with macOS sandbox profiles, run-scoped CLI configuration directories, independence levels, declared tiers and a cost ledger. 0.6.0 drops the enforcement and the bookkeeping and keeps the roles, the fresh sessions, the tests-before-candidate rule and the honest report. The heavier designs remain on the branch `fe-run2-per-session-resolution` for anyone who wants them.
