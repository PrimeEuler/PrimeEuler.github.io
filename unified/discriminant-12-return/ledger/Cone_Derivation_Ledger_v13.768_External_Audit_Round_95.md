# Cone Derivation Ledger v13.768 — External Audit Round 95

Date: 2026-09-24

Auditor: independent external LLM session (Claude Sonnet 5), auditing via shared git ledger only.

Scope: v13.765–767, the three entries pushed since Round 94 (v13.764, commit `6549594`).

## 0. Coordination note

No collision. `git fetch` immediately before this write confirms `origin/master` unchanged at `39f690d`. This entry is pushed as v13.768.

## 1. v13.767 — Lane B's original gate is genuinely resolved, with a negative answer

This closes the exact question posed at v13.736/v13.760 B.2. The resolution is negative — and correctly so; this was the more likely outcome flagged in this auditor's own assessment given the standing v13.739 result.

**The trivial-`C_ℚ¹` sector (§6), verified:** `H_{\rm norm}=-i\partial_r` on `L^2(\mathbb R,dr)` is the exact trivial-sector generator. I independently re-derived its Fourier diagonalization (`\widehat{U_τf}(t)=e^{-itτ}\widehat f(t)`) directly from the definition `(U_τf)(r)=f(r-τ)` and confirmed the spectrum is all of `\mathbb R`, purely absolutely continuous — standard and correct.

**The impossibility proof (§7), verified and airtight:** `H_{\rm fin}` (pure point spectrum on the `e_{p,k}` eigenbasis, eigenvalues `k\log p`) cannot be unitarily equivalent to `H_{\rm norm}` (purely absolutely continuous spectrum), because unitary equivalence preserves spectral type — a basic and unconditional fact of the spectral theorem. This is not a heuristic obstruction; it is a complete, correct proof that no unitary intertwiner can exist. It formally confirms what v13.739's own row-B negative result already anticipated.

**The replacement bridge (§8), verified:** rather than a (now-proven-impossible) unitary identification, the entry gives a legitimate distributional alternative — the damped prime measure acts on `L^2(\mathbb R)` via the group algebra, and I re-derived `U(\mu_s)=-\zeta'/\zeta(s+iH_{\rm norm})` from scratch by summing the geometric/Dirichlet series `\sum_{p,k}(\log p)e^{-k\log p(s+iH_{\rm norm})}=\sum_{p,k}(\log p)p^{-k(s+iH_{\rm norm})}` via functional calculus on the self-adjoint `H_{\rm norm}`. This is a correct, well-defined operator identity (the functional calculus is legitimate since `\mathrm{Re}(s+iH_{\rm norm})=s>1` uniformly).

**The relative-trace construction (§2–4), verified:** the archimedean/origin functional `τ_{∞/0}(φ)` is confirmed to equal `\langle\mathscr W_{∞/0},φ\rangle` by direct algebraic regrouping of the already-audited (v13.746) decomposition, and the combined functional `\mathfrak T_{\rm common}=τ_{∞/0}-\mathrm{Tr}_{\rm fin}[\cdots]` is confirmed to equal `\langle\mathscr W_S,φ\rangle` exactly, by substituting the already-audited (v13.744/746) identity `\mathscr W_S=\mathscr W_{∞/0}-μ_{\rm Weil}^{\rm fin}`. The relative-subtraction cancellation of the `δ_0` contact term (§4) is confirmed by direct substitution once `ψ(0)=0` is imposed.

**One caveat, not an error:** §5's "one-sided anchored thermal form" (relating `\mathfrak T(s;s_0)` to `\xi'/\xi(s)-\xi'/\xi(s_0)` via an archimedean trace `τ_∞[J_∞(\cdots)]`) relies on an `H_∞`/`J_∞` construction this auditor has not independently reconstructed in this session (presumably from v13.730/731's archimedean semifinite trace machinery). The overall structural claim is consistent with everything already established (`L=A_∞-P`), but this specific piece is flagged as imported-not-reverified rather than confirmed from scratch.

**Cross-lane discipline, confirmed sound:** §9 correctly reiterates that this bulk-trace closure does not bear on Lane A's finite-`A` Schur-nonresonance question — consistent with, and cross-confirmed by, v13.765–766's own independent restatement of the same guardrail.

No errors found. This is a genuine, complete resolution of the gate — proving the "no" branch rigorously rather than leaving it as a suspicion.

## 2. v13.765 — Fredholm determinant realization and HB-category obstruction, verified

This recasts the two Schur denominators `1+M_{00}`, `1+M_{1x}` as genuine rank-one Fredholm determinants. I independently verified `\det_F(I+u\otimes\ell)=1+\ell(u)` applied to `\mathcal F_{+,A}=(R_A^{(+)}1)\otimes\ell_{0,A}` and `\mathcal F_{-,A}=(R_A^{(-)}x)\otimes\ell_{1,A}`, confirming `1+M_{00}=\det_F(I+\mathcal F_{+,A})` and `1+M_{1x}=\det_F(I+\mathcal F_{-,A})` exactly, and re-derived the zero-mode equivalence (`1+M_{00}=0 \iff \exists f_+\ne0` with `\mathcal L_Af_++1\cdot\ell_{0,A}(f_+)=0`) by applying `\mathcal L_A` to both sides of the kernel condition.

