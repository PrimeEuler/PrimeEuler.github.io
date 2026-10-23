# Shifted divisor hyperbolas through half and quarter parabolic seats

2026-10-23. Parents v13.200, v13.362, v13.691, v13.984, v14.731, v14.764. No Suzuki sandbox assignment.

## Exact arithmetic model

For a>0, define D_a(X)=# {(m,n) in Z_{\ge0}²: (m+a)(n+a)≤X}, X>0. This is a precisely defined new shifted lattice model, not automatically the unique established Cone parabolic-seat displacement. At a=1 recover the standard summatory divisor function ∑_{k≤X}d(k) (for integer X). Exact floor sum:
\[
D_a(X)=\sum_{m=0}^{\lfloor X/a-a\rfloor}
\left(\left\lfloor\frac{X}{m+a}-a\right\rfloor+1\right),
\]
when X≥a²; zero otherwise.

For rational a=r/q in lowest terms, (m+r/q)(n+r/q)≤X iff (qm+r)(qn+r)≤q²X. Thus a=1/2 samples positive odd factors (2m+1)(2n+1)≤4X, while a=1/4 samples factors congruent to 1 mod 4, (4m+1)(4n+1)≤16X. **Correction to intuitive labels:** the half seat is residue 1 mod 2, i.e. 1 or 3 mod 4, not solely residue 2 mod 4. The local quarter shift 1/4 of v13.362 is a Walsh normalization of mixed curvature, not necessarily a literal shift of both factor coordinates by 1/4; identifying them requires an additional geometric transport.

The Mellin-Dirichlet transform of the positive factor pairs is exactly
\[
Z_a(s)=\sum_{m,n\ge0}((m+a)(n+a))^{-s}=\zeta(s,a)^2,\qquad \Re(s)>1.
\]
Thus
\[
Z_{1/2}(s)=(2^s-1)^2\zeta(s)^2.
\]
For quarter:
\[
\zeta(s,1/4)=\frac{4^s}{2}[(1-2^{-s})\zeta(s)+L(s,\chi_{-4})],\quad
Z_{1/4}(s)=\zeta(s,1/4)^2.
\]
This introduces an exact χ_{-4} character contribution and cross term in the quarter count; not a proof that other mod-12 characters or EM/G physical couplings have been selected.

Near s=1, \(\zeta(s,a)=1/(s-1)-\psi(a)+O(s-1)\) where ψ is digamma. By standard divisor hyperbola summation:
\[
D_a(X)=X\log X+[-1-2\psi(a)]X+O_a(\sqrt X)
\]
for fixed a>0, with X→∞ (coarse elementary hyperbola error bound). Consequently:
a=1 constant \(2\gamma-1\);
a=1/2 constant \(2\gamma+4\ln2-1\);
a=1/4 constant \(2\gamma+\pi+6\ln2-1\).
The leading X log X is unchanged, while the arithmetic offset produces exact different global linear constants. The π arises from ψ(1/4) identity and the mod-4 character L(1,χ4)=π/4, not a derived physical coupling.

Direct integer count examples from the floor sum:
X=10: (a=1,1/2,1/4) = (27,53,97)
X=100: (482,754,1204)
X=1000: (7069,9838,14358).

## Selector scope / next theorem
The count is a faithful example of *hyperbola slices giving global counts from seat offsets*. It also proves the offsets yield distinguishable arithmetic spectra. However a∈{1/2,1/4} was supplied by hand; neither the count nor its asymptotic coefficient fixes the continuous coupling split ψ of v14.759–760. To get a selector, a derivation must specify how the local Walsh quarter mode and the physical dyons determine a shift of the factor lattice and then exhibit an independent boundary/spectral variational constraint that fixes ψ, not just evaluate D_a(X) at a chosen a.

Next productive calculation: compare quarter/half residue-restricted Euler products and mod-12 character projections; test explicit transport of original x=const, y=const parabolas to the shifted grid, including the exact Jacobian, then ask whether a boundary value equation fixes a or ψ. No RH, zeta spectral assertion, α or G derivation.
