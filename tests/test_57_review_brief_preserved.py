#!/usr/bin/env python3
# class: preserves an invariant
# attacks: 5.7 "briefs/review.md: unchanged except the version in the constraint block reference and the
#   replacement rule". Every line of the 0.4.0 reviewer brief except the title and the constraint-block reference
#   (lines 1 and 3, which the replacement rule may touch) is still present byte for byte and in order.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

BASELINE = [
    "## Phase A (receives the specification and the baseline only)",
    "Write adversarial tests against the specification's acceptance criteria and interfaces into `<test directory>`. Attack boundaries, failure paths, injection, path handling, permissions and the data boundary the specification names. No implementation is given; do not guess at one. For each test state its class: reproduces a failure the specification fixes, preserves an invariant that must hold before and after, or exercises new behaviour. Run them on the baseline and report the outcomes truthfully; no outcome is \"expected\".",
    "## Phase B (same session; receives the candidate and the worker's report)",
    "Apply the candidate in your isolated copy. Run the phase A tests, then the full suite, under the isolation the brief states. Then review the candidate for security (secrets, injection, paths, permissions, data boundary) and quality (correctness, clarity, dead code, unhandled errors) against the specification. Do not fix; report.",
    "## Report",
    "1. Phase A tests: names, class, what each attacks, baseline outcome, candidate outcome.",
    "2. Full suite result, verbatim summary.",
    "3. Security findings, severity-ordered, with file:line.",
    "4. Quality findings, with file:line.",
    "5. Specification deviations.",
    "6. Verdict: merge, fix-then-merge (list every required fix), or reject (why).",
]
lines = read(FE_REVIEW).splitlines()
problems = []
pos = 0
for b in BASELINE:
    try:
        pos = lines.index(b, pos) + 1
    except ValueError:
        problems.append("changed, missing or reordered: '%s'" % b[:50])
verdict(problems, "every preserved 0.4.0 reviewer brief line present in order")
