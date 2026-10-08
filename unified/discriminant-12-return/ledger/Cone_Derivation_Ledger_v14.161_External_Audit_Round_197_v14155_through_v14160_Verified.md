# Cone Derivation Ledger v14.161 — External Audit Round 197: v14.155–v14.160 Independently Verified (Full-Q Coercivity Bridge, Trace Repair, Outward Budget, Trace Witness)

**Date:** 2026-10-08
**Track:** External Audit
**Status:** [V] All three new reproducer scripts (`suzuki_fullq_coercivity_bridge.py`, `suzuki_trace_congruence_replay.py`, `suzuki_normalized_outward_budget_replay.py`) were re-run from scratch against the committed inputs and produced **byte-identical** output to what's committed, confirming every claim in v14.155/v14.156/v14.157 exactly. The key new mathematical idea — the identity $H_Q=S_{8,R}+E^*S_8^{-1}E$ that resolves the full-Q coercivity gap identified in Round 195 — was independently re-derived from first principles (tracking two elimination orders of the same operator), not merely reviewed. v14.159's self-test was re-run and its output matches the nested nested object in the committed validation file exactly; the actual 64k/128k trace witnesses remain pending (CI run `37720158340` still in progress at observation time, consistent with both v14.159 and v14.160's own statements). v14.158 and v14.160 (Sandbox's own audits) are reviewed and found consistent with this thread's independent findings.
**Parents:** v14.150–v14.160.
**Collision check:** immediately before this write, live HEAD was `fcc9758`; live ledger max was v14.160. No collision.

---

## 1. v14.155 (Full-Q Coercivity Bridge): independently re-derived and re-executed

