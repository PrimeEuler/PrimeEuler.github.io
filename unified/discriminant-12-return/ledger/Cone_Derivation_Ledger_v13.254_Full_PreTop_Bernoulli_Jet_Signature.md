# Cone Derivation Ledger v13.254 — Full Pre-Top Bernoulli Jet Signature

Date: 2026-09-05
Status: EXACT NEW RESULT + CERTIFIED q=11 FILTER — continuation of v13.252–v13.253; research branch remains open

## 0. Synchronization and audit state

Immediately before this write, the authoritative project README and current `master` tip were re-fetched. The tip was

`53760d2a3f3d303e257b2aa13999f1d6ea7cfbd4`

with `v13.253` as the highest ledger checkpoint. External audit round 7 verified `v13.249`–`v13.252` and found no new mathematical error. No correction is required before continuing.

The round-6 sign correction remains authoritative:

\[
f_{24}=-\ell_7,\qquad f_{240}=+\ell_7=-f_{24}.
\]

## 1. Why the primitive lower-Bernoulli criterion is not enough

The previous entries reduced the lower Hasse problem to the primitive congruences

\[
B_{n,\chi_D}\equiv0\pmod q
\]

for every parity-compatible unit shift

\[
1\le n<e,\qquad n\equiv e\pmod2,\qquad \gcd(n-1,e)=1,
\]

where

\[
e=\frac{q-1}{2}.
\]

That criterion is necessary, but it does not by itself force the target coefficient `B_{e,chi_D}` to vanish.

A concrete counterexample to the hoped-for implication occurs already at

\[
q=11,\qquad e=5,\qquad D=-19.
\]

For the primitive quadratic character `chi_{-19}` one has exactly

\[
B_{3,\chi_{-19}}=66,
\]

so

\[
11\mid B_{3,\chi_{-19}},
\]

while

\[
B_{5,\chi_{-19}}=-13450\equiv3\pmod{11}\ne0.
\]

Thus the unit-shift primitive obstruction is genuinely only the first gate. A stronger invariant is required.

The key observation is that exact Legendre resonance determines not only the first nonzero Hasse coefficient, but the entire moment/Bernoulli jet from index `e` up to index `q-2`.

## 2. Exact centered-Legendre power moments

Let

\[
q=2e+1
\]

be an odd prime and let

\[
\ell_q(k)=\chi(k-e),
\]

where `chi` is the quadratic character modulo `q`, extended by `chi(0)=0`.

Suppose the crossing signal is an exact resonance

\[
f(k)=\epsilon\,\ell_q(k),
\qquad \epsilon\in\{\pm1\}.
\]

Define the power moments

\[
\mu_j(f)=\sum_{k\in\mathbf F_q}f(k)k^j.
\]

Write

\[
u=k-e.
\]

Euler's criterion gives

\[
\chi(u)=u^e
\]

in `F_q`, including the value `0` at `u=0`. Therefore

\[
\mu_j(f)
=\epsilon\sum_{u\in\mathbf F_q}u^e(u+e)^j.
\]

Expand

\[
(u+e)^j
=\sum_{r=0}^j\binom jr e^{j-r}u^r.
\]

For `0<=j<=2e=q-1`, the exponents `e+r` lie between `e` and `3e`. The only positive multiple of `q-1=2e` in this range is `2e`, occurring exactly when `r=e`.

Using

\[
\sum_{u\in\mathbf F_q}u^m
=0
\]

for positive `m` not divisible by `q-1`, and

\[
\sum_{u\in\mathbf F_q}u^{q-1}=-1,
\]

we obtain the exact moment law

\[
\boxed{
\mu_j(f)=0
\qquad(0\le j<e),
}
\]

and

\[
\boxed{
\mu_j(f)
=-\epsilon\binom je e^{j-e}
\qquad(e\le j\le2e).
}
\]

This extends the half-order vanishing theorem of `v13.247` from a root-order statement to a complete centered-Legendre power-moment signature.

## 3. Transfer from crossing moments to carrier moments

Let

\[
P(t)=P_{M,q,\psi}(t)
\]

be the additive pushforward and recall

\[
f(k)=P(-Mk).
\]

Define the carrier power moments

\[
C_j(M,\psi)
=\sum_{r\in U(M)}\psi(r)r^j.
\]

Folding modulo `q` gives

