# Cone Derivation Ledger v13.364 — Casimir / Mixed-Curvature Quarter-Shift Unification

## Scope

This checkpoint closes the exact loop between the local factor-cell mixed difference, normalized V4/Walsh quarter mode, null-diamond midpoint norm, oscillator Casimir completion, and divisor-shell Euclidean transport.

Companion note:

`research-notes/Casimir_Mixed_Curvature_Quarter_Shift_Unification.md`

No causal identification between arithmetic and operator constructions is claimed. The result is equality of exact centered invariants across distinct carriers.

---

## 1. Raw mixed curvature and normalized quarter mode

For lattice spacing \(\delta\),

\[
F(u,v)=uv
\]

satisfies on every elementary cell

\[
\boxed{
F_{11}-F_{10}-F_{01}+F_{00}=\delta^2.
}
\]

The normalized checkerboard V4/Walsh coefficient is therefore

\[
\boxed{
\widehat F_{\chi_{11}}
=\frac14(F_{00}-F_{10}-F_{01}+F_{11})
=\frac{\delta^2}{4}.
}
\]

Define

\[
\boxed{M_F^2:=\delta^2/4.}
\]

Hence

\[
\boxed{\Delta_u\Delta_v(uv)=4M_F^2.}
\]

---

## 2. Null-diamond identification

The null-diamond midpoint norm satisfies

\[
M_F^2=\frac{\Delta^2}{4}.
\]

For primitive spacing \(|\Delta|=\delta\),

\[
\boxed{M_F^2=\frac{\delta^2}{4}.}
\]

Thus the normalized mixed cell mode and null-diamond midpoint norm are equal exact invariants.

---

## 3. Casimir completion

The centered quadratic identity is

\[
q(q+\delta)
=\left(q+\frac\delta2\right)^2-\frac{\delta^2}{4}.
\]

Therefore the Casimir correction is exactly \(M_F^2\).

For unit spacing in the two-oscillator SU(2) realization,

\[
C=j(j+1),
\qquad T_c=j+\frac12,
\]

so

\[
\boxed{T_c^2=C+M_F^2}
\]

and

\[
\boxed{C=T_c^2-M_F^2.}
\]

Using the four-corner mixed coefficient,

\[
\boxed{
C
=T_c^2-rac14(F_{00}-F_{10}-F_{01}+F_{11}).
}
\]

At unit spacing for \(F=uv\), this is \(C=T_c^2-1/4\).

---

## 4. Oscillator transition-cell form

With

\[
F_{00}=K_-^2,
\quad F_{10}=J_+^2,
\quad F_{01}=J_-^2,
\quad F_{11}=K_+^2,
\]

we have

\[
\boxed{
K_-^2+K_+^2-J_+^2-J_-^2
=\delta^2
=4M_F^2.
}
\]

Thus the oscillator transition cell carries the same raw mixed invariant as the elementary factor cell.

---

## 5. Divisor-shell accumulation

For quotient block height \(q\) and endpoint \(R_q\), v13.362 gives

\[
\Delta_k-\Delta_{R_q}=q(R_q-k).
\]

Since the endpoint strip contains exactly \(q(R_q-k)\) elementary unit cells,

\[
\boxed{
\Delta_k-\Delta_{R_q}
=\sum_{C\subset\mathcal R_{k,q}}\Delta_u\Delta_v(Y^2)
=4\sum_{C\subset\mathcal R_{k,q}}M_F^2.
}
\]

Hence the same local quarter invariant that completes the Casimir also accumulates over Euclidean shell-defect transport.

---

## 6. Unified exact chain

The invariant chain is

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

The Casimir and divisor-shell realizations are then

\[
\boxed{C=T_c^2-M_F^2}
\]

and

\[
\boxed{
\Delta_k-\Delta_{R_q}
=4\sum M_F^2.
}
\]

Therefore the Casimir quarter shift, null-diamond midpoint norm, and normalized factor-cell mixed curvature are exact realizations of the same centered four-corner invariant.

---

## 7. Carrier discipline

The carriers remain distinct:

- elementary factor-cell corners;
- oscillator transition cell / null diamond;
- divisor-staircase endpoint strip;
- global mod-12 residue characters.

Only the first three are tied here by the same local mixed invariant. The global mod-12 V4 channels remain a separate arithmetic projection on column residues.

---

## Guardrails

- Equality of invariants does not imply that divisor geometry causes the Casimir or vice versa.
- Local V4/Walsh and global mod-12 V4 carriers are not identified.
- The \(1/4\) is the normalized half-step centered quadratic scale \(\delta^2/4\).
- General spacing scales every occurrence to \(\delta^2/4\).
- No new spectral theorem, divisor asymptotic, primality criterion, or factorization algorithm follows.

## Interpretation

The quarter shift is no longer an isolated numerical recurrence across the project. It is the normalized local mixed-curvature invariant of one lattice cell, simultaneously realized as the null-diamond midpoint norm and the oscillator Casimir centering correction, and accumulated geometrically by Euclidean divisor-shell transport.
