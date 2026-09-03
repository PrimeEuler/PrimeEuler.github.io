# Cone Derivation Ledger v13.180 — Pell Mesh Renormalization

Status tags: [D] exact derived, [I] interpretation, [O] open, [Audit] limitation.

## 1. Setup

Let

\[
\lambda=2+\sqrt3,
\qquad
\lambda^{-1}=2-\sqrt3,
\qquad
R_{12}=\log\lambda.
\]

From v13.179, the discriminant-12 Lorentz return acts in Paper-A null coordinates by

\[
\boxed{x' = \lambda x,\qquad y'=\lambda^{-1}y.}
\]

Hence every shell

\[
xy=n
\]

is invariant, and in rapidity coordinates

\[
x=\sqrt n\,e^s,\qquad y=\sqrt n\,e^{-s}
\]

the return is

\[
\boxed{s' = s+R_{12}.}
\]

The purpose of this note is to determine exactly how the continuous-resolution meshes of v13.171-v13.176 transform under this return.

---

## 2. An anchored one-dimensional mesh is scale-covariant

Generalize the boundary-anchored mesh to

\[
\Lambda_{a,m}
=
\left\{a+\frac{j}{m}:j\in\mathbb Z_{\ge0}\right\},
\qquad a>0,\ m>0.
\]

Under a positive scaling

\[
z' = c z,
\]

a mesh point

\[
z_j=a+\frac jm
\]

becomes

\[
z_j'
=ca+\frac{cj}{m}
=ca+\frac{j}{m/c}.
\]

Therefore

\[
\boxed{(a,m)\mapsto(ca,m/c).}
\]

[D] In particular,

\[
\boxed{ma\ \text{is invariant under simultaneous scaling of the mesh}.}
\]

Indeed

\[
\left(\frac mc\right)(ca)=ma.
\]

This is the exact scale-covariant completion of the special choice \(a=1\) used in the earlier continuous-resolution notes.

---

## 3. The discriminant-12 return creates a two-resolution mesh

Apply the Pell scaling separately to the two null coordinates.

For the x-coordinate,

\[
x' = \lambda x,
\]

so

\[
\boxed{a_x' = \lambda a_x,\qquad m_x'=m_x/\lambda.}
\]

For the y-coordinate,

\[
y'=\lambda^{-1}y,
\]

so

\[
\boxed{a_y'=\lambda^{-1}a_y,\qquad m_y'=\lambda m_y.}
\]

Thus an initially isotropic mesh

\[
m_x=m_y=m
\]

is sent to the anisotropic pair

\[
\boxed{
(m_x',m_y')
=
\left(\frac m\lambda,\lambda m\right).
}
\]

[D] Their product is invariant:

\[
\boxed{m_x'm_y'=m^2.}
\]

Equivalently, the cell-area scale is preserved:

\[
\frac1{m_x'm_y'}=\frac1{m^2}.
\]

This is the mesh counterpart of

\[
\det B_{12}=1.
\]

[I] The natural continuous-resolution object for the Lorentz return is therefore not a single scalar resolution m, but a reciprocal resolution pair \((m_x,m_y)\).

---

## 4. Exact phase covariance for a scaled reference point

For the generalized anchored mesh define the phase of a point z relative to \((a,m)\) by

\[
\boxed{\Theta_{a,m}(z)=\{m(z-a)\}.}
\]

If

\[
z'=cz,\qquad a'=ca,\qquad m'=m/c,
\]

then

\[
\Theta_{a',m'}(z')
=
\left\{\frac mc(cz-ca)\right\}
=
\{m(z-a)\}.
\]

Hence

\[
\boxed{
\Theta_{ca,m/c}(cz)=\Theta_{a,m}(z).
}
\]

[D] Mesh phase is an exact invariant of the scale-covariant mesh transport.

For the discriminant-12 return this gives

\[
\boxed{
\Theta_{\lambda a_x,m_x/\lambda}(\lambda x)
=
\Theta_{a_x,m_x}(x),
}
\]

and

\[
\boxed{
\Theta_{\lambda^{-1}a_y,\lambda m_y}(\lambda^{-1}y)
=
\Theta_{a_y,m_y}(y).
}
\]

This is the cleanest exact connection between the Pell return and the continuous-resolution phase formalism.

---

## 5. What happens to the earlier tangent phase

The previous boundary-anchored tangent phase was

\[
\theta_m(n)
=
\{m(\sqrt n-1)\}.
\]

This is the special case

\[
\theta_m(n)=\Theta_{1,m}(\sqrt n).
\]

Under the return, the diagonal tangent point

\[
(\sqrt n,\sqrt n)
\]

is sent to

\[
(\lambda\sqrt n,\lambda^{-1}\sqrt n),
\]

which is generally not diagonal.

Nevertheless, transporting the x- and y-meshes covariantly gives

\[
\boxed{
\Theta_{\lambda,m/\lambda}(\lambda\sqrt n)
=
\theta_m(n),
}
\]

and

\[
\boxed{
\Theta_{\lambda^{-1},\lambda m}(\lambda^{-1}\sqrt n)
=
\theta_m(n).
}
\]

[D] Thus the phase itself is preserved when the reference anchor and mesh are transported with the Lorentz flow.

[Audit] The original scalar quantity \(\theta_m(n)=\{m(\sqrt n-1)\}\) is not invariant if one insists on resetting the anchor to 1 and the mesh back to isotropic m after every return. Such a reset is an extra renormalization convention, not part of the exact Lorentz action.

---

## 6. Rapidity interpretation of the mesh renormalization

Write the two mesh resolutions as

\[
m_x=m e^{-\rho},
\qquad
m_y=m e^{\rho}.
\]

Then

\[
m_xm_y=m^2.
\]

Under one discriminant-12 return,

\[
(m_x,m_y)
\mapsto
\left(\frac{m_x}{\lambda},\lambda m_y\right),
\]

so

\[
\boxed{\rho' = \rho+R_{12}.}
\]

Thus the same Pell length that translates shell rapidity also translates mesh anisotropy rapidity:

\[
\boxed{
s' = s+R_{12},
\qquad
\rho'=\rho+R_{12}.
}
\]

[D] Therefore

\[
\boxed{s-\rho\ \text{is invariant}.}
\]

This is a new exact invariant of the jointly transported shell point and anisotropic mesh.

[I] The discriminant-12 return acts as a simultaneous translation on physical shell rapidity and logarithmic mesh anisotropy. Their relative rapidity is unchanged.

---

## 7. Integer iterates

After k returns,

\[
x_k=\lambda^k x_0,
\qquad
y_k=\lambda^{-k}y_0,
\]

and

\[
\boxed{s_k=s_0+kR_{12}.}
\]

The mesh resolutions evolve as

\[
\boxed{
m_{x,k}=m_{x,0}\lambda^{-k},
\qquad
m_{y,k}=m_{y,0}\lambda^k.
}
\]

Hence

\[
\boxed{m_{x,k}m_{y,k}=m_{x,0}m_{y,0}.}
\]

If

\[
m_{x,0}=m_{y,0}=m,
\]

then

\[
\boxed{
(m_{x,k},m_{y,k})
=(m\lambda^{-k},m\lambda^k).
}
\]

The anisotropy ratio is

\[
\boxed{
\frac{m_{y,k}}{m_{x,k}}=\lambda^{2k}.
}
\]

---

## 8. The gnomon arm does not simply scale

For a shell point define

\[
h=x+y=2T,
\qquad
g=x-y=2X.
\]

Then under

\[
x'=\lambda x,\qquad y'=\lambda^{-1}y,
\]

we obtain

\[
\begin{pmatrix}
h'\\g'
\end{pmatrix}
=
\begin{pmatrix}
2&\sqrt3\\
\sqrt3&2
\end{pmatrix}
\begin{pmatrix}
h\\g
\end{pmatrix}.
\]

Therefore

\[
\boxed{g'=\sqrt3\,h+2g.}
\]

Equivalently, with shell rapidity,

\[
g=2\sqrt n\sinh s,
\]

so

\[
\boxed{
g'=2\sqrt n\sinh(s+R_{12}).
}
\]

[Audit] The Paper-A one-sided gnomon arm is not multiplied by a single constant under the return except on a null ray. Therefore the scalar arm phase

\[
\{mg\}
\]

is not itself a Lorentz invariant under the exact return.

This rules out a naive identification of the earlier modular arm phase with a fixed cyclotomic/Pell phase.

---

## 9. Null-ray exception and tangent endpoints

At a tangent endpoint one null coordinate vanishes.

On the expanding null ray

\[
y=0,\qquad h=g=x,
\]

so

\[
\boxed{g'=\lambda g.}
\]

On the contracting null ray

\[
x=0,\qquad h=-g=y,
\]

so

\[
\boxed{g'=\lambda^{-1}g.}
\]

These are exactly the parabola/circle tangent endpoints from v13.177-v13.179.

Thus the tangent family is the unique place where the gnomon displacement itself transforms by a pure Pell-unit scale.

---

## 10. A renormalized mesh coordinate

For a general shell point, define the local null-coordinate mesh phases

\[
\phi_x=\Theta_{a_x,m_x}(x),
\qquad
\phi_y=\Theta_{a_y,m_y}(y).
\]

Under the jointly transported return,

\[
\boxed{\phi_x'=\phi_x,\qquad\phi_y'=\phi_y.}
\]

Hence the pair

\[
\boxed{(\phi_x,\phi_y)}
\]

is an exact phase invariant of the Pell-renormalized mesh.

[I] This pair, rather than the single isotropic arm phase \(\{mg\}\), is the more natural candidate for comparison with finite arithmetic quotients in the new discriminant-12 paper.

---

## 11. Relation to area preservation

A rectangular mesh cell has dimensions

\[
\Delta x=\frac1{m_x},
\qquad
\Delta y=\frac1{m_y}.
\]

Under the return,

\[
\Delta x'=\lambda\Delta x,
\qquad
\Delta y'=\lambda^{-1}\Delta y.
\]

Therefore

\[
\boxed{\Delta x'\Delta y'=\Delta x\Delta y.}
\]

[D] The Pell return preserves shell product and mesh-cell area simultaneously:

\[
\boxed{xy=n,\qquad \Delta x\Delta y=\text{constant}.}
\]

This is the discrete-resolution shadow of the determinant-one Lorentz action.

---

## 12. n=11 specialization

Let

\[
r=\sqrt{11}.
\]

Start at the diagonal tangent point

\[
(r,r).
\]

After k Pell returns,

\[
\boxed{
(x_k,y_k)
=(r\lambda^k,r\lambda^{-k}).
}
\]

The shell remains

\[
x_ky_k=11.
\]

Starting from an isotropic mesh \((m,m)\), transport it to

\[
\boxed{
(m_{x,k},m_{y,k})
=(m\lambda^{-k},m\lambda^k).
}
\]

With anchors transported from \((1,1)\) to

\[
(a_{x,k},a_{y,k})=(\lambda^k,\lambda^{-k}),
\]

the original tangent phase is preserved in each null coordinate:

\[
\boxed{
\Theta_{a_{x,k},m_{x,k}}(x_k)
=
\Theta_{a_{y,k},m_{y,k}}(y_k)
=
\{m(\sqrt{11}-1)\}.
}
\]

This is exact for every real \(m>0\) and every integer iterate k.

---

## 13. What this establishes

[D] Exact:

1. The Pell return transports an isotropic resolution m to a reciprocal anisotropic pair
   \[
   (m/\lambda,\lambda m).
   \]
2. The product \(m_xm_y\), hence mesh-cell area, is invariant.
3. Anchored mesh phase is exactly invariant when anchor and resolution are transported covariantly.
4. Physical shell rapidity and mesh-anisotropy rapidity both translate by \(R_{12}=\log(2+\sqrt3)\).
5. Their difference \(s-\rho\) is invariant.
6. The gnomon arm transforms by the Lorentz matrix, not by a scalar, except on the tangent/null rays.
7. Tangent endpoints are precisely the pure Pell-scaling directions.

[I] Interpretation:

The continuous-resolution framework and the discriminant-12 return are compatible after enlarging scalar resolution m to a two-component reciprocal mesh. The Pell return can then be viewed as a renormalization flow that preserves both shell area-product and mesh-cell area while translating physical and resolution rapidities together.

[O] Next question:

Investigate whether the invariant phase pair

\[
(\phi_x,\phi_y)
\]

has a canonical reduction at the ramified prime 2 that reproduces, or naturally maps to, the mod-2 transvection / Boolean quotient already present in the discriminant-12 arithmetic framework.

That comparison must be done algebraically; no identification with the finite quotient is claimed here.

---

## 14. Publication guardrails added

[Audit] Do not claim:

- the scalar isotropic resolution m is preserved by the Pell return;
- the boundary anchor 1 is preserved by the return;
- the original tangent phase \(\{m(\sqrt n-1)\}\) is invariant if the mesh is reset to anchor 1 after each step;
- the gnomon arm phase \(\{mg\}\) is a Lorentz invariant;
- the anisotropic phase pair has already been identified with the arithmetic mod-2 quotient;
- the twelve half-step tangent circles form a finite orbit under the Pell return.
