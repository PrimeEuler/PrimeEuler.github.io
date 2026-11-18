# Cone Derivation Ledger v15.1188 — Exact K4 vector kinetic reduction and logarithmic-time canonical flow: squeeze without a new quarter boost

**Date:** 2026-11-18 Eastern. **Lane:** Gravity/Cone. **Status:** [D] direct reduced-vector-action derivation using the archived v14.935 ADM+solid quadratic vector expressions; [D] exact mode kinetic factor a³ times a k-dependent constant and exact K4 vector dispersion; [D] global coasting vector canonical equation, instantaneous squeezing coefficient -H/2 and exact oscillatory evolution in log cosmic time; [N] not an intrinsically gravitational q=2 hyperboloid boost, a measured G-free coupling or a distinct physical effect from Einstein gravity with identical solid. **Immediately prewrite live HEAD:** f405924c9fc19302cf03d17ba6352148d33b4478. Slot v15.1188 unused; additive-only, protected Lane A/Suzuki, Audit, Sandbox/Muse and certified objects unchanged.

## Parents, problem, and scope
v15.1184–1186 distinguish a Schwinger EM transition at fixed diameter from abstract SO+(1,1) quarter hyperboloid boosts, and show a finite quarter carrier cannot realize a continuous positive-factor dilation internally. v15.1187 gives an exact stable-oscillator/real-boost generator mismatch and a *conditional* canonical squeezing rate sigma=−H/2 from an assumed globally valid qddot+3H qdot+omega² q=0. **This gate removes that extra assumption for the physically propagating K4 transverse vector**, by deriving its full reduced quadratic action from the frozen K4 solid and ADM vector terms in the already certified v14.935 payload (`payloads/k4_full_svt_v14_935/vector_sector.py`). It does *not* redo the coupled scalar kinetic reduction and does not introduce a quarter-sector gravity field. Use cosmic coasting time tau as in v14.935, not conformal time. Nonzero comoving Fourier k throughout.

## Gate 1117 — reconstruct the archived vector action and eliminate the metric shift
The quadratic transverse physical solid displacement f(tau) and auxiliary metric shift B have, for one polarization with one real Fourier k, the real-mode quadratic coefficients (common positive Fourier averaging normalization immaterial)
**L₂ = (C a³/3) ḟ² −(2Ca²/3) B ḟ + [−Ca/6+3a ȧ²/(2κ)+a k²/(4κ)] B² −(2Ca η_s k²/9) f².**
This is the direct second-order expansion of the solid B^IJ and Einstein–Hilbert shift sector used in the archived v14.935 vector script (its printed expressions use the same metric-sign convention). On the exact background **ȧ²=κC/3**, the B² coefficient becomes **aC/3+a k²/(4κ)**; the shift constraint is algebraic:
**B_star = 4Ca κ ḟ/(4κC+3k²)**.
Substitute before varying f. The reduced action is exactly
**L_red= K_f(a,k) ḟ² − V_f(a,k) f²,**
**K_f=Ca³k²/(4κC+3k²), V_f=2Ca η_s k²/9**.
K_f>0 for C,a,k,κ>0 with k>0. The k→0 factor K_f→0 reflects the homogeneous vector constraint/zero-mode caveat, so do not treat k=0 as a propagating oscillator. Crucially at fixed *comoving* k the entire time-dependence of K_f is **a³**; its constraint dressing **k²/(4κC+3k²)** is exactly time-independent on the frozen coasting background. Therefore the reduced vector Euler–Lagrange equation is **f̈+3H ḟ+(V_f/K_f)f=0** with no extra connection/derivative term omitted.

