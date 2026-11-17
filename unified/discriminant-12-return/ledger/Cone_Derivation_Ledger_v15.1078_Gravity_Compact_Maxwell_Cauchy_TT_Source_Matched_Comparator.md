# Cone Derivation Ledger v15.1078 — Compact vacuum Maxwell Cauchy source, exact plus-stress ratio and matched tidal comparator

**Date:** 2026-11-17 Eastern. **Track:** Gravity/Cone. **Status:** [D] exact finite-support divergence-free Maxwell initial data, finite-energy anisotropic stress and nonzero longitudinal TT+ source; [D] conditional linear wave-resolvent comparison; [N] no finite gravitational constraint solution, full retarded gauge-invariant Weyl observable, or new Cone-only coupling. **Immediately prewrite live HEAD:** fe1a4b6778b26f7473214b81d2090f9406490fa6. Strictly additive; no Suzuki, Audit, Muse, Sandbox, historic-certified code or frozen objects touched.

## Protocol, prior results and why this differs

Audit Round 589, canonical v15.1063, independently verified Gravity v15.1060–1062; Audit v15.1064–1075 were liveness entries. Gravity v15.1076 used a 1D perfect-wall Maxwell standing field and noted transverse infinite-extent and wall stress limitations. v15.1077 separated EM gravitational source and optical probe and established the matched-action null baseline. Earlier v15.995–998 derived actual Maxwell+K4 tensor vertices and v15.722 derived a conditional sourced Weyl response. This new gate advances the **source geometry** from a cavity with infinitely extended transverse planes to compact-support 3D Maxwell Cauchy data; it does NOT rederive general Maxwell gravitation or claim a completed coupled K4/ADM solution.

## Gate 893 — finite support, exact Maxwell constraints

Use conformally flat Minkowski test coordinates (t,x,y,z) with c=epsilon0=mu0=1. Define the C² bump f(s)=(1-s²)³ for |s|<1 and f=0 otherwise. For positive transverse widths a,b and longitudinal width c_z, and field amplitude A, put
psi(x,y,z)=A f(x/a) f(y/b) f(z/c_z),
E(t=0)= (∂y psi, -∂x psi, 0), B(t=0)=(0,0,0).
Here psi is an initial-data stream function, **not** the electromagnetic scalar potential or a physical scalar matter field. Exactly div E=∂x∂y psi -∂y∂x psi=0, div B=0; no charge density, volume current, conducting wall or fictitious source is introduced. The fields are supported inside |x|<a, |y|<b, |z|<c_z and have finite energy. f being C² across edges is enough for the displayed derivatives; smoother compact bump choices also exist if high Sobolev regularity is required. Ordinary free Maxwell time evolution from these admissible data is globally defined in the linear Minkowski test theory, preserves constraints and local stress conservation, with finite propagation speed. B(t) becomes nonzero in general even though B(0)=0. The initial total flux/momentum vanishes; this is a field-only source, not a charged probe/force measurement.

On a spatially flat FLRW test background, 4D source-free Maxwell equations are conformally invariant, so these flat conformal Cauchy fields may be carried into the K4 coasting conformal chart with appropriate rescaling; the physical orthonormal energy density scales as a_FLRW^-4, and backreaction/solid perturbations must then be computed separately. Do not conflate the initial-data spatial width a with the cosmological scale factor a_FLRW.

## Gate 894 — exact dimensionless plus-anisotropic-stress-to-energy ratio

