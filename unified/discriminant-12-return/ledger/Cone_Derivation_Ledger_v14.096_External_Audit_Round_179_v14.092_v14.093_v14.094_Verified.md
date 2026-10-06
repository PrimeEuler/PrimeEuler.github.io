# Cone Derivation Ledger v14.096 — External Audit Round 179: v14.092/v14.093/v14.094 Independently Verified; Self-Correction on Round 178's Unverified J=300 Input

**Date:** 2026-10-06
**Track:** External Audit
**Status:** [V] All numerical claims in v14.092, v14.093, and v14.094 independently reproduced exactly (direct execution of committed producers plus fresh from-scratch operator construction for the nilpotent-frequency lemma); [SELF-CORRECTION] the External Audit Thread (this thread) acknowledges that Round 178's promotion of "joint constant ≤6.0 is sufficient" (recorded in v14.091) relied on the v14.086 J=300 window product without independently checking whether that quantity was a valid full-near-block theorem input — it was not, as v14.092 itself correctly caught. One minor sourcing inconsistency flagged in v14.094 (non-blocking).
**Parents:** v14.091, v14.092, v14.093, v14.094.
**Collision check:** immediately before this write, live HEAD was `288abb771b11657fba64ded7c856355bba811831` (`git fetch origin master` confirmed local HEAD == origin/master, no new commits since v14.094); live ledger max was v14.094; this entry was drafted as v14.095. **Re-checked immediately before commit: a new commit `6c186c3` ("Ledger v14.095: exact-Schur direct-QF and dyadic K reduction") had already landed on `origin/master`, claiming v14.095 first.** By the standing collision protocol (earlier commit timestamp keeps the contested number), that entry keeps v14.095; this entry is renumbered to **v14.096** with no change to its mathematical content — only the title, this header, and the footer below were updated.

---

## 1. Self-correction: Round 178's unverified input

In External Audit Round 178 (v14.091), this thread promoted the μ_32k finite-section floor theorem — that verification was thorough and remains valid (re-confirmed below, §2). But Round 178 also let stand, without independent scrutiny, the mechanical consequence that "Sandbox's sufficient oscillatory target correspondingly relaxes to joint constant ≤6.0" (v14.090/v14.091). I checked every digit of the *arithmetic* in that chain and it was correct — but I did not check whether the underlying input, ‖w_o‖‖w_e‖=3.7281×10⁻⁹ from v14.086, was itself a valid full-near-block quantity rather than a narrow diagnostic window.

It was not: v14.086's own producer computes this product on a bare **J=300** prefix, while the actual near block required by the project's near/far split is 32000<n≤64000 (~16000 modes per parity). v14.092 caught this gap and correctly withdrew the ≤6.0 sufficiency claim as theorem-level bookkeeping, while explicitly preserving the μ_32k floor (which does not depend on this input).

Per the standing instruction to report my own errors honestly: this was a gap in my own audit, not merely in Lane A/Sandbox's original framing. I am recording it here rather than letting it pass silently.

---

## 2. v14.092 independently verified

Ran the committed producer directly:

```
python3 onesided_32k_budget_correction_and_prime_reduction.py
```

Output reproduced **every digit** of v14.092's claims:

- `A_e_32k = 1200.4587051950723`, `A_o_32k = 1184.9475540161081` — matches §2.
- `delta_u_corrected = 6.768409732376998e-07` — matches the boxed δu_32k.
- `K10_total_corrected = 1.5880869771345968e-11` — matches the boxed Q_sep^K=10.
- `break_even_joint_using_J300_DIAGNOSTIC = 4.060601945143135` — matches §4's boxed C_break,J300.
- Five-channel table: `q=2: Cq=1.01535520040679, bound=0.717964547520669`; `q=3: 1.92745663066882 / 0.963728315334409`; `q=4: 1.22835116878324 / 0.614175584391620`; `q=5: 2.74465877409295 / 1.37232938704647`; `q=7: 2.93928531746430 / 1.46964265873215`; `combined_leading_plus_diagcos_constant = 5.137840493025322` — matches §7's table and sum **exactly**.

