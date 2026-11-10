# Cone Derivation Ledger v15.616 — Lane A: action quantization, parabolic/oscillator spectral comparison, and mesh selector gate

**Date:** 2026-11-10. **Parents:** v14.592 (Archimedean parabola and Airy), v15.469 (acceleration action), Paper C Quantum Realizations v1.1, v15.595–596 (cross-shell witness), v15.602 (all-q refinement), v15.613–614 (fixed-product and staircase normalization), v15.615 (dilation and Fock-spectrum obstruction). **Status:** [D] exact classical action, operator/spectral and symplectic identities; [A] WKB asymptotic with errors; [O] physical factor-to-action correspondence and selected u,s,X. **Prewrite live HEAD:** 7e03d5948c1a68856aa12b1055ce3f7d52ad2d82; v15.616 collision search empty. Additive-only, no frozen Suzuki/far-tail modifications.

## Gate 94 — the quarter offset quantizes phase-space area, not a factor-mesh length

For H=p²/(2m)+maz on z≥0 (m,a>0) with a hard-wall boundary at z=0 and soft turning point z_t=E/(ma), the round-trip action integral is

**J(E)=2∫₀^{E/(ma)} √[2m(E−maz)]dz=4√2/(3a√m) E^{3/2}.**

Standard one-hard/one-soft semiclassical quantization uses
J(E_n)≈2πħ(n−1/4) (n=1,2,...),
and therefore
E_n^WKB=[3πħ a√m/(2√2) (n−1/4)]^{2/3}
=E0 [(3π/2)(n−1/4)]^{2/3},
E0=(ħ²ma²/2)^{1/3}.
Actual exact Airy quantum-bouncer energies E_n=E0|a_n|, where a_n are negative zeros of Ai. WKB is asymptotic, not the exact spectrum; independent SciPy evaluation n=1..8 gives -0.76372% error at n=1, -0.007801% at n=8. The quarter **Maslov** offset depends on the boundary/turning-point type; it is not a derivation of the proposed quarter-factor-vertex u=1/2, nor is the imported acceleration a a prediction of G.

## Gate 95 — global spectral mismatch with Paper C harmonic oscillator

Paper C's free two-mode oscillator energy is an affine function of total integer occupation N with adjacent gap ħω. The WKB bouncer energy is C(n−1/4)^{2/3}, n>1/4, whose second derivative is −(2/9)C(n−1/4)^{−4/3}<0. Therefore adjacent levels have strictly decreasing gaps, rather than an equal gap. At most selected single transitions can be matched by picking an externally supplied ω, drive or nonlinear Hamiltonian. Standard Paper C Schwinger SU(2) preserves N and does not change the radial shell, two-mode SU(1,1) changes N by ±2 and preserves difference D, and elliptic cuts preserve N parity but have no determined physical ω or u. Hence these native dynamics do not identify the entire Airy spectrum with the free oscillator tower.

## Gate 96 — mapping the action quantum to a geometric shell label requires an independent calibration

The chosen all-q geometric cross-shell boundary witness sends shell j→j+d_q with d_q=1−1/q (q≥2); d_2=1/2, d_3=2/3, d_4=3/4. This geometric j is **not** the WKB quantum number n nor the Paper C physical Schwinger spin. To interpret *one* witness step as ΔJ=2πħ, an additional conversion J=κ_q j+constant is required with κ_q=2πħ/d_q. None of the cited native equations fixes κ_q, and the ad hoc conversion depends on q. At q=2, the auxiliary doubled-occupation quartic operator increases Schwinger spin by 1 even though the geometric witness has Δj=1/2: a further dictionary mismatch, not a contradiction once their distinct meanings are tracked.

Under a canonical variable change Q'=λQ, P'=P/λ, the linear-potential Hamiltonian retains its form H=P'²/(2m')+m'a'Q' with m'=m/λ², a'=λa, so m'a'²=ma², E0 and J(E) are unchanged. This is covariance with simultaneously transformed *parameters*, not proof that physically distinct masses/accelerations are equivalent. It demonstrates that action quantization alone does not choose an absolute coordinate/mesh scale. The physical cutoff X for the divisor hyperbola and the factor-to-action map also remain externally unassigned.

## Reproducibility, outcome and scope

Conversation artifact `cone_action_gates_94_96.zip` (REPORT.md, reproduce.py) independently checks J integral and its WKB inversion, concavity, q=2/3 shell shifts, canonical scaling, and the exact Airy-vs-WKB dimensionless values n=1..8. All exact SymPy tests pass; no numerical fit of G, field or photon attempted.

**Verdict:** Native action quantization supplies the 2/3 exponent and a Maslov quarter phase, but **does not force u=1/2, s=1, or an absolute X**. The equally spaced oscillator and curved Airy spectra cannot coincide as whole towers without an added Hamiltonian. The physical-selector gate therefore stays open. Do not conflate geometrical quarter vertices, the 1/4 Casimir correction and the WKB Maslov phase without deriving an explicit dynamical intertwiner.

**HANDOFF** target external-audit, gravity, sandbox; status open; audit J(E), WKB conventions/errors, gap concavity, q-to-action calibration, canonical rescaling scope, and absence of a physical mesh selector. No change to Suzuki frozen production. **Suggested next gate:** test a fully specified factor-to-phase-space symplectic dictionary (with units and canonical two-form) that could link q-shell cross transitions to J(E), or prove no such natural map follows from the existing cone geometry alone.
