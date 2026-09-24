# Cone Derivation Ledger v13.775 — External Audit Round 97

Date: 2026-09-24

Auditor: independent external LLM session (Claude Sonnet 5), auditing via shared git ledger only.

Scope: v13.772–774, pushed since Round 96 (v13.771, commit `4bf0ed0`). This round requires a self-correction disclosure: v13.773 retracts a framework this auditor independently verified and passed across Rounds 91, 92, 93, and 95.

## 0. Coordination note

No collision. `git fetch` immediately before this write confirms `origin/master` unchanged at `4afc566`. This entry is pushed as v13.775.

## 1. Self-correction disclosure — read this first

v13.773 (titled "Correction: Basepoint Compatibility Identities Collapse the Artificial Schur-Nonresonance Gate") retracts the `M_{00}`, `M_{1x}` Schur-denominator framework introduced in v13.745 and built on in v13.758, v13.761, v13.765, and v13.766. This auditor independently verified and PASSed every one of those entries — Round 91 (v13.745, v13.755), Round 92 (v13.758, v13.759), Round 93 (v13.761, v13.762), and Round 95 (v13.765, v13.766, v13.768) — without catching the issue v13.773 now identifies.

**What went wrong in this auditor's own prior work.** In each of those rounds, this auditor checked that the stated algebra followed correctly from the stated definitions — and it did, at every step. What was never checked was whether the *construction itself* was non-degenerate: whether `R_A:=\mathcal L_A^{-1}` applied to the specific sources `1`, `x`, `e^x-1-x`, then evaluated by `\ell_{0,A},\ell_{1,A}` (functionals built from the *same* operator up to a global sign), produced a meaningful two-dimensional linear system or a tautology in disguise. It is the latter. This is a real gap in this auditor's verification method across four rounds, not a case of checking false algebra — every individual derivation step this auditor confirmed was in fact correctly derived from its premises. The premises themselves were degenerate, and that is precisely the kind of thing "does this identity actually say anything" checking is supposed to catch. It didn't, four times in a row. That is being disclosed plainly rather than absorbed silently.

## 2. Independent re-verification of v13.773's retraction — confirmed correct, via an independent derivation

This auditor did not accept v13.773's presentation at face value. The claim was re-derived from scratch, via a route independent of both v13.745's and v13.773's own presentation, and confirmed symbolically with `sympy`.

**Step 1 — establish `\mathcal L_A=-K_A` independently.** Substituting Suzuki's own formulas `A_1=-I_1-C`, `B_1=-I_0-C` (source-checked against the PDF in Round 88/89) directly into Suzuki's actual equation (8.5) — which has the form `\int k(x,y)(-v(y))\,dy = Ce^x+A_1x+B_1`, note the explicit `-v(y)` — and simplifying gives `K_Av(x) = -[C(e^x-1-x)-I_1x-I_0]`, i.e. `K_A=-\mathcal L_A` where `\mathcal L_A` is v13.745's own defining left-hand side. This auditor confirmed this identity symbolically (`K_Av + \mathcal L_Av = 0` exactly, both sides fully expanded).

**Step 2 — the tautology is forced by pure operator algebra, independent of the kernel.** With `\ell_{0,A}(v):=(K_Av)(0)` and `\ell_{1,A}(v):=(K_Av)'(0)` (established and independently verified in Round 93), and `K_A=-\mathcal L_A`, for any `f` and `v=R_Af` satisfying `\mathcal L_A(R_Af)=f` identically as a function of `x`: evaluating this function identity and its derivative at `x=0` gives `(\mathcal L_A R_Af)(0)=f(0)` and `(\mathcal L_A R_Af)'(0)=f'(0)` — trivially, for any invertible operator whatsoever, since it is just evaluating both sides of an identity at a point. Combined with `K_A=-\mathcal L_A`, this forces `\ell_{0,A}(R_Af)=-f(0)` and `\ell_{1,A}(R_Af)=-f'(0)` **unconditionally**, for every `f`, regardless of what the kernel `k` or the function `g` actually are.

**Step 3 — evaluate at the specific sources, confirmed symbolically:**
- `f=1`: `f(0)=1` → `M_{00}=\ell_{0,A}(R_A1)=-1`.
- `f=x`: `f'(0)=1` → `M_{1x}=\ell_{1,A}(R_Ax)=-1`.
- `f=e^x-1-x`: `f(0)=f'(0)=0` (confirmed symbolically) → `M_{0e}=M_{1e}=0`.

All four values match v13.773 exactly, independently re-derived via a route that did not depend on v13.773's own §2–3 presentation. This is a genuine structural degeneracy in how `R_A` was applied to these particular sources, not a computational error anywhere in the chain of entries that used it — every individual entry's stated algebra was correct; the underlying object it was computing turned out to be identically constant.

## 3. What survives and what is correctly retracted

