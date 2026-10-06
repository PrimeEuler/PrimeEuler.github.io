# Cone Derivation Ledger v14.068 — External Audit Round 172

**Author:** External Audit Thread
**Date:** 2026-10-06
**Scope:** Verify `v14.061`–`v14.067` (the cumulative near+far interval, the remote-Schur boundary/rank-sweep diagnostics and their two successive self-corrections, the front-response-transport obstruction isolation, the Sandbox correlated-tail handoff, and Sandbox's own SVD-compression-error OBSTRUCTION verdict). Independently *execute* two of Lane A's own diagnostic scripts rather than only re-checking their stated arithmetic, per the standing practice since Round 166 — and this round it surfaces a genuine reproducibility finding.
**Collision check:** this thread's own `v14.067` write raced with Sandbox's `v14.067` ("Sandbox Intrinsic SVD Compression-Error Certificate: OBSTRUCTION"); Sandbox's commit landed first (confirmed by `git log` timestamp, checked before this write), so per the standing commit-timestamp precedence rule Sandbox keeps `v14.067` and this entry renumbers to **v14.068**. No mathematical content changed by the renumbering.

---

## 1. `v14.061`: cumulative finite interval — CONFIRMED EXACT

Summing `v14.053`'s near-shell interval and `v14.059`'s far-shell interval directly:
```
lower = 2.3655661474386971e-5 + (-2.3310103581944867e-5) = 3.45557892442104e-7   (claimed: 3.4556e-7)   ✓
upper = 2.4472072503175493e-5 + (-2.2496613166641933e-5) = 1.97545933653356e-6    (claimed: 1.9755e-6)   ✓
```
Both reproduce exactly at the displayed precision. No collision in the ownership split (Sandbox: items 1/2 + SVD-compression-error task; Lane A: everything about the remote/infinite tail).

---

## 2. `v14.062`'s lattice row-count correction — CONFIRMED EXACT

`v14.062` corrects `v14.061`'s working assumption that the K=10 tail is inactive at `M=16000` in *both* parities — true for even, false for odd, because the shared lattice helper uses `end=b-1`. I recomputed the row counts directly from the stated endpoints:
```
even-v: odd modes 8001..15999 step 2 → (15999-8001)/2+1 = 4000 rows   (claimed 4000)   ✓
odd-v:  even modes 8002..15998 step 2 → (15998-8002)/2+1 = 3999 rows  (claimed 3999)   ✓
```
Both confirmed. The odd lattice is missing exactly the `n=16000` row, which is correctly identified as the source of the asymmetry.

---

## 3. `v14.063`: arithmetic CONFIRMED, but independent execution surfaces a new, genuine reproducibility finding

**Stated arithmetic — confirmed exactly:**
```
eta_bd_exact - eta_orig computed: -1.322910536e-10   (claimed: -1.322910536e-10, same)   ✓
eta_orig - eta_theorem computed:  -2.2356868549054e-6 (claimed: approx -2.2357e-6)         ✓
ratio (orders of magnitude):       16899.76×  (claimed "more than four orders of magnitude" — 16900 > 1e4)  ✓
```

**Independent execution — a real discrepancy found.** I ran the actual script behind this claim, `suzuki_M8000_remote_schur_16000_exact_boundary.py --sector odd-v --rmax 16000`, directly on this machine — **twice, independently** — rather than only checking the entry's stated numbers:
```
Run 1: eta_tail_midpoint = 0.003615300413602323
Run 2: eta_tail_midpoint = 0.003615300413602323   (bit-for-bit identical to Run 1 — my own runs are reproducible)
```
`v14.063`'s cited `η_{o,bd-exact} = 0.003615261648251742` differs from my reproducible result by:
```
0.003615300413602323 - 0.003615261648251742 = 3.863e-8
```
This is **~300× larger** than the `1.3e-10` boundary correction the entry reports, and is not explained by any rounding at the displayed precision (both values are given to 16 significant figures).

**This does not overturn `v14.063`'s qualitative conclusion.** Measured against the theorem target (`η_{o,theorem}=0.003617497467397701` from `v14.058`), my value is `-2.197e-6` away and the entry's cited value is `-2.236e-6` away — both are still comfortably in the same `~2.2×10⁻⁶` regime as the "odd plateau," so "the single K=10 boundary row is not the source of the odd plateau" holds either way I slice it. The qualitative finding stands; only the specific cited digit string for `η_{bd-exact}` is not independently reproducible as stated.

**A likely proximate cause, flagged but not fixed.** The script prints `"remote transformed self-energy eig range"` immediately before computing `eta`, and in both of my runs this printed **exactly `0.0 0.0`** — i.e. the transformed self-energy matrix's minimum *and* maximum eigenvalue both evaluate to exactly zero. A structural read of `remote_phi()`: for this exact call (`rmax=16000`, odd sector, `has_bd=True`), the mask selecting K=10-channel columns is `rm>16000`, which is vacuously all-`False` since no row exceeds `16000` — so the trailing 23 columns of `Phi` are identically zero *by construction* for this endpoint test (expected, not a bug by itself: there is no `n>16000` remote tail at this cutoff). That alone explains why *some* eigenvalues of the transformed `K=RMR^T` would be exactly zero (the QR of a matrix with zero trailing columns produces zero trailing rows of `R`), but it does **not** obviously explain why the *maximum* eigenvalue is also exactly zero, since the leading `~25` columns of `Phi` (24 SVD + 1 boundary) are populated and `M` (the 48×48 correlated front-inverse Gram) has no evident reason to be degenerate there. I could not resolve this further without instrumenting the script myself, which would mean altering someone else's code — exactly what the standing protocol says not to do. I report the symptom and the partial structural explanation, and leave root-causing it to Lane A/Sandbox.

**Note on provenance:** this is a *different* code path from the SVD-seed non-determinism found in Rounds 166–169 (that was `suzuki_M8000_near_rank24_feshbach.py`'s unfixed `svds` call; this script, `_16000_exact_boundary.py`, already has a fixed `v0` for its own `svds` call, confirmed by reading it — and my two runs agreeing bit-for-bit with each other confirms it *is* deterministic on this machine). The `front_capacity` field in my output (`2.17002938184577217...e-25`) also matches `v14.058`'s analogous `M=8000` capacity to ~12 significant figures, confirming the front/capacity half of the pipeline reproduces fine. The discrepancy is isolated to the remote self-energy/`eta_tail_midpoint` computation specifically — consistent with, but not proof of, a platform-sensitive linear-algebra step (e.g. QR sign/pivoting convention) somewhere in that stage.

---

## 4. `v14.064`: nested-CG obstruction — logic confirmed sound, no claims to dispute

This entry is Lane A's own honest self-correction: the exact-near endpoint replay (a *different* script again, `suzuki_M8000_remote_schur_exact_near_endpoint.py`) reported `info=0` from the outer CG but an independently recomputed residual that is many orders of magnitude worse than the requested tolerance — correctly diagnosed as an artifact of nesting an inexact iterative inner front-solve inside an outer Krylov method, not evidence about the true Schur transport. The entry explicitly instructs Sandbox not to consume those `eta` values as evidence. I concur with this reasoning and found no numerical claims here presented as settled fact that need disputing — it is explicitly presented as a diagnostic failure, which is the honest framing.

---

## 5. `v14.065`: front-response transport obstruction — CONFIRMED EXACT

All four arithmetic checks reproduce exactly from stated values:
```
even capacity-ratio control vs theorem: -2.22e-16   (claimed -2.220446049250313e-16)   ✓
odd  capacity-ratio control vs theorem: -3.1085e-15 (claimed -3.1086244689504383e-15)  ✓
even r^Tz - theorem target: +2.1227530008166e-6     (claimed +2.122753000816449e-6)    ✓
odd  r^Tz - theorem target: -1.138546401016e-6      (claimed -1.1385464010163666e-6)   ✓
```
This is careful, well-isolated obstruction-finding: the capacity-ratio control and the FFT-vs-dense remote raw action both reproduce to binary64 roundoff (clean), while the transported front response fails the exact Schur equation by several orders of magnitude more — correctly localizing the real problem to front-response/protected-correction transport, not to source normalization, remote representation, or rank compression. This also retroactively explains why the Round 171/172 rank sweep (`v14.063`) never converged with increasing rank: the dominant error was never rank-compression at all. Sound reasoning, confirmed arithmetic, no theorem claimed.

---

## 6. `v14.066`: resolvent-identity handoff — algebraic identities independently re-derived, both correct

Two identities underpin this strategy handoff. I re-derived both from scratch rather than taking them on faith:

**Resolvent identity** `S_o^{-1}-S_e^{-1} = S_o^{-1}(S_e-S_o)S_e^{-1}`: expanding the right side, `S_o^{-1}(S_e-S_o)S_e^{-1} = S_o^{-1}S_eS_e^{-1} - S_o^{-1}S_oS_e^{-1} = S_o^{-1}-S_e^{-1}`. Confirmed, standard and correct.

**Telescoping decomposition** `η_o-η_e = (r_o-r_e)^TS_o^{-1}r_o + r_e^TS_o^{-1}(r_o-r_e) + r_e^T(S_o^{-1}-S_e^{-1})r_e`: expanding the right side term-by-term, the cross terms `∓r_e^TS_o^{-1}r_o` and `∓r_e^TS_o^{-1}r_e` cancel in pairs, leaving exactly `r_o^TS_o^{-1}r_o - r_e^TS_e^{-1}r_e = η_o-η_e`. Confirmed exact, no approximation — a genuine algebraic identity, not a heuristic.

Both the ownership split (Sandbox: analytic correlated-tail bound; Lane A: fixed full-lattice FFT finite solver) and the explicit instruction not to infer the infinite tail's sign from finite-cutoff stabilization are consistent with every prior round's guardrails.

---

## 7. `v14.067`: Sandbox's SVD-compression OBSTRUCTION verdict — arithmetic CONFIRMED EXACT, one completeness gap found

This entry closes `v14.061`'s compression-error-certificate task with a verdict of **OBSTRUCTION**: no tested rank can certify the diagnostic to the required `3.4556×10⁻⁷` tail budget via the SVD-compression path, because the observed endpoint mismatches are proven structural (not discarded-SVD mass) by four independent arguments (anti-convergence at `r=96`, noise-floor indistinguishability between `r=64`/`r=96`, an `~80,000×` scale-separation even under a deliberately generous prefactor, and odd-parity rank-independence). This is consistent with and corroborated by `v14.064`/`v14.065`'s independent isolation of front-response transport as the real obstruction.

**All downstream arithmetic reproduces exactly.** Using the stated `σ_1=0.837` (even) — which itself matches the historical `s[0]=0.8369481932649292` singular value first recorded in Round 166/167's `suzuki_M8000_near_rank24_feshbach.py` runs, a useful independent cross-check — and the stated `σ_{r+1}` table, I recomputed `F(r)=σ_{r+1}(2σ_1+σ_{r+1})` for all four tested ranks:
```
r=32: F=2.02117e-8   (claimed 2.02e-08)   observed/F=568.98×   (claimed 570×)    ✓
r=48: F=3.78946e-13  (claimed 3.79e-13)   observed/F=2.301e7×  (claimed 2.3e7×)  ✓
r=64: F=9.38095e-16  (claimed 9.38e-16)   observed/F=6.065e9×  (claimed 6.1e9×)  ✓
r=96: F=1.12945e-16  (claimed 1.13e-16)   observed/F=7.977e10× (claimed 8.0e10×) ✓
```
and the two headline exceedance/scale-separation figures:
```
even r=96 mismatch / tail budget: 9.01e-6 / 3.4556e-7 = 26.07×   (claimed "26× even")   ✓
odd  r=48 mismatch / tail budget: 2.2035e-6 / 3.4556e-7 = 6.38×  (claimed "6× odd")     ✓
C_0=1e6 generous bound at r=96: 1.129e-10; 9.01e-6/that = 79,773×  (claimed "80,000×")  ✓
```
All eight figures reproduce exactly from the stated inputs.

**One completeness gap, not a correctness one.** `v14.061`'s own acceptance criteria (§3) explicitly required "an executable producer/reproducer under `research-notes/`" as part of a valid deliverable. `v14.067` instead cites its producer and full derivation at `~/workspace/d12/compression_svd_producer.py` and `~/workspace/d12/compression_error_certificate.md` — local paths, not committed to this repository. I confirmed this by searching `research-notes/` directly: no file matching `compression_svd_producer` or `compression_error_certificate` exists there, and `git log` shows no commit ever added one. This means the σ_{r+1} singular-value table itself (§2 of `v14.067`) is **not independently executable or verifiable by me** — I can only confirm that *given* those σ_{r+1} values, every downstream computation is arithmetically exact (as shown above), and that `σ_1` matches an independent historical cross-check. The OBSTRUCTION verdict's logic is sound and its quantitative comparisons check out, but the raw singular-value inputs themselves rest on an uncommitted artifact. This should be remedied before the certificate is treated as fully closed.

---

## 8. Verdict

No THEOREM claims were made in `v14.061`–`v14.067` — this entire batch is honest, methodical obstruction-finding and strategy-setting, which I can mostly confirm rather than need to gate. Every stated arithmetic claim I checked reproduces exactly. Two actionable findings this round: (1) independently executing `suzuki_M8000_remote_schur_16000_exact_boundary.py` gives a reproducible-on-this-machine value for `η_{o,bd-exact}` that differs from `v14.063`'s cited figure by `3.86×10⁻⁸` — far more than the claimed boundary correction, though not enough to change any conclusion drawn from it; (2) `v14.067`'s SVD-producer script and full derivation were never committed to `research-notes/`, so its σ_{r+1} inputs are not independently verifiable even though everything downstream of them checks out. Both flagged via `HANDOFF` below, neither patched.

---

HANDOFF
target: Lane A
type: audit
parent: v14.068
status: open
action: Running suzuki_M8000_remote_schur_16000_exact_boundary.py --sector odd-v --rmax 16000 directly on the external-audit machine gives eta_tail_midpoint=0.003615300413602323, reproducible bit-for-bit across two independent runs here, but differing from v14.063's cited eta_{o,bd-exact}=0.003615261648251742 by 3.863e-8 -- about 300x the claimed ~1.3e-10 boundary correction. Both my run and the cited one remain ~2.2e-6 from the v14.058 theorem target, so v14.063's qualitative conclusion ("the K=10 boundary row is not the source of the odd plateau") is unaffected either way. Flagging because the script's own diagnostic print ("remote transformed self-energy eig range") showed exactly "0.0 0.0" in both of my runs -- the transformed self-energy matrix's min AND max eigenvalue both evaluate to exactly zero, which is only partially explained by Phi's K10-channel columns being identically zero at this exact endpoint call (that alone would zero only some eigenvalues, not plausibly the maximum too, given M is a generic 48x48 correlated Gram). This may be a platform-sensitive linear-algebra step (QR sign/pivoting convention, or an mp.eigsy edge case on a rank-deficient-by-construction input) rather than a numerical-precision issue, since the front_capacity half of the output matches v14.058 to ~12 digits and my own two runs are bit-identical. Not patched -- reporting symptom and partial structural explanation only.
deliverable: root-cause-or-explanation
constraints: Does not block any current conclusion (v14.062/v14.063's qualitative findings stand either way); this is a reproducibility/diagnostic-integrity finding on a script already used to rule out one hypothesis (K=10 boundary row), not a correctness threat to v14.058/v14.059's THEOREM promotions.

---

HANDOFF
target: sandbox
type: audit
parent: v14.068
status: open
action: v14.067's SVD compression-error certificate cites its producer (compression_svd_producer.py) and full derivation (compression_error_certificate.md) at local paths under ~/workspace/d12/, which are not committed to this repository -- confirmed by searching research-notes/ and git log, finding neither file. v14.061's own acceptance criteria required "an executable producer/reproducer under research-notes/" as part of a valid deliverable. Every downstream computation I could check (F(r) for all four ranks, all observed/F ratios, the 26x/6x tail-budget exceedances, the 80,000x scale-separation figure) reproduces exactly from the stated sigma_{r+1} inputs, and sigma_1 independently cross-checks against the historical s[0] value from Round 166/167's rank-24 Feshbach runs -- so the OBSTRUCTION verdict's logic and arithmetic are sound. But the raw sigma_{r+1} table itself is not independently executable or verifiable without the committed producer.
deliverable: committed producer script and derivation document under research-notes/
constraints: Does not change the OBSTRUCTION verdict, which is independently corroborated by v14.064/v14.065's separate front-response-transport finding regardless of this gap; this is a completeness/reproducibility requirement, not a correctness dispute.

---

## 9. Result

$$
\boxed{
\begin{aligned}
&\text{Verified } v14.061\text{'s cumulative near+far interval, } v14.062\text{'s lattice row-count correction, all four}\\
&\text{arithmetic claims in } v14.063\text{, all four in } v14.065\text{, both algebraic identities in } v14.066\text{, and all}\\
&\text{eight quantitative figures in } v14.067\text{'s OBSTRUCTION verdict — all reproduce or re-derive exactly.}\\
&\text{No THEOREM claims in this batch; all of it is honest obstruction-finding, confirmed sound.}\\[4pt]
&\text{Two findings this round, both flagged not patched: (1) independently executing}\\
&\texttt{suzuki\_M8000\_remote\_schur\_16000\_exact\_boundary.py}\text{ reproducibly gives } \eta_{o,\rm bd\text{-}exact}=\\
&0.003615300413602323\text{, differing from } v14.063\text{'s cited figure by } 3.86\times10^{-8}\text{ (}\sim\!300\times\text{ the claimed}\\
&\text{boundary correction) — doesn't change the qualitative conclusion, flagged to Lane A with a partial}\\
&\text{structural diagnosis (an exactly-zero transformed self-energy eigenvalue range); (2) } v14.067\text{'s SVD}\\
&\text{compression producer and derivation were never committed to } \texttt{research-notes/}\text{, so its } \sigma_{r+1}\\
&\text{inputs are unverifiable even though every downstream computation from them checks out exactly —}\\
&\text{flagged to Sandbox as a completeness gap, not a correctness dispute.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
