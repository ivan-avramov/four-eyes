#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: 5.4 remediation (amended to draft 5). four-eyes/SKILL.md sends findings once to a new worker session; the fixed candidate goes through
#   phase B in full and the panel again in fresh sessions; a light-mode panel scoped to the remediation diff gets
#   the full candidate and the diff range with the limit recorded; each panel verdict is bound to the hash of the
#   candidate it read; strict re-runs the full panel; an unresolved blocker or major after one remediation, or a
#   second remediation round, goes to the operator.
#   Rewritten for the rule, not the phrase: "each panel verdict is bound to the hash" may be the imperative "bind
#   each panel verdict to the hash of the candidate it read"; the phrase match required the passive.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(FE_SKILL))
problems = missing(f, [
    ("remediation in a new worker session (draft 5)", r"(?:findings go|go) once to a new worker session|new worker session[^.]{0,60}findings"),
    ("phase B in full after remediation", r"phase B in full"),
    ("panel again in fresh sessions", r"panel again[^.]{0,30}fresh session"),
    ("scoped to the remediation diff with full candidate", r"remediation diff[^.]{0,80}full candidate|full candidate[^.]{0,80}remediation diff"),
    ("limit recorded", r"limit recorded"),
    ("verdict bound to candidate hash",
     r"verdict[^.]{0,30}bound to the hash|bind (?:each |the )?(?:panel )?verdict to the hash of the candidate"),
    ("strict re-runs the full panel", r"full panel"),
    ("unresolved blocker or major goes to the operator", r"unresolved blocker or major[^.]{0,60}operator"),
    ("second remediation round goes to the operator", r"second remediation round[^.]{0,30}operator"),
])
verdict(["missing: %s" % p for p in problems], "remediation follows 5.4")
