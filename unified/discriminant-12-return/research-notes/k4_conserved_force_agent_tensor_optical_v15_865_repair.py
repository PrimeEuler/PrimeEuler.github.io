#!/usr/bin/env python3
"""v15.865: immutable v15.864 SymPy matrix assertion repair and replay.

Sandbox and Gravity independently used v15.864: historical source stays
intact. Its one matrix assertion accidentally uses SymPy *structural*
matrix equality, not algebraic equality; equivalent forms (c²-1) vs
-(1-c²) compare False. Repair the one exact assertion IN MEMORY and
execute every original symbolic and numerical test. Audit pending.
"""
from pathlib import Path
source=Path(__file__).with_name("k4_conserved_force_agent_tensor_optical_v15_864.py")
raw=source.read_text()
old="assert S_TT.subs(az,0)==Q*s.diag(1,-1,0)"
new="assert (S_TT.subs(az,0)-Q*s.diag(1,-1,0)).applyfunc(s.simplify)==s.zeros(3)"
assert raw.count(old)==1,"Unexpected original script; refuse repair"
patched=raw.replace(old,new)
assert patched.count(new)==1
exec(compile(patched,str(source)+"[v15.865 correction]","exec"),
     {"__name__":"__main__","__file__":str(source)})
print("PASS v15.865 additive symbolic equivalence repair")
