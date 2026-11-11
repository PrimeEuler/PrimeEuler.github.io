#!/usr/bin/env python3
"""v15.733 additive version-collision repair for gravity v15.732.
Concurrent Suzuki lane occupied v15.732 first; preserve both historical
files, and rerun gravity's original compact canonical Weyl reproducer.
"""
from pathlib import Path
import runpy
source=Path(__file__).with_name("k4_compact_canonical_weyl_convergence_v15_732.py")
assert source.is_file()
runpy.run_path(str(source),run_name="__main__")
print("PASS gravity v15.733: independently reran preserved original v15.732 source")
