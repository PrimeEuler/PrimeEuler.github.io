# Cone Derivation Ledger v13.312 — Euclidean Dual Defect Transport

## Scope

This checkpoint sharpens v13.311 by deriving the exact arithmetic law that controls the off-shell failure of factor exchange on the divisor staircase.

Companion note:

`research-notes/Euclidean_Dual_Defect_Transport.md`

No RH/GRH, spectral, positivity, Fredholm, or new primality claim is made.

---

## 1. Staircase defect

For fixed \(n\) and column \(k\), write

\[
q=\left\lfloor\frac nk\right\rfloor,
\qquad
r=n-kq,
\qquad
0\le r<k.
\]

Then the staircase vertex \((k,q)\) has

\[
Y^2=kq=n-r,
\]

so

\[
\boxed{\Delta_k=r=n\bmod k.}
\]

---

## 2. Two-step floor drift

Evaluate the staircase at the quotient coordinate \(q\):

\[
\left\lfloor\frac nq\right\rfloor
=
\left\lfloor k+\frac rq\right\rfloor
=
k+\left\lfloor\frac rq\right\rfloor.
\]

Hence

\[
\boxed{
q_q-k
=
\left\lfloor\frac{\Delta_k}{q}\right\rfloor.
}
\]

Thus the failure of naive factor exchange is the quotient obtained by Euclidean division of the original shell defect by \(q\).

---

## 3. Transported defect

Write

\[
\Delta_k=mq+s,
\qquad
m=\left\lfloor\frac{\Delta_k}{q}\right\rfloor,
\qquad
0\le s<q.
\]

Since

\[
q_q=k+m,
\]

the shell defect at the quotient-column vertex is

\[
\begin{aligned}
\Delta_q
&=n-q q_q\\
&=n-q(k+m)\\
&=\Delta_k-mq\\
&=s.
\end{aligned}
\]

Therefore

\[
\boxed{
\Delta_q
=
\Delta_k\bmod q.
}
\]

Equivalently,

\[
\boxed{
\Delta_k
=q(q_q-k)+\Delta_q,
\qquad
0\le\Delta_q<q.
}
\]

This is the exact dual-defect transport law.

---

## 4. Quotient-block endpoint form

For the quotient block at height \(q\),

\[
R_q=\left\lfloor\frac nq\right\rfloor=q_q.
\]

Hence

\[
\boxed{
R_q-k
=
\left\lfloor\frac{\Delta_k}{q}\right\rfloor,
}
\]

and its terminal defect is

\[
\boxed{
\Delta_{R_q}
=n-qR_q
=
\Delta_k\bmod q.
}
\]

So

\[
\boxed{
\Delta_k
=q(R_q-k)+\Delta_{R_q}.
}
\]

The original shell defect is therefore decomposed exactly into:

1. quotient height \(q\),
2. horizontal endpoint drift \(R_q-k\),
3. reduced terminal defect \(\Delta_{R_q}\).

These are the divisor, quotient, and remainder of a Euclidean division.

---

## 5. Contact and near-contact strata

If \(\Delta_k=0\), then

\[
R_q=k,
\qquad
\Delta_{R_q}=0,
\]

and exact factor exchange holds.

If

\[
0<\Delta_k<q,
\]

then

\[
R_q=k,
\qquad
\Delta_{R_q}=\Delta_k>0.
\]

Thus two-step floor closure can occur off-shell: the coordinate pair returns, but the defect survives.

If

\[
\Delta_k\ge q,
\]

then

\[
R_q>k,
\]

and the terminal defect is strictly reduced to

\[
\Delta_{R_q}=\Delta_k\bmod q<q.
\]

So quotient exchange performs one Euclidean-reduction step on the shell defect.

---

## 6. Relation to v13.311

v13.311 established

\[
q_{q_k}-k=\left\lfloor\frac{r_k}{q_k}\right\rfloor
\]

and identified the quotient-block terminal defect as \(n\bmod q\).

v13.312 combines these into one exact identity:

\[
\boxed{
\Delta_k
=
q_k\bigl(R_{q_k}-k\bigr)
+
\Delta_{R_{q_k}}.
}
\]

Thus the same Euclidean division simultaneously controls the two-step floor drift and the reduced terminal remainder.

---

## Guardrails

- This does not promote \(k\mapsto\lfloor n/k\rfloor\) to a global involution.
- Exact factor exchange remains confined to zero-defect shell contacts.
- Two-step closure is weaker than divisibility.
- The result is compatible with, but independent of, the V4 character decomposition of v13.309-v13.310.
- No new factorization or primality theorem is claimed.

## Interpretation

The off-shell failure of factor symmetry is not arbitrary. It is governed by Euclidean division of the shell defect:

\[
\boxed{
\text{original defect}
=
q\times\text{horizontal drift}
+
\text{reduced terminal defect}.
}
\]

This gives the quotient-block endpoint a precise dynamical meaning: it is the Euclidean reduction of the shell-defect field under passage to the quotient coordinate.