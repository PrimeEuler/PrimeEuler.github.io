# Cone Derivation Ledger v13.249 — Audit Reconciliation and Fixed-Support Bernoulli Factorization

Date: 2026-09-05
Status: AUDIT RECONCILIATION + EXACT NEW RESULT — continuation of v13.247 and v13.248; research branch remains open

## 0. Pre-write synchronization and audit reconciliation

Immediately before this write, the authoritative project README and current `master` tip were re-fetched. The current tip was

`2adddfd2bf3ddcad00468787dab4d5072cb52ed2`

with `v13.248` as the highest ledger checkpoint. That external audit verified the main `v13.238`–`v13.247` chain and identified one contained sign error in `v13.238` §8.

The authoritative correction is:

\[
\boxed{
f_{24}=-\ell_7,
\qquad
f_{240}=+\ell_7=-f_{24}.
}
\]

Thus the statement `f_240=f_24=-ell_7` in `v13.238` §8 is superseded by this correction and by `v13.248`. The substantive reachability conclusion remains correct:

\[
\boxed{24\to120\to240}
\]

is still a valid resonant return path. The error is only the sign comparison between the endpoint signals and the inaccurate attribution of that specific comparison to audit round 5.

No other correction from audit round 6 is required before continuing.

## 1. Fixed-support setup

Let `D` be a primitive nonprincipal quadratic discriminant, let

\[
d=|D|,
\]

and let `S` be a finite set of extra support primes with `p\nmid d` for every `p in S`. Put

\[
R_S=\prod_{p\in S}p,
\qquad
L=dR_S.
\]

The fixed-support periodic weight is

\[
W_{D,S}(n)
=
\chi_D(n)\prod_{p\in S}\mathbf 1_{p\nmid n}.
\]

Its period divides `L`, and on one complete period it is exactly the imprimitive quadratic Dirichlet character modulo `L` induced from `chi_D`.

Let `h>=1` contain no prime outside the support already present in `L`, so that

\[
M=Lh
\]

is an actual carrier in this fixed-support stratum. Assume throughout that

\[
q\nmid M.
\]

Define

\[
F_M(x)=\sum_{0\le n<M}W_{D,S}(n)x^n.
\]

## 2. Exact fixed-support polynomial factorization

Because `W_{D,S}` is periodic modulo `L`, write uniquely

\[
n=a+tL,
\qquad
0\le a<L,
\quad
0\le t<h.
\]

Then

\[
W_{D,S}(a+tL)=W_{D,S}(a),
\]

so

\[
\begin{aligned}
F_{Lh}(x)
&=\sum_{t=0}^{h-1}\sum_{a=0}^{L-1}W(a)x^{a+tL}\\
&=\left(\sum_{a=0}^{L-1}W(a)x^a\right)
  \left(\sum_{t=0}^{h-1}x^{tL}\right).
\end{aligned}
\]

Therefore

\[
\boxed{
F_{Lh}(x)
=F_L(x)\,G_h(x^L),
\qquad
G_h(z)=1+z+\cdots+z^{h-1}.
}
\]

This is an exact identity over `Z[x]`.

## 3. Hasse multiplicity is invariant under exponent growth

Reduce modulo `q`. Since `q\nmid h`,

\[
G_h(1)=h\not\equiv0\pmod q.
\]

Therefore `G_h(x^L)` is a unit in the local ring at `x=1`, and hence

\[
\boxed{
\operatorname{ord}_{x=1}\overline F_{Lh}(x)
=
\operatorname{ord}_{x=1}\overline F_L(x).
}
\]

Thus **existing-support exponent growth can never change the Hasse root multiplicity**.

This sharpens the fixed-support viewpoint of `v13.235`: exponent changes alter the folded crossing state, but they do not alter the local `x=1` valuation of the carrier polynomial.

If

\[
\nu=\operatorname{ord}_{x=1}\overline F_L<q,
\]

then the Hasse product rule gives

\[
\boxed{
D^{[\nu]}\overline F_{Lh}(1)
=
h\,D^{[\nu]}\overline F_L(1).
}
\]

So within a fixed-support stratum the multiplicity is constant and the first nonzero Hasse coefficient scales linearly with the cofactor residue `h mod q`.

Consequently, only **new support primes** can raise or lower the Hasse multiplicity, exactly complementing the support-adjunction valuation law of `v13.247`.

## 4. Generalized Bernoulli generating function

Let `psi_{D,S}` denote the induced Dirichlet character modulo `L` represented by `W_{D,S}`. Define its generalized Bernoulli numbers by

\[
\sum_{a=1}^{L}
\psi_{D,S}(a)
\frac{t e^{at}}{e^{Lt}-1}
=
\sum_{n\ge0}
B_{n,\psi_{D,S}}\frac{t^n}{n!}.
\]

