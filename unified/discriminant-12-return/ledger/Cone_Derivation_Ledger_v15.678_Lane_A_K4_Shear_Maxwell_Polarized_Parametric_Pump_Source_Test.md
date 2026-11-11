# Cone Derivation Ledger v15.678 — Gravity lane: anisotropic shear Maxwell pump, polarization response, and K4 source-frequency gate

**Date:** 2026-11-11. **Motivation:** owner's gravity ±1/4 grid pumping EM ±1/2-grid waves at electric antinodes via effective capacitance/impedance. **Parents:** gravity v15.676 (LC pump exact energy, 2ω Floquet threshold, conformal-Maxwell null); K4 elastic-source v14.925–928 and **v14.935 full-SVT return**, with independent η free and tensor mass m_T²=(8η/3)H²; v15.624 EM vs separate gravity Casimir correction. **Status:** [D] exact Maxwell action and polarization mode equations for a specified anisotropic time metric, Floquet monodromy, exact K4 coasting homogeneous tensor mode and source obstruction; [C] externally prescribed shear b(t), comparison with genuine traveling gravitational waves; [O] Cone quarter-grid temporal frequency, physical tensor source, amplitude, phase, novel G-free observable. **Fresh prewrite HEAD:** cde81c7320f9bd949a3874c116228334c61349c5 (additive reproducer), version collision search negative. Suzuki/far-tail and all certified sources untouched.

## Source and model distinctions

**Prescribed shear test metric:** ds²=−dt²+exp(2b(t))dx²+exp(−2b(t))dy²+dz² (c=1). This is *homogeneous, anisotropic Bianchi-I-like*, not automatically a vacuum Einstein solution or a traveling TT gravitational wave. Its volume determinant is −1, and x/y scale factors are reciprocal. It is a deliberately scoped comparator for a *physical oscillatory anisotropy*. By contrast, a purely conformal scalar rescaling cancels from the classical 4D Maxwell action (v15.676) and supplies no such direct pump.

**Existing candidate gravity source:** K4 metric + three-field relativistic elastic solid from v14.928/935. With FLRW a(τ)∝τ and H=1/τ, it has TT action S_T²=(M_Pl²/8)∫a³[γdot_ij²−a^(−2)(∂γ_ij)²−m_T² γ_ij²], m_T²=(8η/3)H², with η in (3/8,3/2] for its previously derived **local linear** stability window. In a homogeneous diagonal, traceless shear γ=diag(2b,−2b,0), trγ²=8b², so S_T²|hom = M_Pl² ∫ a³[bdot²−m_T² b²] per spatial coordinate volume. The background and η are *not* selected from the Cone offset alone. This K4 cosmological source cannot be assumed to yield a locally oscillatory laboratory gravity mode.

## Gate 197 — exact Maxwell shear-polarization reduction

Use electromagnetic potential A=(0,A_x(t,z),A_y(t,z),0), transverse plane Fourier factor exp(ikz), a chosen physical wave model and no external charges. The standard Maxwell action −1/4∫√−g F² reduces to

**L_EM=(1/2)e^(−2b)[Adot_x²−k² A_x²]+(1/2)e^(+2b)[Adot_y²−k² A_y²].**

Thus mode equations are (e^(−2b)Adot_x)dot+k²e^(−2b)A_x=0 and (e^(+2b)Adot_y)dot+k²e^(+2b)A_y=0. With u_x=e^(−b)A_x, u_y=e^(+b)A_y, exact *canonical* equations:

**uddot_x+[k²+bddot−bdot²]u_x=0;**
**uddot_y+[k²−bddot−bdot²]u_y=0.**

The shear pump appears with *opposite linear signs for the two polarizations*, an exact difference from conformal uniform scaling. For an externally prescribed test b(t)=epsilon cos(Ωt), the effective frequencies are k²∓epsilon Ω² cos Ωt−epsilon²Ω²sin²Ωt (sign assignment depends on x/y). This is a genuine parametric Maxwell instability **within the prescribed model**, not a gravity-sector derivation.

## Gate 198 — exact Floquet witness and phase-sensitive quadratures

Using k=1, zero losses and direct 2×2 fundamental monodromy over one pump period, SciPy DOP853-independent solve_ivp at high precision reproduces:
epsilon=0: sigma=0;
epsilon=.001, Ω=2: sigma=0.001000000;
epsilon=.01, Ω=2: sigma=0.010000031;
epsilon=.02, Ω=2: sigma=0.020000250;
epsilon=.01, Ω=2.04 and 2.08: sigma=0 to numerical precision.

At small epsilon and Ω≈2k, the primary maximal growth is **sigma≈epsilon k**. In vacuum without external losses, both transverse polarizations have the same maximal growth exponent in this special homogeneous model, but *opposite pump phase*: they amplify different initial quadratures. The phase and the source amplitude control transfer; no extra energy is created by the coordinate description alone.

