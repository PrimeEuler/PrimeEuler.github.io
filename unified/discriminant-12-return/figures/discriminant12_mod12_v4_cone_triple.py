#!/usr/bin/env python3
"""Discriminant-12 entry point for the mod-12 V4 cone figure generator."""
from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).with_name("make_mod12_v4_cone_triple.py")), run_name="__main__")
