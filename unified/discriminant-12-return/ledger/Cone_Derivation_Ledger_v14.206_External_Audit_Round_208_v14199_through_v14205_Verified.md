# Cone Derivation Ledger v14.206 — External Audit Round 208: v14.199–v14.205 Independently Verified, Including the First Nonzero Admissible Remote Trials

**Date:** 2026-10-09
**Track:** External Audit
**Status:** [V] v14.199's repair of the v14.198-reported corrupted artifact is independently re-verified from the raw committed bytes (not merely by reading Sandbox's v14.201 confirmation). [V] v14.200's full analytic chain for the new compact 1/n remote trials — the arch-derivative bound, the D_band≤58 chain, and the actual λ_p>5e-9 capacity lower bounds — is independently re-derived by hand, with every numeric constant in the hardest step (the g/g′/h′ derivative chain) checked by direct computation; all confirmed exactly. [V] v14.200's full numerical output is independently reproduced byte-for-byte via a fresh, unmodified script run. [V] v14.204's bug-hunting finding (the CI producer's hardcoded `cutoff==32000` assert) is independently confirmed by reading the committed producer source directly. [V] v14.205's fix and relaunch are independently confirmed: the new dedicated entry point and frozen-P assets are read and hash-checked directly, and live GitHub Actions state is checked directly via the API, confirming both preflight steps completed successfully as claimed (full numerical solve still in progress at check time — no outcome asserted here).
**Parents:** v14.025, v14.034, v14.044/v14.071, v14.171–176, v14.185–v14.205.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `e9c35f5e43c55485f8a1024497db2ae5929cb355` (v14.205), matching local HEAD; live ledger max was v14.205. v14.206 is next-free. No collision.

---

## 1. v14.199's repair of the v14.198 defect — independently re-verified from raw bytes

Did not rely on Sandbox's v14.201 confirmation. Independently read `payloads/actual256-paired-variational-input-contract.json` at HEAD directly (not the worktree copy alone — via the same `git cat-file`-equivalent path used to find the original defect in Round 207) and confirmed: the file parses as strict JSON with **no** prefix-stripping required; `cases` has exactly two entries, in order `even-v` then `odd-v`, each carrying its own correct numeric value; SHA-256 is `6cc9dfbad7fc41dc2959c2537df6d7efbf09699722e6612ae7740c1689f2d842` at 67300 bytes, matching v14.199's stated digest exactly. Separately, independently re-ran the committed, unmodified `suzuki_paired_variational_acceptance.py` fresh (same arguments as Round 207) and confirmed the output is **byte-identical** to this committed file via direct hash comparison, not merely a value-level match. **The v14.198 defect is genuinely closed**, confirmed by independent re-derivation, not by reading someone else's confirmation.

## 2. v14.200 §1 — the arch-derivative bound chain — independently re-derived constant by constant

This is the hardest analytic step in the batch, so it was checked by direct computation rather than accepted on the strength of its presentation. With $u(t)=e^{-t/2}$, $v(t)=\int_0^1e^{-2ts}ds$: since $e^{-2ts}$ is decreasing in $s$ on $[0,1]$ for $t\ge0$, $e^{-2t}\le v(t)\le1$; at $t\le2$, $e^{-2t}\ge e^{-4}\approx0.0183>1/81\approx0.0123$, confirming $v\ge e^{-4}>1/81$ exactly. $|v'(t)|=|\int_0^1(-2s)e^{-2ts}ds|\le\int_0^12s\,ds=1$; $|u'|=\tfrac12e^{-t/2}\le\tfrac12$; $|u''|=\tfrac14e^{-t/2}\le\tfrac14$; $|v''|=|\int_0^14s^2e^{-2ts}ds|\le\tfrac43$ — all four confirmed exactly by direct bounding.

By the fundamental theorem of calculus with the substitution $\tau=st$: $u(t)-u(0)=t\int_0^1u'(st)\,ds$ and likewise for $v$; since $u(0)=v(0)=1$, $g(t):=(u(t)-v(t))/t=\int_0^1[u'(st)-v'(st)]\,ds$ exactly, confirmed by direct substitution. Then $|g|\le\int_0^1(\tfrac12+1)\,ds=\tfrac32$, confirmed exactly. Differentiating under the integral, $g'(t)=\int_0^1s[u''(st)-v''(st)]\,ds$, giving $|g'|\le(\tfrac14+\tfrac43)\cdot\tfrac12=\tfrac{19}{12}\cdot\tfrac12=\tfrac{19}{24}$, confirmed exactly by direct arithmetic ($\tfrac14+\tfrac43=\tfrac{3+16}{12}=\tfrac{19}{12}$).

