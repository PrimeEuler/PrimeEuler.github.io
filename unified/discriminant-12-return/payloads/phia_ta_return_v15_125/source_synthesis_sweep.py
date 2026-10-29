#!/usr/bin/env python3
"""Replayable evidence for the v15.115 Phi_a return's absence claim.

Searches the Suzuki finite-a source base named by the handoff
(v13.661, v13.662, v13.785) and the surrounding Suzuki digest range
(v13.640-v13.799 in the local ledger cache) for any prescription of a
sequence-indexed coefficient synthesis: a family of source functions
indexed by an external mode label, a synthesis map from sequence
space, or basis functions attached to the frozen K_full data.

Prints every hit for manual classification. The absence claim in the
return rests on reading the three source entries in full; this sweep
is the reproducible guard against a prescription hiding elsewhere in
the digest.
"""
import glob
import re
import os

CACHE = os.path.expanduser("~/workspace/d12/cache/ledger")
BASE = ["v13.661", "v13.662", "v13.785"]
PATTERNS = {
    "synthesis map / Phi_a": re.compile(r"synthesis|Phi_a|\\Phi_a|coefficient map", re.I),
    "sequence-indexed source family": re.compile(
        r"\\phi_\{?m\}?|\\phi_\{?n\}?[_a]|phi_m|test functions? \$?\\phi", re.I),
    "frozen-data reference": re.compile(r"z_m|p_m|spike|frozen", re.I),
}

def ver_of(path):
    m = re.search(r"_v(1[0-9]\.[0-9]+)_", path)
    return m.group(1) if m else "?"

base_files = []
for v in BASE:
    base_files += glob.glob(os.path.join(CACHE, f"*{v}_*.md"))
digest = sorted(
    p for p in glob.glob(os.path.join(CACHE, "Cone_Derivation_Ledger_v13.*.md"))
    if 13.640 <= float(ver_of(p)) <= 13.799
)

for label, files in (("SOURCE BASE (named by v15.115)", base_files),
                     ("SUZUKI DIGEST RANGE v13.640-v13.799", digest)):
    print(f"## {label}: {len(files)} files")
    for name, pat in PATTERNS.items():
        hits = []
        for p in files:
            text = open(p, encoding="utf-8", errors="replace").read()
            for i, line in enumerate(text.splitlines(), 1):
                if pat.search(line):
                    hits.append(f"  v{ver_of(p)}:{i}: {line.strip()[:110]}")
        print(f"-- pattern '{name}': {len(hits)} hits")
        for h in hits[:14]:
            print(h)
        if len(hits) > 14:
            print(f"  ... and {len(hits) - 14} more")
    print()
print("Classification (manual, from full reads): every hit in the source base")
print("concerns the deficiency pair, parity sources, or the abstract spectral")
print("resolution of T_a. No hit prescribes a sequence-indexed synthesis or")
print("any map from the frozen K_full index data to source functions.")
