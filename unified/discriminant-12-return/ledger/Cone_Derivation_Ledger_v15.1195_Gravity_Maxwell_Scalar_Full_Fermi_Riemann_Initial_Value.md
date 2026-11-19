# Cone Derivation Ledger v15.1195 — Analytic traveling-Maxwell scalar full Fermi Riemann and causal-initial-value boundary comparator

**Date:** 2026-11-18 US Eastern. **Track:** Gravity/Cone. **Status:** [D] exact scalar electric Riemann, tracefree electric Riemann, Ricci completion and gauge-invariant particular response reconstructed from v15.1194 source plus previously audited v15.729 and v15.787 metric identities; [D] exact Green solution for zero propagating scalar data at an initial Cauchy slice with the physical Maxwell wave already present; [N] no source-free-past retarded local apparatus and no q2 quarter-grid physical coupling or matched-Einstein+same-solid residual; [O] fully gauge- and boundary-consistent electromagnetic source including zero Fourier modes, scalar spatial-shear Einstein equation and actual finite detector transfer. **Immediately prewrite live HEAD:** 0b6be88be25d8055dbd0f96dfb92879d2067aa87. Target v15.1195 absent; additive only; original Suzuki/Lane A, Audit, Sandbox, Muse, K4 archive untouched.

## Precedent and collision/repro controls
v15.1194 derived the pressure-corrected null-Maxwell traveling Fourier harmonic and analytic scalar **electric Weyl**. The *full* Fermi electric Riemann metric calculation and its distinction from Weyl are historical v15.787, v15.788; Audit v15.789 found an original 5×5 matrix shape bug in the v15.787 producer, fixed **additively** in v15.792. Use the audited **mathematical** metric identities, not the defective original unpatched reproducer. Sandbox v15.1159 independently obtained a nonzero initial scalar Weyl for a *different compact Maxwell wavepacket* in standard Einstein gravity; do not claim that nonzero Maxwell scalar curvature is novel. This gate's narrow new contribution is plugging **the specific time-dependent traveling Maxwell harmonic of v15.1194** into the full **electric Riemann** and supplying an exactly checked **initial-value Green response**.

## Gate 1140 — reproduce pressure-corrected metric with exact Maxwell scalar source
Work in the v15.1194 convention: cosmic tau>0, scale factor a=tau/sqrt3, k>0, solid parameter η_s in 3/8<η_s≤3/2, κC=1, w=sqrt3 k, and complex positive-traveling stress harmonic plus its physical conjugate. Define
**J_Phi=J_psi=J0 tau^(−1−iw), J_B=+i k J_Phi,**
which obey **tau J_Phi_dot+sqrt3 J_B+J_psi=0**.
The correct **full pressure-corrected** propagating scalar source v15.728–729 is **F=−3sqrt3 J0 tau^(−4−iw)/k²**. With
**nu_S²=(8η_s−3)(1+k²)/3, D=(−1−iw)²+nu_S²**, the eternal-source particular field is
**P_part=−3sqrt3 J0 tau^(−2−iw)/(k² D)**,
as checked at v15.1194. The complete traceful gauge-invariant metric potentials from v15.729 are
**Phi_N=[tau²P_ddot+2tau P_dot]/[3(1+k²)]+sqrt3(J_Phi+J_psi)/[2tau(1+k²)]−3 J_B_dot/[2k²(1+k²)]**,
**Psi_N=[k²P−tau P_dot]/[3(1+k²)]+sqrt3 J_Phi/[2tau(1+k²)]+3J_B/[2k²tau(1+k²)]**.
The source and gauge convention remain conditional on checking the original real Fourier cosine/sine conventions and the remaining scalar shear equation.

## Gate 1141 — full local electric Riemann and Ricci completion
The historical metric-level result v15.787 (signature −+++, flip conventions consistently) for scalar Newtonian-gauge perturbations on the coasting background gives the local Fermi electric matrix
**E_ij=R^i_(0j0)=A(tau)δ_ij−[k² Phi_N/a²] n_i n_j**,
with **A=Psi_N,ddot+2H Psi_N,dot+H Phi_N,dot**, n=khat, H=1/tau. Thus
**E_ij^(STF)=R_S Q_ij, Q_ij=n_i n_j−δ_ij/3, R_S=−k² Phi_N/a²=−3k² Phi_N/tau²**.
The Weyl-only coefficient was **W_S=k²(Phi_N+Psi_N)/(2a²)**. The spatial-Ricci STF coefficient of the *same full metric* is **Ricci_S=k²(3Phi_N+Psi_N)/a²**, and the exact consistency identity is
**R_S=W_S−Ricci_S/2**. It is not legitimate to use W_S by itself as geodesic-deviation acceleration.

