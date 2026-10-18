## four-eyes

Skip this section if you were dispatched as a worker, a reviewer or a review-panel member, or if your brief says you perform one phase only.

For non-trivial development work (multi-file changes, new repositories or components, architecture, substantial single-file changes) and always for anything touching security, authentication, permissions, secrets or a data boundary, follow the installed `four-eyes` skill: read its `SKILL.md` and `briefs/` from the repository's `.agents/skills/four-eyes` or from `~/.agents/skills/four-eyes` (it requires `review-panel`). Use strict mode for security and architecture, light otherwise. Fill its roles as it says, record the evidence of the models that ran, and stop to ask the operator with a recommendation when a role cannot be filled as intended. Small unambiguous edits outside those areas are exempt; the operator may invoke it for anything. If the skill is installed in neither place, say so and ask before proceeding.
