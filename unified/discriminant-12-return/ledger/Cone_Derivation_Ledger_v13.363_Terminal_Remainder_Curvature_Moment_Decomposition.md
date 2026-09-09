# Cone Derivation Ledger v13.363 — Terminal Remainder / Curvature Moment Decomposition

## Scope

This checkpoint combines the full defect-moment hierarchy with the mixed-curvature endpoint-strip identity of v13.362.

The main exact statement is that every quotient-block shell defect splits into:

\[
\boxed{
\text{terminal Euclidean remainder}
+
\text{accumulated mixed-curvature transport}.
}
\]

This is a content decomposition of each defect value, distinct from the earlier carrier decomposition into terminal boundary versus strict-descent interior.

Companion note:

`research-notes/Terminal_Remainder_Curvature_Moment_Decomposition.md`

No new divisor asymptotic, primality theorem, factorization algorithm, RH/GRH, spectral, positivity, or Fredholm claim is made.

---

## 1. Local defect content

For a quotient block

\[
B_q=[L_q,R_q],
\qquad
m_q=R_q-L_q+1,
\]

set

\[
s_q=n-qR_q=n\bmod q.
\]

For every \(k\in B_q\),

\[
\boxed{
\Delta_k=s_q+q(R_q-k).
}
\]

Define

\[
\boxed{C_{k,q}:=q(R_q-k).}
\]

Then

\[
\boxed{\Delta_k=s_q+C_{k,q}.}
\]

By v13.362,

\[
\boxed{
C_{k,q}
=
\sum_{C\subset[k,R_q]\times[0,q]}
\Delta_u\Delta_v(Y^2),
\qquad Y^2=uv.
}
\]

Thus the Euclidean quotient part of the defect is exactly accumulated discrete mixed curvature.

---

## 2. Raw block defect

Summing over the block,

\[
\boxed{
\sum_{k=L_q}^{R_q}\Delta_k
=
m_qs_q+q\binom{m_q}{2}.
}
\]

Hence

\[
\boxed{
\text{raw block defect}
=
\text{terminal remainder mass}
+
\text{triangular curvature transport}.
}
\]

The curvature term is precisely the accumulated endpoint-strip quantity of v13.362.

---

## 3. Normalized first moment

Let

\[
\Delta H_q:=H_{R_q}-H_{L_q-1}.
\]

Then

\[
E_q(n)
=
\sum_{k=L_q}^{R_q}\frac{\Delta_k}{k}
\]

splits as

\[
\boxed{
E_q(n)
=
s_q\Delta H_q
+
q\sum_{k=L_q}^{R_q}\frac{R_q-k}{k}.
}
\]

Since

\[
\sum_{k=L_q}^{R_q}\frac{R_q-k}{k}
=R_q\Delta H_q-m_q,
\]

we obtain

\[
\boxed{
E_q(n)
=
s_q\Delta H_q
+
qR_q\Delta H_q-qm_q.
}
\]

Using \(s_q+qR_q=n\),

\[
\boxed{
E_q(n)
=n\Delta H_q-qm_q,
}
\]

recovering the classical quotient-block first-moment formula.

The new content is therefore not the final closed form, but its exact remainder-versus-curvature resolution.

---

## 4. Transverse to boundary/interior

The earlier v13.316-v13.319 split is a partition of carriers:

\[
\boxed{
\text{terminal endpoint column}
\oplus
\text{strict-descent interior columns}.
}
\]

The present split is a decomposition of values at every carrier:

\[
\boxed{
\Delta_k
=
\text{terminal remainder content}
+
\text{curvature transport content}.
}
\]

These are different axes.

At \(k=R_q\), curvature transport is zero and only \(s_q\) remains. At \(k<R_q\), the column may carry both remainder and curvature content.

---

## 5. Positive real moments

For all \(\alpha>0\),

\[
\boxed{
\mathcal S_{\alpha,q}(n)
=
\sum_{k=L_q}^{R_q}
\left(\frac{s_q+C_{k,q}}{k}\right)^\alpha.
}
\]

This is the exact remainder-curvature representation for the full positive real moment family.

For noninteger \(\alpha\), no finite additive binomial decomposition is claimed in general.

---

## 6. Positive integer moments

For integer \(m\ge1\), the binomial theorem gives

\[
\boxed{
\mathcal S_{m,q}(n)
=
\sum_{r=0}^{m}
{m\choose r}
 s_q^{m-r}q^r
\sum_{k=L_q}^{R_q}
\frac{(R_q-k)^r}{k^m}.
}
\]

