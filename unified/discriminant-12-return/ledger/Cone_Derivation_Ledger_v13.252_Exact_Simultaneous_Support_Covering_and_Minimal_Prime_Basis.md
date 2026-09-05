# Cone Derivation Ledger v13.252 — Exact Simultaneous Support Covering and Minimal Prime Basis

Date: 2026-09-05
Status: EXACT NEW RESULT — continuation of v13.249–v13.251; research branch remains open

## 0. Synchronization

Immediately before this write, the authoritative project README and current `master` tip were re-fetched. The tip remained

`d9540fef6bef7a8688e84a9a8f9079b20dae2531`

with `v13.251` as the highest ledger checkpoint. No newer external-audit checkpoint had landed.

The round-6 correction remains authoritative:

\[
f_{24}=-\ell_7,
\qquad
f_{240}=+\ell_7=-f_{24}.
\]

## 1. Question

v13.251 proved that, for

\[
e=\frac{q-1}{2},
\]

and every parity-compatible lower index

\[
1\le n<e,
\qquad
n\equiv e\pmod2,
\]

support can kill the `n`-th induced generalized-Bernoulli coefficient while preserving the target index `e` if and only if

\[
\gcd(n-1,e)>1.
\]

What remained open was simultaneous realization: can all such nonunit-shift indices be covered by one finite support set, and if so what is the minimum number of support primes required?

This entry solves that problem exactly.

## 2. Local kill sets of one support label

For a new support prime `P`, write

\[
r=P\pmod q,
\qquad
\sigma=\chi_D(P)\in\{\pm1\}.
\]

Its Euler factor at index `n` is

\[
1-\sigma r^{n-1}.
\]

Thus it kills index `n` exactly when

\[
\sigma r^{n-1}=1,
\]

while preserving the target coefficient exactly when

\[
\sigma r^{e-1}\ne1.
\]

Let `d=ord_q(r)`, so `d|2e`.

If `sigma=+1`, the killed shifts `m=n-1` satisfy

\[
m\equiv0\pmod d.
\]

If `sigma=-1`, then `d` must be even and the killed shifts satisfy

\[
m\equiv d/2\pmod d.
\]

Now restrict to the parity-compatible lower indices. Their shifts `m=n-1` have parity opposite to `e`.

A direct parity reduction shows that every nonempty target-safe kill set has the form

\[
\boxed{
K_g
=
\{n:1\le n<e,\ n\equiv e\pmod2,\ g\mid(n-1)\},
}
\]

for an odd divisor

\[
\boxed{g>1,\qquad g\mid e.}
\]

Conversely every such `K_g` is realized by a local label: choose `r` of exact order `g` and take `sigma=+1`. Then

\[
r^{n-1}=1
\iff
g\mid(n-1),
\]

while

\[
r^{e-1}\ne1
\]

because `g|e` but `g\nmid e-1`.

Hence:

\[
\boxed{
\text{The target-safe single-prime kill sets are exactly the divisor classes }K_g
\text{ with odd }g>1\mid e.
}
\]

This turns the simultaneous support problem into the divisor lattice of the odd part of `e`.

## 3. Maximal kill classes are indexed by odd prime divisors of e

If `g` is composite and `p|g` is prime, then

\[
K_g\subseteq K_p.
\]

Therefore the maximal useful kill classes are exactly

\[
\boxed{K_p\qquad(p\mid e,\ p\text{ odd prime}).}
\]

Every parity-compatible nonunit shift satisfies

\[
\gcd(n-1,e)>1.
\]

Because `n-1` has parity opposite to `e`, this common divisor contains an odd prime `p|e`. Therefore

\[
p\mid(n-1),
\]

so

\[
n\in K_p.
\]

Thus the union of the prime-divisor classes covers every support-coverable lower index:

\[
\boxed{
\bigcup_{p\mid e,\ p\text{ odd prime}}K_p
=
\{n:1\le n<e,\ n\equiv e\pmod2,\ \gcd(n-1,e)>1\}.
}
\]

So simultaneous local covering is always possible.

## 4. Global realization by actual rational primes

The preceding construction used local labels `(r,+1)`. These labels are globally realizable by actual new support primes.

Since exact resonance requires `q\nmid M`, and the primitive conductor `d=|D|` divides `M`, we have

\[
\gcd(q,d)=1.
\]

Fix an odd prime divisor `p|e`. Choose `r_p in F_q^*` of exact order `p`.

Choose the residue class

\[
a\equiv1\pmod d,
\qquad
a\equiv r_p\pmod q.
\]

By CRT this defines a class modulo `dq`, coprime to `dq`. Dirichlet's theorem gives infinitely many rational primes `P_p` in this class. For every such prime,

