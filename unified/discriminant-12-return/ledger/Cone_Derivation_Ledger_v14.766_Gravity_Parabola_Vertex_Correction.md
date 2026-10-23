# Cone Derivation Ledger v14.766 — Correction: half-scale gravitational parabola vertices versus affine Hurwitz shifts

**Date:** 2026-10-23 EDT. **Lane:** Cone gravity/divisor geometry. **Parents:** v13.177, v13.200, v13.362, v13.364, v14.731, v14.765. **Pre-write live master:** \`033875f646fe8de1a9f1125ac19c56089cf27024\`; v14.766 verified unoccupied. Additive correction, no Suzuki sandbox work.

## Correct the geometry [D]

For fixed factor row y=u, with \(T=(x+y)/2,\ X=(x-y)/2,\ Y^2=xy\), one gets
\(Y^2=u^2+2uX\) and the row parabola vertex \(X=-u/2\). For fixed column x=u, \(Y^2=u^2-2uX\) and vertex \(X=+u/2\).

Therefore the **unit EM factor level** u=1 has vertices \(X=\pm1/2\), while the **half-scale gravitational factor level** u=1/2 has vertices \(X=\pm1/4\). This exactly instantiates v13.177's half-scale theorem. The gravitational quarter refers here to **vertex coordinates**; it is not a factor-lattice affine offset \(m+1/4\).

For a complete half-spaced multiplicative factor grid \(x=m/2,\ y=n/2\) with m,n positive integers, the count below the *same factor-product cutoff* N is exactly
\[
\#\{m,n\ge1: (m/2)(n/2)\le N\}
=\#\{m,n\ge1:mn\le4N\}=D(4N)
\]
(with appropriate floor if N is nonintegral). Conversely at fixed physical shell / cutoff rescaled by the factor-grid unit, the counts transform accordingly; one cannot compare D(N) and D(4N) without specifying shared dimensionless units.

## Scope correction to v14.765

The shifted count \(D_a(X)=\#\{m,n\ge0:(m+a)(n+a)\le X\}\) and its Hurwitz series \(\zeta(s,a)^2\) in v14.765 are mathematically valid **separate affine-shift models**, but no established Cone map forces a=1/4 from the gravitational vertex \(\pm1/4\). The quarter-Hurwitz \(\chi_{-4}\) contribution therefore must **not** be promoted as the actual gravitational global divisor spectrum. Similarly v13.362/364's normalized Walsh mixed-cell \(1/4\) is a third notion of a quarter, related to finite-difference normalization and not automatically the factor level or vertex.

## Consequence

The core proposed hyperbolic-slice insight remains exact in a more direct form: the same product hyperbolas meet differently scaled parabola grids, giving a precise global rescaling \(D(N)\mapsto D(4N)\) for a complete half-spaced grid. This alone is a scale law, **not** a nontrivial selector for the physical ratio of electromagnetic/gravitational couplings. Next physical gate requires defining which cutoff and measure are invariant in comparing EM and gravitational slices and deriving any additional asymmetry from the actual worldline/field action rather than counting the same lattice in changed units.

**Flags:** \`geometry_correction=EXACT\`; \`vertex_EM=1/2\`; \`vertex_gravity=1/4\`; \`gravity_affine_Hurwitz_quarter=NOT_DERIVED\`; \`half_grid_count=D(4N)\`; \`G_derived=false\`; \`Suzuki_sandbox_reserved=true\`.
