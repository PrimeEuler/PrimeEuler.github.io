# Cone Derivation Ledger v13.247 — Half-Order Hasse Vanishing and Support-Multiplicity Transition

Date: 2026-09-05
Status: EXACT NEW NECESSARY CONDITION + SUPPORT-ADJUNCTION VALUATION LAW — continuation of v13.246; research branch remains open

## 0. Pre-write synchronization

Immediately before this write, the authoritative project README and current `master` tip were re-fetched. The tip remained

`86c693710d51e60e47a7d9d4418d6b0b5f08fde1`

with v13.246 as the highest ledger checkpoint. No newer external-audit checkpoint had landed. This entry extends the reconciled research branch and does not revise the audited principal v0.3.5 paper.

## 1. Question

v13.246 globally classified the low-dimensional universal centered-Legendre support closure: only q=5 and q=7 have rank two, while every prime q>=11 has a rank-three witness.

The remaining open problem is stronger:

\[
q\ge 11 \stackrel{?}{\Longrightarrow} \text{no isolated exact Legendre resonance at all}.
\]

An isolated resonance need not have a rank-two universal operator orbit, so a new invariant is required.

This entry extracts such a necessary condition directly from the carrier polynomial. Exact Legendre resonance forces a root of multiplicity exactly `(q-1)/2` at `x=1` after reduction modulo q. Equivalently, half of the low Hasse derivatives — or half of the low weighted moments — must vanish simultaneously modulo q.

The entry also derives the exact way this multiplicity changes when a genuinely new support prime is adjoined.

## 2. Carrier polynomial

Let `M>=3`, let `psi` be the quadratic carrier character on `U(M)`, and assume `q` is an odd prime with `q\nmid M`.

Define the integer carrier polynomial

\[
\boxed{
F_{M,\psi}(x)
=
\sum_{\substack{0\le r<M\\(r,M)=1}}
\psi(r)x^r
\in\mathbf Z[x].
}
\]

Its folded coefficients modulo `x^q-1` are exactly the additive pushforward

\[
P_{M,q,\psi}(t)
=
\sum_{\substack{r\in U(M)\\r\equiv t\pmod q}}
\psi(r),
\]

because

\[
\boxed{
F_{M,\psi}(x)
\equiv
\sum_{t\in\mathbf F_q}P_{M,q,\psi}(t)x^t
\pmod{x^q-1}.
}
\]

Thus the exact Legendre-resonance condition can be read directly from a polynomial in one variable.

## 3. Affine Legendre polynomial

Let

\[
e=\frac{q-1}{2}
\]

and let

\[
L_{A,B,\epsilon}(x)
=
\sum_{t\in\mathbf F_q}
\epsilon\,\chi(At+B)x^t,
\]

where `A!=0`, `epsilon in {+-1}`, and `chi` is the quadratic character modulo q, extended by `chi(0)=0`.

Every exact centered crossing resonance gives such an affine Legendre pushforward, with `A` and `B` determined by the carrier-to-crossing affine change of variable.

Euler's criterion gives, in `F_q`,

\[
\chi(At+B)=(At+B)^e.
\]

For the j-th Hasse derivative at x=1,

\[
D^{[j]}L(1)
=
\sum_{t\in\mathbf F_q}
\epsilon\chi(At+B)\binom tj.
\]

For `0<=j<e`, the summand is a polynomial in t of degree at most

\[
e+j<q-1.
\]

Every power sum of positive degree strictly below `q-1` vanishes over `F_q`, and the constant term also vanishes after summing over the field. Hence

\[
\boxed{
D^{[j]}L_{A,B,\epsilon}(1)=0
\qquad (0\le j<e).
}
\]

At j=e, the top-degree term has degree `2e=q-1`. Since

\[
\sum_{t\in\mathbf F_q}t^{q-1}=-1,
\]

while every lower power sum vanishes, one gets

\[
\boxed{
D^{[e]}L_{A,B,\epsilon}(1)
=-\epsilon\,A^e(e!)^{-1}
=-\epsilon\,\chi(A)(e!)^{-1}
e0.
}
\]

Therefore:

\[
\boxed{
\operatorname{ord}_{x=1}L_{A,B,\epsilon}(x)=e=\frac{q-1}{2}
\quad\text{in }\mathbf F_q[x].
}
\]

This multiplicity is independent of the affine shift B and depends on the slope A only through the sign of the first nonzero Hasse coefficient.

## 4. Half-order Hasse-vanishing theorem for every exact resonance

Reduce the carrier polynomial modulo q. Since

\[
x^q-1=(x-1)^q
\qquad\text{in }\mathbf F_q[x],
\]

replacing `F_{M,psi}` by its folded polynomial modulo `x^q-1` can change it only by a multiple of `(x-1)^q`.

