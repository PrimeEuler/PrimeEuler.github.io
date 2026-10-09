# Cone Derivation Ledger v14.212 — External Audit Round 210: v14.210's Whole-Remote Schur Model and Finite-Lift Contract Independently Verified

**Date:** 2026-10-09
**Track:** External Audit
**Status:** [V] The full-finite-inverse decomposition, the exact Near/Far channel-remainder identity (the hardest analytic step in this batch), the entrywise remainder bound, the $\chi<21$ coupling-energy bound, and the trace-aware finite-lift energy bound are all independently re-derived from scratch by hand, with no step accepted on the strength of its own presentation. [V] The complete numerical budget is independently reproduced byte-for-byte via a fresh, unmodified run of the committed script against the pinned actual-256k certificates from the frozen v14.207 archive. No correction found.
**Parents:** v14.071, v14.147/v14.156/v14.157, v14.174/v14.177, v14.185, v14.195–v14.211.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `1311ab178a8edf577e7516aa43a3984a95f04c03` (v14.211), matching local HEAD; live ledger max was v14.211. v14.212 is next-free. No collision.

---

## 1. Full finite-inverse decomposition (§2) — independently re-derived

Checked the conjugacy claim $QAW_s=0$ from scratch: with $W_s=W_c-C^{-1}F_g$, $F_g=QAW_c\in Q$, and $C=QAQ|_Q$: $QAW_s=QAW_c-QAC^{-1}F_g=F_g-QAQ(C^{-1}F_g)=F_g-C(C^{-1}F_g)=F_g-F_g=0$, confirmed exactly (using $C^{-1}F_g\in Q$ so $QAC^{-1}F_g=QAQ(C^{-1}F_g)=C(C^{-1}F_g)$). Given this $A$-conjugacy between $\mathrm{ran}(Q)$ and $\mathrm{ran}(W_s)$, which together span the full finite space, the standard block decomposition gives $A^{-1}=QC^{-1}Q+W_sH^{-1}W_s^*$ with $H=W_s^*AW_s\succeq hI$. Independently re-derived the norm bound: $\|A^{-1}\|\le\|QC^{-1}Q\|+\|W_sH^{-1}W_s^*\|\le1/\gamma+\|W_s\|^2/h$, and $\|W_s\|\le\|W_c\|+\|C^{-1}F_g\|\le\|W_c\|+f/\gamma$ (triangle inequality plus $\|C^{-1}\|\le1/\gamma$), giving exactly $G=1/\gamma+[\|W_c\|+f/\gamma]^2/h$ as stated, with no orthonormality assumption anywhere in the chain.

## 2. The exact Near/Far channel-remainder identity (§4) — independently re-derived from scratch, not merely read

