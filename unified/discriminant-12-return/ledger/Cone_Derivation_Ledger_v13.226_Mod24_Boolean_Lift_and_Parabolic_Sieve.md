# Cone Derivation Ledger v13.226 — mod-24 Boolean Lift and Parabolic Sieve

Date: 2026-09-04
Status: EXACT RESEARCH RESULT — downstream of v13.225; research branch remains open

## 0. Pre-write synchronization

Immediately before this write, the current `master` tree and authoritative project README were re-fetched. The tree tip was still

`0fd180c3bba8f30ab7b5ad00bdb9eed27716a779`

with v13.225 as the highest ledger checkpoint. No newer external-audit ledger entry had landed. The active scope remains `unified/discriminant-12-return/` only.

## 1. The eight admissible positions in a 24-block

Every prime `p>3` is coprime to `24`, hence lies in

\[
U(24)=\{1,5,7,11,13,17,19,23\}.
\]

Thus every block

\[
24k+1,\ldots,24k+24
\]

contains exactly eight residue positions that are not automatically excluded by divisibility by `2` or `3`:

\[
\boxed{24k+r,\qquad r\in U(24).}
\]

Since

\[
\varphi(24)=8,
\]

the exact `2,3`-wheel carrier density is

\[
\boxed{\frac{8}{24}=\frac13.}
\]

This is an admissibility ceiling, not the actual prime density.

## 2. Exact two-sheeted lift of the mod-12 V4 carrier

Reduction modulo 12 gives a surjective group homomorphism

\[
\pi:U(24)\to U(12),
\qquad [a]_{24}\mapsto[a]_{12}.
\]

Its fibers are

\[
\boxed{
1\leftarrow\{1,13\},\quad
5\leftarrow\{5,17\},\quad
7\leftarrow\{7,19\},\quad
11\leftarrow\{11,23\}.}
\]

The kernel is

\[
\ker\pi=\{1,13\}\cong C_2.
\]

The subset

\[
\{1,5,7,11\}\subset U(24)
\]

is itself a subgroup mapping isomorphically onto `U(12)`. Therefore the exact sequence splits and

\[
\boxed{U(24)\cong U(12)\times C_2\cong C_2^3.}
\]

Equivalently, the eight mod-24 prime-admissible positions form a Boolean cube whose quotient by the extra sheet bit is the four-state mod-12 carrier

\[
\boxed{U(12)\cong V_4\cong C_2^2.}
\]

This is an exact group-theoretic lift, not merely a visual doubling.

## 3. Divisor rows as exact Cone crossing tests

Fix an admissible integer

\[
N=24k+r,\qquad r\in U(24).
\]

For a prime `q>=5`,

\[
q\mid N
\]

iff the constant-product shell

\[
xy=N
\]

meets the integer row

\[
y=q
\]

at the lattice point

\[
\left(\frac Nq,q\right).
\]

Under Paper A's map, every fixed row `y=q` is one of the row parabolas. Thus:

\[
\boxed{
q\mid N
\Longleftrightarrow
\text{the }N\text{-shell has an integer crossing on the }q\text{-row parabola}.}
\]

This gives a precise meaning to the phrase `parabolic crossing` in the sieve discussion. It is not a new primality criterion; it is the ordinary divisor test expressed in the established Cone geometry.

For `N>1`, primality is equivalent to the absence of such integer crossings for every prime

\[
q\le\sqrt N.
\]

## 4. Periodic crossing schedule on the eight-state carrier

For fixed prime `q>=5` and fixed slot `r\in U(24)`, a crossing occurs when

\[
24k+r\equiv0\pmod q.
\]

Since `(24,q)=1`, `24` has an inverse modulo `q`, giving the unique congruence class

\[
\boxed{
k\equiv-r\,24^{-1}\pmod q.}
\]

Therefore each prime `q>=5` produces, on each of the eight slots, one crossing every `q` consecutive 24-blocks.

**[D] Periodic parabolic-sieve theorem.** For every fixed prime `q>=5` and every fixed mod-24 carrier slot `r`, the `q`-row parabola strikes that slot in exactly one block-index class modulo `q`.

Across `q` consecutive 24-blocks there are `8q` carrier positions, and exactly `8` of them are divisible by `q`. Hence the `q`-sieve removes exactly the fraction

\[
\boxed{\frac1q}
\]

of the mod-24 carrier over a complete `q`-block supercycle.

## 5. Successive crossing percentages are the wheel-sieve product

Let

\[
P=\prod_{q\in\mathcal Q}q
\]

be a squarefree product of primes `q>=5`. Across `P` consecutive 24-blocks there are

\[
8P
\]

positions surviving the initial `2,3` wheel.

By the Chinese remainder theorem, the positions surviving all additional divisor filters `q\in\mathcal Q` are exactly the residue classes coprime to

\[
24P.
\]

Their number is

\[
\varphi(24P)
=8\prod_{q\in\mathcal Q}(q-1).
\]

