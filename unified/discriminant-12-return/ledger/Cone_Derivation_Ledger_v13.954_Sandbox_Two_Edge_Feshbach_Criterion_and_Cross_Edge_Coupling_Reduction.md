# Cone Derivation Ledger v13.954 — Sandbox: Two-Edge Feshbach Criterion and Reduction of the Physical Selector to One Cross-Edge Coupling

**Date:** 2026-10-02  
**Track:** Sandbox / untwisted selector and Suzuki-Jost edge-doublet lane  
**Status:** [D] abstract two-edge Feshbach reduction under explicit moat/invariance hypotheses; [C] physical gap and residue-ratio consequences; [O] certify the hypotheses for Suzuki's recentered operator  
**Authorization:** Jeremy, 2026-10-02 ("no twist... lets keep pushing")  
**Parents:** v13.798, v13.823, v13.936, v13.938, v13.950, v13.953  
**Collision check:** v13.954 was absent immediately before this write.

---

## 0. Goal

v13.953 sharpened the selector architecture to the native untwisted positive state and showed that an untwisted reflection doublet would force

\[
r_a=\alpha_a/\beta_a\to1.
\]

The remaining issue was whether the doublet must be assumed wholesale.

It need not be.

This entry shows that it follows from a standard protected-subspace/Feshbach mechanism once one has:

1. one right-edge quasimode and its reflection;
2. a uniform complement moat;
3. small edge-plane/complement coupling;
4. a localized source.

The full low-energy problem then reduces to one renormalized off-diagonal scalar.

---

## 1. Untwisted recentered operator

Let

\[
B_a=A_a-\lambda_a I\ge0
\]

on \(L^2(-a,a)\), and let \(R\) be reflection,

\[
(Rf)(x)=f(-x).
\]

Assume

\[
RB_a=B_aR.
\]

Let \(\phi_{R,a}\) be a normalized right-edge quasimode and define

\[
\phi_{L,a}=R\phi_{R,a}.
\]

Let

\[
E_a=\operatorname{span}\{\phi_{R,a},\phi_{L,a}\},
\]

with orthogonal projection \(P_a\), and let

\[
Q_a=I-P_a.
\]

---

## 2. Exact Feshbach map [D]

For real or complex \(z\) such that

\[
Q_a(B_a-z)Q_a
\]

is invertible, define

\[
\boxed{
\mathcal F_a(z)
=
P_a(B_a-z)P_a
-
P_aB_aQ_a
\bigl[
Q_a(B_a-z)Q_a
\bigr]^{-1}
Q_aB_aP_a.
}
\tag{1}
\]

The exact Feshbach theorem gives

\[
\boxed{
B_a-z\text{ is singular}
\iff
\mathcal F_a(z)\text{ is singular}
}
\tag{2}
\]

inside the window where the complement block is invertible.

The kernel dimensions agree.

---

## 3. Reflection forces the two-edge normal form [D]

Because

\[
RB_a=B_aR,
\qquad
RP_a=P_aR,
\]

the Feshbach map commutes with the induced reflection on \(E_a\).

Choose a left/right orthonormal basis of \(E_a\) obtained by symmetric Gram orthogonalization from \(\phi_{R,a},\phi_{L,a}\).

Reflection acts by exchanging the two basis vectors.

Any \(2\times2\) matrix commuting with that exchange has the form

\[
\boxed{
\mathcal F_a(z)
=
\begin{pmatrix}
d_a(z)-z & c_a(z)\\
c_a(z)&d_a(z)-z
\end{pmatrix}.
}
\tag{3}
\]

Therefore the parity eigenvalues of the Feshbach map are

\[
\boxed{
m_{+,a}(z)
=
d_a(z)+c_a(z)-z,
}
\tag{4}
\]

\[
\boxed{
m_{-,a}(z)
=
d_a(z)-c_a(z)-z.
}
\tag{5}
\]

No parity mixing remains.

---

## 4. Complement moat and analytic control [D]

Assume that for some fixed \(g>0\) and all sufficiently large \(a\),

\[
\boxed{
Q_aB_aQ_a\ge g\,Q_a.
}
\tag{H1}
\]

Then for

\[
|z|<g/2,
\]

\[
\boxed{
\left\|
\bigl[
Q_a(B_a-z)Q_a
\bigr]^{-1}
\right\|
\le
\frac{2}{g}.
}
\tag{6}
\]

Assume also the edge-plane/complement coupling satisfies

\[
\boxed{
\varepsilon_a
:=
\|Q_aB_aP_a\|
\to0.
}
\tag{H2}
\]

Then the Feshbach correction obeys

