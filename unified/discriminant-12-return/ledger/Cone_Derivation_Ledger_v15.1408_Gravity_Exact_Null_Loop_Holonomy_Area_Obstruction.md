# Cone Derivation Ledger v15.1408 — Exact nonlinear chiral H² target loop gives holonomy but ZERO Weyl–Maxwell area coupling

**Date:** 2026-11-24 Eastern. **Lane:** Gravity/Cone. **Status:** [EXACT POSITIVE] a circularly polarized real chiral null sigma wave is an exact solution of the **full nonlinear H² target equations in a prescribed flat spacetime**, and its image can trace the geodesic circle with π/2 Levi-Civita holonomy; [EXACT NEGATIVE] its spacetime target area two-form is identically **zero** because the sigma map has rank one, so the proposed Weyl–Maxwell–H² area interaction is OFF despite the nonzero target holonomy; [NEGATIVE] wave amplitude/loop radius is arbitrary and its positive null stress-energy means prescribed flat Minkowski is NOT a complete self-consistent Einstein+sigma solution for finite gravitational coupling; [OPEN] independent noncollinear sigma waves, physical target-loop selection, backreaction and quarter-grid normalization. Parent v15.1407 intrinsic H² loop transport and v15.1381 Weyl–F–area coupling. All code commits additive.

## Gate 1340b — exact curved-target sigma field traveling on a null characteristic

Use normalized H² coordinates `phi=(u,v)` with metric `G_AB=δ_AB−phi_A phi_B/(1+u²+v²)`. For the physical sigma kinetic action `L=−(f² r²/2)G_AB∂phi^A·∂phi^B`, the Euler–Lagrange equations are

`Box phi^A−phi^A G_BC ∂phi^B·∂phi^C=0`.

In flat (-+++) spacetime choose arbitrary real k,a and `s=k(t−x)`,

`u=a cos s,quad v=a sin s`.

Since all field derivatives are proportional to the **same null gradient** ds, both `Box phi^A=0` and `G_BC∂phi^B·∂phi^C=0` identically. Therefore these are **exact full nonlinear sigma equations** for any a and k, not just the linearization. Their target image traverses an intrinsic circle of geodesic rapidity radius `χ=asinh(a)`. Picking `a=sinh(ln2)=3/4` gives the conditional `χ=ln2` disk and holonomy `|Θ|=2π(cosh ln2−1)=π/2 (mod 2π)`, just as v15.1407. This particular amplitude is **chosen**, not dynamically fixed by r=1/4 or the historical measured Dirac rapidity.

Their sigma Lagrangian vanishes because the field gradients are null; nevertheless stress-energy is positive and nonzero: `T_tt=f² r² a² k²` and `T_tx=−f² r² a² k²` in the chosen normalization. A finite-amplitude plane-fronted traveling wave has nonzero null stress and is not a solution of **vacuum** Einstein gravity in exactly flat Minkowski. The sigma-field equation is tested in a **prescribed** background, without solving the gravitational constraints.

## Gate 1340c — decisive distinction between a target loop and a spacetime two-form

Although the map `s→(u(s),v(s))` encloses nonzero **intrinsic target disk area** and can generate target tangent-vector parallel-transport holonomy, the pullback two-form of the actual interaction is

`B_mu nu=[∂mu u ∂nu v−∂nu u ∂mu v]/sqrt(1+u²+v²)`.

Because `du=u'(s)ds` and `dv=v'(s)ds`, **`du∧dv=0` identically**, independent of the target area normalization. Hence `B_mu nu=0`, `C_mu nu rho sigma B^rho sigma=0`, and **the Weyl–Maxwell interaction is absent even if a separate Weyl tidal background is present**. The target holonomy and target-area pullback are *different constructions*. This is a sharp falsification of the naive idea that any closed quarter-hyperboloid orbit automatically pumps EM waves.

A free **point particle** on H² also cannot perform a nontrivial constant-χ circle as a geodesic: the radial geodesic equation is `χddot−sinhχcoshχ θdot²=0`, and at χ=ln2 the centripetal factor is `sinhχcoshχ=15/16`. This is not a contradiction with the exact *null sigma field* traveling loop, whose wave equation is hyperbolic with a null gradient, not an auxiliary massive particle geodesic equation.

**Executable tests:** local Python `/mnt/data/cone_gate/k4_exact_chiral_h2_loop_v15_1408.py` (SymPy, actual PASS full nonlinear EOM, Btx=0, rho/flux, π/2 conditional holonomy and noncircular target geodesic); committed equivalent `research-notes/k4_exact_chiral_h2_loop_area_null_v15_1408.py`, SHA **c1ad4361ebfb4e338be807f78bea0ac7aef0b3d8**, external exact-byte Audit replay pending.

**AUDIT:** independently check exact sigma equations and metric inverse/Christoffels, full null stress, pullback rank-one obstruction, nontrivial target holonomy despite B=0, and absence of full Einstein solution or dynamically selected a=3/4.

**NEXT:** construct a rank-two spacetime sigma map using independent null directions, quantify its exact nonlinear EOM residual and solve that residual systematically rather than mislabel the linear waves as full exact solutions. This proceeds in v15.1409.
