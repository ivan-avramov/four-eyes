# four-eyes 0.5.0 and review-panel 0.3.0: principle over models

Status: specification, draft 7 (2026-10-18; draft 7 adds the third candidate panel's amendments under the operator's standing authorisation: vendor evidence only from a runtime's named provider, the split of zero-match selector cases, secrets found at or after the baseline, the scope of gate: deferred, held findings at the gate, the not-re-reviewed label per converge, a history-less checkout, resume-id evidence, escalation cycles under gate: caller, and the cost block's execution placeholder; draft 6 added the second candidate panel's consistency amendments, operator-approved, not re-verified: the none-pair exemption from the L1 stop, the gate: deferred and gate: caller semantics, standalone evidence reconciliation, the unresolved-converge definition, sanitisation scope, none members counted as unresolved, selector matching, phase B re-runs as executions). Draft 4 followed three review-panel converge rounds
(Codex and a Claude model each round) and was approved by the operator on 2026-10-18. Draft 5 applies
the amendments the operator accepted the same day after the implementation's reviewer and panel read
the candidate (fresh-context definition, run-level symbols, cross-vendor unresolved identity, the
step-2 gate flag, the roles-block flags field, the Isolation stop, the none wording in review-panel,
the second-question causes, remediation sessions, the build checkpoint per candidate); they are
disclosed here and not re-verified. The review-panel changes are proposed to the operator for that
repository, applied by the session only to the installed copies.

## 1. Goal

Both skills capture a principle, independent review across separated roles in fresh contexts, and
never a required vendor or model. They run on whatever the operator has, down to one subscription
offering two models that pull double duty, and tell the operator plainly, before anything is built,
what that configuration does not check. They spend the expensive models on design and verification and
the cheaper capable ones on implementation and routine review. They verify a specification in one
round by default and converge over several rounds for security and architecture. Every run reports
what it cost, in the units the runtimes actually report.

## 2. Original request (operator, 2026-10-18, paraphrased from the handoff)

Capture the principle, not specific models or providers; must work with a single subscription (two
models pulling double duty) with the user informed of what that cannot catch; spend expensive models
on design and verification, cheaper ones on implementation and routine review; add a light mode (one
verifier round by default, full three-round converge only for security and architecture) and cost
reporting. Keep review-panel as the review primitive and four-eyes as the workflow on top; relax both
to principle-based selection with a disclosed degraded mode.

## 3. Settled constraints

- S1 (operator, decision record 2026-10-18): the method and the review-panel skill capture role
  separation and independent review, never specific models or providers.
- S2 (operator, same): both must work down to a single subscription offering two models that pull
  double duty, with the user told what that configuration cannot catch.
- S3 (operator, same): expensive models on design and verification; implementation and routine review
  on capable cheaper ones.
- S4 (operator, four-role decision 2026-10-18): the method asks the operator before proceeding
  degraded rather than stopping dead; it names roles, never required models, and reports the models
  actually used.
- S5 (operator, this session): review-panel changes are proposed, not applied, by the Premisa session;
  four-eyes changes follow verification and the operator's approval.
- S6 (four-eyes 0.4.0, unchanged here): isolation of write-capable roles in a fresh copy, disclosure
  scanning before anything leaves the host, evidence of what ran per role, the approval gate before
  dispatch, the reviewer's tests frozen before the candidate is revealed, commit of the candidate's
  files only, push only on the operator's explicit word.

## 4. Assumptions (the designer's)

- A1 review-panel stays the review primitive and four-eyes the workflow on top; neither is retired.
- A2 S4's "asks before proceeding degraded" is satisfied by one question per run, folded into the
  approval gate that every run already has: verification, which is read-only, may run at the planned
  levels with the disclosure printed, and nothing write-capable is dispatched until the operator's
  recorded answer accepts the run's levels and tier substitutions. No acceptance persists between runs
  (the persistent store of earlier drafts was dropped: it saved one prompt per run and created drift,
  forgery and bootstrap problems). The operator may prefer the store (open question Q1).
- A3 Tier and vendor are declared by the operator per member, dated; the host's model list is the
  fallback for tier, model knowledge the last resort and a degradation in its own right.
- A4 Cost is reported from what the runtimes themselves return; nothing is estimated; money is
  bucketed by runtime and by a billing basis the operator declares per runtime, and never summed
  across buckets.
- A5 "Architecture", for the strict trigger: a new component; a new interface between components or a
  material change to an existing interface's contract; a change to a component's responsibilities (an
  example on each side: moving validation from the client to the server is one; renaming a function
  inside one module is not) or to the dependency relationships between components; a data-model
  change; a change to consistency or execution semantics (synchronous to eventual); a change to
  deployment or isolation.
- A6 Runtime facts relied on, checked on this machine on 2026-10-18: the Claude CLI's JSON result
  carries `usage` (uncached input, cache read, cache creation, output), `modelUsage` per model with
  tokens and `costUSD`, `total_cost_usd`, `duration_ms` and `session_id`; Codex CLI 0.161 plain
  output carries a `model:` header, a `session id:` header and a final `tokens used` footer with one
  total. Not checked: whether either runtime reports a resumed session's figures per invocation or
  cumulatively; until checked, a resumed delivery's usage is `unreported`.

## 5. Design

### 5.1 Independence levels replace vendor requirements

Independence is a property of a pair of roles, evidenced per member. Fresh context is a prerequisite
of every level; vendor and model distinctness add to it.

| Level | Meaning | Reduces correlated risk from | Does not reduce (fixed disclosure wording) |
|---|---|---|---|
| L3 | fresh context, different vendor (maker of the model) | transcript anchoring, model-specific errors, vendor-wide habits | blind spots shared across the industry's training data and conventions |
| L2 | fresh context, same vendor, different model | transcript anchoring, model-specific errors | vendor-wide training habits, shared tuning, shared data blind spots |
| L1 | fresh context, same model | transcript anchoring | anything the model gets wrong consistently, including its own code and reasoning habits |
| none | fresh context not established | nothing established | may share the driver's context; independence not established |
| L0 | shared context | nothing | forbidden for any required pair |

A level describes which correlated risks the configuration reduces, never that a class of error was
caught; a report may claim a defect was caught only when a finding shows it.

Fresh context, operationally: a new session with its own session id, started without a resume or fork
flag, inheriting no transcript, summary or memory from any other role's session, with automatic and
shared agent memory disabled. Freshness is evidenced per execution: the runtime's session id, the
recorded command (no resume flag; the memory-disabling flag or configuration), the working directory
and the instruction files present in it, recorded, not required absent: the briefed material includes
the isolated copy for write-capable roles and the read-only checkout for checkout members. One
exemption: the reviewer's phase B resumes the reviewer's own phase A session and no other; the resumed
id is recorded and checked equal to the phase A id, an unequal id meaning `replaced (lost session)`
with a new candidate-blind phase A, and each runtime's resume-id behaviour is probed once per machine
(sandbox probes) before the exemption is relied on. Remediation runs in a new worker session. Where freshness cannot be evidenced (a host subagent exposes no
session id), the role has no level: it is admissible for a required pair only by the operator's answer
in that run's gate (5.3), is reported with the `none` wording, and never counts toward distinct models.
The driver's own session never fills a required pair.

Identity: the member's model is the observed model the runtime resolves the requested selector to
(per runtimes.md's alias rules; after dispatch, zero matches with another model present is an unexpected substitution and a hard stop, more than one match is an evidence mismatch, and a selector that cannot be resolved before dispatch is the unresolvable-selector hard stop), from the
runtime's evidence (0.4.0's sources); other models a runtime reports for the same execution are
auxiliary, listed as such in the ledger and excluded from levels and counts. Vendor comes from the
operator's dated declaration in the panel file, cross-checked against the observed model id and the
runtime, with `vendor basis: declared | observed | model knowledge` recorded; model knowledge as the
basis is a degradation with fixed wording. An unverified alias (a host subagent, an echoed selector
with no resolved model) supports L1 at most on the model axis, since unknown identity cannot establish
model distinctness, but a vendor the runtime's own output names as the model's provider (Codex's `provider:` header, recorded in the execution record) reaches L3 with the model counted as identity unresolved; the maker of a CLI is never vendor evidence, and with no provider named the vendor falls back to the declaration or to unknown; Codex's `model:` header is the resolved model, as
runtimes.md states. An unknown vendor counts as the same vendor, so known-different models of unknown
vendor reach L2 at most, and a request for "a vendor other than X" is never satisfied by an unknown
vendor.

Required pairs, preferred and minimum levels:

| Pair | Preferred | Minimum |
|---|---|---|
| verifier member against designer | L3 | L1 |
| worker against driver (the designer's session) | L1 | L1 |
| reviewer against worker | L2 | L1 |
| panel member against worker | L3 | L1 |
| panel member against reviewer | L3 | L1 |

Levels are planned from the declared roster and the concrete role-to-member assignment before
dispatch, and reported from evidence after it. After every dispatch and every round the driver
recomputes each level from the observed model, vendor and freshness evidence of the members that
returned a valid result; a planned level the evidence does not support is a recorded re-ask of the
operator before the output is adopted, and a changed model identity is an unexpected substitution
(hard stop) as in 0.4.0. A panel's level against a role is the minimum over the members that returned
valid results, printed in the member-by-role matrix beside each member's own level; when a round loses
planned coverage because a member failed or returned no valid result, the effective matrix drops and
the run re-asks before adopting that round's findings. A pair that cannot reach L1 by evidence and is not a `none` pair the operator admits at the gate stops
the run before dispatch, with a stop report; `none` is never admissible for a write-capable role. A
`none` member counts among the identity-unresolved k, never toward m.

Disclosure lines are per member pair: one line per distinct level present, listing the member pairs at
that level, with the wording from the table byte for byte; pairs below their preferred level are
marked degraded in the same line; panel minimums appear in the matrix. A run-level line follows:
`verified distinct models across all roles: m (identity unresolved: k); verified distinct vendors: v`.
When k is zero and m is two: `Every check in this run was made by two models; an error both make
consistently is not reduced, and on L1 pairs an error that model makes consistently is not reduced.`
When k is zero and m is one: `Every check in this run was made by one model; any error it makes
consistently is not reduced.` When k is not zero, no total is asserted; the line stands alone. Further
fixed wordings: `reviewer shares the designer's model: the adversarial tests do not reduce misreadings
of the specification that model makes consistently`; `tier basis: model knowledge, cutoff <date>`;
`vendor basis: model knowledge`; `designer below top tier`; `verifier below top tier`; `top-tier model
filling a capable role: <role>`.

### 5.2 Tiers and precedence

Two tiers, `top` and `capable`, declared by the operator per member in the panel file with a date,
printed with that date; tier basis when undeclared: the host's reported model list, then model
knowledge with its cutoff date (a degradation). Designer and verifier draw from `top`; worker,
reviewer and the candidate panel from `capable`.

Precedence when filling a role: reach the pair's preferred level first, then the cheapest tier that
reaches it; a `top` member takes a `capable` role only when it reaches a higher level than any
`capable` member can, recorded with its fixed wording and put to the operator in the gate beside the
alternative level the `capable` member would reach; a `capable` member sits on a verifier or candidate
panel beside a `top` member when it adds a level no `top` member reaches. The verifier panel always
includes at least one `top` member; a fresh session of the designer's model counts when the designer's
model is `top` (L1). When no `top`
member exists at all, the verifier is all-`capable` only by the operator's answer (`verifier below top
tier`). A session model that is not `top` is `designer below top tier`, put to the operator the same
way. The reviewer's model equalling the designer's is disclosed with its fixed wording, and another
member is preferred when one reaches the same level.

### 5.3 The run's one question

The panel file (`~/.config/review-panel/panel.toml`) gains optional per-member `vendor` and `tier`
with dates, and an optional per-runtime `billing` (`api` or `subscription`) with a date. Nothing in it
records acceptances; four-eyes never writes it.

Before step 2 the driver plans the role-to-member assignment, the level of every required pair, the
tier substitutions and every degradation, and prints them. Step 2 (verification, read-only) runs at
the planned levels with the disclosure printed in the report. Step 3, the approval gate, is one
message to the operator carrying, in this order: the verified specification and the not-re-reviewed
changes (with a recommendation to run a second verification round when an applied change resolved a
blocker); the mode and its reason; the planned assignment with every pair's level and the table
wording for each level below L3; every pair below its preferred level, marked; every degradation and
tier substitution with the alternative; the recommendation; and the request for approval. Nothing
write-capable is dispatched before the operator's answer, which the report records verbatim with a
timestamp, and which may approve, approve with changes to the assignment, or stop. In strict mode the
same message is sent; there is no configuration that skips it. Beyond the gate, questions arise only
from escalation (5.4), lost coverage or an evidence mismatch (5.1), or the procedure's named operator
decisions (an unresolved converge, a changed operator tree at acceptance, an unresolved blocker after
remediation, a second remediation round, an out-of-scope build hit, a found secret); each is recorded
with its cause label; if the operator declines any of them the run stops with a report and no commit.
At step 2 four-eyes passes review-panel `gate: deferred`: no write-capable member is dispatched, nothing
is written to the subject repository or any downstream artifact, orchestration records and runtime
state go to their guarded locations as always, and the driver's own revision of the converge artifact
is permitted, labelled not re-reviewed only when applied after the last dispatch, per converge mode;
levels are reported, no question is asked; a `none` member, a member whose evidence lands below plan,
or a round that lost coverage, runs and is reported, its findings held separately and not applied; the
gate message lists every held finding with the driver's proposed disposition, the operator's answer
that admits the member also approves the resulting specification, a held change applied after the
answer returns to the gate, and a held blocker or major counts as `unresolved converge` until the gate
admits the member. An escalation cycle after the gate runs under `gate: caller` with the escalation
answer. At the candidate panel and every remediation panel four-eyes passes `gate: caller` with the
operator's recorded gate answer, which admits only the members and levels that answer names; any
other `none` member or lower level stops review-panel and returns to the caller as lost coverage or an
evidence mismatch. An `unresolved converge` is a set of findings the driver still holds unresolved,
never the mere reaching of the round cap; named decisions that arise before the gate (`unresolved
converge`, `unsupported context`, `found secret` at step 2) fold into the gate message where possible,
each keeping its cause label. Sanitising a found secret touches only disposable material outside the hashed candidate tree (briefs,
scratch), with the redactions recorded; a secret in any tracked file of that tree, found before the
baseline, waits for the operator to remove it from the tree; a secret found at or after step 4, in the
baseline or the candidate, stops the run with a report, or, on the operator's answer, rebuilds from
step 4 on the cleaned tree with every derived artifact invalidated; a secret in the candidate is also a
candidate finding and is never dispatched for remediation.

Worked minimum: one vendor, two models, A (`top`) and B (`capable`), both on a CLI runtime that
reports the model and session it ran. With two models at least one required pair is always at L1.

- Designer: A, the session.
- Verifier: panel of a fresh A (L1 against the designer, `top`) and B (L2, `capable`, beside A per
  5.2); one round in light mode.
- Worker: B, fresh session, isolated copy (L2 against the driver).
- Reviewer: fresh A (L2 against the worker; shares the designer's model, disclosed; a top-tier model
  filling a capable role, the alternative being B at L1). Precedence picks A; the gate shows both.
- Panel on the frozen candidate: fresh A (L2 against the worker, L1 against the reviewer) and fresh B
  (L1 against the worker, L2 against the reviewer); panel minimum L1 against both roles; both members
  are needed to reach L2 against either role.

Gate message disclosures: L1 (verifier A against designer; panel A against reviewer; panel B against
worker), L2 (the rest), `reviewer shares the designer's model`, `top-tier model filling a capable
role: reviewer` with the alternative, `verified distinct models across all roles: 2 (identity
unresolved: 0); verified distinct vendors: 1`, the two-model sentence. With one model the same shape
runs at L1 throughout and prints the one-model sentence.

### 5.4 Light and strict modes

- **Light** (default): the verifier is one review-panel converge invocation with `rounds = 1` passed
  by four-eyes (dispatch, adjudicate, apply, no re-dispatch); specification changes applied after the
  dispatch are listed at the gate as not re-reviewed. Reviewer phases A and B unchanged. The panel on
  the frozen candidate is one invocation. Remediation: findings go to a new worker session once, with the specification, the candidate, the
  findings and the frozen tests; the fixed
  candidate goes through phase B in full and, since its contents changed after the panel read them,
  through the panel again in fresh sessions, which in light mode may be scoped to the remediation diff
  with the full candidate and the diff range supplied and the limit recorded; each panel verdict is
  bound to the hash of the candidate it read. An unresolved blocker or major after that one remediation
  goes to the operator.
- **Strict**: the verifier converges with `rounds = 3` under review-panel's stop rules. The panel on
  the frozen candidate is one invocation, briefed explicitly on any hunks that triggered strict.
  Remediation re-runs phase B and the full panel; a second remediation round goes to the operator (as
  0.4.0).

Strict is mandatory when the work touches security, authentication, permissions, secrets, a data
boundary, or architecture (A5); the operator may ask for strict on anything. A waiver is the
operator's explicit answer naming the trigger class it covers for this run, recorded in the roles
block; a hit on a waived class is recorded `waived`, not `clear`, and does not escalate. The triggers
are evaluated at three checkpoints and the result recorded each time: after design, against the
specification text; at the gate; after build, against the candidate diff (paths, new or changed
interfaces, permission checks, secret handling), and again against every later candidate hash (each
remediation). The verifier brief asks members to flag strict
triggers they see; a member-flagged trigger escalates unless the operator waives it, since the driver
is the interested party.

Escalation: an unwaived hit at any checkpoint in a light run switches the run to strict and asks the
operator (a recorded second question) with any pair below its preferred level. A build-checkpoint hit
on code the specification does not cover is also a finding against the candidate (out of scope) that
goes to the operator. The verifier then runs a new verification cycle of up to three rounds on the
current specification; cycles are reported separately and R3 counts per cycle. If the cycle changes
the specification, every artifact derived from the superseded text is invalid: the run returns to the
gate, dispatches the worker afresh, and a new reviewer session with no access to any prior candidate
performs a new candidate-blind phase A with newly frozen tests before any candidate is revealed
(recorded `replaced (escalation)`). If the cycle changes nothing, the run proceeds under strict from
where it was.

### 5.5 Cost reporting

Units: an execution is one runtime invocation (one panel member in one round, the worker, each of the
reviewer's two deliveries and each re-run of phase B, resuming the same reviewer session and exempt as
phase B, each remediation dispatch), with a unique execution id; a panel invocation
is one round of one panel; a verification cycle is one converge call of one to three rounds. R3 counts
invocations and cycles; the ledger counts executions.

Each execution has one record: id, role, phase, runtime, requested selector, observed model (the
member's identity), vendor and vendor basis, tier, session id, freshness evidence, dispatch and finish
timestamps, wall seconds, tokens (input uncached, cache read, cache creation, output, or a
`total-only` figure where the runtime reports one unsplit total), money (one authoritative figure per
execution, with currency), each field as the runtime reports it or `unreported`. Per-model breakdown
records (tokens and money per model, auxiliary models marked) attach to the execution record and are
never summed into execution totals. A resumed delivery's usage is `unreported` until A6 is extended
with a checked fact. Sources per A6: the Claude CLI's `usage`, `modelUsage` (breakdown), `total_cost_usd`
(authoritative money), `duration_ms`, `session_id`; Codex's `tokens used` footer (`total-only`),
`model:` and `session id:` headers; a host subagent `unreported` throughout. The driver's own session
(design, adjudication, orchestration) is a record too, with the run-scoped delta where the host exposes
it, else `unreported`; a host figure that includes delegated or earlier work is never used.

The report ends with the ledger, a timestamped event sequence (questions, answers, approvals, dispatch
and finish of every execution id, freezes, hashes, commit), and a totals block that references them:

```
[four-eyes cost] executions: <e> (top <n>, capable <n>, driver 1) | elapsed: <first dispatch to acceptance> | execution seconds summed: <s> over <n> of <e> reported | tokens by runtime and vendor: <runtime>/<vendor>: input <n> cache-read <n> cache-creation <n> output <n> | total-only <n>, over <n> of <e> executions; ... | money by runtime and billing basis: <runtime> (<declared basis, date | basis unknown>, <currency>): <sum> over <n> of <e>; ... | by phase and tier (executions, seconds): verify <...>, build <...>, review <...>, panel <...>, remediate <...>, driver <...>
```

Tokens are never summed across runtime-and-vendor buckets; money is never summed across runtimes,
currencies or billing bases; an undeclared basis is its own bucket labelled `basis unknown`. Every
subtotal states its coverage (`over n of m`). Nothing is estimated. review-panel reports the same
per-execution fields and a per-round totals block.

### 5.6 review-panel 0.3.0, proposed to the operator

1. Panel file: optional per-member `vendor` and `tier` (`top` or `capable`) with dates; optional
   per-runtime `billing` with a date. Existing 0.2.0 files stay valid; absent fields are warned and
   resolved per 5.1 and 5.2, and the report carries a file-load warnings line. No acceptance table.
2. Default panel with no file and no stated panel: as 0.2.0, one member running a model other than
   yours on a CLI runtime, in a fresh session, its level against the driver reported from evidence (L2
   or L3) and disclosed; if only your own model exists, a fresh session of it (L1) after asking the
   operator; a non-interactive caller stops instead of asking; stop when no fresh session is possible.
   The default's order of preference among other models is the roster's, not the skill's; a preference
   for another vendor is the operator's to declare in the file.
3. review-panel always enforces fresh context, never admits L0, and always computes and reports
   evidenced levels, whoever supplies the members. Its standalone preferred level is L2 against the
   driver (L3 welcome); a member at `none` is admitted only by the operator's answer or under `gate:
   caller`, and carries the fixed `none` wording of 5.1; a non-interactive caller stops instead of
   asking. Only the acceptance of levels below preferred is delegated, and only when the caller states
   `gate: caller` and passes the operator's recorded answer as evidence, which admits only the members
   and levels it names; `gate: deferred` dispatches no write-capable member, writes nothing outside the
   converge artifact (the caller's revision of that artifact is permitted), reports levels and asks
   nothing, holding a `none` member's findings separately; otherwise review-panel's own gate applies,
   and a standalone member whose evidence lands below the accepted level is put to the operator before
   its findings are adopted, a non-interactive caller stopping instead. The report states which gate
   applied, `deferred` recording no acceptance. The `checkout` context is a separate history-less copy (an export of the tracked files, or a
   single-branch depth-one clone from a file URL), never a worktree and never a full clone, built per
   four-eyes's Disclosure rule and scanned, any `.git` remnant included.
4. Converge accepts `rounds` (1 to 3); the default stays 3 so standalone callers see no change; the
   caller decides the round count (four-eyes passes 1 in light mode and 3 in strict). The `opinion`
   and `research` modes are unchanged.
5. A caller may request members by constraint (vendor other than X, tier top) instead of by name;
   review-panel resolves from the roster, reports the level achieved per constraint from evidence (an
   unknown vendor never satisfies "other than"), and never silently substitutes.
6. Totals bucket money by runtime, billing basis and currency; the execution record carries role and
   phase, supplied by the caller where applicable; a tier absent from the file resolves per 5.2 (host's
   model list, then model knowledge with its cutoff as a degradation); panel.example.toml ships vendor,
   tier and billing as commented examples or load-failing placeholders, and a declaration that
   contradicts the runtime or the observed model id falls back to same vendor and is an evidence
   mismatch.
7. Report: a questions section (every operator question and answer verbatim with timestamps, or
   `none`); the file-load warnings line; per member and round the 5.5 execution record; a totals block
   per round and per run with coverage; the roster names each member's tier, vendor basis and evidenced
   level against the driver; which gate applied.
8. Runtimes: the evidence fields of A6 are the cost and identity evidence; a subagent is `unreported`.
9. Wording: "a model other than yours" stays the default; the file never names a vendor as required.

### 5.7 four-eyes 0.5.0 changes

- Isolation: a write-capable host subagent that cannot be confined stops the run (settled 2026-10-18,
  replacing 0.4.0's "or gate"); otherwise isolation is unchanged.
- SKILL.md: Roles and tiers rewritten around 5.1 and 5.2; "When a role cannot be filled" rewritten
  around 5.3 (plan, verify read-only, one gate message, proceed on the recorded answer; the unchanged
  hard stops: missing CLI, failed authentication, usage limit, unresolvable selector, unexpected
  substitution, unenforceable isolation, no fresh session possible); Procedure steps 2, 3, 6, 7, 8 and
  9 take the mode, checkpoints and escalation of 5.4; the reviewer's two deliveries come from one
  session, and a replaced reviewer session always means a new candidate-blind phase A with newly frozen
  tests, recorded `replaced (lost session | escalation)`; step 10 records the baseline, the authorised
  candidate delta (paths and content hashes) and the actual commit delta, requires the two deltas to be
  equal, and keeps tree equality with the final candidate hash bound to the last panel verdict as a
  separate check; `push: none` is written when nothing was pushed; step 11 adds the ledger, the event
  sequence and the cost block; a run that stops produces a report with outcome `stopped`, the stop
  cause, `not reached` for every later checkpoint and field, and the statement that no write-capable
  dispatch, commit or push followed.
- Roles block:

```
[four-eyes 0.5.0] outcome: completed|stopped|rejected | mode: light|strict (<reason>; checkpoints: design <hit|clear|waived|not reached>, gate <...>, build <...>; escalation: <none|at <checkpoint>, cycle n>; waiver: <none|operator, classes, reason>; flags: <member-flagged triggers and dispositions | none>) | designer: <runtime:vendor/model, vendor basis, tier, evidence, session> | verifier: <per member: runtime:vendor/model, tier, Lx against designer, fresh <evidenced|none>, returned|failed; cycles n, rounds n> | worker: <runtime:vendor/model, tier, evidence, Lx against driver> | reviewer: <runtime:vendor/model, tier, evidence, Lx against worker, phase B resumed <id equal>|replaced (<cause>)> | panel: <per member: ... Lx against worker, Lx against reviewer, returned|failed; panel minimum Lx/Lx> | verified distinct models: m (unresolved k); vendors: v | gate: <timestamp, operator's answer verbatim; second questions: <...>|none>
```

- briefs/verify.md: the brief states the mode, cycle and rounds and asks members to flag strict
  triggers. briefs/worker.md and briefs/review.md: unchanged except the version in the constraint
  block reference and the replacement rule for the reviewer session.
- README: a section "What a degraded run does not check" carrying the 5.1 table and the run-level
  sentences, a section on cost and its units, and the S6-to-report-field mapping (Q4).
- Snippets (CLAUDE.snippet.md, AGENTS.snippet.md): add "strict mode for security and architecture,
  light otherwise".
- Version 0.5.0; `requires: review-panel 0.3.0 or later`.

## 6. Acceptance

Two kinds. Run criteria (R) are checked from one run's report alone and name the field that evidences
them; each applies to the outcomes named. Release checks (Q) are checked once against the skill files
and scripted scenarios before the version ships, and the qualification report is kept with the
release.

- R1 (completed) On a roster of one vendor with a `top` and a `capable` member, the gate message
  shows the 5.3 worked-minimum assignment, every pair's level, panel minimum L1/L1, the L1 and L2
  disclosures, the reviewer-shares-designer and top-filling-capable wordings with the alternative, and
  the two-model sentence; the questions section holds that one message and the operator's answer with
  timestamps, and the event sequence shows no write-capable dispatch before the answer.
- R2 (completed, stopped) Every second question (escalation, lost coverage, evidence mismatch) appears
  in the questions section with its cause, and a declined second question shows outcome `stopped` with
  no commit.
- R3 (completed) In light mode the report shows one verification cycle of one round and one
  candidate-panel invocation per candidate hash read; in strict mode cycles of up to three rounds under
  review-panel's stop rules and a panel invocation after each remediation; every panel invocation shows
  fresh session ids; the reviewer's phase B session id equals its phase A id or the block says
  `replaced` with its cause and a new phase A freeze time before the new reveal.
- R4 (completed, stopped) The roles block names the outcome, mode, reason, the three checkpoint results
  (`not reached` where applicable), any escalation with its cycle, any member-flagged trigger with its
  disposition, and any waiver with its classes and the operator's reason.
- R5 (completed) The ledger holds one record per execution with the 5.5 fields or `unreported`,
  breakdown records attached and auxiliary models marked, the driver record included; the totals block
  states coverage for every subtotal, buckets tokens by runtime and vendor with a total-only column,
  buckets money by runtime and billing basis, and separates elapsed from summed execution seconds.
- R6 (all outcomes) No required pair is reported at L0; a pair resting on an unverified alias is at L1
  at most; a role with unestablished freshness carries the `none` wording and the operator's answer;
  a run that cannot reach L1 by evidence, with no `none` pair admitted at the gate, has outcome `stopped` naming the pair.
- R7 (all outcomes) Disclosure wording and the run-level sentences match 5.1 byte for byte; one line
  per distinct level listing member pairs; the sentences appear only when unresolved identities are
  zero.
- R8 (completed) The report shows the baseline, the authorised candidate delta and the commit delta
  equal, the committed tree hash equal to the final candidate hash bound to the last panel verdict, the
  frozen test hash and freeze time before the candidate reveal time, the isolation probes, the
  disclosure scan per dispatch, the gate answer, and `push: none` or the operator's words.
- Q1 Neither SKILL.md names a vendor or model as required: a script checks a list of known vendor and
  model names against an allowlist of example and report sections, and a named reviewer signs the
  semantic reading in the qualification report.
- Q2 review-panel honours `rounds` with default 3; with no panel file it follows 5.6.2, asking or
  stopping as stated; a 0.2.0 panel file loads with warnings only; its report carries the questions
  section, the warnings line, the gate that applied and the per-execution fields; with members
  supplied and no `gate: caller`, its own gate applies.
- Q3 A host subagent member without session evidence is reported with the `none` wording and triggers
  the question; it never raises the distinct-model count.
- Q4 Every S6 guarantee maps to a named report field (R8) and the mapping is listed in the README.

## 7. Non-goals

- No money estimation; no pricing tables.
- No change to isolation, the write guard, disclosure scanning or the evidence sources beyond adding
  tier, vendor basis, level, freshness, session, timestamp and cost fields.
- No retirement or merger of review-panel into four-eyes.
- No automatic detection of which tier or vendor a model belongs to.
- No persistent acceptance store.

## 8. Open questions (for the operator)

- Q1 One question per run at the gate (A2) against a persistent acceptance store that skips the
  question when the configuration is unchanged. Recommendation: per run. The gate is interactive every
  run anyway, so the store saves at most one prompt, and three review rounds showed it needs
  fingerprints over observed models, expiry, provenance hashes and a bootstrap rule to be safe.
- Q2 Whether the candidate panel may be scoped to the remediation diff in light mode (5.4) or must
  always read the full candidate again. Recommendation: scoped with the full candidate supplied and the
  limit recorded, since the verdict is bound to the final hash either way.
- Q3 Whether an all-`capable` verifier (no `top` member at all) should be allowed by the operator's
  answer (5.2) or refused outright. Recommendation: allowed; refusing would make the method unusable on
  a subscription with no `top` model, against S2. Having a `top` member of only the designer's vendor
  is a different case: the verifier stays `top` and the independence level drops.
- Q4 Whether review-panel's no-file default should prefer another vendor when one exists (changes
  egress and cost for standalone callers unasked) or keep 0.2.0's roster order (5.6.2 as written).
  Recommendation: keep the roster order; the operator declares vendor preference in the file.
