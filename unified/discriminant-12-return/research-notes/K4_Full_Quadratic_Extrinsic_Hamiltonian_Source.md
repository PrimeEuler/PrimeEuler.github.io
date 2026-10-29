# v15.107 — Exact ADM extrinsic invariant through quadratic order, including lapse and shift
Date 2026-10-29. Parent gravity v15.102; current ledger v15.106 (renumbering collision resolved). Additive gravity only; protected Suzuki/Sandbox files untouched.
Metric: h_ij=a² f δij, f=1−2ψ, N=1+α, contravariant N^i=β^i, H=dot a/a. Define S_ij=(∂iβj+∂jβi)/2, θ=∂iβ^i. Lie derivative formula D_iN_j+D_jN_i=(L_βh)_ij=a²[f(∂iβj+∂jβi)+(β·∇f)δij]. Consequently exact mixed K^i_j=1/N{[H+(dot f−β·∇f)/(2f)]δ^i_j−S^i_j}.
Let A=[H+(dot f−β∇f)/(2f)]/N, U=S/N. Exact invariant K²−KijKij=6A²−4A trU+(trU)²−tr(U²).
Order expansion A0=H, A1=−dotψ−Hα, A2=−2ψdotψ+β·∇ψ+αdotψ+Hα²; U1=S,U2=−α S. Therefore degree-two contribution
𝒦2=6dotψ²+24Hαdotψ+18H²α²−24Hψdotψ+12Hβ·∇ψ+4dotψ θ+8Hαθ+θ²−SijSij.
Checks: α=β=0 gives v15.096 6dotψ²−24Hψdotψ. ψ=β=0 exact K²−Kij²=6H²/(1+α)² gives coefficient 18H²α². ψ=α=0 with β shift gives θ²−S² and no incorrect β² mass. No assumption of constrained first-order data made in deriving 𝒦2.

Combine with earlier exact conformal curvature R3_2=a^-2(16ψΔψ+6|∇ψ|²), and shift-restored triplet normal matter 2κρ2=(2/3)|dotπ−β|²+(2/(3a²))(|∇π|²+4ψ divπ+12ψ²), to obtain complete first-order-generated quadratic Hamiltonian residual 𝓗2[U1]=R3_2+𝒦2−2κρ2 in stated conformal spatial gauge. For actual second-order constrained data 𝓗1[U2]+𝓗2[U1]=0; not 𝓗2=0 separately. Arbitrary U1 need satisfy linear Hamiltonian and momentum constraint and scalar evolution; no zero-mode cancellation claimed. On periodic torus ∫β·∇ψ=−∫ψθ, so integrated advection combines with θ terms; full averaged source may be computed explicitly, but zero-mode solvability requires U2 and evolution. π as coordinate displacement; metric ψ source sign as in v14.996. Full nonlinear future stability remains open.

Next: substitute exact first-order constrained α,β,ψ reconstruction, test combined Hamiltonian quadratic source low-K behavior and compatibility with H1[U2], including spatial zero mode and weighted-norm closure. Audit formulas independently before any physical claim. Suzuki physical-quarter weld parked.
