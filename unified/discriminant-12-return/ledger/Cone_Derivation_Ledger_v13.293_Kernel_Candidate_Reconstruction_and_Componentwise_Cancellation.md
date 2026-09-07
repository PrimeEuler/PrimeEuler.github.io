# Cone Derivation Ledger v13.293 — Kernel-Candidate Reconstruction and Componentwise Cancellation

Date: 2026-09-07

Status: HIGH-PRECISION LIMIT-CANDIDATE RECONSTRUCTION + MODEWISE POLE/PRIME/ARCHIMedean CANCELLATION — STRONG NUMERICAL EVIDENCE FOR A SMOOTH PROJECTED KERNEL CANDIDATE AT a=1 — NOT A PROOF OF ker(G_1) != {0}, RH, OR GRH

## 0. Purpose

The v13.292 audit changed the interpretation of the collapsing positive Ritz branch. The candidate vectors did not escape toward high frequency or toward the boundary; successive embedded vectors were strongly aligned, boundary mass decreased, central mass increased, and the independently evaluated normalized residual ||P_a G_a u_M||/||u_M|| decreased from about 1.13e-7 at M=6 to about 5.27e-10 at M=12.

The next question is therefore no longer merely whether the smallest eigenvalue is small. It is whether the finite vectors themselves are approaching a coherent function and whether the source decomposition cancels in the full projected equation rather than only in one scalar Rayleigh quotient.

This entry adds

`research-notes/suzuki_kernel_candidate_reconstruction.py`.

The source conventions remain those of Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2, especially equations (1.3), (8.6), and (8.7).

---

## 1. Correct even-sector reconstruction

At a=1 the normalized Dirichlet basis is

\[
\psi_n(x)=\sin\left(\frac{n\pi(x+1)}2\right).
\]

For odd n=2j+1,

\[
\psi_{2j+1}(x)=(-1)^j\cos\left(\frac{(2j+1)\pi x}{2}\right).
\]

Therefore the even-v candidate can be reconstructed directly as an ordinary cosine series after absorbing the basis phase.

The high-precision M=12 lowest Ritz vector has odd-index Dirichlet coefficients approximately

\[
(c_1,c_3,c_5,c_7,c_9,c_{11})
=
(0.8528405514,-0.4973980451,0.1574899941,-0.02133229914,-2.18357\times10^{-6},1.156218\times10^{-4}).
\]

After converting to ordinary cosine amplitudes by multiplying c_{2j+1} by (-1)^j, the first four amplitudes are positive:

\[
0.8528405514,
0.4973980451,
0.1574899941,
0.02133229914,
\]

followed by very small higher corrections.

At M=14 the odd-index Dirichlet coefficients are approximately

\[
(0.8431716740,-0.5083070230,0.1731215111,-0.02672731941,-3.46154\times10^{-6},3.021769\times10^{-4},-4.21697\times10^{-6}).
\]

The candidate therefore remains dominated by the first few even cosine modes. No migration of norm into the newly added high-frequency modes is observed.

No simple closed elementary form is identified at this checkpoint. The useful conclusion is structural rather than symbolic: the coefficient sequence is coherent, low-frequency dominated, and compatible with the smooth centrally concentrated profile diagnosed in v13.292.

---

## 2. Stabilization across nested spaces

The lowest high-precision Ritz values from the preceding componentwise audit are

| modes | lowest Ritz value |
|---:|---:|
| 6 | 3.23765e-11 |
| 8 | 1.41673e-12 |
| 10 | 1.23216e-13 |
| 12 | 1.82275e-15 |
| 14 | 4.52235e-17 |

The vector sequence remains strongly aligned under embedding, as already seen in v13.292. The coefficient reconstruction now shows why: the first few odd Dirichlet coefficients evolve gradually while the newly introduced tail coefficients remain very small.

This behavior is inconsistent with the simplest Galerkin-pollution picture in which the minimum is driven by a vector whose mass runs to the highest retained mode.

It is still not, by itself, a convergence proof.

---

## 3. Stronger test: projected equation rather than Rayleigh quotient

The v13.291 audit showed that the scalar quadratic-form value is obtained by cancellation among order-one source contributions. A scalar cancellation could in principle be accidental.

The stronger test is to apply each component matrix to the candidate coefficient vector:

\[
y_{\rm pole}=A_{\rm pole}c,
\qquad
y_{\rm prime}=A_{\rm prime}c,
\qquad
y_{\rm arch}=A_{\rm arch}c.
\]

If c is a projected kernel candidate, then

\[
(A_{\rm pole}+A_{\rm prime}+A_{\rm arch})c\approx0
\]

should hold as a vector, not merely after contraction with c.

At M=14 the component action norms are approximately

\[
\|y_{\rm pole}\|_2=2.61742,
\qquad
\|y_{\rm prime}\|_2=1.03556,
\qquad
\|y_{\rm arch}\|_2=1.88727,
\]