This is the most intricate claim in the batch, so it was reconstructed term by term without consulting the entry's own derivation steps, starting only from the elementary geometric identity $\frac1{1-x}=\sum_{k=0}^{K-1}x^k+\frac{x^K}{1-x}$ with $x=(m/n)^2$. Multiplying by $(z_nm-nz_m)/n^2$:
$$\frac{z_nm-nz_m}{n^2-m^2}=\frac{z_nm-nz_m}{n^2}\sum_{k=0}^{K-1}\Big(\frac mn\Big)^{2k}+\frac{z_nm-nz_m}{n^2-m^2}\Big(\frac mn\Big)^{2K}.$$
Expanding each summand, $\frac{z_nm-nz_m}{n^2}(m/n)^{2k}=\frac{z_n}n(m/n)^{2k+1}-\frac1n z_m(m/n)^{2k}$, and matching term by term against the table: the "$(z_n/n)(R/n)^{2k+1}$" row times "$c(m/R)^{2k+1}$" column reproduces the first piece exactly for $k=0,\dots,K-1$; the "$(1/n)(R/n)^{2k}$" row times "$-cz_m(m/R)^{2k}$" column reproduces the second piece exactly, but **only for $k=1,\dots,K-1$** — the entry's table deliberately starts this second series at $k=1$, not $k=0$. Independently traced where the missing $k=0$ term goes: it is exactly $-cz_m/n$, which is exactly the $-cz_m$ part of $w_1(m)=-cz_m+\alpha Lp_m$ in the row-$1/n$ channel. The remaining $\alpha Lp_m/n$ part of that same channel, together with the final row $(p_n-L/n)$ times column $\alpha p_m$, reconstructs $\alpha p_np_m$ exactly via the trivial identity $\alpha p_m[L/n+(p_n-L/n)]=\alpha p_np_m$ — confirming the pole term is split exactly, not truncated. Summing everything reproduces $B_K(n,m)=B(n,m)-E_K(n,m)$ exactly, with $E_K(n,m)=c(z_nm-nz_m)/(n^2-m^2)\cdot(m/n)^{2K}$, matching the entry's stated remainder precisely. (As a side confirmation, the $w_1(m)=-cz_m+\alpha Lp_m$ column is exactly the same leading-source definition certified as $w_{1,p,R}$ in v14.203/v14.207 — a genuine, independently-noticed cross-consistency between this entry and the earlier M11 self-energy work, not asserted by either entry.)

Independently re-derived the entrywise remainder bound: for $m\le R<n/2$ (so $m<n/2$, $n^2-m^2>\tfrac34n^2$), $|c(z_nm-nz_m)|\le8m+11n<4n+11n=15n$ (using $|z_n|<8$ remote, $|z_m|<11$ finite, $m<n/2$), giving $|c(z_nm-nz_m)/(n^2-m^2)|<15n/(\tfrac34n^2)=20/n$, hence $|E_K(n,m)|<(20/n)(m/n)^{2K}\le(20/n)(R/n)^{2K}$ — confirmed exactly, matching the entry's stated bound and the script's own asserted inequality.

## 3. Coupling-energy bound $\chi<21$ (§3) — independently checked numerically

With $T_0=2^{256}\approx1.16\times10^{77}$, $N=128000$, and the larger of the two certified $G$ values ($1.773\times10^{29}$, even-v): $1024NG/T_0\approx1024\times128000\times1.773\times10^{29}/1.16\times10^{77}\approx2\times10^{-40}$, utterly negligible against the near-block term of $400$. So $\chi^2\le400+2\times10^{-40}\approx400$, giving $\chi<21$ with enormous margin — confirmed independently by direct order-of-magnitude computation, not merely accepted from the entry's own claim.

## 4. Trace-aware finite-lift energy bound (§6) — independently re-derived

With $W_s^*s=W_c^*s-F_g^*C^{-1}Qs$ (direct consequence of $W_s=W_c-C^{-1}F_g$ and self-adjointness of $C$ on $Q$) and $W_c=\tilde Wc R_{tr}$: $\|W_c^*s\|=\|R_{tr}^*\tilde W^*s\|\le\|R_{tr}\|\cdot\|\tilde W^*s\|\le d_s/(1-\rho)$, and $\|F_g^*C^{-1}Qs\|\le f\|Qs\|/\gamma\le fq_s/\gamma$, giving $\|W_s^*s\|\le d_s/(1-\rho)+fq_s/\gamma$ by the triangle inequality. Then $E_z=\langle s,A^{-1}s\rangle=\langle Qs,C^{-1}Qs\rangle+\langle W_s^*s,H^{-1}W_s^*s\rangle\le q_s^2/\gamma+\|W_s^*s\|^2/h$, reproducing the entry's stated bound exactly. Confirmed independently, term for term.

## 5. Full numerical budget — independently reproduced byte-for-byte