\[
C_j(M,\psi)
\equiv
\sum_{t\in\mathbf F_q}P(t)t^j
\pmod q.
\]

Under the change of variable

\[
t=-Mk,
\]

we have

\[
\sum_tP(t)t^j
=(-M)^j\mu_j(f).
\]

Therefore exact resonance forces

\[
\boxed{
C_j(M,\psi)\equiv0\pmod q
\qquad(0\le j<e),
}
\]

and

\[
\boxed{
C_j(M,\psi)
\equiv
-\epsilon(-M)^j\binom je e^{j-e}
\pmod q
\qquad(e\le j\le2e).
}
\]

This is the full carrier moment signature modulo `q`.

## 4. Bernoulli-moment triangular relation

Let `psi` denote the induced Dirichlet character represented by the carrier weight modulo `M`. For `n<q-1`, all ordinary Bernoulli denominators appearing below are invertible modulo `q`.

The generalized Bernoulli number satisfies

\[
B_{n,\psi}
=M^{n-1}\sum_{a=1}^{M}\psi(a)B_n(a/M).
\]

Using

\[
B_n(x)=\sum_{k=0}^n\binom nk B_kx^{n-k},
\]

we get the exact triangular relation

\[
\boxed{
B_{n,\psi}
=\sum_{k=0}^n
\binom nk B_k M^{k-1}C_{n-k}(M,\psi).
}
\]

Because exact resonance gives

\[
C_0=C_1=\cdots=C_{e-1}=0,
\]

this relation becomes especially simple at indices

\[
n=e+s,
\qquad0\le s<e.
\]

Only terms `0<=k<=s` survive.

## 5. Universal pre-top Bernoulli jet theorem

Let

\[
0\le s<e.
\]

From the moment signature,

\[
\frac{C_{e+s-k}}{C_e}
=(-M)^{s-k}
\binom{e+s-k}{e}e^{s-k}.
\]

Also, because all lower moments vanish,

\[
B_{e,\psi}=\frac{C_e}{M}.
\]

Substituting into the triangular Bernoulli relation gives

\[
B_{e+s,\psi}
=M^sB_{e,\psi}
\sum_{k=0}^s
\binom{e+s}{k}B_k
(-1)^{s-k}
\binom{e+s-k}{e}e^{s-k}.
\]

Use the binomial identity

\[
\binom{e+s}{k}\binom{e+s-k}{e}
=\binom{e+s}{e}\binom sk.
\]

Then

\[
B_{e+s,\psi}
=M^sB_{e,\psi}
\binom{e+s}{e}
\sum_{k=0}^s\binom sk B_k(-e)^{s-k}.
\]

The inner sum is the Bernoulli polynomial

\[
B_s(-e).
\]

Since in `F_q`

\[
e\equiv-\frac12,
\]

we have

\[
-e\equiv\frac12.
\]

Hence:

\[
\boxed{
B_{e+s,\psi}
\equiv
M^s B_{e,\psi}
\binom{e+s}{s}
B_s\!\left(\frac12\right)
\pmod q,
\qquad0\le s<e.
}
\]

This is the **full pre-top Bernoulli jet signature**.

It contains the lower parity structure automatically because

\[
B_s\!\left(\frac12\right)=0
\]

for every odd `s>=1`.

## 6. Cofactor-free nonlinear invariants

The leading exact-resonance moment is

\[
C_e
=-\epsilon(-M)^e.
\]

Since

\[
C_e=MB_{e,\psi},
\]

we obtain

\[
\boxed{
MB_{e,\psi}=\delta,
\qquad
\delta\in\{\pm1\}.
}
\]

Here `delta` absorbs both the resonance sign and the quadratic value `(-M)^e`.

Now let

\[
s=2r<e.
\]

Because `delta^{2r}=1`, the factor `M^{2r}` can be eliminated from the jet theorem. Define

\[
c_{2r}(q)
:=
\binom{e+2r}{2r}
B_{2r}\!\left(\frac12\right)
\in\mathbf F_q.
\]

Then every exact resonance satisfies the cofactor-free invariant

\[
\boxed{
B_{e+2r,\psi}
B_{e,\psi}^{\,2r-1}
\equiv
c_{2r}(q)
\pmod q,
\qquad
1\le r<\frac e2.
}
\]

These congruences are independent of

- the cofactor state `h`;
- the overall resonance sign `epsilon`;
- the choice of representative of `M mod q` after the leading signature is imposed.

