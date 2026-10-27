# Covariant finite-strain longitudinal acoustic principal symbol: RMS elastic source

Date 2026-10-26. Parent gravity v14.970 and original elastic-source v14.925–928. Live HEAD checked a3115164de9dff1d3f1c7150254b11d4c1d5a4ca. Suzuki physical quarter link PARKED, protected spectral lanes untouched.

Use locally flat Minkowski spacetime signature +---, three scalar labels φ^I, B^IJ=−g^μν ∂μφ^I ∂νφ^J. Matter L=−W(B) with W(B)=C (detB)^(1/3) [1+ηJ(B)], J(B)=tr(B²)/(trB)²−1/3, C>0. At background φ^1=t x¹, φ²=x², φ³=x³, t>0, B0=diag(t²,1,1). The background has constant gradients and satisfies flat-space material Euler–Lagrange equations (∂ of constant stresses=0), but its stress generally does not solve coupled Einstein equations in flat geometry.

Take longitudinal perturbation φ¹=t x¹+π(τ,x¹), φ²=x²,φ³=x³. Then B11=(t+π')²−dotπ², others 1. Define scalar W(t)=C t^(2/3)[1+η((t^4+2)/(t²+2)²−1/3)]. L=−W(sqrt(B11)) locally near background B11>0. Expand to second order:
sqrt(B11)=t+π'−dotπ²/(2t)+O(π³), 
L^(2)= W'(t)/(2t) dotπ²−W''(t)/2 (π')².
Thus principal equation (W'/t) ∂τ²π−W'' ∂1²π=0 and c_L²=t W''/W' (provided W'/t>0). At t=1: W'=2C/3, W''=2C(8η−3)/27 hence c_L²(1)=(8η−3)/9=−1/3+8η/9, exactly prior healthy longitudinal speed at isotropy. For large t, W∼C(1+2η/3)t^(2/3), W'∼(2C/3)(1+2η/3)t^(−1/3)>0 for η≥0, W''∼−(2C/9)(1+2η/3)t^(−4/3)<0 and c_L²→−1/3. Therefore the longitudinal field suffers a genuine high-frequency gradient instability on sufficiently stretched, constant-gradient anisotropic backgrounds for all η≥0, including locally stable near-isotropic window 3/8<η≤3/2. This is a finite-background covariant matter principal-symbol obstruction, stronger than mere rank-one convexity failure.

Example η=3/4,C=1: c_L²(t=1)=1/3; at t=2 =1/13≈0.0769231; t=3≈−0.3312273; t=5≈−0.4657172; t=10≈−0.3978833. Sign transition t∈(2,3). Values are from analytic derivative substituted numerically, not fitting.

Scope: locally flat background is a valid matter solution with fixed metric but generally not an exact Einstein+matter solution; thus no claim that full coupled K4 global evolution accesses this deformed state. At high frequencies the matter principal symbol is relevant to well-posedness; Einstein lapse/shift constraints, all polarisations, curvature/finite-wavelength corrections, and anisotropic GR background remain not certified. A single unstable longitudinal mode suffices to refute globally stable material model over all positive B. Repair requires genuinely modified constitutive W(B), not merely invoking RMS positivity or increasing η. Any change may affect coasting w=−1/3 and local phonon speeds; audit required.

NEXT test replacement finite-strain penalties with controlled non-saturating response while preserving near-isotropy Hessian, e.g. convex determinant-compatible constructions; require physical selection rather than ad hoc. Keep Sandbox coupled SVT project separate.
