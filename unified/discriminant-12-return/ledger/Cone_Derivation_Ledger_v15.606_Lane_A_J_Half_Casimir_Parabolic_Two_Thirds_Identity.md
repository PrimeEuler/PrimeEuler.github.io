# Cone Derivation Ledger v15.606 — Lane A: exact j=1/2 continuum Casimir-deficit / Archimedean parabola-quadrature identity

**Date:** 2026-11-10. **Parents:** v14.592 Archimedean parabolic segment, v15.469 acceleration/action parabola, v15.572–574 original defective quarter ladder, v15.602 all-q theorem, v15.604 refinement naturality, v15.605 normalized continuum defect density. **Status:** [D] exact operator-to-parabola integral identity; [I] interpretation as a common geometric profile; [O] physical action/energy/current equivalence. **Prewrite HEAD:** 9343ea25f74a92afdc5f334fd762b55cbcb39e26; version collision search negative. Additive only; frozen Suzuki and production untouched.

## Gate 73 — the 2/3 is the same quadratic integral

At the critical geometric shell j=1/2, magnetic values m∈[-1/2,1/2] are refined with step h=1/q, q∈Z_{>0}, and the *original unit-step* J+ remains the chosen dynamics. For interior points, neither m+1 nor m−1 belongs to the shell, so J± vanish there (only the two extreme endpoint states connect to each other at a finite q). The finite Casimir defect E=j(j+1)I−(Jx²+Jy²+M²) therefore has a continuum interior profile, under uniform normalized state counting,

E∞(m)=j(j+1)−m²=3/4−m².

Set x=m+1/2∈[0,1]. The *formal* forward/backward AM–GM squared edge weights at the same j are

W_up(x)=(j−m)(j+m+1)=1−x²,
W_down(x)=(j+m)(j−m+1)=1−(1−x)².

These are the same parabolic-segment profile sampled from opposite ends. The local deficit profile is their arithmetic mean:
E∞(x)=[W_up(x)+W_down(x)]/2 = 1/2+x−x².

The two integrands differ by the odd-about-center function
E∞(x)−W_up(x)=x−1/2,
whose integral on [0,1] is exactly zero. Hence

**lim_{q→∞} tr E_{q,L=q}/(q+1) = ∫₀¹ E∞(x)dx = ∫₀¹(1−x²)dx = 2/3.**

The last integral is exactly the unit-height/unit-width normalized Archimedean parabola-segment quadrature already appearing in v14.592 and the constant-acceleration parabola integration of v15.469. This is now a direct shared-integrand identity, stronger than mere coincidence of numeric values. It does **not** identify the Casimir mean as a physical action or prove that the magnetic and acceleration operators are the same.

## Gate 74 — exact finite refinement correction and critical-shell mechanism

For j=1/2, L=q and a=q−1 in the all-q trace identity, so the mean deficit is **exactly**

e_q(1/2) = (q−1)(4q+1)/[6q(q+1)]
= 2/3 − [7q+1]/[6q(q+1)].

Thus convergence is from below, at rate 7/(6q)+O(q^−2). Examples: q=1 gives 0 (ordinary complete two-state SU2), q=2 gives 1/4 (quarter-offset mesh), q=4 gives 17/40, q=8 gives 77/144, q=16 gives 325/544; only the infinite-refinement limit is 2/3. At j=1/2 the full interval length 2j=1 equals the original step exactly. Except for endpoints (whose proportion tends to zero), the refined interior states have no allowed original-step transitions, which makes the entire formal transverse quadratic moment the defect. At other j the truncation profile is different and the normalized mean is the piecewise function of v15.605, not automatically 2/3.

This is an exact *geometric connection* between the cone's AM–GM transition parabola and the integrated Casimir deficit. The j=1/2 value is a maximum of the chosen normalized density (v15.605), but this does not select q=2 as a physical gravity mesh or derive G.

## Verification and handoff

Independent SymPy expansions checked E∞=(W_up+W_down)/2, E∞−W_up=x−1/2 and both integrals equal 2/3; exact rational evaluations q=1,2,4,8,16 and the closed-form deficit compared to the v15.602 trace formula. No numerical tolerance used. Original Archimedean result sourced to v14.592 and its native dynamics relationship to v15.469.

**HANDOFF** target external-audit, gravity, sandbox; type critical j=1/2 2/3 integral identity and finite-q correction audit; status open; verify exact integrands, physical scope, sign/rate of finite q correction, and avoid claiming that equal integrals identify physical actions or choose q=2. Frozen Suzuki untouched.

**Next gate:** replace uniform state counting by the actual cone circle-pushforward area measure (v13.197) and check whether the same 2/3 survives; that tests whether this bridge is measure-independent or contingent on the chosen coordinate weighting.
