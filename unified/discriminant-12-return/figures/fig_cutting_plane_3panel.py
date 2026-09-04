from pathlib import Path
import runpy
import shutil

# Canonical Paper A cutting-plane figure entry point.
#
# The audited geometry lives in fig_cutting_plane_tangent_circle_audit.py,
# while fig_cutting_plane_tangent_circle_publication.py applies only
# publication-layout changes. Running this file generates the audited
# publication figure and copies it to the stable filenames used by Paper A.

HERE = Path(__file__).resolve().parent

runpy.run_path(
    HERE / "fig_cutting_plane_tangent_circle_publication.py",
    run_name="__main__",
)

for suffix in ("pdf", "png"):
    src = HERE / f"fig_cutting_plane_tangent_circle_audit.{suffix}"
    dst = HERE / f"fig_cutting_plane_3panel.{suffix}"
    if not src.exists():
        raise RuntimeError(f"Expected generated audit figure not found: {src}")
    shutil.copy2(src, dst)
    print(f"saved {dst}")
