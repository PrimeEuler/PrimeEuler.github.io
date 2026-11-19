# Cone Derivation Ledger v15.1194 — Full pressure-corrected Maxwell scalar source produces a nonzero gauge-invariant electric Weyl particular response

**Date:** 2026-11-18 US Eastern. **Track:** Gravity/Cone. **Status:** [D] exact Fourier null Maxwell Ward compatibility, pressure-corrected scalar forcing and particular displacement, Bardeen-potential/electric-Weyl reconstruction and sample nonzero phase-matched Weyl; [C] source convention, infinite-duration traveling test-field wave and selected particular (not uniquely retarded) metric response; [N] no secular log-time resonance for the specified redshifting source; [N] no new quarter-grid coupling or Cone-minus-matched-Einstein–Maxwell–same-solid residual; [O] fully sourced scalar E-shear/metric constraint, causal switched/compact source, full local electric Riemann including Ricci, boundary/initial conditions and physical detector. **Live HEAD immediately before write:** f06ae24cfc3b29c1e3959c97a0e1544c1ec921d0. Target path v15.1194 collision-free; strictly additive, preserved all certified Suzuki/Lane A, Audit, Sandbox, Muse and frozen K4 files.

## Historical redundancy and a necessary correction
The exact scalar P dynamical equation, source trace/pressure Ward, gauge-independent scalar Bardeen potentials and electric Weyl were already established in **v15.728–729**, with a physical canonical spectator example in v15.750, full local electric Riemann in v15.787–788 and the **compact-Maxwell initial-slice** scalar/vector ADM constraint completion in Sandbox **v15.1159**. This gate is **not** claiming the first Maxwell-sourced curvature or a new gravitational Weyl formula. The specific addition is an **analytic time-dependent traveling Maxwell null-harmonic particular solution** using the new coasting scalar log-time solution v15.1190 and phase-match v15.1192, with its *explicit* Weyl transfer at the matched mode.

Importantly, **v15.1193's derivational description is incomplete:** it treated the new direct spatial-metric `J_psi psi` source as changing only the psi Ward equation, while retaining the **lapse/shift-only** physical P forcing formula from v15.713. The correct **full spatial-stress/pressure-corrected** P equation is that of v15.728–729:
**Pddot+3Pdot/tau+[8eta_s(1+k²)−3k²]P/(3tau²)=3sqrt3 J_psi/(2k²tau³)−9(tau dot J_B+J_B)/(2k⁴tau³)**.
The new J_psi term is indispensable to the correct method. For this specific null Maxwell harmonic the two terms happen to simplify to the **same net forcing** claimed numerically in v15.1193; preserving that correct net value does NOT validate omission of the direct term. This ledger is an additive method correction; no historic files overwritten. Audit should prioritize the sign/relative Fourier convention.

## Gate 1136 — full constrained scalar null-Maxwell source
On coasting a(tau)=tau/sqrt3 at κC=1, k>0, define w=sqrt3 k and the positive-frequency analytic Fourier harmonic
**J_Phi=J_psi=J(tau)=J0 tau^(−1−iw)**,
**J_B=+i k J(tau)**,
the same conventional complex-longitudinal source assignment as v15.1193, with the real field obtained by including its conjugate −k harmonic. Then the exact traceful stress Ward
**tau dot J_Phi+sqrt3 J_B+J_psi=0**
holds, since tau dot J=−(1+iw)J.

Evaluate the *correct* full v15.728 scalar forcing:
**3sqrt3 J_psi/(2k²tau³) −9(tau dot J_B+J_B)/(2k⁴tau³)**.
Because **tau dot J_B+J_B=sqrt3 k² J**, the two pieces are **(+3sqrt3/2−9sqrt3/2)J/(k²tau³)**, hence
**forcing=−3sqrt3 J0 tau^(−4−iw)/k²**.
This agrees with v15.1193's final RHS only after applying the pressure-corrected P equation, not its earlier incomplete explanation. The comoving zero Fourier mean of an actual sinusoidal Maxwell wave and physical tensor/electrode boundaries are not captured by this single traveling k>0 harmonic.

## Gate 1137 — exact eternal-source particular solution and phase-match non-pole
With **nu_S²=(8eta_s−3)(1+k²)/3**, define
**D=(−1−iw)²+nu_S²**.
For eta_s in the strict stable window and k>0, D cannot vanish at the proposed phase match w=nu_S (then D=1+2iw, nonzero). In fact D cannot vanish at any positive real k with real eta_s, as Im(D)=2w>0. The exact source-driven particular solution with no *added* homogeneous mode is
**P_part(tau)=−[3sqrt3 J0/(k²D)]tau^(−2−iw)**,
which directly solves the full pressure-corrected forced scalar equation. The complete family adds arbitrary free Cauchy data/homogeneous solutions ∝tau^(−1±i nu_S), and a causal retarded wave with finite-time turn-on does not equal this eternal particular alone. The actual physical Maxwell stress is test-field order and drives an ordinary K4/GR+solid response.

