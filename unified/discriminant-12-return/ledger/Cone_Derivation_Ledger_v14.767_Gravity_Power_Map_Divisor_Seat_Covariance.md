# Cone Derivation Ledger v14.767 — Power-map equivariance of half/quarter vertex grids and divisor hyperbola counts

**Date:** 2026-10-23 EDT. **Lane:** gravity/divisor geometry. **Parents:** v13.177, v13.200–202, v13.691, v14.550, v14.765–766. **HEAD/collision:** immediately before this write \`8a86f173de43aaada3c8d1fc80a5fe22d07060d9\` and v14.767 unoccupied. **Research note:** \`research-notes/Gravity_Power_Map_Divisor_Diameter_Seat_Covariance.md\`. Additive only, Suzuki sandbox and far-tail untouched.

## Exact unit-grid transport [D]
For primitive factor level u, row/column parabolas \(Y^2=u^2\pm2uX\) have vertices \(\mp u/2\). Hence EM u=1 has ±1/2 vertices and the proposed gravitational u=1/2 has ±1/4 vertices. On the pair (un,u), the full circle diameter \(d=u(n+1)\), offset \(o=u(n−1)/2\), half-chord \(h=u\sqrt n\) obey \((d/2)^2=o^2+h^2\). Shape invariants \(h/d=\sqrt n/(n+1)\) and \(2o/d=(n−1)/(n+1)\) do not depend on u.

## Conjugated parabolic power [D]
The raw Paper-B coordinatewise map \((x,y)\mapsto(x^k,y^k)\) does not preserve a half-grid unit; the unit-preserving normalized version is
\[
\mathcal P_{k,u}(x,y)=\big(u(x/u)^k,\;u(y/u)^k\big).
\]
For integer k≥1 it preserves the u-scaled positive integer factor lattice and maps (un,u) to (un^k,u), so \(n\mapsto n^k\), \(s=\tfrac12\log(x/y)\mapsto ks\). It is NOT an unconditional identification with the normalized Lorentz eigen-coordinate power map of Paper B; its circular compactification obeys \(\tan(\theta'/2)=\tanh(ks/2)\), not θ'=kθ.

## Arithmetic test [D]
At physically scaled shell \(xy=u²n\), integer lattice contacts are exactly \(d(n)\); the summatory count through \(xy=u²N\) is exactly \(D(N)\). At the same unscaled physical product cutoff X, u=1 gives \(D(\lfloor X\rfloor)\) and u=1/2 gives \(D(\lfloor 4X\rfloor)\). The latter comparison changes the dimensionless shell index, so cannot by itself derive a coupling hierarchy. Power maps inject divisor contacts on n into those on n^k but typically do not surject: d(12)=6 whereas d(144)=15.

## Outcome / selector burden
This closes the precise power-map/diameter/quarter-vertex geometry the user identified: both d(n) slices and D(N) counts see the u-scaled parabola vertices and are covariant under the normalized power. But after matching dimensionless product level, the counts and shape are identical. **Arithmetic and dilation alone leave the EM/G selector unfixed.** A physical boundary action/cutoff that is fixed independently of those units is the next necessary ingredient; evaluate it before claiming G, α, CFS matching, or a hierarchy. v14.765's quarter-Hurwitz translation is a different arithmetic model, not a consequence of the quarter vertex.

**Flags:** \`diameter_power_covariance=EXACT\`; \`shell_count_d(n)=EXACT\`; \`global_count_at_matched_shell_D(n)=EXACT\`; \`physical_selector=OPEN\`; \`G_derived=false\`; \`Suzuki_sandbox_reserved=true\`; \`far_tail_touched=false\`.
