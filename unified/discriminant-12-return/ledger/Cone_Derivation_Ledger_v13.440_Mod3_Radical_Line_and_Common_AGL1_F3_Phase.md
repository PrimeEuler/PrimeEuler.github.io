# Cone Derivation Ledger v13.440 — Mod-3 Radical Line and Common AGL1(F3) Phase

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 0. Synchronization [Audit]

This checkpoint was assigned after a live ledger recheck through v13.439. It continues the exact Pell–cyclotomic common-quotient analysis without identifying distinct arithmetic carriers.

## 1. The discriminant-12 form degenerates modulo 3 [D]

Start from the primitive preserved form

\[
q_{12}(m,n)=2m^2-2mn-n^2.
\]

Modulo 3,

\[
\bar q_{12}(m,n)=2m^2+mn+2n^2.
\]

But

\[
2(m+n)^2=2m^2+4mn+2n^2
\equiv 2m^2+mn+2n^2\pmod3,
\]

so

\[
\boxed{\bar q_{12}(m,n)=2(m+n)^2.}
\]

Hence the mod-3 form has rank one. Its unique projective null line is

\[
m+n=0
\]

or

\[
\boxed{[m:n]=[2:1].}
\]

This is exactly the projective point previously denoted \(2\in\mathbf P^1(\mathbf F_3)\).

## 2. The fixed projective point is the radical/eigenline [D]

Reduce

\[
g=g_{12}=\begin{pmatrix}3&1\\2&1\end{pmatrix}
\]

modulo 3:

\[
\bar g=\begin{pmatrix}0&1\\2&1\end{pmatrix}.
\]

Its characteristic polynomial is

\[
X^2-X+1\equiv(X+1)^2\pmod3,
\]

so the only eigenvalue is \(2=-1\). Write

\[
\bar g=2I+N,
\qquad
N=\begin{pmatrix}1&1\\2&2\end{pmatrix}.
\]

Then

\[
\boxed{N^2=0.}
\]

Moreover

\[
N\binom{2}{1}=0,
\]

so the unique eigenline is exactly

\[
\boxed{\ker N=\{m+n=0\},}
\]

the radical/null line of \(\bar q_{12}\).

Thus the fixed point is forced simultaneously by the degenerate quadratic form and the repeated-eigenvalue Pell matrix.

## 3. The three complementary points form the anisotropic unit shell [D]

The projective line is

\[
\mathbf P^1(\mathbf F_3)=\{\infty,0,1,2\}.
\]

Using representatives

\[
\infty=[1:0],\quad0=[0:1],\quad1=[1:1],\quad2=[2:1],
\]

one finds

\[
\bar q_{12}(\infty)=2,
\qquad
\bar q_{12}(0)=2,
\qquad
\bar q_{12}(1)=2,
\qquad
\bar q_{12}(2)=0.
\]

Hence

\[
\boxed{
\mathbf P^1(\mathbf F_3)
=\Omega_P\sqcup\{2\},
\qquad
\Omega_P=\{[v]:\bar q_{12}(v)=2\}
=\{\infty,0,1\}.
}
\]

Since every nonzero scalar \(a\in\mathbf F_3^\times\) satisfies \(a^2=1\), the value of a quadratic form is well-defined on projective lines. Equivalently

\[
2\bar q_{12}=(m+n)^2,
\]

so

\[
\boxed{\Omega_P=\{[v]:2\bar q_{12}(v)=1\}.}
\]

This is a natural three-point projective unit shell complementary to the radical line.

## 4. Projective Pell dynamics are characteristic-3 unipotent [D]

Because scalar matrices disappear in projective space, multiply \(\bar g\) by the scalar 2:

\[
[\bar g]=[I+2N].
\]

Since \((2N)^2=0\) and the characteristic is 3,

\[
(I+2N)^3=I.
\]

Thus

\[
\boxed{\operatorname{ord}_{\mathrm{PGL}_2(\mathbf F_3)}([g])=3.}
\]

The unique fixed point is the radical line \(2\), while the action on \(\Omega_P\) is the 3-cycle

\[
\boxed{\infty\to0\to1\to\infty.}
\]

The conjugation involution

\[
J_f=\begin{pmatrix}1&-1\\0&-1\end{pmatrix}
\]

also fixes the radical line projectively and acts on \(\Omega_P\) by

\[
\boxed{0\leftrightarrow1,\qquad\infty\mapsto\infty.}
\]

Therefore

\[
\langle[g],[J_f]\rangle\cong C_3\rtimes C_2\cong S_3
\]

acts faithfully on the anisotropic unit shell and fixes the radical point.

## 5. Comparison with the cyclotomic residue unit shell [D/I]

For the ramified residue field

\[
\mathbf F_4=\mathbf F_2(\omega),
\qquad
\omega^2+\omega+1=0,
\]

one has

\[
\mathbf F_4^\times=\{1,\omega,\omega^2\}.
\]

Every nonzero element has norm

