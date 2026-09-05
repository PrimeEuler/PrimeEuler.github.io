# Cone Derivation Ledger v13.235 — Fixed-Support Periodicity and Infinite Resonance Towers

Date: 2026-09-04
Status: EXACT NEW RESULT — continuation of v13.234; research branch remains open

## 0. Pre-write synchronization

Immediately before this write, the authoritative project README and current `master` tip were re-fetched. The tip remained

`a5482ee70a32d5a48cca12637452cbc3724a0e7a`

with v13.234 as the highest ledger checkpoint. No newer external-audit checkpoint had landed. This entry extends that reconciled branch without revising the audited principal v0.3.5 paper.

## 1. Why the remaining classification problem is not genuinely infinite in the exponent directions

Ledger v13.234 reduced the carrier-crossing problem to a primitive quadratic conductor together with extra-prime exclusions.

Let

\[
\chi_D(n)=\left(\frac{D}{n}\right)
\]

be a primitive nonprincipal quadratic Kronecker character of fundamental discriminant `D`, with conductor

\[
d=|D|.
\]

Fix a finite set `S` of primes not dividing `d`. Put

\[
R_S:=\prod_{p\in S}p,
\qquad
L:=dR_S.
\]

The point of fixing `S` is that we are fixing the **radical support stratum**: the carrier modulus `M` may vary in the exponents of primes already dividing `L`, but no new prime outside the support of `L` is introduced.

Thus every modulus in the stratum has the form

\[
\boxed{M=Lh}
\]

where every prime divisor of `h` already divides `L`.

On this stratum, the unit-carrier weight is the fixed periodic function

\[
W_{D,S}(n)
:=
\chi_D(n)
\prod_{p\in S}\mathbf 1_{p\nmid n}.
\]

Its period divides `L`.

The additive pushforward is therefore

\[
P_h(t)
:=
\sum_{0\le n<Lh\atop n\equiv t\,(q)}
W_{D,S}(n),
\qquad t\in\mathbf F_q,
\]

for an odd prime `q` with `(q,L)=1`.

The central new fact is that, after the radical support is fixed, the dependence on the arbitrarily large exponent vector collapses to one residue class modulo `q`.

## 2. Zero mean over one support period

Because `D` is nonprincipal, the induced character on `U(L)` is nonprincipal. Hence

\[
\sum_{a\bmod L}W_{D,S}(a)=0.
\]

More explicitly, the nonzero values of `W_{D,S}` are exactly the values of the induced quadratic character on `U(L)`, so

\[
\boxed{
\sum_{a=0}^{L-1}W_{D,S}(a)=0.
}
\]

This zero-mean identity is the mechanism that removes complete `qL` blocks from the pushforward.

## 3. Fixed-support q-periodicity theorem

Consider increasing the cofactor by one full `q`-step:

\[
h\longmapsto h+q.
\]

Then the carrier interval length changes from `Lh` to `L(h+q)`, adding an interval of length `qL`.

For fixed `t mod q`, the added contribution is

\[
\sum_{Lh\le n<L(h+q)\atop n\equiv t\,(q)}W_{D,S}(n).
\]

Since `(q,L)=1`, the Chinese remainder theorem implies that, inside any interval of length `qL`, the numbers satisfying `n=t mod q` run exactly once through every residue class modulo `L`.

Therefore the added contribution is

\[
\sum_{a\bmod L}W_{D,S}(a)=0.
\]

Hence

\[
\boxed{P_{h+q}(t)=P_h(t)}
\qquad(t\in\mathbf F_q).
\]

Thus:

\[
\boxed{
P_h\text{ depends only on }h\bmod q
\text{ within a fixed radical-support stratum.}
}
\]

This is exact, not asymptotic.

## 4. Crossing-signal periodicity

The crossing signal is

\[
f_h(k)=P_h(-M k)=P_h(-Lhk),
\qquad k\in\mathbf F_q.
\]

If

\[
h'\equiv h\pmod q,
\]

then simultaneously