## Gate 1138 — gauge-invariant electric Weyl amplitude in closed form
Use the **previously independently derived** v15.729 traceful Bardeen potentials
**Phi_N=[tau²Pddot+2tau Pdot]/[3(1+k²)]+sqrt3(J_Phi+J_psi)/[2tau(1+k²)]−3 dot J_B/[2k²(1+k²)]**,
**Psi_N=[k²P−tau Pdot]/[3(1+k²)]+sqrt3 J_Phi/[2tau(1+k²)]+3J_B/[2k²tau(1+k²)]**.
For the real physical coasting metric a²=tau²/3, the scalar electric Weyl STF is
**E_ij^W=W_S(tau)[khat_i khat_j−delta_ij/3]**,
**W_S=k²(Phi_N+Psi_N)/(2a²)**.
Substituting the complete Maxwell sources and the exact P_part yields the new closed transfer:
**W_S(tau)=J0 tau^(−4−iw) C_W(eta_s,k)**,
**C_W=9[i(2eta_s−3)k−sqrt3]/[4eta_s(1+k²)−6k²+3i sqrt3 k]**.
The real physical mode is the real part after conjugate Fourier pairing. Its STF shape has squared Frobenius norm (2/3)|W_S|² for a real physical amplitude. It is **generically nonzero** for all real eta_s in the stable interval and k>0: its numerator has nonvanishing real part −9sqrt3 and denominator has nonvanishing imaginary part 3sqrt3 k. This is a physically meaningful **gauge-invariant curvature sector**, not by itself the complete local geodesic-deviation tidal tensor: full Riemann includes Ricci and background/observer/boundary details. Compare prior v15.787–788 precisely.

On the v15.1192 necessary Maxwell–scalar phase-match **k²=(8eta_s−3)/[4(3−2eta_s)]**, for the illustrative eta_s=3/4 one has k²=1/2 and
**C_W≈−3.7115374447904514 + 2.727411870290969 i**.
This is a **dimensionless response coefficient normalized by the chosen source coefficient J0**, NOT a source-independent physical coupling constant or nonzero novel residual. The full Weyl response decays as tau^(−4), while the scalar displacement particular decays as tau^(−2); there is no secular log-time gain.

## Gate 1139 — status of physical discrimination
This calculation *does* provide a specified nonzero scalar electric-Weyl curvature (the source-to-curvature stage) for the traveling Maxwell harmonic in the same exact K4 EH+solid action. The same action is **identical** to ordinary Einstein–Maxwell plus that relativistic solid, and therefore the matched source/initial-condition/detector subtraction remains exactly zero. It does not select the previously proposed q=2 quarter hyperboloid Q=1/16 as a physical gravitational carrier, does not equate an SU2 transition amplitude with physical photon momentum and does not derive G or a new dimensionless observable.

**Missing for a complete physical detector:** a source with finite causal turn-on or compact support, its zero Fourier/longitudinal sectors and all Maxwell equations and constraints; the residual spatial-shear (E) Einstein equation/Ward identities under the gauge E=0; complete lapse/shift and all source-compatible initial conditions; then the **full orthonormal electric Riemann R_0i0j** and finite-arm EM probe (not only Weyl). Sandbox v15.1159 is the initial-slice Maxwell-completion benchmark, while v15.788 is the full-Riemann canonical-spectator comparator. Any candidate quarter-mesh modification must be explicitly derived from a physical Lagrangian, coupled before constraint elimination and rechecked against exact Maxwell gauge invariance.

**Reproducer:** `research-notes/k4_null_maxwell_scalar_weyl_particular_v15_1194.py`, additive SHA **f06ae24cfc3b29c1e3959c97a0e1544c1ec921d0**. Independently equivalent local SymPy run PASS for full traceful scalar P forcing, exact driven P(tau), Bardeen potentials, compact closed W_S, sample eta=3/4,k²=1/2 and nonzero transfer. The exact GitHub-transcribed script has not yet been independently byte-verified/executed by Audit; no legacy files modified.

**AUDIT HANDOFF:** prioritize correcting v15.1193's missing traceful-force derivation, independently check source J_B complex Fourier sign against archived real sine/cos mode, the full metric/shear Ward, source pressure J_psi = J_Phi for aligned null radiation, the closed Weyl transfer sign/normalization and real-field pairing, and the distinction between Maxwell-sourced Weyl versus full Fermi electric Riemann. Do not upgrade the analytic particular solution to a unique retarded boundary-driven observable. **NEXT:** complete the sourced Maxwell scalar response to full electric Riemann with valid finite-past source and gauge/constraint-consistent data, then compare matched standard Einstein+identical solid. The physical q2 boost carrier remains a separate unresolved hypothesis.