\[
N_{\mathbf F_4/\mathbf F_2}(z)=z^3=1,
\]

so

\[
\boxed{\mathbf F_4^\times=\{z:N(z)=1\}.}
\]

Thus the common S3 quotient acts on two natural three-point unit-norm shells:

\[
\boxed{
\Omega_P=\{[v]:2\bar q_{12}(v)=1\}
}
\]

and

\[
\boxed{
\Omega_C=\mathbf F_4^\times=\{z:N_{\mathbf F_4/\mathbf F_2}(z)=1\}.
}
\]

The previously established equivariant bijection

\[
\Theta:\Omega_P\to\Omega_C,
\qquad
\Theta(\infty)=1,
\quad
\Theta(0)=\omega,
\quad
\Theta(1)=\omega^2,
\]

satisfies

\[
\boxed{\Theta\circ[g]=M_\omega\circ\Theta,}
\]

and

\[
\boxed{\Theta\circ[J_f]=\mathrm{Fr}\circ\Theta.}
\]

**[Audit]** This is an exact equivariant bijection of three-point S3-sets. It is not a field/ring isomorphism from the Pell projective carrier to \(\mathbf F_4\), nor does it identify their quadratic/norm forms numerically across different base fields.

## 6. Common phase coordinate [D]

There is a canonical cyclic coordinate on both three-point shells.

On the Pell shell, define

\[
p_j=[g]^j(\infty),
\qquad j\in\mathbf F_3,
\]

so

\[
p_0=\infty,
\qquad p_1=0,
\qquad p_2=1.
\]

Then

\[
[g]:j\mapsto j+1,
\qquad
[J_f]:j\mapsto-j.
\]

On the cyclotomic shell write

\[
c_j=\omega^j,
\qquad j\in\mathbf F_3.
\]

Then

\[
M_\omega:j\mapsto j+1,
\qquad
\mathrm{Fr}:j\mapsto2j=-j.
\]

Therefore both actions become exactly

\[
\boxed{
j\mapsto j+1,
\qquad
j\mapsto-j
}
\]

on \(\mathbf F_3\). Hence

\[
\boxed{
S_3\cong\mathrm{AGL}_1(\mathbf F_3)
}
\]

is the common finite phase symmetry.

This is stronger than an abstract group isomorphism: the Pell anisotropic shell and the cyclotomic residue unit group admit the same affine phase coordinate.

## 7. Structural synthesis [D/I]

The four-point Pell projective geometry decomposes canonically as

\[
\boxed{
\mathbf P^1(\mathbf F_3)
=
\underbrace{\{[v]:\bar q_{12}(v)=0\}}_{\text{one radical line}}
\sqcup
\underbrace{\{[v]:2\bar q_{12}(v)=1\}}_{\text{three-state unit shell}}.
}
\]

The S3 quotient fixes the radical line and acts faithfully on the three-state shell.

On the cyclotomic residue side there is no fourth nonzero multiplicative state:

\[
\mathbf F_4^\times
\]

is already exactly the three-state unit shell. The common phase coordinate identifies these two S3 carriers.

Interpretively, the transition from four projective directions to a three-state S3 orbit is therefore explained on the Pell side by discriminant ramification at 3: one direction becomes the unique radical/eigenline, leaving three anisotropic unit directions for the nontrivial finite permutation action.

## 8. Guardrails [Audit]

1. The fixed projective point is a mod-3 radical line, not a fourth element of \(\mathbf F_4^\times\).
2. The bijection \(\Theta\) identifies S3 actions, not the ambient fields or rings.
3. The mod-3 degeneration of \(q_{12}\) and the mod-2 ramification of the cyclotomic ring occur at different primes and on different carriers.
4. The common phase coordinate \(\mathbf F_3\) is a permutation/exponent coordinate, not a claim that \(\mathbf F_3\subset\mathbf F_4\).
5. No identification is made here with geometric mod-12 shell adjacency or Suzuki operator blocks.

## 9. Next exact targets

1. Determine whether the common phase coordinate can be expressed directly from the Pell projective ratio as a rational function on \(\Omega_P\).
2. Compare the unique mod-3 radical line with the discriminant-3 ramified prime in \(\mathbf Q(\sqrt3)\) and its ideal-theoretic meaning.
3. Test whether the two-prime picture — mod 3 producing the Pell three-state shell and mod 2 producing the cyclotomic \(\mathbf F_4^\times\) shell — admits a clean CRT/discriminant-12 synthesis without conflating carriers.

---

**Checkpoint conclusion.** The formerly unexplained fourth projective point is exactly the unique radical/eigenline created when the discriminant-12 quadratic form degenerates modulo 3. The remaining three projective directions form a normalized anisotropic unit shell carrying the same S3 action as \(\mathbf F_4^\times\). Both become the standard affine action \(j\mapsto j+1\), \(j\mapsto-j\) on a common three-phase coordinate \(\mathbf F_3\).