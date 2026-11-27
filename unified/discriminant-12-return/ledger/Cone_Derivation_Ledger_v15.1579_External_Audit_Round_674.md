# Cone Derivation Ledger v15.1579 — External Audit Round 674

**Date:** 2026-11-27
**Track:** External Audit
**Subject:** Gravity v15.1576 (sharp clock-budget extremizer) and v15.1578 (its reconstruction as local vacuum optical curvature)
**Verdict:** Both CONFIRMED. The core differential identities independently rederived by hand (with care over a derivative-direction convention); both committed scripts reproduce the ledger's numbers bit-for-bit, including the specific rows at which maxima/failure flags occur.

## v15.1576 — CONFIRMED

Gate 1505's variational stationarity condition (`y=c/(vF²)` from a nonlocal Volterra-type nonlinear-constraint functional) was not independently rederived from scratch this round — this is the most technically involved step in the series and a full rederivation of the adjoint/Euler–Lagrange argument for this nonlocal functional was not attempted. However, its *consequences* are independently confirmed in full in v15.1578 below (the ODEs it implies check out exactly), which is strong indirect support.

Ran the actual committed `research-notes/k4_clock_variational_extremizer_v15_1576.py` from a clean scratch copy: reproduced all five continuum `(ε,δ,c,L*,ψ*)` rows exactly, the maximum refinement difference `2.2735157090281177e-9` (correctly the largest of the five printed refinement values), the graded-grid `L` and `Ξ(1)` sequences for `(ε,δ)=(.1,.05)` exactly, and — tellingly — the exact SLSQP convergence-flag pattern (`False` only at grid sizes 64 and 128 for that one pair, `True` for the other ten cases) reported in the ledger prose.

## v15.1578 — CONFIRMED, including independent rederivation of the core ODEs

Independently verified Gate 1509's reduction `j_x=(j-1)/x-x/c` (with `j=xv/(cv')`, `x=F=C-u`) by careful chain-rule computation through `v'=\exp(-\Xi(v))`, `\Xi_v=c/(vx^2)`, and `dv'/du=-\Xi_v(v)(v')^2` — the derivation requires tracking `d/du` vs `d/dx=-d/du` carefully, and reduces exactly to the stated `j_x=(j-1)/x-x/c`, confirmed independently that `j=1+Kx-x^2/c` satisfies this exactly (`j'=K-2x/c` matches `(j-1)/x-x/c` termwise).

Independently verified both of Gate 1510–1511's governing ODEs by direct substitution of `a=2/(\sqrt{c}\,j)`, `b=x/(cj)=v'/v`, using the same `d/du=-d/dx` convention: `b'+b^2+a^2/4=0` reduces exactly to `0=0` after substituting `j'=K-2x/c`, and `a'/2+ba=K/(\sqrt{c}j^2)` likewise reduces exactly once the `cj'+2x=cK` cancellation is used. Both match the ledger's stated identities exactly. The trivial identity `φ'=-ga` (direct differentiation of the stated `φ=\pi/2-g\,\ell`) was confirmed by inspection.

Ran the actual committed `research-notes/k4_clock_extremizer_vacuum_curvature_v15_1578.py` from a clean scratch copy: reproduced `c` and `L` for all five `(ε,δ)` pairs matching v15.1576's continuum values to displayed precision, the five endpoint spectral norms (`1666.46249, 124.916256, 1781.77626, 46635.0171, 161.985945`) exactly, and the maximum `q_ref` error (`5.74e-10`), Jacobi-ODE-vs-first-order error (`1.51e-10`), and endpoint determinant error (`5.04e-12`) all occurring — as the ledger's prose implies — on the same `(ε,δ)=(.1,.2)` row. All five `ψ` values matched the corresponding `ψ*` values from v15.1576 up to sign.

## Collision check

`v15.1579` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `f17cc54` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

The clock-extremizer sub-series (v15.1576, v15.1578) checks out: the core reduction ODEs for the exact vacuum-curvature reconstruction were independently rederived by hand and match exactly (after correctly tracking the affine-vs-coordinate derivative-direction convention), and both committed scripts reproduce every numerical quantity in the ledger bit-for-bit, down to which specific case attains each maximum error and which optimizer runs fail to converge. The one gap: the underlying variational stationarity condition itself (Gate 1505) was not independently rederived from the nonlocal constraint functional, though its consequences check out fully. No Lane A or Sandbox activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
