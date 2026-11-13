#!/usr/bin/env python3
"""v15.870 additive audit repair of v15.864/865, no historical edits.

Audit Round 566 found original v15.864 two executable defects:
1. Bare SymPy matrix == compares form rather than algebra.
2. v=s.Function('v')(tau) makes v(tau) throw TypeError.
v15.865 corrected only #1. Correct both on the ORIGINAL content
in memory and run the complete on-shell two-field/coasting K4
tensor-only optical calculation. No Minkowski L=5 *executable*
benchmark exists in original, contrary to v15.865 ledger prose.
"""
from pathlib import Path
src=Path(__file__).with_name("k4_conserved_force_agent_tensor_optical_v15_864.py")
raw=src.read_text()
changes=[
 ("assert S_TT.subs(az,0)==Q*s.diag(1,-1,0)",
  "assert (S_TT.subs(az,0)-Q*s.diag(1,-1,0)).applyfunc(s.simplify)==s.zeros(3)"),
 ("v=s.Function('v')(tau)","v=s.Function('v')")
]
for old,new in changes:
    assert raw.count(old)==1, f"Unexpected original code: {old}"
    raw=raw.replace(old,new)
assert "Minkowski tensor oscillator benchmark" not in raw
exec(compile(raw,str(src)+"[v15.870 exact two-repair replay]","exec"),
     {"__name__":"__main__","__file__":str(src)})
print("PASS two independent additive corrections, no original bytes changed")
print("CORRECTION no implemented Minkowski L=5 oscillator benchmark is claimed")
