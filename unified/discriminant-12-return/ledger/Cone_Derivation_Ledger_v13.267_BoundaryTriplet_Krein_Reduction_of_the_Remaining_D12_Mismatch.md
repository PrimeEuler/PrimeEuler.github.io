# Cone Derivation Ledger v13.267 — Boundary-Triplet / Krein Reduction of the Remaining D12 Mismatch

Date: 2026-09-06
Status: EXACT OPERATOR REDUCTION + FINITE-DIMENSIONAL BOUNDARY CRITERION — RH/GRH NOT PROVED

## 0. Synchronization

Immediately before this write, the authoritative project README, current `master` tip, and the ledger state were re-fetched. The current tip remained

`3c374fd216c6d9e493263091bab956b9757f2efc`,

with v13.266 the highest ledger checkpoint and no v13.267 external-audit file present.

The previous entry proved that the finite-interval arithmetic ramp itself already converges to the full Euler-product logarithmic derivative exponentially fast on every compact real interval `w>1/4`.

Therefore the unresolved analytic burden sits in the map

\[
\text{restricted screw/form kernel}
\longrightarrow
\text{finite-interval self-adjoint extension / boundary Weyl response}.
\]

This entry isolates that burden using the standard boundary-triplet / Krein resolvent formalism.

The main conclusion is:

\[
\boxed{
\text{all dependence on the choice of finite-interval self-adjoint boundary condition is carried by a }2\times2\text{ matrix.}
}
\]

Thus the D12 two-channel extension mismatch is finite-rank and finite-dimensional even though the underlying form/kernel problem is infinite-dimensional.

A second important guardrail is retained:

\[
\boxed{
\text{this does not yet identify the arithmetic truncation of v13.266 with a canonical reference Weyl response.}
}
\]

So after v13.267 the remaining problem splits cleanly into a **reference-response identification** plus a **2x2 boundary correction estimate**.

## 1. Boundary-triplet setup for the D12 two-channel operator

Let `S_a` be the closed symmetric first-order operator associated with the finite-interval D12 two-channel form package on `[-a,a]`.

From v13.265 the full two-channel deficiency indices are

\[
\boxed{n_+(S_a)=n_-(S_a)=2.}
\]

Choose an ordinary boundary triplet

\[
\boxed{
(\mathbf C^2,\Gamma_0,\Gamma_1)
}
\]

for `S_a^*`.

Thus Green's identity is

\[
\langle S_a^*f,g\rangle-\langle f,S_a^*g\rangle
=
\langle \Gamma_1f,\Gamma_0g\rangle_{\mathbf C^2}
-
\langle \Gamma_0f,\Gamma_1g\rangle_{\mathbf C^2}.
\]

Take the reference self-adjoint extension

\[
\boxed{
D_{a,0}:=S_a^*\big|_{\ker\Gamma_0}.
}
\]

For `z` in the resolvent set of `D_{a,0}`, define the gamma field

\[
\gamma_a(z)
:=
\left(\Gamma_0\big|_{\ker(S_a^*-z)}\right)^{-1},
\]

and the matrix Weyl function

\[
\boxed{
M_a(z):=\Gamma_1\gamma_a(z).
}
\]

Here

\[
M_a(z)\in\mathbf C^{2\times2}.
\]

The two-dimensional boundary space is exactly what the deficiency count in v13.265 predicts.

## 2. General self-adjoint extensions and Krein's formula

Let `Theta_a` be a self-adjoint `2x2` boundary matrix. The corresponding self-adjoint extension is

\[
\boxed{
D_{a,\Theta}
:=
S_a^*\big|_{\Gamma_1f=\Theta_a\Gamma_0f}.
}
\]

Whenever `z` belongs to the common resolvent set and `Theta_a-M_a(z)` is invertible, Krein's resolvent formula gives

\[
\boxed{
(D_{a,\Theta}-z)^{-1}
-
(D_{a,0}-z)^{-1}
=
\gamma_a(z)
(\Theta_a-M_a(z))^{-1}
\gamma_a(\bar z)^*.
}
\]

This is the first load-bearing result of the present entry.

