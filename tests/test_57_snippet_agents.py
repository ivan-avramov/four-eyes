#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.7 snippets. codex/AGENTS.snippet.md adds "strict mode for security and architecture, light otherwise"
#   (case-insensitive, whitespace runs collapsed) and keeps its skip-when-dispatched sentence; it still does not name
#   a model or vendor as required.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

text = read(AGENTS_SNIPPET)
f = flat(text)
problems = []
if "strict mode for security and architecture, light otherwise" not in f.lower():
    problems.append("missing 'strict mode for security and architecture, light otherwise'")
if not re.search(r"Skip this section if you were dispatched as a worker, a reviewer or a review-panel member", f):
    problems.append("skip-when-dispatched sentence lost")
hits = q1_hits(text)
if hits:
    problems.append("names '%s'" % hits[0][1])
verdict(problems, "AGENTS snippet names strict and light modes")
