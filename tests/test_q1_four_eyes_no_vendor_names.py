#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: Q1 and S1. four-eyes/SKILL.md names no vendor or model outside example and report sections
#   (headings matching example|report|roles block|cost, and fenced blocks). Runtime names (Claude CLI,
#   Claude Code, `claude ...`, Codex, cursor-agent) and file names (CLAUDE.md, AGENTS.md) are runtimes, not
#   vendors or models, and are not flagged.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

hits = q1_hits(read(FE_SKILL))
verdict(["'%s' in section '%s'" % (n, h) for (h, n) in hits],
        "no vendor or model name outside example and report sections")
