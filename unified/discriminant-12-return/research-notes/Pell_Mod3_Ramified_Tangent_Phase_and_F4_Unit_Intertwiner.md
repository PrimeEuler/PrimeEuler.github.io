# Pell Mod-3 Ramified Tangent Phase and the F4 Unit Intertwiner

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 1. Starting point

Let

\[
F=\mathbf Q(\sqrt3),\qquad \mathcal O_F=\mathbf Z[\sqrt3],
\]

and use the ramified-ideal basis

\[
f_1=2,\qquad f_2=\sqrt3-1.
\]

For

\[
\alpha=m f_1+n f_2
      =2m+n(\sqrt3-1)
      =(2m-n)+n\sqrt3,
\]

the preserved discriminant-12 form is

\[
q_{12}(m,n)=2m^2-2mn-n^2.
\]

Directly,

\[
N_{F/\mathbf Q}(\alpha)
=(2m-n)^2-3n^2
=2q_{12}(m,n).
\]

Hence

\[
\boxed{N(\alpha)=2q_{12}(m,n).}
\]

## 2. Ramification at 3 and the radical line

Modulo 3 set

\[
\epsilon:=\sqrt3\pmod3.
\]

Since \(\epsilon^2=3=0\),

\[
\boxed{
\mathcal O_F/3\mathcal O_F
\cong
\mathbf F_3[\epsilon]/(\epsilon^2).
}
\]

Thus

\[
\bar\alpha=(2m-n)+n\epsilon.
\]

The unique ramified prime is

\[
\mathfrak p_3=(\sqrt3),
\]

and \(\bar\alpha\) is nonunit exactly when its scalar coefficient vanishes:

\[
2m-n=0\pmod3.
\]

But

\[
2m-n=2(m+n)\pmod3,
\]

so

\[
\boxed{
\alpha\in\mathfrak p_3
\iff
m+n=0\pmod3.
}
\]

This is exactly the unique projective radical line of

\[
\bar q_{12}(m,n)=2(m+n)^2.
\]

Therefore the fourth projective point in \(\mathbf P^1(\mathbf F_3)\) is not an extra phase state: it is precisely the nonunit/ramified direction.

## 3. The three anisotropic directions as principal units

Assume \(m+n\neq0\), equivalently \(a:=2m-n\neq0\). Then

\[
\bar\alpha=a+n\epsilon
=a\left(1+\frac na\epsilon\right).
\]

Quotienting units by scalar units \(\mathbf F_3^\times\) leaves exactly the principal-unit group

\[
\boxed{
(\mathcal O_F/3)^\times/\mathbf F_3^\times
\cong
1+\epsilon\mathbf F_3.
}
\]

Because \(\epsilon^2=0\),

\[
(1+s\epsilon)(1+t\epsilon)=1+(s+t)\epsilon,
\]

so

\[
\boxed{
1+\epsilon\mathbf F_3\cong(\mathbf F_3,+)\cong C_3.
}
\]

Thus the three-point projective shell of v13.440 has an intrinsic local-ring realization: it is the projectivized unit group of the ramified dual-number ring.

## 4. Exact rational phase coordinate

On the projective shell define

\[
\boxed{
j([m:n])=\frac{n}{m+n}\in\mathbf F_3.}
\]

This is well-defined whenever \(m+n\neq0\), and gives

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

the denominator vanishes, so the fixed fourth point is literally the pole of the phase coordinate.

Since

\[
a=2m-n=2(m+n),
\]

one also has

\[
\boxed{
j=2\frac na.}
\]

For a general unit \(a+b\epsilon\), the corresponding phase is therefore

\[
\boxed{
j(a+b\epsilon)=2\frac ba.}
\]

This is invariant under multiplication by a nonzero scalar in \(\mathbf F_3\).

## 5. Pell return becomes translation

The fundamental Pell unit is

\[
\lambda=2+\sqrt3.
\]

Modulo 3,

\[
\lambda=2+\epsilon=-1+\epsilon
=-(1-\epsilon)
=-(1+2\epsilon).
\]

The scalar \(-1\) disappears in the projectivized unit group, so the Pell return acts there by multiplication by

\[
1+2\epsilon.
\]

Hence

\[
(1+t\epsilon)(1+2\epsilon)
=1+(t+2)\epsilon,
\]

so

\[
t\mapsto t+2.
\]

Since \(j=2t\),

\[
\boxed{j\mapsto j+1.}
\]

