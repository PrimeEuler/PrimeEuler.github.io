# Cone Derivation Ledger v15.1541 — Shared conic differential–integral dictionary and signed finite-depth departure from 2/3

**Lane:** Gravity/Cone, geometric side gate. **Date:** 2026-11-26. **Status:** exact elementary geometry and symbolic checks; independent Audit pending. Parent v15.1540 (Nyquist defect, not a physical coupling); earlier v14.592 §3, v15.469 (constant-force action, Archimedes and evolute), v15.470 (moment family), v15.606 (Casimir-deficit quadrature), v15.885 (shared-vertex tangency). Live HEAD checked before writing: 0f059704801120777a5abafce7d186f248561bb3. No changes to existing certified objects, Sandbox or Suzuki lane. New content here is the assembled shared-scale dictionary and finite-depth circle/hyperbola segment comparator, not a claim to rediscover earlier parabolic results.

## Gate 1432 — local differential dictionary

Use a common positive length h. Canonical mesh row T(Y)=Y²/(2h)+h/2 (v15.469); subtract its vertex to obtain P(Y)=Y²/(2h). The minus-offset parabola in the conversation differs by axial translation, irrelevant to its local derivatives and segment areas. On the same Euclidean tangent-normal coordinates compare circle cap C(Y)=h−sqrt(h²−Y²) (|Y|≤h) and hyperbolic graph H(Y)=sqrt(h²+Y²)−h. All have equal value, first derivative, second derivative at Y=0: 0,0,1/h. They differ at fourth order: C=P+Y⁴/(8h³)+..., H=P−Y⁴/(8h³)+.... The parabola graph acceleration a_p=P''=1/h is a derivative with respect to spatial graph parameter Y, not a physical time acceleration. Its Euclidean curvature is (1/h)(1+Y²/h²)^(-3/2); only at the vertex is this equal to 1/h. The ambient Minkowski hyperboloid of radius h has quadratic invariant Q=T²−|X|²=h²; intrinsic hyperbolic sectional curvature K=−1/h² for hyperbolic dimension ≥2. Shared h yields Q a_p²=1 and Q K=−1; these are geometric identities conditioned on that identification, not Einstein field equations. h=1/n gives a_p=n, Q=1/n², K=−n². The label 1/n for the radius should not be conflated with the label 1/n for the squared invariant.

## Gate 1433 — exact reciprocal differential–integral pair

At cap depth d>0 the parabolic half-width b=sqrt(2hd). Cap area A_p=∫_{−b}^b[d−P(Y)]dY=(4/3)sqrt(2h)d^(3/2). Rectangle area=2bd. A_p'=2b and therefore A_p/(d A_p')=2/3 and d A_p'/A_p=3/2. The second is the exact logarithmic area elasticity, independent of h and d, not an independently fixed graph acceleration. The physical constant-force bouncer J(E)∝E^(3/2) already appeared in v14.592 and v15.469; its inverse action elasticity is 2/3. The evolute of (Y,P(Y)) has coordinates E=−Y³/h², F=h+3Y²/(2h), with 27h E²=8(F−h)³. Thus the familiar 3/2 coefficient in the normalized evolute is also exact. It is different from P''=3/2, which simply selects h=2/3 in normalized units. Under uniform length rescaling h→λh, a_p→a_p/λ, Q→λ²Q, K→K/λ², while A_p/(d A_p') and d A_p'/A_p are unchanged; arbitrary reparametrization of Y does not preserve the graph second derivative.

## Gate 1434 — circle and hyperbola split about the common parabolic 2/3

Let z=d/h, with 0<z≤1 for the circle comparison. Dimensionless half-widths w_C=sqrt(z(2−z)), w_P=sqrt(2z), w_H=sqrt(z(2+z)). Area A/h²=2∫₀^z w(t)dt. Explicit A_C/h²=acos(1−z)−(1−z)w_C; A_H/h²=(1+z)w_H−acosh(1+z). A_P/h²=(4/3)sqrt(2)z^(3/2). For all three define R=A/(2bd)=∫₀^1 w(zs)/w(z)ds and L=dA'/A=1/R. This is a scale-free normalized segment-area ratio.

For 0<s<1, w_H(zs)/w_H(z)=sqrt(s(2+zs)/(2+z))<sqrt(s), whereas w_C(zs)/w_C(z)>sqrt(s). Therefore R_H<2/3<R_C for positive z in the shared domain, and R_P=2/3 exactly. Hyperbola ratio decreases with z (extends to z>1 and tends to 1/2 as z→∞); circle ratio increases to π/4 at z=1. The parabolic tangent-limit ratio is common. Series at z=0:
R_H=2/3−z/15+z²/35+O(z³),
R_C=2/3+z/15+z²/35+O(z³).
This provides an exact signed dimensionless finite-depth comparator in the prescribed conic atlas; it depends on chosen z, not a parameter-free physical susceptibility or a spacetime curvature measurement.

| z | hyperbola R | parabola R | circle R |
|---:|---:|---:|---:|
| .01 | .6660028445 | .6666666667 | .6673362032 |
| .1 | .6602735676 | .6666666667 | .6736323512 |
| .5 | .6391821181 | .6666666667 | .7091995762 |
| 1 | .6198270018 | .6666666667 | .7853981634 |

## Reproducer / scope

Executed Python SymPy /mnt/data/cone_conic_dictionary.py; all assertions passed. Committed identical source research-notes/k4_conic_operator_dictionary_v15_1541.py at c57ca5123c0104d1aadcdd2ab613a27bdc99d96d. Exact committed replay by Audit pending. The script checks the parabolic area, elasticity, evolute, both cap derivatives and first-order signed correction, prints second-order series and numerical comparator. The inequalities follow directly from the width ratios above. No physical clock, force, action normalization, electromagnetic response, G or new spacetime field equation has been derived. No assertion of a shared dynamical action selecting h; the geometric radius match is explicit input. No alteration of v15.1540 Nyquist mechanism or Sandbox v15.1485 no-selector result. The prior nonlinear GH subsidiary verification and N40 T=.08 remain open. Next compare the new conic cap dictionary with the existing factor-row/action-circle and Casimir-deficit constructions under their actual measures, checking whether any action-selected normalized depth exists rather than fitting z to a desired constant. Keep physical gravity validation distinct from this geometry.
