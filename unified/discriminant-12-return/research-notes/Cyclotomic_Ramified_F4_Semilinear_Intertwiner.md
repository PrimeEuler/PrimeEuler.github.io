# Cyclotomic Ramified F4 Semilinear Intertwiner

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 1. Cyclotomic reduction at the ramified prime [D]

Let

\[
K=\mathbf Q(\zeta_{12}),\qquad \mathcal O_K=\mathbf Z[\zeta_{12}],
\]

with

\[
\Phi_{12}(x)=x^4-x^2+1.
\]

Modulo 2,

\[
\boxed{
\Phi_{12}(x)\equiv x^4+x^2+1=(x^2+x+1)^2\pmod2.
}
\]

Hence

\[
\mathcal O_K/2\mathcal O_K
\cong
\mathbf F_2[x]/\bigl((x^2+x+1)^2\bigr)
\]

is nonreduced. If

\[
f(x)=x^2+x+1,
\]

then the ramified residue-field quotient is

\[
\boxed{
\mathcal O_K/\mathfrak P_2\cong \mathbf F_2[x]/(f)\cong\mathbf F_4.
}
\]

Write

\[
\omega=\bar\zeta_{12}.
\]

Then

\[
\boxed{
\omega^2+\omega+1=0,\qquad \omega^3=1.
}
\]

Thus the full mod-2 ring retains a square-zero ramified layer, while passage to the residue field kills that nilpotent layer.

## 2. Multiplication by zeta reduces to multiplication by omega [D]

Let

\[
\mathcal Z=\times\zeta_{12}:\mathcal O_K\to\mathcal O_K.
\]

Reduction gives the commuting square

\[
\boxed{
\begin{array}{ccc}
\mathcal O_K&\xrightarrow{\ \mathcal Z\ }&\mathcal O_K\\
\downarrow&&\downarrow\\
\mathbf F_4&\xrightarrow{\ M_\omega\ }&\mathbf F_4,
\end{array}}
\]

where

\[
M_\omega(z)=\omega z.
\]

In the \(\mathbf F_2\)-basis \((1,\omega)\),

\[
\boxed{
[M_\omega]=
\begin{pmatrix}
0&1\\
1&1
\end{pmatrix}.
}
\]

Indeed,

\[
M_\omega(1)=\omega,
\qquad
M_\omega(\omega)=\omega^2=1+\omega.
\]

Therefore

\[
\boxed{M_\omega^3=I,}
\]

so the order-12 cyclotomic multiplication collapses to order 3 on the residue field.

## 3. Frobenius matrix and the prior Pell/conjugation collapse [D]

The Frobenius automorphism

\[
\mathrm{Fr}(z)=z^2
\]

acts by

\[
1\mapsto1,
\qquad
\omega\mapsto\omega^2=1+\omega.
\]

Hence in the same basis,

\[
\boxed{
[\mathrm{Fr}]=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
}
\]

This is exactly the matrix already obtained in the audited mod-2 reduction of both the integral Pell return and real quadratic conjugation:

\[
\boxed{
\bar g_{12}=\bar J_f=[\mathrm{Fr}].
}
\]

Thus the two characteristic-zero operators collapse to the same additive Frobenius involution, while multiplication by \(\zeta_{12}\) reduces to the distinct order-3 multiplication operator \(M_\omega\).

## 4. Exact semilinear conjugation law [D]

Since

\[
\mathrm{Fr}(\omega)=\omega^2=\omega^{-1},
\]

one has

\[
\boxed{
\mathrm{Fr}\,M_\omega\,\mathrm{Fr}^{-1}
=M_{\omega^2}
=M_\omega^{-1}.
}
\]

Equivalently,

\[
\boxed{
\mathrm{Fr}\,M_\omega=M_{\omega^2}\,\mathrm{Fr}.
}
\]

This is the finite-field semilinear relation between multiplication and Galois action.

For \(r\in U(12)\), let \(\bar\sigma_r\) denote the induced residue-field Galois action. Since the quotient is controlled by \(\chi_{-3}\),

\[
\bar\sigma_r=
\begin{cases}
\mathrm{id},&\chi_{-3}(r)=+1,\\
\mathrm{Fr},&\chi_{-3}(r)=-1.
\end{cases}
\]

Therefore

\[
\boxed{
\bar\sigma_r\,M_\omega\,\bar\sigma_r^{-1}
=M_{\omega^{\chi_{-3}(r)}}.
}
\]

Here exponent \(-1\) means inversion in \(\mathbf F_4^\times\), so \(\omega^{-1}=\omega^2\).

