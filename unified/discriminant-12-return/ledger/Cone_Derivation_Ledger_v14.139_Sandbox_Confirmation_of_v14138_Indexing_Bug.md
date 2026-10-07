# Cone Derivation Ledger v14.139 — Sandbox: Independent Confirmation of v14.138 mpmath Indexing Bug; Fix Verified, Not Applied

**Date:** 2026-10-07
**Track:** Sandbox / v14.138 handoff response (partial)
**Status:** [D] v14.138's mpmath negative-indexing bug independently reproduced and confirmed on all five reported sites; [D] proposed fix verified correct; [O] fix NOT applied to Lane A's script — research-notes writes require Jeremy's per-item approval.
**Parents:** v14.136, v14.137, v14.138.
**Collision check:** live ledger max v14.138 at write time; v14.139 is next-free. No collision.

---

## 1. Independent reproduction [D]

Direct mpmath test (dps=30), no shared code with v14.138:
```
m = mp.matrix([1,2,3,4,5]);  m[-1] = 0.0   (not 5.0)
vals,_ = mp.eigsy(mp.matrix([[2,1],[1,2]]))  # ascending: [1.0, 3.0]
vals[-1] = 0.0 ;  vals[vals.rows-1] = 3.0
```
**Confirmed:** `mpmath.matrix` negative indexing silently returns `0.0`.
`mp.eigsy` returns ascending-sorted eigenvalues as `mp.matrix`, so `vals[-1]`
is always `0.0`, never the largest eigenvalue.

Indefinite test (mimicking $\delta G$):
eigs `[-0.18, 0.27]`; buggy `max(abs(vals[0]),abs(vals[-1]))` = `0.18`;
corrected `max(abs(vals[0]),abs(vals[vals.rows-1]))` = `0.27`. **Confirmed**
the 33%-scale understatement mechanism.

## 2. Site confirmation [D]

Fetched `suzuki_normalized_protected_gram_pair.py` from research-notes;
all five sites match v14.138 exactly:
- line 56: `spectral_norm_sym` — load-bearing, confirmed wrong.
- lines 167, 170: fail-closed gate — upper half never fires, confirmed.
- lines 229, 232: `D_max`/`G_max` diagnostics — always `0`, confirmed.

## 3. Fix verification [D]

The proposed fix (`vals[-1]` → `vals[vals.rows-1]`) was tested on the
reproduction above: returns the true largest eigenvalue in all cases,
including the indefinite $\delta G$ pattern. No change to the exact algebra
of v14.136/v14.137 is involved or needed.

## 4. Scope boundary [O]

The fix was **not** applied to Lane A's script. Under Jeremy's standing
rules, research-notes writes require explicit per-item approval; the
autonomous ledger authorization covers handoff-response ledger entries,
not patches to Lane A's research code. The verified fix is ready to apply
(a five-site mechanical change); awaiting Jeremy's go-ahead or Lane A's
own application.

## 5. Verdict

$$\boxed{
\begin{aligned}
&\text{[D] v14.138 bug independently reproduced: mpmath }m[-1]\to 0.0\text{ confirmed.}\\
&\text{[D] All five sites confirmed in the script; fix verified correct.}\\
&\text{[O] Fix not applied — needs Jeremy's per-item approval for research-notes.}\\
&\text{v14.136/v14.137 exact algebra unaffected and needs no change.}
\end{aligned}
}$$

---

HANDOFF-NOTE
target: lane-a
type: bug-verification
parent: v14.139
status: open
action: v14.138's mpmath indexing bug independently confirmed; the vals[vals.rows-1] fix is verified correct on reproduction cases. Sandbox has not patched the script (research-notes firewall); Lane A may apply the five-site fix directly, or Jeremy can authorize sandbox to apply it.
constraints: Do not change v14.136/v14.137 exact algebra; numerical-indexing fix only.
