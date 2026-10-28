# v15.049 — ADM shift cancels scalar displacement inverse-k in normal velocity
Date 2026-10-28. Source v15.038 constraint reconstructed directly, v15.044 reduced strain normalization verified by External Audit R387 v15.045. Live HEAD c25cec4c3c351971d4051430ad4d088b458c40db checked. Protected concurrent lanes untouched.

Conformal scalar spatial gauge: h_ij=a²(1+2ψ)δij, N=1+α, N^i=∂^i b, scalar displacement δφ^I=∂^I σ. Define longitudinal strain p:=Δσ (Fourier p_k=−k² σ_k). Corrected linear constraints v15.038:
 (1−Δ)b=dotσ+HΔσ−3Hψ+Δψ/(a²H),
 α=dotψ/H+(dotσ−b)/(3H).
Taking difference, (1−Δ)(dotσ−b)=−Δdotσ−HΔσ+3Hψ−Δψ/(a²H)=−dot p−Hp+3Hψ−Δψ/(a²H).
The normal scalar velocity n^μ∂μφI=(dotφI−N^j∂jφI)/N, at linear order v^I=∂^I(dotσ−b) (background normal velocity zero). Fourier:
 v^I_k = i k^I/(1+k²)[−dot p_k−Hp_k+(3H+k²/(a²H))ψ_k].
Therefore, for bounded p,dot p,ψ at low k, v is O(k), rather than raw coordinate dot δφ_k=−i k dot p_k/k²∼1/k. The leading 1/k cancels between dotδφ and shift. The bounded Fourier multipliers k/(1+k²) and k³/(1+k²) acting on ψ require Sobolev derivatives for high k but no IR pole. This is an EXACT first-order constrained normal-velocity identity in this gauge, not a full quadratic Einstein energy theorem. Note coordinate σ has 1/k² IR as potential and N^i can individually have 1/k, but normal kinetic is gauge-covariant.

Conditional log-time estimate: p=τ^-1 u, ψ=τ^-1 w with controlled u,u_s,w in Sobolev H^(r+3), r>3/2. Because dot p=τ^-2(u_s−u) and Hp=τ^-2u, first two brackets sum −τ^-2 u_s. 3Hψ=3τ^-2w, and (k²/(a²H))ψ=(3k²/τ)τ^-1w=3k²τ^-2w. So
 v_k= τ^-2 i k/(1+k²)[−u_s+3(1+k²)w] = τ^-2 i k[3w−u_s/(1+k²)].
Thus ||v||_H^r ≤ C τ^-2(||w||_H^(r+1)+||u_s||_H^r), uniformly at k→0. The fixed-background-style quadratic normal kinetic weighting τ² |v|² then O(τ^-2)=O(e^-2s) if r>3/2, as a bilinear first-order normal-velocity contribution. Unlike v15.043 raw fixed-shift coordinate kinetic, this IR-regular term accounts for *linear shift constraint* (but h, N and other second-order corrections remain, so no complete nonlinear source bound). Strain gradient term a^-2|p|² gives τ²-weighted O(τ^-2) as before. Need control ψ (not yet independently reconstructed from p at IR) and metric/constraint nonlinearities.

External audit handoff verify signs, gauge source, coefficients, conditional weighted bound and distinction normal vs coordinate velocity. Suzuki weld parked.
