# Centered Cone Closure from the V4 Rank-One Quarter Mode

## Scope

This note sharpens the v13.364 Casimir/mixed-curvature quarter-shift synthesis by showing that the same local quarter invariant closes the centered cone identity itself in V4/Walsh coordinates.

The result is exact. It does not claim that divisor geometry causes the oscillator Casimir, nor that the local V4 carrier is identical to the global mod-12 residue carrier.

---

## 1. Four transition-product values

For a lattice cell with spacing \(\delta\) and lower-left occupation labels \((p,q)\), define

\[
F_{00}=\delta^2pq,\qquad
F_{10}=\delta^2(p+1)q,
\]

\[
F_{01}=\delta^2p(q+1),\qquad
F_{11}=\delta^2(p+1)(q+1).
\]

These are the squared transition amplitudes

\[
F_{00}=K_-^2,\quad F_{10}=J_+^2,\quad F_{01}=J_-^2,\quad F_{11}=K_+^2.
\]

Define normalized V4/Walsh coefficients

\[
\widehat F_{\chi_0}=\frac14(F_{00}+F_{10}+F_{01}+F_{11}),
\]

\[
\widehat F_{\chi_5}=\frac14(F_{00}+F_{10}-F_{01}-F_{11}),
\]

\[
\widehat F_{\chi_7}=\frac14(F_{00}-F_{10}+F_{01}-F_{11}),
\]

\[
\widehat F_{\chi_{11}}=\frac14(F_{00}-F_{10}-F_{01}+F_{11}).
\]

Earlier work gives

\[
\boxed{\widehat F_{\chi_0}=Y_c^2,}
\]

\[
\boxed{\widehat F_{\chi_5}=-\frac{\delta}{2}v_c,\qquad
\widehat F_{\chi_7}=-\frac{\delta}{2}u_c,}
\]

and

\[
\boxed{\widehat F_{\chi_{11}}=M_F^2=\frac{\delta^2}{4}.}
\]

---

## 2. Rank-one determinant identity in Walsh coordinates

The raw four-corner products satisfy

\[
F_{00}F_{11}=F_{10}F_{01}.
\]

Equivalently, the \(2\times2\) product table has determinant zero.

In normalized Walsh coordinates this becomes

\[
\boxed{
\widehat F_{\chi_0}\widehat F_{\chi_{11}}
=
\widehat F_{\chi_5}\widehat F_{\chi_7}.
}
\]

Substituting the geometric values gives

\[
Y_c^2\,M_F^2
=
\left(-\frac{\delta v_c}{2}\right)
\left(-\frac{\delta u_c}{2}\right)
=
\frac{\delta^2}{4}u_cv_c.
\]

Since \(u_cv_c=Y_c^2\), this is exact.

The quarter mode is therefore not merely an additive correction: in the local Fourier coordinates it is the mixed coefficient required by the rank-one product constraint.

---

## 3. Cone coordinates from Walsh coefficients

The centered cone coordinates are recovered from the two first-order Walsh modes by

\[
\boxed{
T_c=-\frac{\widehat F_{\chi_5}+\widehat F_{\chi_7}}{\delta},
}
\]

\[
\boxed{
X_c=\frac{\widehat F_{\chi_5}-\widehat F_{\chi_7}}{\delta}.
}
\]

Therefore

\[
T_c^2-X_c^2
=
\frac{(\widehat F_{\chi_5}+\widehat F_{\chi_7})^2-(\widehat F_{\chi_5}-\widehat F_{\chi_7})^2}{\delta^2}
\]

\[
=
\frac{4\widehat F_{\chi_5}\widehat F_{\chi_7}}{\delta^2}.
\]

Using the rank-one Walsh identity,

\[
T_c^2-X_c^2
=
\frac{4\widehat F_{\chi_0}\widehat F_{\chi_{11}}}{\delta^2}.
\]

With

\[
\widehat F_{\chi_0}=Y_c^2,
\qquad
\widehat F_{\chi_{11}}=\frac{\delta^2}{4},
\]

we obtain

\[
\boxed{T_c^2-X_c^2=Y_c^2.}
\]

