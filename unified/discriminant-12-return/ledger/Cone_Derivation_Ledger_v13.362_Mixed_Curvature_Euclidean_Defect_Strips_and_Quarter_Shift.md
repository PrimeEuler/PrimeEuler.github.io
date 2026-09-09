# Cone Derivation Ledger v13.362 — Mixed-Curvature Euclidean Defect Strips and Quarter Shift

## Scope

This checkpoint reconnects the quotient-block Euclidean defect dynamics of the divisor staircase with the earlier local four-corner mixed-curvature / V4-Walsh quarter-shift structure.

Companion note:

`research-notes/Mixed_Curvature_Euclidean_Defect_Strips_and_Quarter_Shift.md`

The main result is exact: defect loss from a staircase vertex to the right endpoint of its quotient block equals accumulated discrete mixed curvature of `Y^2=uv` over the intervening factor-cell strip. The local quarter shift is exactly one quarter of the raw mixed difference because of normalized four-point Walsh/V4 averaging.

No new factorization algorithm, primality theorem, divisor-problem asymptotic, RH/GRH, spectral, positivity, or Fredholm claim is made.

---

## 1. Endpoint transport

For fixed `n` and column `k`, set

\[
q=\left\lfloor\frac nk\right\rfloor,
\qquad
R_q=\left\lfloor\frac nq\right\rfloor,
\]

with shell defects

\[
\Delta_k=n-kq,
\qquad
\Delta_{R_q}=n-R_q q=n\bmod q.
\]

The Euclidean transport identity gives

\[
\boxed{
\Delta_k-\Delta_{R_q}=q(R_q-k).
}
\]

Thus `R_q-k` is the Euclidean quotient of `\Delta_k` by `q`, and `\Delta_{R_q}` is the terminal remainder.

---

## 2. Mixed-curvature strip identity

Define

\[
\mathcal R_{k,q}=[k,R_q]\times[0,q].
\]

This rectangle contains

\[
N_{k,q}=q(R_q-k)
\]

unit factor cells.

Since

\[
Y^2(u,v)=uv,
\]

every unit cell satisfies

