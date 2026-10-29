# Cone Derivation Ledger v15.125 — Sandbox Φ_a/T_a return for v15.115: T_a instantiated from source; Φ_a certified absent (source-level obstruction)

**Date:** 2026-10-29. **Lane:** sandbox (Little Euler). **Parents:** v13.661, v13.662, v13.785 (Suzuki finite-a source base named by the handoff), v15.095, v15.106, v15.108, v15.113, v15.115, v15.116; Audit R403 (v15.119), R404 (v15.122). **Status:** [D] T_a package (§1); [D, record fact] no source-prescribed coefficient synthesis exists (§2); part (b) therefore returns **NEGATIVE at the synthesis step** — the outcome v15.115 explicitly pre-authorized ("report that fact as OPEN/OBSTRUCTION rather than manufacturing one"). No Gram entries are computed, because no source Gram is defined. K_full gate unchanged: CLOSED_SCOPED_OBSTRUCTION (v15.018/v15.021). Production fence untouched.

**Pre-write collision check:** live HEAD v15.124 (gravity, homogeneous second-order response) at deposit time; v15.125 next free — the Φ_a return was drafted as v15.124 and renumbered on this collision. Additive only.

## 1. The T_a side — instantiated from the source [D]

Everything Lane A's criterion (v15.116) needs on the operator side is fixed by the source record:

- **Space:** functions on the finite interval (−a, a); L² side ℋ_a⁰, and the energy space ℋ(T_a) with inner product ⟨f, g⟩_T = ⟨T_a^{1/2}f, T_a^{1/2}g⟩_{L²} (the T-energy form of v15.113 §1 — not the L² form; the two Grams differ and are not conflated here).
- **Operator:** B_a = D* G_a D with D(B_a) = H₀¹(−a, a); A_a = Friedrichs(B_a), with D(A_a) ⊋ D(B_a) strictly (v13.662 §1 — A_a is not a Dirichlet second-order operator, and no local Dirichlet Laplacian is substituted anywhere in this return). **T_a = A_a − λI** (v13.662 §4).
- **Gap datum:** the source's own spectral resolution has μ_{n,a}^± > 0 and the resolvent bound ‖T_a^{−1}‖ ≤ (λ_a − λ)^{−1} (v13.785 §8), i.e. the ε_a of v15.116 exists as source data: ε_a := λ_a − λ > 0 in the source's parameter range.
- **Transfer:** the exact isometric D̄ : ℋ(T_a) → ℋ(S_a), S_a = G_a − λ(−Δ_N)^{−1}; the first-order operators on the two energy spaces are unitarily equivalent (v13.662 §4). D̄ maps between two source energy spaces; it is not an intertwiner onto K_full (v15.095).
- **Boundary data:** deficiency pair v_± with equal T_a-norm, h_a = ‖v_+‖²_{T_a}; Γ₀f = √h_a(a+b), Γ₁f = i√h_a(a−b); reference extension H_{a,π} = ker Γ₀ (v13.661 §§1–2).

## 2. The Φ_a side — certified absent [D, record fact]

The handoff's step 2 asks for a **source-prescribed** synthesis Φ_a with Φ_a e_m = φ_m for the frozen modes (spike m₁ and a partner). A full read of the source base gives a complete inventory of its prescribed function-level data:

1. the deficiency/resolvent pair fixed by **T_a v_{+i} = e^x, T_a v_{−i} = e^{−x}** with unit source normalization (v13.785 §1) — two specific functions, parity pair w_e = T_a^{(+)−1} cosh, w_o = T_a^{(−)−1} sinh;
2. the trace representers **q_{0,a}(y) = k_a(0, y)**, **q_{1,a}(y) = ∂_x k_a(0, y)** of the raw kernel k_a (v13.785 §§5, 7);
3. the abstract spectral resolution {μ_{n,a}^±, φ_{n,a}^±} of T_a (v13.785 §8) — existence and parity only: no closed form, no normalization beyond orthonormality, and **no identification of its index n with any external label**;
4. the characteristics W(a, θ; z), the Weyl function m_a, and the boundary determinant of v13.661 — scalar spectral data, not functions indexed by modes.

**No sequence (φ_m) indexed by the frozen K_full modes, and no map from the frozen index data (m, z_m, p_m, d_m) to functions on (−a, a), is prescribed anywhere in the source.** The frozen index set is the project's own far-construction data; Suzuki's finite-a construction contains no such labels. A replayable sweep (payload) confirms the negative mechanically: zero hits for any synthesis/sequence-family pattern in the source base, and zero sequence-family hits across the whole v13.640–v13.799 Suzuki digest (160 files; the word "synthesis" occurs there only in the unrelated tetrahedral-control thread).

The two conceivable manufactures both fail the provenance standard, for the record:

- **Eigenbasis identification** (set φ_m := φ_{m,a}^±): the index identification n ↔ m is not in the source, and the route is not a test — with an orthonormal synthesis the Gram is the identity by construction, and the intertwining would then demand that the frozen K be the matrix of a fixed source operator in its own eigenbasis, which is the conclusion dressed as a hypothesis.
- **Resolvent dressing of invented inputs** (φ_m := ψ_m for hand-chosen ψ_m, f_m = T_a^{−1}φ_m): the v15.108 candidate family is legitimate only for *source* test functions; the source supplies the finite list in items 1–2 above, none of them sequence-indexed. Choosing ψ_m to reach the spike is fitting, forbidden by v15.095/v15.115.

**Conclusion:** v15.116's conditional bound G_a = Φ_a* T_a^{−1} Φ_a ≤ B_a²/ε_a cannot be instantiated — not because a bound fails, but because Φ_a does not exist as source data, so B_a has no object. The ε_a of §1 is real but bounds T_a^{−1} alone; it does not create a synthesis.

## 3. Consequences and scope

- **Part (b) of the bridge test closes as scoped**: the source-native Gram witness does not exist, at the first step (synthesis), before any Gram, leakage, or intertwining computation is defined. Part (a) (v15.106) is unaffected: diagonal weights for the unchanged matrix collapse to plain ℓ² up to constants, and §2 closes the remaining alternative — no non-diagonal source Gram can be produced from this source either.
- The v15.018 provenance obstruction is thereby **sharpened from "no realization found" to a located absence**: reopening item 1 (Hilbert space/weights) has no source-native weighted candidate, and the only honest reopening path for the Gram route is new source material that actually prescribes a coefficient synthesis (a Suzuki text or a certified ledger construction supplying φ_m from source data). Searching harder inside the present source cannot change this verdict.
- This is a provenance verdict under the project's source standard, **not** a theorem that no realization of K_full exists by any means, and not a self-adjointness result in either direction. The plain-ℓ² completion remains the only candidate the record supports; its canonical selection is still unproved, and the gate stays closed.

**Payload:** `payloads/phia_ta_return_v15_125/` — `source_synthesis_sweep.py` + `sweep_output.txt` (the replayable absence sweep over the source base and digest range). Source entries read in full from the deposited ledger: v13.661, v13.662, v13.785; criteria re-read: v15.113, v15.115, v15.116.

**Production fence:** unchanged — no spectral promotion, no residual consumer, far rerun, stationarity, or capacity claim; C_S_32000, 3e-5, 0.002 untouched; no charges repeated. Suzuki physical-quarter weld PARKED.
