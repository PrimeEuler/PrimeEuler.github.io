# Cone Derivation Ledger v15.1540 — Nyquist derivative defect explains the numerical quarter ratio

**Date:** 2026-11-26. **Lane:** Gravity/Cone. **Status:** executed local nonlinear diagnostic; linearized discrete identity; independent exact-byte replay pending. Parent v15.1538. Live HEAD before write: Audit Round 667, 215653832285d78c9068ce6c9c7e84d08833cf4c. No other lanes modified.

## Gate 1429 — exact Fourier differentiation defect

For a real periodic N-node collocation grid, even N, the Nyquist cosine (-1)^j has real first derivative zero at every node but direct second derivative -(N/2)^2 (-1)^j on the 2π-periodic torus. Thus the real projected first-derivative operator D and direct second derivative L obey L-D²=-(N/2)^2 P_Nyquist. In three dimensions sum over axes. Odd N has no such exceptional mode. This is an exact discrete operator identity.

The user's quarter-period sine cycle (0,+1,0,-1,0) is realized by the Nyquist cosine on a grid twice as fine, up to phase. On the original grid the mode has only two samples per period, so its derivative quadrature is invisible. The quarter-period phase shift is genuine; it does not alone imply a quarter amplitude.

## Gate 1430 — linearized coefficient

At the unit-lapse, zero-shift initial slice take conformal spatial metric γij≈(1+2ψ)δij and harmonic-compatible shift velocity p0i=-D_iψ. Write L=Σ direct second derivatives, S=Σ D_i². In the flat-background linearized reduced Einstein equations the spatial wave contribution to ∂t C_0 is -3Lψ-Sψ (three spatial metric diagonals supply -3Lψ; differentiated shift supplies -Sψ). The corresponding Hamiltonian principal spatial contribution is -4Lψ, with the same algebraic linear matter contribution. Therefore T-H_direct=(L-S)ψ at this order. The composed-derivative Hamiltonian instead has -4Sψ, so H_composed-H_direct=4(L-S)ψ. When the direct Hamiltonian is solved, T≈H_composed/4. The factor is from the conformal curvature coefficient four and a single missed derivative contribution, not a new physical gravitational coupling. Nonlinear corrections and other aliasing errors remain. No exact nonlinear equality asserted.

## Gate 1431 — actual numerical test

Executed /mnt/data/cone_gh/nyquist1539.py importing gh3d.py with single-thread OpenBLAS. Reconstructed ψ=log γ11/2, matter and extrinsic terms from the unchanged constrained initial state. Compared the same conformal Hamiltonian formula with direct Laplacian and composed real first derivatives. Independently differentiated contracted GH vector using metric accelerations as in v15.1538. Fourier amplitudes normalized by N³.

| N | max H_direct | max H_composed | max T | max abs(T-H_composed/4) | dominant (ky) H_composed coefficient | T coefficient |
|---:|---:|---:|---:|---:|---:|---:|
|16|1.466e-14|4.2169373e-6|1.0542401e-6|9.127e-12| -8: +4.2141547347e-6|+1.0535386839e-6|
|24|3.445e-14|1.1058190e-8|2.7651084e-9|6.149e-13| -12: -1.0930046396e-8|-2.7325103565e-9|
|32|4.837e-14|1.5008331e-10|3.7498157e-11|1.155e-13| -16: -1.4646700038e-10|-3.6615765208e-11|

Dominant Fourier mode in each case is (0,-N/2,0) for both residuals. Coefficients are real to roundoff, same phase, ratio approximately .25. Max Laplacian defect at N16/24/32: 1.0542291e-6, 2.7645513e-9, 3.7511704e-11. Odd N17 control: max Laplacian defect 2.71e-20, H_direct and H_composed about 1.66e-14, T=2.63463e-11, dominant T mode (0,5,0). Thus Nyquist mechanism explains dominant even-grid quarter ratio, but does not remove all other discrete errors.

Canonical equivalent source research-notes/k4_gh_nyquist_quarter_defect_v15_1540.py commit ea92945d49a7e73cfe39275aa71b121df4c06343, imports audited repaired solver. Local driver executed; exact canonical bytes not yet executed. Audit replay requested. Next test consistent derivative jets in the ADM and GH monitors, including Nyquist treatment in the elliptic solve; do not simply erase modes or substitute an inconsistent wave operator. Full evolved subsidiary equation and matched N40 T=.08 remain open. No G-free observable or physical quarter-grid response derived.