# Cone Derivation Ledger v13.268 — Squared Perturbation Determinant and Characteristic-Function Criterion

Date: 2026-09-06
Status: EXACT DETERMINANT-LEVEL REDUCTION + STRONGER SPECTRAL TARGET — RH/GRH NOT PROVED

## 0. Synchronization and strategy

Immediately before this write, the authoritative project README, current `master` tip, and the ledger state were re-fetched. The current tip remained

`4c361607377d050590b5e96aeb0a678fb4f3b0d6`,

with v13.267 the highest ledger checkpoint and no v13.268 external-audit file present.

The user explicitly requested that if the reference-response defect of v13.267 did not reduce cleanly, the analysis should immediately take the next step.

That is what happens here.

The direct attempt to identify the arithmetic truncation of v13.266 with a scalar boundary Weyl function does **not** canonically close, because the Weyl matrix depends on the chosen boundary triplet. However, the next invariant object reduces much further:

\[
\boxed{
\text{boundary resolvent correction}
\longrightarrow
\text{logarithmic derivative of a }2\times2\text{ determinant}.
}
\]

After squaring the first-order spectral parameter, that determinant becomes a positive real scalar on `w>0`.

At the same time, the arithmetic target itself has an exact determinant form:

\[
\boxed{
\mathcal S_K(w)
=2\frac{d}{dw}\log \Psi_K(w),
}
\]

where

\[
\Psi_K(w):=\xi_K\!\left(\frac12+\sqrt w\right)
\]

is a single-valued entire function of `w` because the centered completed Dedekind function is even.

This converts the remaining program from a boundary-vector Weyl-function problem into a **characteristic determinant convergence problem**.

## 1. Why the scalar reference Weyl identification is not canonical

From v13.267, fix an ordinary boundary triplet

\[
(\mathbf C^2,\Gamma_0,\Gamma_1)
\]

for the finite-interval two-channel symmetric operator `S_a^*`, with Weyl matrix

\[
M_a(z)=\Gamma_1\gamma_a(z).
\]

A boundary triplet is not unique. Under an admissible change of boundary coordinates, the pair `(Gamma_0,Gamma_1)` changes and the Weyl matrix transforms by the corresponding linear-fractional rule.

Therefore the statement

\[
M_a(z)\stackrel{?}{=}\text{arithmetic truncation}
\]

is not invariant unless a canonical boundary normalization is first specified.

This means the exact equality suggested at the end of v13.267 is, by itself, not the right invariant target.

The correct object should be built from either:

1. a fixed extension pair;
2. a perturbation determinant;
3. a trace of a resolvent difference;
4. or a characteristic entire function whose zero divisor is extension-invariant after normalization.

The finite boundary dimension makes this possible.

## 2. Krein determinant attached to an extension pair

Retain the boundary-triplet notation of v13.267 and let

\[
D_{a,0}=S_a^*|_{\ker\Gamma_0}
\]

be the reference self-adjoint extension.

Let a second self-adjoint extension be specified by a self-adjoint matrix

\[
\Theta_a=\Theta_a^*\in\mathbf C^{2\times2},
\]

with

\[
D_{a,\Theta}
=S_a^*|_{\Gamma_1f=\Theta_a\Gamma_0f}.
\]

Define the finite-dimensional perturbation determinant

\[
\boxed{
\Delta_{a,\Theta}(z)
:=\det\bigl(\Theta_a-M_a(z)\bigr).
}
\]

Whenever `z` lies in the common resolvent set and the determinant is nonzero, Krein's formula gives

\[
(D_{a,\Theta}-z)^{-1}-(D_{a,0}-z)^{-1}
=
\gamma_a(z)(\Theta_a-M_a(z))^{-1}\gamma_a(\bar z)^*.
\]

Because the correction has finite rank, its trace is well defined.

Using the standard boundary-triplet identity

\[
M_a'(z)=\gamma_a(\bar z)^*\gamma_a(z),
\]

we obtain

