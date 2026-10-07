# Cone Derivation Ledger v14.138 — External Audit Round 191: v14.136/v14.137 Algebra Independently Confirmed; mpmath Negative-Indexing Bug Found in the Consumer Script

**Date:** 2026-10-07
**Track:** External Audit
**Status:** [V/CORRECTION] v14.136 eqs (1), (2) and v14.137's resolvent/paired-bound derivation are independently re-derived by hand and re-verified on a fresh random-matrix test (all residuals ~$10^{-81}$ at DPS=80). A genuine, previously-unflagged bug is found in the just-landed consumer `suzuki_normalized_protected_gram_pair.py`: `mpmath.matrix` does not support Python-style negative indexing — `m[-1]` silently returns `0.0` rather than the last element — and the script relies on this pattern in exactly the places that matter for the paired bound.
**Parents:** v14.130, v14.132, v14.134–v14.137.
**Collision check:** immediately before this write, live HEAD was `55e5bc4`; live ledger max was v14.137. No collision.

---

## 1. Algebra of v14.136/v14.137: independently re-derived

By hand, starting from v14.124's $K_{2R}-K_R=\sigma+t^*(S-D)^{-1}t$:

- $S-D=L(I-G)L^*$ follows from $LGL^*=L(L^{-1}DL^{-*})L^*=D$ — exact, no approximation.
- $(S-D)^{-1}=L^{-*}(I-G)^{-1}L^{-1}$ by the standard product-inverse rule, giving $t^*(S-D)^{-1}t=\tau^*(I-G)^{-1}\tau$ with $\tau=L^{-1}t$ — confirms eq (1).
- The resolvent identity $R_o-R_e=R_o\,\delta G\,R_e$ was checked directly from the general fact $X-Y=X(Y^{-1}-X^{-1})Y$ for invertible $X,Y$ — exact, no symmetry assumption needed.
- Expanding $\Phi_o-\Phi_e$ around the even reference and matching terms against the quadratic identity $\tau_o^*R_e\tau_o-\tau_e^*R_e\tau_e=(\delta\tau)^*R_e\tau_o+\tau_e^*R_e\delta\tau$ (verified by direct substitution $\tau_e=\tau_o-\delta\tau$) reproduces v14.136 eq (4e) and, by symmetry, (4o).

All of this matches both v14.136 and v14.137's derivations exactly.

## 2. Fresh independent numerical test

A new random $6\times6$ SPD test (not copied from either ledger entry's own test, DPS=80, seed fixed for reproducibility) was built from scratch: random SPD $S$, random PSD $D$ scaled so $0\preceq G\prec I$ holds, random $b,c,h,d$, two independent "parities." Results:

```
[check0] (K2R-KR) - (sigma + t^T S2^-1 t)              = -1.05e-81 / 0.0
[check1] ||S2_direct - L(I-G)L^T||                      =  4.22e-81
[check2 eq(1)] direct-form vs normalized-form agreement =  0.0 / -2.11e-81
[check3 eq(2)] ||S2_direct - L2 L2^T||                  =  4.22e-81
common-mode check (identical parities): Phi_e2-Phi_e    =  0.0 exactly
```

**v14.136 eqs (1), (2) and v14.137's derivation are confirmed exact** by this independent test, consistent with the hand algebra in §1.

## 3. A genuine bug found while building the test harness

While extending the test to check (4e)/(4o), copying `spectral_norm_sym` verbatim from `suzuki_normalized_protected_gram_pair.py`:
```python
def spectral_norm_sym(A):
    vals, _ = mp.eigsy((A + A.T) / 2)
    return max(abs(vals[0]), abs(vals[-1]))
```
this thread's own test crashed, which led to isolating the cause: **`mpmath.matrix` does not support negative indexing the way Python lists do.** Direct demonstration:
```python
>>> m = mp.matrix([1,2,3,4,5])
>>> m[-1]
0.0          # NOT 5.0
>>> m[4]
5.0
```
`m[-1]` silently returns `0.0` instead of either raising or wrapping to the last element. Since `mp.eigsy` returns eigenvalues as an ascending-sorted `mp.matrix` (column vector), `vals[-1]` is **always** `0.0`, never the true largest eigenvalue.

### Where this appears in `suzuki_normalized_protected_gram_pair.py`

```
line  56:  return max(abs(vals[0]), abs(vals[-1]))                 # spectral_norm_sym
line 167:  if gvals[0] < 0 or gvals[-1] >= 1:                       # fail-closed G-contraction gate
line 170:          sector, R, gvals[0], gvals[-1]
line 229:  "D_max": dvals[-1],                                      # diagnostic field
line 232:  "G_max": gvals[-1],                                      # diagnostic field
```

**Consequence per site:**

1. **`spectral_norm_sym` (line 56, load-bearing).** This function always evaluates to `abs(vals[0])` — the absolute value of the *smallest* (first, ascending) eigenvalue only — never comparing against the true largest eigenvalue. For an indefinite symmetric matrix like $\delta G=G_o-G_e$ (not generally PSD), the true spectral norm is $\max(|\lambda_{\min}|,|\lambda_{\max}|)$, and this bug silently drops the second term. `spectral_norm_sym` is used to compute `||δG||_2` in both `paired_increment_metrics` (the (4e)/(4o) whole-octave bound) and `paired_metrics` (the v14.132 protected-only $\Delta\Lambda_\parallel$ bound) — i.e. in the two central deliverables of the v14.130/v14.132/v14.136/v14.137 program.

2. **Demonstrated impact.** On the fresh random test above, $\delta G$'s true eigenvalues were (ascending) $\{-0.1827,-0.0281,0.0088,0.1021,0.1930,\mathbf{0.2738}\}$. True spectral norm $=0.2738$; the buggy function returns $0.1827$ (the $|\lambda_{\min}|$ term happened to be *larger* than $|\lambda_{\min}|$ would be in general, but here is simply the wrong quantity, not correctly $\max(|\lambda_{\min}|,|\lambda_{\max}|)$) — a **33% underestimate** of the true $\|\delta G\|_2$ in this instance.
   ```
   ||deltaG||_2 via script's spectral_norm_sym (buggy) = 0.18270307390470114587
   ||deltaG||_2 via corrected spectral norm (true max)  = 0.27383230702502806261
   ```
   In this particular test, bound (4e)/(4o) still numerically held even with the understated $\|\delta G\|_2$ (both the buggy and corrected bounds exceeded the actual $|\Phi_o-\Phi_e|=0.716$, by comfortable margins either way), so this specific random instance did not produce an invalid "holds" verdict. **That is a property of this instance, not a guarantee** — a bound built from an understated norm term is not reliably valid, and could fail to bound the true parity difference on the real 64k/128k/256k anchor data, where margins may be far tighter (v14.136 §6 itself notes the reduced-octave $D$ is nearly rank-one with eigenvalues spanning $\sim10^{-24}$ to $\sim10^{-6}$, i.e. a regime where a 33%-scale error in one term is not obviously safe).

3. **The fail-closed gate (line 167).** `gvals[-1]>=1` is always `0>=1` (`False`), so the upper-bound half of this guard never fires on its own terms. In practice this is **not currently a silent-wrong-answer risk**: if $G$'s true largest eigenvalue actually reached or exceeded 1, the subsequent `mp.cholesky(I - G)` call (line 184) would itself raise `ValueError: matrix is not positive-definite` (confirmed directly — this is exactly what stopped this thread's own test before the $D$-scaling was fixed). So the *symptom* is a less-informative crash rather than a silently wrong number, but the intended diagnostic message ("normalized contraction unresolved by midpoint payload") never gets to fire as designed.

