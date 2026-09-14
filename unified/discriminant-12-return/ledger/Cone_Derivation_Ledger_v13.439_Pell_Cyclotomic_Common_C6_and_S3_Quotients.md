# Cone Derivation Ledger v13.439 — Pell–Cyclotomic Common C6 and S3 Quotients

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 0. Synchronization [Audit]

This checkpoint was assigned after checking the live repository through v13.438. It compares the Pell residue clock from v13.412/v13.414 with the cyclotomic ramified clock from v13.437/v13.438.

The purpose is to determine whether the two recurring six-step phenomena are merely analogous or possess a genuine common quotient.

## 1. Two characteristic-zero/order-12 clocks [D]

On the Pell side, with

\[
g=g_{12}=\begin{pmatrix}3&1\\2&1\end{pmatrix},
\]

the mod-12 cyclic subgroup has exact order 12 and

\[
\boxed{g^6\equiv7I\pmod{12}}.
\]

Since \(7^2\equiv1\pmod{12}\), this is the central order-2 half-turn of the Pell residue cycle.

On the cyclotomic side,

\[
\mathcal Z=\times\zeta_{12},
\qquad
\zeta_{12}^{12}=1,
\]

and

\[
\boxed{\zeta_{12}^6=-1},
\]

so multiplication by \(-1\) is the characteristic-zero central half-turn.

Thus both cyclic clocks have the abstract form

\[
C_{12}=\langle r\rangle,
\qquad r^6\text{ central of order }2.
\]

**[Audit]** The elements \(7I\) and \(-1\) live on different carriers and are not identified as arithmetic elements.

## 2. Natural first reductions kill the two half-turns [D]

### Pell branch

Reduction modulo 6 gives

\[
7I\equiv I\pmod6.
\]

Since the audited local order is

\[
\operatorname{ord}_6(g)=6,
\]

the reduction map on the Pell cyclic subgroup is

\[
\boxed{C_{12}\twoheadrightarrow C_6},
\]

with kernel

\[
\boxed{\{I,g^6\}=\{I,7I\}}.
\]

### Cyclotomic branch

In

\[
R=\mathcal O_K/2\mathcal O_K,
\]

one has \(-1=1\). If \(u=\bar\zeta_{12}\), v13.438 proves

\[
\operatorname{ord}_R(u)=6.
\]

Hence cyclotomic reduction gives

\[
\boxed{C_{12}\twoheadrightarrow C_6},
\]

with kernel

\[
\boxed{\{1,\zeta_{12}^6\}=\{1,-1\}}.
\]

Therefore both branches possess the same exact quotient pattern

\[
\boxed{
C_{12}/\langle\text{half-turn}\rangle\cong C_6.
}
\]

This is a genuine common abstract quotient, not merely a matching order count.

## 3. The surviving six-step midpoints [D]

The two resulting \(C_6\) clocks each have a nontrivial cubic involution.

### Pell mod 6

Using the audited mod-12 power

\[
g^3\equiv
\begin{pmatrix}
5&3\\6&11
\end{pmatrix}
\pmod{12},
\]

one obtains

\[
\boxed{
 g^3\equiv
\begin{pmatrix}
5&3\\0&5
\end{pmatrix}
\pmod6.
}
\]

Its square is the identity mod 6, and it is not the identity, so it is the unique order-2 element of \(\langle g\bmod6\rangle\cong C_6\).

### Cyclotomic mod 2

From v13.438, writing

\[
\eta=u^2+u+1,
\qquad
\varepsilon=(u+1)\eta,
\]

one has

\[
\boxed{u^3=1+\varepsilon\neq1},
\qquad
\boxed{\varepsilon^2=0},
\]

and hence

\[
(1+\varepsilon)^2=1.
\]

So \(u^3\) is the unique order-2 element of \(\langle u\rangle\cong C_6\).

Therefore, after identifying the abstract generators

\[
\bar g\longleftrightarrow u,
\]

the cubic half-turns correspond as group elements.

