# Cone Derivation Ledger v13.225 — V4 Imprimitive-Character Reconciliation and Prime Selector

Date: 2026-09-04
Status: CORRECTION + EXACT NEW RESULT — supersedes the overstrong quadratic-subfield statement in v13.224; research branch remains open

## 0. Pre-write synchronization

Immediately before this write, the current `master` tree was re-fetched. Its tip was still commit

`18378f90919db72db32e1af01ff9ec5ff1121362`

with v13.224 as the highest ledger checkpoint. No newer external-audit ledger entry had yet landed in the repository. This checkpoint therefore performs an internal reconciliation before extending the branch.

## 1. Correction to v13.224: conductor matters

v13.224 correctly identified the Hadamard character table on

\[
U(12)=\{1,5,7,11\}\cong V_4
\]

and correctly proved that every transformed floor channel has Dirichlet series

\[
\zeta(s)L(s,\chi),
\]

where `chi` is the corresponding Dirichlet character **modulo 12**, extended by zero off the units.

However, v13.224 then over-identified the two imprimitive channels `chi_{-4}` and `chi_{-3}` with the primitive quadratic-field Dedekind zeta functions. That is not literally correct because the mod-12 characters vanish at all integers not coprime to 12, so the extra bad prime is removed from the primitive Euler product.

The `chi_12` channel is different: discriminant 12 is its primitive conductor, so that channel was already correct.

## 2. Exact corrected Euler factors

Let `chi_{-4}^{prim}` be the primitive conductor-4 quadratic character and `chi_{-3}^{prim}` the primitive conductor-3 quadratic character.

The corresponding characters occurring in the `U(12)` Fourier transform are their mod-12 inductions:

\[
\chi_{-4}^{(12)}=\chi_{-4}^{prim}\,\chi_{0,3},
\qquad
\chi_{-3}^{(12)}=\chi_{-3}^{prim}\,\chi_{0,4}.
\]

Since

\[
\chi_{-4}^{prim}(3)=-1,
\qquad
\chi_{-3}^{prim}(2)=-1,
\]

we obtain

\[
\boxed{
L(s,\chi_{-4}^{(12)})
=(1+3^{-s})L(s,\chi_{-4}^{prim}),
}
\]

and

\[
\boxed{
L(s,\chi_{-3}^{(12)})
=(1+2^{-s})L(s,\chi_{-3}^{prim}).
}
\]

Therefore the transformed floor-channel Dirichlet series are

\[
\boxed{
\zeta(s)L(s,\chi_{-4}^{(12)})
=(1+3^{-s})\zeta_{\mathbf Q(i)}(s),
}
\]

\[
\boxed{
\zeta(s)L(s,\chi_{-3}^{(12)})
=(1+2^{-s})\zeta_{\mathbf Q(\sqrt{-3})}(s),
}
\]

while the primitive discriminant-12 channel remains exactly

\[
\boxed{
\zeta(s)L(s,\chi_{12})
=\zeta_{\mathbf Q(\sqrt3)}(s).
}
\]

Thus the full `V4` transform still detects the three quadratic-subfield characters of `K_12=Q(zeta_12)`, but only the `chi_12` channel is literally the unmodified Dedekind-zeta ideal-counting channel. The `chi_{-4}` and `chi_{-3}` channels are bad-prime-modified versions forced by restricting the carrier to `U(12)`.

### Audit consequence

The sentence in v13.224 claiming that all three nonprincipal channels are **exactly** the three quadratic-field ideal-counting summatory functions is superseded by this checkpoint.

Correct formulation:

\[
\boxed{
\text{the three nonprincipal Fourier channels correspond to the three quadratic subfield characters,}
}
\]

with Euler-factor modifications at the primes dividing `12` for the two imprimitive channels, and with the real quadratic `chi_12` channel exact without modification.

This actually strengthens the special role of the discriminant-12 branch: among the three nontrivial `V4` characters, `chi_12` is the one whose conductor already equals the full modulus 12.

## 3. Exact coefficient increment law

For any character `chi` in the transform, define

\[
a_\chi(m)=(1*\chi)(m)=\sum_{d\mid m}\chi(d).
\]

Since

\[
\widehat S_\chi(n)=\sum_{m\le n}a_\chi(m),
\]

we have the exact discrete derivative

\[
\boxed{
\widehat S_\chi(n)-\widehat S_\chi(n-1)=a_\chi(n).
}
\]

For a prime `p` not dividing 12,

\[
\boxed{a_\chi(p)=1+\chi(p).}
\]

Every nonprincipal value is therefore either `0` or `2`.

## 4. The prime-residue selector table

In character order

\[
(\chi_0,\chi_{-4},\chi_{-3},\chi_{12}),
\]

the prime increment vector for `p>3` depends only on `p mod 12`:

\[
\boxed{
\begin{array}{c|c}
p\bmod12 &
\Delta\widehat S(p)\\
\hline
1 &(2,2,2,2)\\
5 &(2,2,0,0)\\
7 &(2,0,2,0)\\
11&(2,0,0,2)
\end{array}}
\]

where

\[
\Delta\widehat S(p)
:=\widehat S(p)-\widehat S(p-1).
\]

