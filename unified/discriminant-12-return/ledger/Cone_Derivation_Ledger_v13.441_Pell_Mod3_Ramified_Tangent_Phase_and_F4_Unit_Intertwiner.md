# Cone Derivation Ledger v13.441 — Pell Mod-3 Ramified Tangent Phase and F4 Unit Intertwiner

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 0. Synchronization [Audit]

This checkpoint was assigned only after checking the live ledger twice. The newest numbered entry at the final pre-write check was `v13.440` (`Mod-3 Radical Line and Common AGL1(F3) Phase`), so `v13.441` was free.

The immediate predecessors are:

- `v13.438`: the full mod-2 cyclotomic ring is a ramified square-zero thickening with cyclotomic order `12 -> 6 -> 3`;
- `v13.439`: the Pell and cyclotomic branches share exact `C6`, `C3`, and `S3` quotient architecture, with an explicit three-point equivariant bijection;
- `v13.440`: the fourth Pell projective point is the unique mod-3 radical/eigenline, and the remaining three directions carry the common `AGL_1(F3)` phase.

This entry upgrades the three-point identification to a direct algebraic formula on the ramified local ring at `3`.

## 1. The preserved Pell form is a norm form [D]

Let

\[
F=\mathbf Q(\sqrt3),
\qquad
\mathcal O_F=\mathbf Z[\sqrt3],
\]

and use the ramified-ideal basis

\[
f_1=2,
\qquad
f_2=\sqrt3-1.
\]

For

\[
\alpha=m f_1+n f_2
      =2m+n(\sqrt3-1)
      =(2m-n)+n\sqrt3,
\]

the discriminant-12 form is

\[
q_{12}(m,n)=2m^2-2mn-n^2.
\]

Directly,

\[
N_{F/\mathbf Q}(\alpha)
=(2m-n)^2-3n^2
=4m^2-4mn-2n^2
=2q_{12}(m,n).
\]

Hence

\[
\boxed{N(\alpha)=2q_{12}(m,n).}
\]

Thus the primitive Pell-preserved quadratic form is exactly half the field norm in this ramified-ideal basis.

## 2. Ramification at 3 gives a dual-number ring [D]

Modulo `3`, set

\[
\epsilon:=\sqrt3\pmod3.
\]

Then

\[
\epsilon^2=3=0,
\]

so

\[
\boxed{
\mathcal O_F/3\mathcal O_F
\cong
\mathbf F_3[\epsilon]/(\epsilon^2).
}
\]

This is the exact characteristic-3 first-order ramified thickening.

The element \(\alpha\) becomes

\[
\bar\alpha=(2m-n)+n\epsilon.
\]

Write

\[
a:=2m-n.
\]

The image \(\bar\alpha\) is a unit iff

\[
a\neq0\pmod3.
\]

But

\[
a=2m-n=2(m+n)\pmod3,
\]

hence

\[
\boxed{
\bar\alpha\text{ nonunit}
\iff
m+n=0.
}
\]

Equivalently, for the ramified prime

\[
\mathfrak p_3=(\sqrt3),
\]

\[
\boxed{
\alpha\in\mathfrak p_3
\iff
m+n=0\pmod3.
}
\]

By `v13.440`, this is exactly the unique radical/null line of

\[
\bar q_{12}(m,n)=2(m+n)^2.
\]

So the fixed fourth projective point is precisely the nonunit direction in the ramified local ring.

## 3. The three-state shell is the projectivized local unit group [D]

For \(a\neq0\),

\[
\bar\alpha=a+n\epsilon
=a\left(1+\frac na\epsilon\right).
\]

Quotienting by scalar units gives

\[
\boxed{
(\mathcal O_F/3)^\times/\mathbf F_3^\times
\cong
1+\epsilon\mathbf F_3.
}
\]

Because \(\epsilon^2=0\),

\[
(1+s\epsilon)(1+t\epsilon)
=1+(s+t)\epsilon,
\]

so

\[
\boxed{
1+\epsilon\mathbf F_3
\cong
(\mathbf F_3,+)
\cong C_3.
}
\]

