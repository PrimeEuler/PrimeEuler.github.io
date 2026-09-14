# Cone Derivation Ledger v13.469 — χ12 Pell Time Orientation and Affine Frame Selection

Date: 2026-09-14

Status labels: **[D]** exact derived, **[I]** interpretation, **[Audit]** guardrail.

## 0. Synchronization [Audit]

The live ledger was checked before this write. The newest numbered entry was `v13.468` (`Oriented Pell Phase Selects the Affine Frame`), so `v13.469` was free.

This checkpoint makes the χ12 time-orientation law explicit directly from the Pell correspondence and then shows exactly why the positive Pell orientation selects the affine trivialization `b=w` rather than `b=w^2`.

## 1. Pell generator and its inverse [D]

Let

\[
F=\mathbf Q(\sqrt3),\qquad
\lambda=2+\sqrt3.
\]

Since

\[
(2+\sqrt3)(2-\sqrt3)=1,
\]

we have

\[
\boxed{\lambda^{-1}=2-\sqrt3.}
\]

The Pell orbit is encoded by

\[
\lambda^n=x_n+y_n\sqrt3,
\]

with

\[
x_n=\cosh(nR_{12}),\qquad
y_n=\frac{\sinh(nR_{12})}{\sqrt3},\qquad
R_{12}=\log(2+\sqrt3)>0.
\]

Thus the integer exponent `n` is the discrete Pell-time coordinate and `R12` is the positive fundamental rapidity.

## 2. χ12 acts by Pell-time reversal [D]

For

\[
r\in U(12)=\{1,5,7,11\},
\]

the cyclotomic Galois action on the real quadratic generator is

\[
\boxed{\sigma_r(\sqrt3)=\chi_{12}(r)\sqrt3.}
\]

Therefore

\[
\sigma_r(\lambda)
=
2+\chi_{12}(r)\sqrt3.
\]

If \(\chi_{12}(r)=+1\), this is \(\lambda\). If \(\chi_{12}(r)=-1\), this is \(2-\sqrt3=\lambda^{-1}\). Hence

\[
\boxed{
\sigma_r(\lambda)=\lambda^{\chi_{12}(r)}.
}
\]

More generally,

\[
\boxed{
\sigma_r(\lambda^n)=\lambda^{\chi_{12}(r)n}.
}
\]

Equivalently, if

\[
\lambda^n=x_n+y_n\sqrt3,
\]

then

\[
\sigma_r(\lambda^n)
=x_n+\chi_{12}(r)y_n\sqrt3
=
\lambda^{\chi_{12}(r)n}.
\]

Thus

\[
\boxed{n\mapsto\chi_{12}(r)n}
\]

is the exact Galois action on discrete Pell time.

At the rapidity level,

\[
\boxed{R_{12}\mapsto\chi_{12}(r)R_{12}.}
\]

So `χ12` is precisely the Pell time-orientation character.

The table is

\[
\begin{array}{c|cccc}
r&1&5&7&11\\\hline
\chi_{12}(r)&+1&-1&-1&+1
\end{array}
\]

and therefore `r=5,7` reverse Pell time, while `r=1,11` preserve it.

## 3. Prime-3 tangent phase of λ [D]

At the ramified prime three,

\[
\mathcal O_F/3\mathcal O_F
\cong
\mathbf F_3[\epsilon]/(\epsilon^2),
\qquad
\epsilon=\sqrt3\bmod3.
\]

For a local unit

\[
a+b\epsilon,
\]

the projective tangent coordinate from `v13.441` is

\[
\boxed{
j([a+b\epsilon])=\frac{2b}{a}\in\mathbf F_3.
}
\]

Now

\[
\lambda=2+\epsilon=-1+\epsilon.
\]

Taking \(a=2\), \(b=1\),

\[
j([\lambda])
=
\frac{2}{2}
=1.
\]

Hence

\[
\boxed{j([\lambda])=+1.}
\]

For the inverse,

\[
\lambda^{-1}=2-\epsilon,
\]

so \(a=2\), \(b=-1=2\) in \(\mathbf F_3\), and

\[
j([\lambda^{-1}])
=
\frac{2\cdot2}{2}
=2
=-1.
\]

Therefore

\[
\boxed{j([\lambda^{-1}])=-1.}
\]

Combining with the χ12 law gives

\[
\boxed{
j([\sigma_r(\lambda)])=\chi_{12}(r)\in\{\pm1\}\subset\mathbf F_3.}
\]

Thus the χ12 sign survives exactly as the orientation of the three-state Pell phase.

## 4. Transport to the prime-2 three-state phase [D]

The established two-prime phase intertwiner is

\[
\Psi:\mathbf F_3\longrightarrow\mathbf F_4^\times,
\qquad
\boxed{\Psi(j)=w^j,}
\]

where

\[
w^2+w+1=0,
\qquad
w^3=1.
\]

Therefore

\[
\Psi(+1)=w,
\qquad
\Psi(-1)=w^{-1}=w^2.
\]

Hence

\[
\boxed{
\Psi(j([\sigma_r(\lambda)]))
=
w^{\chi_{12}(r)}.
}
\]

Explicitly,

\[
\chi_{12}(r)=+1
\Longrightarrow
w,
\]

while

\[
\chi_{12}(r)=-1
\Longrightarrow
w^2.
\]

Thus the two Pell time orientations map exactly to the two conjugate nontrivial elements of \(\mathbf F_4^\times\).

