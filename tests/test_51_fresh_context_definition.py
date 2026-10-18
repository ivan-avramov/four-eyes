#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: 5.1 fresh context (amended to draft 5). four-eyes/SKILL.md defines fresh context operationally (new
#   session with its own id, no resume or fork flag, no transcript, summary or memory inherited from another role's
#   session, memory disabled), evidences it per execution (session id, recorded command, working directory,
#   instruction files present, recorded rather than required absent, the briefed material including the isolated
#   copy and the read-only checkout), limits the resume exemption to the reviewer's phase B resuming its own phase A,
#   and runs remediation in a new worker session. Draft 4's "scratch directory holding only the briefed material"
#   and "no project instruction files" are no longer required.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(FE_SKILL))
problems = missing(f, [
    ("own session id", r"(?:its )?own session id"),
    ("no resume or fork flag", r"without a resume or fork flag|no resume (?:or fork )?flag"),
    ("inherits no transcript, summary or memory", r"inheriting no transcript, summary or memory|inherits no transcript, summary or memory"),
    ("memory disabled", r"memory disabled|memory[^.]{0,20}is disabled"),
    ("evidenced per execution", r"evidenced per execution|evidence per execution"),
    ("recorded command", r"recorded command"),
    ("working directory", r"working directory"),
    ("instruction files present", r"instruction files present"),
    ("recorded, not required absent", r"recorded, not required absent"),
    ("briefed material includes the isolated copy and the checkout",
     r"briefed material includes the isolated copy[^.]{0,60}checkout"),
    ("exemption only for the reviewer's phase B", r"phase B resumes the reviewer's own phase A session and no other"),
    ("remediation in a new worker session", r"remediation runs in a new worker session"),
])
if re.search(r"same session resumed", f, re.I):
    problems.append("worker remediation may still resume the same session")
verdict(["missing: %s" % p if not p.startswith("worker") else p for p in problems],
        "fresh context defined and evidenced per draft 5 5.1")
