# Cone Derivation Ledger v13.801 — Lane A Hyperbola-Style Smooth-Bulk Subtraction, Compact Relative Resonance Operator, and Stable Four-Tail-Mode Feshbach Cluster

Date: 2026-09-25

Lane: A — continuation of v13.798–800, explicitly reopening the divisor/hyperbola renormalization idea of v13.770–772 in the corrected source-resolvent form-core setting.

Status: [D] exact smooth-bulk decomposition for both parity sectors; [D] relative-compact/Fredholm reduction on a sufficiently high positive tail; [C] high-precision finite-section resonance diagnostics through N=96; [N] no infinite-cutoff identification of the observed four resonance branches; [N] kappa1 remains blocked.

Parents: v13.298–312, v13.391, v13.770–772, v13.796–800.

## 0. Synchronization and guardrails

The live ledger was checked before work and again immediately before both writes.  v13.800 remained head until the new research script was committed.  No newer audit or collision was present.

The current source-faithful guardrails from v13.796–800 remain in force:

- the finite form-core calculation is at a=1, lambda=0;
- no endpoint condition is imposed on the limiting deficiency vector;
- the odd-v pole channel has the corrected sign -2 d d^T from v13.799;
- the historical odd/full-parity certificate lineage that used +2 d d^T remains on HOLD;
- kappa1 is not promoted until kappa0/protected-structure convergence is under control.

A new reproducible diagnostic was committed first:

research-notes/suzuki_form_core_bulk_subtracted_resonance.py

commit b486f905f99cf64833c41b9db05f42d71656ea6e.

No GitHub workflow or commit status is attached to that research commit.  The formulas were independently executed in-session at 60–70 decimal digits; the committed file freezes the same formulas and supports the extended N=96 run.

## 1. Why the divisor/hyperbola idea is relevant again

v13.770 did not identify the divisor summatory remainder with the Suzuki trace functional.  Its surviving lesson was instead the renormalization principle

\[
\text{large raw object}
=
\text{smooth bulk}
+
\text{structured remainder},
\]

with the hyperbola geometry removing the dominant smooth contribution before the interesting boundary/arithmetic part is studied.

v13.800 then showed that the raw form-core low spectrum does not look stable under a naive fixed protected rank: a four-direction picture at N=16 became at least five near-null directions by N=32.

The present gate asks whether that apparent growth is partly an artifact of looking at the unrenormalized matrix.

There is one important distinction from v13.772.  At lambda=0 the explicit polynomial finite-A correction in Suzuki's Section-8 kernel vanishes.  Thus the useful subtraction here is not the lambda-dependent finite-volume polynomial term.  It is the high-mode smooth archimedean principal part already isolated in v13.298–312.

## 2. Exact common smooth bulk [D]

For either same-parity Dirichlet sector, the exact cusp matrix is

\[
C_{nn}
=
\log(n/4)-\operatorname{Ci}(n\pi)
-\frac{\operatorname{Si}(n\pi)}{n\pi},
\]

and, for m not equal to n,

\[
C_{mn}
=
\frac{2}{\pi}
\frac{n\operatorname{Si}(m\pi)-m\operatorname{Si}(n\pi)}
{m^2-n^2}.
\]

For a fixed parity let

\[
\epsilon=(-1)^n=(-1)^m.
\]

The same-parity sine-integral asymptotic is

\[
\operatorname{Si}(n\pi)
=
\frac{\pi}{2}
-\frac{\epsilon}{n\pi}
+\delta_n,
\qquad
\delta_n=O(n^{-3}).
\]

Substitution gives

\[
\boxed{
C_{mn}
=
-\frac1{m+n}
+
\frac{2\epsilon}{\pi^2mn}
+
E_{mn}
\qquad(m\ne n),
}
\]

where

\[
E_{mn}
=
\frac{2}{\pi}
\frac{n\delta_m-m\delta_n}{m^2-n^2}.
\]

On the diagonal,

\[
\boxed{
C_{nn}
=
\log(n/4)-\frac1{2n}+O(n^{-2}).
}
\]

Therefore both parity sectors have the same principal smooth operator

\[
\boxed{
B_{\rm sm}=D_{\log}-H,
}
\]

with