\[
\boxed{\Delta_u\Delta_v(Y^2)=1.}
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

Equivalently, the Euclidean shell-defect reduction is exactly accumulated discrete mixed curvature over the endpoint strip.

---

## 3. Four-corner telescoping

At the strip corners,

\[
Y^2(R_q,q)-Y^2(k,q)-Y^2(R_q,0)+Y^2(k,0)
=q(R_q-k).
\]

Using

\[
Y^2(k,q)=n-\Delta_k,
\qquad
Y^2(R_q,q)=n-\Delta_{R_q},
\]

gives

\[
\boxed{
\Delta_k-\Delta_{R_q}=q(R_q-k).
}
\]

Thus the same identity is simultaneously:

- Euclidean quotient/remainder transport;
- a factor-cell count;
- a telescoped mixed finite difference of `Y^2`.

---

## 4. Blockwise accumulated transport

For one quotient block

\[
B_q=[L_q,R_q],
\qquad
m_q=R_q-L_q+1,
\]

summing the transport loss over all block columns gives

\[
\boxed{
\mathcal C_q(n)
:=
\sum_{k=L_q}^{R_q}(\Delta_k-\Delta_{R_q})
=q\binom{m_q}{2}.
}
\]

Globally,

\[
\boxed{
\mathcal C(n)
=
\sum_{k=1}^n\bigl(\Delta_k-\Delta_{R_{q_k}}\bigr)
=
\sum_{q\in Q(n)}q\binom{m_q}{2}.
}
\]

This is an exact weighted triangular count of accumulated endpoint-strip cells.

The strips overlap, so `\mathcal C(n)` is a transport-weighted accumulation, not the area of a disjoint union.

---

## 5. Quarter-shift normalization

For an elementary unit factor cell with product values

\[
F_{00}=pq,
\quad F_{10}=(p+1)q,
\quad F_{01}=p(q+1),
\quad F_{11}=(p+1)(q+1),
\]

the raw checkerboard mixed difference is

\[
F_{11}-F_{10}-F_{01}+F_{00}=1.
\]

The normalized local V4/Walsh mixed channel is

\[
\boxed{
\widehat F_{\chi_{11}}
=\frac14(F_{00}-F_{10}-F_{01}+F_{11})
=\frac14
=M_F^2.
}
\]

Hence

\[
\boxed{
\frac{\Delta_k-\Delta_{R_q}}4
=
\sum_{C\subset\mathcal R_{k,q}}M_F^2
=
\frac14q(R_q-k).
}
\]

Equivalently,

\[
\boxed{
\Delta_k-\Delta_{R_q}
=4\sum_{C\subset\mathcal R_{k,q}}M_F^2.
}
\]

The factor `4` is only the normalization difference between raw mixed difference and normalized four-point Walsh coefficient.

---

## 6. Global normalized mixed-mode accumulation

Define

\[
\boxed{
\mathcal Q(n)=\frac14\mathcal C(n).
}
\]

Then

\[
\boxed{
\mathcal Q(n)
=
\frac14\sum_{q\in Q(n)}q\binom{m_q}{2}
=
\sum_{k=1}^n\sum_{C\subset\mathcal R_{k,q_k}}M_F^2.
}
\]

This gives an exact global accumulation of the local quarter mode over the Euclidean endpoint strips.

---

## 7. General spacing

For lattice spacing `\delta`, one elementary cell has

\[
\Delta_u\Delta_v(Y^2)=\delta^2,
\qquad
M_F^2=\frac{\delta^2}{4}.
\]

Thus for `N` elementary cells,

\[
\boxed{
\text{raw mixed curvature}=N\delta^2,
\qquad
\text{normalized local mixed mode}=\frac{N\delta^2}{4}.
}
\]

The divisor staircase uses `\delta=1`.

---

## 8. Relation to V4/mod-12 channels

This checkpoint does **not** identify the local four-cell V4 carrier with the global mod-12 residue carrier.

- local V4/Walsh: four positions of one elementary factor cell;
- global mod-12 V4: residue class of the staircase column `k`.

The bridge is the mixed-difference operator itself, not a literal identification of carriers.

A global character weight may multiply the exact strip identity column by column, but this produces a character-weighted sum of strip identities; it does not make `\chi_{11}` of the local cell equal to `\chi_{12}(k)`.

---

## 9. Strata interpretation

The v13.313 dynamical strata now have a curvature reading:

- contact: `\Delta_k=0`, hence `R_q=k`, zero-width strip;
- stable off-shell closure: `0<\Delta_k<q`, still `R_q=k`, zero-width strip but positive terminal defect;
- strict descent: `\Delta_k\ge q`, hence `R_q>k`, positive-width strip and positive accumulated mixed curvature.

Therefore

\[
\boxed{
R_q-k>0
\iff
\Delta_k-\Delta_{R_q}>0
\iff
\text{positive mixed-curvature endpoint strip}.
}
\]

Stable closure is distinguished from contact by terminal defect, not by strip curvature.

---

## Ledger numbering note

The divisor-shell sequence last recorded v13.319, but concurrent Suzuki/verifier work has advanced the shared ledger numbering through v13.361. This checkpoint therefore uses v13.362 to avoid a collision while preserving the same divisor-shell research thread.

---

## Guardrails

- This is a geometric reformulation of exact Euclidean division, not a new factorization algorithm.
- The quarter shift is a normalized local mixed-difference invariant.
- Do not identify local cell V4 labels with global mod-12 residue characters.
- Endpoint strips overlap in the global accumulation.
- Zero strip width does not imply divisibility: stable off-shell closures also have zero width.
- Exact divisibility remains `\Delta_k=0`.
- No asymptotic improvement or new primality criterion is claimed.

## Interpretation

The local-to-global bridge is now exact: each unit factor cell contributes raw mixed curvature `1` and normalized local quarter mode `1/4`; Euclidean quotient transport removes exactly one unit of squared shell defect for each cell in the endpoint strip. The divisor-staircase defect descent is therefore accumulated local mixed curvature, and the quarter shift is precisely the normalized form of that same local cell invariant.