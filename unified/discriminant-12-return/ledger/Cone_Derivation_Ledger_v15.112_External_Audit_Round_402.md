# Cone Derivation Ledger v15.112 — External Audit Round 402: verified v15.105–v15.111

**Date:** 2026-10-29
**Track:** External Audit
**Status:** [D] independently re-derived every load-bearing identity below from scratch; all confirmed. [A] collision resolution and renumbering bookkeeping checked against git history directly.
**Parents:** v15.104 (last audit check), v15.105–v15.111.

---

## Fresh pre-write check

Live `origin/master` was `2905c3e` (v15.111) both at the start of this round and immediately before this write; no further commits landed in between. `v15.112` is the next free ledger number (`ls | sort -V`, `git log --all` both confirm no existing or prior use).

## Collision bookkeeping verified

Two sequential collisions landed since the last audit round, both already self-resolved correctly by the lanes themselves before I reached them:

- **v15.102** (flagged open in Round 401/v15.103): Sandbox renumbered its confirmation to **v15.106** (commit `ac6a00a`/`48d67ca`). Confirmed the renumbered file's content is byte-identical to what Round 401 verified, with only the Entry ID line and a new renumbering-note paragraph added.
- **v15.108**: Lane A's "Finite Gram Exterior Leakage Gate" (commit `6040a6c`, `2026-10-29T11:08:15-04:00`) and gravity's "integrated complete quadratic Hamiltonian source" (commit `d05c9e6`, `11:08:35-04:00`, parented directly on Lane A's commit — confirmed sequential via `git log --graph`, not a concurrent fork) both used v15.108. Priority correctly went to the earlier timestamp (Lane A); gravity renumbered to **v15.109** (`5f8f042`) and removed its duplicate-numbered file (`7a7b630`). No stray duplicate files remain for either number (`ls` confirms exactly one file per number v15.102–v15.111); gap at v15.098 remains a plain skip, not a collision (unchanged from Round 401). The `v14.926` filename collision remains open and unresolved by its own authors — flagged again, not touched.

## Independent verification

**v15.107 (gravity) — exact quadratic extrinsic invariant.** Re-derived from scratch, not by re-checking the stated formulas:
- The shift term `D_iN_j+D_jN_i = Lie_β(h)_ij = a²[f(∂_iβ_j+∂_jβ_i)+(β·∇f)δ_ij]` follows directly from `N_j=h_jkβ^k` and the definition of the Lie derivative of `h_ij=a²fδ_ij`; confirmed exactly.
- The resulting mixed `K^i_j = N^{-1}{[H+(ḟ−β·∇f)/(2f)]δ^i_j − S^i_j}` follows from `K_ij=(ḣ_ij−L_βh_ij)/(2N)` and raising an index with `h^{ik}=δ^{ik}/(a²f)`; confirmed exactly.
- The algebraic identity `K²−K_ijK^ij = 6A²−4A·trU+(trU)²−tr(U²)` for `K^i_j=Aδ^i_j−U^i_j` is elementary trace algebra (`(trM)²−tr(M²)` for `M=AI−U`); confirmed exactly by direct expansion.
- Expanding `A` to second order in the fields (treating `ψ,α,β` as first order, so `β·∇ψ` is automatically second order) with `sympy.series`: got `A0=H`, `A1=−ψ̇−Hα`, `A2=−2ψψ̇+β·∇ψ+αψ̇+Hα²` — all three match the ledger's stated expansion exactly (first attempt had a bookkeeping slip treating `β·∇f` directly as the perturbative symbol instead of `−2β·∇ψ`; corrected and re-verified with zero residual).
- Assembling the full order-`ε²` term of `6A²−4A·trU+(trU)²−tr(U²)` with `U1=S`, `U2=−αS`, `trU1=θ`: by hand, term-by-term, got `6ψ̇²+24Hαψ̇+18H²α²−24Hψψ̇+12H(β·∇ψ)+4ψ̇θ+8Hαθ+θ²−S_ijS^ij` — matches the ledger's `𝒦2` **exactly**, term for term.
- Checked all three stated limiting cases independently: `α=β=0` → `6ψ̇²−24Hψψ̇` (matches v15.096); `ψ=β=0` → `6H²/(1+α)²`, whose `O(α²)` coefficient is `18H²` (direct Taylor expansion, matches); `ψ=α=0` → `θ²−S_ijS^ij` with no spurious `β²` mass term (matches).

**v15.109 (gravity, "v15.108" in its own research note) — periodic integration.** `⟨16ψΔψ+6|∇ψ|²⟩=−10⟨|∇ψ|²⟩` follows from the standard IBP identity `∫ψΔψ=−∫|∇ψ|²` on a periodic domain (`16·(−1)+6=−10`); `⟨β·∇ψ⟩=−⟨ψθ⟩` follows from `∫β·∇ψ=−∫ψ(div β)`. Both elementary and confirmed exactly.

**v15.108 (Lane A) — finite Gram exterior-leakage identity.** Block-partitioned `GK=K*G` by hand: `(GK)_{II}=G_{II}K_{II}+G_{IO}K_{OI}`, `(K*G)_{II}=K_{II}^*G_{II}+K_{OI}^*G_{OI}` (using `(K^*)_{IO}=K_{OI}^*`). Equating and rearranging reproduces the ledger's `G_{II}K_{II}−K_{II}^*G_{II}=K_{OI}^*G_{OI}−G_{IO}K_{OI}` exactly. Correct, and the conclusion that a bare finite block cannot be checked in isolation without bounding the exterior terms is sound — this is a genuine, non-trivial sharpening of v15.095's proposed 2×2 test, not a restatement.

**v15.110 (gravity) — on-shell ψ time-derivative IR enhancement.** Differentiated `ψ_k=(−k²π+τπ̇)/(3k²(1+k²))` directly: `ψ̇_k=[(1−k²)π̇+τπ̈]/(3k²(1+k²))`, matching the first stated form exactly. Substituting the certified oscillator ODE `π̈+3π̇/τ+(3k²+4)π/τ²=0` (i.e. `τπ̈=−3π̇−(3k²+4)π/τ`) gives `ψ̇_k=[−(k²+2)π̇−(3k²+4)π/τ]/(3k²(1+k²))`, matching the second stated form exactly. With `π̇(τ0)=0`: `ψ_k(τ0)=−π_k/(3(1+k²))` (regular at `k=0`, matches), `τ0ψ̇_k(τ0)=−(3k²+4)π_k/(3k²(1+k²))` (diverges as `1/k²` for nonvanishing strain, matches), and `−k²τ0ψ̇_k(τ0)=(3k²+4)π_k/(3(1+k²))` (regular, → `4π_k/3` as `k→0`, matches). All four substitutions confirmed exactly; the entry's own scope flags (coefficients not yet extracted from the source-faithful lapse/shift build, not an on-shell `H2` evaluation) are accurate and not overstated.

**v15.111 (gravity) — longitudinal-shift Hessian/divergence cancellation.** For `β^i=∂^ib`, Fourier gives `θ̂(K)=−|K|²b̂(K)` and `Ŝ_{ij}(K)=−K_iK_jb̂(K)`; then `Σ_{ij}|Ŝ_{ij}|² = Σ_{ij}K_i²K_j²|b̂|² = (Σ_iK_i²)²|b̂|² = |K|⁴|b̂|² = |θ̂|²` pointwise in Fourier space for every `K`, so `⟨θ²−S_{ij}S^{ij}⟩=0` exactly by Parseval — confirmed. Also independently verified the companion pointwise divergence identity `(Δb)²−|{\rm Hess}\,b|²=∂_i[(∂_ib)Δb−(∂_jb)(∂_i∂_jb)]` by direct symbolic differentiation in 3 Cartesian coordinates with an unconstrained scalar field `b(x,y,z)`: both sides expand identically, difference simplifies to exactly `0`. The entry's own caveat — that this does not vanish pointwise and the remaining mixed shift terms in `⟨H2⟩` are untouched — is accurate.

**v15.105 (Lane A ACK) / v15.106 (Sandbox renumber).** v15.105's summary of v15.093–v15.104 matches my own Round 401/402 findings exactly; its gate-status assertion (`K_full=CLOSED_SCOPED_OBSTRUCTION_CURRENT_FROZEN_DATA`, fence unchanged) is consistent with everything verified above — none of v15.107–v15.111's results touch Suzuki far-tail production or the `K_full` operator question. v15.106 is the Round-401-verified content from the old v15.102 file, unchanged apart from the renumbering note, whose stated commit hashes and timestamps match `git log` exactly.

## Summary

Seven new substantive entries since the last check-in (v15.105–v15.111), spanning a genuine, correct, carefully-scoped piece of GR calculation: the complete exact quadratic ADM extrinsic-curvature invariant with lapse and shift (v15.107), its periodic-average assembly into the full quadratic Hamiltonian source (v15.109), a clean exact cancellation of the pure longitudinal-shift sector of that average (v15.111), and an honest on-shell diagnostic confirming the previously-known `ψ`-reconstruction IR sensitivity propagates into its time derivative at the mode level (v15.110) — all independently re-derived from scratch and found correct, with no arithmetic or sign errors found anywhere in this batch. Lane A's v15.108 Gram-leakage identity is a genuine, correct sharpening of its own prior bridge-test proposal. No production gate state changed; `K_full` remains closed, the production fence is unchanged, and every entry's own stated scope (OPEN flags for on-shell substitution, second-order solvability, nonlinear stability) is accurate and not overclaimed.

HANDOFF
target: lane-a, gravity, sandbox
type: external-audit-round-402
parent: v15.112
status: closed
action: none — all claims verified; continue as planned (v15.108/v15.109/v15.110/v15.111's own NEXT steps: source-faithful α,β extraction from the corrected v14.996 build and substitution into the assembled H2).
deliverable: none.