\[
(D_{\log})_{nn}=\log(n/4),
\qquad
H_{mn}=\frac1{m+n}.
\]

The parity dependence enters only in the compact cusp correction: the leading rank-one term is

\[
-\frac{2}{\pi^2mn}
\]

for odd Dirichlet indices (even-v), and

\[
+\frac{2}{\pi^2mn}
\]

for even Dirichlet indices (odd-v).

The corrected two-index remainder estimates from the v13.303 lineage use only the magnitude of the sine-integral remainder, so the same square-summability argument applies with this sign change.  Thus

\[
\boxed{
K_{\rm cusp}^{(+)}\in\mathcal S_2,
\qquad
K_{\rm cusp}^{(-)}\in\mathcal S_2.
}
\]

This extends the smooth-bulk/cusp-correction organization to the corrected odd-v sector without importing the obsolete +2 d d^T pole sign.

## 3. Full corrected parity decomposition [D]

At a=1, lambda=0 write

\[
A^{(\pm)}
=
B_{\rm sm}^{(\pm)}
+
V^{(\pm)}.
\]

The residual is

\[
V^{(\pm)}
=
B_{\rm prime}^{(\pm)}
+
K_{\rm cusp}^{(\pm)}
+
K_{\rm arch}^{(\pm)}
+
K_{\rm pole}^{(\pm)}.
\]

The pieces have the already-established structure:

1. the prime-power ramp sum is a bounded finite sum of truncated shifts;
2. the cusp correction is Hilbert-Schmidt in both same-parity sectors by Section 2;
3. the smooth archimedean remainder is bounded, with high-mode decay from the v13.312 lineage;
4. the pole term is rank one in each parity sector, with the source-faithful signs

\[
K_{\rm pole}^{(\text{even-v})}=+2cc^T,
\]

\[
K_{\rm pole}^{(\text{odd-v})}=-2dd^T.
\]

Hence

\[
\boxed{V^{(\pm)}\ \text{is bounded}.}
\]

## 4. Compact relative resonance operator [D]

The Hilbert matrix H is bounded on l^2.  The diagonal entries of D_log tend to +infinity.  Therefore B_sm is a bounded perturbation of an operator with compact resolvent.

After discarding a sufficiently large finite set of modes, B_sm is strictly positive.  A crude parity-independent sufficient condition follows from Hilbert's inequality:

\[
\log(N/4)>\|H\|
\]

for a high enough N.

On such a positive tail,

\[
B_{\rm sm}^{-1/2}
\]

is compact.  Since V is bounded,

\[
\boxed{
K
=
B_{\rm sm}^{-1/2}
V
B_{\rm sm}^{-1/2}
\ \text{is compact}.
}
\]

Moreover

\[
A_{\rm tail}
=
B_{\rm sm}^{1/2}(I+K)B_{\rm sm}^{1/2}.
\]

Thus a small eigenvalue of the full tail corresponds to an eigenvalue of K near the resonance value -1.

Because K is compact, its nonzero spectrum is discrete with finite multiplicities and can accumulate only at 0.  Therefore, for every epsilon<1,

\[
\boxed{
\#\{\mu\in\sigma(K):|\mu+1|<\epsilon\}<\infty.
}
\]

This is the theorem-level payoff of the hyperbola-style subtraction:

\[
\boxed{
\text{the near-zero tail problem is a finite-dimensional resonance problem over the smooth bulk.}
}
\]

An endless sequence of independent resonance eigenvalues accumulating at -1 is excluded by relative compactness.

This does not yet identify how many resonance directions occur at -1 in the infinite operator.

## 5. Finite-section normalization [C]

For the numerical diagnostic, retain the first two basis modes of each parity sector as a low core and put the remaining modes in the tail.

For a finite cutoff N define

\[
T_N
=
(B_{{\rm sm},tt}^{(N)})^{-1/2}
V_{tt}^{(N)}
(B_{{\rm sm},tt}^{(N)})^{-1/2}.
\]

The first two basis modes are:

- even-v: n=1,3, leaving tail n>=5;
- odd-v: n=2,4, leaving tail n>=6.

At N=96 the smooth tail remains comfortably positive:

\[
\lambda_{\min}(B_{{\rm sm},tt}^{\rm even})
\approx
0.049776122268,
\]

\[
\lambda_{\min}(B_{{\rm sm},tt}^{\rm odd})
\approx
0.252848899663.
\]

The raw ill-conditioning has therefore been moved into I+T_N, rather than residing in the bulk inverse.

## 6. Four tail resonance branches emerge [C]

Order the eigenvalues of T_N by distance to -1.

The controlling finite-section values are summarized at N=64 and N=96, after the four-versus-fifth separation has become visually and numerically clear.

At N=64:

even-v:

\[
\begin{aligned}
|1+\mu_1|&\approx2.08663\times10^{-17},\\
|1+\mu_2|&\approx2.59610\times10^{-12},\\
|1+\mu_3|&\approx1.03342\times10^{-7},\\
|1+\mu_4|&\approx3.74849\times10^{-4},\\
|1+\mu_5|&\approx1.58070\times10^{-1};
\end{aligned}
\]

odd-v:

\[
\begin{aligned}
|1+\mu_1|&\approx6.31486\times10^{-15},\\
|1+\mu_2|&\approx3.47514\times10^{-10},\\
|1+\mu_3|&\approx5.78514\times10^{-6},\\
|1+\mu_4|&\approx1.37232\times10^{-2},\\
|1+\mu_5|&\approx2.93207\times10^{-1}.
\end{aligned}
\]

At N=96:

even-v:

\[
\boxed{
1.79806\times10^{-17},\
2.20960\times10^{-12},\
8.52066\times10^{-8},\
3.56352\times10^{-4},\
1.50555\times10^{-1}
}
\]

and odd-v:

\[
\boxed{
5.00954\times10^{-15},\
2.73337\times10^{-10},\
4.94853\times10^{-6},\
1.26997\times10^{-2},\
2.88312\times10^{-1}.
}
\]

Thus four tail branches are sharply distinguished from the fifth by N=64–96 in both parity sectors.

No exact four-dimensional infinite-tail theorem is claimed.

## 7. Subspace stability from N=64 to N=96 [C]

Convert the four closest-to--1 normalized eigenvectors back to coefficient space, embed the N=64 space into the N=96 space, and compute Euclidean principal angles.

For the four-dimensional resonance subspaces, the largest principal-angle changes are

\[
\boxed{
\theta_{\max}^{\rm even}(64,96)
\approx0.1803^\circ,
}
\]

\[
\boxed{
\theta_{\max}^{\rm odd}(64,96)
\approx1.2727^\circ.
}
\]

If the fifth direction is included, the largest angles become much larger:

\[
\theta_{\max,5D}^{\rm even}
\approx6.07^\circ,
\]

\[
\theta_{\max,5D}^{\rm odd}
\approx11.61^\circ.
\]

Therefore the observed four-dimensional tail cluster is substantially more stable than the five-dimensional candidate cluster.

This is finite-section evidence only.

## 8. The raw low spectrum reorganizes as 2 core + 4 tail [C/I]

At N=96 the sixth and seventh full eigenvalues are

even-v:

\[
\lambda_6\approx2.51023\times10^{-4},
\qquad
\lambda_7\approx1.85555\times10^{-1},
\]

odd-v:

\[
\lambda_6\approx1.01484\times10^{-2},
\qquad
\lambda_7\approx5.69149\times10^{-1}.
\]

Thus the raw matrix has a clear six-level low cluster before a substantial gap.

The bulk-subtracted Feshbach organization explains this as

\[
\boxed{
2\ \text{low smooth-bulk core modes}
+
4\ \text{tail resonance modes}.
}
\]

This is a much more stable interpretation than assigning a protected rank directly from the raw N=16 spectrum.

The count six is not promoted as an infinite-dimensional multiplicity theorem.

## 9. Source quadratic form: the huge response is not bulk [C]

Let f be the exact exp(x) source projection.

At N=96 the smooth-bulk source energies are only

\[
\boxed{
f_e^TB_{\rm sm}^{-1}f_e
\approx-1.208782348745,
}
\]

\[
\boxed{
f_o^TB_{\rm sm}^{-1}f_o
\approx-1.080451132111.
}
\]

By contrast the full corrected energies are

