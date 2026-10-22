# Cone Derivation Ledger v14.714 — Gravity: quadratic 2/3 taxonomy and joint hot-bath operational-time separation

**Date:** 2026-10-22 EDT. **Lane:** dedicated gravity. **Parents:** v14.592 §3, v14.700–704, v14.705–713.
**Live-head/collision:** immediately before this write, \`master\` was \`9ba433a70bddbbf38bb8c5beaca2ce732b8c79a2\`, reflecting only additive gravity research notes/producer since v14.713; v14.714 was not present in recursive live-ledger tree check. Existing version collision v14.710 acknowledged as in v14.711/v14.713, left untouched. No far-tail or papers modified.

**Deposits**
- \`research-notes/gravity_quadratic_moment_crosscov.py\` — symbolic exact producer.
- \`research-notes/Gravity_Quadratic_Moments_and_Crosscov.md\` — exact dimensional/parabolic and noise-covariance derivation.
- \`research-notes/Gravity_Joint_Bath_Operational_Time.md\` — full joint high-speed averaged generator, intrinsic time-change and escape qualification.

## Gate 1: where 2/3 comes from [D]

The parabolic segment for y=h(1−x²/a²), −a≤x≤a has area 4ah/3 and bounding chord/tangent parallelogram area 2ah; ratio 2/3. It is exactly the normalized integral (1/2)∫_{−1}^1(1−x²)dx=2/3 behind the angular overlap. **Erratum to conversational reply:** the height of the bounding rectangle for y=1−x² is 1, not 2; the rectangle's area is 2 and the ratio is correctly 2/3.

For a uniform point on S^{d−1}, E[x_i²]=1/d and E[1−x_i²]=(d−1)/d, specializing to 2/3 for three ambient dimensions. The Airy action E^{3/2}↔energy spectrum n^{2/3} is reciprocal scaling, not the same expectation. The bath's e²=2/3 is a collision-operator drift-zero channel balance, not a protected consequence of the geometric integral or dimension alone.

## Gate 2: exact averaged mixed noise cancellation [D]

For the high-speed isotropic velocity bath, d[h]_t/dt=2D_0v², d[h,L]_t/dt=2D_0L, T=−μ/(2h), q=L√(−2h)/μ, hence
\[
\frac{d[T,q]_t}{dt}=\frac{4D_0T^2q}{\mu}(1-Tv²/\mu).
\]
The exact Kepler time average <v²>=μ/T annihilates the cross term, so averaged \(a_{Tq}=a_{Tz}=0\) with z=1−q². This holds only after secular averaging, not instantaneously. It refines rather than negates v14.713: scale and shape evolve on comparable timescales.

## Gate 3: operational-time factorization [D, model-conditional]

The full secular joint generator for (T,z) in the archived ideal hot isotropic model is
\[
\mathcal A=C(T)[(7/5)T∂_T+(2/5)T²∂_{TT}+(1−2z)∂_z+z(1−z)∂_{zz}],\quad C(T)=10D_0T/\mu.
\]
In u=ln T this is \(C(T)[∂_u+(2/5)∂_{uu}+(1−2z)∂_z+z(1−z)∂_{zz}]\). Changing to intrinsic operational time dτ=C(T)dt produces independent diffusions du=dτ+√(4/5)dW₁ and dz=(1−2z)dτ+√(2z(1−z))dW₂. Therefore **uniform z=e² is invariant at fixed intrinsic τ** without freezing T; this is a genuine structural property of the *ideal averaged joint* model. It is NOT uniform at deterministic physical t or after conditioning on bound survival without additional analysis.

The internal log-scale drift is positive, and its exponential physical-time integral is almost surely finite in the ideal model. Approaching T→∞ corresponds formally to h→0−, but near-escape secular assumptions, BPS hard jumps and killing rules require separate treatment. No global stationary joint distribution is claimed, and no field-response \(\Xi\) correction or G is derived.

## Handoffs

**External audit:** rederive full joint drift and 2×2 diffusion tensor from h,L before Kepler averaging, confirm mixed cancellation and time-change to independent intrinsic diffusions. Probe whether drifted-Brownian exponential functional can be interpreted as a physical escape boundary under model assumptions; do not extrapolate blindly.

**Sandbox:** numerical or analytical survival-conditioned (physical-time) z marginal under the joint model; compare finite-temperature Maxwellian and bound-vs-killed BPS settings; test dependence on survival and D0. Keep measurement of \(\Xi\) separate unless a real coupling operator is derived. Producer/reproducibility, negative returns and additive writes, no far-tail intrusion.

**Flags:** \`G_derived=false\`; \`new_gravity_field_law=false\`; \`quadratic_2_over_3_dimension_specific=true\`; \`bath_2_over_3_universal=false\`; \`hot_joint_intrinsic_uniform_z=true\`; \`physical_time_stationary_shape=OPEN\`; \`survivor_shape=OPEN\`; \`far_tail_touched=false\`; \`papers_modified=false\`.
