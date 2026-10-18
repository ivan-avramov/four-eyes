#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: 5.6.3 and Q2. review-panel SKILL.md always enforces fresh context, never admits L0, always computes and
#   reports evidenced levels whoever supplies the members; delegates only the acceptance of below-preferred levels,
#   only on `gate: caller` with the operator's recorded answer as evidence; otherwise its own gate applies (also
#   when members are supplied); the report states which gate applied. Amended to draft 5: `gate: deferred`, the
#   standalone preferred level L2, `none` admitted only by the operator's answer or `gate: caller`, a
#   non-interactive caller stops, and `checkout` is a `git clone --no-hardlinks` copy, never a worktree. Amended to
#   draft 6: `gate: deferred` dispatches no write-capable member, writes nothing outside the converge artifact
#   (its revision permitted), holds `none` findings separately and records no acceptance; `gate: caller` admits only
#   the members and levels the answer names; a standalone member whose evidence lands below the accepted level is put
#   to the operator before adoption. Amended to draft 7 (5.3, which defines what four-eyes passes; 5.6.3 still
#   carries draft 6's "writes nothing outside the converge artifact", contradicting 5.3, and is reported to the
#   driver): deferred writes nothing to the subject repository or any downstream artifact, orchestration records and
#   runtime state going to their guarded locations; "not re-reviewed" applies only after the last dispatch, per
#   converge mode; a `none` member, a member whose evidence lands below plan, or a round that lost coverage has its
#   findings held separately and not applied; `checkout` is a history-less copy (an export of the tracked files or a
#   single-branch depth-one clone from a file URL), never a worktree or a full clone, built per four-eyes's
#   Disclosure rule and scanned, any `.git` remnant included.
#   Amended to draft 8 (5.6.3, now aligned with 5.3): `checkout` is a `.git`-less export of the tracked files plus
#   explicitly authorised untracked files, never ignored or secret-bearing files, never a worktree and never a clone,
#   scanned for secret patterns together with the brief before dispatch, and review-panel states this rule itself
#   (no reference to four-eyes's Disclosure rule; draft 7's depth-one clone must be gone); a planned member reported
#   unavailable is the caller's unresolvable-selector hard stop; a held blocker or major counts toward continuing
#   converge (the stop rule lives in review-panel).
#   Rewritten for the rule, not the phrase: "always enforces fresh context" may be the standing imperative "Enforce
#   fresh context for every member"; "otherwise its own gate applies" may read "with neither flag, ask the operator
#   yourself". The phrase match required the words "always" and "own gate".
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

raw = read(RP_SKILL)
f = flat(raw)
problems = missing(f, [
    ("always enforces fresh context",
     r"always enforces? fresh context|fresh context[^.]{0,30}always|enforce fresh context for every member"),
    ("never admits L0", r"never admits? L0|L0[^.]{0,30}never"),
    ("levels computed and reported whoever supplies the members", r"whoever supplies the members|evidenced levels[^.]{0,80}(?:whoever|regardless)"),
    ("gate: caller", r"gate: caller"),
    ("operator's recorded answer as evidence", r"operator's recorded answer[^.]{0,30}evidence"),
    ("otherwise own gate applies", r"otherwise[^.]{0,40}own gate|with neither flag,? ask the operator yourself"),
    ("report states which gate applied", r"which gate applied"),
    # draft 5 additions to 5.6.3
    # draft 6 redefined `gate: deferred` and bound `gate: caller` to the answer's members and levels
    ("gate: deferred asks nothing", r"gate: deferred[^.]{0,120}ask(?:s)? (?:nothing|no question)"),
    ("deferred: no write-capable member dispatched", r"no write-capable member[^.]{0,40}(?:is )?dispatched|dispatch(?:es)? no write-capable member"),
    # draft 7 (5.3) scoped the deferred write prohibition and widened the held findings
    ("deferred: nothing written to the subject repository or any downstream artifact",
     r"nothing (?:is )?written to the subject repository or any downstream artifact"),
    ("deferred: orchestration records and runtime state to their guarded locations",
     r"orchestration records and runtime state[^.]{0,40}guarded locations"),
    ("deferred: the revision of the converge artifact permitted", r"revision of (?:the|that) converge artifact (?:is )?permitted"),
    ("deferred: not re-reviewed only after the last dispatch, per converge mode",
     r"not re-reviewed[^.]{0,60}only[^.]{0,40}after the last dispatch, per converge mode"),
    ("deferred: none, below-plan and lost-coverage findings held separately, not applied",
     r"none member, a member whose evidence lands below plan, or a round that lost coverage[^.]{0,60}"
     r"findings (?:are )?held separately,? (?:and )?not applied"),
    ("deferred records no acceptance", r"deferred[^.;]{0,30}records no (?:operator )?acceptance|it records no (?:operator )?acceptance"),
    ("caller admits only the members and levels the answer names", r"admits only the members and levels"),
    ("standalone evidence below accepted level put to the operator", r"lower level than (?:the )?accepted[^.]{0,80}operator"),
    ("standalone preferred level L2 against the driver", r"standalone preferred level is L2 against the driver"),
    ("none admitted only by operator's answer or gate: caller", r"admitted only by the operator's answer or under gate: caller"),
    ("non-interactive caller stops", r"non-interactive caller stops"),
])
# draft 8: checkout build-and-scan rule stated in review-panel itself; unavailable member; held blocker and converge
RULES = [
    ("checkout is a .git-less export of tracked plus explicitly authorised untracked files",
     [r"checkout", r"\.git-less export", r"tracked files", r"explicitly authorised untracked files"]),
    ("checkout never ignored or secret-bearing files, never a worktree, never a clone",
     [r"checkout", r"never ignored or secret-bearing files", r"never a worktree", r"never a clone"]),
    ("checkout copy and brief scanned for secret patterns before dispatch",
     [r"scan(?:ned)? the copy and the brief|copy and the brief[^.]{0,20}scanned", r"secret patterns", r"before dispatch"]),
    ("a planned member reported unavailable is the caller's unresolvable-selector hard stop",
     [r"unavailable", r"caller", r"unresolvable-selector hard stop"]),
    ("a held blocker or major counts toward continuing converge",
     [r"held blocker or major", r"toward continuing converge"]),
]
problems += [label for (label, rxs) in RULES if not sentence_with(raw, rxs)]
problems = ["missing: %s" % p for p in problems]
ctx = flat(section(raw, r"^Context$") or "")
# draft 6's full local clone and draft 7's depth-one clone carry history or point at it; neither may remain
if re.search(r"checkout[^.]{0,80}git clone --no-hardlinks", f, re.I):
    problems.append("draft 6 full-clone checkout rule still present")
if re.search(r"depth-one clone", ctx, re.I):
    problems.append("draft 7 depth-one clone checkout rule still present")
# draft 8: review-panel is the primitive; its checkout rule must not depend on four-eyes
if re.search(r"four-eyes", ctx, re.I):
    problems.append("checkout rule still refers to four-eyes")
verdict(problems, "gate delegation follows 5.6.3 and draft 8 5.3")
