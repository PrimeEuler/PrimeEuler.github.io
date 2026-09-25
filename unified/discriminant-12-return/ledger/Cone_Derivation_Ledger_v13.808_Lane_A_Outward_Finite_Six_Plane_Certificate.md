# Cone Derivation Ledger v13.808 — Outward Finite-Side Certificate for the Frozen \(\rho=0.10\) \(M=3999\) Six-Planes

Date: 2026-09-25

Lane: A.

Status: [C] frozen six-direction finite Schur solves certified in both parity sectors under the validated v13.357 exact-vs-nominal operator budget; [D] fresh endpoint-buffer conditioning bounds; [D] outward six-RHS residual bounds; [G] remote residual-Gram certification remains separate.

Parents: v13.357, v13.396, v13.400, v13.806–807.

Research artifact:

- research-notes/suzuki_endpoint_M3999_frozen_six_direction_finite_certificate.py
- commit \`ba11b6dcb2647754998b6fe1923ec2b617e0fc15\`.

Related hygiene repairs:

- \`80085103f412cd035c44f3e94e050554d6ce9692\` repairs the v13.807 remote-Gram reproducer import;
- \`6921b0ec817e4435ad6189ac5b5d07adf4a75dc5\` annotates v13.807 with that reproducibility correction.

No GitHub workflow/status run is attached to these research commits.

## 1. Certification target

For the fresh worst endpoint
\[
F^-_{0.10}=A-0.10B_{\rm sm},
\]
v13.806 produced ten-dimensional effective cores \(S_\pm\) with midpoint inertia
\[
(4,0,6)
\]
in both parity sectors.

v13.807 froze exact-dyadic \(10\times6\) positive bases \(Q_\pm\) and exact-dyadic \(6\times6\) preconditioners \(L_{0,\pm}\).

The present target is the exact finite-buffer Schur restriction
\[
B_\pm
=
Q_\pm^T
\left(
F_{CC}
-
F_{CF}F_{FF}^{-1}F_{FC}
\right)
Q_\pm
\]
and its normalized form
\[
\boxed{
C_\pm
=
L_{0,\pm}^{-1}
B_\pm
L_{0,\pm}^{-T}.
}
\]

The certificate must prove
\[
C_\pm\succ0
\]
before any infinite remote-tail correction is applied.

## 2. Exact-vs-nominal operator budget [D]

The validated v13.357 dimension-free source-operator uncertainty is
\[
\boxed{
\epsilon_{\rm source}=2\times10^{-13}.
}
\]

The endpoint modification contributes only explicit smooth-bulk and rank-one scalar data. A deliberately conservative additional budget
\[
\boxed{
\epsilon_{\rm endpoint}=10^{-14}
}
\]
is reserved for the binary64 midpoint representation of the \(0.10B_{\rm sm}\) shift and the pole scalar data.

Hence the finite verifier uses
\[
\boxed{
\epsilon_F=2.1\times10^{-13}.
}
\]

This extra endpoint budget is very loose relative to the actual scalar errors: the binary64-vs-high-precision error in \(\log(n/4)\) through \(n=4000\) is below \(4.45\times10^{-16}\), the Hilbert shift is explicit, and the rank-one pole scalars can be over-resolved independently.

## 3. Pole-free endpoint buffer factorization residuals [C]

The structured pole-free endpoint buffers are

even-v:
\[
F_+^{(0)}\ \text{on}\ \{25,27,\ldots,3999\},
\]

odd-v:
\[
F_-^{(0)}\ \text{on}\ \{26,28,\ldots,4000\}.
\]

The completed binary64 structured \(LDL^T\) factors are checked a posteriori by forming the full nominal buffer matrix and bounding
\[
E_F
=
F^{(0)}-LDL^T.
\]

The outward Frobenius bounds, including \(\gamma_n\) matrix-product and subtraction charges, are

\[
\boxed{
\|E_{F,+}\|_2
\le
\|E_{F,+}\|_F
<
5.466\times10^{-11},
}
\]

\[
\boxed{
\|E_{F,-}\|_2
\le
\|E_{F,-}\|_F
<
5.469\times10^{-11}.
}
\]

The midpoint minimum pivots remain

\[
d_{\min,+}
=
0.466081739272534\ldots,
\]

\[
d_{\min,-}
=
0.511129418300039\ldots.
\]

## 4. Outward inverse-factor bounds [C]

For the exact binary64 unit-lower factors \(L\), use the standard absolute recursions

\[
y_i
=
1+\sum_{j<i}|L_{ij}|y_j,
\]

\[
z_j
=
1+\sum_{i>j}|L_{ij}|z_i.
\]

Each positive dot product is evaluated in 64-bit-significand long-double arithmetic and inflated by the corresponding \(\gamma_n\) bound.

This gives

even-v:
\[
\boxed{
\|L_+^{-1}\|_\infty<4.614605,
}
\]
\[
\boxed{
\|L_+^{-1}\|_1<44.50624,
}
\]
\[
\boxed{
\|L_+^{-1}\|_2<14.33104;
}
\]

odd-v:
\[
\boxed{
\|L_-^{-1}\|_\infty<5.015670,
}
\]
\[
\boxed{
\|L_-^{-1}\|_1<55.94764,
}
\]
\[
\boxed{
\|L_-^{-1}\|_2<16.75157.
}
\]

Hence the pole-free nominal endpoint buffers obey

\[
\boxed{
\mu_{0,+}
>
0.00226937786446,
}
\]

\[
\boxed{
\mu_{0,-}
>
0.00182146258801.
}
\]

These bounds are deliberately much weaker than the midpoint spectral minima near \(0.416\), but they are sufficient and are obtained entirely from the completed structured factorization plus its outward residual.

## 5. Corrected odd pole conditioning [C]

In even-v the pole update
\[
+2c_Fc_F^T
\]
is positive and cannot reduce the buffer floor.

In odd-v the corrected pole update is
\[
-2d_Fd_F^T.
\]

Let
\[
y=(F_-^{(0)})^{-1}d_F.
\]

The long-double solve has outward residual
\[
\boxed{
\|d_F-F_-^{(0)}\widehat y\|_2
<
1.63\times10^{-16}.
}
\]

Using the pole-free inverse bound, this gives an error below \(9\times10^{-14}\) in \(y\). The corresponding Sherman-Morrison denominator satisfies

\[
\boxed{
1-2d_F^T(F_-^{(0)})^{-1}d_F
>
0.9870091073767.
}
\]

The resulting nominal full odd-buffer inverse bound gives

\[
\boxed{
\mu_{-,{\rm nominal}}
>
0.00182140889323.
}
\]

After the exact-vs-nominal endpoint perturbation,

\[
\boxed{
\mu_{+,{\rm exact}}
>
0.00226937786425,
}
\]

\[
\boxed{
\mu_{-,{\rm exact}}
>
0.00182140889302.
}
\]

Equivalently,

\[
\|F_{FF,+}^{-1}\|_2<440.650,
\qquad
\|F_{FF,-}^{-1}\|_2<549.026.
\]

Thus both fresh endpoint buffers are rigorously invertible for the finite certificate.

## 6. Frozen six-right-hand-side solve residuals [C]

Only the frozen positive directions are solved.

Define
\[
B_Q=F_{FC}Q.
\]

For the frozen six-plane solve
\[
F_{FF}Y=B_Q,
\]
the residual is evaluated in long-double arithmetic and charged with the standard \(\gamma_{1988}\) dot-product envelope.

The resulting outward bounds are

\[
\boxed{
\|B_{Q,+}-F_{FF,+}\widehat Y_+\|_2
<
1.29\times10^{-15},
}
\]

\[
\boxed{
\|B_{Q,-}-F_{FF,-}\widehat Y_-\|_2
<
1.93\times10^{-15}.
}
\]

The frozen coupling norms are bounded by outward Frobenius caps

\[
\boxed{
\|B_{Q,+}\|_2<0.788,
}
\]

\[
\boxed{
\|B_{Q,-}\|_2<0.772.
}
\]

Therefore the raw restricted-Schur errors caused by the finite solves satisfy

\[
\boxed{
\epsilon_{{\rm solve},+}
<
4.48\times10^{-13},
}
\]

\[
\boxed{
\epsilon_{{\rm solve},-}
<
8.19\times10^{-13}.
}
\]

## 7. Exact frozen-coordinate reference bounds [D/C]

Because \(Q_\pm\) and \(L_{0,\pm}\) are exact dyadic payloads, their Gram bounds are evaluated exactly with rational arithmetic and Gershgorin.

A conservative common bound is

\[
\|Q_\pm\|_2^2
<
1.00000000000001.
\]

For the frozen preconditioners,

\[
\boxed{
\lambda_{\min}(L_{0,+}L_{0,+}^T)
>
0.0321649112671,
}
\]

\[
\boxed{
\lambda_{\min}(L_{0,-}L_{0,-}^T)
>
0.6598137157128.
}
\]

The outward mismatch between the directly formed nominal restricted Schur matrix and the exact frozen dyadic reference \(L_0L_0^T\) is bounded by

\[
\boxed{
\epsilon_{{\rm ref},+}
<
9.20\times10^{-16},
}
\]

\[
\boxed{
\epsilon_{{\rm ref},-}
<
1.29\times10^{-15}.
}
\]

## 8. Exact-vs-nominal restricted Schur perturbation [C]

For a fixed frozen \(Q\), let

\[
K_Q=\|F_{FC}Q\|_2,
\qquad
q=\|Q\|_2.
\]

The block-resolvent estimate gives

\[
\|\Delta B\|
\le
q^2\epsilon_F
+
\frac{2K_Qq\epsilon_F}{\mu-\epsilon_F}
+
\frac{q^2\epsilon_F^2}{\mu-\epsilon_F}
+
\frac{K_Q^2\epsilon_F}
{\mu(\mu-\epsilon_F)}.
\]

Using the certified finite-buffer floors and frozen coupling caps gives

\[
\boxed{
\epsilon_{{\rm source},+}
<
2.547\times10^{-8},
}
\]

\[
\boxed{
\epsilon_{{\rm source},-}
<
3.791\times10^{-8}.
}
\]

This term dominates the finite-side error budget. The actual arithmetic solve residual is negligible by comparison.

## 9. Rigorous finite six-plane margins [C]

Combining

\[
\epsilon_{\rm ref}
+
\epsilon_{\rm solve}
+
\epsilon_{\rm source}
\]

gives raw restricted-Schur perturbation bounds

\[
\boxed{
\epsilon_{{\rm finite},+}
<
2.547\times10^{-8},
}
\]

\[
\boxed{
\epsilon_{{\rm finite},-}
<
3.791\times10^{-8}.
}
\]

More precisely, the computed scalar budgets are approximately

\[
2.54662\times10^{-8}
\quad\text{and}\quad
3.79049\times10^{-8}.
\]

Therefore the exact finite restricted Schur forms obey

\[
\boxed{
\lambda_{\min}
\left(
Q_+^TS_{+,{\rm exact}}Q_+
\right)
>
0.03216488580,
}
\]

\[
\boxed{
\lambda_{\min}
\left(
Q_-^TS_{-,{\rm exact}}Q_-
\right)
>
0.65981367780.
}
\]

After frozen \(L_0\) normalization,

\[
\boxed{
C_+
>
0.99999920\,I,
}
\]

\[
\boxed{
C_-
>
0.99999994\,I.
}
\]

Using the unrounded computed budgets,

\[
\boxed{
\lambda_{\min}(C_+)
>
0.9999992082,
}
\]

\[
\boxed{
\lambda_{\min}(C_-)
>
0.9999999425.
}
\]

Thus the six positive finite directions are rigorously protected with normalized losses below

\[
8\times10^{-7}
\quad\text{even-v},
\]

\[
6\times10^{-8}
\quad\text{odd-v}.
\]

## 10. Consequence and remaining gate

The finite part of the \(\rho=0.10\) minus-endpoint certificate is now closed on the exact frozen six-planes.

The remaining load-bearing inequality is entirely on the infinite remote correction:

\[
H_\pm
<
\delta_{\rm tail,\pm} C_\pm.
\]

v13.807 supplies very favorable midpoint remote-Gram targets, but those Gram ceilings still require their own outward replay.

The finite certificate proved here must therefore be held fixed while the remote calculation is certified; no basis regeneration is permitted.

## Result

\[
\boxed{
\textbf{The frozen six-direction finite Schur solves are outward-certified in both parity sectors.}
}
\]

\[
\boxed{
\lambda_{\min}(C_+)>0.9999992082,
\qquad
\lambda_{\min}(C_-)>0.9999999425.
}
\]

No infinite endpoint inertia theorem is promoted in this entry because the remote residual-Gram replay is still a separate certification gate.