## 5. Affine-frame trivialization equation [D]

From `v13.466`, the mod-two crossed cocycle is

\[
c(\tau)=1,
\]

for Frobenius

\[
\tau(t)=t^2.
\]

A coboundary trivialization is an element \(b\in\mathbf F_4\) satisfying

\[
\delta b(\tau)
=b+\tau(b)
=b+b^2
=1.
\]

Therefore the frame equation is

\[
\boxed{b+b^2=1.}
\]

Since

\[
w^2+w+1=0,
\]

both

\[
\boxed{b=w}
\]

and

\[
\boxed{b=w^2}
\]

solve the equation, and these are the only two solutions.

Thus the affine-frame torsor is

\[
\boxed{\{w,w^2\}.}
\]

## 6. χ12-equivariant frame selection [D]

Sections 3 and 4 show that the oriented Pell generator determines

\[
[\lambda]\mapsto +1\mapsto w,
\]

while the reversed Pell generator determines

\[
[\lambda^{-1}]\mapsto -1\mapsto w^2.
\]

Hence there is an exact orientation-equivariant correspondence

\[
\boxed{
\lambda\longleftrightarrow w,
\qquad
\lambda^{-1}\longleftrightarrow w^2.
}
\]

Equivalently,

\[
\boxed{
b_r=w^{\chi_{12}(r)}.}
\]

The action of an element with \(\chi_{12}(r)=-1\) exchanges the two affine frames,

\[
w\leftrightarrow w^2,
\]

exactly as it exchanges

\[
\lambda\leftrightarrow\lambda^{-1}.
\]

Thus the frame torsor and the Pell-orientation torsor are χ12-equivariantly identified.

## 7. Why the positive Pell orientation selects b=w [D/I]

The standard real embedding has

\[
\sqrt3>0,
\]

and therefore

\[
\lambda=2+\sqrt3>1.
\]

This is the positive fundamental Pell unit and defines the positive rapidity

\[
R_{12}=\log\lambda>0.
\]

Choosing this orientation means choosing the generator `+1` of the mod-three phase:

\[
\lambda\mapsto j=+1.
\]

Under \(\Psi(j)=w^j\), this gives

\[
\boxed{b=w.}
\]

By contrast, choosing the reversed Pell orientation

\[
\lambda^{-1}=2-\sqrt3<1
\]

means

\[
j=-1,
\]

and therefore

\[
\boxed{b=w^2.}
\]

Hence

\[
\boxed{
R_{12}>0
\Longleftrightarrow
\lambda=2+\sqrt3
\Longleftrightarrow
j=+1
\Longleftrightarrow
b=w.
}
\]

Likewise,

\[
\boxed{
R_{12}<0
\Longleftrightarrow
\lambda^{-1}=2-\sqrt3
\Longleftrightarrow
j=-1
\Longleftrightarrow
b=w^2.
}
\]

This is the precise sense in which the positive Pell time orientation selects the affine frame `b=w` rather than `b=w^2`.

## 8. Affine involution in the selected frame [D]

The cocycle-twisted involution is

\[
F'(t)=t^2+1.
\]

For a trivializing frame \(b\),

\[
F'=T_bFT_b^{-1},
\]

where

\[
F(t)=t^2,
\qquad
T_b(t)=t+b.
\]

With the positive Pell orientation, \(b=w\), so

\[
\boxed{
F'=T_wFT_w^{-1}.
}
\]

With reversed Pell orientation,

\[
\boxed{
F'=T_{w^2}FT_{w^2}^{-1}.
}
\]

The two formulas describe the same affine involution in the two conjugate affine frames.

## 9. Guardrails [Audit]

1. `χ12` controls Pell orientation because it is the sign of `sqrt3` under cyclotomic Galois action.
2. `χ-3`, not `χ12`, controls the direct residue-field Galois quotient on `F4`.
3. The map from Pell orientation to the affine frame uses the previously established two-prime phase intertwiner \(\Psi(j)=w^j\). It is not a direct reduction of \(\lambda\) modulo two; direct residue multiplication by \(\lambda\) is trivial.
4. Selecting `b=w` uses the positive real embedding \(\sqrt3>0\), equivalently `R12>0`. Without an orientation choice, the pair \(\{w,w^2\}\) remains unordered.
5. This selects an affine frame but does not identify the Galois `V4` pointwise with the tangent translation `V4`.

## 10. Compact synthesis [D/I]

The complete orientation chain is

\[
\boxed{
\sigma_r(\sqrt3)=\chi_{12}(r)\sqrt3
\Longrightarrow
\sigma_r(\lambda)=\lambda^{\chi_{12}(r)}
\Longrightarrow
n\mapsto\chi_{12}(r)n
\Longrightarrow
j\mapsto\chi_{12}(r)j
\Longrightarrow
w\leftrightarrow w^2.
}
\]

After choosing the positive Pell generator \(\lambda=2+\sqrt3>1\),

\[
\boxed{
\lambda\mapsto j=+1\mapsto w,
}
\]

so the compatible affine trivialization is

\[
\boxed{b=w.}
\]

Time reversal sends

\[
\boxed{
\lambda\mapsto\lambda^{-1},
\qquad
b=w\mapsto w^2.
}
\]

Therefore the χ12 time-orientation law and the affine-frame choice are two manifestations of the same two-point orientation torsor, connected exactly by the ramified prime-3 to prime-2 phase intertwiner.