Thus the three anisotropic projective directions of `v13.440` are not merely a three-point orbit: they are exactly the projectivized units of the ramified dual-number ring.

## 4. Explicit rational phase coordinate [D]

Define on the anisotropic shell

\[
\boxed{
 j([m:n])=\frac{n}{m+n}\in\mathbf F_3.
}
\]

This gives

\[
\infty=[1:0]\mapsto0,
\qquad
0=[0:1]\mapsto1,
\qquad
1=[1:1]\mapsto2.
\]

At the radical line

\[
2=[2:1],
\]

the denominator vanishes. Therefore

\[
\boxed{
\text{the unique radical/fixed line is exactly the pole of the phase coordinate.}
}
\]

Since

\[
a=2(m+n),
\]

one also has

\[
\boxed{
 j=2\frac na.
}
\]

For a general local unit

\[
a+b\epsilon,
\qquad a\neq0,
\]

the phase therefore has the intrinsic expression

\[
\boxed{
 j(a+b\epsilon)=2\frac ba.
}
\]

This is invariant under multiplication by any scalar in \(\mathbf F_3^\times\), so it is genuinely projective.

## 5. Pell return is translation on the ramified tangent [D]

The fundamental unit is

\[
\lambda=2+\sqrt3.
\]

Modulo `3`,

\[
\lambda=2+\epsilon
=-1+\epsilon
=-(1-\epsilon)
=-(1+2\epsilon).
\]

After quotienting by scalar units, the factor \(-1\) disappears, leaving multiplication by

\[
1+2\epsilon.
\]

For a normalized local unit

\[
1+t\epsilon,
\]

we get

\[
(1+t\epsilon)(1+2\epsilon)
=1+(t+2)\epsilon.
\]

Thus

\[
t\mapsto t+2.
\]

Since

\[
j=2t,
\]

\[
2(t+2)=2t+1\pmod3,
\]

hence

\[
\boxed{j\mapsto j+1.}
\]

So the projective order-three Pell return is literally translation on the first-order ramified tangent coordinate.

## 6. Quadratic conjugation is reflection [D]

Real quadratic conjugation sends

\[
\epsilon\mapsto-\epsilon.
\]

Therefore

\[
1+t\epsilon\mapsto1-t\epsilon,
\]

so

\[
t\mapsto-t
\]

and therefore

\[
\boxed{j\mapsto-j.}
\]

The two generators act exactly as

\[
\boxed{
 j\mapsto j+1,
 \qquad
 j\mapsto-j
}
\]

on \(\mathbf F_3\). Thus

\[
\boxed{
\langle[g],[J_f]\rangle
\cong
\mathrm{AGL}_1(\mathbf F_3)
\cong S_3.
}
\]

This gives a local-ring derivation of the projective `S3` action found in `v13.439-v13.440`.

## 7. Direct algebraic intertwiner to the cyclotomic residue unit group [D]

Let

\[
\mathbf F_4=\mathbf F_2(\omega),
\qquad
\omega^2+\omega+1=0.
\]

Then

\[
\mathbf F_4^\times=\{1,\omega,\omega^2\}\cong C_3.
\]

Define

\[
\boxed{
\Psi:
(\mathcal O_F/3)^\times/\mathbf F_3^\times
\longrightarrow
\mathbf F_4^\times,
\qquad
\Psi([a+b\epsilon])=\omega^{2b/a}.
}
\]

This is well-defined because the exponent lies in \(\mathbf F_3\) and is scalar-invariant.

In normalized tangent coordinate \(t=b/a\),

\[
\Psi(1+t\epsilon)=\omega^{2t}.
\]

Under the Pell return,

\[
t\mapsto t+2,
\]

so

\[
2(t+2)=2t+1.
\]

Hence

\[
\boxed{
\Psi(\lambda x)=\omega\,\Psi(x).
}
\]

Under conjugation,

\[
t\mapsto-t,
\]

so

\[
\Psi(\bar x)
=\omega^{-2t}
=(\omega^{2t})^2.
\]

Therefore

