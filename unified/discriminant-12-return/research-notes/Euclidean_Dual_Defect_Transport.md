# Euclidean Dual Defect Transport on the Divisor Staircase

## Scope

This note continues the quotient-block / shell-defect analysis by deriving the exact law governing what happens to an off-shell staircase defect under passage from the column coordinate

\[
k
\]

to the quotient coordinate

\[
q=\left\lfloor\frac nk\right\rfloor.
\]

The result is an exact Euclidean-division transport law. It does not produce a global factor involution; instead it describes precisely how the failure of factor symmetry propagates.

---

## 1. First defect decomposition

Fix \(n\ge1\) and \(1\le k\le n\). Write

\[
q=\left\lfloor\frac nk\right\rfloor,
\qquad
r=n-kq,
\qquad
0\le r<k.
\]

The divisor-staircase vertex \((k,q)\) has

\[
Y^2=kq=n-r,
\]

so its squared shell defect is

\[
\boxed{\Delta_k=r=n\bmod k.}
\]

---

## 2. Swap to the quotient coordinate

Now evaluate the staircase at column \(q\). Since

\[
n=kq+r,
\]

we have

\[
\left\lfloor\frac nq\right\rfloor
=
\left\lfloor k+\frac rq\right\rfloor
=
k+\left\lfloor\frac rq\right\rfloor.
\]

Define the two-step floor drift

\[
\boxed{m=\left\lfloor\frac rq\right\rfloor.}
\]

Then

\[
\boxed{q_q=k+m.}
\]

Thus the off-shell failure of the naive exchange \((k,q)\mapsto(q,k)\) is exactly the quotient in the Euclidean division of the original defect \(r\) by \(q\).

---

## 3. The transported defect is the Euclidean remainder

Write the Euclidean division

\[
\boxed{r=mq+s,\qquad 0\le s<q.}
\]

At the quotient-column vertex \((q,q_q)=(q,k+m)\), the new shell defect is

\[
\begin{aligned}
\Delta_q
&=n-q\left\lfloor\frac nq\right\rfloor\\
&=n-q(k+m)\\
&=(kq+r)-qk-mq\\
&=r-mq\\
&=s.
\end{aligned}
\]

Therefore

\[
\boxed{\Delta_q=r\bmod q.}
\]

Equivalently,

\[
\boxed{
\Delta_q
=
\Delta_k
-q\left\lfloor\frac{\Delta_k}{q}\right\rfloor.
}
\]

This is the exact dual-defect transport law.

The pair

\[
\left(
\left\lfloor\frac{\Delta_k}{q}\right\rfloor,
\Delta_k\bmod q
\right)
\]

simultaneously gives:

1. the horizontal drift of the twice-applied floor map, and
2. the new shell defect after moving to the quotient coordinate.

---

## 4. Contact and near-contact strata

If \(r=0\), then

\[
m=0,\qquad s=0,
\]

so

\[
q_q=k,
\qquad
\Delta_q=0.
\]

This is the exact factor-pair case.

More generally, if

\[
0<r<q,
\]

then

\[
m=0,
\qquad
q_q=k,
\qquad
\Delta_q=r.
\]

Hence two-step floor closure occurs without shell contact whenever the original defect is positive but smaller than \(q\). In this regime the coordinate pair returns while the defect survives unchanged.

If

\[
r\ge q,
\]

then

\[
m\ge1,
\]

and the quotient-column vertex moves to \((q,k+m)\), while the defect is reduced from \(r\) to

\[
s=r\bmod q<q.
\]

Thus the quotient swap performs one Euclidean-reduction step on the shell defect.

---

## 5. Relation to quotient-block terminal defects

For the horizontal quotient block at height \(q\), the right endpoint is

\[
R_q=\left\lfloor\frac nq\right\rfloor=k+m.
\]

Its terminal defect is

\[
\Delta_{R_q}=n-qR_q.
\]

By the result above,

\[
\boxed{
\Delta_{R_q}
=
\Delta_q
=
r\bmod q.
}
\]

So the terminal remainder of the \(q\)-run is exactly the Euclidean remainder obtained by dividing the original column defect by the quotient coordinate.

This ties together three quantities:

\[
\boxed{
\Delta_k=r,
\qquad
R_q-k=\left\lfloor\frac rq\right\rfloor,
\qquad
\Delta_{R_q}=r\bmod q.
}
\]

They are simply the dividend, quotient, and remainder of one Euclidean division.

---

## 6. Geometric reading

Starting from the staircase vertex

\[
(k,q),
\]

the exact product shell is missing by squared height

\[
r=n-kq.
\]

Passing to the transposed quotient coordinate does not restore symmetry in general. Instead, the missing product \(r\) is decomposed into

\[
r=q(R_q-k)+\Delta_{R_q}.
\]

Hence

\[
\boxed{
\text{off-shell asymmetry}
=
q\times\text{horizontal endpoint drift}
+
\text{residual terminal defect}.
}
\]

This is a discrete geometric Euclidean division of the shell defect.

---

## 7. Guardrails

- The map \(k\mapsto\lfloor n/k\rfloor\) is still not a global involution.
- The Euclidean reduction above is an exact arithmetic identity, not a new factorization algorithm.
- Exact factor exchange remains equivalent to zero shell defect.
- Two-step floor closure may occur with positive defect and must not be identified with divisibility.
- No V4 character identity is needed for this law; it is compatible with the v13.309-v13.311 character decomposition but logically independent of it.

## Interpretation

The quotient-coordinate swap does not merely fail away from the product shell. Its failure is structured by Euclidean division:

\[
\boxed{
\Delta_k
=
q\,(R_q-k)+\Delta_{R_q},
\qquad
0\le\Delta_{R_q}<q.
}
\]

Thus the original shell defect splits exactly into an integer horizontal drift and a reduced terminal remainder. The quotient-block endpoint is therefore the Euclidean reduction of the off-shell defect field.