Hence

\[
\boxed{T_c^2-X_c^2-Y_c^2=0.}
\]

This is the centered cone equation recovered entirely from the four local transition amplitudes in V4/Walsh coordinates.

---

## 4. The quarter mode as the cone-closure coefficient

The previous derivation may be written

\[
T_c^2-X_c^2
=
\frac{4Y_c^2M_F^2}{\delta^2}.
\]

Thus cone closure requires

\[
\frac{4M_F^2}{\delta^2}=1.
\]

But the elementary mixed-curvature identity gives exactly

\[
\boxed{M_F^2=\frac{\delta^2}{4}.}
\]

Therefore the same local quarter invariant identified in v13.364 is precisely the normalized coefficient converting the product-table rank-one relation into the null-cone equation.

This should be read as an equivalence of exact identities, not as an independent derivation of the quarter value from the cone alone.

---

## 5. Casimir closure

Let

\[
j=\frac{p+q}{2},\qquad m=\frac{p-q}{2}.
\]

Then

\[
T_c=\delta\left(j+\frac12\right),\qquad X_c=\delta m.
\]

With the SU(2) Casimir

\[
C=\delta^2j(j+1),
\]

we have

\[
\boxed{T_c^2=C+M_F^2.}
\]

The cone identity gives

\[
Y_c^2=T_c^2-X_c^2,
\]

hence

\[
\boxed{Y_c^2-M_F^2=C-X_c^2.}
\]

Equivalently,

\[
\boxed{
T_c^2-M_F^2
=
X_c^2+(Y_c^2-M_F^2)
=C.
}
\]

Thus the same quarter mode simultaneously:

- closes the local V4 rank-one relation into the null cone;
- supplies the centered Casimir completion;
- equals the null-diamond midpoint norm;
- equals the normalized elementary mixed curvature.

---

## 6. Operator form

Earlier oscillator identities give

\[
\frac12(J_+^2+J_-^2)
=Y_c^2-M_F^2
=\delta^2\bigl(j(j+1)-m^2\bigr).
\]

Therefore

\[
\boxed{
T_c^2-M_F^2
=
X_c^2+rac12(J_+^2+J_-^2).
}
\]

This is the transition-amplitude realization of

\[
J^2=J_z^2+(J_x^2+J_y^2).
\]

The quarter term is the centering correction that makes the discrete transition cell match the usual Casimir decomposition.

---

## 7. Global divisor-shell connection

From v13.362,

\[
\Delta_k-\Delta_{R_q}
=4\sum_{C\subset\mathcal R_{k,q}}M_F^2.
\]

Hence the same local cone-closure coefficient accumulates over endpoint strips to produce Euclidean shell-defect reduction.

The exact chain is now

\[
\boxed{
\begin{array}{c}
\text{rank-one product cell}\\
\downarrow\\
\widehat F_{\chi_0}\widehat F_{\chi_{11}}
=\widehat F_{\chi_5}\widehat F_{\chi_7}\\
\downarrow\\
M_F^2=\delta^2/4\\
\downarrow\\
T_c^2-X_c^2-Y_c^2=0\\
\downarrow\\
T_c^2=C+M_F^2\\
\downarrow\\
\Delta_k-\Delta_{R_q}
=4\sum M_F^2.
\end{array}
}
\]

---

## Guardrails

- The four local V4/Walsh labels are cell-position characters, not literal mod-12 residue classes.
- The determinant-zero product table, cone equation, and Casimir completion are equivalent realizations of the same local algebraic structure; no causal ordering is claimed.
- The global divisor-shell strip identity accumulates the same local mixed invariant but does not turn the oscillator cell into a divisor block.
- No new primality theorem, factorization algorithm, divisor asymptotic, RH/GRH, spectral, positivity, or Fredholm claim is made.

## Interpretation

The quarter shift now has a sharper structural role. It is the local mixed Fourier coefficient that makes the four-corner rank-one product cell close exactly onto the centered null cone. The same coefficient is then the Casimir centering correction and the elementary unit accumulated by Euclidean divisor-shell transport.
