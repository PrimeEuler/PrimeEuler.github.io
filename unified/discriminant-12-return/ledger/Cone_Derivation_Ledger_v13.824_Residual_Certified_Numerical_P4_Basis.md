# Cone Derivation Ledger v13.824 — Residual-Certified Numerical Basis for the Exact Rank-Four Tail Projector

Date: 2026-09-26.

Lane: A.

Status: [C] reproducible four-column numerical basis for the exact sector-wise projector \(P_4\); [C] full finite-plus-infinite residual bound; [C] global smooth-bulk lower floor; [C] Davis–Kahan/Kato subspace-error certificate from the exact \(0.08\) spectral moat; [N] basis is generated reproducibly but not yet frozen as an exact dyadic payload; [G] residue extraction and low-core replay remain subsequent gates.

Parents: v13.821–823.

Research artifact:

- research-notes/suzuki_tail_P4_residual_basis_certificate.py
  - construction commit d1c8bf49a6fa9892d2d7781057850a8fb887475c
  - bulk-floor hardening 173c30ff74223f2d01609e06d3ce03789edcd6a6
  - sharpened Ritz-separation hardening fba050e5e1a58c89bac5a42e3086a1869548ee6b

The exact tail spectral moat used below is the theorem of v13.823, itself based on the externally executed and confirmed \(\rho=0.02\) theorem of External Audit Round 107.

No GitHub workflow/status run is attached to the present basis certificate.  An external replay remains desirable before the basis is used as a frozen residue payload.

## 1. Exact target subspace

For each parity tail,

\[
J_T
=
B_T^{-1/2}A_TB_T^{-1/2},
\]

and

\[
P_4
=
\mathbf 1_{(-0.02,0.02)}(J_T)
\]

has

\[
\boxed{\operatorname{rank}P_4=4.}
\]

Moreover

\[
\sigma(J_T|_{\operatorname{Ran}P_4^\perp})
\cap[-0.10,0.10]
=
\varnothing.
\]

Hence the exact complement is separated from the entire target interval by the certified moat

\[
\boxed{0.08.}
\]

## 2. Numerical basis construction

The numerical basis is not taken from either endpoint negative trial space.

For each parity sector:

1. solve the generalized tail pencil
   \[
   Aq=\delta B_Tq
   \]
   through
   \[
   M_1=8001
   \]
   in even-v and
   \[
   M_1=8002
   \]
   in odd-v;

2. retain the four Ritz pairs in
   \[
   (-0.021,0.021);
   \]

3. graph-extend each Ritz vector by solving its own finite tail equation through
   \[
   M_2=16001
   \]
   in even-v and
   \[
   M_2=16002
   \]
   in odd-v;

4. re-Rayleigh–Ritz in the resulting four-dimensional graph space using the smooth-bulk metric \(B_T\);

5. accumulate the residual directly to \(64001/64000\), by inverse-power expansion through \(2,000,000\), and analytically beyond that cutoff.

The result is a four-column \(B_T\)-orthonormal numerical Ritz basis

\[
\widehat Q_4
\]

with Ritz matrix

\[
\widehat\Theta
=
\operatorname{diag}(\widehat\delta_1,\ldots,\widehat\delta_4).
\]

## 3. Ritz values after graph extension

The source-thread replay gives the second-stage Ritz values

### even-v

\[
\boxed{
5.01\times10^{-16},\
1.6401\times10^{-12},\
7.1920\times10^{-8},\
2.86763\times10^{-4}.
}
\]

### odd-v

\[
\boxed{
4.55\times10^{-15},\
2.2348\times10^{-10},\
4.1596\times10^{-6},\
1.03827\times10^{-2}.
}
\]

The public fail-closed Ritz-location caps are

\[
\boxed{
\max_j|\widehat\delta_j|<3.0\times10^{-4}
\quad\text{even-v},
}
\]

\[
\boxed{
\max_j|\widehat\delta_j|<1.05\times10^{-2}
\quad\text{odd-v}.
}
\]

These are used only for the sharpened separation estimate below.

## 4. Finite graph-extension residual