**[D] V4 prime-selector theorem.** For primes `p>3`, the residue class of `p` in `U(12)` selects exactly which nonprincipal Fourier channel receives the prime jump. In particular,

\[
\boxed{
p\equiv11\pmod{12}
\Longrightarrow
\Delta\widehat S(p)=(2,0,0,2),
}
\]

so among the three nonprincipal channels only the real-quadratic `chi_12` component receives the prime increment.

This is an exact finite Fourier statement, not a numerical pattern.

## 5. The distinguished n=11 shell

For the current shell,

\[
\widehat S(10)=(13,11,9,7),
\]

and

\[
\widehat S(11)=(15,11,9,9).
\]

Therefore

\[
\boxed{
\widehat S(11)-\widehat S(10)=(2,0,0,2).
}
\]

Thus the new prime `11` contributes only to

1. the principal unit-filtered channel; and
2. the discriminant-12 real-quadratic channel.

The two imaginary-quadratic character channels receive zero at the 11-step.

This is the cleanest exact divisor/Fourier statement yet found that singles out the same `chi_12` branch selected independently by the principal paper.

### Scope guardrail

The selector is a residue-class theorem, not an 11-only theorem. Every prime

\[
p\equiv11\pmod{12}
\]

has the same Fourier increment pattern.

What is special about `p=11` in this project is the **combination** of:

- the generic residue-class selector above;
- the geometric outer shell `x+y=12` with `xy=11`;
- the principal-paper narrow-class identity `[p_11]=[p_2]`; and
- the Artin specialization `Art(p_11)=T_11`.

The divisor transform does not by itself make 11 unique; it lands in the same `chi_12` channel in which the independently proved Artin specialization already lives.

## 6. Local ideal-counting interpretation of the chi_12 coefficient

Because `chi_12` is primitive,

\[
a_{12}(m)=\sum_{d\mid m}\chi_{12}(d)
\]

is exactly the number of ideals of norm `m` in `Q(sqrt3)`.

For a prime power `p^e`, the local factor is

\[
\boxed{
a_{12}(p^e)=\sum_{j=0}^{e}\chi_{12}(p)^j.}
\]

Hence:

- if `p=2` or `3` (ramified), `a_{12}(p^e)=1`;
- if `p congruent 1,11 mod 12` (split), `a_{12}(p^e)=e+1`;
- if `p congruent 5,7 mod 12` (inert), `a_{12}(p^e)=1` for even `e` and `0` for odd `e`.

At `p=11`,

\[
\boxed{a_{12}(11)=2,}
\]

exactly expressing the two prime ideals above the split rational prime 11 in `Q(sqrt3)`.

The principal paper further identifies one of these through the explicit generator

\[
1+2\sqrt3,
\qquad N(1+2\sqrt3)=-11,
\]

and its narrow ideal class. Thus the divisor coefficient and the principal-paper ideal specialization now meet at the same rational prime without identifying distinct structures.

## 7. Audit of the previously noticed n=11 equalities

The v13.224 finite-shell identities

\[
\widehat S_{-3}(11)=\widehat S_{12}(11)
\]

and

\[
\widehat F_{12}(11)=-\widehat F_0(11)
\]

are exact but are not evidence of a unique 11-law.

The first equality is equivalent to

\[
S_7(11)=S_{11}(11),
\]

and direct exact computation shows the same equality already occurs at

\[
n=1,2,3,4,5,6,11,12,13
\]

among `1<=n<=5000`, with no further occurrence found in that finite range.

The second equality is equivalent to

\[
F_1(n)+F_{11}(n)=0.
\]

Since these channel sums are nonnegative, this means both vanish. It holds for every

\[
1\le n\le11,
\]

so the `n=11` instance is the endpoint of an elementary initial-range phenomenon, not an exceptional identity.

**[Audit]** Do not use either equality as evidence of the Artin specialization. The prime-increment selector of Sections 3–5 is the structurally meaningful statement.

## 8. Current strongest bridge

The divisor/V4 branch now has the following exact chain:

\[
\boxed{
\text{unit residue classes }U(12)
\xleftrightarrow{H_4}
\text{four characters mod 12}
}
\]

\[
\boxed{
\Delta\widehat S_\chi(p)=1+\chi(p)
}
\]

and at the distinguished shell prime

\[
\boxed{
p=11\Rightarrow(2,0,0,2),}
\]

so the only nonprincipal divisor channel activated at the 11-step is

\[
\boxed{\chi_{12}\leftrightarrow\mathbf Q(\sqrt3).}
\]

That is exactly the real-quadratic branch selected independently by the trace-4 / discriminant-12 theorem.

This is a genuine intertwining at the **character-selection level**. It is not yet an intertwiner between the Cone geometric action, the Pell return, the Artin action, and the divisor transform as operators.

## 9. Next task

The next high-value calculation is to express the `chi_12` coefficients and summatory function in the principal paper's explicit ramified-ideal coordinates as far as possible, while respecting the fact that indefinite norm-form representations have infinitely many unit-equivalent generators unless a reduction/fundamental-domain condition is imposed.

A second branch is to determine whether the A161664 complement can be decomposed into a unit-character part plus explicit `2`- and `3`-adic correction channels, so that the loss incurred by restricting to `U(12)` is accounted for rather than hidden.

Do not revise the audited principal v0.3.5 source from this checkpoint alone.