#!/usr/bin/env python3
"""Additive repair of the historical v15.787 Fermi electric Riemann reproducer.

External Audit Round 557/v15.789 reported a reproducible ShapeError:
historical gi0 has 5 diagonal entries against a 4x4 metric. Preserve the
original bytes and execute an in-memory exact one-token-count correction.
No physics or mathematical expression changes beyond inverse metric shape.
"""
from pathlib import Path
src=Path(__file__).with_name("k4_full_fermi_riemann_v15_787.py")
old="gi0=s.diag(-1,a**-2,a**-2,a**-2,a**-2)"
new="gi0=s.diag(-1,a**-2,a**-2,a**-2)"
raw=src.read_text()
assert raw.count(old)==1, "Refuse unexpected historical source!"
patched=raw.replace(old,new)
assert patched.count(new)==1
exec(compile(patched, str(src)+"[shape-only repair]", "exec"), {"__name__":"__main__","__file__":str(src)})
print("PASS: v15.787 additive inverse-metric dimension repair; original preserved")
