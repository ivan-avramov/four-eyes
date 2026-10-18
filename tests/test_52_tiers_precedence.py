#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: 5.2. four-eyes/SKILL.md has tiers `top` and `capable` declared per member with a date; tier basis when
#   undeclared is the host's model list, then model knowledge with cutoff; designer and verifier from top, worker,
#   reviewer and candidate panel from capable; precedence reaches the preferred level first, then the cheapest tier;
#   the verifier always includes a top member; an all-capable verifier needs the operator's answer. Amended to
#   draft 5: a fresh session of the designer's model counts as top only when the designer's model is top.
#   Rewritten for the rule, not the phrase: 5.2's "Designer and verifier draw from top; worker, reviewer and the
#   candidate panel from capable" may be stated as one sentence or as one bullet per role (the skill's Roles and
#   tiers list), each role's bullet naming its tier; "the verifier panel always includes at least one top member"
#   may be worded "at least one top member always". The phrase match required the spec's sentence shape.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

raw = read(FE_SKILL)
f = prose(raw)
problems = missing(f, [
    ("top and capable tiers", r"\btop\b[^.]{0,20}\bcapable\b"),
    ("declared per member with a date", r"declared[^.]{0,60}per member[^.]{0,40}date|per member[^.]{0,40}dat"),
    ("host's model list then model knowledge", r"host's (?:reported )?model list[^.]{0,80}model knowledge"),
    ("preferred level first, then cheapest tier", r"preferred level first[^.]{0,60}cheapest tier"),
    ("all-capable verifier only by operator's answer", r"all-?`?capable`?[^.]{0,40}only by the operator's answer"),
    # draft 5: a fresh session of the designer's model counts as top only when the designer's model is top
    ("designer-model verifier top only when designer top", r"designer's model[^.]{0,80}only when the designer's model is `?top|designer's model[^.]{0,60}when the designer's model is `?top"),
])


def role_line(role):
    """The Roles and tiers bullet for a role, flattened without emphasis, or ''."""
    body = section(raw, r"^Roles and tiers$") or ""
    for line in body.splitlines():
        if re.match(r"^\s*-\s*(?:\*\*)?" + role + r"(?:\*\*)?\s*:", line, re.I):
            return prose(line)
    return ""


TOP_ROLE = r"\bdrawn from `?top`?|\ba `?top`? model\b|\bfrom `?top`?"
CAP_ROLE = r"\bdrawn from `?capable`?|\ba `?capable`? model\b|\bfrom `?capable`?"
if not (re.search(r"designer and verifier[^.]{0,30}\btop\b", f, re.I)
        or (re.search(TOP_ROLE, role_line("Designer"), re.I) and re.search(TOP_ROLE, role_line("Verifier"), re.I))):
    problems.append("designer and verifier from top")
if not (re.search(r"worker, reviewer and (?:the )?(?:candidate )?panel[^.]{0,30}\bcapable\b", f, re.I)
        or all(re.search(CAP_ROLE, role_line(r), re.I) for r in ("Worker", "Reviewer", "Candidate panel"))):
    problems.append("worker, reviewer, panel from capable")
if not re.search(r"verifier panel always includes[^.]{0,30}\btop\b|at least one `?top`? member always|always[^.]{0,30}at least one `?top`? member", f, re.I):
    problems.append("verifier always includes a top member")
verdict(["missing: %s" % p for p in problems], "tiers and precedence follow 5.2")
