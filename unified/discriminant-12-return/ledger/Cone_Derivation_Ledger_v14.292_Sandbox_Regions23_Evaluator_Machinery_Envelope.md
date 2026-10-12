# Cone Derivation Ledger v14.292 — Sandbox: Regions 2–3 Directed Infinite D·y Evaluator — Machinery Validated, Region-3 Envelope Certified, Full Evaluation In Flight

**Date:** 2026-10-12
**Track:** Sandbox / v14.290 + v14.291 handoff response
**Status:** [D] Regions 2–3 evaluator implemented (bank + subtraction-moment architecture, generalized exact Toeplitz/Hankel channels, certified diagonal, full pole). [V] Machinery validated three ways: Lane A's v14.290 producer smoke reproduced in the sandbox environment; generalized channels byte-identical to Lane A's `channels()` and to brute-force direct sums (both sectors); seed-bank construction aggregates (l1, close-pole moment, max seed error, max z error) rationally identical to Lane A's limit-7 certificate. [N-cert] Region-3 envelope for all n>4R composed and certified from pinned inputs (offdiagonal v14.253 + diagonal + pole): |(Dy)_n| ≤ (A + B·log(n/b))/n with A=41.03346435029798, B=0.9246976885779616 (even-v); A=40.995010915797, B=0.9238311387052199 (odd-v); ℓ² tail beyond the evaluation window ≤ 0.0314715844867336 / 0.031442090487128475. The envelope does NOT close capacity (≫ 0.002); it is a pointwise certified bound, stated as such. Full Region-2 rectangle + Region-3 window evaluation is in flight (checkpointed bank build, §5); a completion entry follows. No whole-action, residual, stationary, or capacity claim.
**Parents:** v14.223, v14.235, v14.250, v14.253, v14.262–264, v14.266, v14.274–278, v14.290, v14.291.
**Collision check:** live ledger max v14.291 (Lane A) at write time; v14.292 is next-free. No collision.

---

## 1. Handoff as received

v14.290 (Lane A) started the directed Region-1 close consumer and handed the sandbox Regions 2–3's actual directed infinite D·y evaluation, retaining the later-start far inputs as a separate contribution. v14.291 completed the Region-1 close rectangle (ℓ² errors 7.78e-35 even / 7.72e-35 odd), restated the handoff, and fixed the scope: Regions 2–3 remain Sandbox-owned; the v14.274/v14.276 later-start far contribution (Region-1 *output* rows, inputs m≥a) must be composed exactly once — this entry does not touch that rectangle. Regions here are v14.264's: Region 2 = output rows b≤n≤4R; Region 3 = output rows n>4R. Sector conventions follow Lane A's producers exactly (even-v: modes ≡1 mod 2, b=512001, a=1024003; odd-v: modes ≡0 mod 2, b=512002, a=1024004; R=256000, 4R=1024000).

## 2. Architecture [D]

For every output row n≥b, with the audited Toeplitz-minus-Hankel kernel,

$$(D y)_n=\tfrac{c}{2}\bigl[z_n V_n-U_n\bigr]+d_n y_n+\sigma\cdot 2\,p_n P_{\mathrm{total}},$$

$$V_n=\sum_{m\ge b,\,m\ne n} y_m\Bigl(\tfrac1{n-m}-\tfrac1{n+m}\Bigr),\qquad U_n=\sum_{m\ge b,\,m\ne n} z_m y_m\Bigl(\tfrac1{n-m}+\tfrac1{n+m}\Bigr),$$

σ=+1 (even-v) / −1 (odd-v), p_m=L·m/(m²+t), P_total=Σ_{m≥b} p_m y_m, d_n the certified raw diagonal (v14.235 evaluator, pole excluded). Inputs split at 2a:

- **Bank [b, 2a):** 768,003 modes per sector, built mode-by-mode with Lane A's exact construction (certified bulk z intervals; Phi from the SHA-pinned v14.223 source far_channels; directed log(m/4) endpoints; 160-bit floors; per-mode errors tracked). Consumed by four exact GMP integer convolutions (generalized `channels_gen`: arbitrary output window; Toeplitz diagonal zeroed, Hankel full, diagonal physics added via d_n — Lane A's convention).
- **Tail m≥2a by subtraction moments:** U_j(2a)=U_j(b)−Σ_bank z_m y_m/m^{2j+2}, V_j(2a)=V_j(b)−Σ_bank y_m/m^{2j+1}, P(2a)=P(b)−Σ_bank p_m y_m, J=42, from the v14.263 b-start master bank (payload SHAs re-verified: even `7ec00186…`, odd `f2487596…`; source SHA `6c2b8d1d…` ✓). Tail action on rows n<2a: −2Σ_j n^{2j}V_j(2a) and −2Σ_j n^{2j+1}U_j(2a) (v14.266 form), geometric ratio (n/2a)²≤0.258 on every evaluated row, remainder bounded exactly with |y_m|≤C_Phi/(m·log(m/4)).
- **Region 2:** all 256,000 rows per sector assembled from bank convolutions + tail moments + certified diagonal + full pole, with Lane-A-style separated error charges (bank seed, tail radii, tail remainder, output-z, c, kernel-floor, diagonal, pole, row floor) and three complete direct-row checks per sector. Expected ℓ² error is dominated by the certified diagonal radius (~1e-11 × |y_n|), ≈1e-15 scale; all other charges ≈1e-25 or below. Both tiers will be reported separately in the completion entry.
- **Region 3:** evaluated window (4R, 4R+2·8192] per sector by the same assembly, joined to the §4 envelope for all larger n.

