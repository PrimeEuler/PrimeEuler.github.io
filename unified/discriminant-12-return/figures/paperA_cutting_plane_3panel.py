#!/usr/bin/env python3
"""Paper A entry point for the canonical cutting-plane figure generator."""
from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).with_name("fig_cutting_plane_3panel.py")), run_name="__main__")
