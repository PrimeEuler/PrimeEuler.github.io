#!/usr/bin/env python3
"""Paper A area-companion entry point for the n=11 area-measure figure."""
from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).with_name("fig_area_measure_11_2panel.py")), run_name="__main__")