The evaluator lives in the sandbox workspace (`sandbox_region23_evaluator.py`) and is **not** committed to research-notes/ — v14.276's earlier request for a repo commit of sandbox code remains subject to Jeremy's explicit approval, which has not been given; the ledgering-only standing authorization is unchanged. Lane A's module stack was fetched read-only and used unmodified.

## 3. Validations [V]

1. Lane A's producer `suzuki_infinite_seed_region1_close_action.py` executed in the sandbox environment (limit-7 smoke, even-v): internal direct-sum asserts pass; smoke ℓ² error 1.53e-41.
2. `channels_gen` == Lane A `channels()` == brute-force integer direct sums, both sectors (random signed test vectors, M=7 inputs, 4 outputs): exact integer equality.
3. Seed-bank construction == Lane A's construction: on the 7-mode limit bank, represented l1, close-pole moment P, max seed error ey, max z error ez are **rationally identical** to Lane A's limit-7 certificate (all four string-equal).
4. Payload integrity: v14.263 master moments and v14.276 later-start moments re-downloaded; SHAs match v14.264's audit and the v14.278 verification respectively. The v14.276 a-start bank was re-verified for integrity only and is **not** used in the subtraction, which starts from the b-start master bank — so the Region-1 far composition remains separate and is composed exactly once, by Lane A.

## 4. Region-3 envelope [N-cert]

For all n>4R: |(Dy)_n| ≤ (A + B·log(n/b))/n, composed of (even-v): offdiagonal constant 28.203283565232784 and slope 0.9246976885779616 (v14.253, recomputed from the pinned source), diagonal coefficient 12.830180429019219 (from |d_n|≤log(n/4)+100 and |y_n|≤C_Phi/(n log(n/4)), C_Phi=1.2714593217946972), pole coefficient 3.56e-07 (P_total ≤ 1.2399406586564998e-07). Odd-v: C_Phi=1.2702678157196774, diagonal 12.818157049534927, pole 7.60e-08. ℓ² tail from the window end (n>1040384): ≤0.0314715844867336 even / 0.031442090487128475 odd (first-term + spacing-two integral bound, Lane A's pattern). **Scope honesty:** this envelope is far above the 0.002 capacity scale — it certifies the pointwise decay of Region-3 rows and nothing more. Capacity closure requires the evaluated action's cancellation, not triangle-inequality envelopes.

## 5. Computation in flight

Bank build launched 2026-10-12 ~16:32 EDT on the sandbox host (2 cores): 188 checkpointed chunks of 4,096 modes per sector, measured 15–22 s/chunk single-worker, both sectors concurrent; resumable after interruption with no recomputation. On bank completion an unattended driver runs, per sector: close-bank aggregate validation against Lane A's published v14.291 certificate (l1 0.032026602152362964 even / 0.031996931668963564 odd; close-pole moments 6.496725555193161e-8 / 2.9994616185738974e-8; max seed error <7.08e-44), tail-moment subtraction, Region-3 window evaluation, then the Region-2 output bank (z_n + d_n per row) and the full Region-2 rectangle. The completion entry will report evaluated buffers (SHA-bound), per-charge error budgets, direct-row checks, and the Region-2/3 ℓ² norms.

## 6. Verdict

$$\boxed{
\text{[D] Regions 2--3 evaluator implemented on Lane A's exact kernel,}\\
\text{bank, and constants. [V] channels and seed construction verified}\\
\text{to rational identity against Lane A. [N-cert] Region-3 envelope}\\
\text{composed for all } n>4R \text{ (does not close capacity).}\\
\text{Full rectangle evaluation in flight; completion entry follows.}
}$$

---

HANDOFF-ACK
from: v14.290 (sandbox part) + v14.291 (sandbox part)
target: sandbox
status: partially closed — implementation delivered and validated; Region-3 envelope certified; full Region-2 rectangle and Region-3 window evaluation in flight (checkpointed, §5), completion entry to follow.
result: Regions 2–3 directed infinite D·y evaluator built on the pinned v14.223 source and Lane A's unmodified module stack; generalized channels rationally verified; seed bank under construction over [b,2a) (768,003 modes/sector); Region-3 envelope A≈41.03, B≈0.9247 (even) / A≈41.00, B≈0.9238 (odd), ℓ² tail ≈0.0315 — certified pointwise bound only, not a capacity closure. Later-start far contribution untouched, left for Lane A's single composition.
constraints: Evaluator code remains in the sandbox workspace; no research-notes/ commit (per-item approval outstanding, as flagged in v14.278). No whole-action, residual-acceptance, stationary, or capacity claim.
