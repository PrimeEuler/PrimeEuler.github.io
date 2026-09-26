# Cone Derivation Ledger v13.812 — Terminal Outward Remote-Residual-Gram Certificate for the Frozen \(\rho=0.10\) Six-Planes

Date: 2026-09-26

Lane: A.

Status: [C] even-v and odd-v frozen six-plane remote residual-Gram ceilings certified with fail-closed outward budgets; [C] combined with v13.809/v13.810 finite-side and remote-tail-floor certificates; [C] frozen six-plane positivity at the \(\rho=0.10\) minus endpoint; [G] complementary four core directions and the plus endpoint remain separate gates.

Parents: v13.807–811.

Research artifact:

- research-notes/suzuki_endpoint_M3999_terminal_remote_gram_certificate.py
- commit bb9b1fab9227b04e5833a04d13d866219133115e.

Round-104 reconciliation:

- f16f86670c298bf17a2544a647a7395d894f6e01 updates the even-v finite reference-defect cap from the stale \(9.20\times10^{-16}\) value to the actually observed outward-rounded \(1.11\times10^{-15}\);
- c5c062d46ce47f6cd5adf62d5a16fb3acb8dcc3f records the correction in v13.809;
- the recomputed finite lower bound is
  \[
  C_+>0.9999992082623\,I,
  \]
  so the published safe value
  \[
  C_+>0.9999992082\,I
  \]
  remains valid unchanged.

No GitHub workflow/status run is attached to these research commits.

## 1. Certified inputs

From v13.809, after the Round-104 correction,

\[
\boxed{
C_+>0.9999992082\,I,
\qquad
C_->0.9999999425\,I.
}
\]

From the outward interval tail-floor certificate v13.810,

\[
\boxed{
\gamma_e(4001)>2.75305442655809082,
}
\]

\[
\boxed{
\gamma_o(4002)>2.75316939956044161.
}
\]

Hence

\[
\boxed{
\gamma_e C_+>2.7530522466895958\,I,
}
\]

\[
\boxed{
\gamma_o C_->2.7531692412532011\,I.
}
\]

## 2. Repaired nominal remote replay

The exact-dyadic \(Q_\pm,L_{0,\pm}\) payloads from v13.807 are held fixed.

The repaired remote replay accumulates the normalized residual Gram directly from \(4001/4002\) through \(16001/16000\), then by the eight-level inverse-power expansion through \(2,000,000\).

The independently reproduced point maxima are

\[
\boxed{
\lambda_{\max}(H_{e,2M}^{\rm point})
=
0.17738742092868218\ldots,
}
\]

\[
\boxed{
\lambda_{\max}(H_{o,2M}^{\rm point})
=
0.012096498661467095\ldots.
}
\]

Use the fail-closed explicit-section caps

\[
\boxed{
H_{e,2M}^{\rm point}<0.177388\,I,
}
\]

\[
\boxed{
H_{o,2M}^{\rm point}<0.012097\,I.
}
\]

## 3. Analytic far-generator bound \(|Z_n|<8\)

For the endpoint generator,

\[
Z_n
=
2A_n
+
\Im\psi\!\left(\frac14+\frac{i n\pi}{4}\right)
-
(-1)^n n\pi
\sum_{k\ge0}
\frac{e^{-2a_k}}
{a_k^2+(n\pi/2)^2}.
\]

The prime sine contribution satisfies

\[
|A_n|
\le
\sum_{q\in\{2,3,4,5,7\}}
\frac{\Lambda(q)}{\sqrt q}.
\]

For \(y=n\pi/4\),

\[
\Im\psi\!\left(\frac14+iy\right)
=
\sum_{k\ge0}
\frac{y}{(k+1/4)^2+y^2},
\]

and decreasing-sum plus integral comparison gives

\[
0<
\Im\psi\!\left(\frac14+iy\right)
<
\frac{\pi}{2}+\frac1y.
\]

Also,

\[
n\pi
\sum_{k\ge0}
\frac{e^{-2a_k}}
{a_k^2+(n\pi/2)^2}
\le
\frac4{n\pi}
\frac{e^{-1}}{1-e^{-4}}.
\]

At \(n\ge2,000,001\), an 80-digit interval evaluation gives a strict total upper bound below \(8\). Therefore

\[
\boxed{
|Z_n|<8
\qquad
(n\ge2,000,001).
}
\]

## 4. Far-tail point envelopes

With \(|Z_n|<8\), the rank-two inverse-power decomposition gives nominal residual-operator tail envelopes

\[
\boxed{
\|Y_{e,>2M}^{\rm point}\|^2
<
4.0\times10^{-4},
}
\]

\[
\boxed{
\|Y_{o,>2M}^{\rm point}\|^2
<
3.0\times10^{-5}.
}
\]