Thus the order-three projective Pell clock is exactly translation on the first-order ramified tangent coordinate.

## 6. Conjugation becomes reflection

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
t\mapsto-t,
\qquad
\boxed{j\mapsto-j.}
\]

Hence the Pell return and conjugation act as

\[
\boxed{
j\mapsto j+1,\qquad j\mapsto-j}
\]

on \(\mathbf F_3\), realizing

\[
\boxed{\mathrm{AGL}_1(\mathbf F_3)\cong S_3.}
\]

This gives a local-ring derivation of the phase action found projectively in v13.440.

## 7. Direct algebraic intertwiner with the cyclotomic F4 unit shell

Let

\[
\mathbf F_4=\mathbf F_2(\omega),
\qquad
\omega^2+\omega+1=0.
\]

Its nonzero group is

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
\Psi([a+b\epsilon])=\omega^{\,2b/a}.
}
\]

Because \(2b/a\in\mathbf F_3\), this is well-defined. Under the identification

\[
1+t\epsilon\leftrightarrow t,
\]

it is simply

\[
t\longmapsto\omega^{2t}.
\]

For the Pell return,

\[
t\mapsto t+2,
\]

so

\[
2(t+2)=2t+1\pmod3.
\]

Hence

\[
\boxed{
\Psi(\lambda\cdot x)
=\omega\,\Psi(x).
}
\]

For conjugation,

\[
t\mapsto-t,
\]

so

\[
\Psi(\bar x)
=\omega^{-2t}
=(\omega^{2t})^2
=\mathrm{Fr}(\Psi(x)).
\]

Therefore

\[
\boxed{
\Psi\circ[g]=M_\omega\circ\Psi,
\qquad
\Psi\circ[J_f]=\mathrm{Fr}\circ\Psi.
}
\]

This recovers the three-point intertwiner of v13.439-v13.440 from a direct algebraic formula rather than a pointwise assignment.

## 8. Two ramified tangent carriers

The project now contains two distinct first-order ramified local structures:

### Pell / real-quadratic side at 3

\[
\boxed{
\mathcal O_F/3
\cong
\mathbf F_3[\epsilon]/(\epsilon^2).
}
\]

Its projectivized unit tangent is

\[
1+\epsilon\mathbf F_3\cong C_3.
\]

### Cyclotomic side at 2

From v13.438,

\[
\boxed{
\mathcal O_{K_{12}}/2
\cong
\mathbf F_4[\eta]/(\eta^2).
}
\]

The cyclotomic generator has a semisimple \(\mathbf F_4^\times\cong C_3\) component plus a square-zero order-two ramification correction.

Thus the two primes produce different local rings but compatible three-phase quotients:

\[
\boxed{
(\mathcal O_F/3)^\times/\mathbf F_3^\times
\cong C_3
\cong
\mathbf F_4^\times.
}
\]

The common \(C_3\) is now realized explicitly by \(\Psi\).

## 9. Guardrails

- The map \(\Psi\) is an equivariant group/set identification of the three-phase quotients, not a ring homomorphism between characteristic 3 and characteristic 2 rings.
- The mod-3 dual-number tangent \(\epsilon\) and the mod-2 cyclotomic nilpotent \(\eta\) are different ramification directions.
- The radical Pell line corresponds to nonunits modulo \(\mathfrak p_3\); it has no fourth counterpart in \(\mathbf F_4^\times\).
- The phase exponent \(j\in\mathbf F_3\) is an exponent/permutation coordinate, not an embedded subfield of \(\mathbf F_4\).
- No Cone-shell, Suzuki, RH, or GRH identification follows from this local-ring equivalence.

## 10. Structural conclusion

The common three-state Pell-cyclotomic phase is no longer merely an abstract S3 orbit. It is the explicit projectivized ramified-unit coordinate

\[
\boxed{
j=2b/a}
\]

on

\[
\mathbf F_3[\epsilon]/(\epsilon^2),
\]

with the unique radical line exactly where \(a=0\). The Pell return translates this tangent phase, conjugation reflects it, and

\[
\boxed{
[a+b\epsilon]\mapsto\omega^{2b/a}
}
\]

intertwines the resulting AGL1(F3) action with multiplication/Frobenius on \(\mathbf F_4^\times\). This supplies the direct algebraic formula sought after v13.440 and gives an exact two-prime ramified explanation for the common S3 phase carrier.