Write **Phi_N=J0 tau^(−2−iw) C_Phi**, **Psi_N=J0 tau^(−2−iw) C_Psi**. Exact symbolic reduction yields
**C_Phi=−[4sqrt3 η_s k²−12i η_s k−6sqrt3 k²+27i k+6sqrt3]/[2k²(4η_s(1+k²)−6k²+3sqrt3 i k)]**,
**C_Psi=[4sqrt3 η_s k²+12i η_s k−6sqrt3 k²−9i k−6sqrt3]/[2k²(4η_s(1+k²)−6k²+3sqrt3 i k)]**.
Accordingly
**R_S(tau)=J0 tau^(−4−iw) C_R**, **C_R=−3k² C_Phi**,
while the isotropic trace-tide term is
**A(tau)=J0 tau^(−4−iw)[(−2−iw)(−1−iw) C_Psi+(−2−iw) C_Phi]**.
These expressions supply the full local electric tidal matrix for the *specific particular solution*; physically real coefficients require pairing conjugate Fourier modes. They do not include a finite-arm optical transfer or absolute SI calibration.

At the v15.1192 source/free-mode phase match η_s=3/4, k²=1/2, the numerical complex **dimensionless transfer coefficients normalized by J0 tau^(−4−iw)** are
**Weyl C_W=−3.71153744479045+2.727411870291i**, 
**full Riemann STF C_R=+5.567306167186−0.909137290097i**,
and **isotropic electric Riemann A coefficient ≈−3.58781952996+0.30304576337i**. This demonstrates a difference in complex phase and magnitude between Weyl and full geodesic-deviation channels. For a tracefree gradiometer comparing z and x, **E_zz−E_xx=R_S**, independent of the isotropic component, whereas an individual-arm test responds to both. Matched Einstein–Maxwell plus identical solid necessarily gives exactly the same metric transfer and curvature, so no distinct Cone residual.

## Gate 1142 — a genuine initial-value Green response, not an unphysical free-wave turn-on
Treat a Maxwell Fourier traveling field as **already present** on a Cauchy slice tau0=1. It satisfies the free conformal Maxwell equations for subsequent tau. Impose **zero propagating K4 scalar data** P(1)=Pdot(1)=0, but **do not force the sourced lapse/shift/Bardeen constraint contacts or tidal curvature to zero on that initial slice**. Let s=ln tau, nu=sqrt(nu_S²), and F0=−3sqrt3 J0/k². The exact compatible reduced physical scalar solution with these initial data is
**P_IV(tau)=tau^(−1) F0/D [ exp((−1−iw)s)−cos(nu s)−((−1−iw)/nu)sin(nu s) ]**.
Direct symbolic differentiation verifies z''+nu² z=F0 exp((−1−iw)s), z(0)=z'(0)=0, as well as the original cosmic-time P equation. The denominator D is nonzero for k>0 and real η_s; in the exact phase-match regime D=1+2iw, no resonance pole. The full metric potentials can be computed from **the same** v15.729 pressure-corrected transfer by substituting P_IV and the unchanged physical Maxwell stress sources.

At η_s=3/4,k²=1/2, J0=1, the complex **source-Fourier-normalized** local scalar full-Riemann STF coefficients for the initial-value solution are about
**R_S(tau=1)=+4.330127018922−2.121320343560i**,
**R_S(tau=2)=−0.199234341021−0.189904503357i**.
The initial nonzero curvature is a conventional *constraint/source contact* and is not a claim of radiation propagating from zero past stress. Both the eternal particular solution and this initial-value solution remain single Fourier harmonics in infinite space. A genuinely zero-past-source Maxwell wave switched on in finite time would require charged current/electrode/other electromagnetic source and its full conserved stress, not simply multiplying an otherwise free plane wave by a Heaviside time envelope.

## Gate 1143 — status, comparator and audit
**Positive:** a complete **local scalar electric Riemann matrix** exists for this model harmonic, explicitly including Ricci vs Weyl and a nontrivial stable finite-initial-data solution. **Negative:** the same Einstein–Hilbert+isotropic K4 solid+Maxwell action has been used throughout, so the matched standard model yields identical source, metric and detector curvature; the quarter representation level Q=1/16 and EM spin null cone never enter these field couplings. This is **not** evidence of G-free new gravity or quarter-specific mass shell, nor a complete external finite detector. Existing v15.788 full-Fermi canonical spectator and Sandbox v15.1159 Maxwell initial-slice are independent comparator checks, not sources to overwrite.

**Reproducer:** `research-notes/k4_maxwell_scalar_full_riemann_initial_value_v15_1195.py`, additive SHA **0b6be88be25d8055dbd0f96dfb92879d2067aa87**. Equivalent exact SymPy local computation PASS for pressure-corrected Ward and P forcing, original Weyl coefficient, Bardeen potentials, Ricci completion and full Riemann STF, exact initial-value Green ODE/initial conditions and sample numerical values. Independent committed-source-byte audit remains pending; no protected sources modified.

**AUDIT HANDOFF:** independently verify C_Phi and C_Psi algebra against v15.729, A isotropic electric curvature, tracefree electric Riemann vs Weyl/Ricci identity from audited-corrected v15.787/v15.792, signs and Fourier pairing, J_B orientation, sample transfer values, Maxwell field physical initial constraints and mean-stress missing sector, and no-source-past vs initial-value response distinction. Confirm no extra quarter-sector action is implied. **NEXT:** put a complete finite-support Maxwell Cauchy packet and material wall/current stress into the *existing* ADM sourced constraints and evolve its full local Riemann + finite-arm light readout; separately derive any physical q2 observable directly from a gauge-invariant field action before asserting a nonzero model-vs-matched-GR residual.
