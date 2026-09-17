# Cone Derivation Ledger v13.555 — M16001 remaining outward-certification DAG

## Scope

This entry freezes the dependency architecture for the remaining M16001 seven-plane outward-arithmetic certification. It does **not** report a new numerical enclosure and does **not** promote the theorem status.

The previously certified status remains

\[
\operatorname{ind}_{\le 0}(A_{\rm even}(1))\le 4,
\qquad
\operatorname{ind}_{\le 0}(A_{a=1})\le 6.
\]

The purpose here is to separate the remaining source leaves, state exactly which downstream quantities each controls, and fix the pre-Gram propagation formula so later implementations do not confuse nominal reduction rounding with operand/source uncertainty.

## Remaining source leaves

| Source leaf | Certification status | Exact downstream quantities controlled | Endpoint theorem component affected |
|---|---|---|---|
| Frozen exact-dyadic \(Q,L_0\) | payload exact; derived \(P=QL_0^{-T}\) arithmetic still open | \(P\to\mathcal B=[P,N]\to W\); finite QQ/QN/NN projection | \(\lambda_Q^L,\ \|B_{QN}\|_2^U\); remote Gram; \(f_Q,f_N,f_X\) |
| \(N\subset\ker Q^T\) | **open**: current basis comes from numerical SVD and lacks an exact/outward certificate | \(\mathcal B\to W\to p,a_q,b_q,S_Z,S_J,S_{J^2Z}\) | all finite Q/N, remote-Gram and far-tail endpoints |
| Frozen \(X\) | payload conversion closed by v13.533; residual/primitive propagation substantially certified | \(X\mathcal B\to W\to p,a_q,b_q,S_Z,S_J,S_{J^2Z}\) | remote Gram and \(f_Q,f_N,f_X\) |
| finite \(Z_j\), odd \(1\le j\le16001\) | payload conversion closed by v13.532; exact-vs-nominal source uncertainty remains separate | \(b_q=\sum Z_jj^{2q}W_j\), \(S_Z=Z^TW\), \(S_{J^2Z}=\sum j^2Z_jW_j\) | remote Gram through \(b_q\); far \(L,C\to f_Q,f_N,f_X\) |
| finite \(c_j\) | payload conversion closed by v13.532; source uncertainty remains separate | \(p=c^TW\) | remote pole branch; far \(L,C\to f_Q,f_N,f_X\) |
| remote \(Z_n^{\rm tail}\), odd \(16003\le n\le1999999\) | **open**: dynamic `tail_Z(n)` lacks an outward source/evaluation enclosure | \(Z_n^{\rm tail}a_qn^{-(2q+2)}\to R_n\to E_{\rm preGram}\) | explicit remote-Gram upper enclosure only |
| \(\pi\) | frozen payload conversion closed; exact transcendental enclosure/propagation still required | \(2/\pi\), \(k_n=n\pi/2\), \(c_n\), `tail_Z(n)`, far coefficients | remote Gram and \(f_Q,f_N,f_X\) |
| \(h=\cosh(1/2)\) | **open** as outward transcendental constant | \(c_n=2k_nh/(k_n^2+1/4)\); far pole terms in \(L,C\) | remote Gram and \(f_Q,f_N,f_X\) |
| exact integer powers / reciprocals | integer inputs exact; floating power/reciprocal realization still needs directed evaluation | \(a_q,b_q\), \(n^{-(2q+1)}\), \(n^{-(2q+2)}\), \(S_2,S_4,S_6\) | remote Gram and \(f_Q,f_N,f_X\) |
| \(N_{\rm far}=2000001\), \(\rho=16001/2000001\) | exact rational leaf available; current diagnostic uses ordinary floating evaluation | \((1-\rho^2)^{-1}\), \(S_r=N^{-r}+[2(r-1)N^{r-1}]^{-1}\) | far \(f_Q,f_N,f_X\) only |

## Remote-row factorization

For each remote odd \(n\), write

\[
R_n=T_n+H_n,
\]

with

\[
T_n=\frac2\pi\sum_{q=0}^{7}\left(
Z_n^{\rm tail}a_q n^{-(2q+2)}-b_q n^{-(2q+1)}
\right),
\]

\[
H_n=2c_np,
\qquad
c_n=\frac{2k_n\cosh(1/2)}{k_n^2+1/4},
\qquad
k_n=\frac{n\pi}{2}.
\]

