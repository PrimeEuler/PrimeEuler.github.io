# Cone Derivation Ledger v15.1236 — External Audit Round 619

**Date:** 2026-11-19
**Track:** External Audit
**Scope:** Independent verification of v15.1233, v15.1234, v15.1235

## Method

`git fetch origin master` + `git merge --ff-only` confirmed `544b480` as the head, three new entries since Round 618/v15.1232. Read all three in full.

## Lane A v15.1233

A further 64-state right extension (arcs 5162–5225, steps 1153–1216), direct-restart mechanism, correctly filed under `research-notes/`. Verified: hash manifest OK (`sha256sum -c`, all four files), no `ledger_version` field, certificate structure (64 records, arcs/steps/rebases/support all matching the ledger exactly), independent re-execution reproduces `certificate_sha256=bf10e8ad7d09b93f835e1ffad0669e00c03239452cc426e5676299521d1fe5e5` bit-for-bit. Union arithmetic independently recomputed: `{3177,...,4008} ∪ {4010,...,5225}` = 832+1216 = **2,048 arcs**, 5,971 uncovered — matches. 5161/5162 adjacency confirmed.

## Gravity v15.1234 and v15.1235 — oblique-mode Maxwell driving the full K4 scalar/vector/tensor curvature

v15.1234 extends the finite-time 3D Maxwell evolution (already verified in Round 617) to an oblique wavevector K=(1,0,1), computing a tensor-plus gravitational response; v15.1235 completes the same mode's scalar and vector sectors and assembles the full 3×3 electric-Riemann matrix. Both are substantially numerical (spectral FFT Maxwell propagation + SciPy ODE integration on three grids), so verification combined formula-level derivation with full independent re-execution.

**Coefficient checks (by hand).** For `η_s=3/4`, `|K|²=2`: `β_S=[8η_s(1+|K|²)−3|K|²]/3=4`, `β_T=3|K|²+8η_s/3=8`, `β_V=2η_s(4+3|K|²)/3=5` — all confirmed by direct substitution, matching the stated values exactly.

**Scalar forcing equation, re-derived symbolically.** Built the general sourced-P ODE forcing term (already established and audited in Round 616) with `J_ψ=J_Φ=−√3R/τ`, `J_B=−i√3|K|F_n/τ`, `J_B'=(−3|K|²Tnn+i√3|K|F_n)/τ²` as given, and confirmed symbolically that the `F_n` terms cancel exactly, giving forcing`(1)=9(3Tnn−R)/(2|K|²)` with **no** `F_n` dependence — matches the claimed `Pddot+3Pdot/τ+β_S P/τ²=9(3Tnn−R)/(2|K|²τ⁴)` exactly.

**Closed-form S(1), re-derived — caught and corrected an initial setup error of my own.** A first attempt kept `F_n` as a free symbol in `Φ_N(1)`'s direct `J_B'` term and got a result that didn't match; this was my own mistake, not the entry's — `F_n(1)=0` identically, since `B(1)=0` is the actual Maxwell initial condition and `F_n=n·(E×B)`. Redoing with `F_n(1)=0` correctly imposed gives exactly `S(1)=−3/(1+|K|²)·{(3/2)(3Tnn(1)−R(1))+|K|²(−3R(1)+4.5Tnn(1))}`, matching the ledger's formula exactly, and the stated numeric example (`R(1)≈0.00068121634, Tnn(1)≈0.00053543769 → S(1)≈−0.00211928629`) matched to the stated precision.

**Vector forcing equation, re-derived by hand.** Using the given `b_V=4τ/[√3(4+3|K|²)]`, `J_V=−√3F_e/τ`, so `b_V J_V=−4F_e/(4+3|K|²)`; converting the given conformal-time Ward `F_e,ξ=−i|K|T_ne` to a τ-derivative via `d/dτ=(√3/τ)d/dξ` and dividing by the given `K_V=2τ³|K|²/[3√3(4+3|K|²)]` gives exactly `−18iT_ne/(|K|τ⁴)` — matches the claimed vector equation `f''+3f'/τ+β_V f/τ²=−18iT_ne/(|K|τ⁴)` exactly.

**Riemann-coefficient formulas, cross-checked directly against the archived v15.787 code** (already read and independently verified in Round 616): v15.787's committed lines `fullV=-s.I*k*(s.diff(B,t)+B/t)/(2*a)` and `fullT=-(s.diff(gamma,t,2)+2*s.diff(gamma,t)/t)/2` match the entries' stated `V=−i|K|(B_V,dot+B_V/τ)/(2a)` and `T=−(γ''+2γ'/τ)/2` exactly, confirming these are genuinely sourced from the archived script, not invented. The tidal-matrix decomposition `E_ij=A_iso δij+S(n_in_j−δij/3)+V(n_ie_j+e_in_j)+T(e_ie_j−b_ib_j)` has every non-isotropic term individually traceless (confirmed: `tr[n_in_j−δij/3]=0`, `tr[n_ie_j+e_in_j]=2n·e=0`, `tr[e_ie_j−b_ib_j]=0`), so `tr(E)=3A_iso` follows automatically.

**Independent numerical re-execution.** Ran both committed scripts end-to-end from a clean environment:
- v15.1234 (all three grids N=32/48/64): reproduced every value in the published table exactly — `scalar_0`, `scalar_at_1.2`, `vector_1_at_1.2`, `tensor_plus_at_1.2`, `gamma_at_1.2`, `tensor_full_tide_at_1.2`, Ward energy/momentum residuals (and the parity-protected ~1e-21 null channels). Exit 0, `PASS`.
- v15.1235 (all three grids): reproduced `A_iso`, `S`, `V`, `T` at τ=1.2 exactly for all three resolutions, and the full 64³ Cartesian tidal matrix `[[−0.00019344,0,+0.00137392],[0,+0.00115108,0],[+0.00137392,0,+0.00181339]]` matched exactly; independently confirmed `tr(E)=3A_iso` numerically (`0.00277103...` both ways). Exit 0, `PASS`.

## Collision and freshness checks

`v15.1236` and "Round 619" both confirmed unused before this write. No other new commits landed during this check. `__pycache__` cleaned before this commit; final freshness check performed immediately before push confirmed no intervening changes.

## Verdict

**PASS (all three entries).** Lane A's v15.1233 is bit-exact. Gravity's v15.1234/v15.1235 are independently confirmed at every level checked: the β-coefficients, both forcing-equation derivations (one of which required catching and fixing my own initial setup slip — the kind of check this audit exists to make reliably, not to skip when inconvenient), the Riemann-coefficient formulas against the actual archived source, and full three-grid numerical re-execution matching the published tables exactly. Filed R4 coverage after v15.1233: 2,048 of 8,019 arcs, 5,971 uncovered. Gravity's oblique-mode result is explicit about its own scope (one Fourier mode's local curvature coefficient, not a real-space field or physical detector) and that framing holds up.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
