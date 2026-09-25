# Cone Derivation Ledger v13.776 — Lane A Post-Retraction Cleanup: Source-Faithful Continuous-Kernel Route Bypasses Primitive Boundary Constants for Weyl Data

Date: 2026-09-24

Lane: A.

Status: [D] post-v13.773 dependency cleanup; [D] exact source-faithful replacement for the retracted primitive inverse-source route; [D] parity-channel reduction; [D] projective Weyl/characteristic data do not require solving \(I_0/C,I_1/C\); [G] primitive edge asymptotics remain a separate question; [C] revised next gate.

Parents: v13.667, v13.685, v13.742–743, v13.757, v13.773–775.

## 0. Synchronization and audit

External Audit Round 97 v13.775 independently re-derived and PASSed the v13.773 retraction and PASSed v13.774. Live head was rechecked immediately before this write: v13.775 remains head; no collision.

This entry performs the dependency cleanup requested by that redirect rather than continuing to build on pre-retraction baggage.

## 1. Two operator levels must be separated [D]

The primitive first-kind equation is
\[
-K_Av
=
C(e^x-1-x)-I_1x-I_0.
\]
Here \(I_0,I_1\) are affine integration/boundary constants. v13.773 proved they cannot be obtained by the artificial inverse-source Schur split.

But Suzuki's exact transported continuous-kernel defect equation, established in v13.667, is
\[
\boxed{
S_Au_z=\bar D e_z,
\qquad
S_A=G_A-\lambda K_A^{N},
}
\]
with \(\bar D:\mathcal H(T_A)\to\mathcal H(S_A)\) unitary/isometric.

For the deficiency points,
\[
\boxed{
S_Au_+=\bar D e_{+i},
\qquad
S_Au_-=\bar D e_{-i}.
}
\]

These equations are source-faithful and contain no free primitive affine constants.

Thus:
\[
\boxed{
(I_0,I_1)\text{ belong to primitive reconstruction, not to the exact }S_A\text{ defect solve.}
}
\]

## 2. Consequence: Weyl data bypass the primitive constants [D]

The transported boundary triple preserves the Weyl function exactly:
\[
\widetilde m_A(z)=m_A(z).
\]

From v13.685 define
\[
F_{A,\pm}(z)
=
\overline{
\langle \bar D e_{\bar z},
S_A^{-1}\bar D e_{\pm i}
\rangle
}.
\]

Then
\[
\boxed{
m_A(z)
=
-i
\frac{
(z-i)F_{A,+}(z)+(z+i)F_{A,-}(z)
}{
(z-i)F_{A,+}(z)-(z+i)F_{A,-}(z)
}.
}
\]

This exact formula uses only the source-faithful \(S_A\) inverse on the actual derivative sources \(\bar D e_{\pm i}\). It does not require \(I_0/C\), \(I_1/C\), \(\alpha_A\), or \(\beta_A\).

Therefore the statement in pre-retraction v13.757 that the primitive feedback ratios are “common control variables” for the finite Weyl shape is retracted.

The correct statement is:
\[
\boxed{
\text{primitive affine constants control primitive edge reconstruction;}
\quad
\text{finite Weyl data are obtained directly from }S_A.
}
\]

## 3. Parity decomposition of the exact defect source [D]

For \(e_{+i}(x)=e^x\),
\[
\bar D e_{+i}\propto e^x
=
\cosh x+\sinh x
\]
(up to the fixed derivative phase/sign convention).

Since \(S_A\) commutes with reflection, decompose
\[
u_+=u_e+u_o
\]
with
\[
\boxed{
S_A^{(+)}u_e=\bar D(\cosh x),
\qquad
S_A^{(-)}u_o=\bar D(\sinh x).
}
\]

Reflection determines the opposite deficiency vector, with the derivative-transport sign fixed by the chosen convention:
\[
u_-=\pm R u_+.
\]

Thus the exact finite problem separates into one even and one odd continuous-kernel solve. No affine source \(1\) or \(x\) is introduced.

This is the source-faithful parity replacement for the retracted split
\[
e^x-1-x,\quad 1,\quad x.
\]

## 4. Relation to the divisor-shell source observation [D/I]

v13.770 found that the reflected smooth density of the divisor rapidity sampling produces the parity profiles
\[
\cosh s,\qquad \sinh s,
\]
while affine subtraction produced the primitive profiles
\[
\cosh s-1,\qquad \sinh s-s.
\]

The post-retraction operator split now clarifies the two levels:

- exact \(S_A\) defect source:
  \[
  \boxed{\cosh x,\ \sinh x;}
  \]