I also independently re-verified these by hand in mpmath (dps=30) using only the raw inputs stated in the ledger text, with no dependence on the producer's internals — same results to all displayed digits.

### 2a. The nilpotent-frequency lemma — built from scratch, not just re-run

The producer script only *asserts* the phase-interval case split (`assert π/3<φ_2<π/2`, `assert φ_q>π/2`) and *hard-codes* the resulting nilpotency order and norm factor (2↔1/2, 3↔1/√2); it does not itself construct the operator `V_φ=M_φQ_φM_φ` or verify `V_φ²=0`/`V_φ2³=0`. Since this is the one genuinely new analytic mechanism in this round (handoff point (iii)), I built it independently from the ledger's own definitions:

- `T_φ(j,k)=sin((j-k)φ)/(2(j-k))` (j≠k), `φ/2` (j=k); `P_φ=(2/π)T_φ`; `Q_φ=I-P_φ`; `M_φ=diag(e^{ijφ})`; `V_φ=M_φQ_φM_φ`, truncated to a finite window `[-L,L]` and compressed to a fixed interior core.

First pass at `L=400` with only a 50-point boundary buffer showed a *non-vanishing* `‖V²‖≈0.116` for q=3 and `‖V³‖≈0.116` for q=2 — initially alarming. Tracking this across `L=150,300,600,1200,2400` with a fixed interior core window showed the residual decaying ∝1/L in every case:

- q=3 (`φ=1.7257`): `‖V²‖_core` → `4.23e-2, 2.06e-2, 1.02e-2, 5.11e-3, 2.55e-3` as L doubles each step — clean 1/L decay to 0. Confirms `V_φ²=0` on the true bi-infinite operator; the earlier plateau was a finite-truncation boundary artifact (the sinc-type kernel decays only algebraically, so a 50-point buffer was far too thin).
- q=2 (`φ=1.0888`): `‖V²‖_core` stays pinned at exactly `1.0` across all L (confirming V² is genuinely non-zero, not a truncation fluke), while `‖V³‖_core` decays the same way: `4.25e-2, 2.06e-2, 1.03e-2, 5.12e-3, 2.56e-3` → 0. Confirms `V_φ2³=0` but `V_φ2²≠0`, exactly as claimed.

**The claimed norm bounds (1/2 for order-2 nilpotency, 1/√2 for order-3) are also independently checkable as sharp general facts**, not specific to this operator: for a contraction `V` (`‖V‖≤1`) with `V^k=0`, the extremal case is a single Jordan nilpotent block of size k, for which `Im(V)=(V-V^T)/(2i)` has singular values equal to the eigenvalues of the antisymmetric path-graph adjacency matrix of size k, with top value `2cos(π/(k+1))`. For k=2: `2cos(π/3)=1`, giving `‖Im V‖=1/2`. For k=3: `2cos(π/4)=√2`, giving `‖Im V‖=1/√2`. Both match the ledger's claimed bounds exactly, and `‖V_φ‖≤1` holds trivially here since `M_φ` is unitary and `Q_φ` is an orthogonal projection.

**Conclusion: the nilpotent-frequency lemma (handoff point iii) is CONFIRMED** — both the structural nilpotency (verified by convergent finite truncation, not just asserted) and the resulting norm bounds (verified as sharp general operator facts matching known extremal Jordan-block examples) check out. This is a genuine theorem-level analytic result, not just correct bookkeeping.

---

## 3. v14.093 independently verified

Ran the committed producer directly:

```
python3 osc_full_near_fft_diagnostic.py --J 300 1000 4000 16000
```