This is the exact finite-field analogue of an orientation law, but it is controlled by \(\chi_{-3}\), not by the Pell-time character \(\chi_{12}\).

## 5. Paired orientation laws on distinct carriers [D/I]

The project now has two exact but distinct formulas:

\[
\boxed{
\sigma_r(\lambda)=\lambda^{\chi_{12}(r)},
\qquad
\lambda=2+\sqrt3,
}
\]

on the real-quadratic/Pell carrier, and

\[
\boxed{
\bar\sigma_r(\omega)=\omega^{\chi_{-3}(r)}
}
\]

on the ramified residue-field carrier.

Thus

\[
\boxed{
\chi_{12}:\ \text{Pell time orientation},
\qquad
\chi_{-3}:\ \text{finite-field multiplication orientation}.
}
\]

The same V4 labels therefore govern two different inversion quotients on two different arithmetic carriers.

## 6. What collapses in the residue field [D]

The characteristic-zero distinguished elements reduce as follows:

\[
\zeta_{12}\mapsto\omega,
\]

\[
i=\zeta_{12}^3\mapsto\omega^3=1,
\]

\[
\sqrt3=\zeta_{12}+\zeta_{12}^{-1}
\mapsto\omega+\omega^2=1,
\]

and hence

\[
\lambda=2+\sqrt3\mapsto1.
\]

So the \(\chi_{-4}\) complex-sign direction and the \(\chi_{12}\) real/Pell-sign direction both collapse as literal element signs in characteristic two, while the \(\chi_{-3}\) quotient survives as the nontrivial residue-field Galois action.

This explains algebraically why the v13.416 finite-field layer sees \(\chi_{-3}\) rather than \(\chi_{12}\).

## 7. Ramified nonreduced layer [D/I]

Before quotienting all the way to \(\mathbf F_4\), one has

\[
R:=\mathcal O_K/2\mathcal O_K
\cong
\mathbf F_2[x]/(f^2),
\qquad f=x^2+x+1.
\]

Let

\[
\eta=f(\bar\zeta_{12})\in R.
\]

Then

\[
\boxed{\eta^2=0,}
\]

and

\[
R/(\eta)\cong\mathbf F_4.
\]

Thus the ramified mod-2 cyclotomic object is not merely \(\mathbf F_4\); it is a first-order nilpotent thickening of \(\mathbf F_4\). The residue-field picture records the semisimple quotient and discards the ramification tangent direction.

**[Audit]** No identification is made between this nilpotent thickening and the Cone shell displacement, Suzuki matrix fluctuation space, or any geometric tangent bundle. Any such relation would require a separate exact map.

## 8. Exact diagram [D]

The multiplication and Galois reductions may be summarized as

\[
\boxed{
\begin{array}{ccccc}
\mathcal O_K
&\xrightarrow{\times\zeta_{12}}&
\mathcal O_K
&\xrightarrow{\sigma_r}&
\mathcal O_K\\
\downarrow&&\downarrow&&\downarrow\\
\mathbf F_4
&\xrightarrow{\times\omega}&
\mathbf F_4
&\xrightarrow{\bar\sigma_r}&
\mathbf F_4,
\end{array}}
\]

with

\[
\bar\sigma_r\,M_\omega\,\bar\sigma_r^{-1}
=M_{\omega^{\chi_{-3}(r)}}.
\]

Hence multiplication by the primitive cyclotomic generator and the surviving Galois involution do not merge under ramified reduction: they become the order-3 multiplication and order-2 Frobenius generators of

\[
\boxed{
\mathbf F_4^\times\rtimes\operatorname{Gal}(\mathbf F_4/\mathbf F_2)
\cong C_3\rtimes C_2\cong S_3.
}
\]

Indeed Frobenius acts on \(\mathbf F_4^\times\cong C_3\) by inversion.

## 9. Structural conclusion [I/Audit]

The v13.436 characteristic-zero V4 module and the v13.416 finite-field quotient now connect by an exact semilinear reduction:

\[
\times\zeta_{12}\longmapsto\times\omega,
\qquad
\chi_{-3}\text{-odd Galois action}\longmapsto\mathrm{Fr},
\]

with

\[
\mathrm{Fr}\,M_\omega\,\mathrm{Fr}^{-1}=M_\omega^{-1}.
\]

The resulting finite-field symmetry generated by multiplication and Frobenius is the dihedral group of order 6, equivalently \(S_3\). This is an exact quotient-level structure.

**[Audit]** This \(S_3\) is not the characteristic-zero Pell dihedral group of order 24, nor is it the V4 Galois group. It is a new finite-field semilinear group arising after ramified reduction.