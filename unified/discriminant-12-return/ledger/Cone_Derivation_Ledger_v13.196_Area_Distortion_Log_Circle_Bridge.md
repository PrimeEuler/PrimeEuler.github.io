# Cone Derivation Ledger v13.196 — Area Distortion and Log–Circle Bridge

Date: 2026-09-03

Status labels: [S] source-established, [D] exact derived, [I] interpretation, [O] open, [Audit] limitation/correction.

## 1. Source checkpoint

[S] Paper A uses
\[
X=\frac{x-y}{2},\qquad Y=\sqrt{xy},\qquad T=\frac{x+y}{2},
\]
with
\[
X^2+Y^2=T^2,\qquad x=T+X,\qquad y=T-X.
\]

[S] The earlier `Note_SemiclassicalArea.tex` already derived the induced cone-surface element
\[
dA_{\rm cone}=\frac{T}{\sqrt2\,Y}\,dx\,dy.
\]
The LQG comparison in that note is not needed for the present geometry.

[Audit] Preserve `Note_SemiclassicalArea.tex` as a historical/research note. The new foundation source is
`foundations/Note_AreaDistortion_AMGM_Cone_v1.0.tex`.

## 2. Flat factor-plane to circle-view Jacobian

[D] Direct differentiation gives
\[
\left|\frac{\partial(X,Y)}{\partial(x,y)}\right|
=\frac14\left(\sqrt{\frac xy}+\sqrt{\frac yx}\right)
=\frac{x+y}{4\sqrt{xy}}
=\frac{T}{2Y}.
\]
Hence
\[
\boxed{dX\,dY=\frac{T}{2Y}\,dx\,dy.}
\]

[D] On the diagonal `x=y`, the flat Jacobian is `1/2`; it diverges toward either factor axis.

[D] Since the cone is the graph `T=sqrt(X^2+Y^2)`,
\[
\boxed{dA_{\rm cone}=\sqrt2\,dX\,dY.}
\]
Therefore
\[
\boxed{dA_{\rm cone}=\frac{T}{\sqrt2Y}\,dx\,dy.}
\]
This reconciles the old induced-area calculation with the flat circle-view distortion.

## 3. Complete anti-diagonal triangle

Let
\[
\Delta_S=\{x\ge0,y\ge0,x+y\le S\}.
\]

[D] Since `T=(x+y)/2`, the image is exactly the upper half-disk of radius `S/2`.

[D]
\[
\operatorname{Area}(\Delta_S)=\frac{S^2}{2},
\qquad
\operatorname{Area}(F(\Delta_S))=\frac{\pi S^2}{8}.
\]
Thus the complete-shell average distortion is
\[
\boxed{\frac{\operatorname{Area}(F(\Delta_S))}{\operatorname{Area}(\Delta_S)}=\frac\pi4.}
\]

[Audit] This global `pi/4` ratio does **not** imply local area preservation or a constant Jacobian.

## 4. Hyperbola-to-secant shell partition

Fix `n>1` and the shell `S=n+1`.

[D]
\[
xy=n\quad\longmapsto\quad Y=\sqrt n.
\]
The extremal points `(1,n)` and `(n,1)` map to
\[
X=\mp\frac{n-1}{2},\qquad Y=\sqrt n,
\]
inside the half-disk of radius
\[
R=\frac{n+1}{2}.
\]

[D] The endpoint triangle satisfies
\[
\boxed{\left(\frac{n-1}{2}\right)^2+n=\left(\frac{n+1}{2}\right)^2.}
\]

Let `B_n` be the part of the shell triangle satisfying `xy<=n`, and `C_n` its complement.

[D]
\[
\operatorname{Area}(B_n)=n\log n+n+1.
\]
Reason: the central under-hyperbola region contributes `n log n`; the two shell wings contribute exactly `n+1`.

[D]
\[
\operatorname{Area}(C_n)=\frac{n^2-1}{2}-n\log n.
\]

[Audit] The classical `n log n` region is not the whole shell portion below the hyperbola. Any triangle-to-half-disk comparison must account for the `n+1` wing area.

## 5. Circular cap and below-secant area

Define
\[
\theta_n=\arccos\left(\frac{2\sqrt n}{n+1}\right).
\]
Then
\[
\sin\theta_n=\frac{n-1}{n+1},
\qquad
\tan\theta_n=\frac{n-1}{2\sqrt n}.
\]

[D] The upper circular cap above `Y=sqrt(n)` is
\[
\boxed{
A_{\rm cap}^{\circ}(n)
=\frac{(n+1)^2}{4}\theta_n
-\frac{(n-1)\sqrt n}{2}.}
\]

[D] The complementary portion below the secant is
\[
\boxed{
A_{\rm below}^{\circ}(n)
=\frac{\pi(n+1)^2}{8}-A_{\rm cap}^{\circ}(n).}
\]

