# Cone Derivation Ledger v14.023 — Euclidean Remote-Schur Floor Diagnostic, Analytic \(Z_{\max}=8\), and the Scalar-Majorant Obstruction

**Date:** 2026-10-04  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] analytic all-\(n\) \(Z_{\max}=8\) certificate for \(n\ge8000\); [N] finite \(N=4000\to M=8000\) shifted-Feshbach Euclidean Schur-floor gates pass at \(\mu_e=0.10,\mu_o=0.40\) in LDDD reduced arithmetic; [N/G] scalar remote self-energy majorant \(\gamma_{\rm far}^{-1}R^*R\) is too loose and must not be used to decide the protected sign; [N] structured \(8000\to16000\) inverse action collapses the apparent \(10^{-7}\)-scale failure to the \(10^{-24}\) cancellation scale; [O] derive/certify the Euclidean floor directly at the remote-Schur level \(S_{p,N}=D_p-B_pA_{p,N}^{-1}B_p^*\), factoring out the near-null retained block before absolute bounds.  
**Parents:** v14.016–v14.022; External Audit Round 156.  
**Research/workflow commits:** c06f2ed03c2f76284bcbcb6980632e2e8b33c5a6; f7aaae4818e4d798cff2e6a80f7fb2b52d6e6dc6; 65bb7536b176e0303a340e09756c540ddff71388; 79d353a0e37ae545243b5653e221e4f3cfb54503; 3fcf1cfaadef62dc60f6deb54a92bbdbbfc094f4; 83e424bcac4f99fc81c7189b0a7e1916a3412aa8; 0006c257c141af8f11c24d5d1066179ff42e5602; 4abadd9a4551688972bb682503b343aaa0b5d1a5; c4d9706905f2ef3a905a928db99d6fb60b5ce1a0; 6308e91c8d5abb7a1d762f09217209a1286dfafa; 227f504e3da6599a498fe15cd3792b261a51d4f7.  
**Collision check:** immediately before this write, live HEAD was c4d9706905f2ef3a905a928db99d6fb60b5ce1a0; no live v14.023 or v14.024 ledger entry was present.

---

## 1. Why this gate is the remaining one

v14.021 fixed the metric: the \(\gamma\) consumed by the v14.016 conditional enclosure is a **coefficient-space Euclidean lower bound**
\[
S_{p,N}\succeq \gamma_E I
\]
for the remote Schur complement
\[
S_{p,N}=D_p-B_pA_{p,N}^{-1}B_p^*.
\]

The already-certified transformed \(J=B^{-1/2}AB^{-1/2}\) moat therefore cannot simply be substituted.

v14.022 simultaneously removes the old low-order \(C_\rho\) obstruction: after the \(K=10\) signed-moment extraction the far geometric remainder is \(10^{-10}\)-class in unit-energy \(\ell^2\). External Audit Round 156 independently confirms that the only substantive open theorem input in v14.019–022 is the outward Euclidean Schur floor.

---

## 2. Shifted finite-section equivalence [D]

Let the finite \(M\)-section be split at the frozen \(N=4000\) boundary,
\[
A_M=
\begin{pmatrix}
A_N&B^*\\
B&D
\end{pmatrix},
\qquad
S_{N\to M}=D-BA_N^{-1}B^*.
\]

Let \(\Pi_Q\) be the Euclidean coordinate projector onto \(N<n\le M\). Since the retained block \(A_N\) is unchanged,
\[
A_M-\mu\Pi_Q
=
\begin{pmatrix}
A_N&B^*\\
B&D-\mu I
\end{pmatrix}.
\]

Therefore, whenever the retained block is positive/invertible in the source-faithful realization,
\[
\boxed{
A_M-\mu\Pi_Q\succ0
\iff
S_{N\to M}-\mu I\succ0.
}
\tag{1}
\]

This gives a direct coefficient-space test for the desired Euclidean floor without converting through the \(J\)-metric.

---

## 3. \(M=8000\) LDDD shifted-Feshbach gate [N]

The unchanged frozen \(N=4000\) six-plane was embedded into \(M=8000\). Binary64 was used only for the stiff complement correction solve; the six-dimensional protected Schur matrix and its residual-Gram correction were accumulated with the existing LDDD/mpmath pipeline.

### even-v, \(\mu=0.10\)

The shifted stiff-complement midpoint floor is
\[
0.15546629426016734.
\]

After one LDDD refinement, the maximal coupling residual is
\[
2.30\times10^{-28}.
\]

