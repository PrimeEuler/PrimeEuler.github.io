# Cone Derivation Ledger v15.118 — Sandbox: source certificate discharging v15.111 + v15.117 (original v14.996 EL execution; B = 0 and α certified; on-shell ⟨H₂⟩ confirmed)

**Date:** 2026-10-29. **Lane:** sandbox (Little Euler). **Parents:** v14.996 (payload `payloads/am3scalar_svt_reconciliation_v14_996/`), v15.107, v15.109, v15.110, v15.111, v15.117; Audit R402 (v15.112). **Status:** [D] source execution and residuals; [D] auxiliary solutions; [D]+[N] Fourier identity; [D] on-shell ⟨H₂⟩ quadratic form, independently assembled and coefficient-identical to v15.117's conditional expression. Discharges the v15.111 handoff and the v15.117 validation handoff. Order-two solvability and nonlinear stability remain OPEN. Production fence untouched.

**Pre-write collision check:** live HEAD v15.117 (f5dcfba7); v15.118 next free. Additive only.

## 1. What was executed

The source-corrected v14.996 pathway was executed from the deposited repo payload bytes, not from any local copy: `scalar_final2.py` sha256 `8e2a8e54694470226ec9987b255ca35702040f97aa0275ad6e25d65cbd32fe56`, `scalar_adm2.py` sha256 `7df79aba16ef15d0a38adf0ef8a0bcdd69be3b5dc670081338e1295ff724e57c` (both in `payloads/am3scalar_svt_reconciliation_v14_996/`). Clean exit; `scalar_final.txt` sha256 `29159b886e8ede57335330a7d67f28648729c1bd85113487a8d77ed2e53029fa`; full stdout in the payload of this entry.

## 2. Original EL residuals [D]

On the reconstruction (ψ, ψ̇ from the constraint solve, π̈ eliminated by the reduced oscillator):

- residual EL_B(orig) = **0**, residual EL_Phi(orig) = **0**, residual E1 = **0** — printed by the producer run and re-verified independently inside `h2_substitution.py` using the producer-identical substitution pattern.
- E2 peels exactly (producer assertion, remainder zero) to the π oscillator with c₂ = −√3 t³/(27(k²+1)) (kinetic A = −c₂/2 > 0 ∀k), **P = 3/t, Q = (3k²+4)/t²**, Ω² = Q − P²/4 − Ṗ/2 = (12k²+13)/(4t²). This closes the long-standing `original_EL_reconstruction_residuals=OPEN` item for the scalar sector.

## 3. Auxiliary solutions [D] — v15.117's candidates promoted

From the source's own EL_B/EL_Phi solve chain (EL_B → Φ(B), EL_Phi → B):

- **solB = 0 identically.** On the constrained scalar modes of the build-2 pathway the longitudinal shift is not excited: β = 0 and θ = div β = 0. (Build 3's restored (N^z)²/N² term rotates the auxiliary (Φ, B) block; per the v14.996 reconciliation note the physical spectrum after simultaneous elimination is identical. The handoff specified the build-2 pathway, and this certificate is a build-2 statement.)
- **PhiS = α = ((3k²+4)π + t π̇) / (3k²(k²+1))** — exactly v15.117's candidate α. Both `candidate_B_zero` and `candidate_alpha` are hereby promoted from CONDITIONAL to source-certified.
- ψ = (t π̇ − k² π)/(3k²(k²+1)) (the R390 reconstruction, re-derived); ψ̇ with π̈ eliminated on-shell: ψ̇ = (−(k²+2)π̇ − ((3k²+4)/t)π)/(3k²(k²+1)); the π̇ coefficient tends to −2/(3k²) as k→0 — the 1/k² pole of v15.110, consistent.

## 4. Fourier Hessian identity [D]+[N]

v15.111's ⟨θ² − S_ij S^ij⟩ = 0 for β^i = ∂^i b on flat periodic T³ is verified: symbolically per mode (θ̂ = −|K|²b̂, Ŝ_ij = −K_iK_j b̂, so Σ_ij|Ŝ_ij|² = |K|⁴|b̂|² = |θ̂|²) and by an independent discrete Parseval check on a random band-limited field (means agree, difference 0 at machine precision). On the constrained modes of §3 the identity is in any case moot: θ = 0 on-shell.

## 5. On-shell ⟨H₂⟩ [D]

Substituting §§3–4 into v15.111's simplified averaged source (formula itself verified by R402), using the scalar_adm2 single-mode dictionary (cos/sin amplitudes, ⟨cos²⟩ = ⟨sin²⟩ = 1/2), the full averaged quadratic source on constrained scalar modes is the exact quadratic form ⟨H₂⟩ = A π² + B ππ̇ + C π̇² with

- A = −(3k⁶ + 7k⁴ + 15k² + 16) / (3k² t² (k²+1)²) — strictly negative for all k > 0;
- B = −2(2k⁴ + 3k² − 4) / (3k⁴ t (k²+1)²);
- C = −(k⁶ + k⁴ + 2k² − 3) / (3k⁴ (k²+1)²).

This is **coefficient-for-coefficient identical** to v15.117's conditional expression −[t²π̇²(k⁶+k⁴+2k²−3) + tππ̇(4k⁴+6k²−8) + π²(3k⁸+7k⁶+15k⁴+16k²)] / [3k⁴t²(1+k²)²] (their π² numerator is k² × the A numerator above over the common denominator). The conditional flag on that expression is therefore lifted: it is now source-certified. Independent term-by-term numeric reassembly agrees with the closed form to machine precision at three sample points (payload `h2_verify.py`).

- **Not identically zero.** IR behaviour: A ~ −16/(3k²t²), B ~ +8/(3k⁴t), C ~ +1/k⁴ as k→0 (the 1/k⁴ terms inherited from ψ̇'s 1/k² pole); C changes sign at k² ≈ 0.8437.
- **Scope.** This certifies the source side only. A nonzero ⟨H₂⟩ source may still be balanced by the homogeneous second-order response H₁[U₂]; order-two solvability, the full zero-output Fourier convolution, and nonlinear future stability remain OPEN, and nothing here is a physical-instability statement about admissible function spaces (v15.117's caution stands).

## 6. Disposition

- v15.111 handoff (Fourier identity, EL_B/EL_Phi extraction, constrained ⟨H₂⟩ evaluation, zero-mode source certificate): **DISCHARGED**.
- v15.117 handoff (execute scalar_final2.py, report original residuals, verify/falsify B = 0 and candidate α, check the H₂ expression and low-k scaling): **DISCHARGED** — all confirmed, no discrepancies.
- v15.115 (Lane A source-native energy Gram handoff): acknowledged as the standing K_full bridge build; untouched by this entry.

**Payload:** `payloads/scalar_h2_source_certificate_v15_118/` — `fourier_hessian_check.py` (c14e9f9c…), `fourier_output.txt` (ff093c61…), `h2_substitution.py` (ff89aaa5…), `h2_substitution_stdout.txt` (74e18bd0…), `h2_verify.py` (a3b21b9b…), `h2_certificate.txt` (f6a4faf4…), `scalar_final2_stdout.txt` (cd93de11…), `scalar_final.txt` (29159b88…). Full hashes in the payload manifest as deposited.

**Production fence:** unchanged — no residual consumer, far rerun, stationarity, or capacity claim; C_S_32000, 3e-5, 0.002 untouched; no charges repeated. Suzuki physical-quarter weld PARKED.