while

\[
\boxed{
\|y_{\rm pole}+y_{\rm prime}+y_{\rm arch}\|_2
\approx4.52235\times10^{-17}.
}
\]

Thus the cancellation is a full projected operator cancellation to the available high precision.

---

## 4. Entrywise cancellation

The effect is visible mode by mode in the even-v sector. For M=14:

| n | pole | prime | arch | sum |
|---:|---:|---:|---:|---:|
| 1 | 2.353669916 | -0.4835424034 | -1.870127513 | 3.81e-17 |
| 3 | 0.8544297532 | -0.7390063089 | -0.1154234444 | -2.30e-17 |
| 5 | 0.5163366738 | -0.3922155708 | -0.1241211030 | 7.83e-18 |
| 7 | 0.3695425159 | -0.2371047709 | -0.1324377450 | -1.21e-18 |
| 9 | 0.2876564586 | -0.1957916641 | -0.09186479453 | -1.57e-22 |
| 11 | 0.2354525255 | -0.1603847504 | -0.07506777514 | 1.37e-20 |
| 13 | 0.1992764146 | -0.1353854533 | -0.06389096134 | -1.91e-22 |

The first projected mode alone exhibits the order-one cancellation

\[
2.353669916-0.4835424034-1.870127513
\approx3.8\times10^{-17}.
\]

The same phenomenon continues through every retained even-v mode.

This is substantially stronger numerical evidence than a tiny eigenvalue or tiny Rayleigh quotient alone.

---

## 5. Interpretation

The combined evidence from v13.291-v13.293 is now internally consistent:

1. arbitrary precision removes the spurious negative signs and leaves positive finite Ritz values;
2. those values collapse rapidly toward zero as the space grows;
3. the associated vectors remain strongly aligned under embedding;
4. their mass remains concentrated in low modes and in the interval interior;
5. an independently evaluated P_a G_a residual decreases with M;
6. the source components cancel in the full projected equation, entry by entry, to high precision.

The natural numerical interpretation is therefore that the sequence is approximating a smooth even-v / odd-u solution candidate of

\[
P_1G_1u=0,
\qquad u=Dv,
\]

rather than merely exploiting the generic compact near-kernel through high-frequency escape.

However, Suzuki's lambda=0 case is exceptional. A theorem-level statement that ker(G_1) is nontrivial requires more than finite-section numerics. One needs a convergence argument or a certified residual plus compactness/coercivity mechanism that prevents the normalized candidates from converging weakly to zero or to a non-domain object.

Therefore this ledger does not state lambda_1=0 as proved.

---

## 6. Exact, numerical, and open

Exact/source-established:

- Suzuki's source decomposition g=g_pole+g_prime+g_arch;
- the direct form identity Q_W(v)=<G_a Dv,Dv> on the stated test/form domain;
- the generalized formulation of equation (8.7);
- the parity identity psi_(2j+1)(x)=(-1)^j cos((2j+1)pi x/2) at a=1.

Numerically established to high precision:

- the M=6 through M=14 positive Ritz branch quoted above;
- stable low-frequency coefficient structure of the corresponding even-v candidates;
- order-one component action vectors whose sum is approximately 4.52e-17 at M=14;
- modewise pole/prime/archimedean cancellation through every retained even-v coordinate;
- no evidence of high-frequency escape in the reconstructed coefficient sequence.

Still open:

- prove convergence of v_M or u_M in a topology strong enough to pass G_1 to the limit;
- prove the limiting candidate is nonzero and lies in the correct operator/form domain;
- certify P_1G_1u=0 rather than merely observe rapidly decreasing numerical residuals;
- determine whether ker(G_1) is genuinely nontrivial;
- determine the exact value/sign of lambda_1 in Suzuki's A_1 problem;
- certify any lambda<lambda_1 for the Section-8 Fredholm problem;
- D12 transfer remains downstream;
- RH/GRH remains unproved.

---

## 7. Next target

The clean next step is to turn the observed convergence into a quantitative compactness test.

For the candidate sequence, compute

\[
\|v_{M+2}-v_M\|_{L^2},
\qquad
\|D(v_{M+2}-v_M)\|_{L^2},
\qquad
\|G_1(Dv_{M+2}-Dv_M)\|_{L^2},
\]

under consistent normalization, and track the tail in the exact Fourier coefficients.

Because the basis diagonalizes the H_0^1 seminorm, the first two quantities are available directly from the coefficient sequence. If the sequence is Cauchy in H_0^1 rather than merely L^2, then u_M=Dv_M converges strongly in L^2. Since G_1 is bounded/compact on the mean-zero L^2 space, the observed residual decay could then be passed numerically much closer to a genuine kernel statement.

The preferred v13.294 target is therefore

\[
\boxed{\text{H}_0^1\text{-Cauchy audit + strong-}L^2\text{ convergence of }u_M + independent residual transfer}. 
\]
