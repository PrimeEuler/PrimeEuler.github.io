# Cone Derivation Ledger v15.1083 — Conformal-Maxwell sourced K4 tensor and electric Weyl time jet

**Date:** 2026-11-17 Eastern. **Lane:** Gravity/Cone. **Status:** [D] physical conformal-power normalization for source-free Maxwell stress on coasting K4 and exact *tensor-sector* electric Weyl initial-time series; [N] no complete ADM constrained metric or detector-local full Weyl, no novel Cone-only tidal law. **Live HEAD immediately before ledger write:** 1428dc31715d43accce00c5e572b7dd2d386a43a (canonical reproducer). All changes additive; earlier certified files, Suzuki, Audit, Muse, Sandbox remain untouched.

## Concurrent version collision, resolved by precedence
Sandbox published **canonical v15.1082** `Ledger v15.1082 (Sandbox): charge at the seat`, commit **dde35b8f2ab5603cdce0cea8c86308f7e8cb77a1**, *before* Gravity uploaded the provisional file `research-notes/k4_compact_maxwell_coasting_weyl_v15_1082.py` at commit **0c0b1b1748c282189b15b39b4d4d1860db90dab3**. Thus **Sandbox retains v15.1082** and the provisional gravity-named reproducer is a historical, superseded artifact; no rename, overwrite or deletion. The substantive gravity result is **v15.1083**, with canonical equivalent reproducer `research-notes/k4_compact_maxwell_coasting_weyl_v15_1083.py` at commit **1428dc31715d43accce00c5e572b7dd2d386a43a**. This entry explicitly resolves the collision and requests independent Audit.

## Previously established
The frozen K4 EH+elastic-solid model and tensor equation are v14.928/935, retarded proper-time/source-to-tensor Weyl v15.722, conformal coasting Green function v15.1061–1062. Gravity v15.1078 constructed compact free-Maxwell Cauchy data with transverse TT+ Fourier stress P(q,0); v15.1080 differentiated the integrated stress twice; v15.1081 derived nonzero-q Fourier stress P(q,eta)=P0(q)+P2(q)eta²/2+O(eta⁴) in conformal flat Maxwell time, where P2=Pdd. The latest independently completed External Audit Round 590, canonical v15.1079, confirmed v15.1076–1078. v15.1080–1081 await independent Audit. This gate corrects the **previously conditional constant forcing prefactor** to the physical conformal scaling; it does NOT introduce a new matter coupling.

## Gate 905 — source normalization from the real Maxwell field
Write the spatially flat coasting physical metric ds²=a(eta)²(-deta²+dx²+dy²+dz²), with a(eta)=a0 exp(Hc eta), Hc=1/sqrt(3) under kappa C=1 and arbitrary positive a0. The four-dimensional source-free Maxwell action is conformally invariant. For the source-free compact Maxwell field evolved in conformal Minkowski coordinates, the physical orthonormal electromagnetic anisotropic stress obeys
Pi_plus^phys(q,eta)=a(eta)^(-4) P(q,eta).
Using the standard Einstein TT tensor normalization (metric h_xx=h_plus, h_yy=-h_plus), with kappa=8pi G in ordinary units, the *tensor-projected* sourced equation is
h''+2Hc h'+[q²+8zeta/9]h =2 kappa a² Pi_plus^phys=2kappa a^-2 P(q,eta).
This assumes the same linear EH+K4 tensor action and that the source is treated as a perturbative Maxwell test field; gravity/Maxwell backreaction beyond leading order, baseline scale a and matter solid constraints are not solved. The source sign convention is consistent with the chosen plus metric and physical stress convention; reversals of gravitational metric/TT conventions change displayed component signs, not its status as sourced curvature.

For psi=a h, the equation is
psi''+[q²+(8zeta-3)/9]psi=2kappa a^-1 P(q,eta).
Therefore conformal canonical forcing has factor a^-1, *not constant* as used in v15.1081's explicitly conditional time jet.

