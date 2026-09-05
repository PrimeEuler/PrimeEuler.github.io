# Cone Derivation Ledger v13.234 — Centered Involution and Conductor-Möbius Decomposition

Date: 2026-09-04
Status: EXACT NEW RESULT + CLASSIFICATION FRAMEWORK — continuation of v13.233; research branch remains open

## 0. Pre-write synchronization

Immediately before this write, the authoritative project README, current `master` tip, and the v13.233 checkpoint were re-fetched. The tip remained

`5295abf1cf226c874f589fad0e4a1dc372d5665b`

with v13.233 as the highest ledger checkpoint. No newer external-audit checkpoint had landed. This entry extends that reconciled branch without revising the audited principal v0.3.5 paper.

## 1. General carrier crossing signal

Retain the v13.233 setup. Let

\[
R_M=U(M)=(\mathbf Z/M\mathbf Z)^\times,
\]

let

\[
\psi:R_M\to\{\pm1\}
\]

be a nonprincipal real quadratic character, and let `q` be an odd prime with `(M,q)=1`.

For the block decomposition

\[
N=Mk+r,
\qquad r\in R_M,
\qquad k\in\mathbf Z/q\mathbf Z,
\]

the row-`q` crossing condition is

\[
q\mid(Mk+r)
\iff
k\equiv-rM^{-1}\pmod q.
\]

The character-weighted crossing signal is

\[
\boxed{
f_{M,q,\psi}(k)
=
\sum_{r\in R_M\atop k\equiv-rM^{-1}\,(q)}\psi(r).
}
\]

Equivalently, with the additive pushforward

\[
P_{M,q,\psi}(t)
=
\sum_{r\in R_M\atop r\equiv t\,(q)}\psi(r),
\]

one has

\[
\boxed{f_{M,q,\psi}(k)=P_{M,q,\psi}(-Mk).}
\]

## 2. Carrier negation induces an exact centered involution in block time

The unit carrier has the canonical involution

\[
r\longmapsto M-r\equiv-r\pmod M.
\]

For a quadratic character,

\[
\psi(M-r)=\psi(-1)\psi(r).
\]

If

\[
\kappa(r):=-rM^{-1}\pmod q
\]

is the crossing time of `r`, then the crossing time of the reflected carrier point is

\[
\begin{aligned}
\kappa(M-r)
&=-(M-r)M^{-1}\\
&=-1+rM^{-1}\\
&=-1-\kappa(r)
\pmod q.
\end{aligned}
\]

Therefore the full crossing signal satisfies the exact reflection law

\[
\boxed{
f_{M,q,\psi}(-1-k)=\psi(-1)f_{M,q,\psi}(k).
}
\]

Writing the involution as

\[
\iota_q(k):=-1-k,
\]

its unique fixed point in `F_q` is

\[
2k=-1,
\]

hence

\[
\boxed{k_*=\frac{q-1}{2}.}
\]

Thus every carrier crossing signal has an exact parity symmetry about the discrete midpoint `(q-1)/2`:

- if `psi(-1)=+1`, the signal is even about `k_*`;
- if `psi(-1)=-1`, the signal is odd about `k_*`, and therefore
  \[
  \boxed{f_{M,q,\psi}(k_*)=0.}
  \]

This midpoint is forced by the carrier reflection. It is not a fitted parameter.

## 3. Centered-shift theorem for every exact Legendre resonance

Suppose an exact Legendre resonance occurs:

\[
\boxed{
f_{M,q,\psi}(k)
=
\epsilon\left(\frac{k-a}{q}\right),
\qquad \epsilon\in\{\pm1\}.
}
\]

The Legendre sequence has exactly one zero, at `k=a`.

But the carrier involution maps zeros to zeros because

\[
f(-1-k)=\psi(-1)f(k).
\]

Therefore the unique zero must be fixed by `k\mapsto-1-k`:

\[
a\equiv-1-a\pmod q.
\]

Hence

\[
\boxed{a=\frac{q-1}{2}.}
\]

So the shifts `a=2` for `q=5` and `a=3` for `q=7` found in v13.233 are not accidental search outputs. They are theorem-forced by the canonical unit-pair reflection.

This is the first general explanation for the centered positions appearing in every audited resonance.

## 4. Parity-matching theorem

With

\[
a=(q-1)/2,
\]

one has

\[
-1-k-a=-(k-a).
\]

Therefore a centered Legendre sequence transforms under the carrier involution as

\[
\left(\frac{-1-k-a}{q}\right)
=
\left(\frac{-1}{q}\right)
\left(\frac{k-a}{q}\right).
\]

