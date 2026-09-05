# Cone Derivation Ledger v13.250 — Safe-Prime Primitive Half-Order Obstruction

Date: 2026-09-05
Status: EXACT NEW RESULT — continuation of v13.249; research branch remains open

## 0. Synchronization

Immediately before this write, the authoritative README and current `master` tip were re-fetched. The tip remained

`0e2fced1abfb7835fb7d3c4dfd6355bc55923157`

with v13.249 as the highest ledger checkpoint. No newer external-audit entry had landed.

The round-6 correction remains authoritative:

\[
f_{24}=-\ell_7,\qquad f_{240}=+\ell_7=-f_{24}.
\]

## 1. Starting point from v13.249

Let q be an odd crossing prime, put

\[
e=\frac{q-1}{2},
\]

and let \(\chi_D\) be a primitive quadratic character with parity forced by exact resonance:

\[
\chi_D(-1)=\left(\frac{-1}{q}\right).
\]

For fixed extra support S, v13.249 gives

\[
B_{n,\psi_{D,S}}
=
B_{n,\chi_D}
\prod_{p\in S}
\left(1-\chi_D(p)p^{n-1}\right).
\]

Exact Legendre resonance requires

\[
B_{n,\psi_{D,S}}\equiv0\pmod q\quad(1\le n<e),
\qquad
B_{e,\psi_{D,S}}\not\equiv0\pmod q.
\]

For a support prime p, write

\[
r=p\bmod q,\qquad \sigma=\chi_D(p)\in\{\pm1\}.
\]

Its Euler factor kills index n exactly when

\[
\sigma r^{n-1}=1,
\]

and it preserves the target e-th coefficient exactly when

\[
\sigma r^{e-1}\ne1.
\]

v13.249 defined the support-uncoverable indices by

\[
\mathcal U_q
=
\left\{
1\le n<e:
\gcd(2(n-1),q-1)\mid(e-n)
\right\}.
\]

For every \(n\in\mathcal U_q\), exact resonance forces the primitive divisibility

\[
q\mid B_{n,\chi_D}.
\]

## 2. Safe-prime specialization

Assume now that

\[
\boxed{q=2e+1}
\]

is a safe prime with

\[
\boxed{e\ge5\text{ prime}.}
\]

Then q is necessarily congruent to 3 modulo 4, because e is odd. Hence the resonance-parity condition forces

\[
\boxed{\chi_D(-1)=-1.}
\]

Thus \(\chi_D\) is odd. Its generalized Bernoulli numbers satisfy the standard parity vanishing

\[
B_{n,\chi_D}=0
\qquad(n\text{ even}).
\]

The only nontrivial lower Hasse conditions are therefore the odd indices

\[
3,5,\ldots,e-2.
\]

## 3. Every parity-compatible lower index is support-uncoverable

Take an odd integer n with

\[
3\le n\le e-2.
\]

Because e is prime and

\[
0<n-1<e,
\]

we have

\[
\gcd(n-1,e)=1.
\]

Since \(q-1=2e\),

\[
\gcd(2(n-1),q-1)
=
\gcd(2(n-1),2e)
=2.
\]

Both e and n are odd, so e-n is even. Therefore

\[
2\mid(e-n).
\]

Hence every odd lower index belongs to \(\mathcal U_q\):

\[
\boxed{
\mathcal U_q
=
\{3,5,\ldots,e-2\}
\qquad(q=2e+1,\ e\ge5\text{ prime}).
}
\]

The equality is understood on the parity-compatible indices: even indices already vanish identically for the odd primitive character and require no support covering.

## 4. Safe-prime primitive-divisibility theorem

Combining the preceding section with v13.249 gives the exact necessary condition:

\[
\boxed{
q\mid B_{n,\chi_D}
\quad
\text{for every odd }n,\ 3\le n\le e-2.
}
\]

Thus support Euler factors cannot manufacture even one of the nontrivial lower vanishing conditions without also killing the required surviving coefficient at index e.

For safe crossing primes, all nontrivial half-order vanishing must already be present in the primitive quadratic character.

Examples:

\[
\begin{array}{c|c|c}
q&e&\text{forced primitive indices}\\
\hline
11&5&3\\
23&11&3,5,7,9\\
47&23&3,5,7,9,11,13,15,17,19,21\\
59&29&3,5,7,9,11,13,15,17,19,21,23,25,27
\end{array}
\]

These agree with the finite support-uncoverable sets computed in v13.249.

## 5. Stronger polynomial consequence: support cannot create the half-order root

Let the primitive conductor be \(d=|D|\), and define the primitive carrier polynomial

\[
F_d(x)=\sum_{a=0}^{d-1}\chi_D(a)x^a.
\]

For an odd primitive character, parity gives

\[
B_{2m,\chi_D}=0
\]

identically. Under the safe-prime necessary divisibilities of section 4, every generalized Bernoulli number below e vanishes modulo q:

\[
B_{n,\chi_D}\equiv0\pmod q
\qquad(1\le n<e).
\]

Here \(B_{1,\chi_D}\) also requires attention. Since n=1 is not a support-coverable index in the Euler-factor sense: every support factor at n=1 is \(1-\chi_D(p)\). Exact half-order resonance itself forces the induced first coefficient to vanish. If a support prime with \(\chi_D(p)=1\) kills n=1, then at e its factor is \(1-r^{e-1}\). For safe q and any \(r\in\mathbf F_q^\times\), Euler's criterion gives \(r^e=\pm1\); the n=1 case is separate from the odd n>=3 theorem and is not needed for the statement below when the primitive B1 is known to vanish. Therefore the clean universal theorem is stated for the nontrivial indices n>=2, with B1 retained as an explicit condition.

