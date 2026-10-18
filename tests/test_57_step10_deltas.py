#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.7 step 10 and R8. four-eyes/SKILL.md's Accept step records the baseline, the authorised candidate delta
#   (paths and content hashes) and the actual commit delta, requires the two deltas equal, keeps tree equality with
#   the final candidate hash bound to the last panel verdict as a separate check, and writes `push: none` when
#   nothing was pushed.
#   Rewritten for the rule, not the phrase: "requires the two deltas to be equal" may read "the two deltas must be
#   equal"; the phrase match did not allow "must". Amended to draft 8 (5.3): the listed authorised untracked files
#   are excluded from the step 10 delta and tree comparisons, stated in the Accept step.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(FE_SKILL))
problems = missing(f, [
    ("authorised candidate delta", r"authori[sz]ed candidate delta"),
    ("paths and content hashes", r"paths and content hashes"),
    ("actual commit delta", r"commit delta"),
    ("the two deltas equal", r"(?:two )?deltas (?:must |to )?(?:be )?equal|requires[^.]{0,40}equal"),
    ("tree equality bound to the last panel verdict", r"last panel verdict"),
    ("push: none", r"push: none"),
])
accept = section(read(FE_SKILL), r"^Procedure$") or ""
step10 = re.search(r"^10\. \*\*Accept\.\*\*.*$", accept, re.M)
if not (step10 and sentence_with(step10.group(0), [r"authorised untracked files", r"excluded", r"delta", r"tree"])):
    problems.append("Accept step excludes the listed authorised untracked files from the deltas and tree comparisons")
verdict(["missing: %s" % p for p in problems], "step 10 delta checks present")
