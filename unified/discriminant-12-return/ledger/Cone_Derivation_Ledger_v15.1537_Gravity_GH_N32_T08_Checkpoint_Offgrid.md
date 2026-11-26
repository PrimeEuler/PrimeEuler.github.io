# Cone Derivation Ledger v15.1537 — Checkpointed unrestricted Einstein–H² GH evolution through T=.08 with independent 64³ off-grid constraints

**Date:** 2026-11-26. **Lane:** Gravity/Cone. **Status:** locally executed numerical result, independent exact-byte Audit replay pending. Prior v15.1505 confirmed by Audit Round 655 (37c7ae90bd3032f57d541d6d8b52a7a436e2a070). Live HEAD before new gravity work was Lane A v15.1536, 6c13e14c261244e5697fe49411485e11bb7eacef. No Suzuki or Sandbox objects modified.

## Gates 1424–1425

Use the full unrestricted nonlinear 3D generalized-harmonic Einstein–H² solver with the previous N32³ nonlinear constrained torus data, κ=.003, RK4 dt=.004. An initial uninterrupted attempt timed out after t=.04. A fresh run used four five-step segments, saving all evolved metric, metric velocity, target field and target velocity arrays after each step using atomic NPZ replacement and restarting from the stored step counter. No constraint projection or resetting. Actual local driver /mnt/data/cone_gh/gate1537_checkpoint.py with /mnt/data/cone_gh/gh3d.py and /mnt/data/cone_gh/gate1497_offgrid_fast.py. Single-thread OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1. All four segments completed, followed by a separate independent 64³ monitor.

| t | native GH max | native ADM H max | native ADM M max | max inverse g^tt |
|---|---:|---:|---:|---:|
| .02 | 7.174469351944879e-13 | 1.4551166139533354e-10 | 2.1962214138233557e-11 | -.999368938295959 |
| .04 | 1.712783486275491e-12 | 1.2621636521310473e-10 | 4.1794216010119026e-11 | -.9987381424513845 |
| .06 | 3.5433252062707157e-12 | 9.396349732906754e-11 | 5.746719471274274e-11 | -.9981076128267071 |
| .08 | 5.576599478149171e-12 | 5.234775007673283e-11 | 6.736734179399809e-11 | -.997477350607694 |

At t=.08 interpolate the entire evolved state in all three spatial dimensions with scipy.signal.resample to N64³, recompute the full ADM constraint monitor and inverse-divergence GH vector (not interpolate residuals). Result GH=5.577698283169667e-12, H=4.046728869968458e-11, M=6.744011635760865e-11, max inverse g^tt=-.9974773506076943. The off-grid Hamiltonian max is ~0.77 of native; off-grid gauge and momentum agree closely. This corroborates the resolved bandlimited state at this endpoint. GH and momentum grow over the interval, Hamiltonian falls: not a demonstration of monotonic constraint damping. Absolute residuals are in model units.

Canonical additive equivalent driver research-notes/k4_gh3d_checkpoint_t08_v15_1537.py commit 839920d0b22b94927682d213ce2fc38cba83107e uses corrected Audit-confirmed v15.1485 solver. The exact committed driver has not been executed in this turn; the reported results come from the actual local driver. Use four invocations with --steps 5 and same fresh checkpoint path, then --steps 0 --offgrid. No N40 equal-time run or T=.08 temporal refinement performed in this gate. No assertion of long-time stability or new physical gravitational observable. κ remains input; Weyl–Maxwell interaction absent.

## Next and Audit

Replay exact committed driver, check checkpoint consistency and all tabulated native/off-grid constraints. Compare N40 at matched endpoint and timestep, then examine the GH subsidiary equation. For C_mu=g_mu nu C^nu, on-shell conserved sigma stress and reduced Einstein equations R_mu nu - ∇_(mu C_nu)=κ G_AB ∂_mu φ^A ∂_nu φ^B give □ C_nu + R_nu mu C^mu=0 by the contracted Bianchi identity. This continuum identity does not establish numerical subsidiary propagation; independently compute C and its normal derivative from the evolving metric and acceleration before claiming closure. No numerical subsidiary test reported here. Sandbox variance→area selector remains closed absent a new action-selected pullback operator.
