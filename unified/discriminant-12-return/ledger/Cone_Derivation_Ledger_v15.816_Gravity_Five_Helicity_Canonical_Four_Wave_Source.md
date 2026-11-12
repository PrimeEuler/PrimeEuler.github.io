# Cone Derivation Ledger v15.816 — Gravity: an on-shell positive-energy canonical matter source with all five nonzero stress helicities

**Date:** 2026-11-12 US Eastern. **Parents:** v15.727 canonical matter Lagrangian, conservation and positivity; v15.730 two-wave exact on-shell scalar Weyl benchmark; v15.731/740 spatially compact canonical wavepacket and spherical source null; v15.750/812 evolved common matter source to three selected curvature and optical responses; v15.815 full five-helicity finite-arm optical readout. **Prewrite live HEAD:** c84da154d2d52a03d3db300f19cc3120a6309987. Target absent; additive-only, no certified Suzuki modification.

**Status:** [D] exact four-wave real on-shell massless canonical scalar with one common stress Fourier wavevector and nonzero S, two vector and two tensor projections; [N] no-new-Cone claim, no full five-mode sourced optical readout yet; [O] spatial localization and full five-mode dynamical source integration.

## Gate 427 — why the previous physical source was three-helicity only

Our original v15.730–812 canonical positive-energy real scalar used χ=A(τ)cos(2x)+B(τ)cos(z), with no y-dependence. Reflection y→−y and its source geometry force stress components containing a single y index to vanish. At K=(2,0,1), this kills the vector-b helicity and the tensor e-b cross helicity identically. Their absence was due to **spatial reflection symmetry**, not a theorem forbidding canonical matter from coupling to them. A 5×5 optical detector cannot recover a sector that its source fails to excite.

## Gate 428 — exact four-wave common-K on-shell canonical source

Construct four *real* canonical scalar wave modes at τ>0 on coasting FLRW a=τ/sqrt3, each with exact time amplitude

**A_q(τ)=τ^(-1)cos[sqrt(3|q|²−1) log τ]**,

which solves **A_q''+3A_q'/τ+3|q|² A_q/τ²=0** and has A_q(1)=1, A_q'(1)=−1.

Choose

**p=(2,0,0), q=(0,0,1)**,

**r=(1,1,0), v=(1,−1,1)**,

so **p+q=r+v=K=(2,0,1)**.

Let the actual *real* canonical scalar field be

**χ(τ,x)=A_p cos(p·x)+A_q cos(q·x)+sqrt2[A_r cos(r·x)+A_v cos(v·x)]**.

This is an exact solution of the *linear* canonical massless KG equation by superposition. At each spacetime point the canonical local energy density **rho=(χdot²+|gradχ|²/a²)/2≥0**. The configuration is spatially periodic/unbounded, used as an analytic Fourier witness, **not** an already localized finite-energy source. A smooth compact spatial cutoff on Cauchy data followed by correct KG evolution is the planned localized implementation; it cannot be inserted directly into a globally on-shell plane-wave formula without recomputing time evolution.

The positive-K quadratic spatial-gradient cross-stress at τ=1 receives two resonant products: from (p,q) and from (r,v), the latter with coefficient sqrt2×sqrt2=2. Four-wave cross terms at other total wavevectors are distinct. Apart from the isotropic trace piece, the positive-K spatial stress in a physical orthonormal basis is

**T_K,anisotropic=−(3/4) S**,

**S=(p q^T+q p^T)+2(r v^T+v r^T)=[[4,0,4],[0,−4,2],[4,2,0]]**,

using each real cosine's +wave coefficient 1/2, a(1)²=1/3 and the two gradient derivatives.

## Gate 429 — exact nonzero S/Ve/Vb/T+/T× projections

Use the same detector-aligned orthonormal basis as v15.815:

**n=(2,0,1)/sqrt5, e=(1,0,−2)/sqrt5, b=(0,1,0)**.

For the raw S dyad the five independent coefficients, in the convention

**(n S n−trS/3, n S e, n S b, (e S e−b S b)/2, e S b)**,

are exactly

**(32/5, −4/5, 2sqrt5/5, 4/5, −4sqrt5/5)**.

All are nonzero. Multiplying by the physical Fourier stress prefactor −3/4 yields

**(−24/5, +3/5, −3sqrt5/10, −3/5, +3sqrt5/5)**.

Therefore one conventional real, on-shell, nonnegative-local-energy canonical matter field can have nonzero stress projections in **all five** metric/solid helicity sectors at the *same* K. This closes the source-level availability test suggested by the full-rank five-helicity optical detector gate v15.815.

## Gate 430 — honest remaining dynamical/originality controls

The existence of the above stress projections does **not** imply that every field mode or detector channel has a nonzero *physical response* for all time. Each metric/solid sector must be sourced using the complete stress (including isotropic pressure, density, momentum and the K4 solid constraints) and evolved from consistently specified initial conditions. The full five-helicity **source-to-optical detector** calculation remains open. Positive pointwise energy density does not assert that one complex Fourier stress coefficient is positive.

**Reproducer:** research-notes/k4_fourwave_five_helicity_matter_v15_816.py, additive commit **ec9d2256213131133f07accec43e6e44bd2fb61b**. Locally checked using exact SymPy rational/surd dyad projections and explicit KG mode differential equations. This is an independently specified four-wave physical-source extension, not an unearned novel Cone force or a Yang–Mills quantum gap.

**HANDOFF — external audit:** independently derive the four-wave K-sum matching, all five source projections and Fourier cosine prefactors, the on-shell coasting KG equation and canonical local positive-energy inequality. Verify there are no extra cross terms at the selected K and that the nonlocalized witness is not mislabeled a compact wavepacket. Audit together with v15.815 five-helicity detector inversion. The matched Einstein–Hilbert+ordinary elastic solid GR comparator remains exactly null for Cone novelty.

**NEXT:** propagate compact asymmetrically localized four-wave Cauchy data, evolve complete five-helicity K4 metric/solid modes and project into v15.815 photon/mirror/clock detector. Full cosmological gauge-invariance tests (including source, free-endpoint initial conditions and emitter clock transformations) are also required before treating an optical transfer as an operational gauge-invariant observable.