**[Audit]** There is no claimed ring, module, or matrix map sending the Pell operator \(g^3\bmod6\) to the cyclotomic element \(1+\varepsilon\). The correspondence here is at the cyclic-group level.

## 4. The branches diverge after C6 [D]

The common \(C_6\) quotient does not mean the subsequent reductions coincide.

On the cyclotomic side,

\[
R\twoheadrightarrow\mathbf F_4
\]

kills the nilpotent half-turn \(u^3=1+\varepsilon\), leaving

\[
\boxed{C_6\twoheadrightarrow C_3}.
\]

On the Pell side, direct reduction modulo 3 retains order 6:

\[
\operatorname{ord}_3(g)=6,
\qquad
\boxed{g^3\equiv-I\pmod3}.
\]

Thus reduction to \(\mathrm{GL}_2(\mathbf F_3)\) does not itself kill the half-turn.

The correct Pell analogue of the cyclotomic \(C_3\) quotient is projectivization.

## 5. Pell projectivization produces the same C3 quotient [D]

Let \([g]\) denote the image of \(g\bmod3\) in \(\mathrm{PGL}_2(\mathbf F_3)\). Since

\[
g^3=-I,
\]

and scalar \(-I\) becomes trivial projectively,

\[
\boxed{[g]^3=1}.
\]

Because \([g]\neq1\),

\[
\boxed{\operatorname{ord}([g])=3}.
\]

Thus the Pell branch has the natural quotient

\[
\boxed{
C_6\xrightarrow{\bmod3}C_6
\xrightarrow{\mathrm{projectivize}}C_3,
}
\]

which kills the same abstract cubic half-turn as the cyclotomic residue map

\[
\boxed{
C_6\xrightarrow{R\to\mathbf F_4}C_3.
}
\]

Hence both branches possess a common abstract order-3 quotient.

## 6. Adjoining inversion: common S3 quotient [D]

The Pell inversion operator satisfies

\[
J_f^2=I,
\qquad
J_fgJ_f=g^{-1}.
\]

Reducing mod 3 and projectivizing gives

\[
[J_f]^2=1,
\qquad
[J_f][g][J_f]=[g]^{-1}.
\]

Since \([g]\) has order 3,

\[
\boxed{
\langle[g],[J_f]\rangle
\cong C_3\rtimes C_2
\cong S_3.
}
\]

On the cyclotomic residue-field side, v13.437 proves

\[
M_\omega^3=I,
\qquad
\mathrm{Fr}^2=I,
\qquad
\mathrm{Fr}M_\omega\mathrm{Fr}^{-1}=M_\omega^{-1},
\]

hence

\[
\boxed{
\langle M_\omega,\mathrm{Fr}\rangle
\cong C_3\rtimes C_2
\cong S_3.
}
\]

Therefore the Pell and cyclotomic branches share an exact abstract semidirect-product quotient

\[
\boxed{S_3}.
\]

An explicit abstract isomorphism is determined by

\[
\boxed{
[g]\longmapsto M_\omega,
\qquad
[J_f]\longmapsto\mathrm{Fr}.
}
\]

## 7. Concrete equivariant three-point identification [D]

The common \(S_3\) quotient is visible on natural three-point sets.

Modulo 3,

\[
g=\begin{pmatrix}0&1\\2&1\end{pmatrix},
\qquad
J_f=\begin{pmatrix}1&2\\0&2\end{pmatrix}.
\]

Act on

\[
\mathbf P^1(\mathbf F_3)=\{\infty,0,1,2\}
\]

by fractional linear transformations.

For \(g\),

\[
x\mapsto\frac{1}{2x+1}=\frac1{1-x},
\]

so

\[
\boxed{
\infty\mapsto0\mapsto1\mapsto\infty,
\qquad
2\mapsto2.
}
\]

For \(J_f\),

\[
x\mapsto\frac{x+2}{2}=2x+1,
\]

so

\[
\boxed{
0\leftrightarrow1,
\qquad
\infty\mapsto\infty,
\qquad
2\mapsto2.
}
\]

Thus the Pell projective \(S_3\) acts faithfully on the three-point orbit

