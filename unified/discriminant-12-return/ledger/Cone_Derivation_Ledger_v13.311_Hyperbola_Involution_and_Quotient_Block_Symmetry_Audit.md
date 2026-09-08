# Cone Derivation Ledger v13.311 — Hyperbola Involution and Quotient-Block Symmetry Audit

## Scope

This checkpoint tests whether the quotient-block / V4 shell-defect matrix of v13.310 carries an exact factor-exchange symmetry.

Companion note:

`research-notes/Hyperbola_Involution_Quotient_Block_Defect_Symmetry.md`

The result is deliberately restrictive:

- exact factor exchange holds on the shell-contact subset \(kq=n\);
- the full staircase map \(k\mapsto\lfloor n/k\rfloor\) is not an involution;
- quotient-block remainders measure the failure of exact duality away from shell contacts;
- there is no forced transpose/self-duality of the full \((q,\chi)\) matrix.

No new primality, spectral, RH/GRH, or positivity claim is made.

---

## 1. Staircase vertex and shell defect

For fixed \(n\),

\[
q_k=\left\lfloor\frac nk\right\rfloor,
\qquad
r_k=n-kq_k,
\]

and the divisor-staircase vertex

\[
D_k=(k,q_k)
\]

has

\[
Y_k^2=kq_k=n-r_k.
\]

Hence

\[
\boxed{r_k=n-Y_k^2}.
\]

---

## 2. Exact factor involution on shell contacts

If \(r_k=0\), then

\[
kq_k=n,
\]

so

\[
\boxed{(k,q_k)\leftrightarrow(q_k,k)}
\]

is the exact factor-pair involution, and

\[
q_{q_k}=k.
\]

Thus

\[
\boxed{
D_k\in\{xy=n\}
\iff
k\mid n
\iff
r_k=0.
}
\]

The shell-contact set

\[
\{(d,n/d):d\mid n\}
\]

is exactly invariant under factor exchange.

---

## 3. Off-shell floor map is not an involution

For general \(k\), writing \(q=q_k\),

\[
n=kq+r_k.
\]

Then

\[
q_q
=\left\lfloor\frac nq\right\rfloor
=\left\lfloor k+\frac{r_k}{q}\right\rfloor
=k+\left\lfloor\frac{r_k}{q}\right\rfloor.
\]

Therefore

\[
\boxed{
q_{q_k}-k
=\left\lfloor\frac{r_k}{q_k}\right\rfloor.
}
\]

So

\[
\boxed{
q_{q_k}=k
\iff
r_k<q_k.
}
\]

This condition can occur off-shell and is therefore weaker than divisibility. Exact two-step closure of the floor map alone must not be identified with genuine factor-pair duality.

---

## 4. Quotient blocks are exact defect ramps

For a constant quotient block

\[
B_q=\{k:L_q\le k\le R_q\},
\]

with

\[
L_q=\left\lfloor\frac{n}{q+1}\right\rfloor+1,
\qquad
R_q=\left\lfloor\frac nq\right\rfloor,
\]

we have

\[
Y_k^2=kq,
\qquad
\Delta_k=n-kq.
\]

Hence

\[
\boxed{
\Delta_{k+1}-\Delta_k=-q.
}
\]

At the right endpoint,

\[
\boxed{
\Delta_{R_q}
=n-q\left\lfloor\frac nq\right\rfloor
=n\bmod q.
}
\]

Therefore

\[
\boxed{
q\mid n
\iff
\Delta_{R_q}=0
\iff
(R_q,q)\text{ is a shell contact}.
}
\]

The quotient-run endpoint defect is thus the remainder in the dual factor coordinate.

---

## 5. Interaction with v13.310 V4 channels

The block/channel entry remains

\[
E_{\chi,q}(n)
=
\sum_{k=L_q}^{R_q}\chi(k)\left(\frac nk-q\right).
\]

No general relation of the form

\[
E_{\chi,q}=E_{\chi',k}
\]

is induced by factor exchange, because the off-shell floor map is many-to-one and not an involution.

The exact statements are:

1. shell-contact endpoints pair under \((k,q)\leftrightarrow(q,k)\);
2. each quotient row terminates with defect \(n\bmod q\);
3. the V4 transform acts independently on \(k\bmod12\);
4. quotient compression and character projection commute as in v13.310.

Hence the \((q,\chi)\) matrix has no forced transpose symmetry.

---

## 6. Prime and square contact strata

For a prime \(p\), only

\[
(1,p),\qquad(p,1)
\]

are shell contacts.

For a nonsquare composite, there are additional interior contact pairs.

For a square \(n=m^2\), the diagonal contact

\[
(m,m)
\]

is the unique fixed point of factor exchange.

Thus the contact geometry reproduces the classical divisor symmetry while keeping the full staircase distinct from the symmetric hyperbola.

---

## Guardrails

- Do not promote \(k\mapsto\lfloor n/k\rfloor\) to a global involution.
- Two-step floor closure \(q_{q_k}=k\) can occur off-shell; it is not equivalent to divisibility.
- Exact factor exchange belongs to the zero-defect shell-contact subset.
- Do not infer a transpose/self-duality of the v13.310 \((q,\chi)\) matrix.
- The V4 character overlay and quotient-block compression remain valid independently.

## Interpretation

The correct symmetry statement is local to the contact set:

\[
\boxed{
\text{factor exchange is exact on divisor contacts, while quotient remainders quantify the off-shell failure of that symmetry.}
}
\]

This sharpens the geometry of v13.309-v13.310 by distinguishing the symmetric product shell from its one-sided integer staircase approximation.