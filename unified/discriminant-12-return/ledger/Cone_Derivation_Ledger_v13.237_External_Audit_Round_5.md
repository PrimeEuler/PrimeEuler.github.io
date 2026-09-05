# Cone Derivation Ledger v13.237 — External Audit Round 5

Date: 2026-09-05

Status labels: **[S]** source-established, **[D]** exact derived, **[N-cert]** certified numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

Independent external audit of every ledger entry landed on `master` since the round-4 audit (`v13.221_External_Audit_Round_4`), covering `v13.221` (parallel-session numbering) through `v13.236` — the principal-paper v0.3.5 theorem-hardening/promotion, and the entirely new **Divisor / V4 quadratic-character resonance** research branch (`v13.223`–`v13.236`). This is the largest and most novel batch audited so far: roughly 6,300 new lines, most of it genuinely new mathematics rather than reconciliation of earlier foundations.

Note on numbering: this session's own `v13.221_External_Audit_Round_4.md` (previous round) collided with the parallel session's `v13.221_Principal_v0.3.5_Theorem_Hardening.md`. Both files coexist on `master` under the same version number; this is a documentation-hygiene collision only, consistent with prior rounds, and no content conflict exists between them.

Every claim below was checked by one or both of: (a) independent hand re-derivation, (b) an independent Python/sympy script re-implementing the construction from its stated definition (not copying any formula from the ledger's own numeric tables) and comparing against the ledger's boxed results.

## 1. Principal v0.3.4 → v0.3.5 (`v13.221`, `v13.222`)

**[D] Verified by hand.** The signed 3D boost made explicit in v0.3.5,
`X'=2X+√3 T`, `Y'=Y`, `T'=√3 X+2T`, is exactly the `λ=2+√3` factor action `x'=λx, y'=λ⁻¹y` rewritten in Paper-A coordinates: expanding `X'=(x'-y')/2` and `T'=(x'+y')/2` using `λ+λ⁻¹=4`, `λ-λ⁻¹=2√3` reproduces both boxed identities exactly, and `Y'=Y` follows from `x'y'=xy`.

**[D] Verified by hand.** The other three hardening items — the direct `O_{K₁₂}/𝔓₂≅𝔽₄` quotient proof, the trace/XOR identity promoted into the theorem, and the `n=11` Artin proposition — are the same identities independently re-derived and confirmed in round 4 (`v13.220`/`v13.221` round-4 review); v0.3.5 correctly folds them into the formal theorem/proposition structure as v13.220 recommended. No new mathematical content beyond packaging.

**Verdict: PASS.** This is exactly the "theorem hardening" the round-4 audit anticipated, executed correctly.

## 2. Divisor summatory identities (`v13.223`)

**[N-cert] Confirmed exactly**, for `n=11,20,30`, the exact identities `D(n)=nH_n-F_n` and `A_n=T_n-D(n)=F_n-G_n` (`F_n=Σ{n/k}`, `G_n=nH_n-T_n`), computed independently with exact rational arithmetic (Python `fractions`), including the specific values `D(11)=29`, `T_11=66`, `A_11=37`, `11H_11=83711/2520`.

## 3. V4 Hadamard / character-Fourier structure (`v13.224`, `v13.225`)

**[N-cert] Confirmed exactly**: `H_4²=4I`; the character table rows `χ₋₄=(1,1,-1,-1)`, `χ₋₃=(1,-1,1,-1)`, `χ₁₂=(1,-1,-1,1)` on `(1,5,7,11)` (re-derived independently from the standard mod-4 and mod-3 quadratic characters, not copied); and the full exact `n=11` vector set `S(11)=(11,2,1,1)`, `F(11)=(0,1/5,4/7,0)`, `R(11)=(1,1/5,1/7,1/11)`, their Hadamard transforms `Ŝ(11)=(15,11,9,9)`, `F̂(11)=(27/35,-13/35,13/35,-27/35)`, `R̂(11)=(552/385,372/385,328/385,288/385)`, and the transform identity `F̂=11R̂-Ŝ` componentwise.

**[Audit] Concur** with `v13.225`'s self-correction of `v13.224`'s overclaim (the two imprimitive channels are conductor-modified, not literally the unmodified Dedekind-zeta channels): verified by hand that `L(s,χ₋₄^{(12)})=(1+3⁻ˢ)L(s,χ₋₄^{prim})` and `L(s,χ₋₃^{(12)})=(1+2⁻ˢ)L(s,χ₋₃^{prim})` follow from the standard induced-character Euler-factor formula, using `χ₋₄^{prim}(3)=-1`, `χ₋₃^{prim}(2)=-1`.

**[N-cert] Confirmed exactly** the prime-residue selector table `Δŝ(p)=1+χ(p)` for all four residue classes mod 12 (hand-verified via direct character evaluation, matching all four table rows), and the exact `Ŝ(11)-Ŝ(10)=(2,0,0,2)` shell increment via independent computation.

## 4. Mod-24 lift and sieve (`v13.226`)

**[N-cert] Confirmed exactly**: `U(24)≅U(12)×C₂`, the stated fiber decomposition; the `k=1` block `{25,29,31,35,37,41,43,47}` with exactly 6 primes; the wheel-density identities `4/5·6/7=24/35` and `(1/3)(24/35)=8/35`; and the crossing congruences `k≡r (mod 5)` and `k≡2r (mod 7)`.

## 5. Character self-duality and H₄/H₈ factorization (`v13.227`, `v13.228`)

**[N-cert] Confirmed exactly via independent sympy DFT computation**: `DFT₁₂(χ₁₂)(m)=√12·χ₁₂(m)` for all `m=0,…,11` (the Gauss-sum self-duality claim); the block-diagonalization `(1/4)H₄K₁₂H₄=diag(0,2i,0,2√3)` (verified numerically to machine precision); the sheet character `η=χ₋₂₄` and product identities `χ₋₄η=χ₂₄`, `χ₋₃η=χ₈`, `χ₁₂η=χ₋₈` (all confirmed against the real Kronecker symbol, independently computed via sympy — not assumed); and the 24-point DFT sheet-parity claim (`DFT₂₄` vanishes on all odd frequencies, equals `4√3·χ₁₂(k)` on `m=2k`, confirmed exactly at all 24 points).

## 6. Legendre/Kronecker H₈ selector and crossing spectra (`v13.229`, `v13.230`)

**[D] Verified by hand.** `χ₁₂(p)=(3/p)` for `p>3` is the standard quadratic-reciprocity identification; the splitting interpretation (`+1`=split, `-1`=inert in `ℚ(√3)`) is standard.

**[N-cert] Confirmed exactly, independently computed**: the full 8-row prime-selector increment table of `v13.229` §6 (reproduced exactly using representative primes `97,101,31,59,37,41,43,47` for each residue class mod 24); and the complete `v13.230` crossing-mask tables for `q=5` (5 rows) and `q=7` (7 rows), including every individual Walsh-coefficient vector, the exact `χ₁₂` and `χ₋₈` columns, the full-cycle cancellation `Σₖ Ĉ_q(k)=(8,0,…,0)` for both `q=5,7`, and the `5∪7` 35-block supercycle counts (removed-slot distribution `{2:20,3:12,4:3}`, total removed `88`, survivors `192`, Walsh sum `(88,0,…,0)`) — all reproduced from scratch and matching exactly.

## 7. Block-index DFT, q=7 resonance, and rigidity (`v13.231`, `v13.232`)

**[N-cert] Confirmed exactly via independent exhaustive search.** Re-implemented the crossing signal `f_{q,ψ}` from its definition and searched all `q∈{5,7,11,13,17,19,23}`, all 7 nonprincipal `H₈` characters, all shifts, both signs: the **unique** shifted-signed-Legendre match is exactly `(q,ψ,a,ε)=(7,χ₋₈,3,-1)`, i.e. `Ĉ₇(k;χ₋₈)=-((k-3)/7)`, matching `v13.232`'s claimed uniqueness exactly. Independently re-ran the flat-nonzero-spectrum search over the same range and found the same unique pair `(7,χ₋₈)` with magnitude² `7`, matching the Gauss-sum prediction `|τ₇|²=7`.

**[D] Verified by hand.** The large-`q` rigidity argument (autocorrelation `R(t)=-8/(q-1)` must be an integer, forcing `(q-1)|8`, impossible for prime `q>23`) is a correct, standard Parseval/inverse-DFT argument; re-derived independently and confirms no prime `q>23` can produce a flat nonprincipal spectrum on this fixed 8-state carrier.

## 8. Carrier pushforward and expanded resonance family (`v13.233`, `v13.234`)

**[N-cert] Confirmed exactly**, the six specific carrier resonances tabulated in `v13.233`: `(8,5,χ₈)`, `(17,5,χ₁₇)`, `(20,7,χ₋₄)`, `(24,7,χ₋₈)`, `(30,7,χ₋₁₅)`, `(32,5,χ₈)`, each checked against its stated Legendre-sequence formula and matching exactly.

**[D] Verified by hand**, the `v13.234` centered-involution theorem: the crossing-time reflection law `κ(M-r)=-1-κ(r) (mod q)` follows directly from `κ(r)=-rM⁻¹`; the forced center `a=(q-1)/2` follows because the Legendre sequence's unique zero must be a fixed point of `k↦-1-k`; and the parity condition `χ_D(-1)=(-1/q)` follows from comparing the transformed centered Legendre sequence under the same involution. Both are correct, standard finite-Fourier/quadratic-residue arguments.

**[N-cert] Full independent replication.** This is the single most substantial independent check performed this round: re-implemented the entire `3≤M≤300`, `5≤q<80` search from scratch (own fundamental-discriminant test, own pushforward/crossing-signal code, own Legendre-match search over all shifts and signs) with **no code or data copied from the ledger**. Result: **exactly 33 resonances found, exactly matching the ledger's table row-for-row and sign-for-sign** — all 5 `q=5` pairs `(8,8),(17,17),(32,8),(128,8),(169,13)` and all 28 `q=7` triples `(M,D,ε)`, including every individual epsilon sign. Also confirms the claim that only `q∈{5,7}` occur anywhere in this search window.

## 9. Infinite resonance towers and support-prime transitions (`v13.235`, `v13.236`)

**[D] Verified by hand.** The fixed-support periodicity theorem (`P_h` depends only on `h mod q` within a fixed radical-support stratum) follows from a standard CRT + zero-mean argument: since `(q,L)=1`, a `qL`-length interval hits every residue mod `L` exactly once at each fixed residue mod `q`, and the nonprincipal character sums to zero over one full period mod `L`.

**[N-cert] Confirmed exactly, independently computed.** Verified the three claimed infinite towers numerically for several tower members each: `f_{24·8^j,7,-8}` constant `=(-1,1,1,0,-1,-1,1)` for `j=0,1,2,3`; `f_{20·8^j,7,-4}` constant for `j=0,1,2`; `f_{8·16^j,5,8}` constant for `j=0,1,2`; and confirmed `M=32` sits in the same `D=8` support stratum but a different cofactor class (`h≡4 mod 5` vs. `h≡1 mod 5` for the `8·16^j` tower), correctly explaining its opposite sign without contradicting the theorem.

**[N-cert] Confirmed exactly** the new-support-prime transition operator `f_{pM}=T_{p mod q, χ_D(p)}f_M` on both worked examples in `v13.236`: `p=5` applied to `f_24` (giving `(-1,2,-1,0,1,-2,1)`, matching direct computation of `f_120`) and `p=11` applied to `f_24` (giving `(2,-3,0,0,0,3,-2)`, matching direct computation of `f_264`), both independently re-derived from the operator definition and cross-checked against direct crossing-signal computation at the enlarged modulus.

**[D] Concur** with the derivation of the operator itself (`P_{pM}(t)=Σⱼ P_M(t-jM)-χ_D(p)P_M(p⁻¹t)`, reduced via the same zero-mean argument to `p mod q`) — the interval-decomposition and exclusion-by-Möbius-style argument is correct and mirrors the periodicity argument of `v13.235`.

## 10. Overall verdict for this round

**No mathematical error was found in any of `v13.221`–`v13.236`.** This is the most extensively independently-computed round to date: beyond hand re-derivation, this audit re-implemented — from definitions, not from the ledger's own code or tables — the Hadamard/Walsh transforms, the Gauss-sum DFT self-duality, the H₈ prime-selector table, the full q=5/q=7 crossing-mask tables, the q=7 rigidity search, and (most substantially) the entire 33-resonance exhaustive search over `3≤M≤300, 5≤q<80`, and every one of these independent computations matched the ledger's claims exactly, including individual signs and shift values.

This branch is genuinely new mathematics (not principal-paper reconciliation), and its central discoveries — the exact quadratic-subfield decomposition of the mod-12 divisor transform, the isolated `q=7`/`χ₋₈` Gauss resonance and its proof of rigidity for large `q`, the exact 33-member resonance family with proved center/parity selection rules, and the infinite-tower and support-transition theorems that explain the family's internal structure — all check out. The parallel session's own self-corrections in this round (`v13.225`'s conductor fix to `v13.224`, `v13.234`'s correction of the "naive CRT factorization" idea proposed in `v13.233`) are themselves accurate.

## 11. Scope note

Given the size of this batch, three items were read but not independently re-derived beyond the ledger's own presentation: the general Fourier-space form of the support-transition operator in `v13.236` §6 (the `D_r(m)` geometric-sum bookkeeping), the full non-constancy argument in `v13.236` §7 (character-independence of the shifted-signed-Legendre obstruction), and the "no resonance for `q≥11`" observation, which all sides already flag as an unproved finite-window observation rather than a theorem. These are flagged for follow-up in a future round rather than treated as open defects.

## 12. Guardrails

No new guardrails are required. All guardrails from prior rounds remain in force, and every explicit guardrail added in `v13.223`–`v13.236` (character-layer separation, CRT non-factorization warning, support-vs-exponent distinction, "not yet a classification theorem" disclaimers) was checked against its corresponding claim and found to be stated at the correct strength — none overclaims, and none is contradicted by the verified mathematics.

**External audit round 5: CLOSED. No corrections required to `master`.**
