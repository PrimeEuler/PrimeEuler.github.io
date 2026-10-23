# Cone intrinsic metric versus elliptic boundary operator

Date 2026-10-23. Gravity-only calculation. Parents v13.748, v14.768, v14.773, v14.780–783. [D] exact geometric/algebraic conclusions; [O] missing field dynamics.

## Cone coordinate pullback [D]

Let x,y>0, Y=sqrt(xy), β=(1/2)log(x/y), r=log(xy)=2log Y; x=Y exp(β), y=Y exp(-β). Define T=(x+y)/2=Y coshβ, X=(x-y)/2=Y sinhβ, so the unit cone relation T²-X²=Y² holds.

The symmetric bilinear quadratic form dx dy=dT²-dX² pulls back to
\[
\boxed{g_L=dY^2-Y^2dβ^2=e^r(dr²/4-dβ²)}.
\]
It has signature (+,-), not a Riemannian hyperbolic-plane metric. Consequently the scalar wave equation associated to g_L is hyperbolic, and ordinary elliptic boundary Dirichlet-to-Neumann conclusions from v14.781–783 cannot be transported without an extra choice of metric, analytic continuation, well-posed time evolution, or boundary prescription.

For reference, the Euclidean quadrant metric dx²+dy² pulls back instead to
\[
g_E=e^r[(\cosh2β/2)dr²+2\sinh2β\,dr\,dβ+2\cosh2β\,dβ²].
\]
This is positive definite, flat, and NOT the same quadratic form as dxdy. Thus even a positive operator must declare which metric is physically intended.

## Conformal representative and its precise scope [D]

A distinct positive metric choice is \(g_+=dY²+Y²dβ²=e^r(dr²/4+dβ²)\), the Euclidean polar metric in coordinates (Y,β). In two dimensions, its massless scalar Dirichlet integral is conformally equivalent to the flat strip metric \(du²+dβ²\), where \(u=\log Y=r/2\). For a rectangular strip \(u_i<u<u_o\), β periodic with period B, inner Dirichlet zero and outer constant Θ, its harmonic minimizer is Θ(u-u_i)/(u_o-u_i), giving
\[
\boxed{k_+=KB/(u_o-u_i)=2KB/(r_o-r_i)}.
\]
This is an exact model response for the explicitly chosen positive metric; not a unique intrinsic Lorentzian Cone stiffness. It depends only on the logarithmic radial width and angular/boost period B. Making β periodic is an extra quotient and not inherent in β∈R.

Uniform half-grid scaling (x,y)→(x/2,y/2) sends Y→Y/2, r→r-log4, β unchanged. If both radial boundaries scale together, their difference r_o-r_i remains the same, so k_+ remains unchanged. If one physical boundary is held fixed, this creates a changed width, conditional on a physically specified anchor.

## Physical selection verdict [D/O]

Cone factor coordinates distinguish an intrinsic Lorentzian form from optional positive geometries. They do not furnish a unique positive radial Dirichlet-to-Neumann stiffness or a coupling normalization. To derive G requires specifying a physical action and causal boundary problem, a sector embedding, and an operationally fixed source and geometric wall. The quarter vertex and unit-circle ħ interpretation remain consistent but do not force a source response ratio.

No Suzuki/Weil divisor carrier equivalence; no Suzuki/far-tail file touched.
