# Cone Derivation Ledger v13.197 — Discrete Staircase Push-Forward

Status: **[D] exact derivation with [N-cert] numerical checks**

This note extends the continuous area-distortion result of `Note_AreaDistortion_AMGM_Cone_v1.0.tex` to the discrete column staircases associated with
\[
T_n=\frac{n(n+1)}2,\qquad nH_n,\qquad D(n)=\sum_{k=1}^n\left\lfloor\frac nk\right\rfloor,\qquad A_n=T_n-D(n).
\]
The purpose is to define the exact flat-circle-view area carried by each staircase under
\[
F(x,y)=\left(\frac{x-y}{2},\sqrt{xy}\right),
\]
whose flat Jacobian is
\[
J(x,y)=\left|\frac{\partial(X,Y)}{\partial(x,y)}\right|
=\frac{x+y}{4\sqrt{xy}}
=\frac14\left(\sqrt{\frac xy}+\sqrt{\frac yx}\right).
\]

## 1. [D] A universal column-strip weight

For an integer column index \(k\ge1\) and height \(h\ge0\), define
\[
R_k(h)=[k-1,k]\times[0,h].
\]
Its ordinary factor-plane area is simply \(h\). Its flat circle-view image area is
\[
W_k(h):=\operatorname{Area}(F(R_k(h)))
=\int_{k-1}^{k}\int_0^h J(x,y)\,dy\,dx.
\]
Write
\[
\Delta_{3/2}(k):=k^{3/2}-(k-1)^{3/2},\qquad
\Delta_{1/2}(k):=\sqrt{k}-\sqrt{k-1}.
\]
Direct integration gives
\[
\boxed{
W_k(h)=\frac13\left[
\sqrt h\,\Delta_{3/2}(k)
+h^{3/2}\,\Delta_{1/2}(k)
\right].}
\]
This formula remains finite for \(k=1\), even though the local Jacobian diverges on the axes; the singularity is integrable.

The corresponding induced cone-surface area is simply
\[
\boxed{W_k^{\rm cone}(h)=\sqrt2\,W_k(h).}
\]

## 2. [D] The four column staircases

Define the following exact factor-plane regions using the same width-one column partition \([k-1,k]\), \(1\le k\le n\).

### Triangular staircase
\[
\mathcal T_n:=\bigcup_{k=1}^n R_k(n+1-k).
\]
Hence
\[
\operatorname{Area}(\mathcal T_n)
=\sum_{k=1}^n(n+1-k)
=T_n.
\]
Its flat push-forward area is
\[
\boxed{
\mathcal W_T(n):=\sum_{k=1}^n W_k(n+1-k).}
\]

### Harmonic staircase
\[
\mathcal H_n:=\bigcup_{k=1}^n R_k(n/k).
\]
Therefore
\[
\operatorname{Area}(\mathcal H_n)
=\sum_{k=1}^n\frac nk
=nH_n,
\]
and
\[
\boxed{
\mathcal W_H(n):=\sum_{k=1}^n W_k(n/k).}
\]

### Divisor staircase
\[
\mathcal D_n:=\bigcup_{k=1}^n R_k\!\left(\left\lfloor\frac nk\right\rfloor\right).
\]
Hence
\[
\operatorname{Area}(\mathcal D_n)
=\sum_{k=1}^n\left\lfloor\frac nk\right\rfloor
=D(n),
\]
and the exact flat push-forward is
\[
\boxed{
\mathcal W_D(n):=\sum_{k=1}^n
W_k\!\left(\left\lfloor\frac nk\right\rfloor\right).}
\]

### Complementary staircase
For \(1\le k\le n\),
\[
\frac nk\le n+1-k,
\]
because
\[
k(n+1-k)-n=(k-1)(n-k)\ge0.
\]
Thus \(\mathcal D_n\subseteq\mathcal T_n\), and
\[
\mathcal A_n:=\mathcal T_n\setminus\mathcal D_n
\]
has factor-plane area
\[
\operatorname{Area}(\mathcal A_n)=T_n-D(n)=A_n.
\]
Its exact flat push-forward is therefore
\[
\boxed{
\mathcal W_A(n)=\mathcal W_T(n)-\mathcal W_D(n).}
\]

## 3. [D] The harmonic-floor discrepancy also pushes forward exactly

Because
\[
\left\lfloor\frac nk\right\rfloor\le\frac nk,
\]
we likewise have \(\mathcal D_n\subseteq\mathcal H_n\). The ordinary factor-plane discrepancy is
\[
\operatorname{Area}(\mathcal H_n\setminus\mathcal D_n)
=nH_n-D(n)
=\sum_{k=1}^n\left\{\frac nk\right\}.
\]
Its exact flat-circle push-forward is
\[
\boxed{
\mathcal W_{H-D}(n)
=\mathcal W_H(n)-\mathcal W_D(n).}
\]
This is the exact geometric image of the total fractional-part error between the harmonic staircase and the divisor staircase.

