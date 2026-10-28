# v15.053 — Independent linear triplet wave-equation compatibility for scalar ψ reconstruction

Date 2026-10-28. Parent gravity v15.052 and v15.049. Live HEAD checked, no deposited Sandbox reconstruction certificate. No protected lanes touched, Suzuki physical-quarter weld parked.

Exact canonical source field equation is □g φI=0, equivalently ∂μ(√−g g^μν∂νφI)=0. In ADM +--- signature and gauge h_ij=a²(1+2ψ)δij, N=1+α, N^i=∂i b, φI=zi+∂Iσ, expand to first order around homogeneous a and zero scalar normal velocity. The time density is √−g g^{tν}∂νφI=a³∂I(dotσ−b). The spatial density is √−g g^{jν}∂νφI=−a[δjI(1+α+ψ)+∂j∂Iσ]. Therefore wave divergence = ∂I{∂τ[a³(dotσ−b)]−a[Δσ+α+ψ]}=0. For nonzero longitudinal k, bracket=0; homogeneous integration function needs independent boundary/gauge specification.

As v15.038 constrained equations yield α=dotψ/H+(dotσ−b)/(3H), (1−Δ)b=dotσ+HΔσ−3Hψ+Δψ/(a²H), any candidate reconstructed ψ must satisfy this wave equation as well as corrected quadratic ADM Euler equations. This is a genuinely independent, source-faithful first-order consistency equation. It does not yield psi_sol coefficients by itself and no uniform k or late-time decay estimate of ψ is claimed.

Strong caveat: v14.996 raw scalar mode has φ3=z+π(t)sin(kz)/k while this σ scalar gauge has displacement ∂zσ; map must respect Fourier phases and p=Δσ signs. Missing certificate still requires actually executing corrected scalar_final2.py or otherwise symbolically extracting psi_sol and checking unreduced Euler residuals. No asynchronous sandbox completion claimed.

NEXT: reconstruct ψ and exact Fourier multiplier with independent wave-equation residual; determine k→0 and time-weighted bound before future stability bootstrap.
