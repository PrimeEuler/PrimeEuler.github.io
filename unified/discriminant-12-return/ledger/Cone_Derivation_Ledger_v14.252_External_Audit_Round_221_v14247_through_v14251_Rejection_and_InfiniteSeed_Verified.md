# Cone Derivation Ledger v14.252 — External Audit Round 221: Composition Fix Confirmed; Near-Only Trial's Rejection and the Infinite Diagonal Seed Independently Reproduced

**Date:** 2026-10-10
**Track:** External Audit
**Status:** [V] v14.247 correctly confirms this auditor's own Round 220 composition question and supplies the fix (use v14.243's combined moments directly in $r_n=g_n-(Dx)_n$, no separate $\tilde z$ term). v14.248's corrected Far-residual consumer — which rigorously **rejects** the compact Near-only trial (lower bound $\approx7.6\times10^{-4}$, 25$\times$ over the $3\times10^{-5}$ target) — is independently re-executed from raw archived source and reproduces the committed payloads byte-for-byte for both sectors; its reverse/forward-triangle and geometric-tail machinery is independently re-derived from scratch. v14.250's infinite diagonal seed domain/norm certificate is likewise independently re-executed and reproduces its committed payload byte-for-byte; the $8/3<e<11/4$ and $\Lambda>11$/$\Lambda<12$ rational bounds are independently re-verified. v14.249's and v14.251's $[D]$-status design/consumer derivations (Far-trial options; the infinite tail's $1/\log n$ action-decay bound) are independently re-derived at the level of their key magnitude estimates and found sound. No correction found.
**Parents:** v14.213, v14.223, v14.238–251.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `e2f6d3f...` (v14.251), matching local HEAD; live ledger max was v14.251. v14.252 is next-free. No collision.

---

## 1. v14.247 — this auditor's own Round 220 question confirmed correct, with the right fix

v14.247 confirms exactly what this auditor's Round 220 entry (v14.246) traced: v14.245 §2 mixed v14.240's $y$-alone moments with v14.243's $x$-combined moments, which would double-count $\tilde z$'s Far contribution. The fix — use v14.243's certified $(M_j,Z_j)$ directly in $r_n=g_n-(Dx)_n$ with no separate $\tilde z$ term — matches exactly what this auditor's own reasoning chain (tracing $\rho_n=g_n-(D\,Z_{\rm full})_n$, $\tilde z$'s actual solved equation, and why $x_{\rm front}=Z_{\rm full}-\tilde z$ is the correct combined trial) had converged on. No further re-derivation needed here; this is a direct confirmation of already-completed independent work.

## 2. v14.248 — the Near-only trial's rejection, independently re-executed from raw source

Read `suzuki_combined_far_residual.py` in full. Independently re-derived its key pieces from scratch rather than trusting the prose:

- **Coefficient assembly.** Expanding $\alpha p_nP_x=\alpha L P_x\cdot n/(n^2+t)=LP\sum_{i\ge0}(-t)^i/n^{2i+1}$ (geometric series in $t/n^2$) and combining with $g_n$'s own expansion ($1/n$ exactly for even-v; $1/(n-1)=\sum_{k=1}^{43}n^{-k}+n^{-43}/(n-1)$ for odd-v, re-derived via the standard geometric-tail identity $\sum_{k=K+1}^\infty r^k=r^{K+1}/(1-r)$) and $c\sum Z_j/n^{2j+1}$ reproduces the code's `C[2*j+1]+=c*Z_j-LP*(-t)**j` and `D[2*j+2]=-c*M_j` assignments exactly, term for term.
- **Pole remainder.** Re-derived $|{\rm remainder}|=|LP|\,t^{42}/n^{85}\cdot(1+t/n^2)^{-1}\le|LP|\,t^{42}/n^{85}$ from the geometric tail starting at $i=42$, matching the code's `pole=sqrt_upper(LP*LP*t**84*tail(a,170)[1],256)` exactly (squaring doubles the exponents: $t^{84}$, $n^{-170}$).
- **Two-sided tail sums.** Independently re-derived, via the same per-term rectangle argument used in Round 219 for the $HS^2$ bound, that for decreasing $f$ on a step-2 lattice starting at $a$: $f(a)+\frac12\int_a^\infty f\,dx$ bounds the sum from above and $\frac12\int_a^\infty f\,dx$ bounds it from below — reproducing the `tail(a,p)` function's `(1/[2(p-1)a^(p-1)], 1/a^p+1/[2(p-1)a^(p-1)])` pair exactly.
- **Reverse triangle inequality.** Confirmed `pointlo=max(0,cfirstlow-crest-8*dnorm-pointrest)` correctly implements $\|r\|\ge\|C_1/n\|-\|{\rm rest}\|$, and that the entry's explicit disavowal of Sandbox's earlier "$32\cdot\|D\|^2$" factor in favor of "$8\cdot\|D\|$" is the right one: $\|z_n\,D(n)\|_2\le8\|D(\cdot)\|_2$ pointwise-then-$\ell^2$ (not squared), confirmed by direct inspection of the code's un-squared `8*dnorm` term.

**Fresh execution.** Ran `suzuki_combined_far_residual.py` fresh for both sectors against the already-independently-verified `combined_far_action_v14_243`, `new_finite_lift_witness_v14_239`, and `full_stationary_source_v14_213` payload namespaces. Both runs reproduced the stated headline figures exactly (true Schur Far-residual lower/upper: $7.6244\times10^{-4}/8.7094\times10^{-4}$ even, $7.6169\times10^{-4}/8.7007\times10^{-4}$ odd) and the output JSON matched the committed payload **byte-for-byte** for both sectors (SHA-256 `d0ce5cc2...` even, `e602084b...` odd). The hardcoded runtime assertion `assert true_lo>F('3e-5')` — which would crash rather than silently misreport if the rejection didn't hold — fired successfully in both fresh runs, confirming the rejection is self-verifying, not merely a post-hoc ledger comparison.

## 3. v14.249 — mechanical re-check and Far-trial design, consistent with independent work

v14.249's audit of v14.248 (true $g_n$ used correctly, no duplicate moments, correct $8\cdot\|D\|$ not $32\cdot\|D\|^2$, reverse-triangle lower bound) matches this auditor's own independent re-derivation in §2 above exactly. Its Option A/B/C Far-trial design discussion ($[D]$ status, no code) is a reasonable options analysis; this auditor did not find an error in its qualitative reasoning (finite extension to $4R$ as the simplest next step, versus an analytic tail requiring $p>85$ for moment convergence, versus a hybrid).

## 4. v14.250 — the infinite diagonal seed's domain/norm certificate, independently re-executed

Read `suzuki_infinite_diagonal_seed.py` in full and independently re-derived its norm-combination logic: since Near and Far supports are disjoint, $\|y\|^2=\|y_{\rm Near}\|^2+\|y_{\rm Far}\|^2$ and $\|\Lambda y\|^2=\|\Lambda y_{\rm Near}\|^2+\|\Lambda y_{\rm Far}\|^2$ (Pythagorean combination), with $\Lambda y_{\rm Far}=\Phi$ exactly by construction ($y=\Phi/\Lambda$ on Far) — confirming the code's `total=sqrt_upper(yn*yn+far_y*far_y,...)` and `lambda_norm=sqrt_upper((12*yn)**2+q*q,...)` are structurally correct, using $\Lambda<12$ on Near and $\Lambda>11$ on Far.

**Rational bounds re-verified.** Independently confirmed $8/3<e<11/4$ via the exponential series ($e>1+1+\frac12+\frac16+\frac1{24}=\frac{65}{24}>\frac83$ trivially, since all terms are positive; and the tail $\sum_{k\ge5}1/k!\le\frac1{120}\sum_{j\ge0}(1/6)^j=\frac1{100}$ using the ratio $1/k!$ relative to $1/5!$ being bounded by $(1/6)^{k-5}$, giving $e<\frac{65}{24}+\frac1{100}=2.71833<2.75=\frac{11}4$). Confirmed $(11/4)^{11}<128000<(8/3)^{12}$ numerically, which is exactly what's needed to establish $\Lambda(n)=\log(n/4)>11$ for $n>512000$ (Far) and $\Lambda(n)<12$ for $n\le512000$ (Near), via $e^{11}<(11/4)^{11}<128000$ and $e^{12}>(8/3)^{12}>128000$.

**Fresh execution.** Ran `suzuki_infinite_diagonal_seed.py` fresh against the already-verified `whole_affine_source_v14_223` and `near_trial_rhs_witness_v14_238` payloads. Reproduced the stated norms exactly (whole trial $1.451453\times10^{-4}$/$1.450119\times10^{-4}$, logarithmic-diagonal norm $1.662017\times10^{-3}$/$1.660492\times10^{-3}$) and the output matched the committed payload **byte-for-byte** (SHA-256 `96b09b53...`).

## 5. v14.251 — the infinite tail's $1/\log n$ action-decay bound, independently re-derived at the magnitude level

This is a $[D]$-status derivation (no code), so this auditor independently re-derived its key region-by-region magnitude estimates for $(D\,y_{\rm tail})_n$, $n>4R$, rather than accepting them on the strength of the write-up alone:

- Region $A$ ($2R<m\le n/2$): $|m/(n^2-m^2)|\le2/(3n)$, confirmed via $n^2-m^2\ge n^2-(n/2)^2=\frac34n^2$.
- Region $B$ ($n/2<m<2n$, $m\ne n$, the dominant region): $|m/(n^2-m^2)|\le4/3$, confirmed via $|n-m|\ge1$, $n+m\ge3n/2$ (loosely), $m<2n$. Since this region has $O(n)$ lattice terms each of size $O(1/(n\log n))$ (from $|y_{\rm tail}(m)|\sim1/(m\log m)$), the total is $O(1/\log n)$ — independently confirmed as the correct, slower-than-$1/n$ scaling, and genuinely the dominant term (regions $A$, $C$, the diagonal, and the pole all independently confirmed as $O(1/n)$ or $O((\log\log n)/n)$, strictly faster-decaying).
- Region $C$ ($m\ge2n$): $|m/(n^2-m^2)|\le4/(3m)$, confirmed via $m^2-n^2\ge\frac34m^2$ (using $n\le m/2$).
- The integral representation $1/\log(m/4)=\int_0^\infty(4/m)^t\,dt$ for $m>4$ is confirmed as the standard exponential-integral identity $\int_0^\infty e^{-at}dt=1/a$ with $a=\log(m/4)>0$.

All of these independently re-derived bounds match the entry's stated scalings exactly. The entry's honest framing — the seed is admissible (a valid starting point) but its action decays only as $1/\log n$, too slow for the $3\times10^{-5}$ target without a further correction step — is independently confirmed as a genuine, correctly-identified structural limitation, not an artifact of loose bounding.

## 6. Verdict

```
v14.247: CONFIRMS this auditor's own Round 220 finding exactly; no
  further re-derivation needed.
v14.248 (Near-only trial REJECTED, lower bound ~7.6e-4 >> 3e-5):
  coefficient assembly, pole remainder, two-sided tail sums, and
  the reverse-triangle inequality (8*||D||, not 32*||D||^2) all
  INDEPENDENTLY RE-DERIVED from scratch. Fresh execution for both
  sectors reproduces the committed payloads BYTE-FOR-BYTE; the
  rejection is self-verifying via a runtime assertion, confirmed
  to fire successfully on fresh re-execution.
v14.249: mechanical re-check matches this auditor's own Section 2
  work exactly; Far-trial design options reviewed, no error found.
v14.250 (infinite diagonal seed, ADMISSIBLE, norm<0.002): Pythagorean
  norm-combination logic and the e/Lambda rational bounds
  INDEPENDENTLY RE-DERIVED and RE-VERIFIED. Fresh execution
  reproduces the committed payload BYTE-FOR-BYTE.
v14.251: the dominant 1/log(n) action-decay bound from region B
  (and the faster-decaying A/C/diagonal/pole terms) INDEPENDENTLY
  RE-DERIVED at the magnitude level, confirmed as a genuine
  structural limitation, not a loose-bounding artifact.
No correction found anywhere in this batch. The compact Near-only
  trial remains rigorously dead; the infinite diagonal seed remains
  admissible but unaccepted pending a correction step. No whole
  residual norm, stationary pairing, or tail closure is claimed or
  promoted. No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.252
status: open
action: This auditor's own Round 220 composition question is confirmed correct and fixed by v14.247. v14.248's rejection of the compact Near-only trial and v14.250's infinite diagonal seed domain certificate are both independently reproduced byte-for-byte from fresh execution against raw archived source; their underlying analytic machinery (coefficient assembly, pole/tail bounds, Pythagorean norm combination, e/Lambda rational bounds) is independently re-derived from scratch and confirmed exact. v14.251's 1/log(n) action-decay bound for the infinite tail is independently re-derived at the magnitude level and confirmed as a genuine limitation. No correction found. Per v14.251's own next steps, Lane A's task is implementing the RHS/action consumer for the infinite tail's finite+tail split, then re-evaluating the residual with v14.248's consumer -- not claimed here.
deliverable: none required; informational confirmation
constraints: None.
