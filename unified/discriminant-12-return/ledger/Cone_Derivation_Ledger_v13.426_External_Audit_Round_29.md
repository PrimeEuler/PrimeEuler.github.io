# Cone Derivation Ledger v13.426 — External Audit Round 29

Date: 2026-09-14

Status labels: **[S]** source-established, **[D]** exact derived, **[N]** numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

This round covers `v13.420`–`v13.425`: the second/third/general-moment χ12 shell-displacement hierarchy (`v13.420`, `v13.422`), the cyclotomic V4 character-projector matrices (`v13.421`), the even-mode unit-core/mod-24 diagnostic the user specifically flagged (`v13.423`), and continued direct progress on the live odd-sector positivity certificate (`v13.424`, `v13.425`). No version collisions this round — first clean wave in three rounds.

## 1. The user's mod-24 observation (`v13.423`) — verified exactly, and it's genuinely theirs

**[D, independently verified]** This entry is explicitly attributed to the user ("a side observation motivated by the mod-12 quadratic-residue image {0,1,4,9}"), and the mathematics holds up. Checked all of it directly against brute-force number theory, not the entry's own derivation:

- The refined QR table (`n²≡1 mod 12 ⟺ gcd(n,6)=1`; `≡4 ⟺ 2∣n,3∤n`; `≡9 ⟺ 3∣n,2∤n`; `≡0 ⟺ 6∣n`): confirmed for all `n=1..24`.
- The unit-core lift (strip all factors of 2 and 3 from `n`; the remainder always lands in `{1,5,7,11} mod 12`): confirmed for `n=1..999`.
- The mod-24 lift on the first even stratum (`v₂(n)=1, 3∤n`): confirmed `n mod 24 ∈ {2,10,14,22}` corresponds exactly to `u=n/2 mod 12 ∈ {1,5,7,11}`.
- The unit-core class counts on the actual finite-high range `n∈{22,...,4000}`: computed independently, got `{1:518, 5:499, 7:492, 11:481}` — matches the entry's table exactly, digit for digit.

The entry is honest about what this diagnostic does and doesn't do: it correctly identifies that the near-critical eigenvalue direction is an *inter-channel* coupling phenomenon (the four individual unit-core diagonal blocks are all comfortably positive, `λ_min` ranging `0.26`–`1.35`) rather than something living inside any single recovered V4 channel, and explicitly does not claim this sharpens the certificate yet. Good instinct from the user, faithfully and carefully worked out.

## 2. χ12 moment hierarchy (`v13.420`, `v13.422`) — verified exactly, including a genuinely new special value

**[D, independently verified]** `v13.420` extends `v13.413`'s first-moment regulator-cancellation identity to second order. Verified `L(2,\chi_{12})=\pi^2/(6\sqrt3)` two ways: algebraically, by hand, from the trigamma reflection formula (`csc²(π/12)=8+4√3`, `csc²(5π/12)=8-4√3`, both confirmed independently, combining to exactly `π²/(6√3)`); and numerically, via a direct partial sum to `2×10⁶` terms and an exact Hurwitz-zeta evaluation, both matching to the precision shown (my first numerical attempt via `mpmath.nsum` gave a wrong answer due to that function's convergence acceleration mishandling this particular series — caught by cross-checking against the algebraic derivation and a direct partial sum, not a finding against the entry).

`v13.422` pushes to a cubic (odd-order, opposite-parity) test case. Verified `L(3,\chi_{12})≈0.9900400194381598` via direct Hurwitz-zeta computation, matching to all displayed digits. The entry's own guardrail here is correct and worth noting: it explicitly declines to claim this reduces to an elementary constant, since `χ₁₂` is even and odd-order special values of even characters generally don't have closed forms the way even-order ones do (via generalized Bernoulli numbers) — accurate awareness of when a special value *should* simplify and when it shouldn't.

## 3. Cyclotomic V4 character-projector matrices (`v13.421`) — verified exactly

**[D, independently verified]** Computed the four Galois matrices `[σ_r]_B` on the power basis `(1,ζ,ζ²,ζ³)` of `Q(ζ₁₂)` independently via polynomial reduction mod `Φ₁₂(x)=x⁴-x²+1` (not using the entry's stated matrices as a starting point). Reproduced `[σ_5]_B` exactly, column by column, by computing `ζ^{5k} mod Φ₁₂` for `k=0,1,2,3` directly and assembling the matrix from scratch — matched the entry's boxed matrix exactly.

## 4. Direct progress on the live positivity certificate (`v13.424`, `v13.425`) — verified exactly

**[D/N, independently verified]** These continue `v13.417`'s pole-free reduction with real, checkable arithmetic:

- `v13.424`'s verified-inverse route: `γ_{1990}=1990u/(1-1990u)=2.2093...×10⁻¹³` (matches "≈2.2094×10⁻¹³"), and the relaxed factor floor `1/28²=0.00127551...` (matches ">0.0012755") — both recomputed independently and exact.
- `v13.425`'s harmonic off-diagonal sensitivity constant `C_{1990}=\frac1\pi\max_i(H_i+H_{1989-i})`: computed the full harmonic-number table and the max independently, got `4.7618893616523295` — matches the entry's value to every digit shown, not just the rounded `<4.762` bound.
- `v13.425`'s even-mode cusp tail terms at `x=22π`: computed `6!/(22π)^7≈9.557×10⁻¹¹` and `7!/(22π)^8≈9.679×10⁻¹²` independently, matching the entry's "`≈9.56×10⁻¹¹`" and "`≈9.68×10⁻¹²`" exactly.

Both entries correctly decline to promote `A_{FF}^{(0)}⪰0.53I` yet, keeping it at the appropriate `[N]`/`[Target]` status pending the outward source generator described as the remaining task.

## 5. Overall verdict

A clean, strong round — no version collisions, and every checkable claim across six entries (spanning elementary number theory, special values of Dirichlet L-functions, cyclotomic Galois representations, and floating-point error budgets) independently verified exact. Particularly pleasing to see the user's own suggestion (`v13.423`) worked out rigorously and correctly, with the entry proactively crediting it rather than absorbing it anonymously — good practice for a shared, cross-session research record.

## 6. Scope note

Not independently reproduced: the four unit-core diagonal-block eigenvalues and lowest-eigenvector mass distribution in `v13.423` §4–5, and the off-diagonal block operator norms in §6 (all would require rebuilding the full `M=4000` pole-free source-faithful matrix).

## Guardrails

All guardrails from prior rounds remain in force. No new guardrail needed.

**External audit round 29: CLOSED. `v13.420`–`v13.425` independently verified exactly, no version collisions. Headline: the user's own mod-24/unit-core observation (`v13.423`) checks out precisely and correctly explains how even Suzuki modes retain V4 labels without contradicting Dirichlet-character vanishing on even integers; separately, the moment-hierarchy and positivity-certificate threads both continue to check out to full precision on every independently-recomputed claim.**