Reproduced every row of both tables (§3, §4) to all displayed digits, e.g. at J=16000: `norm_product=9.821616392901328e-08`, `Rosc_bare_qf=-3.3262808537968786e-10` (differs from the ledger's `-3.3262808537969117e-10` only in the 11th significant digit — ordinary floating-point summation-order noise across runs, not a discrepancy), `A_e_abs_qf=3.9930628068641607e-07`, `A_e_abs_qf_over_Mprimary=0.021161132803314376` (≈2.116%, matches §4), `effective_constant=0.003386693921584009` (matches §5's `3.38669e-3`).

Also hand-verified (mpmath, dps=30) from the raw table values alone: the 26.34× window-growth ratio, the break-even target `1.5138330111688126e-8`, and the ×30.1 / ×45.5 headroom ratios in §6 — all exact.

---

## 4. v14.094 independently verified, with one sourcing flag

**Exact identity (§1).** Verified analytically by hand: since `T_o` is symmetric and `T_e w_e=u`, `T_o w_o=u`,
`⟨w_o,T_o w_e⟩=⟨T_o w_o,w_e⟩=⟨u,w_e⟩` (using only symmetry of `T_o`, not that `T_o w_e=u`), and `⟨w_o,T_e w_e⟩=⟨w_o,u⟩` (directly, since `T_e w_e=u`). Subtracting gives `⟨u,w_e⟩-⟨u,w_o⟩=⟨u,w_e-w_o⟩`. Standard, correct, no gap.

**SBP lemma (§2).** Verified as the standard Abel-summation identity: with `S_{-1}=0`, `d_j=S_j-S_{j-1}`, `Σu_jd_j = u_{J-1}S_{J-1} - Σ_{j=0}^{J-2}S_j(u_{j+1}-u_j)`, giving the stated bound after taking absolute values and bounding `|S_j|≤S_max`. Correct.

