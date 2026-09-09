# Mixed Curvature, Euclidean Defect Strips, and the Quarter Shift

## Scope

This note reconnects the quotient-block Euclidean defect dynamics of v13.312-v13.319 with the local four-corner mixed-curvature / V4-Walsh structure developed earlier in the cone ledger.

The key point is exact and elementary: the loss of squared shell defect from a staircase vertex to the right endpoint of its quotient run equals the accumulated discrete mixed curvature of `Y^2=uv` over the intervening factor-cell strip.

The quarter shift enters only through normalization of that same local mixed-difference mode:

\[
\Delta_u\Delta_v(Y^2)=1,
\qquad
\widehat F_{\chi_{11}}=\frac14.
\]

This is a local-to-global normalization bridge. It is not a claim that the global mod-12 V4 residue characters cause Euclidean transport.

---

## 1. Quotient-block endpoint transport

Fix `n` and a staircase column `k`. Put

\[
q=\left\lfloor\frac nk\right\rfloor,
\qquad
R_q=\left\lfloor\frac nq\right\rfloor.
\]

The shell defect is

\[
\Delta_k=n-kq.
\]

At the right endpoint of the same quotient block,

\[
\Delta_{R_q}=n-R_q q=n\bmod q.
\]

From the Euclidean transport identity,

\[
\boxed{
\Delta_k-\Delta_{R_q}=q(R_q-k).
}
\]

Equivalently,

\[
R_q-k=\left\lfloor\frac{\Delta_k}{q}\right\rfloor.
\]

Thus the decrease in squared shell defect is an integer multiple of the quotient height `q`.

---

## 2. The endpoint strip

Define the factor-plane rectangle

\[
\mathcal R_{k,q}=[k,R_q]\times[0,q].
\]

It contains exactly

\[
\boxed{
N_{k,q}=q(R_q-k)
}
\]

unit factor cells.

Since

\[
Y^2(u,v)=uv,
\]

every unit cell satisfies

\[
\boxed{
\Delta_u\Delta_v(Y^2)=1.
}
\]

Therefore

\[
\boxed{
\Delta_k-\Delta_{R_q}
=
\sum_{C\subset\mathcal R_{k,q}}\Delta_u\Delta_v(Y^2)
=
N_{k,q}.
}
\]

This is the exact mixed-curvature strip identity.

For a stable off-shell terminal or a true contact terminal, `R_q=k`, the rectangle has zero width and the accumulated curvature is zero. For a strict-descent state, `R_q>k` and the defect loss is positive.

---

## 3. Corner telescoping

The same identity follows from the four corners of the strip:

\[
Y^2(R_q,q)-Y^2(k,q)-Y^2(R_q,0)+Y^2(k,0)
=q(R_q-k).
\]

Because

\[
Y^2(k,q)=n-\Delta_k,
\qquad
Y^2(R_q,q)=n-\Delta_{R_q},
\]

we obtain

\[
(n-\Delta_{R_q})-(n-\Delta_k)
=
\Delta_k-\Delta_{R_q}.
\]

Hence

\[
\boxed{
\Delta_k-\Delta_{R_q}
=
q(R_q-k).
}
\]

The Euclidean quotient is therefore the horizontal strip width, the quotient height is the vertical strip height, and their product is the accumulated mixed curvature / defect loss.

---

## 4. Blockwise accumulated reduction

For a quotient block

\[
B_q=[L_q,R_q],
\qquad
m_q=R_q-L_q+1,
\]

we have

\[
\Delta_k-\Delta_{R_q}=q(R_q-k).
\]

Summing over the whole block gives

\[
\sum_{k=L_q}^{R_q}(\Delta_k-\Delta_{R_q})
=q\sum_{j=0}^{m_q-1}j.
\]

Thus

\[
\boxed{
\mathcal C_q(n)
:=
\sum_{k=L_q}^{R_q}(\Delta_k-\Delta_{R_q})
=
q\binom{m_q}{2}.
}
\]

This is a weighted triangular cell count. It measures the total raw defect removed by transporting every point of the quotient ramp to its terminal state.

Globally define

\[
\mathcal C(n)
=
\sum_{k=1}^n\bigl(\Delta_k-\Delta_{R_{q_k}}\bigr).
\]

Then

\[
\boxed{
\mathcal C(n)
=
\sum_{q\in Q(n)}q\binom{m_q}{2}.
}
\]

No asymptotic claim is made here; this is an exact finite identity.

---

## 5. Local V4/Walsh quarter normalization

For one elementary factor cell with unit spacing, let the four product values be

\[
F_{00}=pq,
\quad
F_{10}=(p+1)q,
\quad
F_{01}=p(q+1),
\quad
F_{11}=(p+1)(q+1).
\]

The raw checkerboard mixed difference is

\[
F_{11}-F_{10}-F_{01}+F_{00}=1.
\]

Under the normalized four-point V4/Walsh transform,

