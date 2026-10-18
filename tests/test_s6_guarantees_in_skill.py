#!/usr/bin/env python3
# class: preserves an invariant
# attacks: S6 (unchanged from 0.4.0). four-eyes/SKILL.md still carries every S6 guarantee: isolation of write-capable
#   roles in a fresh copy (never a worktree), disclosure scanning before anything leaves the host, evidence of what
#   ran per role, the approval gate before dispatch, the reviewer's tests frozen before the candidate is revealed,
#   commit of the candidate's files only, and push only on the operator's explicit word.
#   Rewritten for the rule, not the phrase: "evidence of what ran per role" is carried when the skill records
#   evidence per execution and every execution record names its role (0.5.0 moved the record from per role to per
#   execution, 5.5); the phrase match required the words "per role". Both parts must be present.
#   Amended to draft 8 (5.3, isolation non-goal): write-capable copies are built from the scanned tracked files with a
#   fresh repository initialised in the copy, never from a clone; a read-only sandbox that can still read the
#   operator repository is a residual exposure stated in the report.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

raw = read(FE_SKILL)
f = flat(raw)
problems = missing(f, [
    ("isolation of write-capable roles in a fresh copy", r"write-capable roles[^.]{0,80}fresh copy"),
    ("never a worktree", r"never a worktree"),
    ("disclosure scanning before anything leaves the host", r"before anything leaves the host"),
    ("scan the copy and the brief", r"scan the copy and the brief"),
    ("approval before dispatch", r"approv[^.]{0,80}before[^.]{0,30}dispatch|nothing write-capable is dispatched before"),
    ("tests frozen before the candidate is revealed", r"freeze[^.]{0,60}before the candidate is revealed|frozen before the candidate is revealed"),
    ("commit only the candidate's files", r"commit only the candidate's files|commit of the candidate's files only"),
    ("push only on the operator's explicit word", r"push only on the operator's explicit word"),
])
per_role = re.search(r"record per role|per role[^.]{0,40}evidence|evidence[^.]{0,40}per role", f, re.I)
per_execution = (re.search(r"record per execution: runtime[^.]{0,80}observed model[^.]{0,80}session id", f, re.I)
                 and re.search(r"each execution has one record: id, role\b", f, re.I))
if not (per_role or per_execution):
    problems.append("evidence of what ran per role")
# draft 8: no history leaves the host through a write-capable copy
if not sentence_with(raw, [r"write-capable roles", r"fresh repository initialised in the copy", r"never from a clone"]):
    problems.append("write-capable copy built with a fresh repository, never from a clone")
if not sentence_with(raw, [r"read-only sandbox", r"operator repository", r"residual exposure", r"report"]):
    problems.append("residual read exposure of the operator repository stated in the report")
verdict(["S6 guarantee missing: %s" % p for p in problems], "every S6 guarantee present")