\[
P_{h'}=P_h
\]

and

\[
Lh'\equiv Lh\pmod q.
\]

Therefore

\[
\boxed{f_{h'}(k)=f_h(k)\quad\text{for every }k\in\mathbf F_q.}
\]

Equivalently, for two carrier moduli in the same support stratum,

\[
M=Lh,
\qquad
M'=Lh',
\qquad
h'\equiv h\pmod q,
\]

one has the exact equality

\[
\boxed{
f_{M',q,D}=f_{M,q,D}.
}
\]

So the entire pointwise crossing sequence, its autocorrelation, and its block-frequency DFT are unchanged.

## 5. Classification consequence: exponent directions reduce to a finite state space

Fix `(D,S,q)`.

All exponent vectors supported on the primes of `L=dR_S` map to the single cofactor residue

\[
\boxed{h=M/L\pmod q.}
\]

There are only `q-1` admissible nonzero residue classes because `q\nmid M`.

Therefore the exact resonance problem on a fixed support stratum reduces from infinitely many exponent choices to at most

\[
\boxed{q-1}
\]

finite cofactor states.

This materially sharpens the v13.234 classification program:

\[
\boxed{
\text{fixed conductor + fixed extra-prime support}
\Longrightarrow
\text{finite }h\bmod q\text{ resonance test}.
}
\]

The genuinely unbounded part of the global problem is therefore the introduction of **new prime support**, not the growth of exponents on an already fixed support.

## 6. Infinite-tower theorem

Suppose `(M,q,D)` is an exact Legendre resonance and let `c>=1` satisfy

1. every prime dividing `c` already divides `M`;
2. `c\equiv1 mod q`.

Then `cM` lies in the same support stratum as `M`.

Writing

\[
M=Lh,
\qquad
cM=L(ch),
\]

we have

\[
ch\equiv h\pmod q.
\]

By the fixed-support periodicity theorem,

\[
\boxed{
f_{cM,q,D}=f_{M,q,D}.}
\]

Therefore:

\[
\boxed{
(M,q,D)\text{ resonance},\quad
\operatorname{rad}(c)\mid\operatorname{rad}(M),\quad
c\equiv1\pmod q
\Longrightarrow
(cM,q,D)\text{ is the same resonance.}
}
\]

This proves that every such scaling factor generates an exact infinite tower.

If one admissible `c>1` exists, then

\[
M,\ cM,\ c^2M,\ c^3M,\ldots
\]

all carry the identical centered Legendre sequence and identical Gauss spectrum.

## 7. The original U(24), q=7 resonance sits in an exact infinite tower

The original resonance is

\[
(M,q,D)=(24,7,-8),
\]

with

\[
f_{24,7,-8}(k)
=-\left(\frac{k-3}{7}\right).
\]

Take

\[
c=2^3=8.
\]

Its only prime divisor already divides `24`, and

\[
8\equiv1\pmod7.
\]

Hence

\[
\boxed{
f_{24\cdot8^j,\,7,\,-8}(k)
=-\left(\frac{k-3}{7}\right)
\qquad(j\ge0).
}
\]

The first two members are

\[
24,\qquad192,
\]

and `M=192,D=-8` was independently present in the expanded v13.234 audit.

Thus the occurrence at `192` is no longer merely another finite-search hit; it is theorem-predicted from the `24` resonance.

## 8. Two other q=7 towers already visible in the audit

### 8.1 D=-4 tower from M=20

The audited resonance

\[
(20,7,-4)
\]

also admits the scaling

\[
c=8\equiv1\pmod7,
\]

with no new prime support. Therefore

\[
\boxed{
20\cdot8^j
}
\]

is an infinite resonance tower for `D=-4`.

The next member

\[
20\cdot8=160
\]

appears in the v13.234 table exactly as predicted.

### 8.2 D=-15 tower from M=30

Likewise

\[
(30,7,-15)
\]

has

\[
30\cdot8=240,
\]

and the v13.234 audit contains

\[
(240,-15,-1).
\]

Hence

\[
\boxed{
30\cdot8^j
}
\]

is another exact infinite `q=7` resonance tower.

These three examples show that a significant part of the expanded q=7 table is generated by support-preserving exponent motion rather than by unrelated sporadic coincidences.

## 9. Exact q=5 tower generated from the D=8 carrier

The first q=5 resonance is

\[
(M,q,D)=(8,5,8).
\]

Take

\[
c=2^4=16.
\]

Then

\[
16\equiv1\pmod5
\]

and no new prime support is introduced. Therefore

\[
\boxed{
8\cdot16^j
}
\]

is an exact infinite q=5 resonance tower.

Its first members are

\[
8,\ 128,\ 2048,\ldots
\]

The first two are already present in the expanded search window.

The separately observed resonance at `M=32` belongs to the same single-prime support stratum but a different cofactor state modulo `5`; it is not generated from `8` by a `c=1 mod 5` scaling. Its opposite overall Legendre sign is therefore compatible with the finite-state picture.

## 10. Prime-power exponent periodicity

Suppose the support stratum contains a prime `p\ne q`. Increasing its exponent by `m` multiplies the cofactor `h` by `p^m`.

Let

\[
\operatorname{ord}_q(p)
\]

be the multiplicative order of `p mod q`. Then

\[
p^{\operatorname{ord}_q(p)}\equiv1\pmod q.
\]

Hence increasing the exponent of `p` by `ord_q(p)` leaves the complete crossing signal unchanged.

Therefore:

\[
\boxed{
\text{within fixed support, exponent dependence is periodic with period dividing }
\operatorname{ord}_q(p)
}
\]

in each prime-exponent direction.

For several support primes, the exponent lattice factors through the finite group

\[
\langle p\bmod q:p\mid L\rangle\subseteq\mathbf F_q^\times.
\]

Thus the exponent-classification problem is naturally a finite multiplicative-orbit problem in `F_q^*`.

## 11. Refined classification geometry

The current resonance search can now be organized into three levels.

### Level A: primitive conductor

Choose a fundamental discriminant

\[
D.
\]

### Level B: radical support

Choose the finite set of extra carrier primes

\[
S=\{p:p\mid M,\ p\nmid |D|\}.
\]

This fixes

\[
L=|D|\prod_{p\in S}p
\]

and the periodic carrier weight `W_{D,S}`.

### Level C: exponent/cofactor state

All remaining exponent information enters through

\[
\boxed{h=M/L\bmod q.}
\]

Therefore an exact global classification may be written schematically as

\[
\boxed{
(D,S,h\bmod q).
}
\]

The centered-shift, parity, and collision-energy filters from v13.234 act before the final finite `h` test.

This is substantially smaller than classifying raw integers `M` one by one.

## 12. Interaction with the centered involution

The new periodicity theorem is independent of, but compatible with, the centered reflection theorem of v13.234.

If one state `h mod q` yields

\[
f_h(k)
=\epsilon\left(\frac{k-(q-1)/2}{q}\right),
\]

then every support-preserving exponent vector with the same cofactor state yields the **same** centered sequence, not merely another translated copy.

Thus both the center

\[
a=(q-1)/2
\]

and the overall sign `epsilon` are constant along a `c=1 mod q` tower.

Consequently the corresponding DFT is also literally unchanged:

\[
\boxed{
\widehat f_{cM}(m)=\widehat f_M(m).
}
\]

The Gauss-spectrum phase and magnitude are tower invariants.

## 13. What this explains in the expanded v13.234 table

The expanded table contained repeated families such as

\[
(24,-8),\ (192,-8),
\]

\[
(20,-4),\ (160,-4),
\]

and

\[
(30,-15),\ (240,-15).
\]

Each pair differs by the support-preserving multiplier

\[
8\equiv1\pmod7.
\]

Likewise the q=5 pair

\[
(8,8),\ (128,8)
\]

differs by

\[
16\equiv1\pmod5.
\]

These recurrences are therefore exact consequences of the theorem.

Other entries in the finite table correspond either to different radical-support strata or to different cofactor states in the same stratum. They still require separate finite classification.

## 14. A useful obstruction/certification principle

For fixed `(D,S,q)`, it is now sufficient to inspect one representative for each attainable cofactor class

\[
h\in\mathbf F_q^\times.
\]

If no representative resonates, then **no modulus anywhere in that entire exponent tower** resonates.

Conversely, one resonant representative certifies infinitely many resonant moduli whenever the support admits a nontrivial multiplier `c=1 mod q`.

Thus:

\[
\boxed{
\text{one finite support-stratum computation}
\Longrightarrow
\text{an infinite theorem in the exponent directions}.
}
\]

This is the first step that converts the large finite resonance audit into genuine infinite families.

## 15. Guardrails

1. The periodicity theorem requires a fixed primitive discriminant `D` and fixed extra-prime support `S`.
2. Introducing a new prime divisor of `M` changes `S`, changes the carrier weight, and moves to a different stratum; the theorem does not identify those strata.
3. The result does not imply that every cofactor class resonates; it only proves that the signal is constant on each class `h mod q`.
4. Multipliers `c=1 mod q` with no new prime support preserve the complete signal. No general sign rule for `c=-1 mod q` is asserted here.
5. The absence of q>=11 resonances remains unproved globally.
6. The audited principal Discriminant-12 v0.3.5 source remains unchanged.

## 16. Next task

The classification problem has now separated cleanly into finite support strata and finite cofactor states.

The next exact target is to classify the **new-prime support transitions**:

\[
S\longmapsto S\cup\{p\}.
\]

Using the conductor-Möbius formula from v13.234, adding one new prime `p` changes the pushforward by the exact exclusion operator

\[
P_{S\cup\{p\}}(t)
=
P_S(t)
-
\chi_D(p)\,Q_{\text{scaled}}(p^{-1}t),
\]

with the interval lengths tracked explicitly.

The immediate q=5/q=7 goal is to determine which residue classes of a newly introduced support prime `p mod q|D|` can carry one resonant support stratum into another. If that transition law closes, the current resonance table should organize into a finite directed graph of support types rather than a raw list of moduli.

Do not revise the principal v0.3.5 paper from this checkpoint alone.