Because

\[
e=(q-1)/2<q,
\]

the order of vanishing at x=1 below level q is unchanged by folding.

Hence exact Legendre resonance forces

\[
\boxed{
\operatorname{ord}_{x=1}\overline{F}_{M,\psi}(x)
=\frac{q-1}{2},
}
\]

where the bar denotes reduction modulo q.

Equivalently,

\[
\boxed{
D^{[j]}\overline F_{M,\psi}(1)=0
\quad (0\le j<e),
\qquad
D^{[e]}\overline F_{M,\psi}(1)\ne0.
}
\]

This is the **half-order Hasse-vanishing obstruction**.

For the first three relevant crossing primes:

\[
q=5:\ e=2,
\qquad
q=7:\ e=3,
\qquad
q=11:\ e=5.
\]

Thus a hypothetical q=11 resonance already requires five consecutive Hasse conditions at x=1, rather than the two or three required by the actual q=5 and q=7 resonances.

## 5. Weighted binomial-moment formulation

By definition,

\[
D^{[j]}F_{M,\psi}(1)
=
\sum_{\substack{0\le r<M\\(r,M)=1}}
\psi(r)\binom rj.
\]

Therefore every exact q-resonance satisfies

\[
\boxed{
\sum_{r\in U(M)}
\psi(r)\binom rj
\equiv0\pmod q
\qquad
0\le j<\frac{q-1}{2},
}
\]

and

\[
\boxed{
\sum_{r\in U(M)}
\psi(r)\binom re
\not\equiv0\pmod q,
\qquad e=\frac{q-1}{2}.
}
\]

Because `j!` is invertible modulo q for `j<q`, the binomial basis and the monomial basis are related by an invertible triangular transformation. Hence the same necessary condition is equivalently

\[
\boxed{
\sum_{r\in U(M)}\psi(r)r^j\equiv0\pmod q
\qquad
0\le j<e,
}
\]

with a nonzero e-th normalized moment.

So exact resonance forces simultaneous cancellation of the first half of the carrier's character-weighted power moments modulo q.

This is substantially stronger than the second-moment collision-energy condition alone.

## 6. Exact leading Hasse signature of a Legendre target

For an affine Legendre pushforward, the first nonzero coefficient is not arbitrary. The calculation above gives

\[
\boxed{
e!\,D^{[e]}L_{A,B,\epsilon}(1)
=-\epsilon\chi(A)\in\{\pm1\}.
}
\]

Thus every exact resonance satisfies the normalized signature condition

\[
\boxed{
-e!\,D^{[e]}\overline F_{M,\psi}(1)\in\{\pm1\}\subset\mathbf F_q.
}
\]

The half-order root multiplicity and this first nonzero sign together are an intrinsic mod-q fingerprint of exact Legendre folding.

## 7. Exact polynomial identity for adjoining a new support prime

Now let p be a genuinely new support prime:

\[
p\nmid Mq,
\qquad
\sigma=\psi(p)=\chi_D(p)\in\{\pm1\}.
\]

The enlarged support polynomial is obtained by taking all p lifts of each old unit class modulo M and subtracting those divisible by p. Exactly:

\[
\boxed{
F_{pM}(x)
=
F_M(x)
\sum_{j=0}^{p-1}x^{jM}
-\sigma F_M(x^p).
}
\]

This is the polynomial-level form of the support-transition identity of v13.236.

It is exact over `Z[x]`, before any reduction modulo q.

## 8. Multiplicity-transition law

Work modulo q and suppose

\[
\nu=\operatorname{ord}_{x=1}\overline F_M(x)<q.
\]

Write

\[
\overline F_M(1+y)=c y^\nu+O(y^{\nu+1}),
\qquad c\ne0.
\]

The geometric factor satisfies

\[
\sum_{j=0}^{p-1}(1+y)^{jM}
=p+O(y),
\]

while

\[
(1+y)^p-1=py+O(y^2).
\]

Therefore

\[
\overline F_{pM}(1+y)
=
 c\bigl(p-\sigma p^\nu\bigr)y^\nu
+O(y^{\nu+1}).
\]

Reducing `p` modulo q to `r in F_q^x`, we obtain the exact first-order transition rule:

\[
\boxed{
\operatorname{ord}_{x=1}\overline F_{pM}=\nu
\iff
r-\sigma r^\nu\ne0.
}
\]

Equivalently, the multiplicity can increase only when

\[
\boxed{
r^{\nu-1}=\sigma.
}
\]

Thus new-support growth carries a finite local valuation label, depending only on

\[
\boxed{(r,\sigma)=(p\bmod q,\chi_D(p)),}
\]

exactly as in the signal-space transition operator.

## 9. First nonzero Hasse coefficient under a nonraising support step

