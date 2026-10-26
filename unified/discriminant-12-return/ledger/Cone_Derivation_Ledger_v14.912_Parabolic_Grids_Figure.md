# Cone Derivation Ledger v14.912 — Parabolic-coordinate figure for the weld: EM on the 1/2 lattice, dyons on the 1/4 lattice, and the n = 4 shell

Date 2026-10-26. Sandbox lane. Parent v14.904 (the weld); requested by Jeremy as the visual companion. Payload `payloads/parabolic_grids_figure_v14_912/` (`grids_parabolic.png`, `make_figure.py`, `README.md`). Additive only.

## Content [D, figure of record facts]

Two panels of the cone's (X, Y) = (offset, GM) plane with the canonical row/column parabola mesh (rows #7fa7cf, columns #b08fcf), one per dictionary:

- **EM (h = 1, q = 1/2)**: members x, y ∈ ℤ; crossings at offsets (1/2)ℤ; pair products (k/2)² (Dirac); smallest parabolas' vertices at X = ±1/2; r = log n; unit raw pair (1,1) = grid (1,1), shell n = 1.
- **Gravitational dyons (h = 1/2, q = 1/4)**: members in (1/2)ℤ; offsets (1/4)ℤ; pair products (k/4)² (Taub–NUT/Misner, G cancelling); vertices at ±1/4; r = log(n/4); unit raw pair (1,1) = grid (2,2), shell **n = 4**; the shell's remaining nodes, grid (1,4) and (4,1) at X = ±3/4, are circled. EM nodes are the even sublattice of the dyon nodes (v14.731 §4).

The radial function r = log(xy) is the same in both panels — the dashed r = 0 line Y = 1 is one geometric line; what the weld changes is the grid shell index n = xy/h² assigned to it. Reading chain: mesh offset lattice (h/2)ℤ [D] + node = state premise ⇒ h = 2q; vertices = ±q (the pair quantum IS the vertex); counting starts at the shell carrying the first complete pair — n = 1 (EM) vs n = 4 (dyons), which is the 4 in Suzuki's (D_log)_nn = log(n/4).

Flags: figure_of_record_facts=TRUE; new_claims=NONE; weld_premise=node_equals_state (unchanged, v14.904); G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.
