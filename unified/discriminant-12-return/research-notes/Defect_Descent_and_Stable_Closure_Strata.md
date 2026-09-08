# Defect Descent and Stable Off-Shell Closure Strata

## Scope

This note continues the Euclidean dual-defect transport of ledger v13.312. The aim is to distinguish what is genuinely new from what is simply the Euclidean algorithm written in staircase coordinates.

No new factorization, primality, RH/GRH, spectral, positivity, or Fredholm claim is made.

---

## 1. State variables

Fix n and a staircase column k. Let

\[
q=\left\lfloor\frac nk\right\rfloor,\qquad
r=n-kq,\qquad 0\le r<k.
\]

Then the staircase vertex is \((k,q)\), with

\[
Y^2=kq=n-r,
\]

so the shell defect is

\[
\Delta_k=r.
\]

Passing to the quotient coordinate q gives

\[
R_q=\left\lfloor\frac nq\right\rfloor
=k+\left\lfloor\frac rq\right\rfloor,
\]

and the transported terminal defect is

\[
\Delta_q=n-qR_q=r\bmod q.
\]

Thus the transport step is exactly

\[
\boxed{(k,q,r)\longmapsto\left(q,\,R_q,\,r\bmod q\right)}.
\]

The first two entries are staircase coordinates; the third is the Euclidean remainder.

---

## 2. Three exact strata

The transport law gives three sharply distinct cases.

### Contact stratum

If

\[
r=0,
\]

then

\[
R_q=k,\qquad \Delta_q=0,
\]

and the point lies exactly on the product shell:

\[
kq=n.
\]

This is the genuine factor-exchange stratum.

### Stable off-shell closure stratum

If

\[
0<r<q,
\]

then

\[
\left\lfloor\frac rq\right\rfloor=0,
\]

so

\[
R_q=k,
\qquad
\Delta_q=r.
\]

Hence the coordinate pair closes after the quotient exchange but the defect survives unchanged:

\[
\boxed{(k,q,r)\longmapsto(q,k,r).}
\]

This is an exact off-shell fixed-defect stratum. It is weaker than divisibility because r remains positive.

### Descending stratum

If

\[
r\ge q,
\]

write

\[
r=mq+s,\qquad m\ge1,\qquad 0\le s<q.
\]

Then

\[
R_q=k+m>k,
\qquad
\Delta_q=s<q.
\]

Thus the defect strictly descends below the quotient height:

\[
\boxed{\Delta_q=r\bmod q<q\le r.}
\]

If s>0 this is a strict positive defect reduction; if s=0 the quotient endpoint lands on an exact shell contact.

---

## 3. Descent invariant

Define the local defect-height pair

\[
(r,q).
\]

Whenever r\ge q, one transport step gives

\[
(r,q)\mapsto(r\bmod q,\,\cdot),
\]

with

\[
0\le r\bmod q<q.
\]

Therefore r\ge q is a genuine descent condition. The step cannot cycle with the same positive defect while r\ge q.

By contrast, when 0<r<q, the defect does not decrease at that exchange; the pair is in the stable closure stratum.

So the shell-defect dynamics has an exact trichotomy:

\[
\boxed{
\begin{array}{ccl}
r=0 &\Rightarrow& \text{exact contact},\\[1mm]
0<r<q &\Rightarrow& \text{stable off-shell closure},\\[1mm]
r\ge q &\Rightarrow& \text{Euclidean defect descent}.
\end{array}}
\]

---

## 4. This is Euclidean structure, not a new factoring algorithm

The identity

\[
r\mapsto r\bmod q
\]

is exactly one Euclidean remainder step. Iterating the transported defect therefore does not constitute a new arithmetic algorithm in itself.

What the cone/staircase framework contributes is the geometric realization:

- q is the height of a horizontal quotient run;
- \(R_q-k\) is its horizontal endpoint drift from the starting column;
- \(r\bmod q\) is its terminal squared shell defect;
- r=0 is exact contact with \(Y^2=n\).

Thus Euclidean division is encoded directly in the geometry of quotient-run transport.

---

## 5. Relation to two-step floor closure

From v13.311-v13.312,

\[
q_q-k=\left\lfloor\frac rq\right\rfloor.
\]

Therefore

\[
q_q=k
\iff
r<q.
\]

This splits into two subcases:

\[
\boxed{r=0}
\]

for a true divisor contact, and

\[
\boxed{0<r<q}
\]

for a stable off-shell closure.

Hence two-step floor closure has an exact defect refinement:

\[
\boxed{
q_q=k
\iff
\Delta_k<q_k,
}
\]

while

\[
\boxed{
k\mid n
\iff
\Delta_k=0.
}
\]

The defect distinguishes genuine factor symmetry from apparent coordinate closure.

---

## 6. Geometric reading

On a quotient run of height q,

\[
\Delta_k=n-kq
\]

falls with slope -q. The endpoint is reached after

\[
R_q-k=\left\lfloor\frac{\Delta_k}{q}\right\rfloor
\]

horizontal steps, leaving residual defect

\[
\Delta_{R_q}=\Delta_k\bmod q.
\]

Thus one can read Euclidean division directly from the ramp:

\[
\boxed{
\Delta_k
=q\times(\text{number of horizontal steps})
+\text{terminal defect}.
}
\]

The stable closure regime 0<\Delta_k<q is exactly the case where the starting vertex already lies in the final incomplete q-sized defect segment, so no horizontal step occurs.

---

## Guardrails

- The descent law is Euclidean division in geometric coordinates, not a new factoring algorithm.
- Stable two-step closure with positive defect is not a divisor criterion.
- Exact factor exchange remains the r=0 contact stratum.
- No global involution of the staircase is implied.
- This structure is independent of the V4 character transform, though both act on the same shell-defect field.

## Interpretation

The quotient-block geometry resolves off-shell factor exchange into three exact dynamical strata: contact, stable positive-defect closure, and strict Euclidean descent. This gives a clean geometric classification of the failure of factor symmetry without overstating the arithmetic content.