Before graph extension, the endpoint-trial four-space has a residual at the \(10^{-2}\) scale and is not accurate enough to serve as a canonical resonance basis.

After the \(M_2\) graph extension and four-dimensional re-Rayleigh–Ritz, the finite-support residual operator norms drop to approximately

\[
\boxed{
2.32290\times10^{-4}
\quad\text{even-v},
}
\]

\[
\boxed{
1.21282\times10^{-3}
\quad\text{odd-v}.
}
\]

Thus the remaining uncertainty is dominated by the infinite remote tail rather than the finite graph solve.

## 5. Infinite residual through two million

Adding the explicit remote rows through \(2,000,000\) gives total finite-plus-explicit residual operator norms

\[
\boxed{
2.5256569\times10^{-3}
\quad\text{even-v},
}
\]

\[
\boxed{
1.2998224\times10^{-2}
\quad\text{odd-v}.
}
\]

The widened public caps are

\[
\boxed{
2.60\times10^{-3},
\qquad
1.310\times10^{-2}.
}
\]

## 6. Analytic far-tail residual

The far residual is expanded as a \(1/n\), \(1/n^2\), \(1/n^3\) majorant.

For the source-faithful endpoint part, the already audited bound

\[
|Z_n^{(-,0.02)}|<8
\]

is used.

For the smooth-bulk residual term,

\[
-\sum_m\frac{\widehat Q_m}{n+m}
(0.02I-\widehat\Theta),
\]

the first two inverse-power coefficients are retained exactly and the remaining term is bounded by the positive \(n^{-3}\) remainder.

The resulting far-tail norms are approximately

\[
\boxed{
2.32176\times10^{-4}
\quad\text{even-v},
}
\]

\[
\boxed{
1.19518\times10^{-3}
\quad\text{odd-v}.
}
\]

The fail-closed public caps are

\[
\boxed{
4.0\times10^{-4},
\qquad
1.5\times10^{-3}.
}
\]

After Minkowski, the inherited source/operator uncertainty, and a \(10^{-8}\) arithmetic reserve, the final Euclidean residual caps are

\[
\boxed{
\|A_T\widehat Q_4-B_T\widehat Q_4\widehat\Theta\|
<
0.00301
\quad\text{even-v},
}
\]

\[
\boxed{
<
0.01461
\quad\text{odd-v}.
}
\]

## 7. Global smooth-bulk floor

To convert the Euclidean residual to the natural transformed residual

\[
B_T^{-1/2}
(A_T\widehat Q_4-B_T\widehat Q_4\widehat\Theta),
\]

a global lower floor for \(B_T\) is certified.

The low finite block is cut at \(3999/4000\).

For even-v, a shifted Cholesky certificate proves

\[
B_{FF}>0.0415\,I
\]

up to the explicit \(10^{-10}\) entry/log reserve.

For odd-v,

\[
B_{FF}>0.2400\,I
\]

with the same reserve.

The infinite finite-to-remote Hilbert cross block satisfies the elementary Hilbert–Schmidt cap

\[
\boxed{\|B_{FR}\|<0.42.}
\]

The remote bulk satisfies

\[
\boxed{B_{RR}>5.33\,I.}
\]

Therefore comparison with the scalar block matrices

\[
\begin{pmatrix}
b&-0.42\\
-0.42&5.33
\end{pmatrix}
\]

gives the public full-tail floors

\[
\boxed{
B_{T,e}>0.00830\,I,
}
\]

\[
\boxed{
B_{T,o}>0.20500\,I.
}
\]

The conservative scalar comparison actually lands slightly above these public values; only the widened constants above are used downstream.

## 8. Transformed residual certificate

Consequently,

\[
\|B_T^{-1/2}R\|
\le
\frac{\|R\|}{\sqrt{\beta}}.
\]

Using only the public residual and bulk-floor caps gives

### even-v

\[
\boxed{
\|B_{T,e}^{-1/2}R_e\|
<
0.0331.
}
\]

### odd-v

\[
\boxed{
\|B_{T,o}^{-1/2}R_o\|
<
0.0323.
}
\]

