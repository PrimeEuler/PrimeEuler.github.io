# Cone Derivation Ledger v13.365 — Centered Cone Closure from the V4 Rank-One Quarter Mode

## Scope

This checkpoint sharpens v13.364 by showing that the same local quarter invariant closes the centered cone equation itself in V4/Walsh coordinates.

Companion note:

`research-notes/Centered_Cone_Closure_from_V4_Rank_One_Quarter_Mode.md`

The main result is exact: the four transition-product values form a rank-one 2x2 table. In normalized Walsh coordinates this rank-one condition is

\[
\widehat F_{\chi_0}\widehat F_{\chi_{11}}
=
\widehat F_{\chi_5}\widehat F_{\chi_7}.
\]

Because \(\widehat F_{\chi_{11}}=M_F^2=\delta^2/4\), this identity is exactly what converts the four local transition amplitudes into the centered null-cone equation.

No causal claim is made between divisor geometry, oscillator Casimir structure, and null-diamond geometry; the statement is equivalence of exact invariants across distinct carriers.

---

## 1. Four local transition values

For cell spacing \(\delta\),

\[
F_{00}=\delta^2pq,
\quad F_{10}=\delta^2(p+1)q,
\quad F_{01}=\delta^2p(q+1),
\quad F_{11}=\delta^2(p+1)(q+1).
\]

These are

\[
F_{00}=K_-^2,\quad
F_{10}=J_+^2,\quad
F_{01}=J_-^2,\quad
F_{11}=K_+^2.
\]

Normalized Walsh coefficients satisfy

\[
\widehat F_{\chi_0}=Y_c^2,
\]

\[
\widehat F_{\chi_5}=-\frac{\delta}{2}v_c,
\qquad
\widehat F_{\chi_7}=-\frac{\delta}{2}u_c,
\]

\[
\widehat F_{\chi_{11}}=M_F^2=\frac{\delta^2}{4}.
\]

---

## 2. Rank-one Walsh identity

The raw product table has determinant zero:

\[
\boxed{F_{00}F_{11}=F_{10}F_{01}.}
\]

In Walsh coordinates this is equivalent to

\[
\boxed{
\widehat F_{\chi_0}\widehat F_{\chi_{11}}
=
\widehat F_{\chi_5}\widehat F_{\chi_7}.
}
\]

Hence

\[
\boxed{Y_c^2M_F^2
=\widehat F_{\chi_5}\widehat F_{\chi_7}.}
\]

The local quarter mode is therefore the mixed coefficient required by the rank-one constraint after V4/Walsh diagonalization.

---

## 3. Cone reconstruction

Recover

\[
T_c=-\frac{\widehat F_{\chi_5}+\widehat F_{\chi_7}}{\delta},
\qquad
X_c=\frac{\widehat F_{\chi_5}-\widehat F_{\chi_7}}{\delta}.
\]

Then

\[
T_c^2-X_c^2
=
\frac{4\widehat F_{\chi_5}\widehat F_{\chi_7}}{\delta^2}.
\]

Using the rank-one identity,

\[
T_c^2-X_c^2
=
\frac{4Y_c^2M_F^2}{\delta^2}.
\]

Since

\[
M_F^2=\frac{\delta^2}{4},
\]

we obtain

\[
\boxed{T_c^2-X_c^2=Y_c^2,}
\]

or

\[
\boxed{T_c^2-X_c^2-Y_c^2=0.}
\]

Thus the centered cone closes directly from the local four-amplitude Walsh data.

---

## 4. Quarter mode as cone-closure coefficient

The preceding equation has the form

\[
T_c^2-X_c^2
=Y_c^2\left(\frac{4M_F^2}{\delta^2}\right).
\]

The elementary mixed-curvature value

\[
\boxed{M_F^2=\delta^2/4}
\]

makes the coefficient exactly one.

This should not be read as an independent derivation of the quarter value from the cone alone. Rather, the determinant-zero product cell, normalized mixed mode, and cone equation are exact equivalent descriptions of the same local structure.

---

## 5. Casimir completion

With

\[
j=\frac{p+q}{2},\qquad m=\frac{p-q}{2},
\]

\[
T_c=\delta\left(j+\frac12\right),
\qquad X_c=\delta m,
\]

and

\[
C=\delta^2j(j+1),
\]

we have

\[
\boxed{T_c^2=C+M_F^2.}
\]

Combining with the cone equation gives

\[
\boxed{Y_c^2-M_F^2=C-X_c^2.}
\]

Therefore

\[
\boxed{
T_c^2-M_F^2
=X_c^2+(Y_c^2-M_F^2)
=C.
}
\]

The local quarter mode therefore simultaneously appears as:

- normalized mixed curvature;
- V4/Walsh mixed coefficient;
- null-diamond midpoint norm;
- Casimir centering correction;
- cone-closure coefficient.

---

## 6. Transition-amplitude form

Earlier identities give

\[
\frac12(J_+^2+J_-^2)
=Y_c^2-M_F^2.
\]

Hence

\[
\boxed{
T_c^2-M_F^2
=X_c^2+rac12(J_+^2+J_-^2).
}
\]

This is the transition-amplitude realization of the standard SU(2) decomposition

\[
J^2=J_z^2+(J_x^2+J_y^2).
\]

---

## 7. Global divisor-shell continuation

From v13.362,

\[
\Delta_k-\Delta_{R_q}
=4\sum_{C\subset\mathcal R_{k,q}}M_F^2.
\]

Thus the same local quarter coefficient that closes the centered cone is accumulated over quotient-block endpoint strips to produce Euclidean shell-defect reduction.

The exact structural chain is

\[
\boxed{
\text{rank-one product cell}
\to
\text{Walsh determinant identity}
\to
M_F^2=\delta^2/4
\to
\text{centered cone closure}
\to
\text{Casimir completion}
\to
\text{global strip accumulation}.
}
\]

This is a chain of equivalent/local-to-global exact relations, not a causal derivation between distinct theories.

---

## Guardrails

- Local V4/Walsh labels are cell-position characters, not literal mod-12 residue classes.
- The four-corner product cell and Farey/null-diamond carrier remain distinct realizations of the same centered quarter invariant.
- The global divisor-shell strip accumulation does not identify a quotient block with an oscillator transition cell.
- No new primality theorem, factorization algorithm, divisor-problem asymptotic, RH/GRH, spectral, positivity, or Fredholm claim is made.

## Interpretation

The quarter shift now has a precise local algebraic role: it is the normalized mixed Walsh coefficient that turns the rank-one four-transition product table into the centered null cone. The same coefficient is the Casimir centering correction and the elementary mixed-curvature unit accumulated by divisor-shell Euclidean transport.