Because the middle factor acts on `C^2`, the extension-dependent resolvent correction has rank at most two:

\[
\boxed{
\operatorname{rank}
\left[(D_{a,\Theta}-z)^{-1}-(D_{a,0}-z)^{-1}\right]
\le2.
}
\]

Therefore every finite-interval self-adjoint-boundary effect in the full D12 pair is a finite-rank perturbation of a chosen reference extension.

No RH input is involved.

## 3. H4 covariance at the boundary-triplet level

Let

\[
U_2
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}
\]

be the normalized D12 Hadamard transform.

Transport the boundary maps by

\[
\boxed{
\widetilde\Gamma_j
:=U_2\Gamma_j,
\qquad j=0,1.
}
\]

Then `(C^2,\widetilde\Gamma_0,\widetilde\Gamma_1)` is again a boundary triplet, and its Weyl matrix is

\[
\boxed{
\widetilde M_a(z)
=U_2M_a(z)U_2^*.
}
\]

Similarly a boundary matrix transforms as

\[
\boxed{
\widetilde\Theta_a
=U_2\Theta_aU_2^*.
}
\]

Therefore

\[
\widetilde\Theta_a-\widetilde M_a(z)
=
U_2(\Theta_a-M_a(z))U_2^*.
\]

Hence

\[
\boxed{
(\widetilde\Theta_a-\widetilde M_a(z))^{-1}
=
U_2(\Theta_a-M_a(z))^{-1}U_2^*.
}
\]

Thus the exact H4/Hadamard covariance established in v13.265 survives all the way to the Krein boundary correction.

## 4. Character basis versus split/inert basis

When the character-basis boundary data are uncoupled, write

\[
M_{\rm char,a}(z)
=
\begin{pmatrix}
m_{0,a}(z)&0\\
0&m_{12,a}(z)
\end{pmatrix}.
\]

Then in split/inert coordinates

\[
\boxed{
M_{S/I,a}(z)
=
\frac12
\begin{pmatrix}
m_{K,a}(z)&m_{\Delta,a}(z)\\
m_{\Delta,a}(z)&m_{K,a}(z)
\end{pmatrix},
}
\]

with

\[
\boxed{
m_{K,a}=m_{0,a}+m_{12,a},\qquad
m_{\Delta,a}=m_{0,a}-m_{12,a}.}
\]

This is the boundary-triplet analogue of the kernel, form, and operator block identities in v13.260-v13.265.

The Dedekind field response remains the common diagonal self-sector:

\[
\boxed{
[M_{S/I,a}]_{SS}
=[M_{S/I,a}]_{II}
=\frac12m_{K,a}.
}
\]

The principal/quadratic difference remains off-diagonal.

## 5. Squared resolvent and the `w=z^2` variable

For a self-adjoint first-order operator `D` and `w>0`, put

\[
\kappa=\sqrt w.
\]

Then the exact functional-calculus identity is

\[
\boxed{
(D^2+w)^{-1}
=
\frac1{2i\kappa}
\left[
(D-i\kappa)^{-1}
-
(D+i\kappa)^{-1}
\right].
}
\]

Apply this to the two finite-interval extensions `D_{a,Theta}` and `D_{a,0}`.

Define the squared-resolvent correction

\[
\Delta^{(2)}_{a,\Theta}(w)
:=
(D_{a,\Theta}^2+w)^{-1}
-
(D_{a,0}^2+w)^{-1}.
\]

Substituting Krein's formula at `z=\pm i\kappa` gives the exact identity

\[
\boxed{
\begin{aligned}
\Delta^{(2)}_{a,\Theta}(w)
={1\over2i\kappa}
\Big[&
\gamma_a(i\kappa)
(\Theta_a-M_a(i\kappa))^{-1}
\gamma_a(-i\kappa)^*
\\
-&
\gamma_a(-i\kappa)
(\Theta_a-M_a(-i\kappa))^{-1}
\gamma_a(i\kappa)^*
\Big].
\end{aligned}
}
\]

Therefore

\[
\boxed{
\operatorname{rank}\Delta^{(2)}_{a,\Theta}(w)\le4,
}
\]