Since

\[
F_L(e^t)=\sum_{a=1}^{L}\psi_{D,S}(a)e^{at},
\]

we obtain the exact formal identity

\[
\boxed{
F_L(e^t)
=
\frac{e^{Lt}-1}{t}
\sum_{n\ge0}B_{n,\psi_{D,S}}\frac{t^n}{n!}.
}
\]

Because the character is nonprincipal,

\[
B_{0,\psi_{D,S}}=0.
\]

Also

\[
\frac{e^{Lt}-1}{t}=L+O(t)
\]

has nonzero constant term modulo `q`, because `q\nmid L`. The change of local coordinate

\[
x=e^t,
\qquad
x-1=t+O(t^2)
\]

also has invertible linear coefficient.

Hence, below degree `q`, the root order at `x=1` is exactly the index of the first nonzero generalized Bernoulli number modulo `q`:

\[
\boxed{
\operatorname{ord}_{x=1}\overline F_L
=
\min\{n\ge1:B_{n,\psi_{D,S}}\not\equiv0\pmod q\},
}
\]

whenever the displayed minimum is `<q`.

Moreover, if the first nonzero index is `nu<q`, then

\[
\boxed{
\nu!\,D^{[\nu]}\overline F_L(1)
\equiv
L\,B_{\nu,\psi_{D,S}}
\pmod q.
}
\]

For `M=Lh`, this becomes

\[
\boxed{
\nu!\,D^{[\nu]}\overline F_M(1)
\equiv
M\,B_{\nu,\psi_{D,S}}
\pmod q.
}
\]

## 5. Exact Euler-factor decomposition

The Dirichlet `L`-series of the induced character satisfies

\[
L(s,\psi_{D,S})
=
L(s,\chi_D)
\prod_{p\in S}
\left(1-\chi_D(p)p^{-s}\right).
\]

Using

\[
L(1-n,\chi)=-\frac{B_{n,\chi}}{n}
\qquad(n\ge1),
\]

we obtain the exact rational identity

\[
\boxed{
B_{n,\psi_{D,S}}
=
B_{n,\chi_D}
\prod_{p\in S}
\left(1-\chi_D(p)p^{n-1}\right).
}
\]

Thus support growth modifies generalized Bernoulli data only through explicit Euler factors.

## 6. Bernoulli form of the half-order resonance obstruction

Let

\[
e=\frac{q-1}{2}.
\]

By `v13.247`, exact Legendre resonance requires

\[
\operatorname{ord}_{x=1}\overline F_M=e
\]

and normalized leading Hasse coefficient `+-1`.

The Bernoulli factorization therefore gives the following exact necessary conditions:

\[
\boxed{
B_{n,\chi_D}
\prod_{p\in S}
\left(1-\chi_D(p)p^{n-1}\right)
\equiv0\pmod q
\qquad(1\le n<e),
}
\]

while

\[
\boxed{
B_{e,\chi_D}
\prod_{p\in S}
\left(1-\chi_D(p)p^{e-1}\right)
\not\equiv0\pmod q.
}
\]

The leading Legendre signature sharpens this to

\[
\boxed{
M\,B_{e,\chi_D}
\prod_{p\in S}
\left(1-\chi_D(p)p^{e-1}\right)
\equiv\pm1\pmod q.
}
\]

This converts the simultaneous moment system of `v13.247` into an explicit primitive-Bernoulli times support-Euler-factor system.

## 7. At most two Hasse-admissible cofactor states per support stratum

For fixed `(D,S,q)`, define

\[
\boxed{
C_{D,S,q}
:=
L\,B_{e,\chi_D}
\prod_{p\in S}
\left(1-\chi_D(p)p^{e-1}\right)
\in\mathbf F_q.
}
\]

If the fixed support stratum can contain an exact resonance, then necessarily

\[
C_{D,S,q}\ne0.
\]

Since `M=Lh`, the normalized leading-sign condition is

\[
\boxed{hC_{D,S,q}=\pm1.}
\]

Therefore

\[
\boxed{
h\in\{+C_{D,S,q}^{-1},-C_{D,S,q}^{-1}\}
\subset\mathbf F_q^\times.
}
\]

So every fixed-support stratum has **at most two Hasse-admissible cofactor residues**.

This is a strong new finite-state reduction. The full resonance subset may be smaller, but it can never be larger than this Hasse-signature pair.

### Known examples

Exact evaluation gives:

\[
(D,S,q)=(8,\varnothing,5):
\qquad
C=1,
\]

so

\[
h=\pm1=\{1,4\},
\]

which is exactly the q=5 resonance subset.

For the original q=7 prototype,