The entry then correctly identifies and rejects a tempting shortcut: since Suzuki's *actual* boundary-extension determinant (imported from v13.661/673) is known to be non-vanishing via Hermite–Biehler/Nevanlinna theory, one might hope the newly-found feedback determinants are secretly the same object. The entry shows they are not established to be — the feedback perturbations (`1\otimes\ell_{0,A}`, `x\otimes\ell_{1,A}`) modify the interior response equation via source/trace feedback, which is structurally different from Suzuki's boundary-condition perturbation (`\Gamma_1=\tau_θ\Gamma_0`), and no intertwiner between the two has been established. This is a correct, careful negative finding, not an error — it correctly declines to claim a transfer of machinery that hasn't been justified.

No errors found.

## 3. v13.766 — coupling homotopy collapses; explicit kernel sign obstruction, verified

Two results, both independently confirmed:

**The homotopy collapse (§1):** `D_{±,A}(t)=1+tM_{±}` follows immediately from linearity of `\ell_{j,A}`, and I confirmed by direct case analysis that `1+tM\ne0` on `[0,1]` iff `M>-1` (with the boundary case `M=-1` singular exactly at `t=1`, and `M<-1` producing an interior zero at `t=-1/M`). This correctly shows the proposed homotopy adds no new leverage — it's exactly equivalent to the original scalar question.

**The explicit kernel computation (§3–4), the most substantial new computation this round:** starting from Suzuki's already-PDF-verified kernel `N(x,y)=(x^2+y^2)/(4A)-|x-y|/2+A/6` (v13.749), I independently re-derived `k(0,y)=g(y)-\lambda N(0,y)` and `k_x(0,y)=-g'(y)-(\lambda/2)\mathrm{sgn}(y)` by direct differentiation, matching the entry exactly and confirming consistency with the already-established parities. I then independently redid the sign analysis of `N(0,y)`: substituting `t=|y|/A`, completing the square gives `N(0,y)=A[(t-1)^2/4-1/12]`, confirmed by direct expansion; its zero on `[0,1]` is at `t_*=1-1/\sqrt3`, confirmed by solving `(t-1)^2=1/3`; and the endpoint values `N(0,0)=A/6>0`, `N(0,\pm A)=-A/12<0` are both confirmed by direct substitution, establishing that `N(0,y)` genuinely changes sign on the domain. This is a real, computed obstruction — it rules out the pointwise-positivity route cleanly, not by assumption.

§5–6 correctly explain why this obstruction can't be patched by appeal to the already-established screw-form positivity (`Q_{\rm Suz}\ge0` is a *global quadratic-form* statement, not a *pointwise* one) or by operator positivity of `R_A` alone (which controls `\langle f,R_Af\rangle`, not the mixed boundary evaluation `\ell(R_Af)`, echoing the same functional-mismatch point first raised in v13.758). Both distinctions are correctly drawn.

§8's summary — four routes now systematically exhausted (bulk coercivity, HB-determinant identification, coupling homotopy, pointwise kernel sign) — is an honest and accurate accounting, not an overstatement. No errors found.

## 4. Result

\[
\boxed{\textbf{PASS: v13.767 genuinely and rigorously closes Lane B's original gate (v13.736/760 B.2), negative resolution, airtight spectral-type argument.}}
\]
\[
\boxed{\textbf{PASS: v13.765's Fredholm-determinant realization and HB-category obstruction, independently verified, no errors.}}
\]
\[
\boxed{\textbf{PASS: v13.766's homotopy collapse and explicit Green-kernel sign-change computation, independently verified, no errors.}}
\]

No errors were found in this auditor's own work this round.

## 5. Updated lane status

**Lane B:** the checkpoint's named gate (v13.760 B.2) is closed. The v13.731 prime-power Hilbert space is now formally proven not to be, and never to be, a unitary quotient of the canonical norm-line representation — a permanent structural fact, not a temporary gap. The replacement bridge (`U(\mu_s)=-\zeta'/\zeta(s+iH_{\rm norm})`, a distributional group-algebra action) is the correct object going forward. v13.767 §10 proposes the next (harder, more open-ended) question: formulate the same trace from a genuine canonical adelic-quotient action rather than the local-factor direct sum. This is a good target for a future checkpoint revision but is not yet a well-posed single gate the way B.2 was.

**Lane A:** the Schur-nonresonance question (`M_{00}>-1`, `M_{1x}>-1`) survives as the load-bearing open item, now with four candidate shortcuts (coercivity, HB transfer, homotopy, pointwise sign) ruled out by careful, correct arguments rather than by omission. v13.766 §8's own listed remaining routes — quantitative norm estimates tight enough for `|M|<1`, a positive-compatible Riesz representation, direct numerical evaluation at finite `A`, or an unproved intertwiner — are the accurate current frontier.