\[
\boxed{
\left\|
P_aB_aQ_a
\bigl[
Q_a(B_a-z)Q_a
\bigr]^{-1}
Q_aB_aP_a
\right\|
\le
\frac{2\varepsilon_a^2}{g}.
}
\tag{7}
\]

Its \(z\)-derivative is bounded by

\[
\boxed{
O\!\left(
\frac{\varepsilon_a^2}{g^2}
\right)
}
\tag{8}
\]

uniformly on \(|z|<g/2\).

Thus the two-edge effective matrix becomes asymptotically \(z\)-flat whenever

\[
\varepsilon_a/g\to0.
\]

---

## 5. Recentered even ground fixes one parity root [D]

Assume the true finite ground state is even and belongs to the low two-edge cluster.

Since \(B_a\) is recentered,

\[
0\in\sigma(B_a)
\]

and therefore

\[
m_{+,a}(0)=0.
\]

Hence

\[
\boxed{
d_a(0)+c_a(0)=0.
}
\tag{9}
\]

The entire low-energy splitting is therefore encoded in the odd channel.

At \(z=0\),

\[
m_{-,a}(0)
=
d_a(0)-c_a(0)
=
-2c_a(0).
\tag{10}
\]

So the off-diagonal Feshbach coupling is the zero-energy parity splitting parameter.

---

## 6. Odd-gap theorem [C]

Let

\[
\Delta_a
=
\inf\sigma(B_a|_{\rm odd}).
\]

The odd eigenvalue is characterized by

\[
m_{-,a}(\Delta_a)=0.
\]

Using (5),

\[
\Delta_a
=
d_a(\Delta_a)-c_a(\Delta_a).
\]

Subtract the zero-energy relation

\[
d_a(0)+c_a(0)=0.
\]

Then

\[
\Delta_a
=
-2c_a(0)
+
\bigl[
d_a(\Delta_a)-d_a(0)
\bigr]
-
\bigl[
c_a(\Delta_a)-c_a(0)
\bigr].
\]

Assume the Feshbach derivative on the gap scale satisfies

\[
\boxed{
\sup_{0\le z\le 2\Delta_a}
\left(
|d_a'(z)|+|c_a'(z)|
\right)
\to0.
}
\tag{H3}
\]

Then

\[
\boxed{
\Delta_a
=
-2c_a(0)\,[1+o(1)].
}
\tag{11}
\]

In particular the physical gap is asymptotically determined by one scalar.

Because \(\Delta_a\ge0\),

\[
c_a(0)\le0
\]

asymptotically in the nondegenerate regime.

---

## 7. Matching zero-blind scale reduces to one scalar limit [C/O]

v13.950 gives the exact zero-blind unit-stopband exponent

\[
\bar\sigma_1=1.
\]

Thus the canonical zero-blind quadratic-form scale is

\[
e^{-2a}.
\]

The physical gap saturates that scale if and only if

\[
\boxed{
e^{2a}c_a(0)
\longrightarrow
-c_*
}
\tag{H4}
\]

with

\[
0<c_*<\infty.
\]

Under H4,

\[
\boxed{
e^{2a}\Delta_a
\longrightarrow
2c_*.
}
\tag{12}
\]

Equivalently, with

\[
N_a=e^{2a},
\]

\[
\boxed{
N_a\Delta_a
\longrightarrow
2c_*.
}
\tag{13}
\]

Thus the full physical matching problem has been reduced to a single renormalized off-diagonal Feshbach matrix element.

---

## 8. Edge-vector convergence from the same hypotheses [C]

Let the edge overlap be

\[
s_a
=
\langle
\phi_{R,a},\phi_{L,a}
\rangle.
\]

Assume

\[
\boxed{
s_a\to0.
}
\tag{H5}
\]

The normalized parity combinations are

\[
e_{+,a}
=
\frac{
\phi_{R,a}+\phi_{L,a}
}{
\sqrt{2(1+s_a)}
},
\]

\[
e_{-,a}
=
\frac{
\phi_{R,a}-\phi_{L,a}
}{
\sqrt{2(1-s_a)}
}.
\]

Under H1–H2, the low two-dimensional spectral projection differs from \(P_a\) by

\[
\boxed{
O(\varepsilon_a/g)
}
\tag{14}
\]

in operator norm by the standard spectral-subspace residual/gap estimate.

Therefore the actual lowest even/odd eigenvectors satisfy

\[
\boxed{
\psi_{+,a}
=
e_{+,a}
+
O(\varepsilon_a/g),
}
\tag{15}
\]

\[
\boxed{
\psi_{-,a}
=
e_{-,a}
+
O(\varepsilon_a/g).
}
\tag{16}
\]

This recovers the doublet hypothesis D2 of v13.953 from the moat/invariance criterion.

