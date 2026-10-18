#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.1 exemption and 5.7. In four-eyes/SKILL.md the reviewer's two deliveries come from one session: phase B
#   resumes the phase A session and no other, and its id is recorded and checked equal to the phase A id. 0.4.0's
#   "record `resumed` or `new session`" (a new phase B session reusing tests written by another session) must be
#   gone. Amended to draft 7 (5.1): an unequal resumed id means `replaced (lost session)` with a new candidate-blind
#   phase A, and each runtime's resume-id behaviour is probed once per machine (sandbox probes) before the exemption
#   is relied on, so sandbox/probes.md carries that probe. Amended to draft 8 (5.1): the replacement happens at most
#   once per run, a second loss going to the operator; where a runtime documents id rotation on resume, the recorded
#   chain of ids stands in for equality; four-eyes states that the reviewer's sessions start without an ephemeral
#   flag (fourth panel P1, F1).
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(FE_SKILL))
problems = missing(f, [
    ("two deliveries from one session", r"two deliveries[^.]{0,40}(?:one|the same|a single) session|(?:one|the same|a single) session[^.]{0,40}two deliveries"),
    ("phase B resumes the phase A session", r"phase B[^.]{0,60}resum[^.]{0,60}phase A"),
    ("resumed id checked equal to phase A id", r"(?:id|session id)[^.]{0,60}(?:checked |verified )?equal[^.]{0,30}phase A"),
    # draft 7
    ("unequal id is replaced (lost session) with a new candidate-blind phase A",
     r"unequal (?:resumed )?id[^.]{0,30}replaced \(lost session\)[^.]{0,30}new candidate-blind phase A"),
    ("resume-id behaviour probed once per machine before relied on",
     r"resume-id behaviour[^.]{0,40}probed once per machine[^.]{0,40}before the exemption is relied on"),
])
RULES = [
    ("replacement at most once per run, a second loss to the operator",
     [r"at most once per run", r"second loss", r"operator"]),
    ("recorded chain of ids stands in for equality where a runtime documents rotation",
     [r"id rotation", r"recorded chain of ids", r"stands in for equality"]),
    ("reviewer sessions started without an ephemeral flag",
     [r"phase A", r"without (?:any |an )?ephemeral flag"]),
]
problems += [label for (label, rxs) in RULES if not sentence_with(read(FE_SKILL), rxs)]
probes = flat(read("sandbox/probes.md"))
if not re.search(r"resume[^.]{0,80}(?:session )?id", probes, re.I):
    problems.append("sandbox/probes.md carries no resume-id probe")
if re.search(r"record resumed or new session", f, re.I):
    problems.append("0.4.0 'record resumed or new session' still allowed for phase B")
verdict(problems, "one reviewer session, phase B resume checked by id")
