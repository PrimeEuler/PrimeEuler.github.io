# Cone Derivation Ledger v13.807 — Frozen Six-Direction \(M=3999\) Endpoint Bases and Normalized Remote Residual Grams

Date: 2026-09-25

Lane: A.

Status: [D] exact-dyadic six-direction freezes in both parity sectors; [N] frozen-coordinate normalized remote residual-Gram replay through two million; [N] coarse far-tail envelopes; [I] large midpoint margin relative to the v13.804 raw endpoint-tail floors; [G] no infinite endpoint inertia theorem promoted yet.

Parents: v13.804–806.

Research artifacts:

- research-notes/suzuki_endpoint_M3999_frozen_six_direction_inputs.py
- commit d20a4202996d53ef22aa1fc36e9a1b39498731eb

- research-notes/suzuki_endpoint_M3999_frozen_six_direction_remote_gram.py
- commits 6d772d9aa9dda460bbf9d325082009f541a6b6f2 and 0b6e5181dec94d1d02fd82d4669661aec9e04c8c

Implementation hygiene:

- commit db5c628ff63f088fc7be6b46aef053a45666104b corrects the near-zero Taylor fallback in the v13.806 midpoint builder from the erroneous \(-11t/48\) coefficient to
  \[
  h(t)=\frac14-\frac{t}{48}-\frac{t^2}{32}+\frac{7t^3}{11520}+\cdots.
  \]
  Re-running the fresh \(M=3999/4000\) midpoint problems leaves every v13.806 displayed pivot/eigenvalue unchanged at the reported precision.

No GitHub workflow/status run is attached to these research commits.

## 1. Frozen positive six-planes [D]

For each \(10\times10\) effective core from v13.806, take the six positive midpoint eigenvectors.

Column signs are canonicalized by requiring the largest-magnitude component of each column to be positive.

The resulting \(10\times6\) matrices \(Q_\pm\) and the \(6\times6\) midpoint Cholesky factors
\[
L_{0,\pm}L_{0,\pm}^T
=
Q_\pm^TS_\pm Q_\pm
\]
are stored as exact IEEE-754 hexadecimal dyadics.

They are verifier inputs, not quantities to be regenerated during an outward replay.

### even-v frozen payload

SHA-256:
\[
\boxed{
\texttt{af158c4f87c4d90e7c23b0f0ef2adb4dbb8f27cd88d96efa1563cb6fd546d5b0}.
}
\]

The exact-dyadic determinant of the first six rows is nonzero; its decimal diagnostic is
\[
\det Q_{+,1:6}
\approx
-3.96645702505283\times10^{-6}.
\]

The binary64 orthonormality diagnostic is
\[
\|Q_+^TQ_+-I\|_2
\approx
1.2151\times10^{-15}.
\]

The Cholesky diagonal is approximately
\[
0.17934579,\ 
0.96228561,\ 
1.25644000,\ 
1.38575156,\ 
1.51913074,\ 
1.56799729.
\]

### odd-v frozen payload

SHA-256:
\[
\boxed{
\texttt{c983603a88bbdc9d9a217cb8c6936fb5b05ae56d84f9c85e5baf8bf1924ec9eb}.
}
\]

The exact-dyadic first-six-row determinant is nonzero, with decimal diagnostic
\[
\det Q_{-,1:6}
\approx
-2.638188240960451\times10^{-7}.
\]

The orthonormality diagnostic is
\[
\|Q_-^TQ_--I\|_2
\approx
1.4839\times10^{-15}.
\]

The Cholesky diagonal is approximately
\[
0.81228918,\ 
1.17040207,\ 
1.30769572,\ 
1.38555918,\ 
1.51986385,\ 
1.57813250.
\]

Thus rank six and preconditioner invertibility are exact properties of the frozen dyadic payloads.

## 2. Dressed finite six-planes [D/N]

For each parity let
\[
X=F_{FF}^{-1}F_{FC}
\]
be the fresh \(M=3999/4000\) midpoint high-buffer solve from v13.806.

The dressed finite six-plane is
\[
\boxed{
W=
\begin{pmatrix}
Q\\
-XQ
\end{pmatrix}.
}
\]

Residual rows against remote coordinate modes are computed using the full endpoint pencil
\[
F^-_{0.10}=A-0.10B_{\rm sm},
\]
including

\[
+2cc^T
\quad\text{in even-v},
\]
and
\[
-2dd^T
\quad\text{in corrected odd-v}.
\]

The remote starts are

