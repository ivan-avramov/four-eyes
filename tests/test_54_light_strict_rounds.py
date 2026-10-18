#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: 5.4 modes. four-eyes/SKILL.md makes light the default, passes `rounds = 1` to review-panel converge in
#   light mode and `rounds = 3` in strict, lists specification changes after the dispatch as not re-reviewed at
#   the gate, and runs the candidate panel as one invocation in both modes.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(FE_SKILL))
problems = missing(f, [
    ("light is the default", r"light[^.]{0,20}\(?default\)?|default[^.]{0,20}\blight\b"),
    ("light passes rounds = 1", r"light[^.]{0,120}rounds ?= ?1|rounds ?= ?1[^.]{0,60}light"),
    ("strict passes rounds = 3", r"strict[^.]{0,120}rounds ?= ?3|rounds ?= ?3[^.]{0,60}strict"),
    ("not re-reviewed at the gate", r"not re-reviewed"),
    ("candidate panel is one invocation", r"one invocation"),
])
verdict(["missing: %s" % p for p in problems], "light and strict round counts follow 5.4")
