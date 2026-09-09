# Terminal Remainder / Curvature Moment Decomposition

## Scope

This note combines the quotient-block defect-moment hierarchy with the mixed-curvature endpoint-strip identity.

For each quotient block, every shell defect splits exactly into two pieces:

1. the common terminal Euclidean remainder carried by the block endpoint;
2. accumulated discrete mixed curvature between the column and that endpoint.

This is a second decomposition, transverse to the earlier terminal-boundary / strict-descent-interior split.

No new divisor-problem asymptotic, primality theorem, factorization algorithm, RH/GRH, spectral, positivity, or Fredholm claim is made.

---

## 1. Exact local decomposition

Fix n and a quotient block

\[
B_q=[L_q,R_q],
\qquad
L_q=\left\lfloor\frac{n}{q+1}\right\rfloor+1,
\qquad
R_q=\left\lfloor\frac nq\right\rfloor.
\]

Let

\[
m_q=R_q-L_q+1,
\qquad
s_q=n-qR_q=n\bmod q.
\]

For k in the block,

\[
\Delta_k=n-qk.
\]

Using the endpoint defect \(\Delta_{R_q}=s_q\),

\[
\boxed{
\Delta_k=s_q+q(R_q-k).
}
\]

Define the curvature-transport content

\[
\boxed{
C_{k,q}:=q(R_q-k).
}
\]

Then

\[
\boxed{
\Delta_k=s_q+C_{k,q}.
}
\]

By the mixed-curvature strip identity for \(Y^2=uv\),

\[
\boxed{
C_{k,q}
=
\sum_{C\subset [k,R_q]\times[0,q]}
\Delta_u\Delta_v(Y^2).
}
\]

Thus every defect is exactly terminal remainder plus accumulated local mixed curvature.

---

## 2. Raw block defect

Summing unnormalized defects over the block gives

\[
\sum_{k=L_q}^{R_q}\Delta_k
=
m_q s_q
+
q\sum_{k=L_q}^{R_q}(R_q-k).
\]

Hence

\[
\boxed{
\sum_{k=L_q}^{R_q}\Delta_k
=
m_q s_q
+
q\binom{m_q}{2}.
}
\]

This is the cleanest additive form:

\[
\boxed{
\text{raw block defect}
=
\text{terminal remainder mass}
+
\text{triangular mixed-curvature transport}.
}
\]

The second term is exactly the v13.362 accumulated endpoint-strip curvature.

---

## 3. Normalized first moment

The harmonic defect contribution of block q is

\[
E_q(n)
=
\sum_{k=L_q}^{R_q}\frac{\Delta_k}{k}.
\]

Substitute \(\Delta_k=s_q+C_{k,q}\):

\[
\boxed{
E_q(n)
=
R_q^{(1)}(n)+K_q^{(1)}(n),
}
\]

where the propagated-remainder term is

\[
\boxed{
R_q^{(1)}(n)
=
s_q\left(H_{R_q}-H_{L_q-1}\right),
}
\]

and the normalized curvature-transport term is

\[
\boxed{
K_q^{(1)}(n)
=
q\sum_{k=L_q}^{R_q}\frac{R_q-k}{k}.
}
\]

Since

\[
\sum_{k=L_q}^{R_q}\frac{R_q-k}{k}
=
R_q\left(H_{R_q}-H_{L_q-1}\right)-m_q,
\]

we get

\[
\boxed{
K_q^{(1)}(n)
=
qR_q\left(H_{R_q}-H_{L_q-1}\right)-qm_q.
}
\]

Therefore

\[
\boxed{
E_q(n)
=
(s_q+qR_q)\left(H_{R_q}-H_{L_q-1}\right)-qm_q.
}
\]

Using \(s_q+qR_q=n\),

\[
\boxed{
E_q(n)
=
n\left(H_{R_q}-H_{L_q-1}\right)-qm_q,
}
\]

recovering the earlier quotient-block harmonic formula exactly.

---

## 4. Distinction from the boundary/interior split

This decomposition must not be confused with v13.316-v13.318.

Boundary/interior split:

\[
\text{one endpoint column}
\quad\oplus\quad
\text{all nonterminal columns}.
\]

Remainder/curvature split:

\[
\boxed{
\Delta_k
=
\underbrace{s_q}_{\text{common endpoint remainder content}}
+
\underbrace{q(R_q-k)}_{\text{curvature transport content}}
}
\]

at every column in the block.

Thus the two resolutions are transverse rather than identical.

At the endpoint \(k=R_q\), curvature transport vanishes and only the terminal remainder survives. At earlier columns, both pieces may be present.

