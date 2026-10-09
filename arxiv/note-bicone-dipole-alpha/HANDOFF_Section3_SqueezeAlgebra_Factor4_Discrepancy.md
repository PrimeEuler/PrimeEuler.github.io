# HANDOFF — §3 "Squeeze-algebra 128/81" Theorem: Independently Computed Value is 32/81, Not 128/81

**From:** External Audit (conversational session, not the discriminant-12-return numerical ledger protocol)
**To:** The arxiv/bicone-dipole thread (Lane A)
**Date:** 2026-10-09
**Status:** Confirmed discrepancy, cross-checked by two independent methods. Not a certified ledger finding — a research-review result the thread should verify against the primary Barut–Kleinert convention before deciding how to act on it.

---

## 1. What was checked

`Note_BiconeDipole_FineStructure_v1.0.tex` §3, Theorem ("Squeeze-algebra 128/81"), claims:

$$\langle0|D_1^\dagger z|\psi\rangle = \frac{128}{81}$$

with $D_1^\dagger=S(-\zeta)$, $\zeta=\ln\sqrt2$, applied identically on all four KS oscillator modes, $|\psi\rangle=\frac12(b_1^{\dagger2}+b_2^{\dagger2})|0\rangle$, and $z=u_1^2+u_2^2-u_3^2-u_4^2$ with $u_i=(b_i+b_i^\dagger)/\sqrt2$ (the standard harmonic-oscillator position normalization — the note does not state this relation explicitly, so it was taken as the natural default). This was independently re-derived and computed, not just read.

## 2. Exact 4-mode combinatorics, re-derived independently

Factorizing the bra/ket over the four independent modes (using that $D_1^\dagger$ acts as a product of single-mode operators, and that $z$ and $|\psi\rangle$ are each sums of single-mode pieces), and resumming the two symmetric terms in $|\psi\rangle$ against the four pieces of $z$, gives exactly:

$$\langle0|D_1^\dagger z|\psi\rangle = d_0^2(e_1d_0-e_0d_1)$$

matching the note's own stated combinatorial formula exactly (re-derived from scratch via direct mode-by-mode expansion, not assumed). So the combinatorics in the note's formula are correct; the question is the *value* of this expression.

## 3. The value: two independent methods both give 32/81, not 128/81

**Method 1 — exact, via the closed-form squeezed-vacuum Fock coefficients** (sympy, exact rational/radical arithmetic):

```python
import sympy as sp
zeta = sp.log(sp.sqrt(2))
tanh_z, cosh_z = sp.simplify(sp.tanh(zeta)), sp.simplify(sp.cosh(zeta))
d0 = sp.simplify(1/sp.sqrt(cosh_z))
def c(n): return (-tanh_z)**n * sp.sqrt(sp.factorial(2*n)) / (2**n * sp.factorial(n))
def bra0_S_ket(n): return sp.simplify(d0*c(n))   # <0|S(-zeta)|2n>
ov0, ov1, ov2 = bra0_S_ket(0), bra0_S_ket(1), bra0_S_ket(2)
d1 = sp.simplify(sp.sqrt(2)*ov1)
e0 = sp.simplify((d0 + d1)/2)
e1 = sp.simplify(ov0 + sp.sqrt(6)*ov2 + sp.Rational(5,2)*sp.sqrt(2)*ov1)  # from u^2 b^dag2|0> = |0>+sqrt6|4>+(5sqrt2/2)|2>
print(sp.simplify(d0**2*(e1*d0 - e0*d1)))   # -> 32/81
```
Result: **`32/81`** exactly.

**Method 2 — fully independent, brute-force numeric** (mpmath, 50-digit precision, 40×40 truncated Fock-space matrix exponential of the squeeze generator, no closed-form formula assumed):

```python
import mpmath as mp
mp.mp.dps = 50
N = 40
zeta = mp.log(mp.sqrt(2))
b = mp.zeros(N, N)
for n in range(1, N): b[n-1, n] = mp.sqrt(n)
bdag = b.transpose()
u = (b + bdag)/mp.sqrt(2)
G = (b*b - bdag*bdag)/2
Smat = mp.expm(-zeta*G)
# ... (extract d0, d1, e0, e1 as matrix elements, same definitions as above)
```
Result: `0.39506172839506172839506172276...`, matching $32/81=0.39506172839506172839506172839506...$ to **27 significant digits** (nowhere near $128/81=1.5802...$).

Two structurally independent computations (infinite-series closed form vs. truncated-matrix numerical exponential) agree on $32/81$ to well beyond any reasonable doubt about arithmetic mistakes on this thread's part.

## 4. What this means, and what it doesn't

**Confirmed:** under the standard oscillator convention $u=(b+b^\dagger)/\sqrt2$, the stated theorem's value is wrong by **exactly a factor of 4**: $32/81$, not $128/81$. Downstream, the note's own chain multiplies this by the $\S3$ node-bridge factor $1/3$ to get the final $-128/243$; using $32/81$ instead gives $-\frac13\cdot\frac{32}{81}=-\frac{32}{243}$, which does **not** match the independently-known correct answer $-128/243$ (confirmed via the §2 parabolic gamma-integral route, already audited earlier in this thread's review and unaffected by this finding).

**Not confirmed — a real, unresolved alternative:** the factor is exactly $4=2^2$, which is precisely what you'd get if the note's intended $u$ is normalized as $u=\sqrt2(b+b^\dagger)$ instead of $(b+b^\dagger)/\sqrt2$ — i.e. twice the standard textbook harmonic-oscillator position operator. Since $z$ is built purely from $u_i^2$ terms, doubling $u$ quadruples every $u^2$-dependent quantity, which would exactly repair the discrepancy. The note never states the $u\leftrightarrow(b,b^\dagger)$ relation explicitly, and this thread does not have access to the primary Barut–Kleinert reference to check whether their specific KS-oscillator convention uses this non-standard normalization. **This is plausible, not confirmed** — it would need to be checked against the original source, or re-derived independently from the physical boundary conditions of the KS map, before concluding either "the theorem has a real error" or "the theorem is correct under an unstated convention."

## 5. Suggested next step

Before this section is relied on further: (a) pin down the exact $u_i\leftrightarrow(b_i,b_i^\dagger)$ normalization the Barut–Kleinert KS-oscillator construction actually uses (check the primary 1967 reference, or re-derive it from the canonical commutation relations implied by the original KS coordinate map rather than assuming the generic textbook convention); (b) once settled, redo the two computations above with the correct convention and confirm $128/81$ falls out; (c) if it doesn't, the theorem needs an actual fix, not just a convention clarification. The code above is fully reproducible and parameterized cleanly enough that trying a different $u$-normalization is a one-line change.

---

HANDOFF
target: arxiv-bicone-thread
type: correctness-finding
status: open
action: Verify the u-to-(b,b^dagger) normalization convention in the Barut-Kleinert/KS-oscillator construction against the primary source; re-run the squeeze-algebra computation above under the correct convention; confirm whether 128/81 is recovered or whether Theorem (Squeeze-algebra 128/81) needs correction.
constraints: This is not a discriminant-12-return ledger entry and carries none of that protocol's certification weight. The combinatorial formula d0^2(e1*d0-e0*d1) itself was independently re-derived and confirmed correct; only the numerical value under the assumed u-normalization is in question. Both computations above are fully reproducible.
