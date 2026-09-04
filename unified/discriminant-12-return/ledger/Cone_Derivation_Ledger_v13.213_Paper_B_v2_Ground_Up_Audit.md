# Cone Derivation Ledger v13.213 — Paper B v2 Ground-Up Audit

Date: 2026-09-04

Authoritative source audited:
`unified/discriminant-12-return/foundations/PaperB_EigenCoordinates_v2.tex`

Source blob at audit: `56f1d395e37e4f90f6434c6e2472785d122caa71`

## Verdict

**CORE CONTINUOUS LORENTZ GEOMETRY: PASS, WITH NORMALIZATION / WORDING CORRECTIONS REQUIRED BEFORE PAPER B IS AN AUDITED FOUNDATION BASELINE.**

The v2 source already repairs the strongest defects of the original Paper B: it restricts the orbit theorem to the signed cone, explicitly makes the eigen-coordinate power map dependent on a chosen equation, and correctly states that the parabolic failure is failure of diagonalization rather than failure of every power operation. The remaining work is mostly to make the intrinsic/projective structure explicit and to remove one normal-vector ambiguity.

## 1. Cone and Lie algebra

With
\[
X=(x-y)/2,\qquad Y^2=xy,\qquad T=(x+y)/2,
\]
the signed cone is
\[
X^2+Y^2=T^2,
\]
and the line `ax+by=c` becomes
\[
(a-b)X+(a+b)T=c.
\]

For
\[
L=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&0\end{pmatrix},\quad
B_X=\begin{pmatrix}0&0&1\\0&0&0\\1&0&0\end{pmatrix},\quad
B_Y=\begin{pmatrix}0&0&0\\0&0&1\\0&1&0\end{pmatrix},
\]
direct multiplication confirms
\[
[L,B_X]=B_Y,\qquad [L,B_Y]=-B_X,\qquad [B_X,B_Y]=-L.
\]
All three lie in `so(2,1)` for `eta=diag(1,1,-1)`.

**Status: PASS.**

## 2. Cutting-plane generator and invariant covector

Paper B defines
\[
G_{a,b}=(a+b)L+(a-b)B_Y
=\begin{pmatrix}
0&-(a+b)&0\\
a+b&0&a-b\\
0&a-b&0
\end{pmatrix}.
\]

Set
\[
\alpha=a+b,\qquad \gamma=a-b.
\]
Then
\[
m=(\gamma,0,-\alpha)
\]
satisfies `Gm=0`, and because
\[
\langle m,(X,Y,T)\rangle_\eta=\gamma X+\alpha T,
\]
the cutting functional is invariant under the flow.

The proof in v2 is now algebraically correct.

**Status: PASS.**

### Required wording correction

The subsequent classification proposition introduces
\[
n=(\gamma,0,+\alpha)
\]
and calls it the "plane normal." Its Lorentz norm happens to equal
\[
\gamma^2-\alpha^2=-4ab,
\]
so the displayed causal classification is numerically correct. However, the Lorentz metric-dual vector representing the plane functional is the already-defined
\[
\boxed{m=(\gamma,0,-\alpha)},
\]
not `n`.

The next version should use `m` consistently as the Lorentz normal. This removes an unnecessary Euclidean/Lorentz normal ambiguity.

## 3. Characteristic polynomial and trichotomy

Direct determinant expansion gives
\[
\chi_G(\lambda)=\lambda(\lambda^2+4ab).
\]
Also
\[
m^2=\gamma^2-\alpha^2=-4ab.
\]
Therefore:

- `ab>0`: timelike Lorentz normal; eigenvalues `0, ±2 i sqrt(ab)`; elliptic section.
- `ab=0`: null Lorentz normal; nilpotent generator; parabolic section.
- `ab<0`: spacelike Lorentz normal; eigenvalues `0, ±2 sqrt(-ab)`; hyperbolic section, with `c=0` separately degenerate.

This is the exact common invariant connecting Paper A's conic classification with the Lorentz generator type.

**Status: PASS.**

## 4. Intrinsic normalized generator

The source correctly observes
\[
G_{\kappa a,\kappa b}=\kappa G_{a,b},
\]
so the one-parameter subgroup as an unparameterized set depends only on the projective cutting direction `[a:b]`.

For the next audited version, make the scale-free generator explicit for `ab != 0`:
\[
\boxed{
\widehat G_{a,b}=\frac{G_{a,b}}{2\sqrt{|ab|}}.
}
\]
Then the nonzero eigenvalues are exactly
\[
\pm i\quad(ab>0),\qquad \pm1\quad(ab<0).
\]
A negative common rescaling reverses the flow orientation but leaves the subgroup/orbits unchanged.

This is the clean intrinsic Lorentz object; the unnormalized `G` remains useful when a particular equation is chosen.

## 5. Orbit theorem

For `ab != 0` and a nondegenerate intersection with the future cone, each connected signed section is a full orbit of `exp(tG)`.

The v2 proof by Lorentz reduction is sound:

- timelike normal -> fixed-time circle -> rotation transitive on the signed circle;
- spacelike normal -> fixed-space future hyperbola -> boost transitive on the connected future branch.

The restriction to the signed cone is essential. Paper A's positive-factor image is only the `Y>=0` portion.

The `ab<0,c=0` null-generator intersection remains excluded by the theorem's nondegeneracy hypothesis.

**Status: PASS.**

## 6. Elliptic eigen-coordinate

