#!/bin/bash
# Far585 step 5: finite far residual composition F1/F2, both sectors
# serial. Per-class certs in far_compose.py give resume: a class whose
# cert + buffer verify on disk is skipped. A failed stage aborts
# without the DONE stamp.
set -u
cd /home/hatch/workspace/d12/dm490/far585
step() { echo "=== $* $(date -Is) ==="; "$@" || { echo "=== FAR_COMPOSE FAILED rc=$? $(date -Is) ==="; exit 1; }; }
step python3 far_compose.py --sector even-v
step python3 far_compose.py --sector odd-v
echo "=== FAR_COMPOSE_ALL_DONE $(date -Is) ==="
