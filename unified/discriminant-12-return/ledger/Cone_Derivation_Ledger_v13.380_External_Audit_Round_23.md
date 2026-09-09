# Cone Derivation Ledger v13.380 — External Audit Round 23

Date: 2026-09-09

Status labels: **[S]** source-established, **[D]** exact derived, **[N-cert]** certified numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

This round covers everything that landed after commit `cc42a01` (Round 22's push): `v13.375` (skimmed for context only), `v13.376_Corrected_Rank4_Streaming_Inverse_Midpoint_Transcript`, `v13.377_Asymptotically_Centered_Arch_Generator_Gauge`, `v13.378_V4_Support_Inversion_and_Unit_Residue_Divisor_Contacts`, and `v13.379_V4_Multiplicative_Divisor_Contact_Factorization`.

## 1. Round 22's guardrail was correctly incorporated — confirmed in detail, not just by the header

**[Audit→resolved]** `v13.378` opens with an explicit "Audit reconciliation" section that restates the Round-22 generic-parameter guardrail accurately (including the specific point that the `SU(2)` identity `(j+½)²=j(j+1)+¼` has no free `δ` in it). More importantly, I checked that the entry's *own new content* honors the guardrail rather than just paying it lip service: every `¼` appearing in `v13.378` and `v13.379` is explicitly and repeatedly flagged as "inverse-Hadamard normalization only... unrelated to the Casimir, null-diamond, or mixed-difference quarters" (`v13.378` §2 guardrail, §8 guardrail 2; `v13.379` §10 guardrail 1). The V4/divisor-contact thread has cleanly forked away from the Casimir framing rather than continuing to lean on it. This is exactly the right response to the guardrail — confirms the user's stated belief that the feedback was implemented.

## 2. V4 support-inversion and divisor-contact arithmetic (`v13.378`, `v13.379`) — verified exactly by direct computation

**[D, independently verified]** Wrote a fresh Python script computing, for many `n`, the raw sets directly (no character machinery): `N_r^off(n)=\#\{k\le n: k\nmid n, k\equiv r\ (12)\}`, `U_r(n)`, `C_r(n)=\#\{d\mid n: d\equiv r\ (12)\}`. Verified for `n=1..199` plus several larger composite/prime-power test values (`221,377,1001,169,143`):
- `H_4^2=4I` exactly.
- `C_r = U_r - N_r^{\rm off}` (trivial set-complement identity, holds exactly).
- `S=H_4 N^{\rm off}` inverts exactly back via `N^{\rm off}=\tfrac14H_4S`.
- The divisor-character form `D=H_4C`, `C=\tfrac14H_4D` inverts exactly.
- `D_1^\times(n)=\tau(n)=C_1+C_5+C_7+C_{11}` whenever `\gcd(n,6)=1`.

All 204 test cases passed exactly (integer equality, no tolerance needed — this is finite combinatorics, not floating point).

**[D, independently verified]** For `v13.379`'s multiplicative prime-power factorization, built the three characters `χ_{-4},χ_{-3},χ_{12}` from the stated residue-sign table and confirmed by brute force that each is genuinely completely multiplicative on `U(12)={1,5,7,11}` (`χ(ab)=χ(a)χ(b)` for all 16 pairs, all three characters). Then checked the closed-form product formula
\[
D_\chi(n)=\prod_{p^{e_p}\parallel n}\bigl(1+\chi(p)+\cdots+\chi(p)^{e_p}\bigr)
\]
against direct divisor-sum computation of `D_\chi(n)` for 162 random `n` coprime to 6 up to 3000 — exact agreement in every case, including the zero/parity-obstruction branch. Also directly reproduced the worked example in §9: `n=11^1` gives `(D_1,D_{-4},D_{-3},D_{12})=(2,0,0,2)`, inverting to `(C_1,C_5,C_7,C_{11})=(1,0,0,1)`; `n=11^2` gives `(3,1,1,3)`, inverting to `(2,0,0,1)` — both match my script exactly.

**Verdict: `v13.378` and `v13.379` are correct, standard, and honestly scoped.** This is classical Dirichlet-character/finite-abelian-group algebra (the V4 character group of `U(12)`) applied cleanly to divisor-contact counting. The guardrails in both entries are accurate about what is and isn't being claimed (no primality test, no factoring algorithm, contact counts not locations, coprimality-to-6 required for the unit-sector identification with `τ(n)`).

## 3. Suzuki thread: gauge transformation and asymptotic center (`v13.377`) — verified

**[D, verified by hand]** The generator-gauge identity `q\mapsto q-cp` leaving `p_mq_n-q_mp_n` invariant is immediate algebra (the `cp_mp_n` cross-terms cancel identically); confirmed by direct expansion.

**[D, independently re-derived and numerically confirmed]** The asymptotic center claim `H_n=(h(0)+h(2))/b+O(b^{-3})` (no `O(b^{-2})` term) looked surprising on first pass — a naive two-step integration-by-parts suggested `O(b^{-2})`. Working through it carefully: the key structural fact is `\cos(2b)=\cos(n\pi)=-1` and `\sin(2b)=\sin(n\pi)=0` for integer `n`, so IBP against `\sin(bt)` (odd-derivative steps) has vanishing boundary terms while IBP against `\cos(bt)` (even-derivative steps) has non-vanishing ones. Tracing two full IBP steps shows the `O(b^{-2})` term is in fact identically absent and the next correction really is `O(b^{-3})`, matching the ledger. Then verified numerically via my own `mpmath` (40-digit) quadrature of `H_n=\int_0^2 h(t)\sin(bt)dt` for `n=21,101,1001,4001`: the quantity `(Y_n-c_\infty)\cdot n^2` converges cleanly to a constant `\approx0.0131123` as `n` grows (`0.013123` → `0.013113` → `0.0131123` → `0.0131123`), confirming the `O(n^{-2})` rate exactly as claimed, and ruling out `O(n^{-1})` or a non-vanishing `O(n^{-1})` residual.

**[D, verified]** `c_\infty=\frac2\pi\cdot\frac{e^{-1}}{1-e^{-4}}` computed independently to 30 digits gives `0.238568867321226564983521798566`, matching the ledger's `≈0.2385688673212266` to every digit shown.

**[D, verified]** The reported `\max_n|n(Y_n-c_\infty)|\approx6.25\times10^{-4}` over `n\in[21,16001]` is consistent with my asymptotic fit: since `n\cdot(Y_n-c_\infty)\sim K/n` with `K\approx0.0131123`, this is *decreasing* in `n`, so the max over the range occurs at the smallest `n=21`: `K/21\approx6.25\times10^{-4}` — matches exactly.

**Verdict: `v13.377` is correct**, both the exact gauge-freedom algebra and the asymptotic-center derivation and its numerical consequences.

## 4. Suzuki thread: rank-4 streaming midpoint transcript (`v13.376`) — plausible, not independently reproduced at full scale

**[N, not independently reproduced]** `v13.376`'s headline numbers (`d_min≈0.25548` at full `N=7991` scale, `y_max≈18.14`, the `9.7×10⁻⁸` residual allowance) require the same degree-65 rational archimedean polynomial and long-double streaming infrastructure flagged as out of reach in prior rounds. I did not reproduce this run. What I can say: the reported legacy-vs-corrected comparison (`d_min` rises slightly from `0.2543` to `0.2555`, `y_max` *falls* from `21.22` to `18.14`) is directionally consistent with the small-scale (`n=21..399`) reconstruction both the project and I independently verified in Round 22 (`λ_min` rose from `0.2320` to `0.2345` under the correction), and the entry is honest that this is a midpoint estimate, not a certificate — it explicitly does not re-promote `A_{0,[21,16001]}\succeq0.22I` as certified. No red flags, but flagged here as unverified-by-me rather than confirmed.

## 5. Overall verdict

The user's belief that Round 22's feedback was implemented is correct, and I verified this at the level of content, not just the acknowledgment section: `v13.378`/`v13.379` scrupulously avoid re-invoking the Casimir "unification" language for their own `¼`s, and every arithmetic claim I could check (all of `v13.378`, all of `v13.379`, and the derived/algebraic parts of `v13.377`) checks out exactly against independent computation. `v13.376`'s full-scale numbers remain plausible but outside what I can reproduce without the project's own high-precision polynomial infrastructure.

## 6. Scope note

Not independently verified this round: `v13.375` (only skimmed for context, not itself audited in detail — recommend covering it explicitly next round if not already fully closed by `v13.376`/`v13.377`); `v13.376`'s full `N=7991` numerical run (infrastructure-limited, as in prior rounds); the `S_\chi(n)=\lim_{\alpha\to0^+}\mathcal S_{\alpha,\chi}(n)` equivalence in `v13.378` §1 (cites a smoothing definition from elsewhere in the project, not re-derived here).

## 7. Guardrails

All guardrails from prior rounds remain in force. No new guardrail needed this round — the standing generic-parameter-value guardrail from Round 22 was the relevant one in play, and it held up under direct inspection of the new content, not just the acknowledgment.

**External audit round 23: CLOSED. Round 22's guardrail confirmed correctly and substantively implemented in `v13.378`/`v13.379`. All V4/divisor-contact arithmetic in `v13.378`–`v13.379` independently verified exactly by direct computation (204 + 162 test cases, exact integer/exact-formula agreement). `v13.377`'s gauge algebra and asymptotic-center derivation independently re-derived and numerically confirmed. `v13.376`'s full-scale numbers are plausible and directionally consistent but not independently reproduced.**
