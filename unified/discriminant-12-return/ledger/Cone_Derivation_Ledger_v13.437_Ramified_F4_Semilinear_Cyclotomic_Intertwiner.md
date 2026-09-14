# Cone Derivation Ledger v13.437 — Ramified F4 Semilinear Cyclotomic Intertwiner

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 0. Synchronization [Audit]

This checkpoint was assigned only after two fresh live-ledger checks. The newest numbered entry was `v13.436` (`V4 Hadamard Module Intertwiner`) at both checks, so `v13.437` was free immediately before writing.

The concurrent Suzuki thread has also advanced materially: `v13.434` outward-certified the pole-free odd finite-high block above `0.53 I`, and `v13.435` independently re-executed and verified that closure. This checkpoint does not alter that positivity certificate; it continues the exact cyclotomic/ramified-reduction target stated at the end of `v13.436`.

## 1. Cyclotomic polynomial and the ramified mod-2 layer [D]

Let

\[
K=\mathbf Q(\zeta_{12}),
\qquad
\mathcal O_K=\mathbf Z[\zeta_{12}],
\]

with

\[
\Phi_{12}(x)=x^4-x^2+1.
\]

Modulo two,

\[
\boxed{
\Phi_{12}(x)\equiv x^4+x^2+1=(x^2+x+1)^2\pmod2.
}
\]

Therefore

\[
\boxed{
\mathcal O_K/2\mathcal O_K
\cong
\mathbf F_2[x]/\bigl((x^2+x+1)^2\bigr).
}
\]

This is a nonreduced ring: the ramified mod-2 layer is a square-zero thickening of the degree-two residue field.

Let

\[
f(x)=x^2+x+1.
\]

Passing to the ramified residue-field quotient gives

\[
\boxed{
\mathcal O_K/\mathfrak P_2
\cong
\mathbf F_2[x]/(f)
\cong
\mathbf F_4.
}
\]

Write

\[
\omega=\bar\zeta_{12}.
\]

Then

\[
\boxed{
\omega^2+\omega+1=0,
\qquad
\omega^3=1.
}
\]

This refines the earlier `v13.416` statement: the residue field is the semisimple quotient of a nonreduced ramified mod-2 cyclotomic ring.

## 2. Multiplication by zeta reduces to multiplication by omega [D]

Let

\[
\mathcal Z=\times\zeta_{12}.
\]

Reduction modulo \(\mathfrak P_2\) gives the exact commuting square

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

In the ordered \(\mathbf F_2\)-basis \((1,\omega)\),

