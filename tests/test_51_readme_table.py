#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: 5.7 README and R7. README.md has a section "What a degraded run does not check" carrying the 5.1 level
#   table with every header and row cell byte-identical to the specification; a row with the same level but
#   different wording is reported as drift.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

body = section(read(README), r"^What a degraded run does not check$")
if body is None:
    fail("README has no section 'What a degraded run does not check'")
verdict(check_table(body, TABLE_HEADER, TABLE_ROWS, "README level table"),
        "README section carries the 5.1 table byte for byte")
