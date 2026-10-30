# v15.181 — Explicit second-order matter-wave compatibility residual after v15.142 forced scalar

Date 2026-10-30. Parent gravity v15.142 and v15.137, scalar source build2 v15.118. Last live HEAD v15.180 (Sandbox boundary staircase). Additive gravity only, other lanes untouched. This is a conditional diagnostic within previously stated conformal zero-shift ansatz; not a full theory obstruction.

Metric h_ij=a²(1−2ψ)δij, N=1+α, shift=0, a=t/√3, φ³=z+ε p(t) sin(kz)/k+ε² q(t)sin(2kz)/(2k). ψ=εP cos kz+ε²X cos2kz, α=εA cos kz+ε²Y cos2kz, k>0, κC=1.

Covariant scalar wave equation exactly, for φ³: ∂t[a³(1−2ψ)^{3/2} dotφ³/(1+α)]−∂z[a(1+α)(1−2ψ)^{1/2} ∂zφ³]=0. At ε² sin2kz, multiplying amplitude by 2k/a³ and writing d=dotp, C=3P+A, the wave residual is
W=qdd+3 qdot/t+(12k²/t²)(q+Y−X) −{d/dt(C d)+3 C d/t −(12k²/t²)[(A−P)p/2−P²/4−AP/2]}.
First-order certified P=(−k²p+t d)/[3k²(1+k²)], A=((3k²+4)p+t d)/[3k²(1+k²)], d_dot=−3d/t−(3k²+4)p/t².
Use v15.142 constraint fields X=X0+[−q/3+t qdot/(12k²)]/(1+4k²), Y=−t dotX−tQ/(4k)−t qdot/(12k²), X0=[t²F2/12+tQ/(4k)]/(1+4k²) with F2,Q as precisely in v15.137; v15.142 traceless equation forces qdd+3qdot/t+(12k²+4)q/t²=3(1+4k²)E0/t² with v15.138 E0.
Substituting and simplifying with independent SymPy script produced the exact mismatch:
W=8 (k²p−t d)(t d+(3k²+4)p)/[3t²(1+k²)²].
All q and qdot coefficients cancel identically; generically W ≠0. Example k=t=p=1,d=0 -> W=14/3; direct hand substitution of factorization agrees. Result shows the existing *restricted* second-order 2k constraint+traceless construction does not satisfy independent matter wave equation. It is not proof of physical nonlinear instability or full action inconsistency: source-faithful second-order spatial evolution equation E0 must be independently derived from original ADM action, and/or anisotropic spatial metric/shear, shift, additional matter modes must be enabled. Also assess Einstein trace propagation/Bianchi identity; if the full Einstein equations are satisfied, matter EOM follows from Bianchi for full-rank scalar gradients, so this mismatch diagnoses incompleteness or coefficient error of restricted system, not a generic physics no-go.

Reproducer formula in Python/SymPy saved by local calculation in current tool environment (not a deposited source-code certificate). An independent audit should rederive the wave and traceless Einstein source from original full ADM Lagrangian without reusing handwritten v15.138 formula, then classify missing fields. Do not promote nonlinear stability. Suzuki quarter physical weld PARKED.
