#!/usr/bin/env python3
"""Paper A entry point for the canonical n=11 divisor-summatory figure."""
from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).with_name("fig_divisor_summatory_11_3panel.py")), run_name="__main__")
