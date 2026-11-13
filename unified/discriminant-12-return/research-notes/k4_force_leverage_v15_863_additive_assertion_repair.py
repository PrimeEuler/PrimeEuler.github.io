#!/usr/bin/env python3
"""v15.863 additive repair to first committed v15.862 code reproducer.

v15.862 mistakenly used SymPy structural equality for two equivalent
fractions (-(beta+1)/(beta-1) and (beta+1)/(1-beta)); the false Python
boolean causes a reproducibility failure, not a mathematical failure.
Do not overwrite certified/historical v15.862 source. Patch only that
assertion IN MEMORY, and execute the original complete script.
"""
from pathlib import Path
src=Path(__file__).with_name("k4_force_leverage_nullstress_tt_selector_v15_862.py")
old="assert lever==(beta+1)/(1-beta)"
new="assert s.simplify(lever-(beta+1)/(1-beta))==0"
raw=src.read_text()
assert raw.count(old)==1,"Historical source assertion changed; refuse repair"
fixed=raw.replace(old,new)
assert fixed.count(new)==1
exec(compile(fixed,str(src)+" [v15.863 repair]","exec"),
     {"__name__":"__main__","__file__":str(src)})
print("PASS additive v15.863 assertion-normalization repair")