---

## 5. Positive real moments

For \(\alpha>0\),

\[
\boxed{
\mathcal S_{\alpha,q}(n)
=
\sum_{k=L_q}^{R_q}
\left(
\frac{s_q+C_{k,q}}{k}
\right)^\alpha.
}
\]

This is already an exact remainder-curvature representation for every positive real moment.

For noninteger \(\alpha\), no finite additive binomial decomposition is asserted in general.

---

## 6. Positive integer moments

For integer \(m\ge1\), the binomial theorem yields a finite exact decomposition:

\[
\boxed{
\mathcal S_{m,q}(n)
=
\sum_{r=0}^{m}
{m\choose r}
 s_q^{m-r}
 q^r
\sum_{k=L_q}^{R_q}
\frac{(R_q-k)^r}{k^m}.
}
\]

Define the curvature-distance moments

\[
\boxed{
\mathcal K_{m,r,q}(n)
:=
q^r
\sum_{k=L_q}^{R_q}
\frac{(R_q-k)^r}{k^m}.
}
\]

Then

\[
\boxed{
\mathcal S_{m,q}(n)
=
\sum_{r=0}^{m}
{m\choose r}s_q^{m-r}\mathcal K_{m,r,q}(n).
}
\]

Here \(r=0\) is pure terminal-remainder content, while \(r\ge1\) contains one or more powers of accumulated curvature transport.

---

## 7. Generalized-harmonic closure

Expand

\[
(R_q-k)^r
=
\sum_{j=0}^{r}
{r\choose j}R_q^{r-j}(-k)^j.
\]

Hence

\[
\boxed{
\mathcal K_{m,r,q}(n)
=
q^r
\sum_{j=0}^{r}
{r\choose j}
R_q^{r-j}(-1)^j
\left(
H_{R_q}^{(m-j)}-H_{L_q-1}^{(m-j)}
\right).
}
\]

Because \(0\le j\le r\le m\), only generalized harmonic orders \(m-j\ge0\) occur.

Therefore every positive integer defect moment has an exact finite expansion simultaneously in:

- powers of terminal Euclidean remainder \(s_q\);
- powers of accumulated mixed-curvature distance \(q(R_q-k)\);
- generalized harmonic block sums.

---

## 8. First two integer cases

For \(m=1\),

\[
\mathcal S_{1,q}
=
s_q\Delta H_q
+
q\left(R_q\Delta H_q-m_q\right),
\]

where

\[
\Delta H_q=H_{R_q}-H_{L_q-1}.
\]

For \(m=2\),

\[
\mathcal S_{2,q}
=
s_q^2\Delta H_q^{(2)}
+2s_qq
\sum_{k=L_q}^{R_q}\frac{R_q-k}{k^2}
+q^2
\sum_{k=L_q}^{R_q}\frac{(R_q-k)^2}{k^2}.
\]

So the second moment resolves into pure remainder, mixed remainder-curvature, and pure curvature-square channels.

---

## 9. Quarter-shift normalization

For unit lattice spacing, v13.362 gives one raw mixed-curvature unit per elementary factor cell and normalized local V4/Walsh mixed coefficient

\[
M_F^2=\frac14.
\]

Thus

\[
C_{k,q}=4\sum_{C\subset[k,R_q]\times[0,q]}M_F^2.
\]

Therefore the integer moment hierarchy may equivalently be viewed as a polynomial in terminal remainder and accumulated local quarter-mode content.

This does not identify the local four-cell V4 carrier with global mod-12 characters.

---

## 10. Structural synthesis

The defect field now carries two exact resolutions:

\[
\boxed{
\text{carrier resolution:}
\quad
\text{terminal boundary}\oplus\text{strict-descent interior},
}
\]

and

\[
\boxed{
\text{content resolution:}
\quad
\text{terminal remainder}+\text{mixed-curvature transport}.
}
\]

The first partitions columns. The second decomposes the defect value at each column.

Together they provide a two-axis organization of the full defect-moment hierarchy.

---

## Guardrails

- The remainder/curvature split is exact Euclidean division plus mixed finite differences; it is not a new factoring algorithm.
- Do not confuse propagated remainder content with the single terminal endpoint contribution of the boundary/interior split.
- For noninteger positive moments, retain the exact nonlinear form; no finite binomial split is claimed.
- The quarter shift enters only through normalized local mixed curvature.
- Local four-cell V4/Walsh and global mod-12 V4 characters remain distinct carriers.
- No new divisor asymptotic or prime criterion is implied.