Ran the committed, unmodified `research-notes/suzuki_whole_remote_schur_model_budget.py --terms 42` fresh against the pinned certificates in the frozen archive `payloads/exact_remote_leading_run_37965642729/` (independently reconstructed and hash-verified in Round 209). Output matches `payloads/whole_remote_schur_model_v14_210/whole-remote-schur-model-budget.json` **byte-for-byte** (identical SHA-256 `f87966e6...a9a03515`, 31056 bytes), and two successive runs are byte-identical to each other. Every table value in v14.210 §§2–6 is confirmed exactly from this fresh run: $G\le1.773\times10^{29}$/$7.040\times10^{25}$; $\epsilon_{42}\le6.157\times10^{-9}$/$1.227\times10^{-10}$; combined geometric+M11 error $\le3.454\times10^{-8}$/$1.334\times10^{-10}$; total action error $\le8.750\times10^{-11}$/$4.894\times10^{-11}$; stationary error $\le4.875\times10^{-13}$/$4.490\times10^{-13}$. The script's own internal assertions (`chi<21`, `epsilon<1e-8`, `combined<1`, `action<1e-10`, `total_action<1e-10`, `stationary<5e-12`, `energy_target<2e-24`, `j>a` both sectors) all held, since the run completed without raising. The script also pins both certificate SHA-256 values and checks `cutoff==256000`, `remote_start==0`, and all six `checks_exact` flags before computing anything — correctly refusing to run against unaudited or mismatched input.

## 6. Scope and flags — correctly stated

Confirmed directly from the fresh output: `higher_channel_and_near_cross_arithmetic_certified: false`, `finite_lift_targets_achieved: false`, `infinite_remote_trial_constructed: false`, `infinite_capacity_tail_closed: false`. The entry correctly states these are sufficient *targets* for a new trial-dependent finite lift, not an achieved certificate, and that the cached-$M_{11}$ charge is optional and applies only to the Far-Far block, leaving Near and mixed blocks untouched. v14.209's display-rounding note is correctly incorporated — the entry and script use only `_rational`/exact-`Fraction` fields throughout, never a `display_approximate` string as a bound.

## 7. Verdict

```
Full finite-inverse decomposition (A-conjugate Q/graph-block split, no
  orthonormality assumption): INDEPENDENTLY RE-DERIVED, confirmed exact.
Near/Far channel-remainder identity B-B_K=E_K: INDEPENDENTLY RE-DERIVED
  from the elementary finite geometric series, term by term, including
  correctly tracing where the k=0 second-series term and the pole's
  leading term combine into the w_1(m) channel. Confirmed exact; no
  untracked O-term. Entrywise bound (20/n)(R/n)^(2K): confirmed exact.
chi<21: INDEPENDENTLY CHECKED by direct order-of-magnitude computation
  (far term ~2e-40, utterly negligible against the near term's 400).
Trace-aware finite-lift energy bound: INDEPENDENTLY RE-DERIVED, confirmed
  exact, term for term.
Full numerical budget (G, epsilon_42, combined error, action/stationary
  totals, both sectors): INDEPENDENTLY REPRODUCED byte-for-byte via a
  fresh, unmodified script run against the pinned frozen certificates.
All scope flags (targets not achieved, no infinite trial, no closure)
  confirmed false as stated. v14.209's display-rounding note correctly
  incorporated throughout.
No correction found. No infinite-tail theorem is claimed or promoted.
No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.212
status: open
action: v14.210's whole-remote Schur channel model and finite-lift contract are independently re-confirmed from scratch: the full-inverse decomposition, the exact channel-remainder identity (reconstructed term by term from the elementary geometric series, not merely read), the entrywise and HS remainder bounds, the chi<21 coupling bound, and the trace-aware lift energy bound all check out, and the complete numerical budget reproduces byte-for-byte from a fresh script run against the pinned certificates. No correction found. The next gate (per v14.210 §8) remains Lane A's: construct a source-faithful infinite trial with explicit Near/Far channel data, evaluate it against the finite-lift residual contract, and certify the remaining remote scalar/action arithmetic.
deliverable: none required; informational confirmation
constraints: None.