\[
(D,S,q)=(-8,\{3\},7):
\qquad
C=1,
\]

so

\[
h=\pm1=\{1,6\},
\]

again exactly the known resonance subset.

After adjoining support prime `5`,

\[
(D,S,q)=(-8,\{3,5\},7):
\qquad
C=4,
\]

and since

\[
4^{-1}=2\pmod7,
\]

the Hasse-admissible pair is

\[
\boxed{h=\pm2=\{2,5\}.}
\]

This matches the exact resonance subset of `v13.239`. In particular `h=2` corresponds to `M=240`; the corrected endpoint signal is `+ell_7`, consistent with the round-6 audit correction.

These agreements are exact examples; the Hasse-signature pair is a necessary condition in general, not asserted to be sufficient.

## 8. Parity removes half the Bernoulli conditions automatically

For a nonprincipal primitive character,

\[
B_{n,\chi_D}=0
\qquad\text{whenever}\qquad
(-1)^n\ne\chi_D(-1).
\]

The resonance parity theorem of `v13.234` gives

\[
\chi_D(-1)
=\left(\frac{-1}{q}\right)
=(-1)^e.
\]

Therefore the primitive Bernoulli conditions of parity opposite to `e` vanish identically. Only indices

\[
\boxed{n\equiv e\pmod2}
\]

carry nontrivial information.

So the half-order Hasse obstruction consists of roughly `q/4` genuinely arithmetic Bernoulli/Euler-factor constraints, rather than `q/2` independent ones.

## 9. Which lower Bernoulli indices can support Euler factors kill safely?

Fix an active lower index

\[
1\le n<e,
\qquad
n\equiv e\pmod2.
\]

For a support prime `p`, write

\[
r=p\pmod q,
\qquad
\sigma=\chi_D(p)\in\{\pm1\}.
\]

Its Euler factor vanishes at index `n` exactly when

\[
\boxed{\sigma r^{n-1}=1.}
\]

But exact resonance also requires the same support factor to remain nonzero at index `e`:

\[
\boxed{\sigma r^{e-1}\ne1.}
\]

Eliminating `sigma`, a **safe support kill** at index `n` exists exactly when there is an `r in F_q^x` such that

\[
r^{2(n-1)}=1
\]

but

\[
r^{e-n}\ne1.
\]

Because `F_q^x` is cyclic of order `q-1=2e`, the subgroup of roots of

\[
x^{2(n-1)}=1
\]

has order

\[
g_n=\gcd(2(n-1),q-1).
\]

Every element of that subgroup satisfies `r^{e-n}=1` if and only if

\[
g_n\mid(e-n).
\]

Therefore define the **support-uncoverable index set**

\[
\boxed{
\mathcal U_q
=
\left\{
1\le n<e:
 n\equiv e\pmod2,
\ \gcd(2(n-1),q-1)\mid(e-n)
\right\}.
}
\]

For `n in U_q`, no possible local support label `(r,sigma)` can make the `n`-th Euler factor vanish without also killing the required nonzero `e`-th factor.

Hence exact resonance forces a purely primitive generalized-Bernoulli divisibility:

\[
\boxed{
q\mid B_{n,\chi_D}
\qquad
\text{for every }n\in\mathcal U_q.
}
\]

This condition is independent of the size of the support set and cannot be engineered away by adding more support primes.

## 10. Universal low-index divisibility corollaries

### Case 1: `q = 1 mod 4`

Then `e` is even and `n=2` is active. We have

\[
\gcd(2,q-1)=2,
\]

and

\[
e-2\equiv0\pmod2.
\]

Thus

\[
2\in\mathcal U_q.
\]

Therefore every exact resonance with `q=1 mod 4` must satisfy

\[
\boxed{q\mid B_{2,\chi_D}.}
\]

Equivalently: the first nontrivial even primitive generalized Bernoulli number must be `q`-divisible before support growth can even be considered.

### Case 2: `q = 3 mod 4`, `q>=11`

Then `e` is odd and `n=3` is active. Since `e` is odd,

\[
\gcd(4,q-1)=2,
\]

and

\[
e-3\equiv0\pmod2.
\]

Thus

\[
3\in\mathcal U_q.
\]

Therefore every exact resonance with `q=3 mod 4`, `q>=11`, must satisfy

\[
\boxed{q\mid B_{3,\chi_D}.}
\]

These are universal necessary conditions for isolated higher-prime resonance.

They do not by themselves rule out all primitive discriminants: generalized Bernoulli divisibility can occur. Their value is that they move an unavoidable part of the obstruction completely into the primitive quadratic character, beyond the reach of support engineering.

## 11. First support-uncoverable sets

The exact group criterion gives, for the first higher crossing primes:

\[
\begin{array}{c|c|c}
q&e&\mathcal U_q\\
\hline
11&5&\{3\}\\
13&6&\{2\}\\
17&8&\{2,4,6\}\\
19&9&\{3,5\}\\
23&11&\{3,5,7,9\}\\
29&14&\{2,4,6,10,12\}\\
31&15&\{3,5,9\}
\end{array}
\]

Thus, for example, a hypothetical `q=23` resonance would require simultaneous primitive divisibility

\[
23\mid B_{3,\chi_D},
\quad
23\mid B_{5,\chi_D},
\quad
23\mid B_{7,\chi_D},
\quad
23\mid B_{9,\chi_D},
\]

while still requiring the `e=11` generalized Bernoulli/Euler product to remain nonzero and satisfy the normalized leading-sign congruence.

This is substantially sharper than the raw statement that eleven Hasse derivatives must vanish: parity and support-factor freedom are now separated exactly from the primitive obstructions that cannot be removed.

## 12. Structural interpretation

The Hasse obstruction now splits into three independent layers:

\[
\boxed{
\text{primitive Bernoulli divisibility}
\quad+\quad
\text{support Euler-factor covering}
\quad+\quad
\text{two-state cofactor signature}.
}
\]

More explicitly:

1. `U_q` identifies lower indices that **must** vanish primitively;
2. the remaining active indices may be killed either primitively or by selected support labels;
3. once the half-order `e` survives, the leading Hasse signature restricts `h` to at most two residues modulo `q`.

This replaces the open-ended moment-polynomial system proposed at the end of `v13.247` by a much more rigid arithmetic classification.

## 13. What is proved and what remains open

Proved exactly in this entry:

- audit-round-6 sign correction is reconciled and authoritative;
- fixed-support carrier polynomials factor as `F_{Lh}=F_L G_h(x^L)`;
- Hasse multiplicity is invariant under existing-support exponent growth;
- the leading Hasse coefficient scales by `h`;
- Hasse multiplicity is controlled by generalized Bernoulli numbers of the induced character;
- induced generalized Bernoulli numbers factor into primitive values times explicit support Euler factors;
- exact resonance permits at most two Hasse-admissible cofactor residues in each fixed support stratum;
- the support-uncoverable index criterion is
  \[
  \gcd(2(n-1),q-1)\mid(e-n);
  \]
- every uncoverable index forces primitive generalized-Bernoulli divisibility;
- universally, `q=1 mod 4` forces `q|B_{2,chi_D}`, while `q=3 mod 4`, `q>=11`, forces `q|B_{3,chi_D}`.

Still open:

\[
\boxed{
q\ge11
\Longrightarrow
\text{no exact Legendre resonance}.
}
\]

Generalized Bernoulli divisibility can occur, so a final no-resonance theorem will require combining the forced primitive-divisibility pattern with additional structure, rather than assuming those divisibilities never happen.

## 14. Next theorem target

The next natural question is whether the simultaneous divisibilities

\[
q\mid B_{n,\chi_D}
\qquad(n\in\mathcal U_q)
\]

can themselves be characterized through the reduction of the primitive character polynomial

\[
F_d(x)=\sum_{a=0}^{d-1}\chi_D(a)x^a
\]

or through the finite-field moments of `chi_D mod q`.

A particularly promising route is to study the primitive Hasse order

\[
\nu_0(D,q)
=
\operatorname{ord}_{x=1}\overline F_d(x)
\]

and ask how large it can be before any support Euler factors are introduced. The support-uncoverable set says that certain gaps in the primitive Bernoulli sequence are mandatory regardless of later support growth.

The goal is now sharper than the previous moment-polynomial problem:

\[
\boxed{
\text{classify primitive quadratic characters whose generalized Bernoulli sequence}
\text{ has all forced }\mathcal U_q\text{ divisibilities mod }q.
}
\]

If those primitive patterns can be ruled out, or shown incompatible with the surviving `e`-th signature, then the isolated-resonance problem closes globally.

## 15. Checkpoint

The current obstruction chain is

\[
\boxed{
\text{exact Legendre resonance}
\Longrightarrow
\begin{cases}
\dim V_q=2 & \text{only for }q=5,7,\\
\operatorname{ord}_{x=1}\overline F=e,\\
B_{n,\chi_D}\prod_{p\in S}(1-\chi_D(p)p^{n-1})=0 & (n<e),\\
hC_{D,S,q}=\pm1,\\
q\mid B_{n,\chi_D} & (n\in\mathcal U_q).
\end{cases}
}
\]

For the known `q=5,7` resonances, the two-state Hasse signature reproduces the exact observed cofactor pairs. For every `q>=11`, any isolated resonance must now satisfy a growing family of primitive generalized-Bernoulli divisibilities that no choice of support primes can evade.