Comparing this with

\[
f(-1-k)=\psi(-1)f(k)
\]

gives the necessary parity condition

\[
\boxed{
\psi(-1)=\left(\frac{-1}{q}\right)=(-1)^{(q-1)/2}.
}
\]

Thus:

\[
\boxed{
q\equiv1\pmod4
\Longrightarrow
\psi\text{ must be even},
}
\]

while

\[
\boxed{
q\equiv3\pmod4
\Longrightarrow
\psi\text{ must be odd}.
}
\]

This exactly explains the character signs in the current resonance families:

- `q=5` has `(-1/5)=+1`, and the observed characters `chi_8`, `chi_17`, `chi_13` are even;
- `q=7` has `(-1/7)=-1`, and the observed negative-discriminant characters are odd.

For a primitive quadratic Kronecker character `chi_D`, this becomes the discriminant-sign constraint

\[
\boxed{
\chi_D(-1)=\operatorname{sgn}(D)=\left(\frac{-1}{q}\right).
}
\]

Hence positive quadratic discriminants can resonate only with crossing primes `q=1 mod 4`, and negative quadratic discriminants only with crossing primes `q=3 mod 4`.

This is an exact reciprocity-compatible selection rule.

## 5. Autocorrelation test for a Legendre/Gauss resonance

Define the cyclic autocorrelation

\[
A_{M,q,\psi}(h)
:=
\sum_{k\bmod q}
 f_{M,q,\psi}(k)f_{M,q,\psi}(k+h).
\]

If

\[
f(k)=\epsilon\left(\frac{k-a}{q}\right),
\]

then the standard quadratic-character correlation identity gives

\[
\boxed{
A(0)=q-1,
}
\]

and for every nonzero `h`,

\[
\boxed{
A(h)=-1.
}
\]

Equivalently,

\[
\boxed{
A(h)=
\begin{cases}
q-1,&h=0,\\
-1,&h\ne0.
\end{cases}
}
\]

Thus exact Legendre resonance implies a perfect two-level periodic autocorrelation.

The zero-frequency character sum is already zero because `psi` is nonprincipal:

\[
\sum_k f(k)
=
\sum_{r\in U(M)}\psi(r)
=0.
\]

The two-level autocorrelation is therefore equivalent to flat nonzero Fourier power

\[
\boxed{
|\widehat f(m)|^2=q,
\qquad m\ne0.
}
\]

when the signal is known to be an exact Legendre sequence.

Guardrail: flat spectrum alone does not automatically prove pointwise equality with a Legendre character without an additional classification argument.

## 6. Exact collision-energy criterion

The zero-lag energy can be written directly in the carrier basis:

\[
\begin{aligned}
A(0)
&=\sum_k f(k)^2\\
&=\sum_{r,s\in U(M)\atop r\equiv s\,(q)}
\psi(r)\psi(s).
\end{aligned}
\]

Therefore every exact Legendre resonance must satisfy

\[
\boxed{
\sum_{r,s\in U(M)\atop r\equiv s\,(q)}
\psi(r)\psi(s)
=q-1.
}
\]

Separating diagonal and collision terms gives

\[
\boxed{
\varphi(M)
+
2\sum_{r<s\atop r\equiv s\,(q)}
\psi(r)\psi(s)
=q-1.
}
\]

This formula measures exactly how signed residue collisions must change the raw carrier energy `phi(M)` into the Legendre energy `q-1`.

For the collision-free case it immediately reduces to the v13.233 size condition

\[
\boxed{\varphi(M)=q-1.}
\]

For collision resonances, the signed pair sum is forced to be

\[
\boxed{
\sum_{r<s\atop r\equiv s\,(q)}
\psi(r)\psi(s)
=
\frac{q-1-\varphi(M)}2.
}
\]

Thus collisions are not merely allowed; their total signed contribution is numerically prescribed.

## 7. Why naive CRT factorization is not valid for the pushforward

The next task proposed in v13.233 was to factor

\[
P_{M,q,\psi}(t)
=
\sum_{0\le r<M\atop (r,M)=1,\ r\equiv t\,(q)}\psi(r)
\]

through prime-power CRT components of `M`.

There is an important structural obstruction.

Although

\[
U(M)\cong\prod_{p^a\parallel M}U(p^a)
\]

multiplicatively, the pushforward uses the **canonical integer representative** `0<=r<M` and then reduces that representative modulo the unrelated prime `q`.

A CRT representative is defined only modulo `M`; replacing it by `r+M` changes its residue modulo `q` because `(M,q)=1`.

Therefore the map