\[
4001,4003,\ldots
\quad\text{for even-v},
\]
and
\[
4002,4004,\ldots
\quad\text{for odd-v}.
\]

## 3. Normalized residual Gram [D/N]

Let \(R_n\) be the six-component residual row at remote mode \(n\), and define
\[
G_N
=
\sum_{n\le N}R_n^TR_n.
\]

The normalized Gram is
\[
\boxed{
H_N
=
L_0^{-1}G_NL_0^{-T}.
}
\]

Residual rows are accumulated directly through mode \(16001/16000\), then by the exact eight-level inverse-power expansion through two million.

### even-v through two million

The normalized Gram is

\[
H_{e,2M}\approx
\begin{pmatrix}
1.7478307281\!\times10^{-1}&1.8718120708\!\times10^{-2}&7.6859228018\!\times10^{-3}&5.8857034208\!\times10^{-3}&-2.5185912263\!\times10^{-3}&-2.1839659192\!\times10^{-3}\\
1.8718120708\!\times10^{-2}&2.0045884838\!\times10^{-3}&8.2311204243\!\times10^{-4}&6.3032011342\!\times10^{-4}&-2.6972478489\!\times10^{-4}&-2.3388901216\!\times10^{-4}\\
7.6859228018\!\times10^{-3}&8.2311204243\!\times10^{-4}&3.3798132328\!\times10^{-4}&2.5881829739\!\times10^{-4}&-1.1075274539\!\times10^{-4}&-9.6038002376\!\times10^{-5}\\
5.8857034208\!\times10^{-3}&6.3032011342\!\times10^{-4}&2.5881829739\!\times10^{-4}&1.9819716466\!\times10^{-4}&-8.4811838450\!\times10^{-5}&-7.3543463328\!\times10^{-5}\\
-2.5185912263\!\times10^{-3}&-2.6972478489\!\times10^{-4}&-1.1075274539\!\times10^{-4}&-8.4811838450\!\times10^{-5}&3.6292490313\!\times10^{-5}&3.1470743126\!\times10^{-5}\\
-2.1839659192\!\times10^{-3}&-2.3388901216\!\times10^{-4}&-9.6038002376\!\times10^{-5}&-7.3543463328\!\times10^{-5}&3.1470743126\!\times10^{-5}&2.7289950186\!\times10^{-5}
\end{pmatrix}.
\]

Its numerical eigenvalues are

\[
\sim0,\ \sim0,\ \sim0,\
5.3075\times10^{-15},\
1.2908132\times10^{-9},\
\boxed{0.177387420928682}.
\]

The tiny signed \(10^{-19}\)-scale values produced by binary64 eigensymmetrization are roundoff around the positive-semidefinite zero cluster.

Thus the Gram is numerically almost rank one.

### odd-v through two million

\[
H_{o,2M}\approx
\begin{pmatrix}
8.4639523699\!\times10^{-3}&3.6087940807\!\times10^{-3}&1.7893200098\!\times10^{-3}&3.4555642969\!\times10^{-3}&-8.9364895577\!\times10^{-4}&1.3345802613\!\times10^{-3}\\
3.6087940807\!\times10^{-3}&1.5386895138\!\times10^{-3}&7.6291633756\!\times10^{-4}&1.4733566115\!\times10^{-3}&-3.8102708137\!\times10^{-4}&5.6902796519\!\times10^{-4}\\
1.7893200098\!\times10^{-3}&7.6291633756\!\times10^{-4}&3.7827082825\!\times10^{-4}&7.3052286932\!\times10^{-4}&-1.8892166477\!\times10^{-4}&2.8213671155\!\times10^{-4}\\
3.4555642969\!\times10^{-3}&1.4733566115\!\times10^{-3}&7.3052286932\!\times10^{-4}&1.4107978329\!\times10^{-3}&-3.6484863389\!\times10^{-4}&5.4486709973\!\times10^{-4}\\
-8.9364895577\!\times10^{-4}&-3.8102708137\!\times10^{-4}&-1.8892166477\!\times10^{-4}&-3.6484863389\!\times10^{-4}&9.4354082153\!\times10^{-5}&-1.4090890947\!\times10^{-4}\\
1.3345802613\!\times10^{-3}&5.6902796519\!\times10^{-4}&2.8213671155\!\times10^{-4}&5.4486709973\!\times10^{-4}&-1.4090890947\!\times10^{-4}&2.1043431597\!\times10^{-4}
\end{pmatrix}.
\]

Its eigenvalues are

\[
\sim0,\ \sim0,\ \sim0,\
4.8848\times10^{-14},\
2.8142531\times10^{-10},\
\boxed{0.0120964986614671}.
\]

