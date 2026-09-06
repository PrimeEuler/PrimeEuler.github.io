# Cone Derivation Ledger v13.265 — H4 Covariance of Finite-Interval Weyl Functions and a Real-Axis Stieltjes Criterion

Date: 2026-09-05
Status: EXACT OPERATOR-COVARIANCE RESULT + SHARP CONVERGENCE CRITERION — RH/GRH NOT PROVED

## 0. Synchronization and scope

Immediately before this write, the authoritative project README, current `master` tip, and v13.264 were re-fetched. The current tip remained

`ab0ec262e50dc2a1909c16054b4854a604ec5ed7`,

with v13.264 the highest ledger checkpoint and no newer external-audit entry present.

This entry tests the next target proposed in v13.264:

\[
\text{does the D12/H4 transform survive the finite-interval derivative, Friedrichs-extension,
 deficiency-space, and boundary-Weyl constructions?}
\]

The answer is yes at the level of exact unitary covariance, with one important correction:

\[
\boxed{
\text{the full D12 two-channel direct sum has deficiency indices }(2,2),\text{ not }(1,1).
}
\]

Thus the scalar Dedekind field channel is a boundary compression of a matrix Weyl problem; it is not automatically the Weyl function of a single deficiency-`(1,1)` operator.

The second main result is a sharp normal-family criterion:

\[
\boxed{
\text{pointwise convergence of positive finite-interval squared Weyl functions on one real interval}
\Longrightarrow
\text{GRH for }\zeta_{\mathbf Q(\sqrt3)},
}
\]

provided the limit is the arithmetic function `mathcal S_K` of v13.263.

This reduces the operator-identification problem from complex local-uniform convergence to a real-axis convergence problem.

## 1. Abstract finite-interval channel package

Fix a finite interval `[-a,a]`. For each analytic character channel `D`, let

\[
q_{D,a}
\]

be the closed semibounded quadratic form associated with the restricted screw/Weil kernel, and let

\[
G_{D,a}
\]

denote its corresponding kernel/form operator before differentiation, in the sense of the finite-interval Suzuki construction inherited from v13.264.

For the D12 pair use

\[
D\in\{0,12\}.
\]

On the algebraic two-channel core write

\[
\mathcal C_a
=
C_c^\infty(-a,a)\otimes\mathbf C^2.
\]

The normalized two-channel Hadamard transform is

\[
\boxed{
U_2=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
}
\]

It acts only on the finite channel coordinate and is independent of `x`.

Define the character-basis kernel block

\[
\mathbf G_{\rm char,a}
=
\begin{pmatrix}
G_{0,a}&0\\
0&G_{12,a}
\end{pmatrix},
\]

and the split/inert-basis block

\[
\boxed{
\mathbf G_{S/I,a}
=
U_2\mathbf G_{\rm char,a}U_2^*.
}
\]

Therefore

\[
\boxed{
\mathbf G_{S/I,a}
=
\frac12
\begin{pmatrix}
G_{0,a}+G_{12,a}&G_{0,a}-G_{12,a}\\
G_{0,a}-G_{12,a}&G_{0,a}+G_{12,a}
\end{pmatrix}.
}
\]

This is the finite-interval operator analogue of v13.262's sector-compression identity.

## 2. The H4 transform commutes exactly with differentiation

Let

\[
\mathscr D=i\frac d{dx}
\]

on the common algebraic core. On two-channel functions,

\[
\mathbf D=I_2\otimes\mathscr D.
\]

Since `U_2` is constant in `x`,

\[
\boxed{
(U_2\otimes I)\mathbf D
=
\mathbf D(U_2\otimes I).
}
\]

The same holds for the formal adjoint on the common core:

\[
\boxed{
(U_2\otimes I)\mathbf D^*
=
\mathbf D^*(U_2\otimes I).
}
\]

Hence if the character-basis symmetric form operator is

\[
\mathbf B_{\rm char,a}
=
\mathbf D^*\mathbf G_{\rm char,a}\mathbf D,
\]

then

\[
\boxed{
\mathbf B_{S/I,a}
=
U_2\mathbf B_{\rm char,a}U_2^*.
}
\]

