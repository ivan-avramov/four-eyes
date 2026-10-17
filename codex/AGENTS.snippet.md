## four-eyes (role-based multi-provider method)

For any multi-file change, new component, architecture, or anything touching security or a data
boundary, work in four roles and never name a required model: Designer (this session) writes a
specification with pre-registered acceptance criteria; Verifier (a different provider's strongest
available model, cold context, adversarial; use `claude -p` when available) reviews it before any
implementation and every finding gets a disposition; Worker (a capable model in its own context)
implements from the approved specification only, commits and pushes nothing; Reviewer (a capable model
distinct from the worker, cold context) writes adversarial tests first, runs the suite, reviews for
security and quality. Report the provider and model actually used per role as
`[four-eyes] designer: … | verifier: … | worker: … | reviewer: …`. If a role cannot be filled as
intended (missing CLI, auth, usage limit, same model as another role), stop and ask the operator with
a recommendation. Workers and reviewers never edit running scripts in place, never print environment
variables, never touch decision logs or agent instruction files, never push.
