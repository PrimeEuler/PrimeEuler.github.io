#!/usr/bin/env python3
"""Check the base certificate's P against the frozen joint producer payloads."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from suzuki_M8000_embedded_p4_ldd_capacity import embedded_protected_basis
from suzuki_M8000_M16000_capacity_ratio_source_sensitivity import embedded_P, modes_for


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--joint-root", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    rows = []
    for sector in ("even-v", "odd-v"):
        _, modes, oldp, _, _ = embedded_protected_basis(sector)
        newp = embedded_P(sector, modes_for(sector, 8000))
        if not np.array_equal(modes, modes_for(sector, 8000)) or not np.array_equal(oldp, newp):
            raise RuntimeError("base-certificate and normalized-producer geometry differ")
        if np.any(oldp[2000:] != 0):
            raise RuntimeError("protected plane not supported in frozen 4k base")
        phash = hashlib.sha256(np.asarray(oldp[:2000], dtype="<f8").tobytes()).hexdigest()
        for cutoff in (64000, 128000):
            raw = (args.joint_root/f"joint-{cutoff}-{sector}.json").read_bytes()
            row = json.loads(raw)["rows"][0]
            if row["frozen_base_P_sha256"] != phash:
                raise RuntimeError("frozen producer P differs from base-certificate P")
            if (row["cutoff"], row["sector"]) != (cutoff, sector):
                raise RuntimeError("wrong frozen row")
        rows.append({"sector": sector, "frozen_base_P_sha256": phash,
                     "base_helper_and_producer_arrays_component_identical": True,
                     "protected_support_through_mode": 4000,
                     "new_shell_protected_entries_exact_zero": True,
                     "cutoff_matches": [64000, 128000]})
    here = Path(__file__).resolve().parent
    # In the repository all three files share research-notes/.
    dependencies = ["suzuki_M8000_embedded_p4_ldd_capacity.py",
                    "suzuki_M8000_M16000_capacity_ratio_source_sensitivity.py",
                    "suzuki_M3999_frozen_p4_source_capacity_midpoint.py",
                    "suzuki_M8000_mu1_penalized_cholesky_outward.py"]
    sourcehashes = {name: hashlib.sha256((here/name).read_bytes()).hexdigest()
                   for name in dependencies}
    for sector in ("even-v", "odd-v"):
        for name in ("Z.npy", "modes.npy"):
            path = Path("p4_payload")/sector/name
            sourcehashes[str(path)] = hashlib.sha256((here/path).read_bytes()).hexdigest()
    out = {"schema": "cone.fullq-geometry-match.v1", "passed": True,
           "rows": rows, "source_hashes": sourcehashes,
           "scope": "Exact array identity and payload hashes; base spectral certificate is replayed separately"}
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True)+"\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