If

\[
r^{\nu-1}\ne\sigma,
\]

so that the multiplicity remains nu, then the leading Hasse coefficient transforms multiplicatively:

\[
\boxed{
D^{[\nu]}\overline F_{pM}(1)
=
\bigl(r-\sigma r^\nu\bigr)
D^{[\nu]}\overline F_M(1).
}
\]

Hence the pair

\[
\boxed{
\left(
\operatorname{ord}_{x=1}\overline F,
\ D^{[\nu]}\overline F(1)
\right)
}
\]

behaves as a local arithmetic state under support adjunction.

For an exact Legendre resonance the target state is

\[
\boxed{
\left(e,\ \pm(e!)^{-1}\right),
\qquad e=(q-1)/2.
}
\]

## 10. If the leading term cancels

Assume now

\[
r^{\nu-1}=\sigma,
\]

so the order rises above nu. Write

\[
\overline F_M(1+y)=c y^\nu+d y^{\nu+1}+O(y^{\nu+2}).
\]

A direct expansion of the exact support identity gives the next coefficient

\[
\boxed{
[y^{\nu+1}]\overline F_{pM}(1+y)
=
r(r-1)
\left(
-d+\frac{M-\nu}{2}c
\right)
}
\]

in `F_q`, with M read modulo q.

Thus a multiplicity jump by more than one requires an additional exact congruence. Higher jumps require further successive Hasse cancellations.

This produces a genuine valuation filtration on support growth.

## 11. Relation to the q=5 and q=7 operator pictures

The Gaussian and Eisenstein cases can now be viewed from two complementary sides:

1. v13.243-v13.244 describe the **rank-two signal-plane operator ring**;
2. the present entry describes the **x=1 Hasse-valuation state** of the carrier polynomial.

For q=5, exact resonance requires a double root at x=1 modulo 5.

For q=7, exact resonance requires a triple root at x=1 modulo 7.

For every q>=11, an isolated resonance — if one exists — must satisfy increasingly long simultaneous moment cancellation:

\[
\boxed{
q\ge11
\Longrightarrow
\text{at least }(q-1)/2\ge5
\text{ consecutive Hasse conditions.}
}
\]

This is independent of the rank-three obstruction of v13.246 and therefore attacks the isolated-resonance problem from a genuinely different direction.

## 12. What is proved and what is not

Proved exactly:

- exact Legendre resonance forces
  \[
  \operatorname{ord}_{x=1}\overline F=(q-1)/2;
  \]
- all weighted binomial/power moments below that degree vanish modulo q;
- the first nonzero Hasse coefficient has normalized sign `+-1`;
- adjoining a new support prime obeys the exact polynomial identity
  \[
  F_{pM}=F_M\sum_{j=0}^{p-1}x^{jM}-\sigma F_M(x^p);
  \]
- the multiplicity remains nu unless
  \[
  r^{\nu-1}=\sigma;
  \]
- when no rise occurs, the leading Hasse coefficient is multiplied by
  \[
  r-\sigma r^\nu.
  \]

Not proved:

\[
q\ge11\Longrightarrow\text{no exact Legendre resonance}.
\]

The new theorem supplies a much sharper necessary condition for that target, but not yet the final contradiction.

## 13. Next theorem target

The natural next step is to combine the half-order moment conditions with the conductor-Mobius decomposition of v13.234.

For a primitive quadratic discriminant D and fixed extra support S, write the carrier weight

\[
W_{D,S}(n)=\chi_D(n)\prod_{p\in S}\mathbf1_{p\nmid n}.
\]

The required moments are

\[
\sum_{0\le n<M}W_{D,S}(n)n^j.
\]

Because W is periodic on the fixed-support period L, these moments are explicit polynomials in the cofactor h=M/L whose coefficients are finite generalized character moments over one period.

The next question is therefore finite-dimensional and arithmetic:

\[
\boxed{
\text{Can the first }(q-1)/2\text{ moment polynomials vanish simultaneously mod q?}
}
\]

If one can show that for q>=11 these equations are incompatible with a primitive quadratic carrier and its support Euler factors, the isolated-resonance problem closes globally.

## 14. Checkpoint

The research chain is now

\[
\boxed{
\text{exact Legendre resonance}
\Longrightarrow
\text{half-order root at }x=1\pmod q
\Longrightarrow
\text{half-order moment cancellation}
}
\]

alongside the independent universal-span theorem

\[
\boxed{
q\ge11\Longrightarrow\dim V_q\ge3.
}
\]

The Gaussian/Eisenstein mechanism is globally confined to q=5,7, while every hypothetical higher-prime isolated resonance must now pass both a higher-dimensional support-orbit obstruction and a half-order Hasse-moment obstruction.