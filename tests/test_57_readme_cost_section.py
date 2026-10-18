#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.7 README "a section on cost and its units". README.md has a section whose heading names cost, defining
#   the execution (one runtime invocation), the panel invocation and the verification cycle, and saying that nothing
#   is estimated and money is never summed across billing bases. Amended to draft 6: the execution unit includes each
#   re-run of phase B. Amended to draft 8 (5.5): coverage is written `over n of e`; `over n of m` (m is the
#   distinct-model count) must be gone.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

body = section(read(README), r"\bcost")
if body is None:
    fail("README has no section whose heading names cost")
f = flat(body)
problems = missing(f, [
    ("execution unit", r"execution[^.]{0,40}(?:one )?runtime invocation"),
    ("panel invocation unit", r"panel invocation"),
    # draft 6 (5.5 units): each re-run of phase B is an execution
    ("phase B re-runs counted as executions", r"re-run of phase B|phase B re-runs?"),
    ("verification cycle unit", r"verification cycle"),
    ("nothing estimated", r"nothing is estimated|never estimated|no estimat"),
    ("money not summed across bases", r"never summed|not summed"),
    ("coverage written over n of e", r"over n of e\b"),
])
problems = ["missing: %s" % p for p in problems]
if re.search(r"over n of m\b", f):
    problems.append("draft 7 coverage symbol 'over n of m' still present")
verdict(problems, "README cost section defines the units")