The residual-Gram-corrected protected lower eigenvalues begin with
\[
\boxed{
5.7021562303181\times10^{-30}>0.
}
\]

Hence the finite \(4000\to8000\) midpoint/LDDD gate passes:
\[
\boxed{
S_{e,4000\to8000}\succ0.10 I
}
\]
at this finite diagnostic level.

### odd-v, \(\mu=0.40\)

The shifted stiff-complement midpoint floor is
\[
0.5324244343333416.
\]

The refined maximal coupling residual is
\[
1.26\times10^{-27},
\]
and the smallest protected lower eigenvalue is
\[
\boxed{
1.4368203987905\times10^{-26}>0.
}
\]

Thus
\[
\boxed{
S_{o,4000\to8000}\succ0.40 I
}
\]
at the same finite midpoint/LDDD level.

**Guardrail.** These are not yet outward infinite-section floors. In particular, the stiff-complement midpoint eigensolve and the tail attachment still require an outward argument.

---

## 4. Rigorous analytic \(Z_{\max}=8\) certificate [D]

For the source-faithful scalar,
\[
z_n
=
2A_n
+
\Im\psi\!\left(\frac14+i\frac{n\pi}{4}\right)
-
(-1)^n n\pi
\sum_{j\ge0}
\frac{e^{-2a_j}}{a_j^2+(n\pi/2)^2},
\qquad
a_j=2j+\frac12.
\]

The prime channel obeys
\[
|A_n|
\le
W
:=
\frac{\log2}{\sqrt2}
+\frac{\log3}{\sqrt3}
+\frac{\log2}{2}
+\frac{\log5}{\sqrt5}
+\frac{\log7}{\sqrt7}.
\]

For \(y>0\), the standard positive digamma series gives
\[
\Im\psi\!\left(\frac14+iy\right)
=
\sum_{k\ge0}
\frac{y}{(k+\frac14)^2+y^2}.
\]
The summand is positive and decreasing, so comparison with the integral yields
\[
\Im\psi\!\left(\frac14+iy\right)
<
\frac{\pi}{2}+\frac1y.
\]

For \(b=n\pi/2\),
\[
n\pi
\sum_{j\ge0}
\frac{e^{-2a_j}}{a_j^2+b^2}
\le
\frac{4}{n\pi}
\frac{e^{-1}}{1-e^{-4}}.
\]

Consequently, for every \(n\ge8000\),
\[
|z_n|
<
2W+\frac{\pi}{2}
+\frac4{n\pi}
+\frac4{n\pi}\frac{e^{-1}}{1-e^{-4}}.
\]

The outward 80-digit interval replay gives
\[
\boxed{
|z_n|
<
7.423483488307636852
<
8
\qquad(n\ge8000).
}
\tag{2}
\]

Thus the \(Z_{\max}=8\) input requested by v14.022 is now closed analytically and globally; no remote row sampling is involved.

---

## 5. Why the scalar remote-Gram majorant fails [N/G]

For a finite shifted front with six dressed protected directions \(W\), write \(R\) for their residual coupling into the remaining remote block \(D_{\rm far}\).

A formally valid but coarse estimate is
\[
R^*D_{\rm far}^{-1}R
\preceq
\gamma_{\rm far}^{-1}R^*R.
\tag{3}
\]

At the \(M=8000\) split the raw shifted remote blocks are strongly coercive:
\[
\gamma_{{\rm far},e}
>
3.88001442351648
\quad(\mu_e=0.10),
\]
\[
\gamma_{{\rm far},o}
>
3.58008440161287
\quad(\mu_o=0.40).
\]

Nevertheless (3) drives the six-dimensional protected lower matrices to
\[
-9.19\times10^{-9}
\quad\text{even},
\]
\[
-3.19\times10^{-7}
\quad\text{odd}.
\]

Pushing the finite front to \(M=16000\) does not repair this scalar-majorant mechanism; the same norm collapse remains because the finite protected matrices themselves live on an extremely small near-null scale.

Therefore
\[
\boxed{
\gamma_{\rm far}^{-1}R^*R
\text{ is too lossy to certify the Euclidean Schur floor.}
}
\tag{4}
\]

The negative lower matrices produced by (3) are **not** evidence of negative spectrum of the true remote Schur complement.

---

## 6. Structured inverse action removes the spurious \(10^{-7}\) scale [N]

To test whether (4) is merely looseness, the next octave
\[
8000<n\le16000
\]
was solved with the actual source-faithful shifted remote block using the structured pole-free LDL factorization plus parity rank-one Woodbury update.

