# Cone Derivation Ledger v13.449 — Odd Frozen-8D Normalized Provenance Reconciliation

Date: 2026-09-14

Status labels: **[D]** exact derived; **[N]** midpoint numerical; **[N-cert]** previously outward-certified; **[O]** open.

## 0. Synchronization

A live-head check immediately before this write found `v13.448` already occupied by `compare two ramified local filtrations`, so this checkpoint uses `v13.449`.  No theorem is promoted here.

The already-closed odd-sector inputs are

\[
A_{FF}\succeq0.53I,
\qquad
\|A_{FT}\|<1.015,
\qquad
\delta_{\rm odd}>0.637.
\]

External Audit Round 32 independently re-executed the finite-high/cross certificate scripts and identified the normalized frozen-eight-dimensional bounds as the remaining theorem-level obligation.

## 1. New independent midpoint replay [N]

The new artifact

`research-notes/suzuki_odd_M4000_normalized_frozen8_midpoint_replay.py`

reconstructs

\[
C=\{2,4,\ldots,20\},
\qquad
F=\{22,24,\ldots,4000\},
\]

from the source-faithful same-parity matrix, loads the frozen exact-dyadic `Q8,L0`, forms

\[
S_F=A_{CC}-A_{CF}A_{FF}^{-1}A_{FC},
\]

and then

\[
C_{\rm nom}
=L_0^{-1}Q_8^TS_FQ_8L_0^{-T}.
\]

The resulting normalized spectrum is essentially the identity; a representative replay gives

\[
\lambda(C_{\rm nom})
\approx
(1,1,1,1,1,1,1.00000019,1.00379169),
\]

with the exact last digits depending on the midpoint source generator.  In particular the frozen preconditioner is functioning as intended and the historical `0.80` lower target is not a midpoint phenomenon; its loss comes from deliberately conservative outward perturbation charges.

## 2. Exact frozen L0 floor [D]

The historical scalar verifier used

\[
1.6689485801587743\times10^{-10}
\]

as a midpoint minimum scale for `L0 L0^T`.

Because `L0` is exact dyadic data, this denominator need not remain a midpoint input.  Exact-Fraction formation of

\[
G_0=L_0L_0^T
\]

followed by Gershgorin gives

\[
\boxed{
\lambda_{\min}(L_0L_0^T)>1.6689\times10^{-10}.
}
\]

The first-row diagonal is

\[
1.6689485801587743\times10^{-10},
\]

while its off-diagonal row radius is only about

\[
8.64\times10^{-16}.
\]

Thus the tiny normalization scale is now tied directly to the immutable exact payload rather than to a floating eigenvalue call.

## 3. Re-derivation of the historical finite-Schur source bound [D/N-cert input]

Use the audited v13.357 source target

\[
\varepsilon_A=2\times10^{-13},
\]

the now-certified

\[
A_{FF}\succeq\mu I,
\qquad \mu=0.53,
\]

and the conservative coupling envelope

\[
\|A_{CF}\|<B,
\qquad B=5.15.
\]

The resolvent identity gives

\[
\|F^{-1}-\widehat F^{-1}\|
\le
\frac{\varepsilon_A}{\mu(\mu-\varepsilon_A)}.
\]

Hence the exact-vs-nominal finite Schur perturbation obeys

\[
\begin{aligned}
\varepsilon_S
&\le
\varepsilon_A
+\frac{B\varepsilon_A}{\mu}
+\frac{B^2\varepsilon_A}{\mu(\mu-\varepsilon_A)}
+\frac{B\varepsilon_A}{\mu-\varepsilon_A} \\
&=
2.297073691706\ldots\times10^{-11}.
\end{aligned}
\]

This independently explains the previously transcript-only number

\[
\boxed{2.2970736917061\times10^{-11}}.
\]

It is a resolvent bound, not a fitted constant.

For an outward solve residual target

\[
\|R_F\|<10^{-12},
\]

the additional Schur charge is

\[
\frac{B}{\mu}10^{-12}
<9.717\times10^{-12}.
\]

Adding the historical `10^-15` formation allowance gives total finite-Schur error below

\[
\boxed{3.269\times10^{-11}}.
\]

Dividing by the new exact `L0 L0^T` floor reproduces the large historical normalized perturbation charge of about `0.19587`.

## 4. Residual-Gram replay through two million [N]

For the normalized basis

