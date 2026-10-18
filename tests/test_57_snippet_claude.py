#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.7 snippets. claude/CLAUDE.snippet.md adds "strict mode for security and architecture, light otherwise"
#   (case-insensitive, whitespace runs collapsed) and keeps its skip-when-dispatched clause.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(CLAUDE_SNIPPET))
problems = []
if "strict mode for security and architecture, light otherwise" not in f.lower():
    problems.append("missing 'strict mode for security and architecture, light otherwise'")
if not re.search(r"skip it when you were dispatched as a worker, reviewer or review-panel member", f, re.I):
    problems.append("skip-when-dispatched clause lost")
verdict(problems, "Claude snippet names strict and light modes")
