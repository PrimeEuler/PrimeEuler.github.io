#!/usr/bin/env python3
"""Arch-200 scalar interval audit extended through mode 16000.

Reuses the successful M8000 420-digit interval producer unchanged except for
TARGET_MAX=16000 and a distinct result path.
"""
from pathlib import Path
import suzuki_M8000_scalar_interval_audit_arch200 as audit

audit.TARGET_MAX=16000
audit.OUT=Path(__file__).resolve().parent/"M16000_scalar_interval_audit_arch200_result.json"

if __name__=="__main__":
    audit.main()