\[
U(M)\to\mathbf F_q,
\qquad r\mapsto r\bmod q,
\]

is not a homomorphism of the CRT product and the finite fiber sum does not generally factor into an Euler product of prime-power contributions.

Hence:

\[
\boxed{
\text{multiplicative CRT factorization of }U(M)
\text{ does not imply product factorization of }P_{M,q,\psi}.
}
\]

This corrects the overly optimistic form of the proposed v13.233 route before it is promoted into a false theorem.

CRT remains useful for constructing and labeling the quadratic character itself, but not for blindly factorizing the additive pushforward.

## 8. Correct conductor decomposition

Every real quadratic Dirichlet character on `U(M)` is induced by a primitive quadratic Kronecker character

\[
\chi_D(n)=\left(\frac{D}{n}\right)
\]

of fundamental discriminant `D`, with conductor

\[
d=|D|\mid M.
\]

On the unit carrier,

\[
\psi(r)=\chi_D(r).
\]

The primitive character already vanishes at primes dividing `d`. The additional unit condition for primes dividing `M` but not `d` can be isolated explicitly.

Let

\[
R=\prod_{p\mid M,\ p\nmid d}p
\]

be the squarefree product of the extra carrier primes not present in the primitive conductor.

For `0<=r<M`, define the zero-extended carrier weight

\[
W_{M,D}(r)
:=
\chi_D(r)
\prod_{p\mid R}\mathbf1_{p\nmid r}.
\]

Then exactly

\[
P_{M,q,D}(t)
=
\sum_{0\le r<M\atop r\equiv t\,(q)}W_{M,D}(r).
\]

Expand the extra-prime exclusion by Möbius inversion:

\[
\prod_{p\mid R}\mathbf1_{p\nmid r}
=
\sum_{e\mid R\atop e\mid r}\mu(e).
\]

Because `(e,d)=1`,

\[
\chi_D(es)=\chi_D(e)\chi_D(s).
\]

Writing `r=es` gives the exact decomposition

\[
\boxed{
P_{M,q,D}(t)
=
\sum_{e\mid R}
\mu(e)\chi_D(e)
\sum_{0\le s<M/e\atop es\equiv t\,(q)}
\chi_D(s).
}
\]

Since `e` is invertible modulo `q`, this can be written as

\[
\boxed{
P_{M,q,D}(t)
=
\sum_{e\mid R}
\mu(e)\chi_D(e)
Q_{M/e,q,D}(e^{-1}t),
}
\]

where

\[
Q_{L,q,D}(u)
:=
\sum_{0\le s<L\atop s\equiv u\,(q)}\chi_D(s).
\]

This is the correct exact replacement for a nonexistent naive CRT product formula.

The arithmetic separates into:

1. a primitive quadratic conductor `D`;
2. squarefree Möbius exclusions from the extra carrier primes;
3. incomplete additive fibers modulo `q`.

## 9. Fourier form of the conductor-Möbius decomposition

Take the `q`-point DFT of the pushforward:

\[
\mathcal P_{M,q,D}(m)
:=
\sum_{t\bmod q}P_{M,q,D}(t)e^{2\pi i mt/q}.
\]

Directly,

\[
\boxed{
\mathcal P_{M,q,D}(m)
=
\sum_{0\le r<M\atop(r,M)=1}
\chi_D(r)e^{2\pi i mr/q}.
}
\]

Applying the Möbius decomposition gives

\[
\boxed{
\mathcal P_{M,q,D}(m)
=
\sum_{e\mid R}
\mu(e)\chi_D(e)
\sum_{0\le s<M/e}
\chi_D(s)e^{2\pi i m e s/q}.
}
\]

The inner terms are incomplete mixed character/exponential sums.

This identifies the precise analytic object that must be classified to prove a full resonance theorem.

The special Gauss sum appears only after the entire finite pushforward has collapsed to an affine Legendre character; it should not be assumed at the individual conductor/exclusion stage.

## 10. Expanded exact audit

To stress-test the centered/parity theorem and the conductor formulation, the exact search was extended from the v13.233 window to

\[
3\le M\le300,
\qquad 5\le q<80,
\qquad q\nmid M,
\]

using every nonprincipal primitive quadratic discriminant `D` with `|D|\mid M`, all shifts, and both signs.

Within this finite window, 33 exact Legendre resonances were found.

Every one obeys the two new theorems:

\[
\boxed{a=(q-1)/2}
\]

and

\[
\boxed{\chi_D(-1)=(-1/q).}
\]

Moreover, within this search window the only crossing primes that occur are