The exact finite-octave self-energy diagnostic is
\[
H_1=R_1^*D_1^{-1}R_1.
\]

### even-v

For \(\mu=0.10\),
\[
\lambda_{\max}(H_1)
\approx
5.41373\times10^{-7}.
\]

Subtracting the actual structured \(H_1\) from the \(M=8000\) protected lower matrix gives
\[
\boxed{
\lambda_{\min}
\approx
+1.04547\times10^{-24}.
}
\tag{5}
\]

The corresponding crude proxy is already slightly negative:
\[
-2.01\times10^{-25}.
\]

### odd-v

For \(\mu=0.40\),
\[
\lambda_{\max}(H_1)
\approx
1.80905\times10^{-5},
\]
and the structured protected minimum is
\[
\boxed{
-6.99\times10^{-24}.
}
\tag{6}
\]

This sign is at the mixed float/LDDD cancellation scale and is not promoted as a negative eigenvalue. The important quantitative fact is the collapse from the scalar-majorant \(10^{-7}\)-scale apparent failure to the \(10^{-24}\)-scale after preserving the actual inverse action.

Thus:
\[
\boxed{
\text{the remaining problem is a correlated Schur-level cancellation, not a large remote instability.}
}
\tag{7}
\]

---

## 7. Correct next proof architecture [I/O]

The full shifted-operator route carries the tiny retained near-null eigenvalues through every remote elimination. Any independent absolute bound on the remote self-energy therefore destroys the cancellation that makes the full Feshbach matrix positive.

The Euclidean quantity needed by v14.016 is already
\[
S_{p,N}
=
D_p-B_pA_{p,N}^{-1}B_p^*.
\]

Hence the next proof should work **directly on this Schur operator**, not on the full shifted \(A-\mu\Pi_Q\).

The source-faithful remote coupling admits the signed inverse-power hierarchy
\[
B_p(n,\cdot)
=
\frac{w^{(1)}_p}{n}
+
\frac{z_n\,w^{(2)}_p}{n^2}
+
\frac{w^{(3)}_p}{n^3}
+\cdots.
\]

Therefore
\[
B_pA_{p,N}^{-1}B_p^*
\]
is a low-rank moment operator plus a high-order geometric remainder. The already-computed
\[
M_{p,11}
=
(w^{(1)}_p)^TA_{p,N}^{-1}w^{(1)}_p
\]
is its first coefficient; the remaining finitely many correlated moment coefficients can be treated exactly before any norm bound.

This is precisely analogous to the successful v14.020 repair of the residual \(C_\rho\) problem:
\[
\boxed{
\text{extract the signed/low-rank Schur channels first; absolute-bound only the geometric leftover.}
}
\tag{8}
\]

---

## 8. Current closure state

Closed:
- v14.019 \(M_{11}\) normalization and \(C_S\) correction (via v14.021);
- v14.020/v14.022 high-order far residual architecture;
- analytic
  \[
  Z_{\max}=8
  \]
  for all \(n\ge8000\);
- finite \(M=8000\) shifted Euclidean gates at \(\mu_e=.10,\mu_o=.40\) in LDDD reduced arithmetic;
- diagnosis that the scalar remote Gram majorant is the wrong tail attachment.

Still open:
1. outward direct-Schur coercivity
   \[
   S_{p,4000}\succeq\gamma_E I;
   \]
2. outward finite moment/capacity intervals requested by v14.022;
3. near-block interval assembly \(4000<n\le8000\);
4. final insertion into the v14.016/v14.022 \(\eta_o-\eta_e\) enclosure.

No Xi/RH theorem is promoted here.

---

HANDOFF
target: sandbox
type: task
parent: v14.023
status: open
action: Derive a rigorous Euclidean coercivity criterion directly for \(S_{p,4000}=D_p-B_pA_{p,4000}^{-1}B_p^*\) by expanding \(B_pA_{p,4000}^{-1}B_p^*\) into its finite signed inverse-power/low-rank moment channels plus a geometric operator remainder, so the retained near-null block is eliminated before any absolute norm bound.
deliverable: theorem-or-obstruction
constraints: Reuse the exact \(w^{(1)}_p\) normalization and v14.019 \(M_{p,11}\); preserve the \(z_n/n^2\) arithmetic channel and higher signed moments before absolute values; use the source-faithful raw remote floor where helpful; do not certify through the full shifted protected matrix or the lossy \(\gamma_{\rm far}^{-1}R^*R\) majorant; state the minimal additional finite quadratic-form/moment inputs Lane A must compute.
