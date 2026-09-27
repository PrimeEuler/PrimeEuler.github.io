# Cone Derivation Ledger v13.830 — Full Smooth-Bulk Pontryagin Index Two and Low-Core Signed-Flow Handoff

Date: 2026-09-27.

Lane: A.

Status: [T] exact full smooth-bulk negative index two in both parity sectors; [N] invariant N=96 six-root Krein-signature diagnostic; [N] M3999/4000 low-core endpoint Schur sign pattern at rho=0.02 and 0.10; [G] infinite low-core endpoint signs and full low-core zero count remain unproved.

Parents: v13.801, v13.823–829.

Research artifacts:

- research-notes/suzuki_full_bulk_pontryagin_index_signature.py
  - commit 94f7010e251d23c874b3219298e040048f0d8600

- research-notes/suzuki_low_core_endpoint_schur_M3999.py
  - commit bade97d9a10039813b9c870fd24162e4b3ee0049

External Audit Round 110, v13.829, independently confirms the grouped-residue numerical-center work of v13.828 that motivated the present low-core continuation.

No GitHub workflow/status run is attached to the new artifacts.

## 1. Exact two-negative-direction structure of the full smooth bulk

Restore the first two parity modes and split

\[
\mathcal H
=
\mathcal H_C\oplus\mathcal H_T,
\qquad
\dim \mathcal H_C=2.
\]

The smooth bulk is

\[
B_{\rm sm}
=
D_{\log}-H.
\]

The certified parity tail satisfies

\[
B_T>0
\]

with explicit lower floors from v13.824.

The two-dimensional core blocks are

### even-v core \(\{1,3\}\)

\[
B_{CC}^{(e)}
=
\begin{pmatrix}
-\log 4-\frac12 & -\frac14\\
-\frac14 & \log\frac34-\frac16
\end{pmatrix}.
\]

Numerically,

\[
B_{CC}^{(e)}
\approx
\begin{pmatrix}
-1.88629436 & -0.25\\
-0.25 & -0.45434874
\end{pmatrix},
\]

with eigenvalues approximately

\[
-1.92868628,\qquad -0.41195682.
\]

### odd-v core \(\{2,4\}\)

\[
B_{CC}^{(o)}
=
\begin{pmatrix}
-\log 2-\frac14 & -\frac16\\
-\frac16 & -\frac18
\end{pmatrix},
\]

with eigenvalues approximately

\[
-0.97579633,\qquad -0.09235085.
\]

The committed verifier uses interval arithmetic on the exact formulas and checks

\[
\operatorname{tr}B_{CC}<0,
\qquad
\det B_{CC}>0
\]

in both sectors.

Hence

\[
\boxed{
B_{CC}^{(e)}\prec0,
\qquad
B_{CC}^{(o)}\prec0.
}
\]

## 2. Exact full negative index

Because

\[
B_T>0,
\]

the exact core Schur complement is

\[
S_B
=
B_{CC}
-
B_{CT}B_T^{-1}B_{TC}.
\]

The second term is positive semidefinite, therefore

\[
S_B
\preceq
B_{CC}
\prec0.
\]

Block congruence then gives

\[
\boxed{
\operatorname{ind}_{-}(B_{\rm sm})=2
}
\]

in each parity sector, with no kernel.

Equivalently, the full smooth-bulk form has exactly two negative directions and an infinite positive tail.

This is the exact operator-level reason the first two modes must be treated separately from the positive tail metric.

## 3. Consequence for generalized spectral counting

On the positive tail, every generalized crossing has positive bulk signature and the endpoint inertia difference

\[
\operatorname{ind}_{-}(A-\rho B_T)
-
\operatorname{ind}_{-}(A+\rho B_T)
\]

equals the ordinary number of tail generalized eigenvalues in the window.

After restoring the two negative bulk directions, this statement no longer holds without a Krein-signature analysis.

For a regular real crossing

\[
(A-\delta B)q=0,
\]

the crossing slope is controlled by

\[
-\langle q,Bq\rangle.
\]

Thus positive- and negative-\(B\)-signature roots contribute with opposite signs to endpoint spectral flow.

The full endpoint inertia difference is therefore a signed crossing invariant, not automatically the raw number of generalized eigenvalues in the interval.

This is a guardrail for all subsequent low-core work.

## 4. N=96 six-root invariant-subspace diagnostic

At N=96 the full generalized pencil

\[
Aq=\delta B_{\rm sm}q
\]

has six real generalized Ritz roots inside

\[
|\delta|<0.02
\]

in each parity sector.

The basis-invariant restriction of \(B_{\rm sm}\) to the six-dimensional generalized invariant subspace has the following eigenvalues.

### even-v

\[
\boxed{
-1.5390,\ -0.2152,\
0.1502,\ 0.2183,\ 0.2427,\ 0.3262.
}
\]

Hence its Krein inertia is

\[
\boxed{
2^-+4^+.
}
\]

### odd-v

\[
\boxed{
-0.5302,\ -0.005118,\
0.005864,\ 0.07659,\ 0.1549,\ 0.3174.
}
\]

Again,

\[
\boxed{
2^-+4^+.
}
\]

This statement is invariant under rotations among the nearly degenerate Ritz vectors; it does not assign signatures to individual machine-zero eigenvectors.

## 5. Finite endpoint inertia difference at N=96

At both radii

\[
\rho=0.02,\qquad0.10,
\]

the N=96 full endpoint inertias satisfy

\[
\operatorname{ind}_{-}(A-\rho B_{\rm sm})=4,
\]