Thus the finite internal Fourier transform survives the derivative sandwich exactly.

This is the first requested commuting square:

\[
\boxed{
H4\text{/Hadamard transform}
\quad\text{commutes with}\quad
D^*GD.
}
\]

## 3. Friedrichs extension is unitarily covariant

Let `B` be semibounded symmetric and let `B_F` be its Friedrichs extension. For any unitary `U`, the quadratic form of `UBU^*` is the transported form

\[
q_U[f]=q[U^*f].
\]

Closure and representation by a self-adjoint operator commute with unitary transport. Therefore

\[
\boxed{
(UBU^*)_F
=
UB_FU^*.
}
\]

Applying this to the D12 block gives

\[
\boxed{
\mathbf A_{S/I,a}
=
U_2
\begin{pmatrix}
A_{0,a}&0\\
0&A_{12,a}
\end{pmatrix}
U_2^*,
}
\]

where `A_{D,a}` denotes the channel Friedrichs extension.

So the H4/Hadamard transform also survives the finite-interval self-adjoint form construction exactly.

### Hilbert-space guardrail

The channel Hilbert norms induced after the Suzuki shift need not be equal.

Therefore the statement above should be interpreted as follows: form the direct-sum character Hilbert space first, then define the split/inert Hilbert space by transported inner product through `U_2`. With that definition, `U_2` is unitary by construction.

One must not silently assume that two independently completed residue-sector spaces carry identical scalar norms.

## 4. Deficiency spaces also transform, but their dimensions add

Let `S_0` and `S_{12}` be the two minimal closed symmetric first-order operators in the character channels. Source-established Suzuki-type finite-interval models motivate the scalar deficiency pattern

\[
n_+(S_D)=n_-(S_D)=1.
\]

For the direct sum

\[
\mathbf S_{\rm char}
=S_0\oplus S_{12},
\]

one has

\[
\ker(\mathbf S_{\rm char}^*-z)
=
\ker(S_0^*-z)
\oplus
\ker(S_{12}^*-z).
\]

Hence

\[
\boxed{
n_+(\mathbf S_{\rm char})
=n_-(\mathbf S_{\rm char})
=2.
}
\]

Unitary conjugation preserves adjoints and kernels, so

\[
\boxed{
n_+(\mathbf S_{S/I})
=n_-(\mathbf S_{S/I})
=2.
}
\]

This corrects an overly compressed reading of the target chain in v13.264.

The full D12 pair does **not** become a scalar deficiency-`(1,1)` problem merely because the Dedekind quadratic form appears as a common diagonal self-sector.

The four-channel H4 bank similarly has deficiency indices `(4,4)` if each scalar channel contributes `(1,1)`.

## 5. Why the scalar self-sector is not automatically reducing

From v13.262 the D12 residue-basis operator has the universal form

\[
\mathbf T_{S/I}
=
\frac12
\begin{pmatrix}
T_K&T_\Delta\\
T_\Delta&T_K
\end{pmatrix},
\]

with

\[
T_K=T_0+T_{12},
\qquad
T_\Delta=T_0-T_{12}.
\]

The split coordinate subspace is reducing only if

\[
T_\Delta=0.
\]

Generically this is false.

Therefore

\[
\boxed{
Q_K=2Q_{SS}
}
\]

as a scalar quadratic-form identity does **not** imply that the full two-channel operator restricts to the split coordinate as an autonomous self-adjoint operator.

This distinction is load-bearing for the Hilbert--Pólya program.

A scalar deficiency-`(1,1)` Dedekind operator, if it exists, requires an additional reduction/compression/boundary construction. It is not supplied for free by the finite Hadamard transform.

## 6. Boundary triples give the correct exact statement

Suppose each scalar symmetric channel admits a boundary triple

\[
(\mathbf C,\Gamma_{0,D},\Gamma_{1,D})
\]

with scalar Weyl function `m_D(z)`.

The direct sum has boundary space

\[
\mathbf C^2
\]

and matrix Weyl function

\[
\boxed{
M_{\rm char}(z)
=
\begin{pmatrix}
m_0(z)&0\\
0&m_{12}(z)
\end{pmatrix}.
}
\]