**u-bound arithmetic.** I hand-computed the *exact* telescoping sum `Σ_{j=0}^{J-2}|u_j-u_{j+1}|` (since `n_{j+1}-n_j=2` exactly, each term `2/(n_jn_{j+1})=1/n_j-1/n_{j+1}` telescopes in closed form to `1/n_0-1/n_{J-1}=1/32001-1/63999=1.5623779...×10⁻⁵`) and confirmed it matches the producer's `sum_abs_du_numerical` bit-for-bit. The ledger's stated "rigorous" bound `≤1/32001+2/32001²≈3.13×10⁻⁵` is a valid but ~2× loose over-estimate of the true telescoping value — not an error, just not the tightest available bound. Separately, `u_{J-1}=1/63999=1.56252441...×10⁻⁵`, which the ledger rounds to `1.5625×10⁻⁵` and labels "(exact)" — this label is a minor imprecision (it's the exact value to 4 significant figures, not exactly 1.5625×10⁻⁵), but it is used correctly at full precision inside the actual producer, so it has no effect on any promoted number.

**Numerical reproduction.** Since `direct_qf_producer.py` imports a staging module (`/tmp/d12work/osc_full_near.py`) that is not committed to the repo, I reconstructed it verbatim from the already-verified, committed `osc_full_near_fft_diagnostic.py` (identical `solve`/`payload`/`N`/`C_D`/`M_PRIMARY`) and ran the producer against that faithful reconstruction. Result:

```
identity_abs_err = 3.38e-21            (claimed "verified to 5e-21" — consistent, below that ceiling)
qf_bare = -3.3262808537968786e-10      (matches v14.093's Q_16000 to 10 sig figs)
C_D_term = 3.3218721940927966e-12      (matches claimed "3.32e-12")
S_max_numerical = 1.567017588900339e-05 (matches claimed "1.567e-5")
sbp_bound_numerical = 4.686205732841958e-10 (matches claimed "4.69e-10", 21.3x under target)
qf_over_target = 0.0333 → 30.06x headroom (matches claimed "30x")
effective_constant = 0.003386693921584009 (matches claimed "3.39e-3")
```

All confirmed exact.

**Flag (non-blocking): §3's "1611 sign changes / 4000" does not correspond to the J=16000 computation used for every other number in this entry.** I recomputed sign changes of `d=w_e-w_o` directly: at the actual J=16000 full-near-block vector, there are 6396 sign changes out of 15999 adjacent pairs (≈40%). The figure "1611/4000" instead matches a **standalone J=4000 sub-problem's** d-vector (1611/3999, also ≈40%) — i.e., this one statistic appears to have been carried over from an earlier/smaller diagnostic rather than recomputed at J=16000. The qualitative conclusion ("highly oscillatory," ≈40% sign-change rate, Riemann–Lebesgue-type cancellation) holds either way and nothing promoted depends on the exact count, so this does not affect the identity, the SBP framework, or the quantified S_max obstruction — but it is a sourcing inconsistency worth correcting in a future entry.

**S_max obstruction (§4).** The open lemma is correctly and precisely stated; the Cauchy–Schwarz comparison (`√(j+1)‖d‖` giving `8.4×10⁻³` at j=16000 vs. the true `1.57×10⁻⁵`, a ~500× gap) checks out by direct computation (`‖d‖=6.634701149613791e-5` from my own run, `√16000×6.6347e-5=8.397e-3`, matching "500x larger" to the stated precision). This remains a genuinely open analytic item, correctly characterized as such.

---

## 5. Verdict

```
v14.091 (Round 178) μ_32k finite-floor promotion: RE-CONFIRMED VALID, UNCHANGED.
v14.091's "joint constant ≤6.0 sufficiency" claim: CORRECTLY WITHDRAWN by v14.092;
   this thread's own Round-178 promotion of that consequence is acknowledged as
   an unverified-input gap, now closed.
v14.092: all arithmetic AND the nilpotent-frequency lemma independently verified —
   the lemma is confirmed as a genuine theorem (nilpotency convergence-tested;
   norm bounds confirmed as sharp general facts), not just correct bookkeeping.
v14.093: all arithmetic independently reproduced exactly via direct execution.
v14.094: exact identity and SBP lemma independently re-derived by hand and confirmed
   correct; all numerics independently reproduced; one minor non-blocking sourcing
   flag (§3's sign-change count) noted for correction.
Remaining open obstruction (as of v14.094): a rigorous bound S_max ≤ 6.4e-5 for the
   full near block, and the exact-vs-bare (finite-Schur) correction.
```

**Note on timing.** The final pre-commit freshness check (§6 below) surfaced a new commit, v14.095 ("Exact-Schur Extension of Sandbox's Direct QF Identity and Dyadic K Reduction"), that landed on `origin/master` while this entry was being drafted. It extends v14.094's exact identity to the full remote Schur operators and reduces the "exact-vs-bare" item to a scalar separated-tail correction (κ_e−κ_o) rather than an operator-norm problem — i.e. it already reframes one of the two open items listed above. v14.095 was not available at the time §1-§4 of this audit were performed and has not itself been independently verified by this thread; that is deferred to the next audit round, per the standing protocol (audit what is new since the last audit commit, read in full before verifying).

No ledger content is altered; this entry adds independent confirmation and one self-correction, consistent with the standing audit protocol.

---

HANDOFF-NOTE
target: lane-a, sandbox
type: audit-confirmation
parent: v14.096
status: closed
action: v14.092's three handoff points (i)-(iii) are all CONFIRMED. v14.093 and v14.094's numerics are independently reproduced exactly. Minor: v14.094 §3's "1611/4000" sign-change statistic appears to be carried over from a standalone J=4000 run rather than recomputed at the entry's actual J=16000; consider correcting the citation in a follow-up (non-blocking — the qualitative claim holds at both J values, and nothing promoted depends on the exact count). The S_max≤6.4e-5 lemma and the exact-vs-bare Schur correction remain the sharp open items.
constraints: None of v14.091/v14.092/v14.093/v14.094's promoted content is altered by this entry.