## 4. [D] Relation to the continuous hyperbola calculation

The continuous region
\[
E_n=\{1\le x\le n,\ 0\le y\le n/x\}
\]
has area \(n\log n\) and, from v13.196,
\[
\operatorname{Area}(F(E_n))=\frac23(n-1)\sqrt n.
\]
This is **not** the same region as \(\mathcal H_n\): \(\mathcal H_n\) is the width-one right-endpoint staircase whose column heights are \(n/k\). Thus
\[
n\log n\quad\text{and}\quad nH_n
\]
are two different continuous/staircase approximants to the same hyperbolic boundary, and their push-forwards must be kept distinct.

Likewise, the raw circular cap and below-secant areas of v13.196 are the images of the **continuous shell partition**. They are not equal to \(\mathcal W_D(n)\), \(\mathcal W_A(n)\), \(\mathcal W_H(n)\), or \(\mathcal W_T(n)\), because the latter are images of staircase regions with different boundaries.

## 5. [N-cert] The \(n=11\) values

For \(n=11\),
\[
T_{11}=66,\qquad D(11)=29,\qquad A_{11}=37,
\]
and
\[
H_{11}=\frac{83711}{27720},\qquad
11H_{11}\approx33.2186507936508.
\]
Evaluating the exact sums above gives
\[
\boxed{\mathcal W_D(11)\approx30.1810563510192,}
\]
\[
\boxed{\mathcal W_H(11)\approx32.7507152319907,}
\]
\[
\boxed{\mathcal W_T(11)\approx51.2635200516399,}
\]
\[
\boxed{\mathcal W_A(11)\approx21.0824637006206,}
\]
and
\[
\boxed{\mathcal W_H(11)-\mathcal W_D(11)
\approx2.56965888097146.}
\]
The corresponding average flat distortion factors are
\[
\frac{\mathcal W_T(11)}{T_{11}}\approx0.7767200008,
\]
\[
\frac{\mathcal W_H(11)}{11H_{11}}\approx0.9859134688,
\]
\[
\frac{\mathcal W_D(11)}{D(11)}\approx1.0407260811,
\]
\[
\frac{\mathcal W_A(11)}{A_{11}}\approx0.5697963162.
\]
The first is already close to the continuum complete-triangle mean factor \(\pi/4\approx0.785398\), as expected from a staircase approximation to a straight anti-diagonal boundary. This numerical closeness is an observation, not yet an asymptotic theorem in this ledger entry.

For comparison, the continuous \(x+y\le12\) half-disk has raw flat area
\[
18\pi\approx56.5486677646,
\]
with secant partition
\[
A_{\rm cap}^{\circ}(11)\approx18.8808642484,
\qquad
A_{\rm below}^{\circ}(11)\approx37.6678035162.
\]
These are deliberately listed separately from the staircase push-forward values.

## 6. [I] What this gives conceptually

The four classical quantities now live on a single exact column carrier:
\[
T_n\leftrightarrow\mathcal T_n,
\qquad
nH_n\leftrightarrow\mathcal H_n,
\qquad
D(n)\leftrightarrow\mathcal D_n,
\qquad
A_n\leftrightarrow\mathcal A_n.
\]
Applying the same Jacobian to each produces
\[
\mathcal W_T(n),\quad
\mathcal W_H(n),\quad
\mathcal W_D(n),\quad
\mathcal W_A(n),
\]
so the triangle-to-circle comparison is now an exact transformation of regions rather than a comparison of unrelated scalar values.

The next natural theorem target is asymptotic: determine the leading behavior of each \(\mathcal W_*(n)\), and in particular quantify
\[
\mathcal W_T(n)-\frac\pi4T_n
\]
and the push-forward divisor error
\[
\mathcal W_D(n)-\mathcal W_H(n).
\]

## 7. [Audit] Indexing guardrail

The column convention above is chosen because it realizes the scalar identities exactly as Euclidean areas. In particular, \(\mathcal T_n\) has area \(T_n\) by construction. This staircase must **not** be silently identified with the continuous triangle \(x+y\le n+1\), whose Euclidean area is \((n+1)^2/2\), nor with a visual cell-count convention in Paper A until the boundary/indexing convention is written explicitly. The continuous and discrete shell carriers are related approximations, not identical sets.

## Publication-safe summary

**[D]** For every width-one column \([k-1,k]\) and height \(h\), the flat-circle-view image area is
\[
W_k(h)=\frac13\left[
\sqrt h\,(k^{3/2}-(k-1)^{3/2})
+h^{3/2}(\sqrt k-\sqrt{k-1})
\right].
\]
Therefore the exact push-forwards of \(T_n\), \(nH_n\), \(D(n)\), and \(A_n\) are obtained by substituting the respective column heights \(n+1-k\), \(n/k\), \(\lfloor n/k\rfloor\), and by taking the triangular-minus-divisor difference. No equality with raw circular cap areas is asserted.