\[
\boxed{
E_e
\approx9.6900149773\times10^{28},
}
\]

\[
\boxed{
E_o
\approx3.4518888855\times10^{24}.
}
\]

Therefore the enormous source-resolvent response is not a large smooth bulk contribution.  It is generated by resonance amplification after the bulk subtraction.

The positive-tail source energies are approximately

\[
E_{t,e}\approx1.0123218238\times10^{15},
\]

\[
E_{t,o}\approx1.3926837722\times10^{12}.
\]

The first four resonance modes account for

\[
0.9999999999999934
\]

of the even-v tail energy and

\[
0.9999999999997803
\]

of the odd-v tail energy.

Thus the source sees essentially the same four-dimensional tail resonance cluster found spectrally.

## 10. Two-dimensional core Schur collapse [C]

Eliminating the resonant tail leaves a 2 by 2 effective core Schur matrix.

At N=96 its eigenvalues are

even-v:

\[
\boxed{
8.24930\times10^{-30},
\qquad
8.99158\times10^{-23},
}
\]

odd-v:

\[
\boxed{
2.14488\times10^{-26},
\qquad
8.93801\times10^{-20}.
}
\]

The source energy in this two-dimensional effective core is itself almost entirely in the lowest Schur direction:

even-v fraction:

\[
0.999999899954,
\]

odd-v fraction:

\[
0.999999224178.
\]

The large full source energy therefore has a two-stage structure:

\[
\boxed{
\text{smooth bulk}
\longrightarrow
\text{four tail resonances}
\longrightarrow
\text{nearly singular 2D core Schur response}.
}
\]

This is precisely the kind of bulk-removal/focused-remainder organization suggested by the divisor-hyperbola analogy.

## 11. kappa0 remains unconverged [N]

The enlarged corrected finite-section values remain cutoff-sensitive.

At N=64,

\[
\kappa_{0,64}
\approx0.9999369812174818709,
\]

and at N=96,

\[
\boxed{
\kappa_{0,96}
\approx0.9999287562314239928.
}
\]

The audited infinite target remains

\[
\kappa_{0,\infty}
\approx0.9968019520324009035.
\]

Therefore the present reorganization explains the conditioning and protected-structure anatomy, but it does not yet prove convergence of the source-resolvent scalar.

kappa1 remains blocked.

## 12. Strategic consequence

The N=16 -> N=32 moving protected-rank problem from v13.800 should no longer be attacked by repeatedly enlarging a raw Ritz protected basis.

The correct next object is the compact relative interaction

\[
K
=
B_{\rm sm}^{-1/2}
(A-B_{\rm sm})
B_{\rm sm}^{-1/2}
\]

together with the two-dimensional low-core Schur complement.

The next analytic/numerical gates are:

1. construct the infinite-tail parity realizations of K explicitly and bound finite-section-to-infinite truncation error;
2. prove a spectral enclosure separating the observed first four eigenvalues of K near -1 from the fifth branch;
3. propagate that enclosure through the 2 by 2 core Feshbach map;
4. only after this stabilization revisit the source-energy ratio and kappa0 convergence.

If the four-versus-fifth separation can be certified, Lane A reduces from an unstable raw near-null ladder to a controlled four-channel Fredholm resonance coupled to a two-dimensional boundary/core problem.

## Result

The divisor-summatory hyperbola analogy has now produced a concrete Lane A operator reorganization rather than a metaphor.

The smooth high-mode bulk is

\[
\boxed{
B_{\rm sm}=D_{\log}-H,
}
\]

and the corrected arithmetic/compact remainder is relatively compact in the bulk metric:

\[
\boxed{
K=B_{\rm sm}^{-1/2}(A-B_{\rm sm})B_{\rm sm}^{-1/2}
\ \text{compact on a sufficiently high positive tail}.
}
\]

Consequently the near-zero problem is intrinsically finite-dimensional at the resonance value -1.

Finite sections through N=96 strongly resolve this into four stable tail resonance directions plus a two-dimensional low-core Schur collapse.  This explains the apparent growth of the raw near-null ladder without yet asserting that the infinite resonance multiplicity is exactly four or that kappa0 has converged.

No RH/GRH, exact-kernel, or kappa1 claim is made.
