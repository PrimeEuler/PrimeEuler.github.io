# Cone Derivation Ledger v13.200 — Parabola–Secant Divisor Chamber

Status: **[D] exact derivation**

This note closes the current area branch by identifying the canonical continuous divisor chamber in the flat circle view.

## 1. [S] Mean-value map and boundary images

Use
\[
X=\frac{x-y}{2},\qquad Y=\sqrt{xy},\qquad T=\frac{x+y}{2}.
\]
Paper A already gives the row/column parabolas at factor level `u=1`:
\[
x=1\iff Y^2=1-2X,
\]
\[
y=1\iff Y^2=1+2X.
\]
The constant-product boundary is
\[
xy=n\iff Y=\sqrt n.
\]
Therefore the positive-factor chamber
\[
\Omega_n:=\{(x,y):x\ge1,\ y\ge1,\ xy\le n\}
\]
transports exactly to the region bounded by the two `u=1` parabolas and the secant `Y=sqrt(n)`.

The two parabolas meet at
\[
(X,Y)=(0,1),
\]
and the secant endpoints are
\[
(X,Y)=\left(\pm\frac{n-1}{2},\sqrt n\right).
\]

## 2. [D] Raw flat-circle area

For fixed `Y`, solve the two parabolas:
\[
X_L(Y)=\frac{1-Y^2}{2},\qquad
X_R(Y)=\frac{Y^2-1}{2}.
\]
Hence the horizontal width is
\[
X_R-X_L=Y^2-1.
\]
Integrating from `Y=1` to `Y=sqrt(n)` gives
\[
\boxed{
P_n
=\int_1^{\sqrt n}(Y^2-1)\,dY
=\frac{n^{3/2}-3\sqrt n+2}{3}.}
\]
This is the raw Euclidean area of the parabola–secant chamber in the flat `(X,Y)` view.

## 3. [D] Factor-plane area of the same chamber

In factor coordinates,
\[
\Omega_n=\left\{1\le x\le n,\ 1\le y\le\frac nx\right\}.
\]
Therefore
\[
\boxed{
\operatorname{Area}_{xy}(\Omega_n)
=\int_1^n\left(\frac nx-1\right)dx
=n\log n-n+1.}
\]

So the exact geometric transport is
\[
\boxed{
 n\log n-n+1
\quad\xrightarrow{F}\quad
\frac{n^{3/2}-3\sqrt n+2}{3}.}
\]
The arrow denotes the same region under different area measures, not equality of the numbers.

## 4. [D] Exact angular recovery

From v13.199 / `Note_AreaDistortion_AMGM_Cone_v1.1.tex`,
\[
 dx\,dy=2\cos\theta\,dX\,dY
 =2\operatorname{sech}s\,dX\,dY.
\]
Therefore
\[
\boxed{
 n\log n-n+1
 =\iint_{F(\Omega_n)}2\cos\theta\,dX\,dY.}
\]
This is the exact inverse area rule for the chamber. No constant renormalization is introduced.

## 5. [D] Why this chamber is canonical

The three bounding curves are forced by the positive divisor geometry:

- `x=1` is the first positive row;
- `y=1` is the first positive column;
- `xy=n` is the continuous divisor boundary.

Their flat images are exactly the two `u=1` parabolas and the secant `Y=sqrt(n)`. Thus this is the natural continuous positive-factor divisor chamber in the circle view, not an ad hoc region chosen to fit `D(n)`.

## 6. [N-cert] n=11

For `n=11`,
\[
P_{11}=\frac{8\sqrt{11}+2}{3}\approx9.51099944095,
\]
while
\[
11\log11-10\approx16.37684800078.
\]
The secant endpoints are
\[
(\pm5,\sqrt{11}).
\]
The discrete count remains
\[
D(11)=29.
\]
No equality between the continuous chamber areas and `D(11)` is claimed.

## 7. [Audit] Publication guardrails

Do not claim:

1. `P_n` approximates `D(n)` asymptotically merely because both arise from the same divisor boundary.
2. The raw circle area and factor-plane area should be numerically equal.
3. The `u=1` parabolas are fitted envelopes; they are exact images of `x=1` and `y=1`.
4. The weighted measure `2 cos(theta) dX dY` is optional normalization; it is the exact pullback of ordinary factor-plane area.

Publication-safe summary:

> The positive-factor continuous divisor region bounded by `x=1`, `y=1`, and `xy=n` maps exactly to the flat circle chamber bounded by the row-1 parabola, column-1 parabola, and secant `Y=sqrt(n)`. Its raw circle area is `(n^(3/2)-3 sqrt(n)+2)/3`, while the canonical angular weight `2 cos(theta)` recovers exactly its factor-plane area `n log n-n+1`.

## 8. Area-branch stopping point

This result supplies the final structural piece needed for the current area branch:

- exact local Jacobian and cone surface factor;
- exact triangle/half-disk and hyperbola/secant transport;
- exact rapidity-to-angle map;
- exact inverse angular area measure;
- exact discrete staircase push-forward;
- canonical row-1/column-1/secant divisor chamber.

Absent a new theorem-level connection, further attempts to tune circle-area magnitudes toward `D(n)` should be deferred. The main project should return to Paper A citation cleanup and then the Paper B audit.
