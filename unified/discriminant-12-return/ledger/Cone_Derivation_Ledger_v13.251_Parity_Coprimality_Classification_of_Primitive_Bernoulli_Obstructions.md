# Cone Derivation Ledger v13.251 — Parity-Coprimality Classification of Primitive Bernoulli Obstructions

Date: 2026-09-05
Status: EXACT NEW RESULT — continuation of v13.249–v13.250; research branch remains open

## 0. Synchronization

Immediately before this write, the authoritative project README and current `master` tip were re-fetched. The tip remained

`5f641374299d7ad4f1d7506e626a70a1ac13b150`

with `v13.250` as the highest ledger checkpoint. No newer external-audit checkpoint had landed.

The round-6 correction remains authoritative:

\[
f_{24}=-\ell_7,
\qquad
f_{240}=+\ell_7=-f_{24}.
\]

## 1. Question

v13.249 introduced the support-uncoverable lower-index set

\[
\mathcal U_q
=
\left\{
1\le n<e:
 n\equiv e\pmod2,
\ \gcd(2(n-1),q-1)\mid(e-n)
\right\},
\qquad
 e=\frac{q-1}{2},
\]

and proved that every exact Legendre resonance forces

\[
q\mid B_{n,\chi_D}
\qquad(n\in\mathcal U_q).
\]

v13.250 specialized this to safe primes `q=2e+1` with `e` prime and found that every nontrivial parity-compatible lower index is uncoverable.

The present entry solves the support-uncoverability criterion exactly for **every** odd prime `q>=5`, with no safe-prime assumption.

The result is unexpectedly simple:

\[
\boxed{
 n\in\mathcal U_q
 \iff
 n\equiv e\pmod2
 \text{ and }
 \gcd(n-1,e)=1.
}
\]

Thus the unavoidable primitive generalized-Bernoulli obstructions are indexed precisely by parity-compatible shifts `n-1` that are units modulo the half-order `e=(q-1)/2`.

## 2. Parity of the primitive quadratic character

Exact centered Legendre resonance forces

\[
\chi_D(-1)=\left(\frac{-1}{q}\right)=(-1)^e.
\]

Generalized Bernoulli parity gives

\[
B_{n,\chi_D}=0
\qquad
\text{whenever }
(-1)^n\ne\chi_D(-1).
\]

Therefore only indices satisfying

\[
\boxed{n\equiv e\pmod2}
\]

can carry a nontrivial primitive Bernoulli obstruction.

All parity-incompatible lower Hasse conditions vanish identically and need no support explanation.

Hence throughout the rest of this entry `n` is assumed parity-compatible:

\[
1\le n<e,
\qquad
n\equiv e\pmod2.
\]

## 3. Collapse of the v13.249 support-uncoverability criterion

Set

\[
g:=\gcd(n-1,e).
\]

Because

\[
q-1=2e,
\]

we have the exact gcd identity

\[
\gcd(2(n-1),q-1)
=
\gcd(2(n-1),2e)
=2g.
\]

The v13.249 uncoverability criterion is therefore

\[
2g\mid(e-n).
\]

Now use the definition of `g`. Since

\[
g\mid e
\qquad\text{and}\qquad
g\mid(n-1),
\]

we have

\[
e-n
=e-(n-1)-1
\equiv -1\pmod g.
\]

Consequently

\[
g\mid(e-n)
\iff
g=1.
\]

On the other hand, because `n` and `e` have the same parity,

\[
2\mid(e-n).
\]

Thus:

- if `g=1`, then `2g=2` divides `e-n`;
- if `g>1`, then `g` does not divide `e-n`, so `2g` cannot divide `e-n`.

Therefore the general criterion collapses exactly to

\[
\boxed{
\gcd(2(n-1),q-1)\mid(e-n)
\iff
\gcd(n-1,e)=1
}
\]

for every parity-compatible lower index.

Hence:

\[
\boxed{
\mathcal U_q
=
\left\{
1\le n<e:
 n\equiv e\pmod2,
\ \gcd(n-1,e)=1
\right\}.
}
\]

This is the **parity-coprimality classification**.

## 4. Exact support-coverability criterion

The complement among parity-compatible lower indices is equally simple.

A parity-compatible index can be killed by some support Euler factor while preserving the target `e`-th coefficient if and only if

\[
\boxed{\gcd(n-1,e)>1.}
\]

Thus the support problem has a purely arithmetic interpretation:

\[
\boxed{
\text{unit shift }n-1\pmod e
\Longrightarrow
\text{primitive zero forced},
}
\]

whereas

\[
\boxed{
	ext{nonunit shift }n-1\pmod e
\Longrightarrow
\text{support covering is locally possible}.
}
\]

The existence statement is exactly the negation of the v13.249 subgroup obstruction; no claim is made that all coverable indices can be realized simultaneously by one finite support set without further compatibility conditions.

## 5. Global primitive-divisibility theorem

Combining the classification with v13.249 yields the exact necessary condition for any isolated exact Legendre resonance:

\[
\boxed{
q\mid B_{n,\chi_D}
\quad
\text{for every }1\le n<e
\text{ such that }
 n\equiv e\pmod2,
\ \gcd(n-1,e)=1.
}
\]

Equivalently, defining

\[
\boxed{
\mathcal P_q
:=
\{n:1\le n<e,\ n\equiv e\pmod2,\ \gcd(n-1,e)=1\},
}
\]

we have

\[
\boxed{
\mathcal P_q=\mathcal U_q,
\qquad
q\mid B_{n,\chi_D}
\quad(n\in\mathcal P_q).
}
\]

The notation `P_q` emphasizes that these are the lower indices that must vanish **primitively**, independently of all support engineering.

## 6. Exact cardinality

The number of forced primitive congruences can now be counted in closed form.

### 6.1 `e` even (`q\equiv1 mod 4`)

Parity compatibility requires `n` even, so

\[
m:=n-1
\]

is odd. Every unit modulo even `e` is odd.

The range `1<=n<e` corresponds to

\[
0\le m\le e-2.
\]

The value `m=0` is not a unit, while `m=e-1` is a unit but corresponds to the excluded target index `n=e`.

Therefore all units modulo `e` except `e-1` occur exactly once, and

\[
\boxed{
|\mathcal U_q|=\varphi(e)-1
\qquad(e\text{ even}).
}
\]

### 6.2 `e` odd (`q\equiv3 mod 4`)

Parity compatibility requires `n` odd, hence `m=n-1` is even.

Among the `\varphi(e)` units modulo odd `e`, pairing

\[
u\longleftrightarrow e-u
\]

switches parity. Hence exactly half of the units are even.

The even unit `m=e-1` corresponds to the excluded target index `n=e`, so

\[
\boxed{
|\mathcal U_q|=\frac{\varphi(e)}2-1
\qquad(e\text{ odd}).
}
\]

Thus the exact obstruction count is

\[
\boxed{
N(q):=|\mathcal U_q|
=
\begin{cases}
\varphi(e)-1,&e\text{ even},\\[4pt]
\dfrac{\varphi(e)}2-1,&e\text{ odd},
\end{cases}
\qquad e=\frac{q-1}{2}.
}
\]

## 7. q=5 and q=7 are uniquely obstruction-free

For `q=5`,

\[
e=2,
\qquad
N(5)=\varphi(2)-1=0.
\]

For `q=7`,

\[
e=3,
\qquad
N(7)=\frac{\varphi(3)}2-1=0.
\]

Now let `q>=11`, so `e>=5`.

If `e` is odd, then `\varphi(e)>=4`, hence

\[
N(q)=\frac{\varphi(e)}2-1\ge1.
\]

If `e` is even, then `e>=6` and `\varphi(e)>=2`, hence

\[
N(q)=\varphi(e)-1\ge1.
\]

Therefore:

\[
\boxed{
N(q)=0
\iff
q\in\{5,7\}.
}
\]

Equivalently:

\[
\boxed{
q\ge11
\Longrightarrow
\text{every exact resonance forces at least one nontrivial primitive generalized-Bernoulli divisibility.}
}
\]

This is now a global theorem, not merely the low-index `B_2` / `B_3` corollary of v13.249.

## 8. Recovery of the universal first obstruction

The parity-coprimality theorem immediately recovers the universal low-index statements.

### `q\equiv1 mod4`

Then `e` is even. The first active index is `n=2`, and

\[
\gcd(1,e)=1.
\]

Hence

\[
\boxed{2\in\mathcal U_q}
\]

and every exact resonance requires

\[
\boxed{q\mid B_{2,\chi_D}.}
\]

### `q\equiv3 mod4`, `q>=11`

Then `e` is odd. The first nontrivial active index is `n=3`, and

\[
\gcd(2,e)=1.
\]

Hence

\[
\boxed{3\in\mathcal U_q}
\]

and every exact resonance requires

\[
\boxed{q\mid B_{3,\chi_D}.}
\]

The earlier corollaries are therefore the first members of the complete unit-shift family.

## 9. Safe primes become the maximal-obstruction case

Suppose `q=2e+1` is safe with `e>=5` prime.

For every lower parity-compatible index other than the special `n=1` issue in the odd case, one has

\[
0<n-1<e
\]

and therefore

\[
\gcd(n-1,e)=1.
\]

Thus v13.250 is recovered immediately: every nontrivial parity-compatible lower index is primitive-forced.

The safe-prime theorem is therefore not an isolated phenomenon; it is the **maximal unit-density case** of the general parity-coprimality classification.

For prime `e`, essentially every admissible lower shift is a unit modulo `e`.

## 10. First exact sets and counts

The classification gives:

\[
\begin{array}{c|c|c|c}
q&e&\mathcal U_q&N(q)\\
\hline
5&2&\varnothing&0\\
7&3&\varnothing&0\\
11&5&\{3\}&1\\
13&6&\{2\}&1\\
17&8&\{2,4,6\}&3\\
19&9&\{3,5\}&2\\
23&11&\{3,5,7,9\}&4\\
29&14&\{2,4,6,10,12\}&5\\
31&15&\{3,5,9\}&3\\
37&18&\{2,6,8,12,14\}&5\\
41&20&\{2,4,8,10,12,14,18\}&7\\
43&21&\{3,5,9,11,17\}&5\\
47&23&\{3,5,7,9,11,13,15,17,19,21\}&10
\end{array}
\]

These values agree with the earlier finite sets recorded in v13.249 and with an independent exact arithmetic audit performed before this write.

## 11. A second global q=5/q=7 dichotomy

v13.246 proved the universal support-span classification

\[
\boxed{
\dim_{\mathbf Q}V_q\le2
\iff
q\in\{5,7\}.
}
\]

The present theorem independently proves

\[
\boxed{
N(q)=0
\iff
q\in\{5,7\}.
}
\]

Thus the same two crossing primes are exceptional in two genuinely different senses:

1. **signal-space exception:** only `q=5,7` have universal centered-Legendre support span of dimension two;
2. **primitive-arithmetic exception:** only `q=5,7` require no unavoidable lower primitive Bernoulli divisibility.

This parallel is structurally striking but must not be conflated into an equivalence. The two theorems arise from different invariants and neither has been shown to imply the other.

The correct statement is:

\[
\boxed{
q=5,7
\text{ are simultaneously the unique rank-two primes and the unique primitive-obstruction-free primes.}
}
\]

## 12. Density interpretation

The number of unavoidable primitive congruences is controlled by the unit density of the half-order `e`.

For `e` even,

\[
N(q)=\varphi(e)-1.
\]

For `e` odd,

\[
N(q)=\frac{\varphi(e)}2-1.
\]

Thus highly composite `e` reduce the number of primitive-forced indices because more lower shifts are nonunits and may, in principle, be covered by support Euler factors.

Conversely, prime or nearly-prime `e` produce large primitive obstruction blocks.

This identifies the arithmetic of

\[
\boxed{e=(q-1)/2}
\]

as the exact combinatorial controller of support flexibility.

## 13. What is proved and what remains open

Proved exactly in this entry:

- for every odd prime `q>=5`, among parity-compatible lower indices,
  \[
  n\in\mathcal U_q\iff\gcd(n-1,e)=1;
  \]
- support-coverability is locally possible exactly at the complementary nonunit shifts;
- every unit-shift lower index forces primitive generalized-Bernoulli divisibility;
- the exact number of primitive-forced indices is
  \[
  \varphi(e)-1
  \]
  for even `e`, and
  \[
  \varphi(e)/2-1
  \]
  for odd `e`;
- `q=5,7` are exactly the primes with zero unavoidable primitive lower Bernoulli congruences;
- every `q>=11` forces at least one such primitive congruence;
- the safe-prime theorem of v13.250 is the maximal-obstruction special case.

Not proved:

\[
q\ge11\Longrightarrow\text{no exact Legendre resonance}.
\]

Primitive generalized-Bernoulli divisibility can occur, so the existence of at least one forced primitive congruence is not itself a contradiction.

Also not proved: simultaneous local coverability of all nonunit-shift indices by one globally realizable support set. That is a separate compatibility problem.

## 14. Next theorem target

The remaining lower-index conditions now split canonically into two classes:

\[
\boxed{
\text{unit shifts}
\quad\leftrightarrow\quad
\text{forced primitive Bernoulli zeros},
}
\]

and

\[
\boxed{
\text{nonunit shifts}
\quad\leftrightarrow\quad
\text{potential support-covering problem}.
}
\]

The next natural target is to classify **simultaneous support covering** on the nonunit shifts while preserving the target coefficient at `e`.

Because each support prime contributes a local label

\[
(r,\sigma)\in\mathbf F_q^\times\times\{\pm1\},
\]

and kills exactly the indices satisfying

\[
\sigma r^{n-1}=1,
\]

this becomes a finite set-cover problem in the divisor lattice of `e`, coupled to the surviving `e`-th Euler factor.

If one can derive a lower bound on the primitive-forced set plus the minimum support needed to cover the complementary set, and then combine that with the Hasse-signature / cofactor restriction, the isolated-resonance classification may become finite for each `q`.

## 15. Checkpoint

The Bernoulli branch now has the exact structure

\[
\boxed{
\text{exact resonance}
\Longrightarrow
\begin{cases}
q\mid B_{n,\chi_D},&\gcd(n-1,e)=1,\\
\text{support cover required or primitive zero},&\gcd(n-1,e)>1,
\end{cases}
}
\]

for parity-compatible `1<=n<e`, with

\[
\boxed{e=(q-1)/2.}
\]

The exceptional-prime picture has now sharpened to

\[
\boxed{
q=5,7
\iff
\text{no unavoidable primitive lower Bernoulli obstruction},
}
\]

in exact parallel with the independent rank-two support-span theorem.