\[
\boxed{
[M_\omega]
=
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

Hence

\[
\boxed{M_\omega^3=I.}
\]

Thus the order-12 characteristic-zero cyclotomic multiplication collapses to an order-3 residue multiplication.

## 3. Frobenius and the prior mod-2 Pell/conjugation collapse [D]

The Frobenius automorphism

\[
\mathrm{Fr}(z)=z^2
\]

satisfies

\[
1\mapsto1,
\qquad
\omega\mapsto\omega^2=1+\omega.
\]

Therefore

\[
\boxed{
[\mathrm{Fr}]
=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}
}
\]

in the same basis.

From `v13.416`, the mod-2 reductions of the integral Pell-return matrix and real quadratic conjugation are exactly this same matrix after the audited additive identification:

\[
\boxed{
\bar g_{12}=\bar J_f=[\mathrm{Fr}].
}
\]

Hence three distinct characteristic-zero operators reduce as follows:

\[
\boxed{
\times\zeta_{12}\mapsto M_\omega,
\qquad
g_{12}\mapsto\mathrm{Fr},
\qquad
J_f\mapsto\mathrm{Fr}.
}
\]

The first has order three in the residue field; the latter two collapse to the same order-two additive involution.

## 4. Exact semilinear conjugation law [D]

Because

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

This is the literal finite-field semilinear relation between multiplication and Galois action.

For \(r\in U(12)\), let \(\bar\sigma_r\) be the induced action on \(\mathbf F_4\). By `v13.416`,

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

The exponent \(-1\) is interpreted in \(\mathbf F_4^\times\), so \(\omega^{-1}=\omega^2\).

## 5. Two exact orientation laws on different carriers [D/I]

The real-quadratic/Pell carrier obeys

\[
\boxed{
\sigma_r(\lambda)=\lambda^{\chi_{12}(r)},
\qquad
\lambda=2+\sqrt3.
}
\]

The ramified residue-field carrier obeys

\[
\boxed{
\bar\sigma_r(\omega)=\omega^{\chi_{-3}(r)}.
}
\]

Thus the project now has two exact inversion/orientation quotients:

\[
\boxed{
\chi_{12}:\ \text{Pell-time orientation},
\qquad
\chi_{-3}:\ \text{finite-field multiplication orientation}.
}
\]

They use the same ambient V4 labels but act on different arithmetic carriers.

**[Audit]** This is not evidence that \(\chi_{12}=\chi_{-3}\), nor that the Pell and residue-field dynamics are the same action.

## 6. Literal collapse of the other sign channels [D]

Reduction sends

\[
\zeta_{12}\mapsto\omega.
\]

Since

\[
i=\zeta_{12}^3,
\]

we get

\[
\boxed{i\mapsto\omega^3=1.}
\]

Also

\[
\sqrt3=\zeta_{12}+\zeta_{12}^{-1},
\]

so

\[
\boxed{
\sqrt3\mapsto\omega+\omega^2=1.
}
\]

Hence

\[
\boxed{
\lambda=2+\sqrt3\mapsto1.
}
\]

Therefore the literal \(\chi_{-4}\) complex-sign direction and \(\chi_{12}\) real/Pell-sign direction both collapse as element signs in characteristic two. The nontrivial surviving Galois quotient is \(\chi_{-3}\).

This gives an exact algebraic explanation for the character split previously observed in `v13.416`.

## 7. Nilpotent ramification layer [D/I]

Set

\[
R=\mathcal O_K/2\mathcal O_K
\cong
\mathbf F_2[x]/(f^2),
\qquad
f=x^2+x+1.
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
\boxed{R/(\eta)\cong\mathbf F_4.}
\]

Thus the ramified mod-2 cyclotomic ring is a first-order nilpotent thickening of \(\mathbf F_4\). Passing to the residue field discards this ramification tangent direction.

**[Audit]** No relation is asserted between this nilpotent direction and the Cone shell displacement, the Suzuki fluctuation sector, or any geometric tangent bundle. Such a relation would require a new exact intertwiner.

## 8. Finite-field semilinear group [D]

The two residue operators satisfy

\[
M_\omega^3=I,
\qquad
\mathrm{Fr}^2=I,
\qquad
\mathrm{Fr}\,M_\omega\,\mathrm{Fr}^{-1}=M_\omega^{-1}.
\]

Therefore

\[
\boxed{
\langle M_\omega,\mathrm{Fr}\rangle
\cong
C_3\rtimes C_2
\cong
D_6
\cong
S_3.
}
\]

Equivalently,

\[
\boxed{
\mathbf F_4^\times\rtimes\operatorname{Gal}(\mathbf F_4/\mathbf F_2)
\cong S_3.
}
\]

This is the exact semilinear symmetry generated by residue multiplication and Frobenius.

**[Audit]** This `S3` is not the characteristic-zero Pell dihedral group of order 24 and not the V4 cyclotomic Galois group. It is a quotient-level group arising only after ramified reduction.

## 9. Exact commuting/semilinear diagram [D]

The reduction may be summarized by

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
\boxed{
\bar\sigma_r M_\omega\bar\sigma_r^{-1}
=M_{\omega^{\chi_{-3}(r)}}.
}
\]

This exactly completes the reduction target stated in `v13.436` while preserving the distinction between multiplication and Galois action.

## 10. Interaction with the newly closed Suzuki finite-high obligation [Audit]

The simultaneous Suzuki progress is logically independent:

\[
\boxed{
A_{FF}^{(0)}\succeq0.53125I,
\qquad
A_{FF}\succeq0.53I
}
\]

is now outward-certified by `v13.434` and independently verified by `v13.435`.

The remaining odd-sector proof obligations recorded there are the cross-tail norm and normalized frozen-subspace bounds. The present `F4/S3` calculation supplies no automatic improvement to those inequalities.

## 11. Next exact target [I/Audit]

The new nonreduced layer suggests a precise arithmetic question:

\[
\boxed{
R=\mathbf F_2[x]/(f^2)
\longrightarrow
\mathbf F_4=R/(f)
}
\]

retains a square-zero ramification ideal. The next exact target is to determine the action of the full V4 Galois group, multiplication by \(\zeta_{12}\), and the transported Pell/conjugation operators on this square-zero ideal before passing to the residue field.

That calculation would distinguish what is genuinely lost in the semisimple \(\mathbf F_4\) quotient from what survives on the first-order ramified thickening.

---

**Checkpoint conclusion.** The characteristic-zero V4 Hadamard/cyclotomic module now reduces through the ramified prime to an exact finite-field semilinear system. Multiplication by \(\zeta_{12}\) becomes the order-3 map \(M_\omega\), the surviving \(\chi_{-3}\) Galois quotient becomes Frobenius, and Frobenius conjugates \(M_\omega\) to its inverse. These generators form `S3`. Simultaneously, the full mod-2 cyclotomic ring is not merely `F4` but the nonreduced thickening `F2[x]/((x^2+x+1)^2)`, exposing a square-zero ramification layer that is the next exact object to audit.