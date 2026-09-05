# Cone Derivation Ledger v13.259 — External Audit Round 8

Date: 2026-09-05

Status labels: **[S]** source-established, **[D]** exact derived, **[N-cert]** certified numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

Independent external audit of `v13.254`–`v13.258`. This batch has two distinct parts: (1) a deep extension of the q=11 Bernoulli/Hasse obstruction theory (`v13.254`, `v13.255`), culminating in an extremely intricate explicit construction; and (2) a strategic pivot (`v13.256`–`v13.258`) connecting the project's `χ₁₂`/V4 apparatus to genuine, correctly-cited published analytic number theory (Suzuki's weighted-Chebyshev GRH criteria and, in `v13.258`, his Selberg-class screw-function theory). This round included, for the first time, verification of *external citations*, not just internal derivations — two separate Suzuki papers were checked.

## 1. Full pre-top Bernoulli jet theory (`v13.254`)

**[N-cert] Confirmed exactly, independently computed** (own implementation of generalized Bernoulli numbers `B_{n,χ} = fⁿ⁻¹ Σ χ(a)B_n(a/f)` from the textbook definition, not the ledger's stated values): for `D=-19`, `B_1=-1`, `B_3=66`, `B_5=-13450`, `B_7=5303074`, `B_9=-66751985430/19` — all five match exactly — and their mod-11 reductions `0, 3, 7, 3` also match exactly. This is the load-bearing empirical claim of the entry (the "primitive lower gate passes but the target coefficient survives" counterexample), and it checks out.

**[D] Verified by hand**, the two universal jet constants: substituting `e≡-1/2 (mod q)` into `c_{2r}(q)=binom(e+2r,2r)·B_{2r}(1/2)` symbolically (using `B_2(1/2)=-1/12`, `B_4(1/2)=7/240`) gives exactly `c_2=-1/32` and `c_4=49/6144` as claimed, and both reduce correctly to the stated `q=11` targets `(1,10)` (independently re-derived: `-1/32 mod 11 = 1`, `49/6144 mod 11 = 10`).

## 2. q=11 jet reachability and the explicit repair (`v13.255`)

**[N-cert] Confirmed exactly**: the local multiplier formula `Λ_a(r,c)` evaluated at all three worked labels `(1,-1)→(4,5)`, `(3,1)→(6,9)`, `(2,1)→(5,6)`, matching exactly.

**[N-cert] Confirmed exactly, independently computed — the centerpiece of this round.** Built the Euler-factor-corrected generalized Bernoulli numbers for the explicit repair `D=-19`, `S={101,67,47,157}` from the primitive values (not from the ledger's claimed outputs) and got `B_1≡0, B_3≡0, B_5≡4, B_7≡3, B_9≡6 (mod 11)`, giving `J_1=B_7B_5=1`, `J_2=B_9B_5³=10` — exactly the Legendre target `(1,10)` — and `M·B_5≡1` for the stated `h=3`. All match exactly.

Then, independently implementing the conductor-Möbius pushforward formula from scratch (own code, `sympy.mobius`/`divisors`, exploiting the period-209 structure of `χ₋₁₉ mod 19` combined with `mod 11` to make the sum over a modulus of order `4.46×10¹⁰` tractable) reproduced **both** `P_M(t)` for `t=0,…,10` and the folded crossing signal `f(k)` for `k=0,…,10` **exactly**, including the critical value `f(0)=-12`. This is a nontrivial, independently reconstructed confirmation that a carrier satisfying every one of the mod-11 necessary conditions derived so far (lower Hasse zeros, leading signature, full pre-top jet) can still fail exact resonance at the integer level — which is precisely the entry's thesis. I consider this the most rigorously checked single claim across all 8 audit rounds, given the size of the numbers involved.

**[D] Verified by hand**, the discrete-log subgroup-generation argument for `G_{11}^{jet}=(F_11^×)²`: the determinant-mod-5 and parity-mod-2 checks on the three generator vectors are elementary linear algebra over the stated residue rings and check out as stated.

## 3. Strategic pivot to the Suzuki GRH frontier (`v13.256`, `v13.257`)

**[Audit] External citation independently verified — new for this audit.** Searched for Masatoshi Suzuki, "On variants of Chebyshev's conjecture," *The Ramanujan Journal* 68 (2025), article 95, DOI `10.1007/s11139-025-01238-9`. **The paper is real**, matches the stated venue, volume, article number, and DOI exactly, and its publicly described content (weighted von-Mangoldt summatory functions whose sign constancy is equivalent to RH/GRH for Dirichlet L-functions) matches the ledger's characterization of Theorem 8/9. Also searched for the stated correction, "Correction: On variants of Chebyshev's conjecture," and confirmed a correction to this article was indeed published (December 2025) — consistent with `v13.257`'s claim that a publisher correction exists and should be cited going forward. I did not verify every symbol of the Mellin identity against the corrected PDF text itself (that would require fetching and reading the full corrected article), but the citation is genuine, not fabricated, and its general content is accurately characterized. This is an important check to have run: the project is now citing external literature as load-bearing input for the first time in this branch, and a fabricated or mischaracterized citation at that point would have been a serious problem going forward.

**[D] Verified by hand**, the elementary log-derivative decomposition in `v13.256` §4 (`-ζ'_K/ζ_K = -ζ'/ζ - L'/L`, hence Dirichlet coefficients `Λ(n)(1+χ₁₂(n))`) — standard and correctly applied, given the already-audited factorization `ζ_{ℚ(√3)}=ζ·L(·,χ₁₂)`.

**[N-cert] Confirmed exactly, independently computed — `v13.257`'s coefficient-level bridge.** Implemented `a₁₂(n)=Σ_{d∣n}χ₁₂(d)` and the claimed recursion `b(n)=a(n)log n - Σ_{d∣n,d<n}b(d)a(n/d)` from scratch and compared against the direct definition `b(n)=Λ(n)(1+χ₁₂(n))` for all `n=1,…,30`: **exact match in every case**, including the ramified cases (`n=2,3,4,8,9,16,27,...`) and the inert-prime-power alternation this entry uses to correct an oversimplification in `v13.256` (`b(p^k)=log(p)[1+χ(p)^k]`, so inert primes contribute `0` at odd `k` and `2log p` at even `k` — confirmed exactly via `n=5` (`b=0`) vs. `n=25` (`b=log 25=2log5`), since `5` is inert for `χ₁₂`).

**[Audit] Concur** with `v13.257`'s self-correction of `v13.256`'s prime-power oversimplification — this is a legitimate, correctly-derived refinement (`v13.256` only stated the `k=1` case correctly; `v13.257` correctly generalizes to all `k` and the fix is exactly right, as verified above).

## 4. Screw-function specialization to the D12 field (`v13.258`)

**[Audit] Second external citation independently verified.** `v13.258` invokes a second Suzuki paper, "Screw functions of Dirichlet series in the extended Selberg class" (arXiv:2209.12832, *International Journal of Number Theory*, DOI `10.1142/S1793042125500885`). Confirmed this paper is real and its publicly described content — screw functions for the extended Selberg class, with GRH equivalent to non-positivity/non-negativity of the screw function — matches the ledger's characterization of the zero-free formula and the `GRH(F) ⟺ Re(-g_F(t))≥0 eventually` criterion it states.

**[D] Verified by hand**, the one fully self-contained calculus step in this entry (§5): `∫_{log n}^∞ (t-log n)e^{-zt}dt = n^{-z}/z²` follows immediately from the substitution `u=t-log n` and the standard Gamma-type integral `∫_0^∞ u e^{-zu}du=1/z²`; summing termwise against `Λ(n)χ₁₂(n)/√n` then reproduces the claimed Laplace identity `∫₀^∞ R₁₂(t)e^{-zt}dt = -(1/z²)(L'/L)(1/2+z,χ₁₂)` exactly, since the sum is literally `-(L'/L)` evaluated at `s=z+1/2`.

**[D] Verified by hand**, the completed-function normalizations: `Λ₁₂(s)=(12/π)^{s/2}Γ(s/2)L(s,χ₁₂)` is the standard completed L-function for an even primitive character (χ₁₂ is even since `χ₁₂(-1)=+1`, already established in earlier rounds), and `Λ_K(s)=12^{s/2}π^{-s}Γ(s/2)²ζ_K(s)` is the standard completed Dedekind zeta for a real quadratic field with two real places — both correctly instantiate the general formulas with `D_K=12`.

**[D] Concur** with the additivity argument `Φ_K=Φ_ζ+Φ_{12}` (§8): this follows immediately from `ζ_K=ζ·L(·,χ₁₂)` ⟹ additive log-derivatives ⟹ additive (linear) inverse Laplace/screw transforms — a direct, correctly-drawn consequence requiring no new machinery beyond what was already audited in `v13.257`.

**[Audit] Appropriately scoped.** The entry explicitly and repeatedly flags what is *not* proved (GRH for either `L(s,χ₁₂)` or `ζ_K`), and correctly identifies that positivity of a sum (`Φ_K=Φ_ζ+Φ_{12}`) does not imply positivity of either summand — the right caveat to raise before anyone is tempted to claim more than the additive identity supports.

## 5. Overall verdict for this round

**No mathematical error was found in `v13.254`–`v13.258`.** This round contained the single most computationally demanding independent check of the whole audit series (the `M≈4.46×10¹⁰` folded-signal reconstruction in `v13.255`), and it passed exactly. The strategic pivot in `v13.256`–`v13.258` is a genuine improvement in research direction — it correctly identifies that the project's own `χ₁₂` apparatus is literally one of the channels in real, peer-reviewed GRH-criterion frameworks (two separate Suzuki papers, both independently confirmed genuine), and derives exact (not heuristic) coefficient-level and screw-function-level bridges from the project's divisor-staircase work to those frameworks. This is a materially different, more externally-anchored kind of claim than the q=5/q=7/q=11 combinatorial resonance work of prior rounds, and it holds up under scrutiny.

## 6. Scope note

Not independently re-derived this round: the full statements of Suzuki's Theorem 8/9, the Mellin/Fourier-Laplace identities, and the archimedean (Gamma-factor / Hurwitz-Lerch) term formulas were checked for citation accuracy and general topical match, not re-derived or checked symbol-for-symbol against the published PDFs. This is appropriately treated as **[S]** source-established material by the project itself, and I've verified both sources are genuine; a full line-by-line check of each cited theorem's precise statement (especially the exact archimedean constant in `v13.258` §3) is a reasonable follow-up for a future round if the project begins deriving new consequences from their precise hypotheses.

## 7. Guardrails

All guardrails from prior rounds remain in force. Add one new guardrail from this round's practice:

77. When a ledger entry cites external published literature as load-bearing input (not merely background), verify the citation resolves to a real paper with matching venue/volume/DOI before treating its stated theorems as available premises — a fabricated or mischaracterized external citation is a more serious failure mode than an internal algebra error, since it can't be caught by re-deriving the project's own downstream math. This round checked two such citations (Suzuki 2025 Ramanujan Journal + correction, and Suzuki 2022/2025 extended-Selberg-class screw functions); both are genuine.

**External audit round 8: CLOSED. No corrections required to `master`.**
