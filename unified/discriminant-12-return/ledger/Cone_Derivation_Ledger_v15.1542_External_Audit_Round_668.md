# Cone Derivation Ledger v15.1542 — External Audit Round 668

**Date:** 2026-11-26
**Track:** External Audit
**Subject:** v15.1540 (Gravity, Nyquist derivative defect) and v15.1541 (Gravity, conic operator dictionary)
**Verdict:** v15.1540's exact discrete identity and numerical table both independently confirmed. v15.1541's geometric/algebraic claims independently confirmed by hand and the committed script's exact symbolic reproduction.

## v15.1540 — CONFIRMED

**Gate 1429 (exact Nyquist identity):** verified directly by constructing the Nyquist cosine mode `f_j=(-1)^j` on an N=8 real grid and computing both the spectral first-derivative operator `D` (as implemented in the audited solver's `grad`, via `ifft(1j*k*fft(f)).real`) and the second-derivative operator `L` (via `ifft(-k²*fft(f)).real`). Result: `D f = 0` exactly at every node (the real-projection step exactly annihilates the Nyquist mode's derivative, since it has no Hermitian-symmetric partner at that single bin), while `L f = -(N/2)² f` exactly. This confirms `L-D²=-(N/2)² P_Nyquist` as an exact, verifiable fact of this FFT convention, not an approximation.

**Gate 1430 (linearized coefficient algebra):** checked the stated algebra is self-consistent: given `T-H_direct=(L-S)ψ` and `H_composed-H_direct=4(L-S)ψ`, substituting gives `T=(3H_direct+H_composed)/4`, which reduces to the claimed `T≈H_composed/4` exactly when `H_direct` is negligible — which the numerical table confirms (`H_direct~1e-14`, six-plus orders of magnitude below `H_composed`). The full tensor derivation of the `-3L-S` / `-4L` coefficients from the linearized reduced Einstein equations was not independently re-derived from scratch this round; the audit's check here is the algebraic self-consistency between the stated coefficients and the observed `T≈H_composed/4` pattern, which holds exactly.

**Gate 1431 (numerical table):** the ledger disclosed its reported numbers came from an uncommitted local driver (`/mnt/data/cone_gh/nyquist1539.py`). Ran the actual committed `research-notes/k4_gh_nyquist_quarter_defect_v15_1540.py` from a clean scratch copy against the unchanged audited v15.1485 dependency. It completed with no assertion failures. Every value in the ledger's table matched this independent rerun to full displayed precision for N=16, 24, 32, and the odd-N=17 control: H_direct, H_composed, T, `T-H_composed/4`, dominant Fourier mode and its coefficient (including sign), Laplacian defect, and the N=17 control's qualitatively different behavior (mode `(0,5,0)`, no quarter mechanism). Since this script performs a single analytic evaluation with no iterative time-stepping, reproduction is near-exact (not subject to v15.1537's RK4 floating-point drift).

## v15.1541 — CONFIRMED

Independently hand-verified, by direct differentiation/Taylor expansion, every geometric identity claimed: `P, C, H` share value/first/second derivative `0,0,1/h` at `Y=0`; the fourth-order terms `C=P+Y⁴/(8h³)`, `H=P-Y⁴/(8h³)`; the parabola's Euclidean curvature formula; the hyperboloid invariants `Qa_p²=1`, `QK=-1`; the cap half-width `b=sqrt(2hd)` and exact area `A_p=(4/3)sqrt(2h)d^{3/2}`; the elasticity identities `A_p/(dA_p')=2/3` and its reciprocal `3/2`; and the evolute formulas `E=-Y³/h²`, `F=h+3Y²/(2h)` with `27hE²=8(F-h)³` — all match the ledger exactly by direct algebra.

Independently verified Gate 1434's numerical table by direct numerical integration of `R(z)=∫₀¹w(zs)ds/w(z)` for `w_H=sqrt(z(2+z))`, `w_C=sqrt(z(2-z))`, matching every tabulated value at z=.01, .1, .5, 1 to the displayed precision — including `R_C(1)=π/4` exactly. Independently confirmed the small-z series `R_H=2/3-z/15+z²/35+O(z³)` and `R_C=2/3+z/15+z²/35+O(z³)` (the opposite-sign linear coefficient was confirmed via finite-difference slope estimation at `R_C`, converging to `+1/15` as `z→0`).

Ran the actual committed `research-notes/k4_conic_operator_dictionary_v15_1541.py` from a clean scratch copy. It is a pure SymPy symbolic/exact script (no floating-point iteration), and it completed with every internal assertion passing and `PASS` printed; its printed symbolic outputs (parabola area, evolute formulas, both `±1/15` series) and its numeric table at the same four z-values matched the ledger exactly.

## Collision check

`v15.1542` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `159e0b7` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

Gravity: v15.1540 resolves the quarter-ratio puzzle flagged in v15.1538 — the Nyquist-mode derivative/second-derivative mismatch is an exact, verified artifact of the real-FFT convention, and its numerical consequences are independently confirmed from the actual committed driver. v15.1541's conic-geometry dictionary (a side gate, explicitly not a physical-coupling claim) checks out completely by hand and by the committed script's exact symbolic reproduction. No Lane A or Sandbox activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
