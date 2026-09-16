# Cone Derivation Ledger v13.525 — Figure-Source Sign Audit and Carrier Separation

**Status:** exact source-code/geometric audit. This entry refines v13.517–v13.524 by comparing the finite signed carrier directly with the source of `figures/mod12_v4_cone_triple.png`. The cone's signed geometry is native, but the figure's visible sign symmetries must not be identified automatically with the U(24) sign bit `c`.

## 1. Source inspected

The generating script is

`figures/discriminant12_mod12_v4_cone_triple.py`.

Its stated shell data are, for
\[
r\in U(12)=\{1,5,7,11\},
\]
\[
T=\frac{r+1}{2}=R,\qquad |X|=\frac{r-1}{2}=c_r,\qquad Y^2=r.
\]
The plotted values are
\[
(r,c_r,R)=(1,0,1),(5,2,3),(7,3,4),(11,5,6).
\]
For each nonzero `c_r`, the script explicitly plots both
\[
X=+c_r\quad\text{and}\quad X=-c_r,
\]
and for each such X it plots both
\[
Y=+\sqrt r\quad\text{and}\quad Y=-\sqrt r.
\]
Thus signed structure is visibly native to the cone construction.

## 2. Exact cone equation used by the script

For a fixed plotted shell,
\[
T=R=\frac{r+1}{2},\qquad X=\pm\frac{r-1}{2},\qquad Y=\pm\sqrt r.
\]
Therefore
\[
T^2-X^2
=\frac{(r+1)^2-(r-1)^2}{4}
=r
=Y^2.
\]
Hence every marked endpoint lies on
\[
\boxed{T^2=X^2+Y^2.}
\]
This is exactly the upper circular cone plotted in panel (c), with
\[
T\ge0.
\]

## 3. Two visible native sign involutions

The source realizes two independent geometric reflections:
\[
\boxed{R_X(X,Y,T)=(-X,Y,T),}
\]
\[
\boxed{R_Y(X,Y,T)=(X,-Y,T).}
\]
They commute and preserve the cone equation. Their product is
\[
R_XR_Y(X,Y,T)=(-X,-Y,T).
\]
Thus each generic shell point has a visible Klein-four sign orbit
\[
\boxed{
\{(X,Y,T),(-X,Y,T),(X,-Y,T),(-X,-Y,T)\}.
}
\]
For r=1 the X-reflection degenerates at X=0, but the symmetry remains an exact symmetry of the ambient cone.

This gives a literal geometric V4 of cone reflections:
\[
\boxed{\langle R_X,R_Y\rangle\cong C_2\times C_2.}
\]

## 4. Meaning of X reflection

The factor-line coordinates for an ordered factor pair `(u,v)` are
\[
X=\frac{u-v}{2},\qquad T=\frac{u+v}{2},\qquad Y^2=uv.
\]
For the plotted pair `(r,1)`,
\[
(X,T)=\left(\frac{r-1}{2},\frac{r+1}{2}\right).
\]
Swapping the factors,
\[
(r,1)\longmapsto(1,r),
\]
gives
\[
X\longmapsto-X,\qquad T\longmapsto T,
\]
while `uv=r` is unchanged. Therefore
\[
\boxed{R_X=\text{ordered-factor swap}.}
\]
This is an exact geometric interpretation already present in the figure.

## 5. Meaning of Y reflection

Since the shell condition is
\[
Y^2=uv=r,
\]
the two square-root branches are
\[
Y=\pm\sqrt r.
\]
Thus
\[
\boxed{R_Y=\text{square-root branch reversal}.}
\]
Again this is directly visible in the source: both `+Y` and `-Y` branches are plotted.

## 6. Crucial separation from the U(24) sign bit

The signed finite carrier introduced in v13.515/v13.517 is
\[
G=V\times\mathbf F_2\cong U(24),
\]
with the extra bit represented arithmetically by
\[
r\mapsto-r\pmod{24}.
\]
On the affine factor-line coordinates satisfying
\[
T-X=1,\qquad T+X=r,
\]
that arithmetic sign operation was organized as
\[
\boxed{S_{24}(X,T)=(-T,-X).}
\]
This operation changes
\[
T^2-X^2=r
\]
to
\[
T'^2-X'^2=-r.
\]

However, the actual `mod12_v4_cone_triple` source plots only the positive shells
\[
r=1,5,7,11
\]
on the upper cone `T>=0`. It does **not** explicitly plot the negative-r U(24) states or the transformation `(X,T)->(-T,-X)`.

Therefore the correct hierarchy is:

\[
\boxed{
\text{native signed cone geometry is real and explicit,}
\quad
\text{but its visible }R_X,R_Y\text{ signs are not automatically }S_{24}.
}
\]

This does not undo the signed-carrier algebra of v13.517–v13.524. It prevents a pointwise geometric identification that the figure source itself does not establish.

## 7. Three distinct involutions now in play

We must keep separate:

1. **Factor-swap reflection**
\[
R_X:(X,Y,T)\mapsto(-X,Y,T).
\]

2. **Square-root branch reflection**
\[
R_Y:(X,Y,T)\mapsto(X,-Y,T).
\]

3. **U(24) arithmetic sign bit**
\[
S_{24}:(v,c)\mapsto(v,c+1),
\]
represented in the affine signed-factor organization by
\[
(X,T)\mapsto(-T,-X).
\]

The first two preserve a fixed positive shell `r`; the third changes the signed arithmetic label `r` to `-r`.

## 8. Relation to the QR deck involution remains exact

On the finite carrier,
\[
S_{24}=001,
\qquad
T_{11}=110,
\qquad
K=111,
\]
with
\[
K=S_{24}+T_{11}^{\uparrow}.
\]
The exact identities
\[
PS_{24}=T_{11}P,
\qquad
PK=P
\]
remain unchanged.

What is refined is only the geometric interpretation: `S_{24}` should not be called the same operation as the figure's visible `X->-X` or `Y->-Y` reflection without an additional map.

## 9. A useful new structural observation

The figure itself already supplies a geometric Klein four
\[
V_{\mathrm{geom}}=\{1,R_X,R_Y,R_XR_Y\}\cong V_4,
\]
while the residue labels supply the arithmetic Klein four
\[
V_{\mathrm{arith}}=U(12)=\{1,5,7,11\}\cong V_4.
\]
These are two different V4 structures:

- `V_geom` acts **within each cone shell** by sign/reflection symmetries;
- `V_arith` indexes the four distinguished mod-12 shells.

The existing Hadamard/A3/S4 construction is built from `V_arith`, not from `V_geom`.

Thus the source reveals a natural next exact question:
\[
\boxed{
\text{How, if at all, does }V_{\mathrm{geom}}\text{ act on or intertwine with }V_{\mathrm{arith}}?
}
\]
No identification is asserted here.

## 10. Guardrails

1. The cone is intrinsically signed; this audit strengthens that point by locating two explicit source-level reflections.
2. `R_X`, `R_Y`, `S_{24}`, and the QR deck involution `K` are distinct unless an explicit intertwiner is proved.
3. The A3 tetrahedron comes from the arithmetic shell-label V4.
4. v13.522/v13.524 finite identities remain exact.
5. No Pell-to-cone-sign, Pell-to-QR, or Suzuki spectral implication is asserted.