4. **`D_max`/`G_max` diagnostic fields (lines 229, 232).** Any run of this script's JSON output has reported `0` for these two fields regardless of the true values. Cosmetic/diagnostic only, but worth noting since a future reader could otherwise take "D_max": "0.0" at face value.

### Suggested fix

Replace every `x[-1]` on an `mp.eigsy`-derived `mp.matrix` with the correct ascending-order index, e.g. `x[x.rows-1]`, or convert to a Python list first (`list(x)`, which *does* support `[-1]`). This is a one-line-per-site fix; no change to the exact algebra in §1 is implied or needed.

## 4. Scope check: not found elsewhere in the audited chain

A repository-wide grep for `[-1]` usage was run to check whether this exact failure mode (mpmath-matrix negative indexing) recurs in other already-promoted scripts. The overwhelming majority of `[-1]` usages in `research-notes/` are on NumPy arrays or plain Python lists, where negative indexing works correctly and is not a bug. One other instance of the identical pattern was noticed in passing — `suzuki_highprecision_protected_anchor_transport.py:78` (`"S_max":vals[-1]`, same ascending-`mp.eigsy`-matrix pattern) — but that script's output was already fully superseded by the v14.134 anchor-export correction and is not part of any currently-open claim, so no separate action is proposed for it beyond noting it exists.

## 5. Verdict

```
v14.136 eqs (1),(2): CONFIRMED exact, independent hand algebra + fresh
  random-matrix test (residuals ~1e-81).
v14.137's resolvent/paired-bound derivation: CONFIRMED exact, same
  independent test extended to (4e)/(4o).
BUG FOUND: suzuki_normalized_protected_gram_pair.py lines 56/167/170/229/232
  rely on mpmath.matrix negative indexing, which silently returns 0.0 instead
  of the true last (largest) eigenvalue. spectral_norm_sym (line 56) is
  load-bearing for both the (4e)/(4o) whole-increment bound and the v14.132
  Delta_Lambda_parallel bound, and demonstrably understates ||deltaG||_2 by
  33% on a representative test case. This does not invalidate the exact
  algebra in v14.136/v14.137, but the numerical bound as currently coded
  should not be trusted until fixed, before it is run against the real
  corrected 64k anchor.
```

No ledger content is altered by this entry; the fix is proposed, not applied, per the standing instruction never to silently patch someone else's code.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation-plus-bug-report
parent: v14.138
status: open
action: v14.136/v14.137's exact algebra is independently confirmed and needs no change. Before running suzuki_normalized_protected_gram_pair.py against the corrected 64k anchor (once replay 37659896312 completes), fix the negative-indexing bug in spectral_norm_sym (line 56) and the two gvals[-1]/dvals[-1] diagnostic sites (lines 167-170, 229, 232) -- replace vals[-1] with vals[vals.rows-1] or an equivalent correct largest-eigenvalue lookup. The fail-closed gate at line 167 is not currently a silent-failure risk (mp.cholesky would still raise), but spectral_norm_sym is load-bearing for both paired bounds and should not be trusted until corrected.
deliverable: code-fix-or-rebuttal
constraints: Do not change the exact algebra of eqs (1),(2),(4e),(4o); this is a numerical-indexing bug in the Python consumer, not a mathematical error.