and, more sharply, it is built from two rank-at-most-two boundary terms.

The infinite-dimensional extension problem has been reduced to the two matrices

\[
\boxed{
\Theta_a-M_a(i\sqrt w),
\qquad
\Theta_a-M_a(-i\sqrt w).
}
\]

## 6. Exact norm bound for the boundary correction

From the preceding formula,

\[
\boxed{
\begin{aligned}
\|\Delta^{(2)}_{a,\Theta}(w)\|
\le {1\over2\sqrt w}
\sum_{\sigma=\pm1}
&\|\gamma_a(i\sigma\sqrt w)\|
\|\gamma_a(-i\sigma\sqrt w)\|
\\
&\times
\|(\Theta_a-M_a(i\sigma\sqrt w))^{-1}\|.
\end{aligned}
}
\]

Using the adjoint symmetry of the gamma/Weyl data for an ordinary boundary triplet, this may be simplified on the real `w>0` axis to the schematic estimate

\[
\boxed{
\|\Delta^{(2)}_{a,\Theta}(w)\|
\lesssim
{1\over\sqrt w}
\|\gamma_a(i\sqrt w)\|^2
\|(\Theta_a-M_a(i\sqrt w))^{-1}\|,
}
\]

with the exact two-term bound above retained as the rigorous statement.

This gives a concrete sufficient condition for disappearance of the boundary-condition mismatch.

For a compact interval

\[
J\subset(1/4,\infty),
\]

if

\[
\boxed{
\sup_{w\in J}
\sum_{\sigma=\pm1}
\|\gamma_a(i\sigma\sqrt w)\|
\|\gamma_a(-i\sigma\sqrt w)\|
\|(\Theta_a-M_a(i\sigma\sqrt w))^{-1}\|
\longrightarrow0,
}
\]

then

\[
\boxed{
\sup_{w\in J}
\|\Delta^{(2)}_{a,\Theta}(w)\|
\longrightarrow0.
}
\]

Thus the extension-choice part of the finite-interval mismatch is reduced to an explicit `2x2` boundary estimate.

## 7. Scalar split-sector compression

Let `e_S=(1,0)^T` in split/inert boundary coordinates.

For any Hilbert-space probe `f` for which the scalar resolvent pairing is defined, the split-sector correction is

\[
\delta_{S,a}(w;f)
:=
\langle f,\Delta^{(2)}_{a,\Theta}(w)f\rangle.
\]

Then

\[
\boxed{
|\delta_{S,a}(w;f)|
\le
\|f\|^2\,\|\Delta^{(2)}_{a,\Theta}(w)\|.
}
\]

For the rigged-Hilbert-space boundary probes identified in v13.264, the same finite-rank formula persists after replacing ordinary Hilbert pairings by the corresponding `H_{-1},H_{+1}` dual pairing, provided the gamma field is interpreted between the appropriate scale spaces.

The load-bearing point is unchanged:

\[
\boxed{
\text{the split-sector boundary mismatch is controlled by a }2\times2\text{ inverse boundary matrix.}
}
\]

## 8. Correct three-term decomposition of the full finite-interval error

Let

\[
s_{K,a}^{\Theta}(w)
\]

denote the actual finite-interval squared boundary response of the chosen self-adjoint extension.

Let

\[
s_{K,a}^{0}(w)
\]

denote the corresponding response for the reference extension `D_{a,0}`.

Let

\[
\mathcal S_{K,a}^{\rm arith}(w)
\]
be the explicit finite arithmetic approximation from v13.266.

Then the exact algebraic decomposition is

\[
\boxed{
\begin{aligned}
s_{K,a}^{\Theta}(w)-\mathcal S_K(w)
={}&
\underbrace{
\bigl[s_{K,a}^{\Theta}(w)-s_{K,a}^{0}(w)\bigr]
}_{\text{finite-dimensional Krein boundary correction}}
\\
&+
\underbrace{
\bigl[s_{K,a}^{0}(w)-\mathcal S_{K,a}^{\rm arith}(w)\bigr]
}_{\text{reference-response identification defect}}
\\
&+
\underbrace{
\bigl[\mathcal S_{K,a}^{\rm arith}(w)-\mathcal S_K(w)\bigr]
}_{\text{explicit exponentially small arithmetic tail}}.
\end{aligned}
}
\]