\[
U=Q_8L_0^{-T},
\]

solve the finite elimination and form low+finite coefficients

\[
W=
\begin{pmatrix}
U\\
-A_{FF}^{-1}A_{FC}U
\end{pmatrix}.
\]

The normalized tail residual is then generated from the exact Cauchy-type source formula.  The band

\[
4002\le n\le16000
\]

is accumulated directly.  For

\[
n\ge16002,
\]

one has

\[
\frac{4000}{16002}<\frac14,
\]

so the denominator admits the rapidly convergent inverse-power expansion

\[
\frac1{1-j^2/n^2}
=
\sum_{k\ge0}\frac{j^{2k}}{n^{2k}}.
\]

The independent replay obtains

\[
\boxed{
\lambda_{\max}(H_{\le2\times10^6,\rm nom})
\approx0.22441485.
}
\]

The historical transcript value was

\[
0.22441479153402388.
\]

The difference is only about

\[
5.7\times10^{-8},
\]

well inside the old `7e-7` residual-operator comparison allowance.  This is a provenance/regression match only; it does not itself certify that allowance.

## 5. Far-tail leading channel recovered [D structure / N coefficients]

For each normalized direction, write the residual for large even `n` as

\[
r_n
=
\frac{L}{n}
+O(n^{-2}),
\]

where for the odd-sector sinh pole

\[
\boxed{
L
=-\frac2\pi\sum_j Z_jw_j
+\frac{8\sinh(1/2)}\pi\sum_j d_jw_j.
}
\]

The independent midpoint coefficients give

\[
\boxed{\|L\|_2\approx43.84645}.
\]

Therefore the leading rank-one Gram contribution beyond two million is

\[
\|L\|_2^2
\sum_{\substack{n>2\times10^6\\n\ \mathrm{even}}}\frac1{n^2}
\approx4.8063\times10^{-4},
\]

which independently explains the historical far-tail scale.  The remaining `Z_n/n^2`, denominator, and pole-correction terms must still be outward enclosed before retaining the rounded theorem input

\[
\Delta H_{>2M}<4.82\times10^{-4}.
\]

## 6. Scalar reconciliation helper

The additional artifact

`research-notes/suzuki_odd_M4000_normalized_bound_reconciliation.py`

uses exact dyadic arithmetic for the `L0` floor and replays the Schur perturbation arithmetic.  It also confirms that, *if* the historical remaining normalized charges are independently validated, then

\[
C_{\rm odd}>0.804I
\]

and

\[
H_{\rm odd}<0.224898I<0.225I.
\]

Those are comparison calculations, not newly promoted certificates.

## 7. Remaining proof obligations [O]

The normalized theorem bottleneck is now reduced to two explicit outward tasks:

1. **Frozen finite normalization.**  Certify a lower bound for the actual frozen-nominal quantity
   \[
   L_0^{-1}Q_8^TS_{F,\rm nom}Q_8L_0^{-T}
   \]
   with its arithmetic/solve residual.  The midpoint replay is essentially `I`, so only a small one-sided loss is needed.

2. **Normalized residual map.**  Outward-certify the explicit Gram through `2M`, the far-tail inverse-power remainder beyond `2M`, and the exact-vs-point residual-map error.  The historical targets remain
   \[
   H_{\le2M}\approx0.2244148,
   \qquad
   \Delta H_{>2M}<0.000482,
   \qquad
   \|\Delta Y\|<7\times10^{-7}.
   \]

Until these two steps are closed, do **not** restore the v13.404 theorem language.

## 8. Guardrails

- `Q8` has exact rank eight and `L0` is exactly invertible; this is already closed.
- The first two odd directions remain unresolved; no exact kernel statement is made.
- The finite-high and cross-block inequalities are closed independently in v13.434 and v13.443.
- This checkpoint is a provenance reconciliation and reconstruction, not the odd-sector index theorem.
- No exact-zero, RH, or GRH conclusion follows.

---

**Checkpoint conclusion.**  The historical normalized `C` and `H` scales have now been independently reconstructed at midpoint level, the tiny `L0` denominator has been replaced by an exact dyadic Gershgorin floor, and the `2.2970736917061e-11` Schur-source constant has been re-derived explicitly from the resolvent identity.  The remaining theorem work is confined to outward certification of the frozen-nominal one-sided loss and the normalized residual-map/far-tail remainder.