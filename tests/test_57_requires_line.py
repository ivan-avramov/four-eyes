#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.7 "`requires: review-panel 0.3.0 or later`". The frontmatter of four-eyes/SKILL.md has exactly one
#   `requires:` line, beginning `requires: review-panel 0.3.0 or later` (a trailing source URL in parentheses is
#   allowed), and README.md, where it states a review-panel version, states 0.3.0.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

fm = frontmatter(read(FE_SKILL))
if fm is None:
    fail("SKILL.md has no frontmatter")
req = [l.strip() for l in fm if re.match(r"\s*requires\s*:", l)]
problems = []
if len(req) != 1:
    problems.append("%d requires lines" % len(req))
elif not re.fullmatch(r"requires: review-panel 0\.3\.0 or later(?: \(https://[^\s)]+\))?", req[0]):
    problems.append("requires line is '%s'" % req[0])
for m in re.finditer(r"review-panel (\d+\.\d+\.\d+)", read(README)):
    if m.group(1) != "0.3.0":
        problems.append("README states review-panel %s" % m.group(1))
verdict(problems, "requires review-panel 0.3.0 or later")
