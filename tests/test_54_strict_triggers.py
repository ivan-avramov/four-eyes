#!/usr/bin/env python3
# class: exercises new behaviour
# attacks: 5.4 and A5. four-eyes/SKILL.md makes strict mandatory for security, authentication, permissions, secrets,
#   a data boundary and architecture, defines architecture with A5's classes (new component, interface contract,
#   responsibilities, dependency relationships, data model, consistency or execution semantics, deployment or
#   isolation), and lets the operator ask for strict on anything.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

f = flat(read(FE_SKILL))
problems = missing(f, [
    ("strict mandatory", r"strict is mandatory|strict[^.]{0,20}(?:mandatory|required)"),
    ("security", r"strict[^.]{0,160}security"),
    ("authentication", r"strict[^.]{0,200}authentication"),
    ("permissions", r"strict[^.]{0,220}permissions"),
    ("secrets", r"strict[^.]{0,240}secrets"),
    ("data boundary", r"strict[^.]{0,260}data boundary"),
    ("architecture", r"strict[^.]{0,300}architecture"),
    ("A5: new component", r"new component"),
    ("A5: interface contract", r"interface[^.]{0,60}contract"),
    ("A5: responsibilities", r"responsibilit"),
    ("A5: dependency relationships", r"dependency relationships"),
    ("A5: data-model change", r"data-model change|data model change"),
    ("A5: consistency or execution semantics", r"consistency or execution semantics"),
    ("A5: deployment or isolation", r"deployment or isolation"),
    ("operator may ask for strict on anything", r"operator may ask for strict"),
])
verdict(["missing: %s" % p for p in problems], "strict triggers and A5 architecture classes present")