\[
\begin{aligned}
\operatorname{Tr}\bigl[(D_{a,\Theta}-z)^{-1}-(D_{a,0}-z)^{-1}\bigr]
&=
\operatorname{tr}_{\mathbf C^2}
\bigl[(\Theta_a-M_a(z))^{-1}M_a'(z)\bigr]
\\
&=-\frac{d}{dz}\log\Delta_{a,\Theta}(z).
\end{aligned}
\]

Hence

\[
\boxed{
\operatorname{Tr}\bigl[(D_{a,\Theta}-z)^{-1}-(D_{a,0}-z)^{-1}\bigr]
=-\partial_z\log\Delta_{a,\Theta}(z).
}
\]

This is the determinant form of the rank-two reduction in v13.267.

## 3. Squaring the spectral parameter folds the determinant

For real `w>0`, put

\[
\kappa=\sqrt w.
\]

For any self-adjoint first-order operator `D`,

\[
(D^2+w)^{-1}
=
\frac1{2i\kappa}
\bigl[(D-i\kappa)^{-1}-(D+i\kappa)^{-1}\bigr].
\]

Apply this to the extension pair `(D_{a,Theta},D_{a,0})`.

Define the **squared perturbation determinant**

\[
\boxed{
\mathfrak D_{a,\Theta}(w)
:=
\Delta_{a,\Theta}(i\sqrt w)
\Delta_{a,\Theta}(-i\sqrt w).
}
\]

Differentiating gives

\[
\boxed{
\begin{aligned}
&\operatorname{Tr}\Bigl[
(D_{a,\Theta}^2+w)^{-1}
-(D_{a,0}^2+w)^{-1}
\Bigr]
\\
&\qquad=
\frac{d}{dw}\log\mathfrak D_{a,\Theta}(w).
\end{aligned}
}
\]

This follows directly from the first-order trace identity and the chain rule.

For a self-adjoint extension and an ordinary boundary triplet,

\[
M_a(-i\kappa)=M_a(i\kappa)^*,
\]

so

\[
\Delta_{a,\Theta}(-i\kappa)
=\overline{\Delta_{a,\Theta}(i\kappa)}.
\]

Therefore

\[
\boxed{
\mathfrak D_{a,\Theta}(w)
=
\left|\det(\Theta_a-M_a(i\sqrt w))\right|^2
>0
}
\]

for every positive `w` away from a boundary singularity.

Thus the entire extension dependence on the squared real axis is encoded by the logarithmic derivative of one positive scalar function.

## 4. H4 covariance becomes determinant invariance

Under the normalized Hadamard transform

\[
U_2=\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
\]

v13.267 gives

\[
\widetilde M_a=U_2M_aU_2^*,
\qquad
\widetilde\Theta_a=U_2\Theta_aU_2^*.
\]

Hence

\[
\widetilde\Theta_a-\widetilde M_a
=
U_2(\Theta_a-M_a)U_2^*.
\]

Taking determinants,

\[
\boxed{
\det(\widetilde\Theta_a-\widetilde M_a)
=
\det(\Theta_a-M_a).
}
\]

Therefore

\[
\boxed{
\mathfrak D_{a,\Theta}(w)
}
\]

is exactly invariant under the D12 character/residue Hadamard change of basis.

This is stronger than covariance of the matrix Weyl function: the squared perturbation determinant is an actual scalar invariant.

## 5. Character-diagonal factorization

When the extension and Weyl data are diagonal in the character basis,

\[
M_{\rm char,a}(z)
=
\begin{pmatrix}
m_{0,a}(z)&0\\
0&m_{12,a}(z)
\end{pmatrix},
\]

and

\[
\Theta_{\rm char,a}
=
\begin{pmatrix}
\theta_{0,a}&0\\
0&\theta_{12,a}
\end{pmatrix},
\]

then

\[
\boxed{
\Delta_{a,\Theta}(z)
=
(\theta_{0,a}-m_{0,a}(z))
(\theta_{12,a}-m_{12,a}(z)).
}
\]

Consequently the squared determinant factors into the product of the two scalar channel determinants:

\[
\boxed{
\mathfrak D_{a,\Theta}(w)
=
\mathfrak D_{0,a}(w)
\mathfrak D_{12,a}(w).
}
\]

Thus the determinant-level direct sum matches the analytic factorization

\[
\zeta_K(s)=\zeta(s)L(s,\chi_{12}).
\]

The H4/D12 structure therefore survives at the level of characteristic determinants, not only operator blocks.

## 6. The arithmetic target is already a logarithmic derivative

From v13.263 define

\[
\Xi_K(z)
:=
\xi_K\!\left(\frac12+z\right).
\]

The functional equation gives

\[
\Xi_K(-z)=\Xi_K(z).
\]

Therefore there exists an entire function of one variable `w` such that

\[
\boxed{
\Psi_K(w)
:=\Xi_K(\sqrt w)
}
\]

is single-valued and entire.

This is not a branch-dependent definition: because `Xi_K` is even, its Taylor series contains only even powers,

\[
\Xi_K(z)=\sum_{n\ge0}c_{2n}z^{2n},
\]

hence

\[
\Psi_K(w)=\sum_{n\ge0}c_{2n}w^n.
\]

Now differentiate:

\[
\Psi_K'(w)
=
\frac1{2\sqrt w}
\Xi_K'(\sqrt w).
\]

Therefore

\[
2\frac{\Psi_K'(w)}{\Psi_K(w)}
=
\frac1{\sqrt w}
\frac{\Xi_K'(\sqrt w)}{\Xi_K(\sqrt w)}.
\]

Using the definition of `Xi_K`, this is exactly the v13.263 Stieltjes target:

\[
\boxed{
\mathcal S_K(w)
=
2\frac{d}{dw}\log\Psi_K(w).
}
\]

This identity is unconditional as a meromorphic identity.

It is one of the most important simplifications of the current branch.

## 7. Zero divisor of the folded characteristic function

Let

\[
\rho=\frac12+\alpha
\]

be a nontrivial zero of `xi_K` of multiplicity `m`.

Then `Xi_K(z)` has zeros at the symmetry-related centered points. Pairing `+alpha` and `-alpha`, the local even factor contains

\[
(z^2-\alpha^2)^m.
\]

Therefore `Psi_K(w)` has a zero at

\[
\boxed{w=\alpha^2}
\]

with multiplicity `m`.

Hence

\[
\boxed{
\operatorname{Res}_{w=\alpha^2}\mathcal S_K(w)=2m.
}
\]

Under GRH,

\[
\alpha=i\gamma,
\]

so

\[
w=-\gamma^2\le0.
\]

Thus

\[
\boxed{
\mathrm{GRH}(\zeta_K)
\iff
\text{all zeros of }\Psi_K(w)\text{ lie on }(-\infty,0]
}
\]

with the usual explicit treatment of a possible central zero at `w=0`.

This is the characteristic-function version of the Stieltjes pole criterion in v13.263.

## 8. New trace realization: no boundary vector is needed

The ordinary-vector resolvent ansatz was ruled out in v13.264 because the Stieltjes spectral measure has infinite total mass.

There is, however, a more natural realization that avoids this obstruction completely.

Assume the Hilbert-Pólya spectral picture and let a self-adjoint first-order operator `D_K` have spectrum

\[
\ldots,-\gamma_j,\ldots,+\gamma_j,\ldots
\]

with each sign occurring with the zero multiplicity `m_j`.

Set

\[
A_K=D_K^2\ge0.
\]

Then the eigenvalue `gamma_j^2` of `A_K` has multiplicity `2m_j`.

Since the zero-counting law implies

\[
\sum_j\frac{m_j}{1+\gamma_j^2}<\infty,
\]

the resolvent `(A_K+w)^{-1}` is trace class for `w>0`.

Its trace is

\[
\begin{aligned}
\operatorname{Tr}(A_K+w)^{-1}
&=
\sum_j\frac{2m_j}{w+\gamma_j^2}
\\
&=\mathcal S_K(w)
\end{aligned}
\]

under GRH.

Thus the exact conditional spectral model is

\[
\boxed{
\mathcal S_K(w)
=
\operatorname{Tr}(D_K^2+w)^{-1}.
}
\]

This is substantially cleaner than the generalized boundary-vector representation of v13.264.

The v13.264 no-go remains correct: `mathcal S_K` is not an ordinary one-vector resolvent. But it is naturally a **resolvent trace**.

## 9. Spectral determinant interpretation

If `A_K=D_K^2` is the positive spectral operator above, then formally and after the standard determinant regularization appropriate to the spectrum,

\[
\frac{d}{dw}\log\det(A_K+w)
=
\operatorname{Tr}(A_K+w)^{-1}.
\]

From the previous section,

\[
\frac{d}{dw}\log\det(A_K+w)
=
2\frac{d}{dw}\log\Psi_K(w).
\]

Hence the normalized characteristic determinant must satisfy

\[
\boxed{
\det(A_K+w)
\propto
\Psi_K(w)^2.
}
\]

The square has an exact multiplicity meaning:

- `Psi_K` folds the pair `+i gamma,-i gamma` into one zero at `-gamma^2` of multiplicity `m`;
- `A_K=D_K^2` has the squared eigenvalue `gamma^2` with multiplicity `2m`;
- therefore the determinant of `A_K+w` has zero multiplicity `2m`, matching `Psi_K(w)^2`.

This is the determinant counterpart of the factor `2` in `mathcal S_K`.

## 10. Finite-interval positive characteristic determinants

Suzuki's finite-interval framework produces self-adjoint operators with discrete spectra on each fixed interval. For the first-order self-adjoint extension `D_{K,a}` relevant to the D12/Dedekind package, define

\[
A_{K,a}=D_{K,a}^2\ge0.
\]

Its squared spectrum is nonnegative.

A normalized spectral determinant of `A_{K,a}+w`, whenever defined by the standard regularized or relative construction, has zeros only at

\[
\boxed{w=-\lambda_{j,a}^2\le0.}
\]

Thus every finite-interval characteristic determinant lies in the real-negative-zero class that the limiting arithmetic function must inherit under GRH.

This suggests a stronger target than convergence of Weyl functions:

\[
\boxed{
\mathfrak Z_{K,a}(w)
\longrightarrow
\Psi_K(w)^2.
}
\]

Here `mathfrak Z_{K,a}` denotes a normalized finite-interval squared spectral determinant.

If this convergence is locally uniform on the complex plane (or on a domain large enough to control all zeros), Hurwitz's theorem forces every zero of the nonzero limit `Psi_K^2` to lie in the closure of the finite negative-real zero set.

Therefore

\[
\boxed{
\mathfrak Z_{K,a}\to\Psi_K^2
\text{ locally uniformly}
\Longrightarrow
\mathrm{GRH}(\zeta_K).
}
\]

This is a determinant form of the operator program.

## 11. Relative determinant is explicitly controlled by the 2x2 boundary matrix

The determinant in Section 2 has a standard relative interpretation for the extension pair.

At the first-order level, the relative perturbation determinant is proportional, after normalization, to

\[
\Delta_{a,\Theta}(z)
=
\det(\Theta_a-M_a(z)).
\]

At the squared level, the relative determinant between `D_{a,Theta}^2+w` and `D_{a,0}^2+w` is therefore encoded by

\[
\boxed{
\mathfrak D_{a,\Theta}(w)
=
\Delta_{a,\Theta}(i\sqrt w)
\Delta_{a,\Theta}(-i\sqrt w).
}
\]

Its logarithmic derivative is exactly the squared-resolvent trace difference:

\[
\boxed{
\partial_w\log\mathfrak D_{a,\Theta}(w)
=
\operatorname{Tr}\Bigl[
(D_{a,\Theta}^2+w)^{-1}
-(D_{a,0}^2+w)^{-1}
\Bigr].
}
\]

Thus the entire extension correction is now a scalar determinant factor rather than a matrix-valued mismatch.

This is the cleanest form of the v13.267 reduction.

## 12. Arithmetic truncation also integrates to a characteristic factor

From v13.266, define the explicit finite arithmetic approximation

\[
\mathcal S_{K,a}^{\rm arith}(w)
\]

on the real Euler-product axis `w>1/4`, using the exact completed archimedean terms together with the truncated positive prime-power transform at cutoff `T=2a`.

Fix one normalization point

\[
w_*\in(1/4,\infty).
\]

Define the normalized arithmetic characteristic factor by

\[
\boxed{
\frac{\Psi_{K,a}^{\rm arith}(w)}
{\Psi_{K,a}^{\rm arith}(w_*)}
:=
\exp\left(
\frac12
\int_{w_*}^{w}
\mathcal S_{K,a}^{\rm arith}(u)\,du
\right).
}
\]

Similarly,

\[
\frac{\Psi_K(w)}{\Psi_K(w_*)}
=
\exp\left(
\frac12
\int_{w_*}^{w}
\mathcal S_K(u)\,du
\right).
\]

Hence

\[
\boxed{
\log
\frac{
\Psi_{K,a}^{\rm arith}(w)/\Psi_{K,a}^{\rm arith}(w_*)
}{
\Psi_K(w)/\Psi_K(w_*)
}
=
\frac12
\int_{w_*}^{w}
\bigl(
\mathcal S_{K,a}^{\rm arith}(u)-\mathcal S_K(u)
\bigr)du.
}
\]

Using the exponential real-axis error from v13.266, on every compact interval

\[
J\Subset(1/4,\infty)
\]

we obtain

\[
\boxed{
\frac{
\Psi_{K,a}^{\rm arith}(w)/\Psi_{K,a}^{\rm arith}(w_*)
}{
\Psi_K(w)/\Psi_K(w_*)
}
=
1+O_J\!\left((1+a)^2e^{-2a(\sqrt{w_0}-1/2)}\right)
}
\]

uniformly for `w in J`, where `w_0=min J`.

Thus the arithmetic characteristic factor already converges exponentially fast on the real axis.

The remaining determinant mismatch is entirely operator-theoretic.

## 13. Determinant-level three-term decomposition

Let

\[
\mathfrak Z_{K,a}^{\Theta}(w)
\]

be a normalized squared spectral determinant for the chosen finite-interval extension, and let

\[
\mathfrak Z_{K,a}^{0}(w)
\]

be the corresponding reference determinant.

Then schematically, after choosing compatible normalizations at `w_*`,

\[
\boxed{
\frac{\mathfrak Z_{K,a}^{\Theta}(w)}{\Psi_K(w)^2}
=
\underbrace{
\frac{\mathfrak Z_{K,a}^{\Theta}(w)}{\mathfrak Z_{K,a}^{0}(w)}
}_{\text{2x2 boundary determinant}}
\cdot
\underbrace{
\frac{\mathfrak Z_{K,a}^{0}(w)}{igl(\Psi_{K,a}^{\rm arith}(w)\bigr)^2}
}_{\text{reference determinant defect}}
\cdot
\underbrace{
\frac{igl(\Psi_{K,a}^{\rm arith}(w)\bigr)^2}{\Psi_K(w)^2}
}_{\text{explicit arithmetic tail}}.
}
\]

The first factor is controlled by

\[
\mathfrak D_{a,\Theta}(w)
=
\left|\det(\Theta_a-M_a(i\sqrt w))\right|^2
\]

up to the chosen relative normalization.

The third factor converges exponentially fast on every compact real interval `w>1/4` by v13.266 and Section 12.

Therefore the only genuinely structural factor left is

\[
\boxed{
\frac{\mathfrak Z_{K,a}^{0}(w)}{igl(\Psi_{K,a}^{\rm arith}(w)\bigr)^2}.
}
\]

This is a sharper version of the reference-response defect from v13.267.

Instead of comparing two Weyl functions, one now compares two scalar characteristic determinants.

## 14. Why this is a better next target

The Weyl-matrix route had three normalization problems:

1. the boundary triplet is not canonical;
2. the Weyl function changes under boundary-coordinate transformations;
3. the scalar Dedekind channel is only a compression of a matrix problem.

The determinant route removes most of this ambiguity:

- the extension-pair relative determinant is scalar;
- it is H4 invariant;
- the square map is built in;
- the arithmetic target `Psi_K^2` is also scalar;
- zero multiplicities match exactly;
- the GRH statement becomes a real-negative-zero statement for one entire function.

Thus the operator frontier should now be formulated as

\[
\boxed{
\text{construct normalized finite-interval squared characteristic determinants}
\quad\text{and prove}
\quad
\mathfrak Z_{K,a}\to\Psi_K^2.
}
\]

This is closer to Suzuki's own characteristic-entire-function viewpoint than the earlier boundary-vector resolvent ansatz.

## 15. Source-audit refinement

Suzuki's current arXiv v2 (August 2026) states unconditionally that the finite-interval localized Weil form admits a canonical self-adjoint operator `A_a`, identifies it as the Friedrichs extension of `B_a=D^*G_aD`, and records that `A_a` has discrete lower-bounded spectrum with only `+infinity` as an accumulation point.

His paper also formulates the infinite-volume Hilbert-Pólya limit through self-adjoint finite-interval first-order realizations without assuming RH.

The present entry does **not** claim Suzuki proves the determinant convergence above, nor that his Riemann-zeta finite-interval operator has already been constructed for the D12 Dedekind direct sum.

The determinant criterion is a derived target for the audited D12 extension of that framework.

## 16. What is exact and what remains open

### Exact in this entry

1. Boundary-triplet Weyl matrices are not canonical scalar targets without fixed normalization.
2. The extension resolvent trace difference is
   \[
   -\partial_z\log\det(\Theta-M(z)).
   \]
3. The squared extension trace difference is
   \[
   \partial_w\log\bigl[\Delta(i\sqrt w)\Delta(-i\sqrt w)\bigr].
   \]
4. For self-adjoint data and `w>0`, the squared determinant is
   \[
   |\det(\Theta-M(i\sqrt w))|^2>0.
   \]
5. The folded completed Dedekind function
   \[
   \Psi_K(w)=\xi_K(1/2+\sqrt w)
   \]
   is entire.
6. The arithmetic target satisfies
   \[
   \boxed{\mathcal S_K=2\Psi_K'/\Psi_K.}
   \]
7. Under the critical-line spectral model,
   \[
   \mathcal S_K(w)=\operatorname{Tr}(D_K^2+w)^{-1}.
   \]
8. The corresponding spectral determinant must be proportional to
   \[
   \Psi_K(w)^2.
   \]
9. The arithmetic finite-cutoff characteristic factor converges exponentially on compact real intervals `w>1/4`.

### Still open

1. Constructing the canonical D12 finite-interval first-order extension directly from the Dedekind screw package.
2. Choosing/identifying the finite spectral determinant normalization compatible with the D12 direct sum.
3. Proving
   \[
   \mathfrak Z_{K,a}^{0}/(\Psi_{K,a}^{\rm arith})^2\to1.
   \]
4. Controlling the finite 2x2 boundary determinant if a nonreference extension is required.
5. Upgrading real-axis convergence to the characteristic-function convergence needed to force the global zero geometry.

No RH or GRH theorem is proved here.

## 17. Immediate next move

The remaining reference determinant defect is now scalar.

The next derivation should therefore examine the finite-interval Fredholm/form determinant attached to the restricted convolution operator

\[
G_a=P_aGP_a
\]

and the Friedrichs operator

\[
A_a=(D^*G_aD)_F.
\]

The key question is whether the ratio

\[
\boxed{
\frac{\det_{\rm rel}(A_{K,a}+w)}{(\Psi_{K,a}^{\rm arith}(w))^2}
}
\]

can be expressed as an endpoint determinant or a trace-class Fredholm determinant whose kernel norm tends to zero as `a->infinity` on `w>1/4`.

If yes, the last infinite-dimensional mismatch becomes a norm estimate.

If not, the next step is to use the exact identity

\[
\mathcal S_K=2\Psi_K'/\Psi_K
\]

and move fully into characteristic-entire-function / de Branges convergence, where Suzuki's finite-interval boundary entire functions are the natural objects to compare directly with `Psi_K` rather than with the Weyl matrix.