\[
P_p\equiv r_p\pmod q,
\qquad
\chi_D(P_p)=\chi_D(1)=+1.
\]

Therefore its Euler factor kills exactly `K_p` and preserves the target index `e`.

Hence:

\[
\boxed{
\text{Every maximal local kill class }K_p
\text{ is realized by infinitely many genuine support primes.}
}
\]

In particular, the simultaneous covering construction has no hidden CRT or character-compatibility obstruction.

## 5. Exact minimum number of support primes

Let

\[
e_{\rm odd}=\frac{e}{2^{v_2(e)}}
\]

be the odd part of `e`, and let

\[
\omega(e_{\rm odd})
\]

denote its number of distinct prime factors.

The construction above uses one support prime for each odd prime divisor of `e`, so

\[
N_{\rm supp}(q)\le\omega(e_{\rm odd}).
\]

We now prove the matching lower bound.

### 5.1 e even

For each odd prime `p|e`, the lower index

\[
n_p=p+1
\]

is parity-compatible and satisfies `n_p<e`. Its shift is

\[
n_p-1=p.
\]

Any target-safe kill class containing `n_p` is `K_g` with odd `g>1|e` and `g|p`; hence necessarily

\[
g=p.
\]

So the witnesses `n_p` for distinct odd primes require distinct support kill classes.

### 5.2 e odd and composite

For each prime `p|e`, take

\[
n_p=2p+1.
\]

Because `e` is odd composite, `e\ge3p` for each prime divisor after choosing the complementary factor at least `3`, so

\[
2p+1<e.
\]

This index is parity-compatible and its shift is `2p`. Any odd divisor `g>1|e` satisfying `g|2p` must be `g=p`. Again distinct prime divisors force distinct support classes.

### 5.3 e odd prime

Then the only parity-compatible support-coverable lower index is `n=1`, and the only odd divisor `g>1|e` is `g=e`. Exactly one support prime is required if that index needs support killing. Since `omega(e)=1`, the same formula holds.

Therefore:

\[
\boxed{
N_{\rm supp}^{\min}(q)=\omega(e_{\rm odd}).
}
\]

This is the exact minimum number of target-safe support primes required to cover every support-coverable parity-compatible lower index.

## 6. Power-of-two half-order rigidity

If

\[
e=2^a,
\]

then

\[
e_{\rm odd}=1,
\qquad
\omega(e_{\rm odd})=0.
\]

Hence there are no support-coverable parity-compatible lower indices at all:

\[
\boxed{
\gcd(n-1,e)=1
\quad
\text{for every parity-compatible }1\le n<e.
}
\]

Thus every nontrivial lower Hasse zero must already be primitive.

For prime `q=2e+1`, this includes the Fermat-prime-type cases such as

\[
q=17,257,65537,
\]

whenever prime.

This is a second maximal-rigidity family, complementary to the safe-prime family of v13.250.

## 7. Exact Hasse-multiplicity realization criterion

Let `chi_D` be a primitive quadratic character with the parity forced by `q`, and assume

\[
B_{e,\chi_D}\not\equiv0\pmod q.
\]

Then there exists a finite support set `S`, disjoint from the primitive conductor and from `q`, such that the induced character satisfies

\[
B_{n,\psi_{D,S}}\equiv0\pmod q
\qquad(1\le n<e)
\]

and

\[
B_{e,\psi_{D,S}}\not\equiv0\pmod q
\]

if and only if

\[
\boxed{
B_{n,\chi_D}\equiv0\pmod q
\quad
\text{for every parity-compatible }n<e
\text{ with }\gcd(n-1,e)=1.
}
\]

Proof.

Necessity is exactly v13.251.

For sufficiency:

- parity-incompatible indices already vanish identically;
- parity-compatible unit shifts vanish primitively by hypothesis;
- every parity-compatible nonunit shift is killed by at least one class `K_p` with `p|e` odd;
- choose one globally realizable support prime for each odd prime divisor of `e` as in section 4;
- every chosen support factor is nonzero at index `e`, so the nonzero primitive target coefficient remains nonzero.

Therefore the lower Hasse-multiplicity problem is completely classified.

Equivalently:

\[
\boxed{
\operatorname{ord}_{x=1}\overline F_{L}=e
}
\]

can be achieved by support extension if and only if the primitive character has precisely the unavoidable unit-shift Bernoulli zeros and a surviving `e`-th coefficient.

This is a statement about the Hasse multiplicity only; it does not by itself imply exact Legendre folding or the full crossing-signal autocorrelation condition.

## 8. Clarification of the v13.250 B1 discussion

For safe primes `q=2e+1` with `e` odd prime, v13.250 correctly proved that every nontrivial odd lower index

\[
3,5,\ldots,e-2
\]

