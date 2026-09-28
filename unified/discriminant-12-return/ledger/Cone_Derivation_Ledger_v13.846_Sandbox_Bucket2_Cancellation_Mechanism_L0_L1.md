# v13.846 — Sandbox Bucket 2: the cancellation mechanism behind L₀+L₁=0

**Date:** 2026-09-28
**Lane:** Sandbox (our Lane B — Jeremy's exploratory track under LIttle Euler; disambiguated from the ledger's dormant norm-quotient Lane B)
**Status:** [I]/[O] — discovery, not certified
**Entry kind:** sandbox discovery (analytic mechanism, exact at the discrete level; asymptotic step numerically established, analytically open)
**Supersedes nothing. Refines:** v13.844 (R2 — the cancellation identity as analytic target), v13.842 (Horn B), v13.838 (the (8.5) gap), v13.743 (edge-criteria archaeology)

**Headline:** the mechanism behind L₀+L₁=0 is found and proven exactly at the discrete level: the Tikhonov-regularized (8.5) solve selects the affine coefficients by ker(Kᵀ)-minimization, and the cancellation is equivalent to an asymptotic orthogonality that the numerics confirm monotonically. The cancellation is a property of the **minimum-norm selection**, not of Suzuki's equation alone.

---

## 1. The selection principle — proven exactly

Eliminating v from the regularized problem
min_{v,A,B} ‖Kv + X[A;B] + f‖² + α·vᵀMv (f_j = e^{x_j})
gives min_{A,B} (Xa+f)ᵀW_α(Xa+f) with W_α = I − K(KᵀK+αM)⁻¹Kᵀ.
As α→0, W_α → I − UUᵀ = P_{ker(Kᵀ)} exactly (SVD/Woodbury argument). Hence:

> **(A*,B*) = argmin_{A,B} ‖P_{ker(Kᵀ)}(eˣ + Ax + B)‖²**

The solve picks the affine that makes the right-hand side **as resolvable as possible** — it minimizes the part of the source lying in the unresolvable space ker(Kᵀ).

**Verification:** the reduced argmin matches the full Tikhonov (A,B) to 10⁻⁶ at A = 2, 3, 4, 5. The α = 10⁻¹⁰ used sits deep in the asymptotic regime (W_α = P_{ker} + weights ≤ 10⁻⁴ on Ran(K)).

**What the Tikhonov term does NOT do:** it does not select by minimizing ‖K†(Xa+f)‖. The huge small-σ components of eˣ carry Tikhonov weights d_i = αh/(σ_i²+αh) ≤ 10⁻⁴ and do not move (A,B). The selection lives entirely in the kernel projection.

**The house creed, honored:** the cone does not force dynamics; it selects them. Here is the selection principle, stated exactly: ker(Kᵀ)-minimization.

## 2. How the selection forces the cancellation

Write the 2×2 ker system M_{ker}a + b_{ker} = 0 with M_{ker} = XᵀP_{ker}X, b_{ker} = XᵀP_{ker}f. By parity (K symmetric/convolution), M_{ker} is **diagonal**: M_{ker} = diag(‖P_{ker}x‖², ‖P_{ker}1‖²). Let w = A·P_{ker}x/‖P_{ker}x‖² + P_{ker}1/‖P_{ker}1‖² ∈ ker(Kᵀ) — the minimal-norm representer of "evaluation at x=A" on span{P_{ker}x, P_{ker}1}. Then exactly:

> **ℓ*(A) = −⟨w_A, P_{ker}eˣ⟩**, where ℓ(A) = A·A_coef + B_coef

The cancellation ℓ(A) = o(e^A) — i.e. L₀+L₁=0 — is therefore **equivalent** to w_A becoming orthogonal to P_{ker}eˣ as A→∞. Numerically:

| A | corr(w, P_{ker}f) | ℓ*(A)/e^A |
|---|---|---|
| 2 | +0.094 | −0.171 |
| 3 | +0.051 | −0.145 |
| 4 | +0.0097 | −0.036 |
| 5 | +0.00032 | −0.0015 |

The correlation → 0 **monotonically** — a genuine A→∞ phenomenon, not a fixed-A coincidence.

## 3. What this decides about the other angles (v13.844's open list)

- **Suzuki's A±, B±:** his (8.5) definitions give the affine constants as explicit integrals but contain **no identity** linking B₊ to −aA₊. The identity B₊≈−aA₊ is a property of the regularized *selection*, unprovable from (8.5) alone — the 2D near-nullspace characterized in v13.838 stands.
- **Parity:** x→−x symmetry gives A₋=−A₊, B₋=B₊ and mirrors the same selection to the left edge, but supplies **no within-(+)-channel constraint**. Parity is consistent, not the driver.
- **The common magnitude |L₀|=|L₁|≈0.48:** not a second fact. Since ℓ(A)/e^A = A(L₀+L₁) when limits exist, the equality-with-opposite-signs **is** the cancellation. The number 0.48 itself (lim A*/e^A) is set by D12-screw ker-geometry — unexplained by this mechanism.
- **β_A→0 (the 1/p single pole):** consequence of the selection, not an imposed p=0 regularity condition. No independent zero-frequency matching condition exists in Suzuki forcing β=0; the selection drives β_A→0, leaving the double pole −0.48/p² (v13.844 R2–R3).
- **Self-correction on the record:** an intermediate Euclidean-representer check in the anatomy scripts was inconsistent (mass-norm vs Euclidean) and is **superseded** by the ker-projection result above. The endpoint-spike observation on the preimages stands descriptively.

## 4. What is NOT claimed — the exact wall

1. **The asymptotic orthogonality is numerically established, not analytically proven.** The needed lemma: for the D12-screw convolution K_A, the evaluation-representer w_A ∈ ker(K_Aᵀ) satisfies ⟨w_A, P_{ker}eˣ⟩ = o(e^A‖w_A‖‖P_{ker}eˣ‖). This needs hard analysis of ker(K_Aᵀ) — the 359-dimensional "unresolvable" space — and its pairing with eˣ, likely via **Wiener–Hopf / truncated-convolution theory**, since P_{ker} encodes the finite-interval truncation. Not obtainable from (8.5), compactness, or parity alone.
2. **The selection gap stands** (v13.844 judgment call #1): this mechanism is proven for the *discretized Tikhonov* problem. Identifying it with Suzuki's true v₊ still requires closing Tikhonov-vs-true-v±.
3. **The value 0.48** is D12 ker-geometry — unexplained.
4. **No positivity, RH, or Hilbert–Pólya claim.** The prime ramp is untouched.

## 5. Judgment calls (updated from v13.844)

- **(a) Selection identity:** Tikhonov minimum-norm vs Suzuki's true v± — open, now the single load-bearing question for the whole cancellation story.
- **(b) The 0.48:** unexplained; needs the analytic lemma plus specific kernel analysis.
- **(c) λ_a sign, (d) D12-twist dependence:** untouched by this entry.
- **(e) Downstream absorption:** the −0.48/p² remnant still awaits the paired-transfer/Weyl test.

## 6. Provenance

- Run: `~/workspace/d12/lane_b/sandbox/runs/20260928-200000-bucket2-cancellation-mechanism/` (report.md, STATUS.md, scripts anatomy1–8.py, anatomy1.json)
- Scripts posted to `research-notes/` (11 files: 8 anatomy scripts with portable imports, the D12-screw kernel module, the (8.5) regularized-LS module, README) for use by other threads.
- Numerics: D12Screw kernel (tmax=12.0), regularized (8.5) least squares, α=10⁻¹⁰, A=2…5, N=120 collocation.