This is the cleanest formulation of the frontier obtained so far.

The third term is controlled quantitatively by v13.266.

The first term is now finite-dimensional and controlled by the Krein estimate above.

The genuinely structural unresolved term is the middle one:

\[
\boxed{
s_{K,a}^{0}(w)-\mathcal S_{K,a}^{\rm arith}(w).}
\]

This is precisely the question of whether a natural reference boundary triplet/extension reads the restricted screw kernel in the same way that the arithmetic ramp transform does.

## 9. Why v13.266 did not already solve the operator problem

The arithmetic transform

\[
\mathfrak M_{K,2a}(z)
=
z^2\int_0^{2a}R_K(t)e^{-zt}\,dt
\]

is linear in the restricted arithmetic ramp.

A boundary Weyl function, by contrast, is obtained from deficiency solutions and the inverse boundary map

\[
\Gamma_0|_{\ker(S_a^*-z)}.
\]

That dependence is nonlinear in the underlying operator/form data.

Therefore one may not identify

\[
\mathcal S_{K,a}^{\rm arith}
\]

with

\[
s_{K,a}^{0}
\]

merely because both are built from the same finite-interval kernel.

This is the principal guardrail of the present entry.

## 10. A sufficient criterion that now implies the v13.265 convergence hypothesis

Let

\[
J\subset(1/4,\infty)
\]

be a nonempty compact real interval.

Suppose the following two conditions hold:

### A. Reference-response identification

\[
\boxed{
\sup_{w\in J}
|s_{K,a}^{0}(w)-\mathcal S_{K,a}^{\rm arith}(w)|
\longrightarrow0.
}
\]

### B. Boundary correction decay

\[
\boxed{
\sup_{w\in J}
|s_{K,a}^{\Theta}(w)-s_{K,a}^{0}(w)|
\longrightarrow0.
}
\]

Condition B follows, for example, from the explicit gamma/Weyl matrix norm criterion in Section 6.

Then v13.266 gives

\[
\sup_{w\in J}
|\mathcal S_{K,a}^{\rm arith}(w)-\mathcal S_K(w)|
\longrightarrow0,
\]

hence

\[
\boxed{
\sup_{w\in J}
|s_{K,a}^{\Theta}(w)-\mathcal S_K(w)|
\longrightarrow0.
}
\]

This is stronger than the pointwise real-axis convergence hypothesis required by v13.265.

Accordingly, if the finite squared boundary responses are Stieltjes functions as in v13.265, Conditions A+B imply the GRH conclusion of that criterion.

Again: the present entry does not establish A or B for Suzuki's finite-interval operator. It isolates them exactly.

## 11. Boundary coupling and the D12 off-diagonal defect

In split/inert coordinates write

\[
M_{S/I,a}(z)
=
{1\over2}
\begin{pmatrix}
m_{K,a}&m_{\Delta,a}\\
m_{\Delta,a}&m_{K,a}
\end{pmatrix}.
\]

A general self-adjoint boundary matrix has the form

\[
\Theta_{S/I,a}
=
\begin{pmatrix}
\theta_{SS}&\theta_{SI}\\
\overline{\theta_{SI}}&\theta_{II}
\end{pmatrix}.
\]

Then the only matrix that must be inverted is

\[
\boxed{
\Theta_{S/I,a}-M_{S/I,a}(z).
}
\]

Its determinant is explicit:

\[
\boxed{
\det(\Theta-M)
=
\left(\theta_{SS}-{m_K\over2}\right)
\left(\theta_{II}-{m_K\over2}\right)
-
\left(\theta_{SI}-{m_\Delta\over2}\right)
\left(\overline{\theta_{SI}}-{m_\Delta\over2}\right).
}
\]

Thus the previously identified off-diagonal principal/quadratic defect `m_Delta` enters the finite-interval extension theory in one exact place: the `2x2` boundary determinant and its inverse.

This is a useful structural localization.

The field self-sector is diagonal, while the split/inert imbalance controls cross-boundary coupling.