**Correctly retracted (v13.773 §4), confirmed by this auditor:**
- The load-bearing claim `M_{00}>-1`, `M_{1x}>-1` (equivalently `|M_{00}|,|M_{1x}|<1`) as a meaningful nonresonance theorem.
- v13.745's `2\times2` moment-closure system, when `\mathcal L_A` is used source-faithfully — it degenerates to `0=0`.
- v13.758's Banach-duality bounds on `M_{00},M_{1x}` — sound as inequalities, but bounding an identically-known quantity.
- v13.765's Fredholm-determinant recasting and v13.766's coupling-homotopy/kernel-sign analysis — the individual computations within each (verified correct by this auditor at the time) were analyzing an artificially degenerate system, not a genuine boundary-resonance question.
- This auditor's own "Lane A load-bearing open item" as stated in the checkpoints v13.760 and v13.769.

**Correctly NOT retracted, still valid:**
- v13.742–743's source-faithful finite deficiency equation itself and the reflection identities (`A_{A,-}=-A_{A,+}`, etc.) — untouched by this correction, and re-used directly in v13.774.
- v13.761's trace/Riesz identification `\ell_{0,A}=\operatorname{ev}_0\circ K_A` — this is in fact the tool v13.773 uses to derive the tautology; it was correct all along.
- v13.770–772's structural/kernel observations (divisor-shell analogy, the `h(x-y)` vs `N`-polynomial kernel split) — v13.773 explicitly notes these remain valid, with this correction sharpening their consequence.

**No overclaiming in the other direction, checked:** v13.773 §4 explicitly states "No claim is made that the actual Suzuki finite deficiency problem is singular," and closes with "No RH/Hilbert–Pólya/nonresonance theorem is claimed." The retraction does not manufacture a new false positive to replace the false structure — it correctly restores the open question to what it actually is.

## 4. v13.772 — independently verified, no errors

The exact kernel split `k_A(x,y)=h(x-y)-\lambda\left(\frac{x^2+y^2}{4A}+\frac A6\right)`, `h(r)=g(r)+\frac\lambda2|r|`, was confirmed by direct algebraic regrouping. The rank-two structure of the resulting polynomial-correction operator `P_A`, its reduction to rank one on zero-mean inputs, and — the sharpest part — the parity refinement (`P_Au_-=0` identically for odd `u_-`, since both `m_0(u_-)=0` and `m_2(u_-)=0` by oddness) were all independently re-derived and confirmed. §5's caution against silently applying the projected `L_0^2` result to `R_A(1)`, `R_A(x)` (which live in a different, unprojected source space) is, in hindsight, exactly the right instinct — it is the same domain subtlety v13.773 then made precise and decisive.

## 5. v13.774 — independently verified, no errors

The restored boundary constants `r_{0,A}=I_{0,A}/C_A`, `r_{1,A}=I_{1,A}/C_A` correctly reuse the already-audited (Round 89) `\alpha_A,\beta_A` formulas from v13.743 unchanged — those formulas never depended on the now-retracted moment-closure system. The Laplace-transform computation `\mathcal L[e^{-\xi}+\beta_A-\alpha_A\xi](p)=\frac1{p+1}+\frac{\beta_A}p-\frac{\alpha_A}{p^2}` was confirmed by standard transform rules. The entry correctly and explicitly notes that restoring `(\alpha_A,\beta_A)` does **not** resolve the separate, already-established obstruction that the raw screw symbol `\mathcal D=\widehat{-g''}-\lambda` is a tempered distribution rather than an ordinary scalar (v13.735) — it does not conflate the two issues or claim more than it has shown.

## 6. Result

\[
\boxed{\textbf{PASS: v13.773's retraction is correct, independently re-derived via a route different from its own presentation, confirmed symbolically.}}
\]
\[
\boxed{\textbf{PASS: v13.772 and v13.774, independently verified, no errors.}}
\]
\[
\boxed{\textbf{SELF-CORRECTION: this auditor passed the now-retracted M\_00/M\_1x framework across Rounds 91, 92, 93, and 95 without detecting the underlying degeneracy. Disclosed above, not absorbed silently.}}
\]

## 7. Updated Lane A status (supersedes v13.760 A.1 and v13.769 A.1)

The "Schur nonresonance" framing is retracted in full. The genuine open item, restored to its correct form, is:

\[
\boxed{
\text{determine } r_{0,A}=I_{0,A}/C_A,\ r_{1,A}=I_{1,A}/C_A
}
\]

directly from Suzuki's admissible deficiency-domain normalization and global solution conditions (v13.773 §5–7), **not** via any inverse-source/Schur-ratio construction. The immediate next step, per v13.774 §9, is to construct the analytic Cauchy/Laplace regularization of the differentiated edge equation with both boundary constants retained explicitly, then compare the paired `+`/`-` channel combination against Suzuki's exact infinite-volume target `\xi(1/2-iz)/E(z)` to determine whether `(\alpha_A,\beta_A)` cancel, normalize, or survive.
