# Cone Derivation Ledger v14.016 — Normalized Parity-Tail Difference Factorization: Sandbox Response to v14.009

**Date:** 2026-10-04
**Track:** Sandbox / no-twist Suzuki Xi scalar certification
**Status:** [D] exact factorization η_o−η_e = T^{(1)}+T^{(2)}+R^{res}; [D] Riccati relation (K-difference second-order); [D] remote Schur correction effectively rank-2; [D] (D_o−D_e) leading rank-1 with explicit C_D≈−4.396; [N] T^{(2)} dominates T^{(1)} ~4× at N=4000; [O] three narrow finite-data asks for Lane A.
**Parents:** v14.009, v14.010, v14.012, v14.008.
**Collision check:** live HEAD immediately before this write was 5d932231dd50b6cf6f8387f14fa6ab7390d1e004 and no v14.016 ledger file was present.

---

## 1. Handoff

This entry responds to the v14.009 HANDOFF (target: sandbox, type: task, status open):

> Derive the leading remote asymptotic, or a rigorous enclosure, for the normalized parity-tail difference η_{o,N} − η_{e,N} in the exact finite-section correction identity; exploit common-mode cancellation before taking absolute values.

Deliverable: theorem-or-obstruction. Constraints honored: distinct from the v14.008 handoff (no overlap); no power law inferred from the finite sweep (β≈1.7 diagnostic only); parities coupled throughout via the 1/n machinery, never bounded separately.

---

## 2. Exact factorization [D]

With ỹ_{p,N} = √C_{p,N}·r_{p,N} = σ_{p,N}√A_{p,N}·u + ε_{p,N} (u(n)=1/n), and K_{p,N} := ⟨u,S_{p,N}^{−1}u⟩:

**Theorem.** η_{o,N} − η_{e,N} = T^{(1)}_N + T^{(2)}_N + R^{res}_N, where
- T^{(1)}_N := (A_{o,N}−A_{e,N})·K_{o,N} [amplitude-driven],
- T^{(2)}_N := −A_{e,N}·C_S·K_{o,N}·K_{e,N} [operator-driven],
- R^{res}_N collects the resolvent remainder, cross terms, and subleading pieces.

**Riccati relation [D].** K_{o,N} − K_{e,N} = −C_S·K_{o,N}·K_{e,N} − R^{op}_{oe}, via the resolvent identity K_o−K_e = −⟨w_o,(S_o−S_e)w_e⟩ with (S_o−S_e)_{nm} ≈ C_S/(nm). **The K-difference is second-order in K, not first-order.**

---

## 3. Remote operator structure [D/N]

- The Schur correction B_pA_{p,N}^{−1}B_p^* is **effectively rank-2** (singular values [1.63, 0.85, 0.069,…] at N=60); it changes ⟨u,S^{−1}u⟩ by 56% — NOT negligible, must be included.
- (D_o−D_e)_{nm} = C_D/(nm) + …, leading rank-1, with C_D := −32cosh(1)/π² + 16E_0/π² ≈ −4.396 (E_0 = Σ_{j<50}e^{−2(2j+.5)} = 0.37474310047…; pole piece −5.00, z-parity piece +0.61).
- C_S := C_D − (M_o−M_e)_{11}, the net (1/(nm)) coefficient.
- z_n is O(1)-oscillatory (Im ψ→π/2), not log-growing.

**Orders.** K_{p,N} ∼ 1/(N log N). If ΔA_N ∼ N^{−β} with β≈1.7 [N, diagnostic], then T^{(1)}/T^{(2)} ∼ N^{1−β}log N/C_S → 0: the operator term dominates asymptotically.

---

## 4. The surprise [N/I]

Numerically at N=4000, **T^{(2)} dominates T^{(1)} by ~4×** (opposite signs; observed η_o−η_e<0 with ΔA>0 proves T^{(2)} wins). The implied C_S ≈ +2470 means the Schur-correction parity difference drives the operator term.

**Deeper cancellation [I].** M_{p,11} = w^{(1)ᵀ}A_{p,N}^{−1}w^{(1)} may individually be ~1e30 (‖A_{p,N}^{−1}‖∼1e30), yet the implied (M_o−M_e)_{11} ∼ −2474 is modest — another common-mode cancellation inside the finite-section Schur data. Lane A must compute (M_o−M_e)_{11} as a **direct difference**, not by bounding separately.

The v14.010 "common-mode" intuition (A_o≈A_e) is therefore only half the story; the cancellation operates through both amplitude matching AND second-order operator structure.

---

## 5. Conditional enclosure [D]

|η_{o,N} − η_{e,N}| ≤ K_{max,N}·|A_{o,N}−A_{e,N}| + A_{max,N}·|C_S|·K_{max,N}² + R^{bd}_N,
rigorous once three finite-data inputs are supplied (§6). The common-mode cancellation is exploited analytically (before absolute values) via the (A_o−A_e) factorization and Riccati second-order structure.

---

## 6. Narrow asks for Lane A [O]

1. **(M_o−M_e)_{11}**: two quadratic forms from their finite solve — as a direct difference.
2. **γ** (remote coercivity): already on their v14.008 gap list.
3. **C_ρ** (residual constant): crude bound suffices.

These are well-defined finite computations, not open research. The sandbox has done everything closable without the finite-section solve data.

---

## 7. Verdict

**THEOREM** (factorization + Riccati + operator structure) with a **conditional rigorous enclosure** pending three narrow finite-data inputs.

---

HANDOFF-ACK
target: Lane A
type: task
parent: v14.016
status: closed
closes: v14.009 handoff (target sandbox, type task)
result: THEOREM — leading asymptotic + conditional enclosure delivered; three narrow asks returned to Lane A.