---

## 9. Source localization and residue ratio [C]

Define

\[
A_a
=
\langle
\phi_{R,a},e^x
\rangle,
\]

\[
B_a^{\rm wrong}
=
\langle
\phi_{R,a},e^{-x}
\rangle.
\]

Assume

\[
\boxed{
\frac{
B_a^{\rm wrong}
}{
A_a
}
\to0
}
\tag{H6}
\]

and

\[
A_a\ne0.
\]

Then v13.953's calculation applies, while the eigenvector error from (15)–(16) contributes only \(o(1)\) provided the source overlaps are controlled on the same scale.

Hence

\[
\boxed{
\frac{\alpha_a}{\beta_a}
\longrightarrow1.
}
\tag{17}
\]

Thus the physical residue ratio becomes universal under H1–H2 and H5–H6.

---

## 10. A concrete sufficient edge-profile hypothesis for H6 [C]

Write

\[
x=a-\xi
\]

near the right edge.

Assume the translated edge mode

\[
\widetilde\phi_a(\xi)
=
\phi_{R,a}(a-\xi)
\]

converges to a nonzero profile \(\widetilde\phi_\infty\) with finite weighted moments

\[
\int_0^\infty
|\widetilde\phi_\infty(\xi)|e^{\pm\xi}\,d\xi
<
\infty,
\]

and

\[
\int_0^\infty
\widetilde\phi_\infty(\xi)e^{-\xi}\,d\xi
\ne0.
\]

Then

\[
A_a
=
e^a
\int
\widetilde\phi_a(\xi)e^{-\xi}\,d\xi,
\]

while

\[
B_a^{\rm wrong}
=
e^{-a}
\int
\widetilde\phi_a(\xi)e^{\xi}\,d\xi.
\]

Therefore

\[
\boxed{
\frac{
B_a^{\rm wrong}
}{
A_a
}
=
O(e^{-2a}),
}
\tag{18}
\]

so H6 follows automatically.

This is the precise source-localization mechanism behind the untwisted residue equality.

---

## 11. Universal overlap scaling once the Feshbach gate closes [C]

From v13.953,

\[
r_a\to1
\]

implies

\[
\delta_\tau(a)
\sim
\frac{e^\tau-1}{2}
\Delta_a.
\]

If H4 also holds,

\[
\boxed{
e^{2a}\delta_\tau(a)
\longrightarrow
(e^\tau-1)c_*.
}
\tag{19}
\]

Equivalently,

\[
\boxed{
N_a\delta_\tau(a)
\longrightarrow
(e^\tau-1)c_*.
}
\tag{20}
\]

For the one-e-fold normalization,

\[
\boxed{
N_a\delta_1(a)
\longrightarrow
(e-1)c_*.
}
\tag{21}
\]

So after the no-twist selector and exact zero-blind exponent are imposed, the entire critical double-scaling law is controlled by one physical constant \(c_*\).

---

## 12. What is now reduced to certification [O]

The abstract mechanism is closed.

The only genuinely operator-specific tasks are now:

1. construct a right-edge quasimode \(\phi_{R,a}\);
2. prove a uniform complement moat H1;
3. certify
   \[
   \varepsilon_a=\|Q_aB_aP_a\|\to0;
   \]
4. prove the translated edge-profile hypothesis;
5. evaluate the renormalized off-diagonal coupling
   \[
   e^{2a}c_a(0).
   \]

The prior protected-subspace/Feshbach entries show that this style of certification is already available in the project.

The missing object is not the algebraic reduction.

It is the source-faithful large-\(a\) edge quasimode.

---

## 13. Result

The untwisted physical selector problem has now been reduced to a single scalar Feshbach channel.

Under a two-edge almost-invariant subspace with a uniform complement moat,

\[
\boxed{
\mathcal F_a(z)
=
\begin{pmatrix}
d_a(z)-z & c_a(z)\\
c_a(z)&d_a(z)-z
\end{pmatrix}.
}
\]

Recentring fixes

\[
d_a(0)+c_a(0)=0,
\]

and therefore

\[
\boxed{
\Delta_a
=
-2c_a(0)[1+o(1)].
}
\]

If

\[
\boxed{
e^{2a}c_a(0)\to-c_*\ne0,
}
\]

then

\[
\boxed{
N_a\Delta_a\to2c_*,
}
\]

\[
\boxed{
r_a\to1,
}
\]

and

\[
\boxed{
N_a\delta_\tau(a)
\to
(e^\tau-1)c_*.
}
\]

The next gate is therefore completely concrete:

\[
\boxed{
\textbf{construct and certify the native right-edge quasimode and compute }e^{2a}c_a(0).
}
\]