## 12. Decoupled boundary conditions

If the boundary matrix is diagonal in the character basis,

\[
\Theta_{\rm char,a}
=
\operatorname{diag}(\theta_{0,a},\theta_{12,a}),
\]

then the two character channels remain extension-decoupled and

\[
(\Theta_{\rm char}-M_{\rm char})^{-1}
=
\operatorname{diag}
\left(
{1\over\theta_0-m_0},
{1\over\theta_{12}-m_{12}}
\right).
\]

After H4 rotation, the correction has the familiar field/defect form

\[
\boxed{
{1\over2}
\begin{pmatrix}
r_0+r_{12}&r_0-r_{12}\\
r_0-r_{12}&r_0+r_{12}
\end{pmatrix},
}
\]

where

\[
r_D(z):={1\over\theta_D-m_D(z)}.
\]

So the common self-sector / off-diagonal defect pattern persists even through the nonlinear inverse boundary matrix.

That persistence is special to the two-channel Hadamard algebra and is exact.

## 13. What is now finite-dimensional

After v13.267, all of the following extension-dependent quantities are controlled by `2x2` data:

- the self-adjoint boundary parameter `Theta_a`;
- the Weyl matrix `M_a(z)`;
- the inverse `(
Theta_a-M_a(z))^{-1}`;
- the finite-rank first-order resolvent correction;
- the finite-rank squared-resolvent correction;
- the split/inert cross-boundary coupling.

Thus the remaining boundary-condition analysis no longer requires direct control of an arbitrary infinite-dimensional resolvent difference.

It requires control of

\[
\boxed{
\gamma_a(\pm i\sqrt w)
\quad\text{and}\quad
(\Theta_a-M_a(\pm i\sqrt w))^{-1}.
}
\]

## 14. What remains genuinely infinite-dimensional

The reference-response identification defect

\[
\boxed{
s_{K,a}^{0}-\mathcal S_{K,a}^{\rm arith}}
\]

still depends on how the restricted screw/form operator determines the deficiency solutions and boundary maps.

This is where one must use the actual finite-interval operator construction, not merely abstract extension theory.

So the frontier is now separated into:

\[
\boxed{
\text{kernel-to-reference-Weyl map}
}
\]

and

\[
\boxed{
\text{finite-dimensional boundary correction}.
}
\]

The second is structurally solved; the first remains open.

## 15. Strategic consequence

The full real-axis convergence problem can now be organized as

\[
\boxed{
\begin{array}{ccccc}
\text{restricted D12 screw kernel}
&\longrightarrow&
s_{K,a}^{0}
&\longrightarrow&
s_{K,a}^{\Theta}
\\
&&\updownarrow&&\downarrow
\\
\mathcal S_{K,a}^{\rm arith}
&\longrightarrow&
\mathcal S_K
&&
\text{Stieltjes limit}
\end{array}
}
\]

with:

1. the lower horizontal convergence exponentially controlled by v13.266;
2. the upper right correction reduced to a `2x2` Krein term in the present entry;
3. only the upper-left vertical identification still requiring detailed finite-interval analysis.

That upper-left arrow is now the highest-value target.

## 16. Next frontier

The next derivation should use the actual restricted screw kernel to compute or characterize the reference gamma field and reference Weyl matrix.

The most promising concrete tests are:

1. choose the natural reference extension determined by the finite-interval derivative operator and Suzuki form norm;
2. solve the deficiency equation
   \[
   (S_a^*-z)f=0
   \]
   in terms of the kernel operator;
3. express
   \[
   M_a(z)=\Gamma_1\gamma_a(z)
   \]
   as a boundary Schur complement;
4. compare that expression on `z=i\sqrt w`, `w>1/4`, directly with the finite arithmetic transform of v13.266;
5. isolate any remaining discrepancy as an endpoint term in `a`.

If the reference-response identification defect can be reduced to an endpoint quantity and shown to vanish, then together with the explicit `2x2` Krein estimate and the exponential arithmetic tail, the v13.265 real-axis Stieltjes criterion would become a genuinely quantitative operator-convergence problem.

No RH or GRH theorem is claimed here.