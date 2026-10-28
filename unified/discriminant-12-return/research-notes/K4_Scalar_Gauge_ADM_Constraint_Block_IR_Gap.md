# Scalar gauge-fixed ADM auxiliary block with a positive infrared gap
Date 2026-10-28. Parents gravity v15.011, v15.013 and v15.010; live HEAD v15.037 concerns protected unrelated Lane A, untouched. Canonical Einstein+three triplet action in +---, κC=1, coasting a=τ/√3,H=1/τ. Conventions h_ij=a²(δij+εij), N=1+α,N^i=β^i, φI=zi+πI, Kij=(dot hij−DiNj−DjNi)/(2N), Πij=√h(K^ij−h^ijK)/(2κ), H_i=−2∂k(hijΠjk)+Πjk∂i hjk+pI∂iφI.

Previously v15.007 Π1ij=(a/2κ)[2H εij+dot εij/2−(∂iβj+∂jβi)/2+δij(2Hα−H trε−dot trε/2+divβ)]. Exact first order momentum constraint after cancellation of background metric products simplifies to
κ H_i^(1)/a³ = −(1/2)∂k(dotε_ik−δik dot trε)−2H∂iα+(1/2)(Δβ_i−∂i divβ)+(2/3)(dotπ_i−β_i)=0.
Check scalar gauge εij=2ψ δij, β_i=∂i b, π_i=∂iσ: H_i^(1)=∂i[2dotψ−2Hα+(2/3)(dotσ−b)], requiring bracket=0 for nonzero k. k=0 is homogeneous gauge/constraint mode and cannot be inferred from dividing spatial gradient.

Hamiltonian v15.011: a^-2(∂i∂jεij−Δtrε)+2H dot trε−4H divβ−12H²α−4H²divπ+2H²trε=0. In conformal scalar gauge:
−4a^-2 Δψ+12Hdotψ−4HΔb−12H²α−4H²Δσ+12H²ψ=0.
Eliminate α=dotψ/H+(dotσ−b)/(3H), obtaining
(1−Δ)b = dotσ+HΔσ−3Hψ+(Δψ)/(a²H).
In Fourier Δ→−k²:
b_k=[dotσ_k−Hk² σ_k−3Hψ_k−k²ψ_k/(a²H)]/(1+k²), α_k=dotψ_k/H+(dotσ_k−b_k)/(3H).
Thus the scalar auxiliary operator for (α,b) has no finite-k pole for k≠0 and a formal finite k→0 shift-potential multiplier; denominator 1+k². Under standard Fourier Sobolev spaces, (1−Δ)^−1 is bounded with two-derivative elliptic gain, but numerator involves dotσ, Δσ, Δψ and time factors, and scalar variable σ=(−Δ)^−1divπ has its own k→0 representation caveat. Physical longitudinal shift ∂b is more meaningful than homogeneous b.

Transverse vector part (div β_T=0, divπ_T=0, metric transverse spatial gauge ε_T=0) of momentum constraint: (1/2)Δβ_T+(2/3)(dotπ_T−β_T)=0, so (−Δ+4/3)β_T=(4/3)dotπ_T, i.e β_T,k=4dotπ_T,k/(3k²+4). This is in contravariant shift vector coordinates, not the V normalization of v14.996; same positive denominator and regular Fourier multiplier. Other vector metric gauge can shift representations. Lapse has no transverse contribution.

Caution: this is complete *linear constraint solution* in stated spatial gauge, NOT second-order source inversion or theorem of nonlinear stability. At τ→∞, α includes H^-1, and zero-mode/π^I=z^I torus winding need careful treatment; nonzero k operator is elliptic only in spatial sense. Crosscheck exact nonlinear derivative/gauge via external audit. Suzuki physical-quarter weld parked.
