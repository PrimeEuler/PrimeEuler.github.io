#!/bin/sh
# Full SVT reproducer chain (see NOTE.md). Run from this directory.
set -e
python3 tensor_check.py
python3 matter_sector.py
python3 eh_scalar.py
python3 assemble.py
python3 vector_sector.py
python3 scalar_statespace.py
python3 final_checks.py