- primitive twice-integrated source:
  \[
  \boxed{\cosh x-1,\ \sinh x-x.}
  \]

So the divisor-shell observation was not merely suggestive: its un-subtracted parity densities align with the exact derivative-space defect sources, while its affine-subtracted versions align with primitive reconstruction.

No arithmetic equality of operators is asserted.

## 5. Projective characteristic data also bypass primitive constants [D]

Define
\[
A_A(z)=(z-i)F_{A,+}(z),
\qquad
B_A(z)=(z+i)F_{A,-}(z).
\]
Then
\[
W_0=A_A+B_A,
\qquad
W_\pi=A_A-B_A.
\]

The normalized cross-ratio
\[
\boxed{
\Delta^{(A)}_{0/\pi}(z;z_*)
=
\frac{W_0(A,z)W_\pi(A,z_*)}
{W_\pi(A,z)W_0(A,z_*)}
=
\frac{m_A(z)}{m_A(z_*)}
}
\]
is exact and independent of any common deficiency normalization.

Hence the finite-to-infinite **projective** spectral-shape problem can be attacked directly through the continuous-kernel source pairings without first controlling primitive edge coefficients.

This survives v13.773 intact because v13.685 never used the artificial Schur decomposition.

## 6. What v13.774 remains good for [G]

v13.774 is not retracted. Its two constants
\[
(\alpha_A,\beta_A)
\]
remain the correct primitive integration data when one reconstructs \(v\) from \(u=\bar Dv\), and its observation that second differentiation loses a two-dimensional affine sector remains exact.

But that sector is a **reconstruction/gauge boundary problem**, not an extra unknown in the exact \(S_A\) defect equation.

Therefore two questions must now be kept separate:

### A. Weyl/characteristic convergence
Study
\[
S_A^{-1}\bar D e_{\pm i},
\quad
F_{A,\pm},
\quad
m_A,
\quad
\Delta^{(A)}_{0/\pi}.
\]
Primitive \(I_0,I_1\) are unnecessary.

### B. Primitive edge-profile convergence
Study
\[
I_0/C,\quad I_1/C,\quad \alpha_A,\quad\beta_A.
\]
These matter if one wants convergence of the primitive first-kind profile itself.

Question B is not a prerequisite for Question A.

## 7. Correction to the immediate-next-step framing in v13.775 [Audit/G]

Round 97 correctly states that the genuine primitive open item is direct determination of
\[
I_0/C,\qquad I_1/C.
\]

However, after the present dependency cleanup, this is **not the unique immediate Lane-A gate** if the objective is Suzuki Weyl/HB/Xi convergence.

The already-established exact continuous-kernel route supplies a stronger bypass:
\[
\boxed{
S_Au_\pm=\bar D e_{\pm i}
\longrightarrow
F_{A,\pm}
\longrightarrow
m_A
\longrightarrow
\Delta^{(A)}_{0/\pi}.
}
\]

Thus the primitive boundary constants can be postponed while the spectral-shape lane proceeds.

## 8. Revised next gate [C]

Use the parity-decomposed exact operator
\[
S_A^{(+)}u_e=\bar D\cosh x,
\qquad
S_A^{(-)}u_o=\bar D\sinh x,
\]
and rewrite \(F_{A,+},F_{A,-}\) in terms of the even/odd response transforms.

Then derive the exact Möbius expression for \(m_A\) in those two parity amplitudes and compare its finite-\(A\) projective shape directly with
\[
m_\infty(z)
=
-i\frac{a}{b}\frac{\xi'(1/2-iz)}{\xi(1/2-iz)}.
\]

The analytic asymptotic target should be the ratio/cross-ratio, not the primitive affine constants.

## Result

The v13.773 correction removes more baggage than previously recognized.

For finite Weyl and characteristic data, the source-faithful route is already exact:
\[
\boxed{
S_Au_\pm=\bar D e_{\pm i}
\to
F_{A,\pm}
\to
m_A
\to
\Delta_{0/\pi}^{(A)}.
}
\]

The primitive constants
\[
I_0/C,\ I_1/C
\]
remain genuine and important for reconstructing the primitive edge profile, but they are **not prerequisites for finite Weyl/HB/Xi spectral-shape analysis**.

The exact parity sources in the continuous-kernel space are
\[
\boxed{\cosh x,\qquad\sinh x,}
\]
while
\[
\cosh x-1,\qquad\sinh x-x
\]
belong to the primitive affine-subtracted reconstruction. This cleanly reconciles the divisor-shell parity observation with Suzuki's two operator levels.