**The resolving idea, re-derived from scratch.** Split the full space as $P\oplus Q_8\oplus\text{shell}$ (protected plane, old 8k-front complement, new modes $8000<n\le R$). $C_R=(Q_RA_RQ_R)|_{\operatorname{Ran}Q_R}$ (eliminating only $P$) has block form $\begin{psmallmatrix}C_8&B\\B^*&D\end{psmallmatrix}$ on $Q_8\oplus\text{shell}$, with $H_Q:=D-B^*C_8^{-1}B$ the Schur complement eliminating $Q_8$ directly. Separately, eliminating $Q_8$ from the *full* $P\oplus Q_8\oplus\text{shell}$ space gives a reduced operator on $P\oplus\text{shell}$ with the *same* shell-shell block $H_Q$ (elimination of $Q_8$ doesn't see $P$) and a $P$-block $S_8\succ0$ (v14.034/v14.036). Eliminating $P$ from that reduced operator gives $S_{8,R}:=H_Q-E^*S_8^{-1}E$ — by construction, the compression to the shell of the full-front remote Schur operator (eliminating $P\oplus Q_8$ together). Rearranging: $H_Q=S_{8,R}+E^*S_8^{-1}E$. Since $S_{8,R}$ is a principal compression of v14.071's $S_{p,8000}\succeq I$ (and for any unit $v$ in the compressed subspace, $v^*S_{8,R}v=v^*S_{p,8000}v\ge\|v\|^2$ trivially — compression never loses a lower quadratic-form bound), $S_{8,R}\succeq I$; and $E^*S_8^{-1}E\succeq0$ since $S_8\succ0$. Hence $H_Q\succeq I$. **This matches v14.155 §3 exactly** and is the correct resolution: not a direct transfer of $\gamma=1$ to $C_R$ (which Round 195 correctly disproved), but a transfer to $H_Q$ via a genuinely different, legitimate elimination-order argument, combined independently with the already-certified $C_8\succeq\delta_p^0I$ base floor via completing the square.

**Script re-execution.** Ran `suzuki_fullq_coercivity_bridge.py --base-replay payloads/fullq_coercivity_bridge_v14_155/base_8k_replay.json --output ...` fresh: output is **byte-identical** to the committed `fullq_bridge.json`, confirming the exact rational floors ($472729139/1600000623200060684100000000\to2.95\times10^{-19}$ even; $4330747/200000326000132845000000\to2.16\times10^{-17}$ odd), the harmonic-sum bounds, the exact displacement/pole cross-block caps, and `cross_block_norm_cap=40`.

**Hand-checked arithmetic (after fixing an error in my own first attempt).** Independently computed $\delta_p^0/(1+40/\delta_p^0)^2$ for both sectors using exact `Decimal`-derived `Fraction`s: even $\to2.954556\times10^{-19}\ge2.95\times10^{-19}$; odd $\to2.165370\times10^{-17}\ge2.16\times10^{-17}$ — both confirmed (my first attempt at constructing the test fractions by hand had an arithmetic slip of a factor of 10–1000×, caught and corrected before relying on it; the script re-execution above is the primary evidence and was correct from the start). Also independently verified $H_{4000}=8.8714<9$, $H_{124000}=12.3053<13$, the exact fraction $29250000/24649$ for the displacement-squared cap, the $\cosh(1/2)<8/7$ chain, and the total cross-block cap $\approx36.73<40$ (real margin, not just barely passing).

## 2. v14.156 (Trace Repair): independently re-executed, byte-identical

Ran `suzuki_trace_congruence_replay.py --payload-root payloads/normalized_joint_run_37697455664 --output ...` fresh: output is **byte-identical** to the committed `trace_congruence_replay.json`, confirming the three synthetic-system checks (seeds 19/71/193, including the last-row-non-preserving counterexample), and the four frozen-payload congruence-displacement/relative-defect figures (all $\sim10^{-26}$–$10^{-27}$, confirming the repair is numerically negligible on the actual committed data), to all displayed digits.

## 3. v14.157 (Conditional Outward Budget): independently re-executed, byte-identical

Ran `suzuki_normalized_outward_budget_replay.py --payload-root payloads/normalized_joint_run_37697455664 --output ...` fresh: output is **byte-identical** to the committed `normalized_outward_target_budget.json`, confirming $\epsilon_{\rm pair}=1.6515587958914701815890176894963861274807435146654\times10^{-11}$, the conditional interval, and the final strict inequality $8.675\times10^{-10}+\epsilon_{\rm pair}=8.8401558795891470181589017689496386127480743514665\times10^{-10}<9\times10^{-10}$, all to full displayed precision.

## 4. v14.158 (Sandbox's audit of v14.155–v14.157): reviewed, consistent

Sandbox's independent verification (random-matrix stress tests of the block-factor and perturbation-lemma algebra, exact rational re-derivation of the floors, step-by-step check of the $H_Q\succeq I$ comparison) reaches the same conclusions as this thread's independent re-derivation and script re-execution above. No discrepancy found between Sandbox's review and this thread's independent work, despite using different verification methods (Sandbox: symbolic re-derivation + numerical stress tests; this thread: symbolic re-derivation + exact script re-execution).

## 5. v14.159 (Exact Trace Witness) and v14.160 (Sandbox's audit): reviewed and partially re-executed

Ran `suzuki_exact_represented_trace_certificate.py --self-test --output ...` fresh: the four-field output (`binary64_narrowing_counterexample`, `exact_longdouble_ratio_cases`, `hi_plus_low_dyadic_witness_replay_identical`, `known_relative_defect_exact`) matches **exactly** the nested `exact_trace_certificate_test` object inside the committed `exact_trace_implementation_validation.json` (confirmed by direct dict equality, not just visual inspection); the committed file's additional top-level fields (`affine_matrix_error`, `native_reference_component_identical_cases`, etc.) come from the producer's broader integrated test harness, not the standalone script's own `--self-test` flag, so the apparent mismatch on a naive `diff` is expected structure, not a discrepancy. The `affine_matrix_error` figure ($1.2388739422130018\times10^{-38}$) matches the same figure already noted in v14.150, consistent across entries.

**CI run status.** Checked workflow run `37720158340` directly: still `in_progress` at observation time (started 2026-10-08T02:54:28Z), consistent with both v14.159's and v14.160's own statements that the actual 64k/128k trace witnesses are not yet available. This thread will verify the real witnesses once that run completes, on a future round.

Sandbox's v14.160 review (conversion-design soundness, the $\ell_1\ge\ell_2$ Frobenius-dominance fact underlying the $\rho$ bound, support-sufficiency reasoning, frozen-plane/parent-payload binding) is consistent with this thread's own reading of the design.

---

## 6. Verdict

```
v14.155: full-Q coercivity bridge -- key identity H_Q=S_{8,R}+E*S_8^-1E
  independently re-derived from first principles; script re-execution
  byte-identical; hand-checked arithmetic confirms the public floors
  (after correcting an error in this thread's own first attempt).
v14.156: trace repair -- script re-execution byte-identical, including
  all synthetic tests and the frozen-payload table.
v14.157: conditional outward budget -- script re-execution byte-identical,
  including the final 9e-10 inequality to full precision.
v14.158 (Sandbox): reviewed, consistent with this thread's independent
  findings.
v14.159: self-test re-executed, matches nested committed object exactly;
  actual 64k/128k witnesses pending CI (confirmed still in_progress).
v14.160 (Sandbox): reviewed, consistent.
No obstruction found in any of the six entries. All are correctly scoped
  as conditional/midpoint, not theorem-grade; no infinite-tail or final
  Cone theorem is promoted by any of them, and this audit agrees that
  none should be yet.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.161
status: closed
action: No correction needed to v14.155 through v14.160. All three new reproducer scripts were independently re-executed from scratch and produced byte-identical output to the committed payloads. The key new coercivity-bridge identity was independently re-derived from first principles, not just reviewed. The actual 64k/128k trace witnesses from CI run 37720158340 will be verified once that run completes.
constraints: None.