**Critical literature comparator:** Brandenberger, Delgado, Ganz and Lin, *Graviton to photon conversion via parametric resonance*, Physics of the Dark Universe **40** (2023) 101202, DOI 10.1016/j.dark.2023.101202, studies **propagating gravitational waves**; in vacuum its primary band is absent in the stated setup, while a dispersive medium permits first-band resonance. Mahajan and Asenjo, Phys Rev E **107** (2023) 035205, DOI 10.1103/PhysRevE.107.035205, find restricted phase-matched plasma/gw amplification. Hence **do not transfer this homogeneous-shear 2:1 instability unmodified to real traveling gravitational waves**; propagation, spatial resonance and electromagnetic dispersion materially change the answer.

## Gate 199 — energy source is the gravitational anisotropic stress, not the grid label

For x polarization canonical p_x=e^(−2b)Adot_x, H_x=(1/2)[e^(+2b)p_x²+e^(−2b)k²A_x²]; for y polarization p_y=e^(+2b)Adot_y, H_y=(1/2)[e^(−2b)p_y²+e^(+2b)k²A_y²]. Explicit time dependence gives

**dot H_EM=bdot[e^(+2b)p_x²−e^(−2b)k²A_x²−e^(−2b)p_y²+e^(+2b)k²A_y²].**

This is exactly the shear-conjugate EM stress term. In a self-consistent metric+Maxwell action its negative enters the gravitational shear energy balance, subject to covariant Einstein constraints. Imposing b(t) externally treats this as pump work by an external source. In the unchanged Cone geometry no dynamical b(t) or source work budget is fixed by u_G=1/4 and u_EM=1/2.

## Gate 200 — K4 self-consistent homogeneous tensor does NOT enforce 2ω_EM laboratory resonance

For k_grav=0, existing K4 tensor EOM is **bddot+3H bdot+(8η/3)H² b=0**. On the certified *coasting* background a∝τ, H=1/τ, the exact solutions for η>3/8 are

**b(τ)=τ^(−1)[C1 cos(nu ln(τ/τ0))+C2 sin(nu ln(τ/τ0))]**,
**nu=sqrt(8η/3−1)∈(0,sqrt3]**, while at η=3/8 the repeated root gives τ^(−1)(C1+C2 ln τ). This is logarithmically oscillatory and power-law damped, **not a sustained fixed-amplitude sinusoidal pump**. Its instantaneous proper-time frequency is nu H. Comparing with an EM mode ω_EM,phys∝1/a∝1/τ, their frequency ratio is constant on the exact coasting background, but the primary 2:1 condition would require ω_EM,phys=nu H/2≤sqrt3 H/2, i.e. horizon-scale, **not subhorizon lab** EM. The amplitude decays as a^(−1), invalidating indefinite exponential Floquet growth even in a hypothetical exactly matched cosmological mode.

For gravity k_grav≠0, the tensor frequency includes k_grav²/a² and is not bounded by H; potentially shorter-wavelength traveling waves need a full spatial Maxwell/gravity phase-matching calculation. Their amplitude, wavenumber, and coupling normalization **are not fixed** by the factor-grid offset ratio. Also η remains free in the full stable interval, so a unique Omega_G is not selected.

## Gate 201 — research verdict and next source gate

The user's peak-pump idea has a concrete, source-aware mathematical mechanism: a nonconformal gravitational shear perturbs electric/magnetic Maxwell coefficients oppositely and **can** parametrically amplify EM in a prescribed homogeneous time-dependent background. This is physically different from conformal-only geometry and exactly verifiable. **But the actual K4 shear mode already in the Cone ledger does not produce a sustained lab-frequency 2:1 pump**. The spatial half/quarter factor ratio cannot be substituted for a temporal frequency selector; no independent gravity-driven source or novel parameter-free EM gain is identified. A testable next gate is the **spatially dependent, propagating tensor mode** from the existing K4 action, retaining full Maxwell wavevector/polarization matching and comparing directly to GR traveling-GW resonance literature. If this yields only standard source-dependent mixing, close the hypothesis without a new gravity claim.

**Reproducer**: `research-notes/gravity_shear_maxwell_k4_pump_v15_678.py` committed as cde81c7320f9bd949a3874c116228334c61349c5, separately executed local reference `/mnt/data/cone_shear_pump/reproduce.py` (PASS: symbolic full metric Maxwell reduction, polarization oscillator, FLRW K4 homogeneous tensor exact coasting mode, high-precision Floquet and exact energy derivative). No images generated; no protected/certified Suzuki object touched.

**HANDOFF:** external audit and gravity/sandbox. Independently check Maxwell e^(±2b) coefficients and field canonical transformation, both polarization Floquet exponents, **homogeneous model versus traveling gravitational-wave caveat**, K4 exact coasting tensor power-law, and ratio to *physical* EM frequency (not incorrectly treating cosmological redshift as absent). Check stability-window provenance and sourcing of η. Audit whether any 1/4 factor can be promoted to Ω_G/ω_EM without an independently supplied action; currently none.