## Gate 906 — electric Weyl initial-time curvature from the same tensor mode
Use the already-established orthonormal plus-tensor electric Weyl convention from v15.722/750:
W_plus = [tau² ddot h+tau dot h-3q² h]/(12 a²)
= [h''-q² h]/(4a²),
where eta=sqrt(3)ln(tau/tau0), primes are conformal time and the displayed Weyl quantity is the **tensor-sector electric Weyl contribution**, not all scalar/vector/constraint-sourced curvature of the compact matter system. The FLRW background Weyl vanishes; the linear tensor Weyl contribution is gauge invariant within this perturbative decomposition.

Let P(q,eta)=P0+P2 eta²/2+O(eta⁴), P'(0)=0, and zero tensor Cauchy data h(0)=h'(0)=0. Define Hc=1/sqrt(3), M=8zeta/9, a0=a(0). The sourced equation fixes
h(eta)= (kappa P0/a0²) eta²
- (4Hc kappa P0/(3a0²)) eta³
+ kappa[12Hc²P0-(q²+M)P0+P2]/(12a0²) eta⁴
+O(eta⁵).
Substituting into W_plus gives
W_plus(q,eta)=
(kappa/a0⁴){ P0/2 -3Hc P0 eta
+[32Hc²P0-MP0-2q²P0+P2]eta²/4 }
+O(eta³).
Therefore W_plus(q,0)=kappa P0/(2a0⁴), and W_plus'(q,0)=-3Hc kappa P0/a0⁴, while the true Maxwell Fourier source curvature P2 first enters at eta². These are exact coefficient identities for the stated **TT subproblem with zero tensor data** and physical conformal Maxwell scaling. In particular the initial Weyl term depends on a0^-4, consistent with a physical source stress a0^-4.

The resulting instantaneous TT Weyl component in Fourier space is not by itself a fully gauge-complete, detector-local physical tidal effect: the full electromagnetic stress also sources scalar and vector constraints, and their electric-Weyl components are generally nonzero. A physical source-to-observable prediction must include them and then reconstruct the local orthonormal curvature for a detector. Nor does the initial value establish a globally retarded isolated-source solution; the initial Maxwell stress is nonzero on the initial slice while the tensor displacement/velocity are set to zero, and the complete constraint initial data must be solved separately.

## Gate 907 — comparison and physical negatives
For any independently specified source P and K4 background, a matched comparator using Einstein gravity with the *same* isotropic elastic solid, same zeta, same boundary/initial data and Maxwell action has the same tensor Weyl transfer, so the matched subtraction remains exactly zero. The nonzero W_plus above is an ordinary sourced Einstein–elastic tensor response, not evidence for an extra X cone, quarter mesh source or predicted G. It contains kappa explicitly; no dimensionless gravitational amplitude follows without the actual electromagnetic source scale and the independently measured gravitational coupling. The q here is spatial Fourier wavenumber, not the q=2 arithmetic mesh.

## Gate 908 — exact reproducibility / Audit handoff
Canonical exact SymPy reproducer `research-notes/k4_compact_maxwell_coasting_weyl_v15_1083.py`, commit 1428dc31715d43accce00c5e572b7dd2d386a43a, was independently run locally (same algebra as provisional v15.1082) to PASS checks for source factor 2kappa a^-2, canonical source 2kappa a^-1, tensor h coefficients through eta⁴, W_plus through eta², and coasting mass (8zeta-3)/9. The historical provisional script at 0c0b1b1 remains unchanged; this ledger and canonical script control the gravity v15.1083 result.

**NEXT:** solve source-first scalar/vector ADM constraints with the full Fourier-space Tmunu for the compact Maxwell wave packet; reconstruct the complete electric Weyl from these and tensor pieces for nonzero spatial q; compute a gauge-invariant local tidal/timing signal and compare matched Einstein+solid versus Cone proposal. No new force, G or source-independent quarter-ladder operator has been derived.

**AUDIT HANDOFF:** independently check version precedence (Sandbox v15.1082 vs provisional Gravity v15.1082); Maxwell a^-4 physical stress, Einstein factor 2kappa TT source, conformal factor in psi forcing, Weyl sign/convention against archived v15.722/750, time-jet coefficients and explicit full-ADM limitation.
