# Cone Derivation Ledger v15.1190 — Full sourced-from-archive K4 scalar canonical normalization, boundary-only metric scalar, and exact logarithmic-time stability

**Date:** 2026-11-18 Eastern. **Track:** Gravity/Cone. **Status:** [D] full exact original v14.935 ADM matter/EH/lapse-shift scalar action regenerated from archived scripts in isolated temporary directory; [D] source-free metric scalar psi contributes only a total derivative on exact coasting and has identically vanishing Euler equation, consistent with **prior** v15.713 / independently audited v15.718; [D] exact scalar P kinetic prefactor, mixed term, canonical frequency and logarithmic-time oscillation index; [D] same instantaneous sigma=-H/2 as vector and scalar critical factorization; [N] no quarter-mesh gravitational boost, physical mass-shell or EM–G coupling; [O] gauge-invariant sourced physical detector response with an independently selected quarter-sector operator. **Immediately prewrite HEAD:** fa2373b0c62a1f33f6b734133c0a9d178340074e. Target v15.1190 checked absent; strictly additive-only, preserve certified Suzuki, Lane A, Audit, Sandbox and original archive.

## Historical priority and distinction
This gate follows v15.1189's deliberately conditional scalar Hessian test and v15.1188's complete vector canonical normalizer. The K4 action itself is frozen v14.935:
**S=∫√−g[R/(2κ)−C b^(2/3)(1+η_s J)] d⁴x**, on a(tau)=tau/sqrt3 and κC=1. We reconstructed **the literal original archived source modules** `payloads/k4_full_svt_v14_935/matter_sector.py`, `eh_scalar.py`, `assemble.py` into a local isolated scratch copy and ran all three, regenerating `scalar_reduced.pkl`. There is no independent new fundamental field or coupling in these equations.

**Nonredundancy check:** v15.713 **already discovered** the exact source-free psi Euler identity E_psi=0, and the direct physical P equation **already confirmed** its frequency and friction; External Audit v15.718 independently reproduced these findings and corrected the older false description of a Python exception: the archived numeric script continues on tiny floating-point residues, but its formal psi=alpha P division remains undefined 0/0. These findings are NOT claimed as new. The **new work here** is the explicit boundary primitive eliminating psi from the action, the full quadratic P canonical Hessian and mixed term after that elimination, and the exact log-time normal form/squeeze matched to v15.1188 vector. Do not describe the original source-free psi state as uniquely slaved.

## Gate 1124 — exact metric-scalar boundary term
Put κ=C=1, a=tau/sqrt3, adot=1/sqrt3, comoving scalar Fourier k>0, and use the archived original `psi,P` variables in the scalar action **after** solving lapse and metric shift constraints. Direct variation confirms **δS/δpsi=0 identically**, as independently established at v15.713. More strongly, define the time-dependent boundary primitive
**F_boundary=−[2sqrt3 k² tau²/9] [psi P−(3/2)psi²]**.
Subtract **dF_boundary/dtau** from the full reduced scalar Lagrangian. The result is *exactly independent of psi and psidot*, with no equations of motion discarded. The source-free psi dependence was a total time derivative and is not a unique auxiliary `psi=alpha P` constraint. Its interpretation is sensitive to the source/boundary conditions and cannot be extrapolated to the sourced system without the v15.713 Ward-compatible external stress. For this source-free canonical derivation the boundary term changes the canonical momenta by a time-dependent canonical transformation but does not change the Euler equations.

## Gate 1125 — closed scalar physical action and scalar kinetic/phase-space connection
The exact one-field scalar Lagrangian after the boundary removal is
**L_P= (K/2) Pdot² + M P Pdot −(V/2)P²**
with
**K=2sqrt3 k⁴ tau³/[27(1+k²)]**,
**M=2sqrt3 k⁴ tau²/[27(1+k²)]**,
**V=2sqrt3 k⁴ tau [8η_s(1+k²)−3k²−6]/[81(1+k²)]**.
For the corresponding un-normalized `L=Kraw Pdot² − Vraw P²` convention of v15.1188, the distinction between the *coefficient* and `∂²L/∂Pdot²` matters: the above K is the **Hessian**, not the Pdot² monomial coefficient. Note K>0 when k>0. The real P equation from this action is exactly
**K Pddot+Kdot Pdot+(V+Mdot)P=0**.
The mixed-term contribution **+Mdot** is necessary; omitting it gives the wrong scalar mode frequency. Direct exact simplification yields
**Pddot+(3/tau)Pdot+[(8η_s(1+k²)−3k²)/(3tau²)]P=0**,
reproducing the previously audited v15.713 P equation and v14.935/15.706 frozen-dispersion formula. The source-free scalar Hessian at general κC=1 before normalization is **K_PP=2 C a³ k⁴/[3(κC+k²)]** in the archived real Fourier normalization. Thus the scalar's constraint dressing **k⁴/(κC+k²)** is time-independent at fixed comoving k, while the complete K scales as **a³**, just like the vector sector, but with a *different* k-dependent prefactor. This proves the v15.1189 conditional kinetic-weight expectation for this actual scalar field.