Rotate the boundary coordinates by the same Hadamard matrix `U_2`. The transformed Weyl matrix is

\[
\boxed{
M_{S/I}(z)
=
U_2M_{\rm char}(z)U_2^*
=
\frac12
\begin{pmatrix}
m_K(z)&m_\Delta(z)\\
m_\Delta(z)&m_K(z)
\end{pmatrix},
}
\]

where

\[
\boxed{
m_K=m_0+m_{12},
\qquad
m_\Delta=m_0-m_{12}.
}
\]

This is the exact boundary-level analogue of the D12 form compression.

In particular,

\[
\boxed{
m_K(z)=2[M_{S/I}(z)]_{SS}=2[M_{S/I}(z)]_{II}.
}
\]

So the field channel is an exact diagonal **boundary compression** of the matrix Weyl function.

That statement is stronger than a mere form analogy and weaker than claiming a standalone scalar operator exists. It is the correct level of generality.

## 7. Matrix Herglotz positivity survives H4

For an ordinary boundary triple of a symmetric operator, the Weyl matrix is a matrix-valued Nevanlinna/Herglotz function:

\[
\frac{\Im M(z)}{\Im z}\ge0.
\]

Unitary boundary rotation preserves this property:

\[
\Im(U M U^*)
=U(\Im M)U^*.
\]

Therefore

\[
\boxed{
M_{S/I}\text{ is matrix Herglotz whenever }M_{\rm char}\text{ is matrix Herglotz}.
}
\]

Every diagonal compression is then scalar Herglotz. Thus

\[
\boxed{
\frac12m_K(z)
=[M_{S/I}(z)]_{SS}
}
\]

inherits the scalar Herglotz sign on the finite-interval first-order problem.

Guardrail: this finite-interval Herglotz property is not yet the arithmetic critical-line Stieltjes function `mathcal S_K`; identifying the two in the infinite-volume limit remains the hard step.

## 8. Squared resolvents are the antisymmetrized first-order resolvents

Let `D=D^*` and choose the principal square root on

\[
\Omega=\mathbf C\setminus(-\infty,0].
\]

Then functional calculus gives

\[
\boxed{
(D^2+w)^{-1}
=
\frac1{2i\sqrt w}
\left[(D-i\sqrt w)^{-1}-(D+i\sqrt w)^{-1}\right].
}
\]

At the scalar boundary level, if

\[
m_D(z)
=\langle\phi,(D-z)^{-1}\phi\rangle
\]

is interpreted in the appropriate ordinary or rigged boundary pairing, then the squared boundary transform is

\[
\boxed{
s_D(w)
=
\frac{m_D(i\sqrt w)-m_D(-i\sqrt w)}{2i\sqrt w}.
}
\]

Thus the passage

\[
\boxed{
\text{first-order Herglotz Weyl function}
\longrightarrow
\text{squared Stieltjes Weyl function}
}
\]

is explicit, not heuristic.

Spectrally, the map is the pushforward

\[
\lambda\mapsto\lambda^2.
\]

If the first-order boundary measure is `rho`, then the squared measure is its positive pushforward under `lambda^2`, with masses from `+lambda` and `-lambda` added.

This exactly explains the folded multiplicity factor in v13.264.

## 9. D12 squared Weyl matrix

Apply the previous construction channelwise to the D12 pair. Let

\[
s_0(w),\qquad s_{12}(w)
\]

be the finite-interval squared boundary Stieltjes functions associated with positive operators `D_0^2` and `D_{12}^2`.

Then

\[
S_{\rm char}(w)
=
\begin{pmatrix}
s_0(w)&0\\
0&s_{12}(w)
\end{pmatrix}
\]

and

\[
\boxed{
S_{S/I}(w)
=
\frac12
\begin{pmatrix}
s_K(w)&s_\Delta(w)\\
s_\Delta(w)&s_K(w)
\end{pmatrix},
}
\]

where

\[
\boxed{
s_K=s_0+s_{12},
\qquad
s_\Delta=s_0-s_{12}.
}
\]

Every finite-interval `s_D` is Stieltjes because it is a boundary resolvent of a positive self-adjoint square. Hence the sum

\[
\boxed{s_K=s_0+s_{12}}
\]