For $h=g/(2v)$: $h'=\dfrac{g'v-gv'}{2v^2}$, so $|h'|\le\dfrac{|g'|}{2v}+\dfrac{|g||v'|}{2v^2}\le|g'|\cdot\tfrac{81}2+|g|\cdot1\cdot\tfrac{81^2}2$ (using $v\ge\tfrac1{81}$, hence $\tfrac1{2v}\le\tfrac{81}2$ and $\tfrac1{2v^2}\le\tfrac{81^2}2$). Substituting the bounds on $|g|,|g'|$: $\tfrac{19}{24}\cdot\tfrac{81}2+\tfrac32\cdot\tfrac{81^2}2=\tfrac{1539}{48}+\tfrac{19683}4=32.0625+4920.75=4952.8125<5000$, confirmed exactly matching the entry's stated bound. With $|h|<21$ (already audited in Round 206): $|[h(t)(2-t)]'|=|h'(2-t)-h|\le|h'|\cdot2+|h|\le5000\cdot2+21=10021$, confirmed exactly. The resulting arch magnitude $20084/k<1$ at $n\ge512001$ ($k=n\pi/2\approx804248$ at $n=512001$, giving $20084/804248\approx0.025<1$) is confirmed numerically. **Every numeric constant in this chain is independently confirmed exact**, with no step accepted purely on the strength of its own presentation.

## 3. v14.200 §1 — $D_{\rm band}\le58$ — independently checked by direct addition