[D] Set correspondence under the exact map:
\[
B_n\longmapsto \{Y\le\sqrt n\}\cap H_{n+1},
\qquad
C_n\longmapsto \{Y\ge\sqrt n\}\cap H_{n+1}.
\]

[Audit] The corresponding numerical areas are not equal; they are related by the nonuniform Jacobian `T/(2Y)`.

## 6. Literal `n log n` region

Define
\[
E_n=\left\{1\le x\le n,\ 0\le y\le\frac n x\right\}.
\]

[D]
\[
\operatorname{Area}(E_n)=n\log n.
\]

[D] Its exact flat circle-view image area is
\[
\boxed{\operatorname{Area}(F(E_n))=\frac23(n-1)\sqrt n.}
\]
This follows from integrating the Jacobian:
\[
\int_1^n\int_0^{n/x}\frac{x+y}{4\sqrt{xy}}\,dy\,dx.
\]

## 7. Product-ratio coordinates and the exact logarithmic/circular bridge

Define
\[
\rho=\sqrt{xy},
\qquad
s=\frac12\log\frac{x}{y}.
\]
Then
\[
x=\rho e^s,\qquad y=\rho e^{-s}.
\]

[D]
\[
\boxed{X=\rho\sinh s,\qquad Y=\rho,\qquad T=\rho\cosh s.}
\]

Let ordinary circle angle `theta` be measured from the positive `Y` axis:
\[
X=T\sin\theta,\qquad Y=T\cos\theta.
\]
Then
\[
\boxed{
\sin\theta=\tanh s,
\quad
\cos\theta=\operatorname{sech}s,
\quad
\tan\theta=\sinh s.}
\]

[D] Differentiation gives
\[
\boxed{d\theta=\operatorname{sech}s\,ds.}
\]
Hence
\[
\boxed{\theta(s)=\int_0^s\operatorname{sech}t\,dt}
\]
and
\[
\boxed{\int_0^\infty\operatorname{sech}t\,dt=\frac\pi2.}
\]

[D] This is an exact logarithmic/exponential-to-circular compactification: unbounded rapidity `s` maps to bounded angle `theta in (-pi/2,pi/2)`.

[I] This provides a precise mathematical version of the observed `log/e` versus `pi` relation in the triangle/circle views. It is not an identity equating `e` and `pi`; it is a change of variables in which exponential factor ratio becomes circular angle.

## 8. Area distortion in rapidity coordinates

[D]
\[
dx\,dy=2\rho\,d\rho\,ds,
\]
while
\[
dX\,dY=\rho\cosh s\,d\rho\,ds.
\]
Therefore
\[
\boxed{\frac{dX\,dY}{dx\,dy}=\frac{\cosh s}{2}.}
\]

[D] The same hyperbolic function pair controls both transformations:
- local area stretching: `cosh(s)/2`;
- angular compression: `dtheta/ds=sech(s)`.

This reciprocal pairing is a central structural result of the area audit.

## 9. n=11 check

For `n=11`:
\[
R=6,\qquad a=5,\qquad h=\sqrt{11}.
\]

[N-cert]
\[
A_{\rm half}=18\pi\approx56.5487,
\]
\[
A_{\rm cap}^{\circ}(11)
=36\arccos(\sqrt{11}/6)-5\sqrt{11}
\approx18.88086425,
\]
\[
A_{\rm below}^{\circ}(11)\approx37.66780352.
\]

[I] The proximity of `A_below^circ(11)` to the discrete complement `A_11=37` is an observation only. No discrete push-forward theorem has yet been proved.

## 10. Open next step

[O] Derive the exact push-forward of the divisor staircase
\[
D(n)=\#\{(x,y)\in\mathbb Z_{\ge1}^2:xy\le n\}
\]
and the triangular complement under the same area map. In particular, determine whether the discrete quantities `D(n)`, `A_n`, `nH_n`, and `T_n` admit canonical weighted circle-view analogues and quantify their errors against the continuous formulas above.

## Publication guardrails added

1. Do not equate raw triangle areas with raw circle areas; always include the Jacobian.
2. Do not identify `n log n` with the entire shell-below-hyperbola area; the latter is `n log n+n+1`.
3. Do not infer a discrete theorem from the numerical closeness `A_below^circ(11)≈37.6678` and `A_11=37`.
4. Do not call the `log/e`–`pi` bridge an identity between constants. Publication-safe statement: logarithmic rapidity is compactified into ordinary angle by `dtheta=sech(s) ds`, with `int_0^infty sech(s) ds=pi/2`.
5. Keep the LQG interpretation outside the geometry foundation paper; the old semiclassical note remains a separate research note.