is also Stieltjes.

This gives an unconditional finite-interval positive class in exactly the algebraic channel that should converge to the arithmetic

\[
\mathcal S_K(w)
=
\frac1{\sqrt w}
\frac{\xi_K'}{\xi_K}\left(\frac12+\sqrt w\right).
\]

The missing theorem is now solely the identification of the limit.

## 10. A normal-family lemma for Stieltjes functions

Let

\[
f_n(w)
=
\int_{[0,\infty)}\frac{d\nu_n(t)}{w+t},
\qquad
\nu_n\ge0,
\]

with

\[
\int\frac{d\nu_n(t)}{1+t}<\infty.
\]

Fix `w_0>0`. Suppose

\[
\sup_n f_n(w_0)<\infty.
\]

For every compact

\[
K\Subset\Omega=\mathbf C\setminus(-\infty,0],
\]

the ratio

\[
\frac{w_0+t}{w+t}
\]

is uniformly bounded for `w in K`, `t>=0`. Therefore

\[
|f_n(w)|
\le C_K f_n(w_0).
\]

Hence

\[
\boxed{\{f_n\}\text{ is a normal family on }\Omega.}
\]

Every locally uniform subsequential limit is a generalized Stieltjes function, possibly with a nonnegative constant term arising from weighted mass escaping to infinity.

If additionally the limit tends to zero as `w->+infinity`, that constant term vanishes and the limit is an ordinary Stieltjes transform.

## 11. Real-axis convergence is enough

This gives a much sharper criterion than v13.264's request for local-uniform complex convergence.

Let `s_{K,a}(w)` be finite-interval D12 squared boundary Weyl functions, each Stieltjes.

Assume there exists a nonempty open real interval

\[
J\subset(1/4,\infty)
\]

such that

\[
\boxed{
s_{K,a}(w)\longrightarrow\mathcal S_K(w)
\qquad
\text{for every }w\in J.
}
\]

The choice `J subset (1/4,infinity)` ensures

\[
s=\frac12+\sqrt w>1,
\]

so the arithmetic function is in the Euler-product zero-free half-plane and is unambiguously analytic there.

Pick `w_0 in J`. Pointwise convergence gives

\[
\sup_a s_{K,a}(w_0)<\infty
\]

after discarding at most finitely many initial terms, which do not affect the limit.

By the normal-family lemma, every subsequence has a locally uniformly convergent subsubsequence on `Omega`. Every such limit is generalized Stieltjes and agrees with `mathcal S_K` on `J`. By the identity theorem, all subsequential limits coincide.

Therefore the full family converges locally uniformly to an analytic generalized Stieltjes continuation of `mathcal S_K` on `Omega`.

Since the arithmetic `mathcal S_K(w)` satisfies

\[
\mathcal S_K(w)\to0
\qquad(w\to+\infty)
\]

from the gamma asymptotic and `zeta_K'/zeta_K(s)->0` as `s->+infinity`, the possible nonnegative constant term is absent.

Hence

\[
\boxed{
\mathcal S_K\text{ is an ordinary Stieltjes function on }\Omega.
}
\]

By v13.263, this forces all its poles to lie on the nonpositive real `w` axis, equivalently all centered nontrivial zeros satisfy

\[
\left(\rho-\frac12\right)^2\le0.
\]

Thus

\[
\boxed{
\Re\rho=\frac12.
}
\]

We obtain the following exact criterion.

## 12. Real-axis finite-interval criterion for D12 GRH

### Theorem

Suppose one constructs for each `a` a finite-interval D12 squared boundary Weyl function `s_{K,a}` satisfying:

1. `s_{K,a}` is a Stieltjes function on `C\(-infinity,0]`;
2. for every `w` in some open interval `J subset (1/4,infinity)`,
   \[
   s_{K,a}(w)\to\mathcal S_K(w),
   \]
   where
   \[
   \mathcal S_K(w)
   =\frac1{\sqrt w}\frac{\xi_K'}{\xi_K}\left(\frac12+\sqrt w\right).
   \]

Then

\[
\boxed{\mathrm{GRH}(\zeta_{\mathbf Q(\sqrt3)})}
\]

follows.

No complex-domain convergence hypothesis is needed separately.

This theorem does not prove GRH because condition 2 is open. Its value is to identify a strictly smaller analytic task than previously stated.

## 13. Even weaker identification data may suffice

The proof used the identity theorem only after normal-family compactness.

Therefore it is enough that convergence hold on any subset

\[
E\subset(1/4,\infty)
\]

having an accumulation point in `(1/4,infinity)`, provided one point of `E` supplies the uniform Stieltjes bound.

For example, convergence on a short real interval or on an infinite sequence accumulating at a finite positive point is sufficient.

Thus the hard operator/arithmetic bridge may be attacked through real positive spectral parameters only.

That is a significant simplification for numerical and analytic finite-interval work.

## 14. What H4 has now been shown to commute with

The D12/H4 transform now survives the following exact chain:

\[
\boxed{
\begin{array}{c}
\text{restricted screw kernels}\\
\downarrow D^*(\cdot)D\\
\text{symmetric form operators}\\
\downarrow\text{ Friedrichs extension}\\
\text{self-adjoint form operators}\\
\downarrow\text{ boundary triples}\\
\text{matrix Weyl functions}\\
\downarrow D\mapsto D^2\\
\text{matrix Stieltjes functions}.
\end{array}
}
\]

At every linear/unitary stage,

\[
\boxed{
U_2(\text{character object})U_2^*
=
\text{split/inert object}.
}
\]

So the finite `V_4/H_4` structure genuinely reaches the finite-interval spectral boundary data.

## 15. The exact place where scalarization fails

The only nontrivial caveat in the preceding chain is scalarization.

The D12 two-channel direct sum has deficiency `(2,2)` and a `2 x 2` Weyl matrix. Its Dedekind sum appears as

\[
\boxed{
m_K=2M_{SS}}
\]

or

\[
\boxed{s_K=2S_{SS}},
\]

but this diagonal compression does not automatically arise from a reducing scalar operator.

Therefore an unconditional scalar deficiency-`(1,1)` model for `zeta_K` remains an additional construction problem.

Fortunately the real-axis convergence theorem does not require such scalarization: a diagonal matrix compression of a positive matrix Stieltjes function is already scalar Stieltjes.

This removes an unnecessary obstacle.

## 16. Strategic consequence

The previous frontier was

\[
\text{construct a D12 scalar boundary operator and prove complex Weyl convergence}.
\]

The present result sharpens it to

\[
\boxed{
\text{construct the finite D12 matrix boundary problem}
\quad\text{and prove only real-axis convergence of its Dedekind diagonal compression}.
}
\]

More explicitly:

\[
\boxed{
S_{SS,a}(w)
\stackrel{?}{\longrightarrow}
\frac12\mathcal S_K(w)
\qquad
(w\in J\subset(1/4,\infty)).
}
\]

Because every finite `S_{SS,a}` is Stieltjes by positivity of the squared self-adjoint operator, real-axis identification on one interval would force the full Stieltjes continuation and hence the critical-line pole geometry.

This is now the shortest precise route on the Suzuki/operator branch.

## 17. Next high-value calculation

The next step should be quantitative rather than another abstract reformulation.

For real

\[
w>1/4,
\qquad
s=\frac12+\sqrt w>1,
\]

the arithmetic target has the explicit zero-free formula

\[
\mathcal S_K(w)
=
\frac1{\sqrt w}
\left[
\frac1s+\frac1{s-1}
+\frac12\log12-\log\pi
+\psi(s/2)
+\frac{\zeta_K'}{\zeta_K}(s)
\right].
\]

Using

\[
-\frac{\zeta_K'}{\zeta_K}(s)
=
\sum_{n\ge1}\frac{\Lambda(n)(1+\chi_{12}(n))}{n^s},
\]

the target on this real interval is determined by the already-audited positive prime-power measure.

Thus the next concrete task is to derive a finite-`a` expression for the diagonal squared Weyl function `S_{SS,a}(w)` and compare it term-by-term or variationally with this explicit real-axis arithmetic formula.

That comparison avoids all zero data and all critical-strip assumptions.

No RH or GRH statement is proved in this entry.