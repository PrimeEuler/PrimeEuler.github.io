# Figures for the arXiv Cone Program Series

Canonical figure generators and outputs. Every figure is produced by its
Python script — never the AI image generator (Jeremy's standing rule).

Each paper's `build.sh` rebuilds the PDF from `.tex`; figures are
pre-built PDFs copied from here.

| Figure | Generator | Used in |
|--------|-----------|---------|
| fig_cutting_plane_4panel | paperA_cutting_plane_4panel.py | paper-a-cutting-plane |
| fig_divisor_summatory_11_4panel | paperA_divisor_summatory_11_4panel.py | paper-a-cutting-plane |
| fig_totient_hyperbolas_4panel | note_totient_hyperbolas_4panel.py | note-totient-v4qr12 |
| fig_lorentz_orbits_4panel | paperB_lorentz_orbits_4panel.py | paper-b-eigencoordinates |
| fig_power_maps_4panel | paperB_power_maps_4panel.py | paper-b-eigencoordinates |
| fig_su2_su11_sectors_4panel | paperC_su2_su11_sectors_4panel.py | paper-c-quantum-realizations |
| fig_cusp_dynamics | paperD_cusp_dynamics.py | paper-d-cusp-cubic |
| fig_cone_roadmap | roadmap_cone_map.py | roadmap-cone-program |
| fig_bicone_sphere | bicone_so4.py / bicone_4view.py | note-bicone-dipole-alpha |
| fig_bicone_dipole_shells | bicone_dipole_shells.py | note-bicone-dipole-alpha |

Cone-figure convention: every cone figure carries the canonical row/column
parabola mesh (rows #7fa7cf, columns #b08fcf), low-alpha projection.
