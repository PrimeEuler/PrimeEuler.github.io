# Cone Derivation Ledger v13.253 — External Audit Round 7

Date: 2026-09-05

Status labels: **[S]** source-established, **[D]** exact derived, **[N-cert]** certified numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

Independent external audit of `v13.249`–`v13.252`, the continuation of the Divisor/V4 resonance branch after round 6 (`v13.248`). This is a smaller, tightly-focused batch: it (a) reconciles the round-6 finding, and (b) develops a generalized-Bernoulli-number theory of the half-order Hasse obstruction, culminating in an exact classification of which lower Hasse conditions must be "primitive" (unavoidable) versus which can be engineered away by support-prime choice.

As in prior rounds, every claim below was checked by independent hand derivation and/or independent from-scratch computation.

## 1. Round-6 reconciliation (`v13.249` §0)

**[Audit] Confirmed correctly reconciled.** `v13.249` adopts exactly the correction from round 6 (`f_24=-ℓ_7`, `f_240=+ℓ_7=-f_24`) and correctly notes the substantive `24→120→240` return-path conclusion is unaffected. No further issue found here.

## 2. Fixed-support polynomial factorization and Bernoulli connection (`v13.249`)

**[N-cert] Confirmed exactly, independently implemented:**

- The polynomial identity `F_{Lh}(x) = F_L(x)·G_h(x^L)` (own construction of `F_L`, `F_{Lh}` and `G_h` from their definitions, `sympy.expand`, exact match) for `L=8, h=4`.
- Hasse-multiplicity invariance under existing-support exponent growth: `ord_{x=1} F̄_{Lh} = ord_{x=1} F̄_L` for the `(D,S,q)=(-8,{3,5},7)` stratum across all `h=1,…,6` (own polynomial construction and repeated exact division by `(x-1)` over `𝔽_q`, not the ledger's numbers).
- The linear scaling law `D^{[ν]}F̄_{Lh}(1) = h·D^{[ν]}F̄_L(1) (mod q)`: verified exactly for the same six values of `h`.
- The claimed values `C_{D,S,q}=1, 1, 4` for the three worked strata `(8,∅,5)`, `(-8,{3},7)`, `(-8,{3,5},7)` — computed independently via `C ≡ e!·D^{[e]}F̄_L(1) (mod q)` from the ledger's own §4 formula (not simply copied), all three matching exactly, including the correctly re-derived resonant pair `h=±2={2,5}` for the third stratum (consistent with the round-6 correction, since the earlier `v13.238` sign error never entered this independent recomputation).

## 3. Safe-prime and parity-coprimality theorems (`v13.250`, `v13.251`)

**[D] Verified by hand**, the core algebraic step of `v13.251`: `gcd(2(n-1), q-1) = 2·gcd(n-1,e)` is the standard identity `gcd(ka,kb)=k·gcd(a,b)` with `k=2`; and `e-n ≡ -1 (mod g)` for `g=gcd(n-1,e)` follows immediately since `g∣e` and `g∣(n-1)`. This correctly collapses the `v13.249` subgroup criterion to `gcd(n-1,e)=1`.

**[N-cert] Confirmed exactly, independently computed** (own script re-implementing both the original `v13.249` subgroup criterion and the simplified `v13.251` gcd criterion from their separate definitions, not assuming they agree): the two criteria produce **identical** sets `𝒰_q` for all 13 tested primes `q∈{5,7,11,13,17,19,23,29,31,37,41,43,47}`, and both match the ledger's own table exactly, including the closed-form counts `N(q)=φ(e)-1` (e even) / `φ(e)/2-1` (e odd). Also independently confirmed the safe-prime specialization `𝒰_q={3,5,…,e-2}` for the safe primes `q=11,23,47` in that list.

**[D] Verified by hand**, the `v13.250` group-theoretic safe-prime argument: for `q=2e+1` with `e≥5` prime, a support prime killing an odd lower index `n` (so `n-1` even) forces `r^{2(n-1)}=1`; since `gcd(2(n-1), 2e)=2` (as `gcd(n-1,e)=1` when `0<n-1<e`, `e` prime), this forces `r=±1`, hence `r^{n-1}=r^{e-1}=1` (both exponents even), so the same prime necessarily also kills the target index `e`. This is airtight given the stated hypotheses.

## 4. Simultaneous support covering and minimum basis (`v13.252`)

**[D] Verified by hand and by direct example construction**, the three worked cases:

- `q=13, e=6`: primitive-forced `{2}`, coverable `{4}` — confirmed by direct `gcd(n-1,6)` computation for even `n<6`.
- `q=31, e=15`: primitive-forced `{3,5,9}`, coverable `{1,7,11,13}`, with the order-3 class covering exactly `{1,7,13}` and the order-5 class exactly `{1,11}` — confirmed by direct computation of `gcd(n-1,15)` and the divisibility-by-3/-by-5 partition of the coverable set, matching the ledger's claim exactly.
- `q=43, e=21`: primitive-forced `{3,5,9,11,17}` (matching the independently-verified `v13.251` table entry for `q=43`), coverable `{1,7,13,15,19}`, with the order-3 class covering `{1,7,13,19}` and the order-7 class covering `{1,15}` — confirmed exactly.

These three hand-checks, worked from the raw `gcd` definitions rather than from the ledger's stated conclusions, corroborate the general claim that maximal single-prime kill classes are exactly `K_p` for odd primes `p∣e`, and that `N_supp^min(q)=ω(e_odd)`.

**[D] Concur** with the §4 CRT/Dirichlet global-realizability argument (choosing a residue class mod `dq` to fix both the character value and the order-`p` residue simultaneously) — this is a standard and correctly-applied construction.

**[Audit] Concur** with `v13.252` §8's own self-correction of an imprecise sentence in `v13.250` §5 (the "if additionally `B_1≡0`" caveat needed clarifying that `n=1`'s shift is `0`, hence always coverable, not automatically primitively forced) — this is a legitimate, correctly-resolved precision fix, not a defect requiring further comment.

## 5. Overall verdict for this round

**No new mathematical error was found in `v13.249`–`v13.252`.** The round-6 correction was properly incorporated. This batch is more purely algebraic/combinatorial than round 6 (generalized Bernoulli numbers, gcd/divisor-lattice arguments) and every falsifiable numerical claim checked — the three `C_{D,S,q}` values, the thirteen-prime `𝒰_q`/`N(q)` table, and the three worked minimum-support-basis examples — was independently reproduced exactly from first principles.

The branch has now assembled a fairly complete necessary-condition toolkit for ruling out `q≥11` resonance (rank-three universal span, half-order Hasse vanishing, primitive-vs-coverable Bernoulli classification), while correctly and repeatedly flagging that none of it yet closes the global `q≥11 ⟹ no resonance` conjecture. That epistemic discipline continues to hold up under audit.

## 6. Scope note

Not independently re-derived this round: the general local kill-set classification argument in `v13.252` §2 (that every target-safe single-prime kill set has the form `K_g` for odd `g`) was checked only via its consequences on the three worked examples above, not via a full independent re-proof of the classification lemma itself. Flagged as a follow-up item, not a defect.

## 7. Guardrails

All guardrails from prior rounds remain in force. No new guardrail is needed this round.

**External audit round 7: CLOSED. No corrections required to `master`.**