\[
\Omega_P=\{\infty,0,1\}
\]

and fixes the fourth point \(2\).

On the cyclotomic side,

\[
\mathbf F_4^\times=\{1,\omega,\omega^2\}.
\]

Multiplication by \(\omega\) gives

\[
1\mapsto\omega\mapsto\omega^2\mapsto1,
\]

while Frobenius gives

\[
1\mapsto1,
\qquad
\omega\leftrightarrow\omega^2.
\]

Define

\[
\boxed{
\Theta:\Omega_P\to\mathbf F_4^\times,
\qquad
\Theta(\infty)=1,
\quad
\Theta(0)=\omega,
\quad
\Theta(1)=\omega^2.
}
\]

Then exactly

\[
\boxed{
\Theta\circ[g]=M_\omega\circ\Theta,
}
\]

and

\[
\boxed{
\Theta\circ[J_f]=\mathrm{Fr}\circ\Theta.
}
\]

Hence \(\Theta\) is an explicit equivariant bijection between the Pell three-point projective orbit and the nonzero cyclotomic residue field.

This is stronger than an abstract group isomorphism: the two \(S_3\) quotients have concretely isomorphic permutation representations.

## 8. Dihedral quotient tower [D]

At the cyclic/inversion level the comparison can be arranged as

\[
\boxed{
D_{24}
\twoheadrightarrow
D_{12}
\twoheadrightarrow
D_6\cong S_3,
}
\]

where the notation \(D_{2n}=C_n\rtimes C_2\) denotes a dihedral group of order \(2n\).

The Pell realization is:

\[
\langle g,J_f\rangle\pmod{12}
\twoheadrightarrow
\langle g,J_f\rangle\pmod6
\twoheadrightarrow
\langle[g],[J_f]\rangle\subset\mathrm{PGL}_2(\mathbf F_3).
\]

The cyclotomic realization is:

\[
\langle\times\zeta_{12},\text{conjugation}\rangle
\twoheadrightarrow
\langle M_u,\bar\sigma\rangle_R
\twoheadrightarrow
\langle M_\omega,\mathrm{Fr}\rangle_{\mathbf F_4}.
\]

Both therefore realize the same abstract quotient tower

\[
\boxed{D_{24}\to D_{12}\to S_3},
\]

although on different arithmetic carriers.

## 9. What is genuinely common [D/I]

The common structure is now precise:

1. order-12 rotation;
2. central half-turn at step 6;
3. quotient by that half-turn to order 6;
4. a second cubic half-turn in the order-6 clock;
5. quotient to order 3;
6. an inversion involution acting by \(r\mapsto r^{-1}\);
7. final semidirect product \(C_3\rtimes C_2\cong S_3\);
8. an explicit equivariant three-point permutation model.

Thus the two six-step phenomena are not the same operator, but neither are they accidental analogies. They are two arithmetic realizations of the same quotient architecture.

## 10. Guardrails [Audit]

The following remain distinct:

- \(g^6=7I\pmod{12}\) and \(\zeta_{12}^6=-1\);
- Pell reduction mod 6 and cyclotomic reduction mod 2;
- the Pell matrix \(g^3\bmod6\) and the cyclotomic unipotent \(1+\varepsilon\);
- projectivization over \(\mathbf F_3\) and reduction to \(\mathbf F_4\);
- the Pell projective three-point orbit and \(\mathbf F_4^\times\) as arithmetic sets.

Only the explicitly constructed cyclic, dihedral, and permutation-representation identifications are asserted.

---

**Checkpoint conclusion.** The Pell and cyclotomic six-step returns possess a genuine common quotient structure. Both order-12 clocks first quotient by their central half-turn to \(C_6\), and both then admit a natural quotient to \(C_3\). After adjoining inversion, both terminate in the same \(S_3\) presentation. Most strongly, the Pell projective orbit \(\{\infty,0,1\}\subset\mathbf P^1(\mathbf F_3)\) is explicitly equivariantly identified with \(\mathbf F_4^\times\) by \(\infty\mapsto1,0\mapsto\omega,1\mapsto\omega^2\).