Define

\[
\boxed{
\mathcal K_{m,r,q}(n)
:=
q^r\sum_{k=L_q}^{R_q}
\frac{(R_q-k)^r}{k^m}.
}
\]

Then

\[
\boxed{
\mathcal S_{m,q}(n)
=
\sum_{r=0}^{m}{m\choose r}s_q^{m-r}\mathcal K_{m,r,q}(n).
}
\]

The \(r=0\) term is pure remainder content. The terms \(r\ge1\) carry increasing powers of curvature transport.

---

## 7. Generalized-harmonic closure

Expand

\[
(R_q-k)^r
=
\sum_{j=0}^{r}{r\choose j}R_q^{r-j}(-k)^j.
\]

Therefore

\[
\boxed{
\mathcal K_{m,r,q}(n)
=
q^r
\sum_{j=0}^{r}
{r\choose j}R_q^{r-j}(-1)^j
\left(
H_{R_q}^{(m-j)}-H_{L_q-1}^{(m-j)}
\right).
}
\]

Because \(j\le r\le m\), every order \(m-j\) is nonnegative.

Thus the integer moment family has a finite exact three-way representation in:

\[
\boxed{
\text{terminal remainder powers}
\leftrightarrow
\text{curvature-distance powers}
\leftrightarrow
\text{generalized harmonic sums}.
}
\]

---

## 8. Second moment channels

For \(m=2\),

\[
\mathcal S_{2,q}
=
\underbrace{s_q^2\sum_{k=L_q}^{R_q}k^{-2}}_{\text{pure remainder}}
+
\underbrace{2s_qq\sum_{k=L_q}^{R_q}\frac{R_q-k}{k^2}}_{\text{mixed remainder-curvature}}
+
\underbrace{q^2\sum_{k=L_q}^{R_q}\frac{(R_q-k)^2}{k^2}}_{\text{pure curvature-square}}.
\]

So higher moments naturally resolve into pure remainder, mixed, and pure curvature channels.

---

## 9. Quarter-shift normalization

For unit lattice spacing, each elementary cell has

\[
\Delta_u\Delta_v(Y^2)=1,
\qquad
M_F^2=\frac14.
\]

Hence

\[
\boxed{
C_{k,q}
=4\sum_{C\subset[k,R_q]\times[0,q]}M_F^2.
}
\]

The integer defect moments can therefore be read as polynomials in terminal Euclidean remainder and accumulated normalized local quarter-mode content.

This remains a local mixed-difference statement and does not identify the local four-cell V4 carrier with global mod-12 residue characters.

---

## 10. Two-axis organization

The defect field now has two exact independent resolutions:

\[
\boxed{
\textbf{carrier axis:}
\quad
\text{terminal boundary}\oplus\text{strict-descent interior},
}
\]

and

\[
\boxed{
\textbf{content axis:}
\quad
\text{terminal remainder}+\text{mixed-curvature transport}.
}
\]

The carrier axis answers **where** the defect contribution sits.

The content axis answers **what** the defect value is composed of.

Together they organize the full positive moment hierarchy without conflating the endpoint geometry with the Euclidean remainder content.

---

## Relation to prior checkpoints

- v13.312-v13.313: Euclidean transport and defect descent.
- v13.314-v13.315: contact/stable/descent carrier counts and hyperbola boundary.
- v13.316-v13.319: boundary/interior moment hierarchy and V4 character commutation.
- v13.362: defect loss equals accumulated mixed curvature; local quarter mode is one-fourth of raw mixed difference.
- v13.363: every defect value and every integer moment is resolved into terminal remainder content plus mixed-curvature transport content.

---

## Guardrails

- This is an exact reorganization of Euclidean division and finite differences, not a new factoring algorithm.
- Do not identify propagated remainder content with the single terminal boundary endpoint contribution.
- For noninteger moments, retain the nonlinear exact expression; no finite binomial expansion is asserted.
- The quarter shift is only the normalized local mixed-curvature invariant.
- Local V4/Walsh cell labels remain distinct from global mod-12 residue characters.
- No new divisor asymptotic, prime criterion, or RH/GRH conclusion follows.

## Interpretation

The quotient-block defect is now resolved at two levels simultaneously. Geometry partitions the staircase into terminal versus descent carriers, while Euclidean transport decomposes the value at each carrier into a terminal remainder baseline plus accumulated local mixed curvature. The full integer moment hierarchy is therefore a finite polynomial coupling of these two contents, closed explicitly by generalized harmonic sums.