\[
\operatorname{ind}_{-}(A+\rho B_{\rm sm})=2.
\]

Therefore

\[
\boxed{
\operatorname{ind}_{-}(F^-_\rho)
-
\operatorname{ind}_{-}(F^+_\rho)
=
2.
}
\]

This matches exactly the signed six-root decomposition

\[
4^+-2^-=2.
\]

Thus the finite data already display the expected Pontryagin-space spectral flow.

## 6. Relation to the certified tail theorem

The certified tail theorem gives exactly four generalized tail eigenvalues in the inner window.

Because the tail metric is positive, those four channels are positive-metric channels.

The full N=96 diagnostic then organizes the six-root cluster as

\[
\boxed{
4\ \text{positive-metric tail channels}
+
2\ \text{negative-metric low-core channels}.
}
\]

This gives a coherent operator interpretation of the old v13.801

\[
2\ \text{core}+4\ \text{tail}
\]

numerical anatomy.

The present entry does not yet promote the existence of two infinite low-core roots.

## 7. Theorem-scale finite low-core endpoint Schur diagnostic

Use the source-faithful theorem-scale finite tails

even-v:

\[
\{5,7,\ldots,3999\},
\]

odd-v:

\[
\{6,8,\ldots,4000\}.
\]

For each endpoint form define the two-mode finite Schur matrix

\[
S_C^{(M)}(\delta)
=
F_{CC}(\delta)
-
F_{CT}(\delta)
F_{TT}^{(M)}(\delta)^{-1}
F_{TC}(\delta).
\]

The structured tail solves are independently checked by a chunked residual replay.

### rho=0.02

even-v minus:

\[
S_{C,e}^{(M)}(+0.02)
\approx
\begin{pmatrix}
0.04227043&0.00812274\\
0.00812274&0.01117907
\end{pmatrix},
\]

with eigenvalues

\[
\boxed{
0.00918488,\quad0.04426462.
}
\]

even-v plus:

\[
S_{C,e}^{(M)}(-0.02)
\approx
\begin{pmatrix}
-0.04362694&-0.00924105\\
-0.00924105&-0.01210050
\end{pmatrix},
\]

with eigenvalues

\[
\boxed{
-0.04613600,\quad-0.00959144.
}
\]

odd-v minus eigenvalues:

\[
\boxed{
0.00348164,\quad0.02660098.
}
\]

odd-v plus eigenvalues:

\[
\boxed{
-0.02138735,\quad-0.00202571.
}
\]

The smallest absolute finite sign margin is therefore approximately

\[
\boxed{
2.03\times10^{-3}.
}
\]

## 8. rho=0.10 finite low-core endpoints

The same sign pattern becomes much stronger.

even-v minus:

\[
\boxed{
0.01891717,\quad0.15834345.
}
\]

even-v plus:

\[
\boxed{
-0.24321735,\quad-0.05036823.
}
\]

odd-v minus:

\[
\boxed{
0.01204398,\quad0.11203389.
}
\]

odd-v plus:

\[
\boxed{
-0.11253740,\quad-0.01207200.
}
\]

Thus at both theorem radii the finite low-core Schur block is

\[
\boxed{
S_C^{(M)}(+\rho)\succ0,
\qquad
S_C^{(M)}(-\rho)\prec0.
}
\]

## 9. Tail solve replay quality

The chunked residual norms for

\[
F_{TT}^{(M)}X=F_{TC}^{(M)}
\]

are between approximately

\[
3.2\times10^{-16}
\]

and

\[
1.5\times10^{-14}.
\]

The solution operator norms remain below

\[
2.3.
\]

Thus the displayed finite Schur signs are not artifacts of a visibly failed structured solve.

They remain finite-section diagnostics because the infinite remote low-core correction has not yet been enclosed.

## 10. Strategic consequence

The next low-core proof target is now sharply defined.

One should certify the infinite correction to

\[
S_C^{(M)}(\pm0.02)
\]

and prove that it is smaller than the finite sign margins.

If this closes, then the full endpoint inertias will be

\[
\operatorname{ind}_{-}(F^-_{0.02})=4,
\]

\[
\operatorname{ind}_{-}(F^+_{0.02})=2.
\]

That result must be interpreted as signed Pontryagin spectral flow:

\[
4-2=2,
\]

not as a raw two-root count.

To establish an actual six-root full cluster, one must additionally control the Krein signatures / meromorphic two-mode zero structure.

This is now the correct formulation of the low-core problem.

## Guardrails

This entry does not claim:

- that the infinite full pencil has exactly six roots in \(|\delta|<0.02\);
- that the two low-core roots are individually real/simple;
- that the finite low-core endpoint signs have already survived the infinite remote correction;
- that the full endpoint inertia difference counts ordinary multiplicity;
- that \(\kappa_0\) has converged;
- that \(\kappa_1\), RH, or GRH is unblocked.

## Result

The full smooth bulk has exact negative index

\[
\boxed{2}
\]

in both parity sectors.

The finite generalized six-root cluster has invariant bulk signature

\[
\boxed{
2^-+4^+,
}
\]

which explains the finite signed endpoint count

\[
\boxed{
4-2=2.
}
\]

The theorem-scale finite low-core Schur diagnostics show the robust sign pattern

\[
\boxed{
S_C^{(M)}(+\rho)\succ0,
\qquad
S_C^{(M)}(-\rho)\prec0
}
\]

for both

\[
\rho=0.02,\ 0.10.
\]

The next theorem gate is to certify that these two-mode endpoint signs persist after the infinite remote-tail correction.
