#!/usr/bin/env python3
# class: reproduces a failure the specification fixes
# attacks: S1 drift into README.md. The README must not keep 0.4.0's "cross-vendor requirement" or "at least one
#   member from a different vendor" as requirements; vendor difference is only the preferred L3.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import *

bad = vendor_requirement_sentences(read(README))
verdict(["requires vendor difference: '%s'" % s for s in bad], "no sentence requires a differing vendor")
