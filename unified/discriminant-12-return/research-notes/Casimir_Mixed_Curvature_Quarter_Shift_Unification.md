# Casimir, Mixed Curvature, and the Quarter-Shift Invariant

## Scope

This note formalizes the exact identity chain connecting the elementary factor-cell mixed difference, the normalized four-corner V4/Walsh quarter mode, the null-diamond midpoint norm, the oscillator Casimir completion, and the Euclidean divisor-shell transport developed in v13.362-v13.363.

The result is an equivalence of exact invariants. It does **not** assert that divisor geometry causes the oscillator Casimir, or conversely.

---

## 1. Elementary factor-cell mixed curvature

For lattice spacing \(\delta\), let

\[
F(u,v)=uv.
\]

Across one elementary cell with corners

\[
(u,v),\ (u+\delta,v),\ (u,v+\delta),\ (u+\delta,v+\delta),
\]

the mixed finite difference is

\[
\boxed{
\Delta_u\Delta_v F
=F_{11}-F_{10}-F_{01}+F_{00}
=\delta^2.
}
\]

For unit spacing, this is \(1\).

---

## 2. Normalized four-corner V4/Walsh mixed channel

Using the normalized Hadamard/V4 coefficient on the checkerboard character,

\[
\widehat F_{\chi_{11}}
=\frac14(F_{00}-F_{10}-F_{01}+F_{11}),
\]

we obtain

\[
\boxed{
\widehat F_{\chi_{11}}=\frac{\delta^2}{4}.
}
\]

Define

\[
\boxed{M_F^2:=\frac{\delta^2}{4}.}
\]

Hence

\[
\boxed{
\Delta_u\Delta_v(uv)=4M_F^2.
}
\]

---

## 3. Null-diamond midpoint norm

For two null spinors with determinant \(\Delta\), the Lorentz midpoint satisfies

\[
M_F^2=\frac{\Delta^2}{4}.
\]

For primitive spacing \(|\Delta|=\delta\),

\[
\boxed{M_F^2=\frac{\delta^2}{4}.}
\]

Thus the null-diamond midpoint invariant equals the normalized mixed four-corner coefficient of an elementary factor cell.

---

## 4. Casimir completion

The centered quadratic completion is

\[
q(q+\delta)
=\left(q+\frac\delta2\right)^2-\frac{\delta^2}{4}.
\]

Therefore the universal quarter term is exactly

\[
\boxed{\frac{\delta^2}{4}=M_F^2.}
\]

For the two-oscillator SU(2) realization with unit spacing,

\[
C=j(j+1),
\qquad
T_c=j+\frac12,
\]

so

\[
\boxed{
T_c^2=C+M_F^2
}
\]

and therefore

\[
\boxed{
C=T_c^2-M_F^2.
}
\]

Using the four-corner formula,

\[
\boxed{
C
=T_c^2-rac14(F_{00}-F_{10}-F_{01}+F_{11}).
}
\]

For \(F=uv\), the bracket is \(1\) at unit spacing, recovering

\[
C=T_c^2-\frac14.
\]

---

## 5. Relation to the oscillator transition cell

For the four transition amplitudes

\[
F_{00}=K_-^2,\quad
F_{10}=J_+^2,\quad
F_{01}=J_-^2,\quad
F_{11}=K_+^2,
\]

the exact identity is

\[
\boxed{
K_-^2+K_+^2-J_+^2-J_-^2
=\delta^2
=4M_F^2.
}
\]

Thus the oscillator transition cell carries the same raw mixed invariant as the elementary factor cell.

---

## 6. Euclidean divisor-shell transport

From v13.362, for a quotient block height \(q\) and endpoint \(R_q\),

\[
\Delta_k-\Delta_{R_q}=q(R_q-k).
\]

The right side counts elementary unit cells in the endpoint strip, hence

\[
\boxed{
\Delta_k-\Delta_{R_q}
=\sum_{C\subset\mathcal R_{k,q}}\Delta_u\Delta_v(Y^2).
}
\]

Since every cell contributes \(4M_F^2\),

\[
\boxed{
\Delta_k-\Delta_{R_q}
=4\sum_{C\subset\mathcal R_{k,q}}M_F^2.
}
\]

So the same local quarter invariant that completes the Casimir accumulates over divisor-shell transport strips.

---

## 7. Exact identity chain

The unification can be summarized as

\[
\boxed{
\Delta_u\Delta_v(uv)
=\delta^2
=4M_F^2
}
\]

with

\[
\boxed{
M_F^2
=\widehat F_{\chi_{11}}
=\frac{\Delta^2}{4}
=\frac{\delta^2}{4}.
}
\]

The same invariant then appears in the Casimir completion

\[
\boxed{
C=T_c^2-M_F^2
}
\]

and in accumulated Euclidean shell-defect reduction

\[
\boxed{
\Delta_k-\Delta_{R_q}
=4\sum M_F^2.
}
\]

Hence the local mixed-curvature quarter mode, the null-diamond midpoint norm, and the oscillator Casimir shift are exact realizations of the same centered four-corner invariant.

---

## 8. Structural interpretation

There are three distinct carriers:

1. elementary factor-cell corners;
2. null-diamond / oscillator transition geometry;
3. divisor-staircase endpoint strips.

They should not be identified literally. What is common is the invariant

\[
\boxed{M_F^2=\delta^2/4}
\]

and the mixed-difference operation that produces it after normalization.

Thus the correct statement is not

> divisor geometry causes the Casimir quarter shift,

but rather

> the Casimir quarter shift, null-diamond midpoint norm, and normalized factor-cell mixed curvature realize the same exact centered quadratic invariant.

---

## Guardrails

- Equality of invariants does not establish causal derivation between physical/operator and arithmetic carriers.
- Local V4/Walsh cell labels remain distinct from global mod-12 Dirichlet-character channels.
- The factor \(1/4\) comes from centering by half a lattice step and normalized four-point averaging.
- At general spacing, every quarter shift scales as \(\delta^2/4\).
- No new spectral theorem, divisor asymptotic, primality criterion, or factorization method is claimed.
