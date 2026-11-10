# Cone Derivation Ledger v15.605 — Lane A: normalized continuum boundary-defect law and circle/secant versus divisor-count scaling

**Date:** 2026-11-10. **Parents:** v13.197 circular staircase pushforward; v14.367 unit-circle/hyperbolic secant dictionary; v14.767 power-map and divisor-seat covariance; v15.602 generalized q,L Casimir theorem; v15.603 independent audit; v15.604 exact refinement naturality. **Status:** [D] exact algebraic and limit identities; [O] physical measure and q=2 / EM-G selector. **Live HEAD checked immediately before writing:** 6abe3af1a82e49319232bf1544636cf051a0957b; v15.605 collision search negative. Additive only; no Suzuki frozen/production modifications.

## Gate 70 — finite normalized defect density

For mesh spacing 1/q (integer q>=1), fixed geometric shell radius j=L/(2q)>0 and L=2qj an integer, let E_{q,L}=j(j+1)I-(Jx²+Jy²+M²) be the defective original unit-step ladder Casimir deficit from v15.602. With a=min(q−1,L),

tr E=a(a+1)[3(L+q)−(2a+1)]/(6q²).

The unnormalized trace generally grows linearly with q, as v15.604 established. Define the uniform **state-counting** mean e_q(j)=tr E/(L+1). At fixed j and along admissible q→∞,

**e∞(j) = j(2j+3)/3 for 0<j≤1/2, and e∞(j)=1/2+1/(12j) for j≥1/2.**

Proof: for j≥1/2, a=q−1 eventually, so tr E=(q−1)(j+1/6+1/(6q)); divide by 2qj+1. For 0<j<1/2, a=L=2qj eventually, and tr E=j(2jq+1)(2jq+3q−1)/(3q); divide by 2qj+1. Both branches give 2/3 at j=1/2. The function strictly increases on (0,1/2], decreases for j≥1/2, and tends to 1/2 as j→∞. It is bounded and maximum 2/3. A continuum interpretation is uniform m-average of one-sided omitted-weight profile, not a physically selected density of states. Do not equate the 2/3 with the parabolic-segment or rotor 2/3 occurrences without an additional operator identification.

Exact rational witness: j=1/4, q=2,4,8,16 gives e_q=1/4,13/48,9/32,55/192 → 7/24; j=1 q=2,4,8,16 gives 1/4,29/72,133/272,565/1056 → 7/12. Native q=2 is not selected by the limit.

## Gate 71 — user circle-view secant scaling, precisely two comparison protocols

The already certified v14.767 and v14.367 cone circle dictionary for factor grid unit u>0 at ordered pair (un,u) is
diameter d=u(n+1), half-chord h=u√n, horizontal center offset o=u(n−1)/2,
(d/2)²=o²+h²; normalized circle fractions 2h/d=2√n/(n+1), 2o/d=(n−1)/(n+1).

At **fixed normalized n**, refining u from 1 to 1/q shrinks absolute chord h and diameter d equally. Their ratio and circle station are unchanged, exactly the v14.767 normalized power/seat covariance.

At **fixed physical product X=xy>0**, however, the normalized hyperbola level is n=X/u²=q²X, yielding h=√X, d/2=(qX+1/q)/2, and

**2h/d = 2q√X/(q²X+1) ~ 2/(q√X)** as q→∞.

Thus, under a *physical-product cutoff* comparison, the √n secant occupies a vanishing fraction of the circle's increasing diameter even though its absolute half-chord is constant. This realizes the user's observed lowering of the secant relative to total circle size. It is a change of normalized level and counting convention, not a prediction of diminished energy or a new constant.

The divisor count at physical cutoff is D(floor(X/u²))=D(floor(q²X)), whereas the triangular count at matched normalized level is T(n)=n(n+1)/2 and complement A(n)=T(n)−D(n). Along n→∞, the classical D(n)=n log n+(2γ−1)n+O(√n) and T(n)~n²/2 imply D(n)/T(n)→0, A(n)/T(n)→1. This supports a *relative-area/count* reduction of divisor content versus the triangle as the effective integer index increases, but does not identify raw D(n),A(n) counts with the separately derived circular pushforward **areas** W_D,W_A of v13.197; nor is the secant aspect ratio equal to D/T. These geometric and arithmetic ratios have different rates.

The normalized power map P_{k,u}(x,y)=(u(x/u)^k,u(y/u)^k) sends n→n^k while preserving u; a change of u and a power map are different operations. Refinement does not by itself select the EM u=1 versus proposed gravity u=1/2 sector.

## Gate 72 — comparison and remaining physical burden

At fixed geometric j, e∞(j) is independent of q but depends on j and the **chosen uniform counting measure** over refined magnetic states. At fixed physical hyperbola X, 2h/d decreases as q^{-1}, D(n)/T(n) decreases approximately log(q)/q². Both are exact/standard asymptotic statements with *different normalizations* and no common scalar identity derived linking the two. There is no derivation that the geometric shell j and arithmetic index n must be locked, or that e∞(j) supplies the scaling weight of the divisor staircase.

Reproducer: exact SymPy simplifications and rational q samples plus fixed-n versus fixed-X circle identities in conversation artifact `cone_density_secant_gates_70_72.zip`. No image generator.

**Next discriminating gate:** compare pushforward circular area densities under u-refinement with the counting-measure e∞(j); test whether any natural invariant measure transports the boundary defect without inserting a q-weight. Only then test a q=2 selector against physical observables.

**HANDOFF** target external-audit, gravity, sandbox; status open; verify the two piecewise density branches and 2/3 maximum, admissible fixed-j q sequences, fixed-n versus fixed-X circle ratios, and careful distinction between D/T and circular W_D/W_T. Confirm no physical G or photon interpretation. Suzuki frozen work unaffected.