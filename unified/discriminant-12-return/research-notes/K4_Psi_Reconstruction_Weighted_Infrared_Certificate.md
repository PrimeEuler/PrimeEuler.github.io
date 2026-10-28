# v15.070 — Returned ψ reconstruction certificate and exact infrared weighted condition
Date 2026-10-28. Directly read External Audit v15.063 (Round 392): audited execution of gravity v15.061 source-faithful psi_certificate_runner.py, matching independently executed v14.996 scalar_final2.py in Audit Round 390. Newest HEAD checked; separate Sandbox and Lane A work untouched, Suzuki physical-quarter weld parked.

Certified exact reconstruction for scalar strain π (nonzero k):
ψ_k = [−k² π_k+τ dotπ_k]/[3k²(1+k²)].
Decomposition A(k)=−1/[3(1+k²)] regular at k=0, B(k)=τ/[3k²(1+k²)] singular 1/k². This is EXTERNAL AUDIT VERIFIED, unlike our prior unexecuted inference v15.052. Corrected scalar oscillator πdd+3/τ πdot+(3k²+4)/τ² π=0, with π=τ^-1 u(s), s=ln(τ/τ0), u_ss+3(k²+1)u=0. Then τ dotπ = τ^-1(u_s−u) and
ψ_k = τ^-1/[3(1+k²)] [−u_k+(u_s−u)_k/k²].
At any fixed k≠0 bounded oscillator energy ensures ψ=O(τ^-1), but the norm bound on R³ is
||τ ψ||_{H^r} ≤ (1/3)[||u||_{H^r}+|| |∇|^-2(u_s−u)||_{H^r}],
assuming Fourier mode k=0 treated separately. The second term is NOT bounded by ordinary H^r oscillator energy; it requires a homogeneous low-frequency weight or cancellation/condition u_s−u=O(k²) under suitable Fourier pointwise hypothesis. This is an explicit necessary/sufficient weighted-norm criterion for the ψ multiplier formula, not assertion that all physical/gauge-invariant quantities diverge. Important: u_s−u=O(k²) at one initial s is generically NOT preserved under nontrivial k≈0 oscillator dynamics unless both u and u_s are suppressed near zero, because u_ss=−3(k²+1)u. A stable sufficient class is both u(s0),u_s(s0) controlled in H^r and |∇|^-2 H^r; their weighted oscillator energy is conserved modewise with frequency lower bounded √3. On a fixed T³ the inverse-k bound is finite for k≠0 but grows with box size; k=0 scalar-gauge ansatz special.

No conclusion full nonlinear instability or nonlinear time-uniform stability; actual nonlinear Einstein metric reconstruction, normal velocity, and nonlinear source may exhibit compensations in gauge-invariant combinations. The first-order ψ raw gauge variable is not uniformly controlled by unweighted strain oscillator norm on R³. Any global future bootstrap should use physically admissible weighted initial data, alternative gauge or gauge-invariant vars, and check constraints/convolution closure.

Next: derive concrete sufficient weighted oscillator energy and its conserved norm, test whether nonlinear quadratic convolution preserves that weighted class, or change to gauge-invariant energy. External audit of exact weighted statement warranted.