\[
\widehat F_{\chi_{11}}
=\frac14
(F_{00}-F_{10}-F_{01}+F_{11})
=\frac14.
\]

Therefore each unit factor cell contributes

\[
\boxed{M_F^2=\frac14}
\]

to the normalized local mixed mode.

Consequently the endpoint strip obeys

\[
\boxed{
\frac{\Delta_k-\Delta_{R_q}}4
=
\sum_{C\subset\mathcal R_{k,q}}\widehat F_{\chi_{11}}(C)
=
\frac14 q(R_q-k).
}
\]

Equivalently,

\[
\boxed{
\Delta_k-\Delta_{R_q}
=4\sum_{C\subset\mathcal R_{k,q}}M_F^2.
}
\]

The factor four is purely the normalization difference between the raw checkerboard mixed difference and the normalized Walsh coefficient.

---

## 6. Global quarter-mode sum

Summing the normalized local mixed coefficient over all endpoint strips gives

\[
\boxed{
\mathcal Q(n)
:=
\frac14\mathcal C(n)
=
\frac14\sum_{q\in Q(n)}q\binom{m_q}{2}.
}
\]

Thus

\[
\boxed{
\mathcal Q(n)
=
\sum_{k=1}^n\sum_{C\subset\mathcal R_{k,q_k}}M_F^2.
}
\]

This is a global accumulation of the same local quarter-mode over the Euclidean endpoint strips. The strips overlap, so `\mathcal Q(n)` is a transport-weighted accumulation, not the area of a disjoint union of cells.

That overlap guardrail is essential.

---

## 7. General lattice spacing

For lattice spacing `\delta`, the product coordinate scales as

\[
Y^2=uv,
\]

and one elementary `\delta\times\delta` cell has

\[
\Delta_u\Delta_v(Y^2)=\delta^2.
\]

The normalized local mixed coefficient is then

\[
\boxed{M_F^2=\frac{\delta^2}{4}}.
\]

If a strip contains `N` elementary cells,

\[
\boxed{
\text{raw mixed curvature}=N\delta^2,
\qquad
\text{normalized mixed mode}=\frac{N\delta^2}{4}.
}
\]

The unit-lattice divisor staircase corresponds to `\delta=1`.

---

## 8. Relation to the moment and V4 hierarchies

The present identity connects three layers without identifying their carriers:

\[
\boxed{
\text{Euclidean defect transport}
\longleftrightarrow
\text{accumulated mixed difference of }Y^2
\longleftrightarrow
\text{normalized local quarter mode}.
}
\]

This is compatible with v13.319 but distinct from the global mod-12 character transform.

- The local V4/Walsh algebra acts on the four positions of one elementary factor cell.
- The global mod-12 V4 algebra acts on the arithmetic residue class of the staircase column `k`.
- Both use a four-character/checkerboard algebra, but they are not the same carrier.

One may multiply a strip identity by an arithmetic weight `\chi(k)` and sum over columns, but that is only a weighted sum of exact strip identities; it does not convert the local cell V4 mode into a mod-12 residue character.

---

## 9. Example: n=11

For `n=11`, take `k=4`:

\[
q=\left\lfloor\frac{11}{4}\right\rfloor=2,
\qquad
R_q=\left\lfloor\frac{11}{2}\right\rfloor=5.
\]

Then

\[
\Delta_4=11-8=3,
\qquad
\Delta_5=11-10=1.
\]

Hence

\[
\Delta_4-\Delta_5=2
=2(5-4).
\]

The strip `[4,5]\times[0,2]` contains two unit cells, each with raw mixed difference `1` and normalized quarter mode `1/4`.

Thus

\[
2=1+1,
\qquad
\frac24=\frac14+\frac14.
\]

For `k=6`, `q=1`, `R_q=11`, and the defect falls from `5` to `0`; the strip contains five unit cells.

---

## Guardrails

- The identity is an exact geometric form of Euclidean division, not a new factorization algorithm.
- The local quarter shift is a normalized mixed-difference coefficient, not evidence that mod-12 V4 arithmetic drives quotient transport.
- Endpoint strips for different starting columns overlap; the global sum is a weighted transport accumulation, not the area of a disjoint cell region.
- Stable off-shell closure has zero strip width but positive terminal defect; zero accumulated transport does not imply divisibility.
- Exact divisibility remains `\Delta_k=0`.
- No new divisor-problem asymptotic, primality theorem, RH/GRH, spectral, positivity, or Fredholm claim is made.

## Interpretation

The quarter shift now has an exact local-to-global geometric role inside the divisor staircase. A unit factor cell carries raw mixed curvature `1` and normalized V4/Walsh mixed mode `1/4`. Euclidean transport from a staircase point to its quotient-block endpoint removes exactly one unit of squared shell defect for every unit cell in the endpoint strip. The global defect descent is therefore accumulated local mixed curvature, while the familiar quarter shift is the normalized version of that same local cell invariant.