They are genuine higher-order necessary conditions beyond the half-order root and its first nonzero coefficient.

## 7. First two nonlinear invariants

For `r=1`,

\[
B_2(1/2)=-\frac1{12}
\]

and

\[
\binom{e+2}{2}
\equiv\frac38\pmod q.
\]

Therefore

\[
\boxed{
B_{e+2,\psi}B_{e,\psi}
\equiv
-\frac1{32}
\pmod q.
}
\]

For `r=2`,

\[
B_4(1/2)=\frac7{240},
\]

and

\[
\binom{e+4}{4}
\equiv\frac{35}{128}\pmod q.
\]

Hence

\[
\boxed{
B_{e+4,\psi}B_{e,\psi}^3
\equiv
\frac{49}{6144}
\pmod q
}
\]

whenever `4<e`.

Thus the first two nontrivial higher jet constraints are already nonlinear and support-sensitive through the induced Bernoulli numbers.

## 8. Euler-factor form of the higher jet

For fixed primitive `chi_D` and extra support set `S`, recall

\[
B_{n,\psi}
=B_{n,\chi_D}
\prod_{p\in S}
\left(1-\chi_D(p)p^{n-1}\right).
\]

The `2r`-th jet invariant therefore becomes

\[
\boxed{
B_{e+2r,\chi_D}
B_{e,\chi_D}^{2r-1}
\prod_{p\in S}
\left(1-\chi_D(p)p^{e+2r-1}\right)
\left(1-\chi_D(p)p^{e-1}\right)^{2r-1}
\equiv
c_{2r}(q)
\pmod q.
}
\]

This is the first place where the already-solved lower support-covering problem interacts nontrivially with a new family of higher coefficients.

The lower-index support basis of `v13.252` is not automatically sufficient to satisfy this higher jet.

## 9. q=11 primitive false positive and higher-jet rejection of the minimal support basis

Take

\[
q=11,\qquad e=5,\qquad D=-19.
\]

The primitive generalized Bernoulli values are

\[
B_{3,\chi_{-19}}=66,
\]

\[
B_{5,\chi_{-19}}=-13450,
\]

\[
B_{7,\chi_{-19}}=5303074,
\]

\[
B_{9,\chi_{-19}}=-\frac{66751985430}{19}.
\]

Modulo `11`,

\[
\boxed{
B_3=0,
\qquad
B_5=3,
\qquad
B_7=7,
\qquad
B_9=3.
}
\]

Thus `D=-19` passes the only unavoidable primitive lower condition at `q=11`, namely `11|B_3`, while preserving `B_5`.

The remaining lower condition is `n=1`, which is support-coverable. A one-prime minimal support basis requires a support prime with

\[
\chi_{-19}(P)=+1
\]

and target-safe residue `r=P mod 11`.

An exhaustive exact check over all target-safe `r in F_11^*` with `sigma=+1` shows that the induced pair of higher invariants

\[
I_2:=B_7B_5,
\qquad
I_4:=B_9B_5^3
\]

never simultaneously equals the exact Legendre targets

\[
\boxed{
I_2=1,
\qquad
I_4=10
\quad\text{in }\mathbf F_{11}.
}
\]

More specifically, every one-prime lower-covering choice lands in one of the pairs

\[
(I_2,I_4)=(1,6)
\]

or

\[
(I_2,I_4)=(5,3),
\]

never `(1,10)`.

Therefore:

\[
\boxed{
(D,q)=(-19,11)
\text{ passes the primitive lower gate but cannot pass the full pre-top jet with the one-prime minimal support basis.}
}
\]

This is a certified finite-field exclusion of the simplest Hasse-admissible false positive.

Guardrail: this does **not** prove that `D=-19,q=11` is impossible with arbitrary larger support. Additional target-safe support primes can alter the higher Euler-factor products without changing the already-covered lower zero. The point is that the new jet adds genuine independent constraints that the lower-covering theorem does not see.

## 10. Structural meaning

The Hasse/Bernoulli branch now has three levels rather than two.

First, the lower half-order root requires

\[
B_{n,\psi}=0
\qquad(1\le n<e).
\]

Second, the leading coefficient requires

\[
MB_{e,\psi}=\pm1.
\]

Third, exact Legendre shape forces the entire higher pre-top jet

