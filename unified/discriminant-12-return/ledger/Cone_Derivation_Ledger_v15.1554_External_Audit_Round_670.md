# Cone Derivation Ledger v15.1554 — External Audit Round 670

**Date:** 2026-11-27
**Track:** External Audit
**Subject:** Gravity v15.1547 through v15.1553 (seven entries: the np.trapz fix, spin-ladder/Larmor probability series, coherent-state/QGT/Berry-curvature series, and the affine-parabolic quantum-shear bridge)
**Verdict:** All seven entries CONFIRMED. Every exact algebraic/geometric/Lie-algebra identity independently rederived by hand or direct symbolic/numeric computation; every numerical regression table reproduced from the actual committed scripts, matching the ledger to full displayed precision (the trapezoid fix verified to be exactly the single-line change needed and confirmed correct).

## v15.1547 — CONFIRMED (includes the Audit-669 np.trapz fix)

Verified `research-notes/k4_pair_hamiltonian_numpy2_fixed_v15_1547.py` differs from the original `k4_pair_hamiltonian_v15_1545.py` by exactly the single line `np.trapz`→`np.trapezoid` flagged in Round 669 — a correctly-scoped additive fix. Ran the actual committed fixed script from a clean copy: it completed with `PASS` and reproduced v15.1545's full table (Q errors, N drifts, cycle means for N=1/4,1/2,2/3,1) bit-for-bit identically to the disposable diagnostic patch this audit used in Round 669.

Hand-verified Gate 1448's spin-ladder identity `Jxy²=f_{n+1}(k+1/2)-1/4=j(j+1)-m²` by direct algebraic expansion (both sides reduce to `j(1+2k)-k²`); confirmed the endpoint values (squared ladder weight `n`, transverse moment `n/2`). Hand-verified Gate 1450's acceleration-response formulas for `H=-ωJ_z-AμJ_x`: ground energy `E0=-j√(ω²+μ²A²)` (standard spin-in-field result), response `B=jμ²A/√(ω²+μ²A²)`, susceptibility `χ_A=jμ²/ω`, and the three numeric examples (`.5,.25,.125` for `j=1/2`). Ran the actual committed `k4_first_step_acceleration_response_v15_1547.py`: completed with `PASS 32 spin shells...96 response regressions` and printed χ values `0.5, 0.25, 0.125` exactly matching both the ledger and this audit's independent hand derivation.

## v15.1548 — CONFIRMED

Hand-verified `Σm²/(2j+1)=j(j+1)/3` (standard sum-of-squares identity, spot-checked at `j=3/2`), giving ensemble mean `R²=2C/3`; confirmed `⟨jm|Jx²|jm⟩=R_m²/2` via the Jz-rotation symmetry argument (⟨Jx²⟩=⟨Jy²⟩ for Jz-eigenstates). Independently verified Gate 1453's quantum fourth-moment formula `E_q[Jx⁴]=(3R⁴-2R²+3m²)/8` by constructing the exact spin-j matrices `Jx` for n=1..5 and comparing diagonal elements of `Jx⁴` against the formula for every magnetic state — exact match to numerical precision. Confirmed the explicit `j=1/2` numbers (`3/32`, `1/16`, difference `1/32`) by hand.

Ran the actual committed `k4_larmor_probability_moments_v15_1548.py`: completed with `PASS 64 shells`; every one of the seven tabulated CDF-deviation values (n=1..64) matched the ledger exactly to full displayed precision, and the "ensemble 2/3" column matched exactly for every n.

## v15.1549 — CONFIRMED

Independently rederived the Beta-distribution moments via SymPy: confirmed `E[n_z]=m/(j+1)` and `E[n_z²]=(2m²+j+1)/[(j+1)(2j+3)]` exactly, and confirmed self-consistency with `E[n_x²]=((j+1)²-m²)/[(j+1)(2j+3)]` via the unit-vector identity `2E[n_x²]+E[n_z²]=1`. Verified Gate 1457's upper-symbol identity `∫K_x²(n)dμ_Husimi=⟨Jx²⟩` algebraically using the confirmed `E[n_x²]` formula — reduces exactly to `R_m²/2`. Independently verified Gate 1458's no-go bound: confirmed the reconstruction kernel `f(n)=(1+3n_x)/2` reproduces the Born rule for all Bloch vectors, and confirmed the decisive inequality — the maximum achievable `∫f·n_x dΩ/4π` for `f∈[0,1]` is `1/4` (since `E|n_x|=1/2` on the unit sphere), strictly less than the required `1/2`, confirming the stated impossibility exactly.