## Gate 1118 — exact dispersion, canonical normalization and instantaneous mixing
Take (H=ȧ/a) and (a(tau)=tau/sqrt3) at **κC=1**. The reduced ratio is
**omega_V²=V_f/K_f = [2η_s(4κC+3k²)]/(9 a²) = (8η_s/3)H²+(2η_s/3)(k/a)²**,
identically matching v14.935 without freezing tau. This is stronger than borrowing the local frozen eigenvalues as a global Ansatz. Normalize the real canonical oscillator as **u=sqrt(2K_f) f = const a^(3/2) f**, whose canonical kinetic term is (1/2)u̇². Its action, after a total time derivative, has
**ü+Omega_V² u=0, Omega_V²=omega_V²−(3/2)Ḣ−(9/4)H²**.
With H=1/tau,
**Omega_V²=[8η_s/3 +2η_s k²−3/4]/tau² = Lambda²/tau²**.
For eta_s>3/8 and k>0, Lambda²>1/4, so Omega_V is positive and the instantaneous annihilation coordinate **alpha=(sqrt(Omega)u+i p/sqrt(Omega))/sqrt2**, p=u̇, obeys
**alphȧ=−i Omega alpha + [Omegȧ/(2Omega)]alpha* =−i Omega alpha−(H/2)alpha***.
Thus v15.1187's sigma=−H/2 is **indeed derived from the actual coupled K4 vector action**, not from an arbitrary gap parameter. It is also the standard instantaneous normalization term for a frequency Omega∝1/tau and does not alone establish net particle production or any physical Lorentz boost.

## Gate 1119 — exact normal modes in log time; physical boost is not supplied
Define log time **s=ln tau**, and **u(tau)=sqrt(tau) z(s)**. Then the exact equation becomes
**d²z/ds² + nu² z=0**, where
**nu²=Lambda²−1/4 =8η_s/3+2η_s k²−1**.
For all eta_s in the open stable window and k>0, **nu²>0** (at eta_s=3/8 and k=0 one finds the limiting marginal nu²=0 but k=0 is not a propagating mode). Thus the full normalized coasting evolution is **oscillatory in logarithmic time**, not an unbounded hyperbolic stretch. With (w=dz/ds), the exact transfer at (Delta s=ln(tau_2/tau_1)) is
**[[cos(nu Delta s), sin(nu Delta s)/nu], [−nu sin(nu Delta s), cos(nu Delta s)]]**,
unit determinant and |tr|≤2. For eta_s=3/4,k=1, **nu²=5/2**, nu=sqrt(10)/2. A time-dependent canonical transformation can exhibit Bogoliubov mixing in the instantaneous oscillator basis, but the complete log-time normal mode is elliptic, not a physical SO+(1,1) rapidity displacement of factor coordinate operators. There is no q=2 level 1/16 in the vector Lagrangian or its normal-mode solution.

## Gate 1120 — matched action comparator and a precise next gate
The underlying theory remains the *frozen* Einstein–Hilbert+isotropic solid. Another treatment of Einstein gravity with the **same material action, background, parameters, initial state and detector** yields exactly this same vector action and log-time transfer. Consequently **the source-and-medium matched residual is zero**. The quarter-grid mathematical placement of boost orbits remains optional, not a selected physical momentum cone. The result makes a concrete route for the next step: (a) calculate whether the actual coupled scalar time-dependent reduced kinetic factor has the same a³ scaling, separately from vector; (b) if a proposed gravitational quarter-sector interaction is supplied, couple it to an electromagnetic source gauge-invariantly and derive a dimensionless difference against this exact vector transfer. The scalar is potentially different because its lapse/shift dressing can carry time-varying k/a dependence; **do not extrapolate the vector sigma result to scalar without the reduced action**.

**Reproducer:** `research-notes/k4_vector_exact_canonical_logtime_v15_1188.py`, additive SHA **f405924c9fc19302cf03d17ba6352148d33b4478**. Equivalent local complete SymPy execution PASS for constraint B_star, K_f and V_f, exact archived m² and c_T², full coasting Omega² and log-time nu², and example log-time transfer. No figure or historical edits.

**AUDIT HANDOFF:** independently expand archived vector quadratic density including EH shift and B^IJ, verify factors from real-mode Fourier averaging, constraint B_star, K_f=a³×constant k dressing, V_f, exactly global friction 3H, canonical total-derivative removal and Omega², positive nu² stable window and log-time evolution. Check interpretation of cosmic versus conformal time, k→0 degeneracy, instantaneous squeeze vs net physical boost/particle production, comparison with standard Einstein+same solid, and no unearned quarter-grid coupling.

**Next:** exact reduced coupled scalar canonical action and time-dependent prefactor from v14.935 assemble.py/scalar_statespace.py, including eliminating the algebraic psi field before and after taking tau derivatives (constraint dressing may be tau dependent). Then test whether the scalar has a different intrinsic squeezing coefficient that could be a source of *dimensionless conventional* mode-ratio checks, still respecting the matched ordinary relativistic-solid control.