must vanish primitively.

The special index `n=1` is different: its shift is `0`, so

\[
\gcd(0,e)=e>1.
\]

It is support-coverable. A support prime with `chi_D(P)=+1` and residue of order `e` modulo `q` kills `n=1` while preserving the target index `e`.

Thus the sentence in v13.250 section 5 suggesting all indices below `e` vanish primitively should be read with the explicit `B_1` caveat stated immediately afterward. The exact corrected formulation is:

\[
\boxed{
B_{n,\chi_D}\equiv0\pmod q
\quad
\text{for all odd }3\le n\le e-2,
}
\]

while `B_1` may be killed by one target-safe support prime.

No theorem from v13.250 concerning the nontrivial indices is changed.

## 9. Examples

### q=13

Here

\[
e=6=2\cdot3.
\]

The primitive-forced set is

\[
\{2\},
\]

while the support-coverable set is

\[
\{4\}.
\]

Since `e_odd=3`, exactly one support prime is necessary and sufficient. Choose residue order `3` and character value `+1`.

### q=17

Here

\[
e=8.
\]

The odd part is `1`, so

\[
N_{\rm supp}^{\min}=0.
\]

All active lower indices

\[
2,4,6
\]

are primitive-forced.

### q=31

Here

\[
e=15=3\cdot5.
\]

The primitive-forced indices are

\[
\{3,5,9\},
\]

and the support-coverable indices are

\[
\{1,7,11,13\}.
\]

Two support primes are necessary and sufficient:

- one residue-order-3, character-`+1` prime kills `n=1,7,13`;
- one residue-order-5, character-`+1` prime kills `n=1,11`.

Their union covers the entire nonunit set and neither kills the target `n=e=15`.

### q=43

Here

\[
e=21=3\cdot7.
\]

Again

\[
N_{\rm supp}^{\min}=2.
\]

The order-3 class covers

\[
\{1,7,13,19\},
\]

and the order-7 class covers

\[
\{1,15\}.
\]

Together they cover every nonunit lower shift.

## 10. Structural consequence

The lower Hasse problem is no longer an open set-cover problem. It is solved exactly:

\[
\boxed{
\text{unit shifts}\longrightarrow\text{primitive Bernoulli zeros},
}
\]

\[
\boxed{
\text{nonunit shifts}\longrightarrow\text{support classes indexed by odd primes }p|e,
}
\]

and

\[
\boxed{
\text{minimum support size}=\omega(e_{\rm odd}).
}
\]

Thus all remaining obstruction to half-order Hasse multiplicity is primitive arithmetic.

Support contributes only a completely classified divisor-lattice correction.

## 11. What is proved and what remains open

Proved exactly:

- every target-safe single-support kill set is `K_g` for an odd divisor `g>1|e`;
- maximal kill classes are `K_p` for odd prime divisors `p|e`;
- all nonunit-shift indices are simultaneously coverable;
- every such local class is globally realizable by infinitely many actual rational primes using CRT plus Dirichlet;
- the exact minimum number of support primes is `omega(e_odd)`;
- if `e` is a power of two, support has no lower-index freedom at all;
- the Hasse-multiplicity condition is realizable by some finite support set if and only if all parity-compatible unit-shift primitive Bernoulli numbers vanish modulo `q` and the primitive `e`-th coefficient survives;
- the `B_1` caveat in v13.250 is now resolved exactly.

Still open:

\[
q\ge11\Longrightarrow\text{no exact Legendre resonance}.
\]

The present theorem closes the support-covering part of the Hasse problem, but exact resonance also requires the precise leading Hasse signature, the folded values `0,\pm1`, and the two-level Legendre autocorrelation.

## 12. Next theorem target

Because support covering is now completely classified, the next obstruction should attack the primitive criterion itself:

\[
B_{n,\chi_D}\equiv0\pmod q
\quad
\text{for every parity-compatible unit shift }n-1\in(\mathbf Z/e\mathbf Z)^\times.
\]

A promising reformulation is through the primitive character polynomial

\[
F_d(x)=\sum_{a\bmod d}\chi_D(a)x^a
\]

or through the special values

\[
L(1-n,\chi_D).
\]

The goal is to determine whether simultaneous vanishing on the unit-shift set forces additional vanishing at the target index `e`, or an incompatible symmetry of the primitive quadratic character.

If such a theorem holds, then the now-complete support classification would immediately upgrade it to a global no-resonance theorem.

## 13. Checkpoint

The Bernoulli/Hasse branch now has the exact architecture

\[
\boxed{
\text{primitive unit-shift obstruction}
\ +\ 
\text{explicit odd-prime divisor support basis}
\ +\ 
\text{two-state/cofactor leading signature}.
}
\]

The middle term is now completely solved.