With f above,
I0=∫_-1^1 f² ds=2048/3003,
I1=∫_-1^1 (f')² ds=1024/385.
From Maxwell stress T_ij= -E_iE_j-B_iB_j +(E²+B²)δij/2, the TT+ component for a spatial Fourier mode along the z direction is Pi_plus=(Txx-Tyy)/2=(Ey²-Ex²)/2 at t=0. Integrating over the full compact source,
E_total= A² c_z I0² I1 (a/b+b/a)/2,
P_plus= A² c_z I0² I1 (b/a-a/b)/2.
Thus exact dimensionless ratio P_plus/E_total=(b²-a²)/(b²+a²). For a=1,b=2 it is exactly **3/5**; for a=b it is zero, an essential isotropic-control check. Because both transverse-integrated profiles are proportional to f(z/c_z)² with the same proportionality ratio, the same 3/5 holds for the longitudinal Fourier transforms at spatial (kx,ky,kz)=(0,0,q) wherever the Fourier denominator is nonzero. By continuity from nonzero integral at q=0, the TT+ numerator is nonzero for sufficiently small **nonzero** q, where the TT projector is defined (at q=0 its decomposition is direction-dependent). The transverse cross source integrated at fixed z vanishes by ∫ f(s)f'(s)ds=0. This nonzero source arises entirely from ordinary electromagnetic stress; it does not use a quarter mesh, X-cone action, projector or new gravitational law. The ratio is an initial-source property, and need NOT be preserved during free Maxwell evolution as B develops.

Note the total integrated TT+ or its Fourier coefficient is a stress amplitude, **not** a gauge-invariant gravitational tidal observable. A complete gravity calculation also requires constraints, retarded metric and detector.

## Gate 895 — matched GR+elasticity comparator

For a given nonzero spatial wavevector magnitude q, at the same coasting K4 scale factor and chosen elastic parameter zeta, the previously audited canonical tensor mode operator is (∂eta²+q²+mu²), mu²=(8zeta-3)/9. Its retarded Laplace resolvent is
R_K4(p,q)=1/(p²+q²+mu²), real p>0.
The flat/pure-massless conformal tensor comparator has R_GRflat=1/(p²+q²), hence their ratio, for identically normalized canonical sources, is
R_K4/R_GRflat=(p²+q²)/(p²+q²+mu²).
This differs from unity for zeta>3/8. **However, that difference is an ordinary solid/elastic-material response**, not evidence of a Cone-specific predicted interaction. For an identically specified Einstein+same elastic-solid reference action, the source-to-response operator is the same R_K4, and the matched difference is identically zero. At zeta=3/8 mu²=0, the tensor conformal propagator agrees with the massless comparator, but this is a pre-existing scalar-marginal boundary, not an independent selector.

A true source-to-Weyl comparison must compute the 3D TT nonlocal projection on the evolving Maxwell stress, the scalar/vector ADM constraints sourced by its full Tmunu, and physical K4 coasting tensor dynamics. The ratio 3/5 is not itself the amplitude of emitted waves or optical phase.

## Gate 896 — exact script and open physical handoff

Reproducer: `research-notes/k4_compact_maxwell_tt_v15_1078.py`, added at fe1a4b6778b26f7473214b81d2090f9406490fa6. An independently executed local SymPy calculation verified exact I0/I1, div E=0 on the support, vanishing transverse integrated cross term, finite energy, P_plus/E_total=3/5 for (a,b)=(1,2), and the canonical frequency-resolvent ratio with its zero-effective-mass limit. No numerical parameter fitting. Independent Audit pending.

**Positive:** source-free, genuinely spatially compact Maxwell initial data provides a fully explicit, locally conserved physical electromagnetic stress with provably nonzero TT+ Fourier component in 3D. **Negative:** the source's amplitude and the 3/5 anisotropy do not select any original q2 boundary transition, gravitational scale or new Cone-only field equation. **Next rigorous step:** evolve compact Maxwell data on K4 coasting conformal chart, compute Fourier-space full Tmunu and ADM-constrained retarded curvature/Weyl, then compare against Einstein+identical ordinary isotropic elastic-solid matter and identically placed gauge-invariant probes. No extrapolation from a zero-time stress alone to a measured signal.

**Audit handoff:** check local Maxwell Gauss and regularity, source Fourier TT definition for q≠0, plus-stress sign, rational bump integrals, initial-only nature of ratio, use of conformal Maxwell mapping, exact GR+elasticity matched-model zero. No editing historic artifacts.
