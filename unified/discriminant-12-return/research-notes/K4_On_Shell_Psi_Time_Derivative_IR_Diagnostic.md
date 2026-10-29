# v15.110 — Source-convention-safe on-shell scalar reconstruction IR time-derivative test
Date 2026-10-29. Gravity parent v15.109. Live repository checked, protected other lanes untouched.
Corrected v14.996 scalar_final2.py source directly fetched: it obtains original EL_B, EL_Phi, solPhi, solB, PhiS, reduced E1/E2, solpsi, solpsid and original residuals. No generated scalar_final.txt was observed in repository. In particular we must NOT infer source-convention lapse/shift by naively copying earlier opposite psi convention v15.038. Full quadratic Hamiltonian source gravity v15.107 and integrated result v15.109 remain formal before source-faithful first-order auxiliary substitution.

Externally audited scalar mode strain π solves πdd+3/τ πdot+(3k²+4)/τ² π=0 for nonzero k and ψ=(-k²π+τ πdot)/[3k²(1+k²)]. Differentiate exactly:
ψdot=[(1−k²)πdot+τ πdd]/[3k²(1+k²)]
=[−(k²+2)πdot−(3k²+4)π/τ]/[3k²(1+k²)].
If πdot(τ0)=0, ψ(τ0)=−π/[3(1+k²)] regular, while τ0 ψdot(τ0)=−(3k²+4)π/[3k²(1+k²)] has 1/k² enhancement as k→0 when strain does not vanish sufficiently. This is a mode-level exact diagnostic, NOT claim of physical instability: lapse/shift, gauge constraints, nonlinear h2, potential low-k admissibility and full second-order source may compensate. Spatial Laplacian of ψdot is regular: −k² τ ψdot=(3k²+4)π/[3(1+k²)] for initial πdot=0; physical curvature derivatives merit preference over raw metric time derivatives.

A smooth family of k-mode test data at k>0 need not be admitted with uniform H^r norm for all constraints, so no direct contradiction established. Next step: run original scalar_final2.py and collect source-faithful PhiS and solB with original EL residual checks; then substitute source coefficients into full quadratic H2 and test low-output Fourier convolution and order-two H1[U2] compatibility. Do not overclaim the full substitution as performed.

Source status: original scalar_final2.py READ; reconstructed ψ and its derivative ANALYTICALLY CHECKED; α/β SOURCE_COEFFICIENTS NOT_EXTRACTED; physical H2-on-shell NOT_COMPUTED. Suzuki physical quarter weld parked; protected lanes untouched.
