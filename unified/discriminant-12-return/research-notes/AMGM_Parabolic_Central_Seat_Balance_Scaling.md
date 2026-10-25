# AM–GM central-seat balance: opposing parabolic grids and stiffness scaling

Date 2026-10-25. Gravity side lane. Parents v13.177, v14.550, v14.767, v14.827–836. Ledger HEAD at initiation f9f7728a (v14.855 audit liveness). No Suzuki/far-tail writes.

## Exact geometry [D]
Set T=(x+y)/2, X=(x-y)/2 and Y=sqrt(xy), with x,y>0. Then T²=X²+Y². The fixed row y=u yields Y²=u²+2uX, vertex X=-u/2; fixed column x=u yields Y²=u²-2uX, vertex X=+u/2. These opposing parabolas intersect at seat (X,Y)=(0,u) where x=y=u. The vertices are NOT themselves at the seat.

Hold T=u and displace X=δ (so x=u+δ, y=u-δ, |δ|<u). Then Y=sqrt(u²-δ²) and the AM–GM gap
\[
\Delta_u(\delta)=T-Y=u-\sqrt{u²-\delta²}
=u[1-\sqrt{1-(\delta/u)^2}].
\]
It is even and positive away from δ=0. Differentiating:
\[
\Delta'_u(\delta)=\frac{\delta}{\sqrt{u²-\delta²}},\qquad
\Delta''_u(\delta)=\frac{u²}{(u²-\delta²)^{3/2}},
\quad\Delta''_u(0)=1/u.
\]
This is a geometric *balance deficit*, not automatically a physical energy. The displacement path T=constant is different from moving along either fixed-factor parabola y=u or x=u; thus the restoring prescription selects a transverse fixed-T slice, which must be disclosed.

## Example energy with an independently declared normalization [D/I]
If a model explicitly defines E_u(δ)=A(u)Δ_u(δ) with A(u)>0 of dimensions energy/length in the physical interpretation, then restoring generalized force is
\[
F_\delta=-A(u)\,\frac{\delta}{\sqrt{u²-\delta²}},\quad
k_{\rm seat}(u)=E_u''(0)=A(u)/u.
\]
For EM grid u=1 and G interlay u=1/2, the raw stiffness ratio is
\[
k_{\rm seat}(1/2)/k_{\rm seat}(1)=2A(1/2)/A(1).
\]
Thus choosing identical A gives raw ratio 2; choosing the same dimensionless energy scale E_* via E_u=(E_*/u)Δ_u produces a raw ratio 4. Neither normalization is preferred by bare Cone geometry.

Define ξ=δ/u and normalized energy E_u/E_*=1-sqrt(1-ξ²) under the fixed E_* prescription. Then the dimensionless seat curvature \(\partial^2(E_u/E_*)/\partial\xi^2|_0=1\) is EXACTLY identical in both grids. The normalized force curve is also identical. The half/quarter vertex separation is pure common dilation until an independently measured energy/displacement ruler or dynamic action breaks it.

## Explicit limits
The model is a potential ansatz based on an AM–GM deficit; it does not derive the physical force from the parabolas alone, and it is not the same as the previously modeled mechanical double-paraboloid rotor. No continuum elastic modulus, gravitational coupling, or hierarchy can be inferred from the raw ratio without independent normalization. Next test might use a scale-sensitive causal/boundary action with a fixed common physical unit to determine A(u) rather than choose it.
