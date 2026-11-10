# Cone Derivation Ledger v15.608 — Lane A: full two-dimensional circle-pushforward of the all-refinement Casimir boundary defect

**Date:** 2026-11-10. **Parents:** v13.197 exact circular staircase pushforward, v14.592 parabolic segment quadrature, v15.602 all-q defect theorem, v15.605–607 normalized and circle-shell Casimir means. **Status:** [D] exact continuum defect support and staircase-area integrals; [C] extension of the refined-shell function to continuous factor coordinates; [O] physical observable/canonical state measure/q=2 selector. **Prewrite HEAD:** 94b5eec4a4fed27e2043ac32436c5a9dabb56220; v15.608 collision search negative. Additive-only; frozen Suzuki/production unchanged.

## Gate 77 — the continuum defect occupies exactly the unit boundary strips

Use positive factor coordinates x,y, shell j=(x+y)/2, magnetic coordinate m=(x-y)/2 and the **original unit-step** AM-GM ladder. This is the coordinatewise continuum extension of v15.602 at fixed (j,m); it is not an assertion that arbitrary real x,y define a physical spin multiplet. The squared formal upward and downward amplitudes are

W_up=(j-m)(j+m+1)=y(x+1),
W_down=(j+m)(j-m+1)=x(y+1).

The upward target m+1 is outside the shell iff y<1; the downward target m−1 is outside iff x<1. Therefore the continuum boundary Casimir deficit is

**E(x,y)=1/2 [ y(x+1) 1_{y<1} + x(y+1) 1_{x<1} ].**

Endpoint equality conventions on x=1 or y=1 do not affect area integrals. Thus E(x,y)=0 for almost every x≥1,y≥1, while E is nonnegative on the union of one-unit-thick strips along the factor axes. This geometric support statement holds independently of the chosen positive area weight, once the original unit step and zero-origin factor coordinates are fixed.

For each integer n≥1, v13.197's exactly indexed staircases are the triangular columns x∈[k−1,k], 0≤y≤n+1−k; the divisor columns x∈[k−1,k], 0≤y≤floor(n/k), 1≤k≤n; and their complement A_n. Both regions contain **identically** the unit boundary cross {0≤x≤1,0≤y≤n} ∪ {0≤x≤n,0≤y≤1}; the complement A_n is a.e. contained in {x≥1,y≥1}. Hence the integrals of E over the two regions are equal for any common locally integrable weighting, and E integrates to zero over the complement. This relies on the **discrete column staircase convention**, not the continuous triangle x+y≤n+1 or a cap area.

## Gate 78 — exact 2D cone circle-area integral

The project's existing factor-to-circle pushforward map is F(x,y)=((x−y)/2,sqrt(xy)) with planar area Jacobian

J_F(x,y)=(x+y)/(4sqrt(xy)).

Write dA_circle=J_F dxdy. Define B_T(n)=∬_{T_n} E dA_circle, B_D similarly, and B_A similarly. Since E vanishes in A_n,

**B_T(n)=B_D(n)=B(n), B_A(n)=0.**

Both are exactly

**B(n)=sqrt(n)(3n²+8n+9)/45.**

Proof by disjoint cross decomposition. The unit corner square contributes 4/9. The horizontal strip 1≤x≤n,0≤y≤1 and the reflected vertical strip each contribute
n^(5/2)/30 + 4n^(3/2)/45 + sqrt(n)/10 − 2/9.
Their sum plus the corner is sqrt(n)(3n²+8n+9)/45.

These are **weighted integrals, not weighted probabilities**; to obtain conditional means divide by the actual pushforward areas W_T,W_D,W_A of v13.197. Since W_T and W_D differ, B/W_T ≠ B/W_D generally. The defect's mean in A_n is exactly zero for n≥3 when W_A>0. For n=1 or 2 the complement has area zero and its mean is undefined (do not report 0/0 as a mean).

At n=11, the audited v13.197 areas are W_T≈51.2635200516399, W_D≈30.1810563510192, W_A≈21.0824637006206. Our exact B(11)≈33.90327563474409, hence means B/W_T≈0.66135286068128, B/W_D≈1.12332965554399, and B_A/W_A=0. Neither average should be mistaken for v15.606's 2/3 uniform mean or v15.607's 5/8 conditional constant-sum shell mean: these integrate over **different domains**.

## Scope and checks

Exact symbolic SymPy integration of the corner and both boundary strips verifies the closed form. An independent evaluation of v13.197 exact column-area formula for n=1,2,3,5,11,20 reproduces the reported staircase areas and normalizations; n=11 agrees with the printed original W_T/W_D/W_A to full quoted precision. Reproducer `research-notes/full_staircase_boundary_defect_v15_608.py` is additive and independently executable with SymPy; conversation artifact provides the same code.

**Interpretation:** the selected original unit-step defect is boundary-localized and the divisor/triangular partition has a shared boundary cross, which forces equality of the two **unnormalized** defect integrals for any common weight. This does not derive a new physical field, energy, q=2 gravity selection, G, or Suzuki coupling. Do not equate the unnormalized B(n) to an arithmetic count D(n).

**Next gate:** test bulk-versus-boundary sensitivity under physical origin shifts (Paper C's x=n1+1,y=n2), u-scaled units and alternate step sizes; verify which parts are geometric invariants and which are artifacts of the assumed unit-step/factor-origin convention.

**HANDOFF** target external-audit, gravity, sandbox; status open; type full 2D circle pushforward/boundary localization audit; verify the support region, exact B(n), n=11 areas, undefined complementary mean at n≤2, and finite/refined continuum scope. Frozen Suzuki untouched.
