#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.7 "Version 0.5.0". The frontmatter of four-eyes/SKILL.md has exactly one `version:` line and it is
#   0.5.0; no `[four-eyes 0.4.0]` tag remains anywhere in SKILL.md or the briefs.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

skill = read(FE_SKILL)
fm = frontmatter(skill)
if fm is None:
    fail("SKILL.md has no frontmatter")
versions = [l.strip() for l in fm if re.match(r"\s*version\s*:", l)]
problems = []
if versions != ["version: 0.5.0"]:
    problems.append("frontmatter version lines: %s" % (versions or "none"))
for rel in (FE_SKILL, FE_WORKER, FE_REVIEW, FE_VERIFY):
    if "four-eyes 0.4.0" in read(rel):
        problems.append("'four-eyes 0.4.0' still in %s" % rel)
verdict(problems, "version 0.5.0, no 0.4.0 tag left")
