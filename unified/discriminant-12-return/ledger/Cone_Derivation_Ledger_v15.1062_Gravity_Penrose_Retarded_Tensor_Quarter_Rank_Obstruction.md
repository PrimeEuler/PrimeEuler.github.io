# Cone Derivation Ledger v15.1062 — Penrose/conformal retarded tensor Green reconciles with proper-time Euler Green; no q2 projection

Date 2026-11-16 Eastern / 2026-11-17 UTC. Lane Gravity/Cone. Status [D] exact temporal Fourier retarded kernels, their reconciliation to already established proper-time tensor Green, boundary effective-mass limit, and diagonality/non-selection control; [N] no independently sourced cross-shell operator, detector signal or G-free force. Latest live HEAD checked before ledger write: 74ce060014ec6764d76517e769155b3819d769db (new reproducer). Additive only, earlier Audit/Sandbox/Muse/Suzuki/certified objects unchanged.

## Redundancy and provenance

Previously v14.928/v14.935 derived the frozen coasting EH+K4 elastic-solid tensor mode equation. v15.722 §Gate340 already gave an exact retarded proper-time Euler tensor kernel with source and zero initial data; v15.872 already tested its logarithmic-time phase response. v15.995-998 source-first Maxwell–TT selection and z2 no-odd-photon obstruction were independently audited v15.999. v15.1052–1058 were independently verified by Audit Round 588, canonical v15.1059. v15.1060 identifies the arithmetic Cone with conditional null coordinates and warns against reading its T/X hinge as future-directed; v15.1061 writes the **actual physical coasting metric** in conformal null coordinates and identifies the effective conformal tensor mass zero at elastic zeta=3/8. This gate only reconciles two coordinate Green kernels and checks if that cancellation produces a q2 sector selector. It does NOT rediscover retarded response or insert a new physical interaction.

## Gate 881 — Fourier retarded conformal tensor kernel

From v15.1061, let psi=a*h and conformal time eta=sqrt(3)ln(tau/tau0). The source-free tensor principal operator is
(∂eta²-∂z²+mu²)psi=0, mu²=(8 zeta-3)/9.
With an independently supplied, correctly normalized tensor source J on the RHS, the causal Fourier kernel (k>=0) is
G_k(Δeta)=Theta(Δeta) sin(omega_k Δeta)/omega_k,
omega_k²=k²+mu².
For omega_k=0 take the continuous limit G_k=Theta Δeta. It satisfies G(0+)=0, ∂_Δ G(0+)=1; and the distributional identity (∂_Δ²+omega_k²)G_k=delta(Δ).
The scale zeta=3/8 has mu²=0 and G_k=Theta sin(kΔeta)/k. This is a special cancellation for canonically rescaled tensor modes, not a vanishing physical tensor mass nor a distinct causal cone. In 1+1 spacetime, the position-space massless retarded scalar kernel has support *inside* (and on) the future causal cone; saying all its amplitude lives exclusively on 45-degree rays would be incorrect. In 3+1 there is a different Huygens support property and additional angular structure. The modewise formula does not depend on selecting the 1+1 spatial Green support.

## Gate 882 — exact equivalence to audited-precursor proper-time Euler kernel

v15.722 writes for tensor h=gamma,
h_ddot+3 h_dot/tau + (beta/tau²)h=J_tau,
beta=3k²+8zeta/3, and the unit-impulse proper-time Green
G_Euler(tau,sigma)=Theta(tau-sigma) sigma²/tau * sin(nu ln(tau/sigma))/nu,
nu²=beta-1.
Conformal tensor frequency obeys the exact identity nu²=3 omega_k²; Δeta=sqrt(3)ln(tau/sigma). These are the same homogeneous dynamics expressed in different variables. The proper-time G_Euler has discontinuity of first tau derivative equal to unity at tau=sigma; it is not literally numerically equal to G_k because the time parameter, canonical variable psi=a h and source/Dirac-delta normalization differ. Confusing kernels without these factors would produce a false amplitude. The script independently tests the Euler ODE and its impulse jump and the conformal oscillator impulse jump.

## Gate 883 — full modal response does not produce the rank-two quarter-ladder projector

For a spatially homogeneous background with diagonal tensor harmonic dynamics, the retarded Laplace-domain resolvent is
R_k(p)=[p²+k²+mu²]^{-1}, Re(p)>0, zeta>=3/8.
At k=2 and k=4, the 2×2 block is diag(1/[p²+4+mu²],1/[p²+16+mu²]); its determinant is strictly nonzero for real p>0. Its off-diagonal entry vanishes exactly. This remains true at zeta=3/8, zeta=3/4, zeta=3/2, verified symbolically. The Green operator therefore does not choose two particular open-quarter *source states* by virtue of the conformal mass cancellation: a generic tensor source couples to the allowed diagonal spatial modes, not to an automatically distinguished rank-two subspace of the q2 finite shell Hilbert spaces. A tensor Fourier mode label k is not the quarter-shell magnetic label i. On q2 shell L>=3, the independent chosen geometric T_q has source projector P_L=|1><1|+|L-1><L-1|, amplitude sqrt[(L+1)/4] and target shell L+2. No map from physical spatial tensor modes to these shell states, boundary conditions selecting P_L, nor action-derived L-dependent coupling follows from the retarded kernel.

The previously proposed spatial 0-to-4 and plus-to-cross mixed exchange also remains zero for reflection-symmetric homogeneous background without independently sourced mode mixing (v15.998); a nonzero physical anisotropic/background source would require doing its actual constrained K4/Maxwell field problem before computing any q2 projection. In particular the massless endpoint does NOT bypass the y-photon parity veto.

## Gate 884 — reproducibility, physical gate

Exact SymPy reproducer research-notes/k4_conformal_retarded_rank_test_v15_1062.py, additive commit 74ce060014ec6764d76517e769155b3819d769db. Executed locally: PASS oscillator ODE plus causal jump, zeta=3/8 k->0 limit, nu²=3omega², proper-time Euler ODE and impulse jump, and k=2/4 resolvent full rank plus zero mixing for zeta=3/8,3/4,3/2. No numerical fit used. Audit of v15.1060-1062 pending.

Verdict: [D] causal propagation agrees between the old K4 proper-time analysis and the new Penrose/conformal description. [N] The edge mass cancellation changes dispersion but selects neither an inter-cone sign reversal nor the quarter-ladder boundary projector; it does not derive G, physical units or a new observable. Next genuinely source-first experiment: take a conserved finite-size Maxwell stress and consistent physical boundary, solve all linear metric/ADM constraints, calculate a gauge-invariant retarded Weyl or phase response and compare with an identical conventional GR+elasticity comparator; independently demonstrate any identification with signed-pair circle/quarter-shell states rather than assuming it.

AUDIT HANDOFF: verify the impulse normalizations and nu²=3omega², ensure no unsupported identification of the 1+1 massless Green with exclusively-null wavefront amplitude, and verify the tensor spatial-mode resolvent cannot automatically equal open q2 T_q. Preserve historic entries.
