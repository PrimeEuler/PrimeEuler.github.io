# Cone Derivation Ledger v15.607 — Lane A: circle-Jacobian weighted Casimir deficit and non-invariance of the j=1/2 two-thirds

**Date:** 2026-11-10. **Parents:** v13.197 area pushforward, v14.592 parabolic segment quadrature, v15.469 action/parabola interpretation, v15.602 all-q mesh theorem, v15.605 normalized defect-density law, v15.606 direct 2/3 shared-parabola integral. **Status:** [D] exact change-of-measure identities; [O] physical shell measure, action/current operator equivalence and q=2 selector. **Live prewrite HEAD:** fcee2754eefe990e99298bdf32a6d00415878cd6; v15.607 collision check negative. Additive only; Suzuki frozen/production unaffected.

## Gate 75 — derive the circle shell measure from the project's actual pushforward Jacobian

The exact v13.197 map F(a,b)=((a−b)/2, sqrt(ab)) has absolute planar Jacobian J_F=(a+b)/(4 sqrt(ab)). On the **constant-sum** shell a+b=1 (j=1/2), let a=x, b=1−x with x in (0,1). Restrict the 2D pushforward area density to a thin constant-sum strip and normalize across its shell: the conditional shell density is

dμ_circle = dx/[π sqrt(x(1−x))].

Equivalently, this is normalized upper-semicircle arc measure for X=x−1/2, Y=sqrt(x(1−x)) at radius 1/2. Cone surface area differs from flat projected area by the global factor sqrt(2), which cancels under normalization. **This shell restriction is NOT the full two-dimensional circular pushforward of the triangle/divisor staircases W_T,W_D,W_A in v13.197.**

The continuum j=1/2 original-unit-step boundary Casimir deficit profile from v15.606 is E∞(x)=1/2+x−x² = (W_up+W_down)/2, with W_up=1−x², W_down=1−(1−x)². The uniform dx mean is 2/3, identical to the normalized Archimedean parabolic segment integral ∫₀¹(1−x²)dx.

Under the actual circle-shell measure,

**∫₀¹ E∞(x) dx/[π sqrt(x(1−x))] = 5/8.**

Proof: arcsine/Beta(1/2,1/2) moments <x>=1/2, <x²>=3/8 imply <E∞>=1/2+1/2−3/8=5/8. The mirror difference E∞−W_up=x−1/2 still integrates to zero under this reflection-invariant measure, so the *same parabola profile* yields <W_up>_circle=5/8. The exact measure-induced shift is 2/3−5/8=1/24.

Thus v15.606's exact mathematical bridge is **measure dependent**: it identifies the same AM–GM quadratic integrand under uniform coordinate measure; it does not imply a universal measure-independent 2/3 or identify Casimir expectation with a physical action. Neither result independently selects q=2 or Newton's G.

## Gate 76 — finite grid with geometrically induced cell weights

On the refined j=1/2 shell with q+1 nodes x_i=i/q, let the *actual finite operator* E_q be the v15.602 truncated original unit-step deficit. For q>=1 its diagonal entries are E_i=1/2+x_i−x_i² except for endpoint corrections −1/2 at i=0 and i=q (endpoints connect across the original unit step). For each site define a clipped nearest-cell interval [l_i,r_i]=[max(0,(i−1/2)/q), min(1,(i+1/2)/q)] and the exact circle area/arc weight

p_i=(2/π)[arcsin(sqrt(r_i))−arcsin(sqrt(l_i))], with sum_i p_i=1.

The normalized finite arc-weighted expectation e_q^arc=Σ_i p_i E_i converges to 5/8. The two endpoints have equal mass p_end=(2/π)asin(sqrt(1/(2q))); together their operator-truncation correction is −p_end. Since the smooth parabola quadrature has error O(q^(−3/2)) under the integrable arcsine singularity,

**e_q^arc = 5/8 − sqrt(2)/(π sqrt(q)) + O(q^(−3/2)).**

Independent symbolic integration verified 2/3 and 5/8 exactly; finite-cell numerical checks:
q=1:0; q=2:0.25; q=4:0.381230325683299; q=8:0.459621298794705; q=16:0.510366471995825; q=32:0.544710798336703; q=64:0.568486113782543; q=128:0.585126901505683; q=512:0.605095389507550; q=2048:0.615051555125003.
The circle cell weights are an explicitly chosen geometrically induced discretization; finite q lattice dynamics does not automatically specify probabilities p_i.

## Status and next test

The calculation is a **negative for measure-independent 2/3**, positive for an exact common parabolic profile and a mathematically natural alternate 5/8. Test whether the actual 2D staircase/area pushforward from v13.197 supplies a canonically induced marginal shell measure; absent such a selected measure, do not promote 2/3 or 5/8 to a universal physical constant or equate them with a gravitational coupling.

Reproducer and report: conversation artifact `cone_circle_area_gates_75_76.zip` with REPORT.md, reproduce.py and checks.txt.

**HANDOFF:** external-audit, gravity, sandbox; status open; type circle-shell Jacobian / boundary-Casimir mean audit. Independently verify the conditional-shell Jacobian, arcsine/Beta integrals and 1/24 difference, q=1 and q=2 endpoint corrections, finite-grid weights and asymptotic q^(−1/2) boundary bias; scrutinize conditional 1D shell measure versus full 2D staircase pushforward. Frozen Suzuki production untouched.
