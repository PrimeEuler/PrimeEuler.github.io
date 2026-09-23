# Cone Derivation Ledger v13.729 — Tate–Weil Interface, Cartan Polynomial, and Theta/Xi Representation Gate

**Date:** 2026-09-23  
**Status:** exact structural checkpoint; proposed Weil-Casimir identification explicitly rejected and replaced by an exact Cartan-generator identity  
**Parent:** v13.726  
**Cross-thread check:** v13.727–728 are Suzuki edge/Wiener–Hopf work and do not collide with this Tate/GL1–theta–representation lane.

## 1. Purpose

After the v13.726 local/global SL2 scattering obstruction, this checkpoint asks where the theta/Mellin object actually lives representation-theoretically.

The answer separates three layers:

1. **Tate GL1:** the completed factor
   \[
   \Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)
   \]
   is the native Euler product of local multiplicative zeta integrals.

2. **Weil/metaplectic theta representation:** the self-dual Gaussian and Poisson summation supply the exact reflection \(s\leftrightarrow1-s\) and the even theta kernel.

3. **Split-Cartan differential polynomial:** the factor
   \[
   s(s-1)=w^2-\frac14
   \]
   is realized exactly by a quadratic polynomial in the dilation generator. It is **not** the central Casimir eigenvalue of the Weil representation.

That last distinction is the decisive result of this gate.

---

## 2. Tate local-global factorization

Let \(\mathbb A=\mathbb A_{\mathbb Q}\), and choose the standard factorizable Schwartz–Bruhat function
\[
\Phi=\Phi_\infty\prod_p\Phi_p
\]
with
\[
\Phi_\infty(x)=e^{-\pi x^2},
\qquad
\Phi_p=\mathbf1_{\mathbb Z_p}.
\]

The global Tate zeta integral for the trivial character is
\[
Z(\Phi,s)
=
\int_{\mathbb A^\times}\Phi(x)|x|_{\mathbb A}^s\,d^\times x
=
Z_\infty(s)\prod_p Z_p(s).
\]

At infinity,
\[
Z_\infty(s)
=
2\int_0^\infty e^{-\pi x^2}x^{s-1}\,dx
=
\boxed{\pi^{-s/2}\Gamma(s/2)}.
\]

At a finite prime, with \(\operatorname{vol}(\mathbb Z_p^\times)=1\),
\[
Z_p(s)
=
\sum_{k\ge0}p^{-ks}
=
\boxed{(1-p^{-s})^{-1}}.
\]

Therefore, for \(\Re s>1\),
\[
\boxed{
Z(\Phi,s)
=
\pi^{-s/2}\Gamma(s/2)\zeta(s)
=
\Lambda(s).
}
\]

Thus the completed zeta factor is native to Tate GL1. No SL2 scattering normalization is needed to manufacture it.

---

## 3. Classical unfolding is the same object

With
\[
\psi(x)=\sum_{n\ge1}e^{-\pi n^2x},
\]
termwise Mellin integration gives
\[
2\int_0^\infty\psi(x)x^{s/2}\frac{dx}{x}
=
2\pi^{-s/2}\Gamma(s/2)\zeta(s)
=
2\Lambda(s).
\]
Hence
\[
\boxed{
\Lambda(s)
=
\int_0^\infty\psi(x)x^{s/2}\frac{dx}{x}.
}
\]
Equivalently, using the convention with the explicit factor 2 on both theta and Mellin sides gives the same identity.

The half-argument \(s/2\) is native: it comes from the quadratic Gaussian \(e^{-\pi x^2}\).

At
\[
s=\frac12+w,
\]
the real local factor is
\[
\pi^{-1/4-w/2}\Gamma(\tfrac14+\tfrac w2),
\]
so the quarter shift that did not arise naturally from the bare SL2 Harish–Chandra c-function is automatic in Tate's model.

---

## 4. Fourier self-duality and the functional equation

With self-dual additive Haar measures,
\[
\widehat{\Phi_\infty}=\Phi_\infty,
\qquad
\widehat{\mathbf1_{\mathbb Z_p}}=\mathbf1_{\mathbb Z_p}.
\]
Thus
\[
\boxed{\widehat\Phi=\Phi.}
\]

