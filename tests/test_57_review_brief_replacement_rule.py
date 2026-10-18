#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.7 "briefs/review.md: ... the replacement rule for the reviewer session". The reviewer brief states that
#   if the session is replaced, a new session performs a new candidate-blind phase A with newly frozen tests
#   before any candidate is revealed; it must not tell a new session to continue at phase B.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(FE_REVIEW))
problems = []
if not re.search(r"replac", f, re.I):
    problems.append("no replacement rule")
elif not re.search(r"replac[^.]{0,200}(?:new|fresh)[^.]{0,40}phase A", f, re.I):
    problems.append("replacement does not require a new phase A")
if not re.search(r"candidate-blind|before (?:any|the) candidate is revealed", f, re.I):
    problems.append("new phase A not stated candidate-blind")
if not re.search(r"newly frozen|frozen anew|re-?frozen", f, re.I):
    problems.append("new phase A tests not stated newly frozen")
verdict(problems, "reviewer brief carries the replacement rule")
