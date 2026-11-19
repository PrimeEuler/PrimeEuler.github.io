#!/usr/bin/env python3
"""Additive v15.1221 execution repair for Audit Round 609's v15.1198 defect.

Only patch the reported *syntactic* bare SymPy equality assertion in
memory; do not overwrite the original historical reproducer.
Run in a real repo checkout. Refuse if source differs.
"""
from pathlib import Path
source=Path(__file__).resolve().with_name(
  "k4_null_maxwell_full_riemann_arm_proxy_v15_1198_corrected.py"
)
old="assert s.limit(geom,kr,0)==R"
new="assert s.simplify(s.limit(geom,kr,0)-R)==0"
data=source.read_text(encoding="utf-8")
assert data.count(old)==1, "original script changed; do not patch silently"
corrected=data.replace(old,new)
scope={"__name__":"__main__","__file__":str(source)}
exec(compile(corrected,str(source)+" [v15.1221 in-memory repair]","exec"),scope)
print("PASS archival v15.1198 source with exact one-line in-memory equality repair")
