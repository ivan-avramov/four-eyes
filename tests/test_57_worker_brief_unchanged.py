#!/usr/bin/env python3
# class: preserves an invariant
# attacks: 5.7 "briefs/worker.md ... unchanged except the version in the constraint block reference". Every line of
#   the 0.4.0 worker brief other than its constraint-block reference (line 3) is still present, byte for byte and
#   in the same order; lines may be added only around them.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

BASELINE = [
    "# Worker brief (template)",
    "## Specification",
    "<path inside the isolated copy, or the text; acceptance criteria and interfaces included>",
    "## Files in scope",
    "<list; the reviewer's test directory is named here as read-only to you>",
    "## Environment",
    "<the isolated copy's path; the test command; whether network is permitted; what is stubbed>",
    "## Acceptance",
    "<which tests must pass; what \"done\" means>",
    "## Report",
    "Every file added, changed or deleted, one line each; the exact commands run and their results; anything in the specification you could not satisfy and why. Facts only. Do not commit.",
]
lines = read(FE_WORKER).splitlines()
problems = []
pos = 0
for b in BASELINE:
    try:
        pos = lines.index(b, pos) + 1
    except ValueError:
        problems.append("changed, missing or reordered: '%s'" % b[:50])
verdict(problems, "every 0.4.0 worker brief line preserved in order")