\[
\boxed{
\Psi\circ[g]
=M_\omega\circ\Psi,
\qquad
\Psi\circ[J_f]
=\mathrm{Fr}\circ\Psi.
}
\]

This upgrades the pointwise bijection \(\Theta\) of `v13.439-v13.440` to a direct algebraic formula on the entire projectivized local unit group.

## 8. Two-prime ramified synthesis [D/I]

The two branches now have parallel but distinct first-order ramified carriers.

### Real-quadratic Pell branch at 3

\[
\boxed{
\mathcal O_{\mathbf Q(\sqrt3)}/3
\cong
\mathbf F_3[\epsilon]/(\epsilon^2).
}
\]

Its projectivized local units are

\[
\boxed{
(\mathcal O_F/3)^\times/\mathbf F_3^\times
\cong1+\epsilon\mathbf F_3
\cong C_3.
}
\]

### Cyclotomic branch at 2

From `v13.438`,

\[
\boxed{
\mathcal O_{K_{12}}/2
\cong
\mathbf F_4[\eta]/(\eta^2).
}
\]

Its residue unit shell is

\[
\boxed{\mathbf F_4^\times\cong C_3.}
\]

The explicit intertwiner \(\Psi\) identifies these two `C3` phase carriers equivariantly under the corresponding inversion extensions.

Thus the common finite phase is not an unexplained coincidence:

\[
\boxed{
(\mathcal O_F/3)^\times/\mathbf F_3^\times
\xrightarrow{\ \Psi\ }
\mathbf F_4^\times
}
\]

is an exact `S3`-equivariant bijection.

## 9. What is lost and what survives [D/I]

On the Pell side, the nonunit radical line is removed when passing to the projectivized unit group. What survives is the first-order tangent phase

\[
1+t\epsilon.
\]

On the cyclotomic side, passage from the full mod-2 ring to \(\mathbf F_4\) removes the nilpotent tangent layer but retains the semisimple three-state unit group.

Thus the two primes contribute complementary local mechanisms:

\[
\boxed{
\begin{array}{c|c|c}
\text{prime}&\text{ramified local carrier}&\text{three-phase quotient}\\
\hline
3&\mathbf F_3[\epsilon]/(\epsilon^2)&1+\epsilon\mathbf F_3\\
2&\mathbf F_4[\eta]/(\eta^2)&\mathbf F_4^\times
\end{array}}
\]

and \(\Psi\) identifies the resulting `C3`/`S3` phase actions.

## 10. Guardrails [Audit]

- \(\Psi\) is an equivariant identification of finite phase carriers; it is not a ring homomorphism between characteristic `3` and characteristic `2` rings.
- The nilpotents \(\epsilon\) and \(\eta\) live at different ramified primes and are not identified.
- The radical Pell line is the nonunit direction at \(\mathfrak p_3\); it has no fourth element counterpart in \(\mathbf F_4^\times\).
- The exponent coordinate \(j\in\mathbf F_3\) is a permutation/phase coordinate, not a subfield embedding \(\mathbf F_3\subset\mathbf F_4\).
- No identification is made with Cone shell adjacency, Suzuki operator blocks, or analytic positivity spaces.

## 11. Checkpoint conclusion

The common three-state Pell-cyclotomic phase now has a direct local-algebra formula. In the ramified ring

\[
\mathcal O_{\mathbf Q(\sqrt3)}/3
\cong
\mathbf F_3[\epsilon]/(\epsilon^2),
\]

the unique radical projective line is exactly the nonunit direction, while the other three projective directions are the projectivized principal units. Their intrinsic phase is

\[
\boxed{j=2b/a=\frac{n}{m+n}},
\]

with the Pell return acting by translation \(j\mapsto j+1\) and conjugation by reflection \(j\mapsto-j\). The explicit formula

\[
\boxed{
[a+b\epsilon]\longmapsto\omega^{2b/a}
}
\]

then intertwines this ramified Pell phase with multiplication/Frobenius on \(\mathbf F_4^\times\). This upgrades the common `S3` quotient from an abstract/permutation coincidence to an explicit algebraic equivalence of the two finite phase carriers.