# Cone Derivation Ledger v13.248 — External Audit Round 6

Date: 2026-09-05

Status labels: **[S]** source-established, **[D]** exact derived, **[N-cert]** certified numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction (real defect found this round).

## Scope

Independent external audit of `v13.238`–`v13.247`, the continuation of the Divisor/V4 resonance research branch after round 5 (`v13.237`). This round deepens the algebraic structure discovered in round 5: reachability/return theory for the support-adjunction dynamics, an exact Gaussian/Eisenstein operator-ring classification of the q=5/q=7 resonance planes, and a global theorem ruling out the same rank-two mechanism for every prime q≥11.

As in round 5, every claim below was checked by independent hand derivation and/or independent from-scratch computation (own code, not the ledger's).

## 1. A confirmed error in `v13.238` §8 (the only defect found this round)

**[Audit] CONFIRMED ERROR.** `v13.238` §8 states, in a boxed equation:

> "Direct exact computation, already present in the v13.234/v13.235 resonance data and independently reproduced by external audit v13.237, gives `f_240 = f_24 = -ℓ_7`."

This is factually wrong on two counts, both independently verified:

1. **The claimed equality is false.** Direct computation (two independent code paths: the raw crossing-signal definition of `v13.230`, and the fixed-support pushforward definition of `v13.235`/`v13.238` itself) gives
   `f_24 = (-1,1,1,0,-1,-1,1) = -ℓ_7`, but
   `f_240 = (1,-1,-1,0,1,1,-1) = +ℓ_7`.
   So `f_240 = -f_24`, not `f_240 = f_24`. This also follows immediately from the project's own `v13.234` table (independently re-verified exactly in round 5), which records opposite signs `ε=-1` for `(24,-8)` and `ε=+1` for `(240,-8)`.
2. **The attribution to round 5 is inaccurate.** Round 5's `v13.237` verified the tower `f_{24·8^j,7,-8}` (members `24, 192, 1536, 12288`) — it never touched `M=240`, which is not a member of that `8^j` tower. Round 5 did not "independently reproduce" this specific (incorrect) claim.

**Consequence and containment.** This error does not appear to propagate: `v13.239`'s own derivation of the resonant cofactor set for the stratum `(D,S,q)=(-8,{3,5},7)` uses the correct transport formula `Φ_{-8,{3,5},7}(h) = -Φ_*(3h)` (verified exactly, independently, below), which correctly identifies `h=2` (i.e. `M=240`) as resonant — without relying on the false `f_240=f_24` claim. So the substantive conclusion "`24→120→240` is a valid return path" survives; only the specific intermediate equation in `v13.238` §8 is wrong and should be corrected to `f_240 = -f_24 = +ℓ_7`.

## 2. Reachability, reflection, and prototype collapse (`v13.238`, `v13.239`)

**[D] Verified by hand.** The exponent-orbit theorem (`Reach_exp(S,h) = h·H_S(q)`) is immediate group theory (nonnegative powers of a residue generate its cyclic subgroup); `ord_7(3)=6` and `ord_5(2)=4` were checked directly, confirming both original strata already have maximal reachability subgroups.

**[N-cert] Confirmed exactly, independently computed** (own implementation of the fixed-support pushforward `P_h(t)=Σ_{0≤n<Lh, n≡t(q)} W(n)`, not copied from the ledger): the complete q=5 prototype fiber table (`h=1..4`) and the complete q=7 prototype fiber table (`h=1..6`), both matching `v13.239`'s tables exactly, entry for entry.

**[D] Verified by hand**, the cofactor-reflection theorem `f_{q-h} = -χ_D(-1)·f_h`: re-derived the interval-decomposition argument (CRT zero-mean over one period, then the substitution `n=qL-m` using `W(-m)=χ_D(-1)W(m)`) independently and confirmed it matches the computed tables exactly (`χ_8(-1)=+1` giving `f_{5-h}=-f_h`; `χ_{-8}(-1)=-1` giving `f_{7-h}=+f_h`).

**[N-cert] Confirmed exactly**: the transport identity `Φ_13(h) = -Φ_8(2h)` for the q=5 prototype family, and four spot-checked rows of the 22-row q=7 equivalence table (`D=-11,S={2,3}`; `D=-3,S={19}`; `D=-4,S={17}`; `D=-8,S={3,5}`), each checked against its full 6-state fiber, all matching exactly.

## 3. Prototype-preserving support alphabet (`v13.240`)

**[N-cert] Confirmed exactly via independent exhaustive search** over all 8 labels at q=5 and all 12 labels at q=7: **no** q=5 label preserves the prototype class (matching the claim), and **exactly** the four q=7 labels `{(2,-1),(3,-1),(4,-1),(5,-1)}` preserve it, with induced phases `(u,δ)` matching the ledger's table exactly in every case.

## 4. Determinantal-divisor no-return theorem (`v13.241`, `v13.242`)

**[N-cert] Confirmed exactly, independently computed** (own `Δ₂` = gcd-of-2×2-minors implementation): the complete `(rank, Δ₂)` table for all 12 q=7 labels and all 8 q=5 labels, matching `v13.241`'s tables exactly.

**[N-cert] Confirmed exactly**: the twelve `2×2` restriction matrices `R_{r,σ}` of `v13.242` (solved independently via `R=(BᵀB)⁻¹Bᵀ(AB)` and verified `AB=BR` exactly for every label), and the infinite-orbit growth `Δ₂(T_{2,+1}ⁿΦ*) = 3ⁿ` for `n=0,1,2,3`.

## 5. Eisenstein and Gaussian operator rings (`v13.243`, `v13.244`)

**[N-cert] Confirmed exactly via direct symbolic matrix computation** (not assumed from the prose): `U²-U+I=0`, `U⁶=I`, `N=U-2I` matches `R_{2,+}` exactly, `N²=3U⁻¹` exactly, `UN=NU` exactly, and `UN` matches `R_{3,+}` exactly — the full Eisenstein-ring closure of the q=7 restricted operator semigroup.

**[N-cert] Confirmed exactly** the parallel Gaussian statements for q=5: `J²=-I`, `J⁴=I`, `P²=2J` for `P=I+J`, and all four determinant-2 letters (`I±J`, `-I±J`) matching their claimed identities exactly.

## 6. Universal Legendre support span and the global rank theorem (`v13.245`, `v13.246`)

**[N-cert] Confirmed exactly, independently computed**: `rank[ℓ_q, T_{2,-1}ℓ_q, T_{3,-1}ℓ_q] = 2` for `q=5,7` and `=3` for every prime `11≤q≤47` (own from-scratch implementation, extending past the ledger's own audited range as a spot-check). Also independently confirmed the exact decomposition formulas `T_{2,-1}ℓ_q(k) = χ(n)+χ(2)X(n)` and `T_{3,-1}ℓ_q(k) = (1+χ(3))χ(n)+Y(n)` (`n=k-a`) by direct substitution at `q=13`, with zero mismatches across all `k`.

**[N-cert] Confirmed exactly, independently computed** — the central result of this round: the Gram-determinant formula
`det G_q = 4q²(q-5)`,
verified by building the exact `3×3` Gram matrix from scratch (own inner-product computation on `χ, X, Y` over `𝔽_q`, not using the ledger's closed form) and comparing determinants for **ten** primes `q ∈ {11,13,17,19,23,29,31,37,41,43}` — exact integer match in every case. This is a genuine, now globally proved theorem: `q=5,7` are the only odd primes with a rank-two universal centered-Legendre support span.

## 7. Half-order Hasse vanishing (`v13.247`)

**[N-cert] Confirmed exactly, independently computed** (own polynomial construction and Hasse-order computation via repeated exact division by `(x-1)` over `𝔽_q`, using `sympy`'s `GF` domain): `ord_{x=1} F̄_{8,χ_8} = 2` (mod 5) and `ord_{x=1} F̄_{24,χ_{-8},S={3}} = 3` (mod 7), matching the claimed `(q-1)/2` exactly for both known resonances.

**[N-cert] Confirmed exactly on an independently chosen test case** (not worked out in the ledger text): adjoining the new support prime `p=11` to the `M=24` stratum. Predicted (via the multiplicity-transition law `r^{ν-1}=σ`) that the order should **not** rise; direct computation of `F_{264}` confirmed `ord=3` (unchanged), and the predicted leading-coefficient multiplier `(r-σr^ν) mod 7 = 3` correctly transformed the leading Hasse coefficient from `-1` to `-3≡4 (mod 7)`, matching the direct computation exactly.

## 8. Overall verdict for this round

**One confirmed, but contained, error was found**: the boxed claim `f_240=f_24=-ℓ_7` in `v13.238` §8 is wrong (correct: `f_240=-f_24=+ℓ_7`), and its attribution to round-5 verification is inaccurate. This should be corrected in the ledger — either as a note in a future entry or a direct fix to `v13.238` — since it currently misstates a specific numerical relationship, even though the paragraph's substantive conclusion (that `M=240` is a valid resonant return point reached from `M=120` by one exponent step) is independently confirmed correct via the (correct) `v13.239` transport formula.

Every other claim checked this round — spanning reachability theory, cofactor reflection, the four-label preserving alphabet, the determinantal-divisor no-return theorem, the full Eisenstein/Gaussian operator-ring identification, the global rank-three witness theorem (`det G_q=4q²(q-5)`), and the half-order Hasse-vanishing necessary condition — was independently reproduced exactly, with no further errors found. The Gram-determinant theorem in particular is a genuine, elegant, now-proved piece of new number theory, and this audit's independent from-scratch verification across ten primes gives strong confidence in its correctness beyond the algebraic derivation itself.

## 9. Scope note

Given the volume, the following were read and spot-checked but not exhaustively re-derived: the full 22-row q=7 prototype-equivalence table in `v13.239` (4 of 22 rows independently verified; the remaining 18 were not individually checked); the general symbolic Fourier-multiplier formula in `v13.236`/`v13.245` §4 (the concrete rank computations it feeds into were verified directly instead); and the higher-order multiplicity-jump formula in `v13.247` §10 (not exercised on a concrete example). None of these is flagged as a defect — they are noted as open follow-up items for a future round, consistent with this project's own practice of distinguishing "proved" from "not yet independently checked."

## 10. Guardrails

All guardrails from prior rounds remain in force. Add one new guardrail from this round's finding:

76. When citing a prior external-audit round as having "independently reproduced" a specific numerical claim, verify that the cited round's checked examples actually include that specific claim (same carrier modulus, same comparison) — a tower-membership check or a different worked example is not equivalent verification, as `v13.238`'s citation of `v13.237` illustrates.

**External audit round 6: CLOSED. One correction recommended for `v13.238` §8 (sign of `f_240` relative to `f_24`); no other corrections required to `master`.**
