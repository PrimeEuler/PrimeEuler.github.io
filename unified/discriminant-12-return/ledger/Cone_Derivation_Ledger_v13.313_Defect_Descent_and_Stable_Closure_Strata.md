# Cone Derivation Ledger v13.313 — Defect Descent and Stable Off-Shell Closure Strata

## Scope

This checkpoint continues v13.312 by classifying the quotient-transport dynamics of the shell defect.

Companion note:

`research-notes/Defect_Descent_and_Stable_Closure_Strata.md`

The main result is a trichotomy separating exact divisor contact, stable positive-defect two-step closure, and strict Euclidean descent.

No new factoring algorithm, primality theorem, RH/GRGRH, spectral, positivity, or Fredholm claim is made.

---

## 1. Staircase state and transported defect

For fixed n and column k, write

\[
q=\left\lfloor\frac nk\right\rfloor,
\qquad
r=n-kq,
\qquad
0\le r<k.
\]

Then

\[
Y^2=kq=n-r,
\]

so

\[
\boxed{\Delta_k=r=n\bmod k.}
\]

Passing to the quotient coordinate q gives

\[
R_q=\left\lfloor\frac nq\right\rfloor
=k+\left\lfloor\frac rq\right\rfloor,
\]

and

\[
\boxed{\Delta_q=r\bmod q.}
\]

Equivalently,

\[
\boxed{
\Delta_k
=q(R_q-k)+\Delta_q.
}
\]

---

## 2. Exact three-stratum classification

### Contact stratum

If

\[
r=0,
\]

then

\[
R_q=k,
\qquad
\Delta_q=0,
\]

and

\[
kq=n.
\]

Thus this is the exact factor-contact stratum.

### Stable off-shell closure stratum

If

\[
0<r<q,
\]

then

\[
R_q=k,
\qquad
\Delta_q=r>0.
\]

Hence

\[
\boxed{(k,q,r)\mapsto(q,k,r)}
\]

under the quotient exchange: the coordinate pair closes but the positive defect survives unchanged.

This is not divisibility.

### Descending stratum

If

\[
r\ge q,
\]

write

\[
r=mq+s,
\qquad
m\ge1,
\qquad
0\le s<q.
\]

Then

\[
R_q=k+m>k,
\qquad
\Delta_q=s<q\le r.
\]

Therefore

\[
\boxed{\Delta_q=r\bmod q<q}
\]

is a strict Euclidean defect reduction unless s=0, in which case the quotient endpoint reaches exact shell contact.

The complete trichotomy is

\[
\boxed{
\begin{array}{ccl}
r=0 &\Rightarrow& \text{exact shell contact},\\[1mm]
0<r<q &\Rightarrow& \text{stable off-shell closure},\\[1mm]
r\ge q &\Rightarrow& \text{Euclidean defect descent}.
\end{array}}
\]

---

## 3. Refined interpretation of two-step floor closure

From v13.311,

\[
q_q-k=\left\lfloor\frac rq\right\rfloor.
\]

Hence

\[
\boxed{q_q=k\iff r<q.}
\]

But this includes both

\[
r=0
\]

and

\[
0<r<q.
\]

Therefore two-step closure decomposes into:

\[
\boxed{
\text{true factor closure }(r=0)
\quad\dot\cup\quad
\text{stable off-shell closure }(0<r<q).
}
\]

The shell defect is the exact discriminator between the two.

---

## 4. Geometric Euclidean reading

Along a quotient run at height q,

\[
\Delta_k=n-kq
\]

falls by q per horizontal step:

\[
\Delta_{k+1}-\Delta_k=-q.
\]

The number of steps from k to the right endpoint is

\[
\boxed{
R_q-k=\left\lfloor\frac{\Delta_k}{q}\right\rfloor,
}
\]

and the residual at the endpoint is

\[
\boxed{
\Delta_{R_q}=\Delta_k\bmod q.
}
\]

Thus the quotient ramp is a literal geometric encoding of Euclidean division:

\[
\boxed{
\text{initial defect}
=
q\times\text{horizontal steps}
+
\text{terminal defect}.
}
\]

The stable closure regime 0<\Delta_k<q is exactly the final incomplete q-sized segment: no horizontal step remains, but the point is still off-shell.

---

## 5. What iteration does and does not mean

Repeated defect transport contains Euclidean-remainder structure, but this does not by itself define a new factorization algorithm.

The arithmetic content is classical Euclidean division. The contribution of the present framework is geometric:

- quotient height = divisor of the defect ramp step size;
- endpoint drift = Euclidean quotient;
- terminal squared shell defect = Euclidean remainder;
- zero remainder = exact shell contact.

This distinction should be kept explicit in later work.

---

## Relation to v13.309-v13.312

- v13.309: local 4V/V4 Fourier overlay.
- v13.310: four-channel shell-defect transform.
- v13.311: factor exchange exact only on shell contacts.
- v13.312: dual defect transport is Euclidean division.
- v13.313: quotient transport splits into contact, stable positive-defect closure, and strict descent strata.

The V4 character transform and Euclidean transport remain independent exact operations on the same defect field.

---

## Guardrails

- Stable two-step closure with positive defect is not a divisor criterion.
- Do not promote the floor map to a global involution.
- Do not present Euclidean defect descent as a new factoring algorithm.
- Exact factor symmetry remains confined to the zero-defect contact subset.
- No new primality theorem is claimed.

## Interpretation

The off-shell staircase is now classified dynamically rather than only kinematically. The shell defect determines whether quotient exchange lands on an exact factor contact, closes off-shell with unchanged positive defect, or performs a strict Euclidean reduction. This gives a precise geometric description of how integer staircase symmetry fails away from the product shell.