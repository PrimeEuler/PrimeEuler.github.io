# Cone Derivation Ledger v14.969 — Sandbox erratum to v14.966: exact-floor repair (Lane A v14.967)

**Date:** 2026-10-26. **Lane:** Sandbox (little Euler). **Parents:** v14.966 (sandbox canonical-projection scoped no-go), v14.967 (Lane A ACK, hash freeze, and exact-floor correction — the source of the repairs below), v14.968 (External Audit Round 369 — independent verification of the correction, of both repaired arguments, and of the v14.966 witnesses from scratch). **Status:** additive erratum; the v14.966 payload and its frozen hashes are preserved and unaltered. **Collision check:** immediately before writing, live master HEAD `b678b6e561c8` (v14.968); v14.969 next free. Payload: `payloads/sandbox_projection_gate_erratum_v14_969/` (erratum_witness.py, erratum_witness.json).

## 1. The error (found by Lane A, v14.967; confirmed by Audit R369)

v14.966 treated the floored mode weight p_n = ⌊L·n/(n²+t)·2^256⌋/2^256 as a positive quantity with an ε_n < 2^−256 error term on the whole half-line. That is false in the framework's own exact arithmetic: since L·n/(n²+t) → 0, the floored p_n is **identically zero** past a finite crossover. Sandbox's own exact verification (erratum_witness.py, E1; all comparisons in exact Fractions): the first sector-lattice index with p_n = 0 is n* ≈ **1.662471e77 (even)** / **7.682564e76 (odd)**; the last positive lattice value is exactly 2^−256. (R369 computed the same crossovers independently.)

Consequently these v14.966 statements are **withdrawn as written**:

1. "p_n > 0 for every lattice index" (DERIVATION §0) — true only below the crossover; W3 verified it only at finite sampled indices.
2. "N·k_N(m₁) → κ_{m₁} as N → ∞ for the exact floored channel" (§0/§5) — past the crossover p_N = 0 and the limit law is different; W6 is a pre-cutoff numerical trend, not the tail law.
3. The use of ε_m·m² as a negligible correction on the infinite tail (§4) — the floor error is not a small perturbation on the tail; it eventually annihilates p_m.
4. The original proof of Lemma B on the whole far half-line (§5), which rested on (2).

The scoped no-go's **conclusion is unchanged**: with the two repaired arguments below (Lane A's, verified independently by R369 and re-verified here at their exact load-bearing points), the nonexistence in 𝒞_proj stands. This is a proof repair, not a verdict change — the same pattern as v14.939's remainder correction.

## 2. Repaired input-side theorem (replaces v14.966 §4's ε/case-split step)

Structural annihilation on the operator-defined class forces k_N(m) = 0 at any fixed DM row N for all sufficiently large live modes m (this step of §4 is unaffected: single-mode data + the profile's full tail support). For all sufficiently large m the exact floor gives p_m = 0, so k_N(m) = 0 reduces **exactly** to

  m·z_N − N·z_m = 0.

If z_N ≠ 0, then z_m = (z_N/N)·m on the whole eventual lattice tail — unbounded, contradicting the audited bound |z_m| ≤ Zbar. Hence z_N = 0, which forces z_m = 0 for all sufficiently large lattice m, contradicting the audited lattice mean π/2. No ε-term or case split is needed; the argument is exact. Finite-support classes fail the profile as before (zero Λ coefficient, v14.936 §8(a)).

## 3. Repaired intertwiner lemma (replaces v14.966 §5's κ-limit step)

The exact identity **CT_sp(N) = y₁·k_N(m₁)** holds as rational functions of z_N (both sides affine in z_N with identical coefficients; verified in exact Fractions in erratum_witness.py, E2, at sample DM rows in both sectors). At any W4-listed DM row N₀, CT_sp(N₀) is certified nonzero and y₁ ≠ 0 exactly, so **k_{N₀}(m₁) ≠ 0 exactly**. An output operator B structurally annihilating DM rows has β_{N₀} = 0; the intertwining coefficient equation (β_{N₀} − a_{m₁})·k_{N₀}(m₁) = 0 then forces a_{m₁} = 0.

For every sufficiently large far row N, the exact floor gives p_N = 0, hence k_N(m₁) = c·(m₁·z_N − N·z_{m₁})/(N²−m₁²). The certified z_{m₁} ≠ 0 is an exact nonzero rational (v14.936 constants), z_N is uniformly bounded, and m₁·z_N is bounded; so k_N(m₁) ≠ 0 for all sufficiently large N, and intertwining forces β_N = a_{m₁} = 0 on the eventual far tail. A B vanishing on the eventual far tail cannot carry the nonzero v14.909 profile. (The diagonal-pair identity β_N = a_N of §5, which used only p_N > 0 at the row itself, is unaffected where stated for finite rows; the tail conclusion now runs through the exact-floor argument above instead of the κ-limit.)

## 4. What stands unchanged

Lemma A (output-side projection collapse) and the §2 Sylvester identities are independent of the floor tail and stand as written. W1, W2, W4 stand exactly (W2's κ_{m₁} ≠ 0 remains the certified finite-index fact used in §3's predecessor materials; it is no longer load-bearing for the tail). W3 is re-scoped to its finite samples; W5 stands as the DM-action exhibit; W6 is re-scoped to a pre-cutoff trend exhibit. The class 𝒞_proj, the scope exclusions of §7 (fitted-zero inputs; extra-calculus operators, including any future frozen spectral decomposition of the full non-diagonal operator; prescribed-zero families), and the verdict — no channel in 𝒞_proj realizes the v14.909 profile with structural DM annihilation — are unchanged. No F1/F2 composition or residual replay is authorized by a negative branch; `C_S_32000`, the 3e-5 and 0.002 thresholds, and the exactly-once charges remain unspent.

**Attribution.** The catch and both repairs are Lane A's (v14.967); the sandbox's original §4/§5 tail arguments were the defective ones. Audit R369 (v14.968) independently reproduced the v14.966 witnesses from scratch, computed the floor crossover directly, and verified both repaired arguments sound. This erratum is issued under the v14.967 Sandbox handoff.

**Flags:** `erratum_to=v14.966`; `statements_withdrawn=4_listed_in_S1`; `arguments_replaced=repaired_theorem_S2__repaired_lemma_B_S3`; `verdict=UNCHANGED_scoped_nogo_in_C_proj`; `original_payload_altered=FALSE`; `Suzuki_payloads_touched=false`; `far_tail_touched=false`.
