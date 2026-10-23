# Gravity invariant areal-wall and physical grid-embedding test

Date 2026-10-23. Gravity lane, parents v14.759, v14.768–772. Theoretical model only. No Suzuki production work.

## Area-based anchor [D, conditional spherical surfaces]

For a geometrically identified closed spacelike two-surface S of area A(S), define its areal radius
\[
R_A(S)=\sqrt{A(S)/(4\pi)}.
\]
For one **independently calibrated physical length** ell_* > 0, set
\[
L_A(S)=\log(R_A^2/\ell_*^2).
\]
Area is diffeomorphism invariant when S itself is physically specified; the construction does not fix S or ell_*. In general, R_A is not the geodesic distance or a universal radial coordinate.

Postulate an **embedding hypothesis** that the physical normalized product shell of a state is \((R_A/\ell_*)^2=h^2 ab\) with positive integers a,b. This equality is an input, NOT a consequence of area geometry or field equations. Under it the counting function inside an areal wall is
\[
N_h(S;\ell_*)=D\left(\left\lfloor\frac{R_A(S)^2}{h^2\ell_*^2}\right\rfloor\right).
\]
For h_EM=1 and h_G=1/2,
\[
N_{\rm EM}=D(\lfloor R_A^2/\ell_*^2\rfloor),\qquad
N_{\rm G}=D(\lfloor4R_A^2/\ell_*^2\rfloor).
\]
At common S and ell_*, the asymptotic ratio is 4 as R_A/ell_* tends to infinity. This is the same arithmetic density theorem as v14.771, but now its wall is built from a geometrically defined scalar rather than coordinate r.

## Absolute grid spacing, non-identifiability [D]

The actual physical lattice spacing is a_h=h ell_*. Counts depend only on the dimensionless quotient R_A/a_h. If sectors have separate calibration lengths ell_EM and ell_G, then
\[
a_{\rm EM}=1\cdot\ell_{\rm EM},\qquad
a_{\rm G}=\tfrac12\ell_{\rm G}.
\]
Choosing ell_G=2 ell_EM makes the physical spacings equal and yields **identical counts on every areal wall**. Thus an invariant area does not alone fix the relative physical lattice spacing. An independent common ell_* or sector-matching rule is indispensable. Setting ell_G=2ell_EM is not a passive change of the same fixed instrument; it represents a distinct physical embedding or free sector calibration.

Further, changing the reference length ell_* while holding h fixed changes the physical state spacing and therefore the count. Invariance under pure unit changes requires physical lengths R_A, ell_* to scale together (their ratio fixed).

## Local invariant wall response [D]

The localized probe from v14.772 can be evaluated at L_A:
\[
\mathcal R_h(S,\varepsilon;\ell_*)
=\sum_{n\ge1}d(n)w_\varepsilon(\log(h^2n)-L_A(S)).
\]
Its exact EM-to-G translation covariance and large-L_A fixed-epsilon ratio 4 hold when one shared ell_* and profile are used. These are invariant under coordinate changes of the prescribed surface and lengths, not invariant under independently changing physical grid embeddings.

## Outstanding physical tests [O]

(1) Produce invariantly specified S and physically measured common ell_* without assuming a gravitational coupling constant in ell_* (e.g. avoid choosing Planck length defined using G if the purpose is to predict G).
(2) Derive shell embedding and actual EM/G state multiplicities from field equations, action or boundary conditions rather than assuming a=ell_* and a=ell_*/2.
(3) Demonstrate a gauge/diffeomorphism-invariant response coefficient, finite under regulator variations, not just geometric state-count ratio.
(4) Check failure of areal-radius uniqueness for general nonspherical surfaces, multiple boundary choices, and possible curvature corrections.
(5) Respect v13.770's Suzuki/Weil vs divisor-current distinction.

Verdict: an invariant common wall is **constructible**, but geometric invariance of the wall does NOT physically calibrate the relative lattice spacings or derive G. This precisely localizes the still-open selector.
