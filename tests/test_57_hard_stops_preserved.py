#!/usr/bin/env python3
# class: preserves an invariant
# attacks: 5.7 "the unchanged hard stops". The section "When a role cannot be filled" of four-eyes/SKILL.md still
#   names the six 0.4.0 hard stops (missing CLI, failed authentication, usage limit, unresolvable selector,
#   unexpected substitution, unenforceable isolation) and still says the run stops on them; the one-question
#   gate of 5.3 must not turn them into degradations the operator can accept.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

body = section(read(FE_SKILL), r"^When a role cannot be filled")
if body is None:
    fail("no section 'When a role cannot be filled'")
f = flat(body)
problems = missing(f, [
    ("missing CLI", r"missing CLI|CLI (?:is )?(?:missing|not installed|absent)"),
    ("failed authentication", r"fail(?:ed|ing)? authentication|authentication (?:fail|error)"),
    ("usage limit", r"usage limit"),
    ("unresolvable selector", r"unresolvable selector|selector (?:that )?(?:does not|cannot|can't) resolve"),
    ("unexpected substitution", r"unexpected (?:model )?substitution"),
    ("unenforceable isolation", r"unenforceable isolation|isolation (?:that )?(?:cannot|can't) be enforced"),
    ("the run stops", r"\bstop"),
])
verdict(["hard stop missing: %s" % p for p in problems], "six 0.4.0 hard stops named with a stop")
