#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: 5.3, 5.1 and R2 (amended to draft 5). four-eyes/SKILL.md says that beyond the gate questions arise only
#   from escalation, lost coverage, an evidence mismatch, or the procedure's named operator decisions (an
#   unresolved converge, a changed operator tree at acceptance, an unresolved blocker after remediation, a second
#   remediation round, an out-of-scope build hit, a found secret), each recorded with its cause label; that a
#   planned level the evidence does not support is a recorded re-ask before the output is adopted, with levels
#   recomputed after every dispatch and round; and that declining any of them stops the run with no commit.
#   Amended to draft 6: an unresolved converge is never the mere reaching of the round cap; named decisions before
#   the gate fold into the gate message; sanitising touches only files outside the candidate's paths and the briefs,
#   redactions recorded, and a secret in a file in scope stops the run until the operator removes it. Amended to
#   draft 7 (5.3 unchanged in "questions arise only from"): sanitising touches only disposable material outside the
#   hashed candidate tree (briefs, scratch), redactions recorded; a secret in a tracked file of that tree found
#   before the baseline waits for the operator to remove it; a secret found at or after step 4 stops the run with a
#   report or, on the operator's answer, rebuilds from step 4 with every derived artifact invalidated; a secret in
#   the candidate is also a candidate finding, never dispatched for remediation. Draft 6's scope must be gone.
#   Amended to draft 8 (5.3): the operator may answer `not a secret` with the pattern, path and reason, recorded in
#   the report, and the run continues on that answer; a pre-baseline removal is committed in the operator repository
#   before step 4 records the state; the specification is committed before step 4; other authorised untracked files
#   are listed and excluded from the step 10 delta and tree comparisons.
#   Rewritten for the rule, not the phrase: the text is read without markdown emphasis, so "**only** from" is
#   "only from" (the phrase match failed on bold markup); the found-secret decision may be worded "a found or
#   non-excludable secret" within the named decisions; the recompute rule may lead with its condition ("after every
#   dispatch and every round, recompute each level"). The phrase match required one word order.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

raw = read(FE_SKILL)
f = prose(raw)
problems = missing(f, [
    ("questions only from escalation, lost coverage, evidence mismatch",
     r"(?:questions|second question)[^.]{0,80}only from[^.]{0,40}escalation[^.]{0,40}lost coverage[^.]{0,40}evidence mismatch"),
    ("named decision: unresolved converge", r"unresolved converge"),
    ("named decision: changed operator tree", r"(?:changed operator tree|operator tree changed)"),
    ("named decision: unresolved blocker after remediation", r"unresolved blocker"),
    ("named decision: second remediation round", r"second remediation"),
    ("named decision: out-of-scope build hit", r"out-of-scope build hit|out of scope"),
    ("named decision: a found secret",
     r"named operator decisions[^.]*\b(?:found (?:or non-excludable )?secret|secret found)\b"),
    ("cause label recorded", r"cause label"),
    ("re-ask before output adopted", r"re-ask[^.]{0,80}before[^.]{0,30}adopt"),
    ("recomputed after every dispatch and round",
     r"recomput[^.]{0,80}(?:every|each) dispatch|after (?:every|each) dispatch and (?:every|each) round,? recompute"),
    ("declining stops with no commit", r"declines?[^.]{0,40}(?:second question|any of them)[^.]{0,60}stops?[^.]{0,40}no commit"),
    # draft 6 (5.3): unresolved converge defined, pre-gate decisions folded into the gate, sanitisation scoped
    ("unresolved converge is not the round cap", r"never the mere reaching of the round cap"),
    ("pre-gate named decisions fold into the gate message", r"before the gate[^.]{0,120}fold into the gate message"),
    # draft 7 (5.3): secrets by where and when they are found
    ("sanitising touches only disposable material outside the hashed candidate tree",
     r"sanitis\w* (?:a found secret )?touch(?:es)? only disposable material outside the hashed candidate tree"),
    ("redactions recorded", r"redactions recorded"),
    ("secret in a tracked file found before the baseline waits for the operator's removal",
     r"secret in any tracked file of that tree, found before the baseline, waits for the operator to remove it"),
    ("secret at or after step 4 stops with a report or rebuilds from step 4, derived artifacts invalidated",
     r"secret found at or after step 4[^.]{0,60}stops the run with a report[^.]{0,60}rebuilds from step 4[^.]{0,60}every derived artifact invalidated"),
    ("secret in the candidate is a candidate finding, never dispatched for remediation",
     r"secret in the candidate is also a candidate finding and is never dispatched for remediation"),
])
# draft 8 (5.3), each rule as key terms in one sentence
RULES = [
    ("operator may answer not a secret with pattern, path and reason, recorded, run continues",
     [r"not a secret", r"pattern, path and reason", r"recorded in the report", r"continues"]),
    ("pre-baseline removal committed before step 4",
     [r"pre-baseline removal", r"committed", r"before step 4"]),
    ("specification committed before step 4", [r"specification is committed before step 4"]),
    ("other authorised untracked files listed and excluded from the step 10 delta and tree comparisons",
     [r"authorised untracked files", r"listed", r"excluded", r"step 10", r"delta", r"tree"]),
]
problems += [label for (label, rxs) in RULES if not sentence_with(raw, rxs)]
problems = ["missing: %s" % p for p in problems]
# draft 6's sanitisation scope and in-scope stop are a second rule for one thing under draft 7
for rx in (r"only files outside the candidate's paths", r"secret in a file in scope stops the run until"):
    if re.search(rx, f, re.I):
        problems.append("draft 6 secret rule still present: '%s'" % rx)
verdict(problems, "questions beyond the gate follow draft 8 5.3")