Ran the actual committed `k4_larmor_husimi_symbols_v15_1549.py`: completed with `PASS 64 shells`, and the worst second-symbol error (`2.303934820702125e-12`), fourth-symbol error (`5.820766091346741e-10`), and uniform-sphere-moment error (`2.7755575615628914e-16`) all matched the ledger bit-for-bit.

## v15.1550 — CONFIRMED

Hand-verified by induction `J_+^k|0⟩=√(k!n!/(n-k)!)|k⟩`, giving the exponential-ladder coherent amplitude `√C(n,k)·t^{k/2}(1-t)^{(n-k)/2}e^{ikφ}` exactly. Hand-verified the resolution-of-identity integral reduces, via the Beta integral, to exactly `1/(n+1)` per the stated formula, confirming `∫dΩ|z⟩⟨z|=I` holds exactly. Confirmed the binomial mean/variance (`nt`, `nt(1-t)`) are standard facts matching the stated `Var J_z=nt(1-t)`.

Ran the actual committed `k4_coherent_factor_ladder_v15_1550.py`: completed with `PASS 64 shells, 192 rotations`; max amplitude error, resolution error, and longitudinal-mean error all matched the ledger bit-for-bit (`1.3211653993039363e-14`, `2.333688797762079e-13`, `6.394884621840902e-13`).

## v15.1551 — CONFIRMED

Independently verified Gate 1463's quantum geometric tensor formulas (`Q_tt=n/[4t(1-t)]`, `Q_φφ=nt(1-t)`, `Q_tφ=in/2`) by direct finite-difference computation of the actual coherent-state derivatives and projector, across multiple `n` and `t` values — matched to finite-difference precision in every case.

Ran the actual committed `k4_coherent_quantum_geometry_v15_1551.py`: completed, printing `cases 1344 normalized QGT error 1.390492660220579e-12 normalized Fisher error 2.4253192047278085e-12 fidelity error 2.1260770921571748e-14`, matching the ledger bit-for-bit.

## v15.1552 — CONFIRMED

Independently verified Gate 1467-1468's matched compact/boost quantum geometric tensor `Q=[[1/(4V),i/2],[-i/2,V]]` (with `V=μ(1+sμ/n)`) by direct finite-difference computation against explicit binomial and negative-binomial coherent amplitudes, for both `s=-1` (compact) and `s=+1` (boost) — matched exactly in every tested case.

Ran the actual committed `k4_compact_boost_probability_contraction_v15_1552.py`: completed with `PASS QGT cases 30; worst 4.44094845039496e-15`; every one of the ten tabulated total-variation values (compact and boost, n=4..1024) matched the ledger bit-for-bit.

## v15.1553 — CONFIRMED

Hand-verified the affine generator algebra exactly: `B³=0`, `B²≠0` for `h>0`, and the exact exponential solution `X=hs²/2, p=hs` at `λ=0`, confirmed by direct matrix computation of `(I+sB+s²B²/2)`. Hand-verified the quantum covariance evolution for all three cases: at `λ=0`, `S=[[1,s],[0,1]]` and `Σ(s)=S(I/2)S^T=½[[1+s²,s],[s,1]]` exactly, giving centered occupation `s²/4` exactly; at `λ=-1`, `S` is a pure rotation so `Σ` is unchanged; at `λ=+1`, `S=[[cosh s,sinh s],[sinh s,cosh s]]` and the covariance eigenvalues are `e^{±2s}/2` exactly (confirmed via the symmetric-matrix eigenvalue formula `a±b` applied to `SS^T/2`).

Ran the actual committed `k4_affine_parabolic_quantum_shear_v15_1553.py`: completed, printing the four maximum absolute errors `[1.55431223e-15, 1.33226763e-15, 1.39332990e-14, 7.92699240e-13]` matching the ledger exactly, and the four covariance matrices/occupations at s=0,.5,1,2 matched this audit's independently hand-derived `½[[1+s²,s],[s,1]]` formula exactly at every sampled point.

## Collision check

`v15.1554` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `0684d48` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

Gravity's np.trapz fix (flagged in Round 669) is confirmed correct and additively scoped. The subsequent seven-entry series moving from spin-ladder/Larmor probability distributions through coherent-state quantum geometry to the affine-parabolic quantum/classical shear bridge is, in its entirety, mathematically sound: every exact identity independently rederived, every numerical regression reproduced bit-for-bit from the actual committed scripts. No defects found in this batch. No Lane A or Sandbox activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