## Gate 1126 — canonical log-time scalar mode and critical coupling
Since K∝tau³, choose **u=sqrt(K)P**. Dropping a total time derivative in canonical variables yields
**uddot+Omega_S² u=0**,
**Omega_S²= [(8η_s(1+k²)−3k²)/3−3/4]/tau²**.
Its instantaneous canonical annihilation variable has mixing coefficient **sigma=Omegadot/(2Omega)=−1/(2tau)=−H/2** (Omega>0 in the open stable range). This is a mathematically exact instantaneous-coordinate squeeze and need not represent a physical Lorentz boost or particle creation.

Let **s=ln tau** and **u(tau)=sqrt(tau) z_S(s)**. The exact scalar equation becomes
**z_S''(s)+nu_S² z_S(s)=0**, with
**nu_S²=[8η_s(1+k²)−3k²]/3−1 = [(8η_s−3)(1+k²)]/3**.
This factorization is the strongest clean result of this gate: for **η_s>3/8** and k>0, nu_S²>0 (oscillatory in log time); at the precise threshold **η_s=3/8**, nu_S²=0 and **P(tau)=tau^(−1)[A+B ln(tau)]** (logarithmic marginal behavior), not a generic oscillatory solution. Below 3/8 log-time modes grow/decay as powers of tau, matching the known scalar gradient instability direction at sufficiently high k.

The apparent contrast with the old v14.935 **locally frozen** τ0 characteristic roots λ=(-3±sqrt5)H/2 at η=3/8 is not an inconsistency: those roots freeze the time-dependent coefficients into a constant-coefficient problem. The globally exact coasting equation has time-dependent H and yields an Euler/Cauchy power-law double root at the threshold. One must not use the frozen eigenvalues as exact global evolution exponents.

## Gate 1127 — compare vector, scalar and physical boost/matched-control
The exact vector result v15.1188 has **nu_V²=8η_s/3+2η_s k²−1**; this scalar has **nu_S²=(8η_s−3)(1+k²)/3**. Their difference is
**nu_V²−nu_S²=(1−2η_s/3)k²**,
the same ordinary solid-elastic dispersion splitting as v15.706. Thus there are *different* log-time oscillation frequencies even though both instantaneous squeezing coefficients equal −H/2. This is NOT an independently fixed q2 quarter hyperboloid level; both dynamics follow the same frozen Einstein–Hilbert+solid action and are shared with an identically matched ordinary GR+solid comparator. The source/medium matched dimensionless residual remains **zero**. A hyperbolic Bogoliubov *coordinate mixing* must not be equated with a physical boost along the q2 representation-space Q=1/16 sheet; an actual source/connection matching remains open.

## Exact reproducibility and Audit handoff
The additive **self-contained archive-runner** `research-notes/k4_scalar_exact_canonical_boundary_logtime_v15_1190.py` (SHA **fa2373b0c62a1f33f6b734133c0a9d178340074e**) copies the **original published archived** `matter_sector.py,eh_scalar.py,assemble.py` into a temporary directory, executes them verbatim, reads the regenerated full reduced scalar action, substitutes the exact coasting background, verifies **E_psi=0**, removes the explicit boundary primitive, asserts psi-absence in the resulting L, and verifies exact K,M,V, P Euler coefficients, nu² factorization, positivity spot checks and sigma=-H/2. Executed locally against recreated original-module byte-equivalent source flow: **PASS**. No pre-existing source modified or pickle written in the repository.

**AUDIT HANDOFF:** verify archived-source regeneration and source vs local reconstructed script equality, formula for F_boundary and no missed psi terms, exact canonical Hessian K and mixed M, EL restoring V+Mdot sign, scalar critical η=3/8 log-time double root, distinction from frozen spectral eigenvalues, vector-vs-scalar nu² difference, physical interpretation of instantaneous squeezing and absence of quarter-specific coupling. The already audited v15.713/v15.718 psi-null result must be credited and not falsely presented as a new defect. **NEXT:** derive a sourced, gauge-invariant EM stress response to this *exact canonical mode* and test whether a genuine q2/quarter-grid operator changes the dimensionless observable relative to the Einstein–Maxwell+same-solid control; absent an action-selected quarter operator, report the remaining no-new-physics null.
