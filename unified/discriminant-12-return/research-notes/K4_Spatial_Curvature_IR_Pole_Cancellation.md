# v15.072 — Intrinsic spatial scalar curvature cancels audited psi reconstruction IR pole

Date 2026-10-28. Parent gravity v15.070/071. Rechecked live HEAD. Scope: source-faithful conformal spatial gauge h_ij=a²(1−2ψ)δij as in corrected v14.996 scalar_adm2.py. Parent prior v15.038 adopts h=a²(1+2ψ) which is the opposite psi convention; maintain sign explicitly. No claim fully time-diffeomorphism-invariant observable.

For conformal spatial metric, linear spatial scalar curvature R3(1)=+4a^-2 Δψ. Audited corrected source reconstruction (External Audit v15.063) ψ_k=[−k²π_k+τ dotπ_k]/[3k²(1+k²)] for k≠0. Fourier Δψ=−k²ψ=(k²π−τ dotπ)/[3(1+k²)]. Therefore exact at linear order
 a² R3_k(1) = (4/[3(1+k²)])(k²π_k−τ dotπ_k).
For π=τ^-1u(s), τdotπ=τ^-1(u_s−u), obtain a²R3_k(1)=4/(3τ)[u_k−u_s,k/(1+k²)]. The Fourier multipliers 1 and 1/(1+k²) are uniformly bounded at k→0. For r≥0, ||a²R3(1)||_H^r ≤4/(3τ)(||u||_H^r+||u_s||_H^r), hence ordinary mode energy controls the spatial-curvature quantity without inverse Laplacian weighting, for smooth integrable-data modes. This is a *linear spatial gauge/slicing* statement. R3 of a foliation has gauge-invariant perturbation under infinitesimal spatial diffeomorphisms because flat background R3=0; under time-slicing change R3 of new slices can change, so not automatically a full spacetime gauge invariant. Physical local curvature tensors and matter-defined slicing deserve separate analysis.

Stronger unscaled R3(1)=a^-2 times above, so O(τ^-3) under bounded u,u_s. No new nonlinear constraint estimate; second-order R3 includes products (∇ψ)² and ψΔψ, potentially still carries undifferentiated ψ inverse-k and may challenge closure. Generic weighted Sobolev product obstruction v15.071 remains. Do not claim global future stability.

Next: test second-order intrinsic curvature in a matter-defined slicing or gauge-invariant geometric variable; inspect quadratic ψΔψ and (∇ψ)² terms for near-zero convolution and physical cancellations. Muse v15.069 coupling/source scope unchanged, Suzuki physical-quarter weld parked.