\[
\boxed{
B_{e+2r,\psi}B_{e,\psi}^{2r-1}
=c_{2r}(q)
\qquad
(1\le r<e/2).
}
\]

So the previous architecture

\[
\text{primitive lower obstruction}
+
\text{support covering}
+
\text{leading signature}
\]

must now be refined to

\[
\boxed{
\text{primitive lower obstruction}
+
\text{support covering}
+
\text{leading signature}
+
\text{universal higher Bernoulli jet}.
}
\]

The last term is new and carries information about the actual Legendre profile, not merely its root multiplicity.

## 11. Relation to the full folded signal

The moment theorem in §2 actually gives all power moments through degree `q-1`.

For degrees `0,...,q-2`, these moments determine a function on `F_q` modulo the one-dimensional constant ambiguity, because the polynomial functions of degree at most `q-2` have codimension one in the full function space.

The final degree `q-1` moment detects that remaining constant component.

Therefore the full moment signature is, modulo `q`, essentially equivalent to the complete folded Legendre profile.

The Bernoulli jet of this entry captures the whole pre-top portion `e,...,q-2` in an arithmetic form compatible with primitive/support factorization. The still-singular top degree `q-1` is excluded from the generalized-Bernoulli reduction because ordinary Bernoulli denominators at that degree involve `q`; it should be treated directly at the raw moment level.

This identifies a natural next invariant: the **top moment / constant-lift condition**.

## 12. What is proved and what remains open

Proved exactly:

- the full centered-Legendre power-moment formula
  \[
  \mu_j=0\ (j<e),\qquad
  \mu_j=-\epsilon\binom je e^{j-e}\ (e\le j\le q-1);
  \]
- the corresponding carrier moment formula after the affine crossing map;
- the complete pre-top generalized-Bernoulli jet
  \[
  B_{e+s,\psi}
  =M^sB_{e,\psi}\binom{e+s}{s}B_s(1/2)
  \quad(0\le s<e);
  \]
- the cofactor-free nonlinear invariants
  \[
  B_{e+2r,\psi}B_{e,\psi}^{2r-1}=c_{2r}(q);
  \]
- the first universal constant
  \[
  B_{e+2,\psi}B_{e,\psi}=-1/32;
  \]
- the second universal constant
  \[
  B_{e+4,\psi}B_{e,\psi}^3=49/6144;
  \]
- `D=-19,q=11` is an explicit primitive-lower false positive;
- the one-prime minimal support basis cannot make that example satisfy the full pre-top jet.

Not proved:

\[
q\ge11\Longrightarrow\text{no exact Legendre resonance}.
\]

Also not proved: that the full higher jet is incompatible with arbitrary enlarged support for every primitive candidate.

## 13. Next theorem target

The next hard step should use the fact that support primes act multiplicatively on the whole invariant tuple

\[
\left(
B_{e+2}B_e,
B_{e+4}B_e^3,
\ldots
\right).
\]

For fixed `q`, each local support label `(r,sigma)` contributes a finite multiplicative vector in

\[
(\mathbf F_q^\times)^m,
\qquad
m=\left\lfloor\frac{e-1}{2}\right\rfloor.
\]

Because infinitely many rational support primes can realize the same local label, arbitrary support enlargement becomes a finite subgroup/semigroup reachability problem in this higher-jet torus.

The next exact target is therefore:

\[
\boxed{
\text{classify the subgroup generated by target-safe local higher-jet multipliers.}
}
\]

If the Legendre target tuple lies outside the orbit of every primitive candidate satisfying the unit-shift lower congruences, then the higher-prime resonance problem closes.

Even if the global theorem remains out of reach, this converts the hard part into a finite algebraic reachability problem for each `q`, rather than an unbounded search over carrier moduli.

## 14. Checkpoint

The strongest exact chain is now

\[
\boxed{
\text{exact resonance}
\Longrightarrow
\begin{cases}
\text{primitive unit-shift lower Bernoulli zeros},\\
\text{explicit support covering of nonunit shifts},\\
MB_e=\pm1,\\
B_{e+2r}B_e^{2r-1}=c_{2r}(q)
\text{ for all }2r<e.
\end{cases}
}
\]

The previous hope that the primitive lower block alone might force `B_e=0` is false in general; `D=-19,q=11` is an exact counterexample. The new higher Bernoulli jet is therefore the correct next obstruction layer.