For `ab>0`,
\[
\zeta=(a+b)X+(a-b)T+2i\sqrt{ab}\,Y
\]
is a left eigen-coordinate with
\[
\zeta(t)=e^{2i\sqrt{ab}\,t}\zeta(0).
\]
On the cut,
\[
|\zeta|^2=c^2.
\]

Direct expansion verifies the identity.

**Status: PASS.**

### Projective normalization

Because a nondegenerate future elliptic cut has `c != 0`, define
\[
\boxed{z=\zeta/c.}
\]
Then
\[
|z|=1,
\]
and `z` is invariant under the simultaneous equation rescaling
\[
(a,b,c)\mapsto(\kappa a,\kappa b,\kappa c).
\]
This separates intrinsic circle phase from the arbitrary scale of the written equation.

## 7. Hyperbolic split eigen-coordinates

For `ab<0`, `r=sqrt(-ab)`,
\[
\eta_\pm=(a+b)X+(a-b)T\pm2rY
\]
obey
\[
\eta_+(t)=e^{2rt}\eta_+(0),\qquad
\eta_-(t)=e^{-2rt}\eta_-(0),
\]
and
\[
\eta_+\eta_-=c^2.
\]

**Status: PASS.**

### Projective normalization

For a nondegenerate hyperbolic cut `c != 0`. Choose the representative orientation `c>0` and set
\[
\boxed{\xi_\pm=\eta_\pm/|c|.}
\]
Then
\[
\xi_+\xi_-=1.
\]
Under positive common rescaling of the oriented equation these are invariant; reversing the equation orientation flips both signs but does not change the geometric cut. Equivalently, using `eta_±/c` gives a fully scale-invariant oriented coordinate pair.

The next version should state which convention is being used rather than leaving equation scale mixed into the split coordinates.

## 8. Power maps

The v2 source correctly retracts the original stronger "canonical power map" claim. For a chosen equation `(a,b,c)`, taking integer powers of `zeta` or `eta_±` and reconstructing against the target level `c^n` gives a valid cone point and exact semiconjugacy
\[
\Psi_n\circ\mathrm{flow}_t
=
\mathrm{flow}_{nt}\circ\Psi_n.
\]

**Status: PASS AS A CHOSEN-EQUATION CONSTRUCTION.**

It is not intrinsic to an unnormalized line because equation rescaling changes the powered coordinate by `kappa^n`. The next version should lead with the normalized projective coordinates and present the chosen-equation power map as a lifted, normalization-dependent construction.

This is a conceptual correction in hierarchy, not a failure of the formulas in v2.

## 9. Parabolic boundary

For `ab=0`, the generator is nilpotent and has no nonzero diagonal eigenvalue. Therefore the elliptic/hyperbolic diagonal eigen-coordinate construction fails.

The v2 source correctly distinguishes this from the existence of other power maps. In particular
\[
(x,y)\mapsto(x^n,y^n)
\]
preserves the cone identity and maps rows/columns to powered rows/columns.

It also correctly warns that literal factor-coordinate translation along a row/column and the Lorentz null-rotation `exp(tG)` are distinct one-parameter notions unless an explicit parameter relation is supplied.

**Status: PASS.**

## 10. Rapidity and constant product

For
\[
s=\frac12\log(x/y),
\]
the `B_X` boost gives `s -> s+phi`, while coordinatewise powers give
\[
s\mapsto ns.
\]
These are distinct operations. The bridge to the area companion through
\[
\cos\theta=\operatorname{sech}s
\]
is consistent.

**Status: PASS.**

## 11. Discriminant-12 interface

The source correctly keeps the arithmetic return separate from the generic cutting-plane generator. For
\[
\lambda=2+\sqrt3,
\]
the factor action
\[
x\mapsto\lambda x,\qquad y\mapsto\lambda^{-1}y
\]
gives
\[
s\mapsto s+\log\lambda.
\]
This is a discrete arithmetic element inside the same real Lorentz geometry, not an identification with generic `G_{a,b}`.

**Status: PASS.**

## Required changes for Paper B v2.1

1. Use `m=(a-b,0,-(a+b))` consistently as the Lorentz normal / metric-dual of the cutting functional; remove the competing `n=(a-b,0,a+b)` terminology.
2. Introduce the normalized generator
   \[
   \widehat G=G/(2\sqrt{|ab|})
   \]
   with eigenvalues `±i` or `±1`, separating projective cutting direction from time normalization.
3. Introduce the elliptic projective coordinate `z=zeta/c`, `|z|=1`.
4. Introduce normalized hyperbolic coordinates, preferably with an explicit oriented-equation convention `c>0`, so `xi_+ xi_-=1`.
5. Reframe power maps as normalized projective dynamics plus a chosen-equation lift; retain the existing warning that the unnormalized powered reconstruction is not canonical under arbitrary equation rescaling.
6. Preserve the signed-cone qualification and the connected-component wording of the orbit theorem.
7. Preserve the parabolic distinction: diagonalization fails, not all power operations.
8. Preserve the separation between Euclidean circle geometry, Lorentz causal geometry, and the later discrete discriminant-12 arithmetic return.

## Dependency consequence

Paper B v2 should remain **ACTIVE / NEEDS AUDIT** until these corrections are incorporated into a new authoritative source and rebuilt. No core theorem has failed. The corrected Paper B should then become the continuous Lorentz foundation between Paper A and the downstream Paper C reconciliation.

Paper C should not be reconciled against the old v2 wording until Paper B v2.1 is established, because Paper C's power-map premise depends directly on this normalization hierarchy.
