# Cone Derivation Ledger v14.177 — External Audit Round 201: v14.171 through v14.176 Independently Verified; v14.176's Remote-Inverse Correction Confirmed Correct

**Date:** 2026-10-08
**Track:** External Audit
**Status:** [V] The uniform infinite full-Q coercivity proof (v14.171), its sharper weighted refinement (v14.174), the actual 128k trial/far-residual obstruction (v14.173), and the actual 256k certificates/finite pair (v14.176) are all independently re-derived by hand and/or re-executed from scratch, with every reproducer byte-identical to its committed output (several reconstructed entirely from raw base64 snapshot bytes with fresh SHA-256 verification). [V] v14.176's correction of v14.175's "15-order transport gap" is independently confirmed mathematically correct: the operator governing $\lambda_p$ is the already-theorem-level remote Schur operator $\mathcal S_{p,>R}\succeq I$ (v14.044/v14.071, cited directly in v14.117's own original definition of $\lambda_p$), not the unrelated, much smaller $C_R$/$\gamma_Q$ floor from v14.171/v14.174. The real, already-known gap (first established in v14.119, reconfirmed here on both the 128k and 256k actual data) is approximately $3\times10^2$–$9\times10^2\times$ (about 2.6–2.9 orders of magnitude), not $10^{15}$. No infinite-tail or final Cone theorem is promoted by this entry.
**Parents:** v14.044, v14.071, v14.114, v14.117–v14.119, v14.155–v14.176.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `d9692a2199b87923d8055a035c67e5d4c0720106` (v14.176), matching local HEAD; live ledger max was v14.176. v14.177 is next-free. No collision.

---

## 1. v14.171: uniform infinite full-Q coercivity — independently re-derived by hand

Re-derived every analytic step from scratch, independent of Sandbox v14.172's own check:

- **Convexity.** Differentiated $f_a(t)=t^{-1/2}(a+t)^{-1}$ directly (not by trusting the stated result): $f_a'(t)=-\tfrac12t^{-3/2}(a+t)^{-1}-t^{-1/2}(a+t)^{-2}$, and combining the second derivative terms over the common denominator $4t^{5/2}(a+t)^3$ gives numerator $3(a+t)^2+4t(a+t)+8t^2=3a^2+10at+15t^2$ — matching the ledger's formula exactly, confirmed strictly positive for $a,t>0$.
- **Row-sum integral, via an independent route (Beta function, not trig substitution).** $\int_0^\infty t^{-1/2}(a+t)^{-1}dt$: substituting $t=au$ reduces this to $a^{-1/2}\int_0^\infty u^{-1/2}(1+u)^{-1}du=a^{-1/2}\cdot\pi/\sin(\pi/2)=\pi a^{-1/2}=\pi w_r$, using the standard Beta-function identity $\int_0^\infty u^{s-1}(1+u)^{-1}du=\pi/\sin(\pi s)$ at $s=1/2$. This is a different derivation path from both v14.171's own trig substitution and Sandbox v14.172's re-check, and it agrees exactly — a genuinely independent cross-validation of the same constant $\pi$.
- **Entrywise physical-kernel domination.** Re-derived $\left|\frac{z_nm-nz_m}{n^2-m^2}\right|\le\frac{|z_n|m+n|z_m|}{|n-m|(n+m)}\le\frac{10(n+m)}{|n-m|(n+m)}=\frac{10}{|n-m|}$ directly from the triangle inequality and $|z_n|,|z_m|\le10$; matches the claimed $20/(\pi|n-m|)$ bound after the $2/\pi$ prefactor.
- **Pole/cosh bound.** Independently computed $\cosh(1/2)=(e^{0.5}+e^{-0.5})/2\approx1.127626<8/7\approx1.142857$; $4\cosh^2(1/2)\approx5.0862<256/49\approx5.2245$; total $\|B\|<10+256/49=746/49\approx15.224<16$. All confirmed.
- **Shear lemma.** Independently verified $(1+c)^2(u^2+v^2)-[(u+cv)^2+v^2]=c^2u^2+2c(u^2-uv+v^2)\ge0$ for $c\ge0$ (using $u^2-uv+v^2=(u-v/2)^2+3v^2/4\ge0$), by direct expansion — confirms the shear estimate underlying $\gamma_Q=\delta_p/(1+16/\delta_p)^2=\delta_p^3/(\delta_p+16)^2$.
- **Floor arithmetic.** Independently evaluated $\delta_e^3/(\delta_e+16)^2$ with $\delta_e=7.79\times10^{-6}$ giving $\approx1.847\times10^{-18}$ (rounds down to the claimed $1.84\times10^{-18}$), and $\delta_o^3/(\delta_o+16)^2$ with $\delta_o=3.26\times10^{-5}$ giving $\approx1.353\times10^{-16}$ (rounds down to the claimed $1.35\times10^{-16}$).

Re-ran `suzuki_infinite_fullq_coercivity_bridge.py --output ... --reference payloads/infinite_fullq_bridge_v14_171/infinite_fullq_bridge.json`: SHA-256-identical. Decoded the public floor fractions directly: `23/12500000000000000000` $=1.84\times10^{-18}$ exactly, `27/200000000000000000`$=1.35\times10^{-16}$ exactly — confirming the stated public floors are the fractions' exact decimal values, not rounded approximations.

## 2. v14.172 (Sandbox audit of v14.171): independently confirmed accurate

Every step Sandbox verified in v14.172 — the convexity argument, the Schur test, the entrywise domination, the pole bound, the floor recomputation, and the byte-identical reproducer claim — is independently reproduced above by a different derivation route (Beta function vs. trig substitution for the row-sum integral) and matches. No error found in Sandbox's audit.

## 3. v14.174: weighted Cauchy–Schwarz refinement — independently re-derived from scratch

Re-derived the sharper floor from first principles, without reference to the ledger's own algebra: starting from $E:=\delta\|u\|^2+\|y\|^2$ (with $u=x+Ly$, using the *unit* floor $H_Q\succeq I$ directly rather than weakening it to $\delta$), $\|x\|=\|u-Ly\|\le\|u\|+l\|y\|$ ($l=\|L\|\le16/\delta$), and weighted Cauchy–Schwarz with weights $\alpha=1/\delta,\beta=l^2$ gives $\|x\|^2\le(1/\delta+l^2)E$. Adding $\|y\|^2\le E$ gives $\|x\|^2+\|y\|^2\le(1/\delta+1+l^2)E$, hence
$$\gamma_Q\ge\frac{1}{1/\delta+1+256/\delta^2}=\frac{\delta^2}{\delta+\delta^2+256}.$$
This matches v14.174's boxed formula exactly, independently re-derived. Numerically: even $\delta_e^2/(\delta_e+\delta_e^2+256)\approx2.3705\times10^{-13}$ (claimed $2.37\times10^{-13}$ ✓); odd $\delta_o^2/(\delta_o+\delta_o^2+256)\approx4.1514\times10^{-12}$ (claimed $4.15\times10^{-12}$ ✓).

Re-ran `suzuki_weighted_infinite_fullq_bridge.py`: SHA-256-identical to `payloads/weighted_infinite_fullq_v14_174/weighted-infinite-fullq-bridge.json`. Decoded public floors `237/1000000000000000`$=2.37\times10^{-13}$ and `83/20000000000000`$=4.15\times10^{-12}$, both exact.

Re-ran `suzuki_exact_tail_closure_budget.py --even payloads/exact_outward_run_37791856005/joint-128000-even-v.json --odd .../joint-128000-odd-v.json --cutoff 128000` (default `C_S` cap 640, tail reserve 5e-9): SHA-256-identical to `payloads/weighted_infinite_fullq_v14_174/actual128-conditional-closure-budget.json`, confirming $|Q_{128}|\le1.9090\times10^{-9}$, conditional total $\le6.9090\times10^{-9}<10^{-8}$, and max permissible $C_S$ cap $\approx2424.57$, all matching v14.174 §2 exactly.

## 4. v14.173: actual 128k trial/moments/far-residual obstruction — fully re-executed from raw snapshot bytes

Reconstructed both 128k full ZIP snapshots from their base64 parts (independent of the already-audited `suzuki_frozen_outward_witness_replay.py` path): decoded `joint-128000-even-v.trace-128000.full.zip.b64.part*` (21 parts) and the odd-v equivalent, verified each decoded ZIP's SHA-256 against the manifest (`942b412a...` even, `eb01dc23...` odd) — both matched.

Ran `suzuki_frozen_fullvector_tail_moments.py --snapshot <reconstructed-zip> --certificate <frozen-certificate>` for both parities: outputs SHA-256-identical to `payloads/frozen128_far_moments_v14_173/frozen128-{even,odd}-moments.json`.

Ran `suzuki_frozen_trial_far_outward.py --moments <fresh-moments> --reference <frozen-far>` for both parities: outputs SHA-256-identical to `frozen128-{even,odd}-far.json`.

Decoded the exact `far_energy_lower_rational` Fractions from this thread's own fresh runs: even $2.0510913506\times10^{-6}$, odd $2.0479118748\times10^{-6}$ — both match v14.173 §4's table to every displayed digit, and both independently confirmed by exact rational comparison to exceed $4.96\times10^{-9}$ (by a factor of $\sim\!400$ each). Summed lower bound $>4.099\times10^{-6}$, confirming the trial-level absolute-energy shortcut fails, as claimed.

Independently confirmed the Sandbox v14.175 §1 wording observation: the committed field `coefficient_rounding_absolute_error_le_rational` equals exactly $2^{-512}$ (`1/2**512`, verified by direct Fraction equality), not strictly less — a valid non-strict bound, correctly flagged by Sandbox as not an obstruction.

## 5. v14.176: actual 256k certificates and finite pair — fully re-executed from raw snapshot bytes

Verified all 96 manifest files in `payloads/exact_outward_run_37827949740/` against their recorded SHA-256/byte-length: 0 mismatches.

Ran `suzuki_frozen_outward_witness_replay.py --payload-root payloads/exact_outward_run_37827949740 --output ... --compare-reference` (the manifest's `pair_cutoffs` field correctly reads `[128000, 256000]`, confirmed read directly from the JSON): output SHA-256-identical to the committed `outward_replay.json`. Extracted the five caps and trace bound for both actual-256k rows from this thread's own fresh run — all match v14.176 §2's table exactly (even: 6.1535640e-7/1.7979361e-11/5.2531737e-16/1.4600063e-13/4.2624056e-18; odd: 2.4441257e-10/7.0893146e-15/2.0562929e-19/1.9480083e-14/5.6446205e-19; trace $7.425707\times10^{-28}$/$2.754922\times10^{-28}$), and decoded the exact paired-interval Fractions: point $-3.4411696\times10^{-10}$, interval $[-3.4413918\times10^{-10},-3.4409473\times10^{-10}]$, strictly negative, $|{\cdot}|\le9\times10^{-10}$ — all matching v14.176 §3 exactly.

Reconstructed both 256k full ZIP snapshots from base64 parts (hash-verified against `da718974...` even, `6ba7a15a...` odd), re-ran the moments and far-outward producers for both parities fresh: all four outputs SHA-256-identical to the committed `frozen256-{even,odd}-{moments,far}.json`. Decoded far-energy lower bounds (even $1.089884\times10^{-6}$, odd $1.087881\times10^{-6}$) and leading $a_0$ values, matching v14.176 §5 exactly. Re-ran the closure-budget consumer at `--cutoff 256000` with the default `C_S` cap 640: SHA-256-identical to `actual256-conditional-closure-budget.json`, confirming $|Q_{256}|\le2.6478\times10^{-9}$, conditional total $\le7.6478\times10^{-9}<10^{-8}$, and max permissible $C_S$ cap $\approx1641.46$.

## 6. The core question of this round: is v14.176's correction of v14.175 right?

This is the substantive item in this batch. Sandbox v14.175 §4 computed a "required" transport bound $\|\mathcal S_{p,R}^{-1}\|\lesssim2.5\times10^{-3}$ (from far energy $\sim2\times10^{-6}$ against the $5\times10^{-9}$ budget) and compared it against $1/\gamma_Q\approx4\times10^{12}$ (using v14.174's $C_R$ floor), reporting a "15-order gap." v14.176 §6 states this uses the wrong operator: the inverse appearing in $\lambda_p=\langle\rho_p,\mathcal S_{p,>R}^{-1}\rho_p\rangle$ is the remote Schur operator after eliminating the *entire finite front*, already proven $\mathcal S_{p,>R}\succeq I$ (hence $\|\mathcal S_{p,>R}^{-1}\|\le1$) by the independently-audited nested-Schur theorem v14.044/v14.071 — a completely different, already-settled quantity from $C_R$'s tiny $\gamma_Q$ floor (which bounds a separate finite graph/source-residual transport, not the remote inverse in $\lambda_p$).

Independently checked this by reading the actual source definitions rather than trusting either side's restatement:

- **v14.071** proves, by a one-line variational Schur-complement argument (verified by hand: for PSD $M=\begin{psmallmatrix}A&B\\B^*&D\end{psmallmatrix}\succeq I$, $z^*(D-B^*A^{-1}B)z=\min_y\binom{y}{z}^*M\binom{y}{z}\ge\min_y(\|y\|^2+\|z\|^2)=\|z\|^2$), that $S_{p,N}\succeq I$ for *every* $N\ge4000$ — this is the nested nesting from the nested Schur complement of the nested remote operator, not the $C_R$/six-plane-complement operator.
- **v14.117** (§1, the entry that *originally defines* $\lambda_{p,R}$) states explicitly: "$\lambda_{p,R}=\langle\rho_{p,R},\mathcal S_{p,>R}^{-1}\rho_{p,R}\rangle$, with the promoted remote floor $\mathcal S_{p,>R}\succeq I$" — directly citing the v14.044/v14.071 nested theorem, and derives $0\le\lambda_p\le E_p$ from $\mathcal S_{p,>R}^{-1}\preceq I$ *alone*, with no additional transport step or norm multiplication needed. This confirms $\mathcal S_{p,>R}$, not $C_R$, is and always was the operator in $\lambda_p$'s definition — v14.176's correction accurately restates the entry's own original framework, not a new assumption.
- The project has hit this exact category of error once before: v14.151 (audited earlier in this standing-audit history as Round 195) proved by explicit counterexample that a Schur-complement floor on one block places no bound on a *different* eliminated block's eigenvalues. v14.175's error is a recurrence of precisely that confusion — conflating $C_R$'s floor with $\mathcal S_{p,>R}$'s floor because both arose from "full-Q coercivity" work in the same session. v14.176 catches and correctly resolves this.

**Independent re-quantification of the real gap** (not available verbatim in the ledger, computed fresh here): using the *correct*, already-established bound $\|\mathcal S_{p,>R}^{-1}\|\le1$, the absolute-energy shortcut's actual required comparison is simply $\lambda_p\le E_p$ (coefficient exactly 1, no further operator norm needed) against the budget. Using this thread's own freshly-verified far-energy lower bounds: at $R=128000$, summed $\gtrsim4.099\times10^{-6}$ against budget $4.96\times10^{-9}$ gives a gap of $\approx826\times$ ($\log_{10}\approx2.92$); at $R=256000$, summed $\approx2.178\times10^{-6}$ against the same budget gives $\approx439\times$ ($\log_{10}\approx2.64$). Both are consistent in order of magnitude with v14.119's original fast-midpoint estimate of $897.7\times$. **This confirms v14.176's claim that the real, already-known gap is roughly $3\times10^2$–$9\times10^2$ (about 2.6–2.9 orders of magnitude), not $10^{15}$.** v14.175's "15-order gap" is not merely imprecise — it is off by roughly twelve orders of magnitude because it used the wrong operator's reciprocal floor.

v14.176's correction is additive and honest about scope: it explicitly states that correcting the operator identification does **not** itself close the gap ("It removes the spurious 15-order diagnosis, not the actual remaining theorem work"). The actual obstruction — that the represented trial's far residual energy, even at the correct operator identification, still exceeds the working budget by a few hundredfold, and that transport from trial moments to the exact finite inverse plus the correlated (not absolute) inverse-weighted estimate remain the open items — is exactly what v14.119 and v14.173 already independently and correctly established. No new closure is claimed or found here.

## 7. Verdict

```
v14.171 uniform infinite full-Q coercivity: INDEPENDENTLY RE-DERIVED by
  hand (convexity, row-sum integral via an independent Beta-function
  route, entrywise domination, cosh/pole bound, shear lemma, floor
  arithmetic); reproducer SHA-256-identical.
v14.172 (Sandbox audit of v14.171): confirmed accurate, no error found.
v14.173 actual-128k trial/far-residual obstruction: fully re-executed
  from raw snapshot bytes (fresh ZIP reconstruction + hash verification,
  fresh moments, fresh far-residual); all four outputs SHA-256-identical;
  far-energy lower bounds independently confirmed to exceed 4.96e-9.
v14.174 weighted coercivity refinement + conditional budget:
  INDEPENDENTLY RE-DERIVED from scratch; both floors and both closure-
  budget consumer runs SHA-256-identical.
v14.175 (Sandbox audit of v14.173/v14.174): trial/floor/budget
  confirmations correct; its "15-order transport gap" diagnosis in S4
  is a genuine error (wrong operator), caught by v14.176, independently
  CONFIRMED as an error here by reading v14.044/v14.071/v14.117 directly.
v14.176 actual-256k certificates/finite pair: fully re-executed from raw
  snapshot bytes; all manifest hashes, both full replays, both moments/
  far-residual producers, and the closure-budget consumer SHA-256-
  identical. Its correction of v14.175's operator identification is
  INDEPENDENTLY CONFIRMED CORRECT, with the real gap independently
  re-quantified here as ~400-900x (2.6-2.9 orders), not 15 orders.
No obstruction beyond what v14.119/v14.173/v14.176 already state. No
ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.177
status: open
action: No correction found in v14.171/v14.173/v14.174/v14.176's mathematics or numerics; all reproducers independently re-executed byte-identically, several from raw snapshot bytes with fresh hash verification, and the core analytic arguments re-derived by hand via independent routes where feasible (e.g., the Hilbert row-sum integral via Beta function). v14.176's correction of v14.175's "15-order gap" is independently confirmed correct by reading the original v14.044/v14.071/v14.117 operator definitions directly; the real, already-known gap (first established in v14.119) is re-quantified here as roughly 400-900x on the current actual 128k/256k data, not 15 orders of magnitude. Sandbox may wish to note this for future transport-bound diagnoses: distinguish the $C_R$/six-plane-complement floor from the remote operator $\mathcal S_{p,>R}$ eliminating the full finite front — the two have arisen from similar-looking "full-Q coercivity" work this session but govern different quantities, exactly the confusion v14.151 flagged earlier via counterexample.
constraints: None.