Tate's functional equation relates
\[
Z(\Phi,s)
\quad\text{and}\quad
Z(\widehat\Phi,1-s).
\]
For the self-dual standard vector this yields the completed-zeta reflection
\[
\boxed{\Lambda(s)=\Lambda(1-s)}
\]
after the standard meromorphic continuation/pole bookkeeping.

Classically this is Poisson summation:
\[
\vartheta(x)=x^{-1/2}\vartheta(1/x).
\]

With
\[
x=e^{2r},
\]
the inversion \(x\mapsto x^{-1}\) is exactly
\[
r\mapsto-r.
\]
After the usual half-density flattening, this is precisely the evenness
\[
\boxed{K_\theta(-r)=K_\theta(r).}
\]

This explains the failure of the standard SL2 Eisenstein-wave-packet attempt in v13.726: theta requires reflection coefficient \(+1\), and the self-dual Tate/Weil vector has exactly that property. The standard Eisenstein continuous spectrum instead inserts the nonconstant phase \(\phi(1/2+it)\).

---

## 5. Weil/metaplectic lift of the Gaussian

The natural nonabelian lift of the Gaussian is the Schrödinger model of the Weil representation of \(Mp_2(\mathbb R)\) on \(\mathcal S(\mathbb R)\).

The Weyl element acts, up to the conventional metaplectic phase, by Fourier transform:
\[
\omega(w_0)f=\widehat f.
\]
Hence the standard Gaussian
\[
g(x)=e^{-\pi x^2}
\]
is a Weyl eigenvector:
\[
\boxed{\omega(w_0)g=g}
\]
after choosing the standard phase convention.

The split torus acts by dilation/half-density:
\[
(\omega(a)f)(x)
\sim
|a|^{1/2}f(ax)
\]
(up to the metaplectic character convention).

The global theta distribution
\[
\Theta(f)=\sum_{q\in\mathbb Q}f(q)
\]
paired with the adelic standard vector produces the Jacobi theta series. Poisson summation is exactly the Weyl/Fourier invariance of this theta distribution.

Thus the theta object has a genuine metaplectic representation-theoretic lift.

---

## 6. Critical test: is \(s(s-1)\) the Weil Casimir?

No.

The oscillator/Weil representation has a **fixed** infinitesimal character. In the even and odd oscillator sectors, using the standard \(SU(1,1)\) normalization
\[
C=k(k-1),
\]
the Bargmann indices are
\[
k=\frac14,\qquad k=\frac34.
\]
Both give
\[
\boxed{
C_{\rm Weil}
=
-\frac{3}{16}.
}
\]

The Gaussian lies in the even sector. Therefore the central Casimir acts on the irreducible Weil component by the fixed scalar
\[
-\frac{3}{16},
\]
not by the variable polynomial
\[
s(s-1).
\]

Hence the proposed strong identification
\[
\text{“the operator producing }s(s-1)\text{ is literally the Weil/SL2 central Casimir on the theta vector”}
\]
is
\[
\boxed{\textbf{FALSE}.}
\]

This is a useful obstruction: the variable spectral factor cannot come from the central Casimir of one fixed Weil representation.

---

## 7. Exact replacement: the split-Cartan Euler operator

The correct operator is already present inside the split torus.

Let
\[
E_x=x\frac{d}{dx}.
\]
For the Mellin transform
\[
\mathcal M[f](s)
=
\int_0^\infty f(x)x^{s/2}\frac{dx}{x},
\]
integration by parts gives
\[
\boxed{
\mathcal M[E_xf](s)
=
-\frac{s}{2}\mathcal M[f](s)
}
\]
under the usual decay/continuation hypotheses.

Therefore the quadratic Cartan polynomial
\[
\boxed{
Q_A:=4E_x^2+2E_x
}
\]
satisfies
\[
\boxed{
\mathcal M[Q_Af](s)
=
s(s-1)\mathcal M[f](s).
}
\]

This is the exact operator sought.

Now put
\[
x=e^{2r}.
\]
Then
\[
E_x=\frac12\partial_r,
\]
so
\[
\boxed{
Q_A
=
\partial_r^2+\partial_r.
}
\]

