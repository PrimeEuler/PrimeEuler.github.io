# Cone Derivation Ledger v13.233 — Carrier Pushforward and Resonance Family

Date: 2026-09-04
Status: EXACT GENERALIZATION + FINITE AUDIT — continuation of v13.232; research branch remains open

## 0. Pre-write synchronization

Immediately before this write, the authoritative README and current `master` tip were re-fetched. The tip remained

`c4c1b468519f482f4ae36b41e1705a61d0686fc8`

with v13.232 as the highest ledger checkpoint. No newer external-audit checkpoint had landed. This entry extends that reconciled branch without revising the audited principal paper.

## 1. General carrier-crossing setup

Let `M>=3`, let

\[
R_M=U(M)=(\mathbf Z/M\mathbf Z)^\times,
\]

and let `psi:R_M->{+/-1}` be a real quadratic character. Let `q` be an odd prime with `gcd(M,q)=1`.

For the `M`-block carrier write

\[
N=Mk+r,
\qquad r\in R_M,
\qquad k\in\mathbf Z/q\mathbf Z.
\]

The row-`q` crossing condition is

\[
q\mid(Mk+r)
\iff
k\equiv-rM^{-1}\pmod q.
\]

Define the character-weighted crossing signal

\[
\boxed{
f_{M,q,\psi}(k)
:=
\sum_{r\in R_M\atop k\equiv-rM^{-1}\,(q)}\psi(r).
}
\]

This recovers the v13.230/v13.231 signal when `M=24`.

## 2. Pushforward theorem

Define the additive pushforward of `psi` from the unit carrier to `F_q` by

\[
\boxed{
P_{M,q,\psi}(t)
:=
\sum_{r\in R_M\atop r\equiv t\,(q)}\psi(r),
\qquad t\in\mathbf F_q.
}
\]

Since the crossing relation is `r=-Mk mod q`, one has the exact identity

\[
\boxed{
f_{M,q,\psi}(k)=P_{M,q,\psi}(-Mk).
}
\]

Thus the crossing signal is not a new independent object: it is the additive pushforward of a multiplicative quadratic character, composed with the invertible dilation `k->-Mk` on `F_q`.

This is the correct general carrier formulation of the resonance mechanism.

## 3. Exact Legendre-resonance criterion

Let

\[
\lambda_q(t)=\left(\frac{t}{q}\right)
\]

be the Legendre character on `F_q`, extended by `lambda_q(0)=0`.

A shifted signed Legendre resonance means

\[
f_{M,q,\psi}(k)
=
\epsilon\lambda_q(k-a),
\qquad \epsilon\in\{+1,-1\}.
\]

Using `t=-Mk`, this is equivalent to

\[
\boxed{
P_{M,q,\psi}(t)
=
\epsilon
\lambda_q\!\left(-M^{-1}t-a\right).
}
\]

Therefore:

\[
\boxed{
\text{Legendre resonance}
\iff
\text{the additive pushforward of }\psi
\text{ is an affine Legendre character on }\mathbf F_q.
}
\]

This converts the search from a time-series comparison into a precise pushforward identity.

## 4. Collision-free support obstruction

If the reduction map

\[
R_M\to\mathbf F_q
\]

is injective, then `P_{M,q,psi}` has exactly `phi(M)` nonzero entries, each equal to `+/-1`.

A Legendre sequence has exactly `q-1` nonzero entries. Hence, in the collision-free regime,

\[
\boxed{
\text{Legendre resonance}
\Longrightarrow
\varphi(M)=q-1.
}
\]

This explains why carrier size matters directly. The fixed `U(24)` carrier has `phi(24)=8`; for large `q` its support can never match a Legendre sequence.

Collisions modulo `q` can change this conclusion by causing signed aggregation and cancellation, as happened at `M=24,q=7`.

## 5. Finite exact carrier audit

A finite exact audit was performed over all moduli

\[
3\le M\le40
\]

with

\[
\varphi(M)\le16,
\]

all odd primes

\[
5\le q<24,
\qquad q\nmid M,
\]

all real quadratic characters `psi:U(M)->{+/-1}`, every shift `a mod q`, and both overall signs.

Exactly six carrier/character resonances occur in this audit:

\[
\boxed{
\begin{array}{c|c|c|c}
M&q&\psi&f_{M,q,\psi}(k)\\
\hline
8&5&\chi_8&\left(\frac{k-2}{5}\right)\\
17&5&\chi_{17}&\left(\frac{k-2}{5}\right)\\
20&7&\chi_{-4}&-\left(\frac{k-3}{7}\right)\\
24&7&\chi_{-8}&-\left(\frac{k-3}{7}\right)\\
30&7&\chi_{-15}&-\left(\frac{k-3}{7}\right)\\
32&5&\chi_8&-\left(\frac{k-2}{5}\right)
\end{array}}
\]