The odd residual Gram is therefore even smaller and likewise essentially rank one.

## 4. Leading \(1/n\) channel [N]

The endpoint large-\(n\) residual coefficient is the v13.805 shifted channel.

After normalization by \(L_0^{-T}\), the squared leading-channel norms are

\[
\boxed{
\|L_e^{\rm norm}\|^2
\approx1520.23402810775,
}
\]
\[
\boxed{
\|L_o^{\rm norm}\|^2
\approx103.184538287410.
}
\]

The dominant Gram eigenvector is almost exactly the normalized leading channel:

\[
\boxed{
|\langle u_{\max,e},\widehat L_e\rangle|
\approx0.999999998681,
}
\]
\[
\boxed{
|\langle u_{\max,o},\widehat L_o\rangle|
\approx0.999999995625.
}
\]

Thus the remote six-plane coupling is not merely low rank numerically; its dominant direction is exactly the asymptotic \(1/n\) channel anticipated by the source-faithful Cauchy expansion.

## 5. Coarse far-tail envelope beyond two million [N-target]

Using the inverse-power residual expansion and the deliberately coarse bound
\[
|Z_n|\le8
\]
for the remote endpoint generator, the normalized Gram contribution beyond two million is bounded at midpoint-envelope level by

\[
\boxed{
H_{e,>2M}^{\rm env}
<
3.804616856\times10^{-4},
}
\]
\[
\boxed{
H_{o,>2M}^{\rm env}
<
2.582370444\times10^{-5}.
}
\]

Therefore the scalar midpoint ceilings are

\[
\boxed{
\lambda_{\max}(H_e^{\rm full})
\lesssim
0.177767882614278,
}
\]
\[
\boxed{
\lambda_{\max}(H_o^{\rm full})
\lesssim
0.0121223223659066.
}
\]

These are not yet outward-rounded interval bounds; they are verifier targets.

## 6. Comparison with the analytic endpoint remote floors [I]

v13.804 gives the raw \(\rho=0.10\) endpoint-tail lower bounds at the actual M3999 remote starts:

\[
\gamma_e(4001)
\approx
2.75305442655809,
\]
\[
\gamma_o(4002)
\approx
2.75316939956044.
\]

If these raw coordinate-tail floors are used in the same exact Schur split, the midpoint normalized correction ratios are only

\[
\boxed{
\frac{0.177767882614278}{2.75305442655809}
\approx
0.0645711
}
\]
for even-v, and

\[
\boxed{
\frac{0.0121223223659066}{2.75316939956044}
\approx
0.00440304
}
\]
for odd-v.

The corresponding nominal normalized positive margins are therefore roughly

\[
0.9354
\quad\text{and}\quad
0.9956.
\]

This is much larger than the historical unshifted M3999 verifier margin.

No theorem is promoted from this comparison until the finite solve, frozen-coordinate normalization, explicit Gram accumulation, far-tail envelope, and the raw endpoint-tail floor are all replayed in one outward-rounded arithmetic contract.

## 7. Consequence for the certification route

The six positive directions are now no longer moving numerical objects.

They are frozen exact-dyadic verifier coordinates with hash identities, exact rank six, and fixed preconditioners.

The remote residual data show that:

1. both parity residual Grams are essentially rank one;
2. the dominant Gram direction is the analytically known \(1/n\) channel;
3. odd-v is extremely far from the positivity boundary;
4. even-v also has a very large nominal margin when paired with the endpoint raw-tail floor.

Therefore the next gate should be an outward replay of this exact frozen contract, not another larger midpoint calculation.

The main validation tasks are:

- outward finite \(M=3999/4000\) solve residuals;
- exact-vs-nominal source-operator perturbation;
- outward evaluation of the frozen \(6\times6\) normalized finite matrices;
- outward accumulation/enclosure of the explicit remote Gram;
- rigorous \(|Z_n|\le8\) or sharper endpoint-generator far-tail bound;
- direct certification of the v13.804 raw endpoint-tail floors at \(4001/4002\).

## Result

\[
\boxed{
\textbf{The six positive M3999 endpoint directions are frozen exactly in both parities.}
}
\]

\[
\boxed{
\lambda_{\max}(H_{e,2M})
\approx0.177387420928682,
\qquad
\lambda_{\max}(H_{o,2M})
\approx0.0120964986614671.
}
\]

\[
\boxed{
\textbf{Both normalized remote Grams are overwhelmingly rank one and aligned with the exact asymptotic }1/n\textbf{ channel.}
}