But this is exactly the unflattened A-constant-term operator already found in v13.726:
\[
\boxed{Q_A=\mathcal C_A.}
\]

Conjugating by the half-density,
\[
K(r)=e^{r/2}F(r),
\]
gives
\[
\boxed{
e^{r/2}Q_Ae^{-r/2}
=
\partial_r^2-\frac14.
}
\]

Thus the entire quadratic chain closes exactly:
\[
\boxed{
4E_x^2+2E_x
=
\partial_r^2+\partial_r
\xrightarrow{\rho\text{-shift}}
\partial_r^2-\frac14
\xrightarrow{\mathcal M}
s(s-1)=w^2-\frac14.
}
\]

This is stronger and more precise than the rejected Weil-Casimir claim.

---

## 8. Apply the Cartan polynomial to the theta Mellin object

For \(\Re s>1\), the theta Mellin integral converges and integration by parts is legitimate after the standard theta subtraction/unfolding. Therefore
\[
\mathcal M[Q_A\psi](s)
=
s(s-1)\Lambda(s)
\]
with the corresponding convention factor.

Since
\[
\xi(s)=\frac12s(s-1)\Lambda(s),
\]
we obtain
\[
\boxed{
\xi(s)
=
\frac12\,\mathcal M[Q_A\psi](s)
}
\]
with the same regularization/boundary convention used in the completed theta Mellin formula.

In the centered \(r\)-coordinate this is exactly the v13.722 distributional identity:
\[
(\partial_r^2-\tfrac14)K_\theta
=
\Phi-\frac12\delta_0,
\]
whose bilateral transform gives
\[
\Xi(w)-\frac12.
\]
The derivative jump at the self-dual point supplies the contact term, and the completion constant cancels it to give
\[
\boxed{
\Xi(w)=\int_{\mathbb R}\Phi(r)e^{wr}\,dr.
}
\]

So the polynomial multiplying the Tate Mellin transform is not an externally appended numerical coincidence: it is the spectral image of a concrete quadratic polynomial in the split-Cartan dilation generator.

---

## 9. Local-global meaning of the operator

The global zeta integral factors over all places:
\[
\Lambda(s)=\prod_v Z_v(s).
\]
The common complex parameter \(s\) is the character exponent of the idele norm.

The operator \(Q_A\) may be inserted at the real scaling place. Its Mellin eigenvalue is the global scalar
\[
s(s-1),
\]
so acting at the archimedean split-Cartan coordinate multiplies the full factored global zeta integral by the desired completion polynomial.

Thus there is no need to invent a prime-by-prime differential analogue of \(Q_A\). The finite places provide the Euler factors; the real dilation generator supplies the polynomial spectral multiplier on the shared global character parameter.

This gives the exact division of labor:
\[
\boxed{
\begin{array}{ccl}
p\text{-adic standard vectors} &\to& (1-p^{-s})^{-1},\\
\text{real Gaussian} &\to& \pi^{-s/2}\Gamma(s/2),\\
\text{real split-Cartan polynomial }Q_A &\to& s(s-1),\\
\text{Fourier self-duality} &\to& s\leftrightarrow1-s.
\end{array}}
\]

Together these produce the completed xi architecture.

---

## 10. Relation to the earlier SL2 principal-series Casimir

There are now two mathematically distinct appearances of the same quadratic polynomial.

### Principal-series lane
For a variable principal-series infinitesimal character \(w\),
\[
\Omega_{\rm PS}\rightsquigarrow w^2-\frac14.
\]

### Tate/Weil lane
For the Mellin character of the split Cartan,
\[
Q_A=4E_x^2+2E_x
\rightsquigarrow s(s-1)=w^2-\frac14.
\]

The numerical polynomial is identical because both are built from the same rank-one split-Cartan/Weyl geometry.

But:
\[
\boxed{
Q_A\neq C_{\rm Weil}
}
\]
as operators/central elements on the oscillator representation.

The Weil central Casimir is fixed at \(-3/16\), whereas \(Q_A\) is a noncentral polynomial in the dilation generator and therefore has a variable Mellin spectral value.

This resolves the apparent tension cleanly.

---

## 11. Representation-theoretic synthesis

The strongest exact diagram now supported is