The corresponding exact block signals are

\[
(-1,1,0,1,-1)
\]

for the positive `q=5` cases,

\[
(1,-1,0,-1,1)
\]

for `M=32`, and

\[
(-1,1,1,0,-1,-1,1)
\]

for all three `q=7` cases.

This finite table is an audited search result within the stated range; it is not yet a classification theorem for all `M`.

## 6. The original M=24 resonance is part of a small carrier family

Ledger v13.232 proved that, for the fixed carrier `U(24)`, the pair

\[
(q,\psi)=(7,\chi_{-8})
\]

is globally unique.

The present audit shows that this does **not** mean the `q=7` Gauss signal is globally unique across carriers. The same seven-point Legendre sequence also appears for

\[
\boxed{(M,\psi)=(20,\chi_{-4}),\ (24,\chi_{-8}),\ (30,\chi_{-15}).}
\]

Thus the correct statement is:

\[
\boxed{
\text{q=7 resonance is rigid on }U(24),
\text{ but belongs to a broader carrier-pushforward family.}
}
\]

This reconciles the rigidity theorem with the generalized search.

## 7. Two visibly distinct resonance mechanisms

The audit already separates two mechanisms.

### 7.1 Collision-free size match

For `M=8,q=5`,

\[
\varphi(8)=4=q-1,
\]

and the four units remain distinct modulo `5`. The pushforward therefore has exactly the correct Legendre support without collisions.

Similarly, `M=17` has `phi(17)=16`, but the reduction modulo `5` aggregates its carrier in a highly structured way that reproduces the same five-point Legendre signal.

### 7.2 Collision-and-cancellation resonance

For `M=20,24,30` at `q=7`, each carrier has eight unit states, while the target Legendre sequence has six nonzero positions and one zero. Signed collisions in the pushforward produce the required support reduction and the exact quadratic sign pattern.

Therefore carrier cardinality alone does not classify resonance; one must retain the signed residue-fiber sums

\[
P_{M,q,\psi}(t).
\]

## 8. Fourier consequence

Whenever the pushforward criterion holds,

\[
f_{M,q,\psi}(k)
=
\epsilon\left(\frac{k-a}{q}\right),
\]

the block DFT is automatically a shifted quadratic Gauss sum:

\[
\boxed{
\widehat f(m)
=
\epsilon e^{2\pi i ma/q}
\left(\frac{m}{q}\right)\tau_q,
\qquad m\ne0,
}
\]

with

\[
|\tau_q|=\sqrt q.
\]

Hence every exact pushforward resonance has the flat spectrum

\[
\boxed{|\widehat f(m)|=\sqrt q\quad(m\ne0).}
\]

So the `q=7` flat spectrum of v13.231 is one instance of a general theorem: the real work is proving the pushforward becomes an affine Legendre character.

## 9. Arithmetic interpretation of the character labels

The six observed carrier resonances use familiar quadratic characters:

\[
\chi_8,\quad \chi_{17},\quad \chi_{-4},\quad \chi_{-8},\quad \chi_{-15}.
\]

Thus the carrier side is again quadratic-field arithmetic, while the crossing side is a Legendre character modulo `q`.

The resonance condition is therefore an exact bridge between two quadratic-character systems:

\[
\boxed{
\text{quadratic character on }U(M)
\xrightarrow{\text{additive pushforward mod }q}
\text{quadratic character on }\mathbf F_q.
}
\]

This is substantially more precise than a generic harmonic analogy.

## 10. Guardrails

1. The finite `M<=40`, `phi(M)<=16`, `q<24` table is exploratory but exact within its stated search range.
2. No claim is made yet that the six listed pairs exhaust all carrier moduli.
3. `psi` is multiplicative on `U(M)`, while the pushforward is taken along additive residue fibers modulo `q`; these structures must not be conflated.
4. Flat Gauss spectrum follows from exact Legendre pushforward, but the converse need not hold without additional hypotheses.
5. This checkpoint does not alter the audited principal v0.3.5 theorem package.

## 11. Next task

The next exact problem is to classify when

\[
P_{M,q,\psi}(t)
=
\sum_{r\in U(M)\atop r\equiv t\,(q)}\psi(r)
\]

can equal an affine Legendre character.

The most promising route is to factor the fiber sum by CRT whenever `M` decomposes into prime-power components, and determine whether the resonance condition factors into local quadratic Gauss/Jacobi data.

That would convert the observed carrier table into a genuine reciprocity theorem rather than a finite search result.
