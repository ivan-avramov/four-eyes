#!/usr/bin/env python3
# class: preserves an invariant
# attacks: skill loading. four-eyes/SKILL.md keeps a frontmatter block with `name: four-eyes`, a non-empty one-line
#   `description:` that still tells dispatched workers, reviewers and panel members to skip the skill, and the
#   unchanged source URL; the body still opens with the skip instruction.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

skill = read(FE_SKILL)
fm = frontmatter(skill)
if fm is None:
    fail("no frontmatter")
lines = [l.strip() for l in fm]
problems = []
if "name: four-eyes" not in lines:
    problems.append("name is not four-eyes")
desc = [l for l in fm if l.startswith("description:")]
if len(desc) != 1 or len(desc[0]) < 40:
    problems.append("description missing or empty")
elif not re.search(r"Skip it when you were dispatched as a worker, reviewer or review-panel member", desc[0]):
    problems.append("description lost the skip-when-dispatched clause")
if "source: https://github.com/ivan-avramov/four-eyes" not in lines:
    problems.append("source changed")
if not re.search(r"Skip this skill if you were dispatched as a worker, a reviewer or a review-panel member", skill):
    problems.append("body lost the skip instruction")
verdict(problems, "frontmatter and skip instruction intact")
