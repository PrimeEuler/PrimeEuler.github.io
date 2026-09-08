# Hyperbola Involution, Quotient-Block Defect, and the Limits of Factor-Exchange Symmetry

## Scope

This note tests whether the quotient-block / V4 shell-defect matrix introduced in ledger v13.310 carries an exact symmetry under factor exchange.

The conclusion is deliberately two-sided:

- **on exact shell contacts** \(kq=n\), the usual factor involution \((k,q)\leftrightarrow(q,k)\) is exact;
- **off the shell**, the staircase map \(k\mapsto q_k=\lfloor n/k\rfloor\) is not an involution, and the failure is measured by the quotient-block remainder ramp.

No new primality, spectral, or RH/GRH claim is made.

---

## 1. Column-to-quotient map

For fixed \(n\), define

\[
q_k=\left\lfloor\frac nk\right\rfloor,
\qquad
r_k=n-kq_k.
\]

Then the staircase vertex is

\[
D_k=(k,q_k),
\]

with

\[
Y_k^2=kq_k=n-r_k.
\]

Thus

\[
\boxed{r_k=n-Y_k^2}
\]

is the squared shell defect from the product shell \(xy=n\).

---

## 2. Exact factor exchange occurs only on shell contacts

If \(r_k=0\), then

\[
kq_k=n.
\]

Hence \(k\mid n\), \(q_k=n/k\), and

\[
\boxed{(k,q_k)\longleftrightarrow(q_k,k)}
\]

is the ordinary factor-pair involution.

Equivalently,

\[
\boxed{
D_k\text{ lies on }xy=n
\iff
k\mid n
\iff
r_k=0.
}
\]

On such a contact,

\[
q_{q_k}=\left\lfloor\frac{n}{q_k}\right\rfloor=k,
\]

so the staircase map closes exactly in two steps.

---

## 3. Off-shell, the floor map is not an involution

For general \(k\), let \(q=q_k\). Then

\[
n=kq+r_k,
\qquad 0<r_k<k
\]

for a nondivisor position.

Applying the floor map again gives

\[
q_q=\left\lfloor\frac nq\right\rfloor.
\]

There is no general identity \(q_q=k\). In fact,

\[
q_q=\left\lfloor k+\frac{r_k}{q}\right\rfloor
=k+\left\lfloor\frac{r_k}{q}\right\rfloor.
\]

Therefore

\[
\boxed{
q_{q_k}-k
=\left\lfloor\frac{r_k}{q_k}\right\rfloor.
}
\]

This is an exact measure of the failure of \(k\mapsto\lfloor n/k\rfloor\) to be an involution.

Hence

\[
\boxed{
q_{q_k}=k
\iff
r_k<q_k.
}
\]

This condition is strictly weaker than divisibility; involutive closure after two floor applications can occur off-shell whenever the remainder is smaller than the quotient. Thus only the shell-contact case carries the genuine factor-pair interpretation.

---

## 4. Quotient blocks as symmetry-defect ramps

Fix a quotient value \(q\) and its horizontal staircase run

\[
B_q=\{k:L_q\le k\le R_q\},
\]

with

\[
L_q=\left\lfloor\frac{n}{q+1}\right\rfloor+1,
\qquad
R_q=\left\lfloor\frac nq\right\rfloor.
\]

Across the block,

\[
Y_k^2=kq,
\]

so

\[
\Delta_k=n-kq.
\]

Therefore

\[
\boxed{
\Delta_{k+1}-\Delta_k=-q.
}
\]

Each horizontal run is an exact linear defect ramp away from the product shell.

At the right endpoint,

\[
\Delta_{R_q}
=n-q\left\lfloor\frac nq\right\rfloor
=\boxed{n\bmod q}.
\]

Thus the terminal defect of the \(q\)-run is the remainder in the **dual factor coordinate**.

Consequently,

\[
\boxed{
q\mid n
\iff
\Delta_{R_q}=0
\iff
(R_q,q)\text{ is an exact shell contact}.
}
\]

This is the correct factor-exchange bridge: exact duality occurs at zero-defect block endpoints, while the remainder ramp measures how far a whole quotient run sits from that exact duality.

---

## 5. Contact pairing and divisor symmetry

If \(q\mid n\), then

\[
R_q=\frac nq.
\]

The shell-contact endpoint is therefore

\[
\left(\frac nq,q\right).
\]

Its exchanged partner is

\[
\left(q,\frac nq\right).
\]

Hence the divisor contacts occur in symmetric pairs around the diagonal, with the usual fixed point only when \(n\) is a square.

Thus

\[
\boxed{
\text{shell-contact set}
=
\{(d,n/d):d\mid n\}
}
\]

is exactly invariant under factor exchange.

The full staircase is not.

---

## 6. Interaction with the V4 character channels

Ledger v13.310 defines block/channel contributions

\[
E_{\chi,q}(n)
=
\sum_{k=L_q}^{R_q}\chi(k)\left(\frac nk-q\right).
\]

The factor-exchange test shows that there is no general symmetry

\[
E_{\chi,q}\stackrel{?}{=}E_{\chi',k}
\]

induced by \(k\leftrightarrow q\), because off-shell the floor map is many-to-one and not an involution.

What is exact is more limited:

1. the **zero-defect endpoints** are paired by \((k,q)\leftrightarrow(q,k)\);
2. each quotient row carries a terminal defect \(n\bmod q\);
3. the V4 character transform acts independently on the column coordinate \(k\bmod12\);
4. quotient compression and character projection still commute linearly.

So the two-axis matrix

\[
(q,\chi)
\]

has no hidden transpose symmetry forced by factor exchange.

This negative result is structurally useful: it prevents identifying the quotient-index axis with the residue-character axis or treating the staircase as a self-dual matrix away from shell contacts.

---

## 7. Prime and square special cases

For a prime \(p\), the only shell contacts are

\[
(1,p),\qquad(p,1).
\]

Thus the contact involution has exactly one nontrivial pair and no interior fixed/contact points.

For a square \(n=m^2\), the diagonal point

\[
(m,m)
\]

is a fixed point of factor exchange and an exact shell contact.

Therefore the contact geometry distinguishes:

- primes: only the two boundary contacts;
- nonsquare composites: boundary contacts plus interior paired contacts;
- squares: paired contacts plus one diagonal fixed contact.

This is the standard divisor symmetry rendered as product-shell contact geometry.

---

## 8. Interpretation

The correct hierarchy is

\[
\boxed{
\text{factor exchange is exact on the shell-contact subset, not on the full divisor staircase.}
}
\]

The quotient-block remainder field records the failure of exact factor exchange away from the shell:

\[
\boxed{
\Delta_{R_q}=n\bmod q.
}
\]

Thus the staircase is best viewed as a one-sided integer approximation to the symmetric hyperbola \(xy=n\), with exact self-duality recovered only at divisor contacts.

This leaves the v13.309-v13.310 V4 overlay intact while ruling out a stronger, unsupported self-duality of the full \((q,\chi)\) defect matrix.