The raw midpoint envelope values are approximately

\[
3.804616856\times10^{-4}
\quad\text{and}\quad
2.582370444\times10^{-5}.
\]

Thus

\[
\boxed{
H_{e,\rm point}<0.177788\,I,
}
\]

\[
\boxed{
H_{o,\rm point}<0.012127\,I.
}
\]

## 5. Residual-operator perturbation budget

The exact-vs-nominal endpoint operator uncertainty is

\[
\epsilon_F=2.1\times10^{-13}.
\]

Using the v13.809 buffer floors, frozen coupling caps, six-RHS residual bounds, and exact frozen \(L_0\) conditioning gives normalized dressed-plane perturbations below approximately

\[
1.80\times10^{-7}
\quad\text{(even-v)},
\]

\[
6.04\times10^{-8}
\quad\text{(odd-v)}.
\]

Use the deliberately crude common remote cross-operator cap

\[
\boxed{\|F_{RF}\|<20.}
\]

This follows from

\[
0.9\|H\|\le0.9\frac{\pi}{2},
\qquad
\|B_{\rm prime}\|<2.05,
\]

the \(N=1\) global versions of the audited cusp and archimedean majorants,

\[
\|K_{\rm cusp}\|<0.789,
\qquad
\|K_{\rm arch}\|<4.893,
\]

and the crude rank-one bounds

\[
\|2cc^T\|
<
\frac{16}{3}\cosh^2(1/2),
\]

\[
\|2dd^T\|
<
\frac{16}{3}\sinh^2(1/2).
\]

The component totals are below approximately \(15.93\) even-v and \(10.60\) odd-v.

Adding the direct source-operator action and a \(10^{-8}\) replay-arithmetic reserve gives derived residual-operator perturbation budgets below

\[
3.61\times10^{-6}
\quad\text{(even-v)},
\]

\[
1.22\times10^{-6}
\quad\text{(odd-v)}.
\]

The terminal verifier rounds both up to

\[
\boxed{
\|\Delta Y_\pm\|<10^{-5}.
}
\]

## 6. Outward remote-Gram ceilings

For

\[
Y_{\rm exact}=Y_{\rm point}+\Delta Y,
\]

\[
\|H_{\rm exact}-H_{\rm point}\|
\le
2\|Y_{\rm point}\|\|\Delta Y\|
+
\|\Delta Y\|^2.
\]

Even-v:

\[
\sqrt{0.177788}<0.422,
\]

so

\[
\|H_e-H_{e,\rm point}\|
<
8.4401\times10^{-6},
\]

and

\[
\boxed{
\lambda_{\max}(H_e)
<
0.1777964401.
}
\]

Odd-v:

\[
\sqrt{0.012127}<0.111,
\]

so

\[
\|H_o-H_{o,\rm point}\|
<
2.2201\times10^{-6},
\]

and

\[
\boxed{
\lambda_{\max}(H_o)
<
0.0121292201.
}
\]

## 7. Final terminal comparisons

Even-v:

\[
\boxed{
\gamma_e C_+-H_e
>
2.5752558065895958\,I.
}
\]

Odd-v:

\[
\boxed{
\gamma_o C_--H_o
>
2.7410400211532011\,I.
}
\]

Equivalently, after dividing by the rigorous tail floors,

\[
\boxed{
C_+-\gamma_e^{-1}H_e
>
0.9354176879\,I,
}
\]

\[
\boxed{
C_--\gamma_o^{-1}H_o
>
0.9955943944\,I.
}
\]

Thus the six frozen positive directions remain strongly positive after the infinite remote tail is eliminated.

## 8. Consequence and guardrail

The \(\rho=0.10\) minus-endpoint positivity problem on the exact frozen six-dimensional subspaces is closed:

\[
\boxed{
H_e<\gamma_e C_+,
\qquad
H_o<\gamma_o C_-.
}
\]

This proves positivity of the infinite remote-corrected Schur form on those six frozen directions.

It does not by itself certify the signs of the four complementary effective-core directions, the exact full inertia of \(F^-_{0.10}\), the plus endpoint, the tighter \(\rho=0.02\) endpoint pair, or any exact-zero/RH/GRH statement.

## Result

\[
\boxed{
\lambda_{\max}(H_e)<0.1777964401,
\qquad
\lambda_{\max}(H_o)<0.0121292201.
}
\]

\[
\boxed{
\gamma_e C_+-H_e>2.5752558065895958\,I,
}
\]

\[
\boxed{
\gamma_o C_--H_o>2.7410400211532011\,I.
}
\]

The frozen six-plane positivity certificate for the \(\rho=0.10\) minus endpoint is closed with very large rigorous margins.
