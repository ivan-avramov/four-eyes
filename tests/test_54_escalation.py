#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: 5.4 escalation. four-eyes/SKILL.md says an unwaived hit in a light run switches to strict with a
#   recorded second question; a build hit on code the specification does not cover is also an out-of-scope
#   finding; a new verification cycle of up to three rounds runs, cycles reported separately; if the cycle changes
#   the specification, every derived artifact is invalid and the run returns to the gate, dispatches the worker
#   afresh and replaces the reviewer `replaced (escalation)`; if it changes nothing, the run proceeds under strict.
#   Amended to draft 7 (5.3): an escalation cycle after the gate runs under `gate: caller` with the escalation answer.
#   Rewritten for the rule, not the phrase: "cycles are reported separately" may be the imperative "report cycles
#   separately"; the phrase match required the passive.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(FE_SKILL))
problems = missing(f, [
    ("unwaived hit switches to strict", r"unwaived hit[^.]{0,80}switch[^.]{0,30}strict"),
    ("second question recorded", r"second question"),
    ("out-of-scope finding on uncovered code", r"out of scope|out-of-scope"),
    ("new verification cycle of up to three rounds", r"new verification cycle[^.]{0,40}up to three rounds"),
    ("cycles reported separately", r"cycles (?:are )?reported separately|report (?:each |the )?cycles? separately"),
    ("derived artifacts invalid", r"every artifact derived from the superseded|derived[^.]{0,40}invalid"),
    ("returns to the gate", r"returns? to the gate"),
    ("worker dispatched afresh", r"worker afresh|dispatch(?:es)? the worker (?:afresh|again)"),
    ("reviewer replaced (escalation)", r"replaced \((?:lost session \| )?escalation\)"),
    ("unchanged spec proceeds under strict", r"changes nothing[^.]{0,60}strict"),
    # draft 7
    ("escalation cycle after the gate under gate: caller with the escalation answer",
     r"escalation cycle after the gate runs under gate: caller with the escalation answer"),
])
verdict(["missing: %s" % p for p in problems], "escalation follows 5.4")