Therefore the exact surviving fraction relative to the eight-state carrier is

\[
\boxed{
\frac{\varphi(24P)}{8P}
=
\prod_{q\in\mathcal Q}\left(1-\frac1q\right).}
\]

Relative to all integers, the exact wheel density is

\[
\boxed{
\frac13
\prod_{q\in\mathcal Q}\left(1-\frac1q\right).}
\]

This rigorously captures the user's intuition that later divisor/parabolic crossings remove a percentage of the initial mod-24 carrier. The percentage statement is exact only over the complete CRT supercycle; individual 24-blocks fluctuate and need not lose candidates monotonically from one block to the next.

For example, adding `5` and `7` gives

\[
\boxed{
\frac45\cdot\frac67=\frac{24}{35}}
\]

of the eight-state carrier surviving over the full `35`-block supercycle, or absolute density

\[
\boxed{
\frac13\cdot\frac{24}{35}=\frac8{35}}
\]

among all integers.

## 6. The first nontrivial correction: eight admissible slots do not mean eight primes

The eight positions in `U(24)` are only prime-admissible after removing factors `2` and `3`.

In every 24-block, at least one of the eight carrier positions is divisible by `5`, and at least one is divisible by `7`. Direct residue analysis modulo `5` and `7` shows that the union of these two hit sets contains at least two distinct carrier positions in every block.

For `k>=1`, all such multiples exceed `5` and `7`, so they are composite. Therefore

\[
\boxed{
\#\{\text{primes among }24k+U(24)\}\le6,
\qquad k\ge1.}
\]

This bound is sharp. At `k=1`,

\[
24+U(24)=\{25,29,31,35,37,41,43,47\},
\]

and exactly six are prime:

\[
29,31,37,41,43,47.
\]

Thus:

\[
\boxed{
\text{mod-24 admissibility maximum}=8,
\qquad
\text{actual prime maximum for a full block with }k\ge1=6.}
\]

The initial block `k=0` is exceptional because the forced `5`- and `7`-hits are the primes `5` and `7` themselves; it contains seven primes among the eight admissible positions, with `1` the lone nonprime.

## 7. Explicit first crossing schedules

For `q=5`, since `24\equiv-1\pmod5`,

\[
24k+r\equiv0\pmod5
\Longleftrightarrow
\boxed{k\equiv r\pmod5.}
\]

For `q=7`, since `24^{-1}\equiv5\pmod7`,

\[
24k+r\equiv0\pmod7
\Longleftrightarrow
\boxed{k\equiv2r\pmod7.}
\]

These are the first two periodic crossing families acting on the Boolean-cube carrier. Higher primes give the same exact rule

\[
k\equiv-r24^{-1}\pmod q.
\]

## 8. Relation to v13.225

v13.225 studies the Fourier/character response of the four-state quotient

\[
U(12)\cong C_2^2.
\]

The present checkpoint adds an independent but compatible structure:

\[
\boxed{
U(24)\cong C_2^3
\twoheadrightarrow
U(12)\cong C_2^2.}
\]

The extra bit distinguishes the two lifts `r` and `r+12` of each mod-12 state. Divisor rows `q>=5` then impose periodic crossing schedules on these eight lifted slots.

This suggests a clean hierarchy:

\[
\boxed{
\text{mod-12 V4 character carrier}
\longleftarrow
\text{mod-24 Boolean lift}
\longrightarrow
\text{successive divisor/parabolic sieve defects}.}
\]

The arrows record quotient/lift and sieve structure, not an operator intertwiner.

## 9. Scope guardrails

1. The density `8/24=1/3` is the `2,3`-wheel density, not the prime density.
2. The product `prod(1-1/q)` counts residues surviving a finite wheel over its full CRT period; it does not by itself prove asymptotics for primes.
3. Individual 24-block prime counts are not monotone with block index.
4. `Parabolic crossing` is legitimate here only in the precise Paper-A sense: a fixed divisor row maps to a row parabola and an integer factorization gives an integer row/shell crossing.
5. Do not identify the extra mod-24 `C_2` sheet bit with Frobenius, factor exchange, or any existing Boolean action without a separate proof.

## 10. Next exact task

The highest-value continuation is to combine this eight-state lift with the v13.225 four-character transform.

Questions to test:

- whether the extra `C_2` sheet has a natural character whose `8x8` Walsh-Hadamard transform separates the two mod-24 lifts of each V4 state;
- whether the divisor crossing schedule `k congruent -r 24^{-1} mod q` becomes diagonal or sparse in that `C_2^3` character basis;
- how projection from the eight-state transform back to the four-state `U(12)` transform recovers the `chi_12` prime selector;
- whether the `q`-row crossing families admit a direct expression in the existing Cone `X,T,Y` coordinates beyond the exact integer-row intersection criterion above.

Do not revise the audited principal v0.3.5 source from this checkpoint alone.