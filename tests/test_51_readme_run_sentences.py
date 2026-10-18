#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.7 README and R7. README.md carries the run-level line and the two-model and one-model sentences of 5.1
#   byte for byte (whitespace runs collapsed, inline-code ticks ignored), in the section
#   "What a degraded run does not check".
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

body = section(read(README), r"^What a degraded run does not check$")
if body is None:
    fail("README has no section 'What a degraded run does not check'")
f = flat(body)
problems = ["missing or drifted: '%s'" % w[:60] for w in [RUN_LINE, TWO_MODEL, ONE_MODEL] if w not in f]
verdict(problems, "README carries the run-level line and both sentences byte for byte")
