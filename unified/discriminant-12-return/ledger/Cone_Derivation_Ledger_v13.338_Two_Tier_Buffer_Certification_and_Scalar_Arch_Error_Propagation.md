# Cone Derivation Ledger v13.338 — Two-Tier Buffer Certification and Scalar Arch Error Propagation

## Main correction

The buffer has two distinct roles and therefore should not be assigned one uniform enclosure radius.

### Tier 1: coarse positivity enclosure

For the 67-dimensional buffer B={21,23,...,153}, a coarse outward-rounded enclosure is used only to prove

\[
B\succeq \gamma I.
\]

The pole-free numerical gap is about 0.2385, so an entrywise radius of order 1e-3 is already sufficient for this purpose by the crude perturbation estimate

\[
\|E\|_2\le67\epsilon.
\]

A deliberately conservative certification target is \(\gamma=0.15\).

### Tier 2: fine nominal matrix for Schur solve

The coarse interval must **not** be propagated through an inverse perturbation formula.  Instead form a separate high-accuracy nominal matrix \(\widehat B\), solve

\[
\widehat B X\approx C^T,
\]

and certify the residual against the true enclosed blocks:

\[
R=C^T-BX.
\]

Since \(B\succeq\gamma I\),

\[
\|B^{-1}C^T-X\|\le\frac{\|R\|}{\gamma},
\]

and therefore

\[
\|CB^{-1}C^T-CX\|
\le\frac{\|C\|}{\gamma}\|R\|.
\]

With conservative values \(\|C\|\le0.8\), \(\gamma=0.15\), a solve-residual norm below about \(9\times10^{-10}\) contributes less than \(5\times10^{-9}\) to the effective-core operator error.

## Scalar archimedean reconstruction error

For odd \(m\ne n\),

\[
K^{arch}_{mn}
=-\frac4\pi\frac{nH_m-mH_n}{n^2-m^2}.
\]

If every \(H_j\) is enclosed to radius \(\epsilon_H\), then

\[
|\delta K_{mn}|
\le \frac4\pi\frac{n+m}{|n^2-m^2|}\epsilon_H
=\frac4{\pi|n-m|}\epsilon_H
\le\frac2\pi\epsilon_H,
\]

because distinct odd modes differ by at least two.

Thus there is no high-frequency amplification.  If both the H-sequence and the independent diagonal D-sequence are enclosed to radius \(10^{-11}\), every arch entry is enclosed to at most \(10^{-11}\), and the full 77x77 arch operator has the crude bound

\[
\|E_{arch}\|_2\le77\times10^{-11}=7.7\times10^{-10}.
\]

## Exact pole vector

For \(k_n=n\pi/2\), odd n,

\[
c_n=\langle\psi_n,\cosh(x/2)\rangle
=\frac{2k_n\cosh(1/2)}{k_n^2+1/4}.
\]

Hence \(P_{pole}=2cc^T\) needs no quadrature.

## Consequence

The proof-grade finite assembly is now naturally split into:

1. coarse 67x67 interval buffer only for positivity;
2. high-accuracy scalar H,D sequences and explicit cusp/prime/pole formulas;
3. high-precision numerical buffer solve;
4. rigorous residual enclosure;
5. 10x10 effective-core operator enclosure.

No positivity, exact zero, lambda_1=0, RH, or GRH conclusion follows yet.