These are the fail-closed transformed-residual bounds for the numerical four-space.

## 9. Moat-only subspace error

Let

\[
Y=B_T^{1/2}\widehat Q_4.
\]

Then \(Y\) is orthonormal in the transformed Hilbert space and

\[
J_TY-Y\widehat\Theta
=
B_T^{-1/2}R.
\]

Since \(\widehat\Theta\subset(-0.02,0.02)\), the exact target projector has rank four, and the exact complement is separated by at least \(0.08\), the invariant-subspace residual theorem gives

\[
\boxed{
\|(I-P_4)Y\|
\le
\|\sin\Theta(\operatorname{Ran}Y,\operatorname{Ran}P_4)\|
\le
\frac{\|B_T^{-1/2}R\|}{0.08}.
}
\]

Therefore the public certificates are

### even-v

\[
\boxed{
\|\sin\Theta\|<0.414,
}
\]

corresponding to

\[
\boxed{
\theta_{\max}<24.4^\circ.
}
\]

### odd-v

\[
\boxed{
\|\sin\Theta\|<0.404,
}
\]

hence

\[
\boxed{
\theta_{\max}<23.8^\circ.
}
\]

Thus the generated numerical four-spaces are rigorously associated with the exact rank-four projector \(P_4\), rather than merely with endpoint inertia witnesses.

## 10. Sharpened certified separation

The widened Ritz-location caps improve the separation from the exact complementary spectrum.

Even-v:

\[
\operatorname{sep}
>
0.10-0.00030
=
0.09970.
\]

Odd-v:

\[
\operatorname{sep}
>
0.10-0.01050
=
0.08950.
\]

Using the same transformed-residual caps gives the sharper certified bounds

### even-v

\[
\boxed{
\|\sin\Theta\|<0.332,
\qquad
\theta_{\max}<19.4^\circ.
}
\]

### odd-v

\[
\boxed{
\|\sin\Theta\|<0.361,
\qquad
\theta_{\max}<21.2^\circ.
}
\]

The uniform \(0.08\)-moat bounds of Section 9 remain the primary theorem statement; these sharper values use the additional widened Ritz-location caps.

## 11. Interpretation

The endpoint negative trial spaces from v13.813/v13.818 were suitable for inertia, but one even-v direction rotated by roughly \(37^\circ\) across endpoint radius.

The present basis is qualitatively different:

\[
\boxed{
\text{it is defined by the generalized tail pencil itself and certified against the exact }P_4.
}
\]

It can therefore be used as a numerical carrier for the next residue/Feshbach calculations, subject to its explicit \(19^\circ\)–\(21^\circ\) sharpened subspace-error envelope.

This is not yet accurate enough to identify individual nearly degenerate eigenvectors without further refinement.  It is, however, sufficient to represent the four-dimensional cluster as a whole in a residual-certified way.

## 12. Next gate

The next natural use of \(\widehat Q_4\) is the grouped four-channel residue

\[
C(\delta)^*P_4C(\delta),
\]

where the present subspace-angle certificate can be propagated to an explicit matrix error bound.

If individual tail eigenvalues/residues are needed, the first three extremely near-zero channels must be separated further before assigning individual eigenvectors.

## Guardrails

No claim is made here that:

- the four individual infinite eigenvalues are simple;
- the first three near-zero Ritz vectors identify unique individual eigenvectors;
- the four infinite eigenvalues are positive;
- the approximate basis is an exact dyadic frozen payload;
- the low-core determinant has been certified;
- \(\kappa_0\) or \(\kappa_1\) has been promoted.

## Result

A reproducible residual-certified numerical basis for the exact four-dimensional tail projector has now been constructed.

The primary moat-only certificate is

\[
\boxed{
\theta_{\max}
<
24.4^\circ
\quad\text{even-v},
\qquad
<
23.8^\circ
\quad\text{odd-v}.
}
\]

With the widened certified Ritz-location caps this sharpens to

\[
\boxed{
\theta_{\max}
<
19.4^\circ
\quad\text{even-v},
\qquad
<
21.2^\circ
\quad\text{odd-v}.
}
\]