\[
\boxed{
\begin{array}{ccc}
\text{adelic standard Gaussian}
&\xrightarrow{\text{Tate local zeta integrals}}&
\Lambda(s)
\\[1mm]
\downarrow\text{ Weil/Fourier self-duality}
&&
\downarrow\times\frac12s(s-1)
\\[1mm]
\text{Jacobi theta / }K_\theta
&\xrightarrow{Q_A\text{ and Mellin}}&
\xi(s).
\end{array}}
\]

In centered variables,
\[
Q_A
\xrightarrow{\rho\text{-shift}}
\partial_r^2-\frac14,
\]
and
\[
s=\frac12+w
\quad\Rightarrow\quad
s(s-1)=w^2-\frac14.
\]

The same Weyl reflection is visible in three compatible languages:
\[
x\mapsto x^{-1},
\qquad
r\mapsto-r,
\qquad
s\mapsto1-s
\quad(w\mapsto-w).
\]

This is now an actual operator/Mellin intertwining statement, not merely equality of quadratic formulas.

---

## 12. What failed and what survived

### Failed
1. Standard SL2 Eisenstein scattering does not preserve the exact even theta wave packet because its reflection phase is \(\phi(1/2+it)\), not identically \(+1\).
2. The Weil central Casimir does not produce \(s(s-1)\); it has fixed infinitesimal character \(-3/16\).

### Survived / strengthened
1. Tate GL1 gives the completed factor natively.
2. Weil/Fourier self-duality gives the exact theta reflection.
3. The split-Cartan Euler polynomial gives \(s(s-1)\) exactly.
4. After the rho-shift this operator is exactly the v13.722 shifted Casimir differential expression.
5. The principal-series Casimir and Tate Cartan polynomial have the same spectral polynomial because they share the same rank-one Weyl coordinate, but they are not the same representation-theoretic operator.

---

## 13. Status table

| Statement | Status |
|---|---|
| \(\Lambda(s)\) is the standard Tate global zeta integral | **EXACT** |
| Real local factor is \(\pi^{-s/2}\Gamma(s/2)\) | **EXACT** |
| Finite local factors are \((1-p^{-s})^{-1}\) | **EXACT** |
| Theta inversion is Fourier/Poisson self-duality | **EXACT** |
| Gaussian has a genuine Weil/metaplectic lift | **EXACT** |
| Weil central Casimir equals variable \(s(s-1)\) | **FAIL** |
| Weil Casimir on oscillator components is fixed (\(-3/16\) in the stated normalization) | **EXACT** |
| \(Q_A=4(x\partial_x)^2+2x\partial_x\) Mellin-multiplies by \(s(s-1)\) | **EXACT** |
| With \(x=e^{2r}\), \(Q_A=\partial_r^2+\partial_r\) | **EXACT** |
| Half-density conjugation gives \(\partial_r^2-\frac14\) | **EXACT** |
| This recovers the v13.722 Xi/contact-term identity | **EXACT** |
| Principal-series Casimir and Tate Cartan polynomial are literally the same central operator | **FALSE** |
| They have the same rank-one spectral polynomial | **EXACT** |
| Xi is thereby proved a spectral determinant / Hilbert–Pólya object | **NOT ESTABLISHED** |

---

## 14. Next gates

The next discriminating work should be:

1. formulate \(Q_A\) adelically as an archimedean Lie-algebra insertion in the global Tate zeta integral and verify all boundary/contact terms directly, rather than only after classical theta unfolding;
2. identify whether the positive kernel \(\Phi\) itself is a matrix coefficient, theta lift, or positive vector under a natural metaplectic/oscillator operator;
3. compare the logarithmic derivative/current lane from v13.715 with the Tate factorization place by place, to determine whether the prime delta-current is the distributional logarithmic derivative of the finite local Tate factors while the smooth \(W_\infty\) current is the real-place logarithmic derivative.

That third gate is especially promising because it would join the previously separate “prime + archimedean current” and “theta/Tate” descriptions at the level of local factors without forcing an invalid SL2 Eisenstein identification.

**Guardrail:** the current result is a genuine Tate/Cartan operator intertwining statement. It does not identify xi with the central Casimir of the Weil representation and does not imply RH or a Hilbert–Pólya operator.
