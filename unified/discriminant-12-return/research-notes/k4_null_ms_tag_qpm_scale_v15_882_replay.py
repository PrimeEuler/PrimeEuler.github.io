#!/usr/bin/env python3
"""v15.882 additive replay of v15.881 null tag scale check.

v15.881 has an assertion comparing the dimensionless identity
(beat/period)/(c/(n_gamma-n_g)) to 0 instead of 1. The correct
mathematical value is 1. Repair the exact one line in memory and
execute every check without rewriting the original.
"""
from pathlib import Path
src=Path(__file__).with_name("k4_null_ms_tag_qpm_scale_v15_881.py")
raw=src.read_text()
old="assert s.simplify((beat/period)/(c/(ngam-ngrav)))==0"
new="assert s.simplify((beat/period)/(c/(ngam-ngrav)))==1"
assert raw.count(old)==1
raw=raw.replace(old,new)
exec(compile(raw,str(src)+"[v15.882 repair]","exec"),
     {"__name__":"__main__","__file__":str(src)})
print("PASS additive identity-value correction, original unchanged")