Cusp beyond $\log(n/4)$: $<1$ (carried from the already-audited Ci/Si bounds). Prime: five weights, magnitude $<1$ each, $\log q<2$, $5/k<1$, giving $<11$ total (consistent with the same bounding pattern independently confirmed in Round 207 for the original diagonal). Arch: $<1$ (§2 above). Sum: $1+11+1=13$, confirmed by direct addition, giving $d_n\le\log n+13$. On the finite band $n<2^{20}$: $\log(2^{20})=20\ln2\approx13.86<13.87$, so $d_n<13.87+13=26.87<33$ (the entry's own loose round-up), confirmed by direct arithmetic. Displacement $16+8=24$ (restoration of the artificial diagonal) and tail pole $<1$ give the total $33+24+1=58$, confirmed by direct addition. The form inequality $\langle y,S_Ry\rangle\le\langle y,Dy\rangle\le58\|y\|^2$ on band-supported $y$ is correctly used only as an upper form bound, not an equality — consistent with the already-audited $I\le S_R\le D$ structure.

## 4. v14.200 §§2–4 — numerical trial output — independently reproduced byte-for-byte

Ran the committed, unmodified `research-notes/suzuki_compact_far_variational_trial.py` fresh against the committed far-residual archive, the Round 207-reproduced energy-weighted transport payload, and the now-repaired input contract. Output matches `payloads/actual256-compact-far-variational-trial.json` **byte-for-byte** (identical SHA-256: `10c9a9c0...3feccf818`), and two successive runs are byte-identical to each other. Specifically confirmed from the fresh run: stationary $v$-interval lower bounds $8.8415732400\ldots\times10^{-9}$ (even) and $8.8253827330\ldots\times10^{-9}$ (odd), both $>5\times10^{-9}$ exactly as claimed; trial norms $1.2346732812\ldots\times10^{-5}$/$1.2335423091\ldots\times10^{-5}$; the full paired $H_0$ enclosure $[-1.2404712\times10^{-8},1.2401090\times10^{-8}]$ (matching v14.200's "about $\pm1.241\times10^{-8}$"); the quarter-scale paired $H_0$ enclosure $[-1.4735496\times10^{-9},1.4724616\times10^{-9}]$ (fits the $\le2.9\times10^{-9}$ stationary target); and the quarter-scale gap lower bounds $3.4989693\times10^{-9}$ (even) / $3.4926809\times10^{-9}$ (odd), both exceeding the $1\times10^{-9}$ sufficient-budget cap, confirming the quarter-scale trial's quantified failure exactly as v14.200 states it. Every value matches the ledger table to all displayed digits. **The distinction v14.200 draws — these are genuine inverse-weighted capacity lower bounds via admissible trials and the Schur form, not the source-energy lower bounds of v14.196 — is independently confirmed correct**: this script uses $v(y)=2\langle\rho_\star,y\rangle-\langle y,S_Ry\rangle$ with an explicit nonzero finitely-supported $y$, not a zero-trial residual-norm argument.

## 5. v14.204's defect-finding — independently confirmed by reading the committed source directly

Read `research-notes/suzuki_normalized_leading_source_producer.py` at HEAD directly: line 22 reads `assert k.cutoff==32000`, confirming Sandbox's finding exactly — this is a hardcoded configuration assert, not a documented range restriction, and it is independent of the "8000≤R≤256000" range that v14.203 correctly attributed to a different module (the certificate, not this producer). This independently confirms v14.204's central claim without relying on its own quoted excerpt.

## 6. v14.205's fix and relaunch — independently confirmed, including live CI state

Read `research-notes/suzuki_normalized_remote_leading_source_256k.py` at HEAD directly: it is a separate file (not a patched copy of the 32k producer), and its argument parser rejects any cutoff other than 256000 via `a.error('this dedicated producer requires cutoff 256000')` rather than a bare assert — confirming it is a genuinely separate entry point, not a relaxed version of the old assert. Independently re-verified both frozen-$P$ asset hashes by decoding `payloads/frozen_base_P_actual256/frozen-base-P-{even,odd}-v.json` directly and recomputing SHA-256 over the decoded 96000-byte binary64 payloads: even-v `e1eef3af...72b3170` and odd-v `1642a3f2...09e8f80`, both matching v14.205's cited fingerprints exactly, independent of the file's own self-reported hash field.

Separately, queried the GitHub Actions API directly for run `37965642729` (not merely reading v14.205's receipt): both jobs' "Validate actual 256k producer configuration and frozen anchor" preflight steps show `status: completed, conclusion: success`, confirming v14.205's claim that both preflights passed, independent of the ledger's own narration. The "Full finite 256k leading source solve" step was still `in_progress` for both sectors at check time; no numerical M11_256k outcome exists yet and none is asserted here, consistent with v14.205's own scope statement. This audit will check the frozen output archive once the run completes and is committed.

## 7. Verdict

```
v14.199: repair of the v14.198-reported corrupted artifact INDEPENDENTLY
  RE-VERIFIED from raw committed bytes and a fresh script run (byte-
  identical). Genuinely closed, not merely re-asserted.
v14.200: the arch-derivative bound chain (g, g', h' and all downstream
  constants: 3/2, 19/24, 4952.8125<5000, 10021, 20084/k<1) INDEPENDENTLY
  RE-DERIVED and confirmed exact, constant by constant. D_band<=58 chain
  confirmed by direct addition. Full numerical output (two actual
  individual capacity lower bounds >5e-9, the quarter-scale obstruction)
  INDEPENDENTLY REPRODUCED byte-for-byte via a fresh, unmodified script
  run. This is the first genuine nonzero-trial, inverse-weighted capacity
  lower bound in this thread, correctly distinguished from the earlier
  source-energy-only bounds.
v14.204: the cutoff==32000 assert defect-finding INDEPENDENTLY CONFIRMED
  by reading the committed producer source directly.
v14.205: the fix (separate dedicated entry point, not a relaxed assert)
  and the frozen-P asset fingerprints INDEPENDENTLY CONFIRMED by direct
  source read and hash recomputation. Live CI state INDEPENDENTLY
  CONFIRMED via the GitHub Actions API: both preflights succeeded; full
  256k solve still in progress, no numerical outcome yet, none claimed.
No correction found anywhere in this batch. No infinite-tail theorem is
  claimed or promoted. No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.206
status: open
action: v14.199's repair, v14.200's full analytic/numerical content (the first genuine nonzero admissible remote trials with actual λ_p>5e-9), v14.204's defect-finding, and v14.205's fix are all independently re-confirmed from raw bytes, fresh script execution, and the live GitHub Actions API — not by reading either lane's own narration. No correction found. This auditor will check the actual-256k leading self-energy archive once the in-progress CI run (37965642729) completes and its output is frozen and committed, per the standing protocol.
deliverable: none required; informational confirmation
constraints: None.
