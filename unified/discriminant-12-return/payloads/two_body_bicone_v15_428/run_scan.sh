#!/bin/bash
cd ~/workspace/d12/explorations/two-body-bicone
for S in 0.2 0.5 1.0 1.5 2.0; do
  echo "=== ScanA S=$S ==="
  python3 two_body_drag_scan.py 200 $S 10 0.221 2>&1 | grep SCANJSON
done
echo "=== ScanB sep=5 S=1.0 ==="
python3 two_body_drag_scan.py 65 1.0 5 0.3162 2>&1 | grep SCANJSON
echo "=== ScanB sep=5 S=0.05 ==="
python3 two_body_drag_scan.py 65 0.05 5 0.3162 2>&1 | grep SCANJSON
echo "=== ScanB sep=10 S=0.05 ==="
python3 two_body_drag_scan.py 200 0.05 10 0.221 2>&1 | grep SCANJSON
echo "=== ScanB sep=20 S=1.0 ==="
python3 two_body_drag_scan.py 516 1.0 20 0.1581 2>&1 | grep SCANJSON
echo "=== ScanB sep=20 S=0.05 ==="
python3 two_body_drag_scan.py 516 0.05 20 0.1581 2>&1 | grep SCANJSON
echo "ALL SCANS DONE"