If additionally

\[
B_{1,\chi_D}\equiv0\pmod q,
\]

then the primitive polynomial itself has

\[
\boxed{
\operatorname{ord}_{x=1}\overline F_d(x)\ge e.
}
\]

If moreover

\[
B_{e,\chi_D}\not\equiv0\pmod q,
\]

then

\[
\boxed{
\operatorname{ord}_{x=1}\overline F_d(x)=e.
}
\]

Thus, in the generic safe-prime case where the target primitive coefficient survives, the half-order root is already a primitive-conductor phenomenon; extra support can only preserve or destroy it, not build it progressively out of lower Euler-factor cancellations.

## 6. A cleaner Euler-factor proof of non-coverability

There is a direct group-theoretic proof that exposes why safe primes are rigid.

Suppose a support prime p kills an odd lower index n:

\[
\sigma r^{n-1}=1.
\]

Because n-1 is even, write n-1=2a with \(1\le a<(e-1)/2\). Since e is prime,

\[
\gcd(a,e)=1.
\]

Squaring away the sign gives

\[
r^{2(n-1)}=1.
\]

The order of r divides \(q-1=2e\) and also divides \(2(n-1)\). Their gcd is 2, so

\[
r^2=1,
\qquad r=\pm1.
\]

Because n-1 is even,

\[
r^{n-1}=1,
\]

so \(\sigma=1\). But e-1 is also even, hence

\[
\sigma r^{e-1}=1.
\]

Therefore the same support prime necessarily kills the target e-th coefficient.

So:

\[
\boxed{
\text{At a safe crossing prime }q=2e+1,
\text{ every support prime that kills a nontrivial lower odd index also kills index }e.
}
\]

This is the local form of the safe-prime obstruction.

## 7. Relation to quadratic irregularity

The forced conditions

\[
q\mid B_{3,\chi_D},
\quad
q\mid B_{5,\chi_D},
\quad\ldots\quad,
q\mid B_{e-2,\chi_D}
\]

are simultaneous generalized Bernoulli divisibilities for a single primitive quadratic character.

Equivalently, using

\[
L(1-n,\chi_D)=-\frac{B_{n,\chi_D}}{n},
\]

and since \(n<q\), exact resonance requires

\[
\boxed{
L(1-n,\chi_D)\equiv0\pmod q
\quad
\text{for every odd }3\le n\le e-2,
}
\]

with the usual interpretation after clearing denominators prime to q.

Thus a safe-prime resonance would require a whole consecutive parity block of generalized irregular pairs for the same quadratic character, not a single accidental divisibility.

For q=47 this is ten simultaneous nontrivial primitive divisibilities; for q=59 it is thirteen.

This does not by itself prove impossibility, but it drastically narrows the arithmetic doorway.

## 8. Second step: support depth becomes irrelevant to the lower vanishing problem

The safe-prime theorem changes the architecture of the search.

For general q, one must solve a covering problem: some lower Bernoulli zeros may come from the primitive character and others from support Euler factors.

For safe q=2e+1 with e prime, there is no such mixed covering problem at the parity-compatible lower indices. Every nontrivial lower odd zero must be primitive.

Therefore the search separates into two stages:

1. **primitive gate** — find a primitive odd quadratic \(\chi_D\) satisfying
   \[
   q\mid B_{3,\chi_D},B_{5,\chi_D},\ldots,B_{e-2,\chi_D};
   \]
2. **support/signature gate** — only after passing the primitive gate can support S and cofactor h be considered, subject to
   \[
   B_{e,\psi_{D,S}}\ne0,
   \qquad
   hC_{D,S,q}=\pm1.
   \]

So for safe primes the infinite support graph is irrelevant until after a finite primitive-character obstruction has been passed.

This is a major reduction in the isolated-resonance problem.

## 9. What is proved and what remains open

Proved exactly:

- for safe q=2e+1 with e>=5 prime, q is 3 mod 4 and the resonance character must be odd;
- every nontrivial parity-compatible lower index \(3,5,\ldots,e-2\) is support-uncoverable;
- exact resonance therefore forces simultaneous primitive divisibility by q of all \(B_{n,\chi_D}\) in that range;
- any support Euler factor that kills one of those lower indices necessarily kills the target index e as well;
- consequently support cannot solve the lower half-order vanishing problem at safe primes.

Not proved:

\[
\text{No primitive quadratic character can satisfy the entire safe-prime divisibility block.}
\]

That is now the sharp next target.

## 10. Next theorem target

The natural next attack is to study the simultaneous primitive congruences through the finite-field power-sum representation of generalized Bernoulli numbers.

For q not dividing d and n<q, one can rewrite \(B_{n,\chi_D}\bmod q\) in terms of the weighted power sums

\[
\sum_{a=1}^{d}\chi_D(a)a^j.
\]

At a safe prime, requiring every odd Bernoulli index below e to vanish should force a large collection of odd moments of the primitive character polynomial to vanish simultaneously.

The key question is whether this forces a stronger algebraic divisibility of \(F_d(x)\) modulo q — potentially enough to contradict the nonzero e-th signature or the quadratic-character structure itself.

The research frontier is therefore now:

\[
\boxed{
\text{safe }q
\Longrightarrow
\text{primitive half-order block}
\Longrightarrow
\text{seek a finite-field rigidity contradiction.}
}

This is strictly narrower than the support-covering problem of v13.249.