\[
\boxed{q=5\quad\text{and}\quad q=7.}
\]

This last statement is an exact finite-search observation only, not a global classification theorem.

### q=5 resonances in the expanded window

The exact pairs `(M,D)` are

\[
\boxed{
(8,8),\ (17,17),\ (32,8),\ (128,8),\ (169,13).
}
\]

All have centered shift

\[
a=2
\]

and even quadratic character parity.

### q=7 resonances in the expanded window

The exact triples `(M,D,epsilon)` are

\[
\boxed{
\begin{array}{c|c|c}
M&D&\epsilon\\
\hline
20&-4&-1\\
24&-8&-1\\
30&-15&-1\\
33&-11&-1\\
88&-8&-1\\
93&-3&+1\\
110&-11&-1\\
114&-3&+1\\
132&-11&+1\\
136&-8&-1\\
136&-4&+1\\
144&-8&-1\\
148&-4&-1\\
160&-4&-1\\
171&-3&-1\\
180&-15&-1\\
180&-4&+1\\
192&-8&-1\\
201&-3&+1\\
204&-4&-1\\
219&-3&+1\\
222&-3&+1\\
240&-15&-1\\
240&-8&+1\\
240&-4&+1\\
244&-4&-1\\
285&-15&-1\\
285&-3&+1
\end{array}
}
\]

Every `q=7` case has centered shift

\[
a=3
\]

and an odd, negative-discriminant quadratic character, exactly as required by

\[
\chi_D(-1)=(-1/7)=-1.
\]

The expanded table shows that the carrier family is considerably richer than the initial six examples in v13.233, while the midpoint and parity laws remain rigid.

## 11. Relation to the Cone midpoint picture

The midpoint

\[
k_*=(q-1)/2
\]

arises here from the additive reflection

\[
k\mapsto-1-k.
\]

This is the block-time image of the carrier reflection

\[
r\mapsto M-r.
\]

It is directly analogous to the fixed-sum Cone reflection already used in the discriminant-12 geometry:

\[
r\mapsto12-r,
\qquad X\mapsto-X.
\]

The two contexts should not be identified literally, because the block variable `k` and the Cone coordinate `X` are different objects. But the same exact reflection principle is operating:

\[
\boxed{
\text{paired residues}
\longleftrightarrow
\text{reflection about a unique midpoint}.
}
\]

The newly proved centered-shift theorem therefore gives a precise reason the Legendre resonance is centered rather than arbitrarily translated.

## 12. Current classification framework

The resonance problem now has four exact filters before any search is needed.

A candidate `(M,q,D)` must satisfy:

1. **conductor condition**
   \[
   |D|\mid M;
   \]
2. **parity condition**
   \[
   \operatorname{sgn}(D)=(-1/q);
   \]
3. **center condition**
   \[
   a=(q-1)/2;
   \]
4. **collision-energy condition**
   \[
   \sum_{r\equiv s\,(q)}\chi_D(r)\chi_D(s)=q-1.
   \]

A full exact Legendre resonance then additionally requires the complete pointwise pushforward identity

\[
P_{M,q,D}(-Mk)
=
\epsilon\left(\frac{k-(q-1)/2}{q}\right).
\]

The conductor-Möbius decomposition reduces that final step to a finite combination of incomplete primitive quadratic character sums.

## 13. Guardrails

1. The midpoint and parity theorems are exact for every exact Legendre resonance in the carrier-crossing setup.
2. The conductor-Möbius formula is exact whenever `psi` is the character induced by the primitive quadratic discriminant `D` with `|D|\mid M`.
3. A naive Euler-product/CRT factorization of the additive pushforward is not valid in general.
4. The expanded `M<=300`, `q<80` resonance table is finite computational evidence, not a global classification theorem.
5. The observation that only `q=5,7` occur in that finite window is not yet promoted to a theorem.
6. The principal Discriminant-12 v0.3.5 publication baseline is unchanged.

## 14. Next task

The next exact target is to use the new centered/parity reduction and the conductor-Möbius formula to classify the two observed crossing-prime families `q=5` and `q=7` by congruence conditions on `(M,D)`.

In particular:

- solve the centered fiber equations for `q=5` and `q=7` symbolically;
- determine whether the repeated `D=8,-4,-8,-3,-11,-15,...` families are governed by residue classes of `M` modulo a finite modulus;
- separate primitive-conductor effects from extra-prime Möbius exclusions;
- then test whether the absence of `q>=11` in the expanded finite window admits a genuine obstruction theorem rather than remaining a numerical observation.

Do not revise the audited principal paper from this checkpoint alone.