The basis-dependent quantities are

\[
\mathcal B=[P,N],\qquad
W=\begin{bmatrix}\mathcal B\\-X\mathcal B\end{bmatrix},
\qquad
p=c^TW,
\]

\[
a_q=\sum_j j^{2q+1}W_j,
\qquad
b_q=\sum_j Z_jj^{2q}W_j.
\]

The basis-independent remote leaves are \(Z_n^{\rm tail}\), \(\pi\), \(\cosh(1/2)\), and exact integer \(n\) with its directed inverse powers.

If

\[
R_{ni}=\widehat R_{ni}+\delta_{ni},
\qquad
|\delta_{ni}|\le\rho_{ni},
\]

then the missing operand/row-formation contribution to one Gram entry is

\[
\boxed{
E^{\rm preGram}_{ij}
=
\sum_n\left(
|\widehat R_{ni}|\rho_{nj}
+|\widehat R_{nj}|\rho_{ni}
+\rho_{ni}\rho_{nj}
\right).
}
\]

Equivalently, chunkwise with midpoint matrix \(\widehat R\) and radius matrix \(\rho_R\),

\[
E^{\rm preGram}
=|\widehat R|^T\rho_R
+\rho_R^T|\widehat R|
+\rho_R^T\rho_R.
\]

The final explicit remote-Gram entry radius is then

\[
\boxed{
E^G_{ij}
=E^{\rm preGram}_{ij}
+E^{\rm gramRnd}_{ij}
+E^{\rm chunkAdd}_{ij}.
}
\]

The latter two terms are already represented by the v13.512 gamma transcript. The first term is the still-missing row-formation propagation. This separation is mandatory to avoid either omission or double counting.

## Far-tail branch

The far branch reuses \(W,p,Z_j\) but does **not** depend on the dynamically evaluated remote \(Z_n^{\rm tail}\). Define

\[
S_Z=Z^TW,
\qquad
S_J=\sum_j jW_j,
\qquad
S_{J^2Z}=\sum_jj^2Z_jW_j.
\]

The existing gamma transcript already charges the nominal reductions for these three moments. What remains is outward propagation of their operand radii and the downstream interval operations

\[
L=-\frac2\pi S_Z+\frac{8\cosh(1/2)}\pi p,
\]

\[
B=\frac{16/\pi}{1-\rho^2}\sum_j|jW_j|,
\]

\[
C=\frac{2/\pi}{1-\rho^2}\sum_j|j^2Z_jW_j|
+\frac{8\cosh(1/2)}{\pi^3}|p|.
\]

For each block \(s\), evaluate outward

\[
E_s=
\left(
\|L_s\|_2\sqrt{S_2}
+\|B_s\|_2\sqrt{S_4}
+\|C_s\|_2\sqrt{S_6}
\right)^2,
\]

then retain only adverse upper endpoints

\[
\boxed{f_Q^U,\qquad f_N^U,\qquad f_X^U=\sqrt{f_Q^Uf_N^U}.}
\]

This branch can be closed independently of the million-row `tail_Z(n)` certification once the shared basis/finite-source leaves are certified.

## Remaining certification order

The dependency DAG now fixes the natural order:

1. certify \(P,N,\mathcal B\) and propagate with the already-frozen \(X\) into \(W\);
2. propagate finite \(Z_j,c_j\) source uncertainty into \(p,a_q,b_q\) and the three far moments;
3. certify outward \(\pi\) and \(\cosh(1/2)\) constants and directed integer-power/reciprocal arithmetic;
4. close the far-tail branch through \(f_Q^U,f_N^U,f_X^U\);
5. separately certify remote `tail_Z(n)` and form row radii \(\rho_{ni}\);
6. accumulate \(E^{\rm preGram}\) and add the already-transcripted Gram/chunk rounding radii;
7. combine with the finite Q/N enclosure and certify the final Schur endpoint.

The final theorem gate remains

\[
\boxed{
a_N^L-
\frac{(\|B_{QN}\|_2^U)^2}{\lambda_Q^L}>0.
}
\]

## Guardrail

This entry freezes a certification DAG only. No new numerical remote-Gram radius, far-tail endpoint, finite Q/N spectral endpoint, or final Schur lower bound has been certified here. No stronger inertia statement follows from this entry alone.
