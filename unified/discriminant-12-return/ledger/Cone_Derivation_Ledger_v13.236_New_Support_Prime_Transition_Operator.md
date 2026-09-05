# Cone Derivation Ledger v13.236 — New-Support-Prime Transition Operator

Date: 2026-09-04
Status: EXACT NEW RESULT — continuation of v13.235; research branch remains open

## 0. Pre-write synchronization

Immediately before this write, the authoritative project README, current `master` tip, and v13.235 were re-fetched. The tip remained

`3cfcb9d6969133beb400ffe1e4935b5a630c0d5c`

with v13.235 as the highest ledger checkpoint. No newer external-audit checkpoint had landed. This entry extends the reconciled research branch and does not revise the audited principal v0.3.5 paper.

## 1. Setup

Let

\[
\chi_D(n)=\left(\frac Dn\right)
\]

be a primitive nonprincipal quadratic Kronecker character of fundamental discriminant `D`. Fix a current radical-support stratum with carrier modulus

\[
M=Lh,
\]

where `L` contains the conductor `|D|` and the currently active extra support primes. Let

\[
W(n)
\]

be the corresponding zero-extended carrier weight; equivalently, on `0<=n<M`, `W(n)=\chi_D(n)` when `(n,M)=1` and `0` otherwise.

Let `q` be an odd prime with `(q,M)=1`. Define the additive pushforward

\[
P_M(t)=\sum_{0\le n<M\atop n\equiv t\,(q)}W(n),
\qquad t\in\mathbf F_q,
\]

and the crossing signal

\[
\boxed{f_M(k)=P_M(-Mk)}.
\]

Now let `p` be a genuinely new support prime:

\[
p\nmid Mq.
\]

The enlarged carrier modulus is

\[
M'=pM,
\]

and its weight is

\[
W'(n)=W(n)\mathbf 1_{p\nmid n}.
\]

Because `p` is outside the primitive conductor and current support,

\[
\sigma_p:=\chi_D(p)\in\{\pm1\}.
\]

## 2. Exact decomposition of the enlarged interval

Every integer `0<=n<pM` has a unique representation

\[
n=a+jM,
\qquad 0\le a<M,
\qquad 0\le j<p.
\]

Since the old weight is periodic modulo the support period dividing `M`,

\[
W(a+jM)=W(a).
\]

Before removing the new multiples of `p`, the enlarged pushforward therefore contributes

\[
\sum_{j=0}^{p-1}P_M(t-jM).
\]

The terms that must be removed are exactly the multiples

\[
n=ps,
\qquad 0\le s<M.
\]

Because `p` is coprime to the old support,

\[
W(ps)=\chi_D(p)W(s)=\sigma_pW(s).
\]

The congruence `ps=t mod q` is equivalent to

\[
s\equiv p^{-1}t\pmod q.
\]

Hence the excluded contribution is

\[
\sigma_pP_M(p^{-1}t).
\]

Therefore the exact new-support-prime transition in pushforward coordinates is

\[
\boxed{
P_{pM}(t)
=
\sum_{j=0}^{p-1}P_M(t-jM)
-
\chi_D(p)P_M(p^{-1}t).
}
\]

This is the exact operator that was missing from v13.235.

## 3. Reduction to `p mod q`

Write

\[
p=aq+r,
\qquad 1\le r\le q-1.
\]

Since the old character is nonprincipal,

\[
\sum_{t\in\mathbf F_q}P_M(t)=0.
\]

As `jM mod q` runs through a complete `q`-cycle, the corresponding translate sum contributes zero. Therefore all `a` complete cycles disappear and only the remainder `r=p mod q` survives:

\[
\boxed{
P_{pM}(t)
=
\sum_{j=0}^{r-1}P_M(t-jM)
-
\chi_D(p)P_M(p^{-1}t),
\qquad r\equiv p\pmod q.
}
\]

Thus the support transition depends on the new prime only through

\[
\boxed{p\bmod q\quad\text{and}\quad\chi_D(p).}
\]

This is a finite local label.

## 4. Crossing-signal transition operator

Evaluate the pushforward identity at

\[
t=-pMk.
\]

Because

\[
f_M(x)=P_M(-Mx),
\]

we obtain

\[
P_M(-pMk-jM)=f_M(pk+j),
\]

while

\[
P_M(p^{-1}(-pMk))=P_M(-Mk)=f_M(k).
\]

Therefore

\[
\boxed{
f_{pM}(k)
=
\sum_{j=0}^{r-1}f_M(rk+j)
-
\chi_D(p)f_M(k),
\qquad r=p\bmod q.
}
\]

Define the finite operator

\[
\boxed{
(T_{r,\sigma}f)(k)
:=
\sum_{j=0}^{r-1}f(rk+j)-\sigma f(k),
}
\]

with

\[
r\in\mathbf F_q^\times,
\qquad \sigma\in\{\pm1\}.
\]

Then every genuinely new support prime acts by

\[
\boxed{f_{pM}=T_{p\bmod q,\,\chi_D(p)}f_M.}
\]

This is an exact finite-state support-prime operator.

## 5. Direct checks on the known resonance examples

For the original discriminant-12 carrier resonance

\[
(M,q,D)=(24,7,-8),
\]

one has

\[
f_{24}=(-1,1,1,0,-1,-1,1).
\]

Adding the new support prime `p=5` gives `r=5` and `chi_{-8}(5)=-1`, hence

\[
T_{5,-1}f_{24}
=(-1,2,-1,0,1,-2,1),
\]

which agrees with the direct carrier computation for `M=120`.

Adding `p=11` gives the direct match

\[
T_{4,\chi_{-8}(11)}f_{24}
=(2,-3,0,0,0,3,-2),
\]

for `M=264`.

Likewise the `q=5,D=8,M=8` resonance transitions correctly under new support primes such as `p=3` and `p=7`.

These checks are confirmations of the exact derivation, not the basis of the theorem.

## 6. Fourier-space form

Use the unnormalized DFT convention

\[
\widehat f(m)=\sum_{k\bmod q}f(k)\zeta_q^{mk},
\qquad \zeta_q=e^{2\pi i/q}.
\]

For the averaging part

\[
(A_rf)(k):=\sum_{j=0}^{r-1}f(rk+j),
\]

put `x=rk+j`. Since `r` is invertible modulo `q`,

\[
\begin{aligned}
\widehat{A_rf}(m)
&=
\sum_{j=0}^{r-1}\zeta_q^{-mr^{-1}j}
\widehat f(mr^{-1}).
\end{aligned}
\]

Define

\[
D_r(m):=
\sum_{j=0}^{r-1}\zeta_q^{-mr^{-1}j}.
\]

Then

\[
\boxed{
\widehat{T_{r,\sigma}f}(m)
=
D_r(m)\widehat f(mr^{-1})
-
\sigma\widehat f(m).
}
\]

At zero frequency,

\[
D_r(0)=r,
\]

and since every nonprincipal carrier signal has `widehat f(0)=0`, the new-support transition preserves zero DC exactly.

Thus the support-prime operator is sparse in crossing-time coordinates and becomes a frequency permutation multiplied by a finite geometric sum, followed by subtraction of the character sign.

## 7. New theorem: a single new support prime cannot carry a Legendre resonance directly to another Legendre resonance

Suppose the old signal is an exact centered Legendre resonance

\[
f(k)=\epsilon\lambda_q(k-a),
\qquad
\lambda_q(x)=\left(\frac{x}{q}\right),
\qquad
a=\frac{q-1}{2}.
\]

By v13.234, any exact resonance at the same `q,D` has the same forced center `a` and therefore must be

\[
\epsilon'\lambda_q(k-a)
\]

for some `epsilon'=+/-1`.

For nonzero frequency `m`, the quadratic Gauss formula gives

\[
\widehat f(m)
=C\,\lambda_q(m)\zeta_q^{ma}
\]

for a nonzero constant `C` independent of `m`. Hence

\[
\frac{\widehat f(mr^{-1})}{\widehat f(m)}
=
\lambda_q(r)
\zeta_q^{ma(r^{-1}-1)}.
\]

If `T_{r,sigma}f` were again `+/-f`, then for every `m neq0`

\[
\lambda_q(r)
D_r(m)
\zeta_q^{ma(r^{-1}-1)}
-
\sigma
\]

would have to be a constant `+1` or `-1`, independent of `m`.

But

\[
D_r(m)
\zeta_q^{ma(r^{-1}-1)}
=
\sum_{j=0}^{r-1}
\zeta_q^{m\left(a(r^{-1}-1)-r^{-1}j\right)}
\]

is a sum of exactly `r<q` distinct additive characters. Viewed as a function on the nontrivial `q`th roots of unity, it cannot be constant: if it were constant on all `q-1` nontrivial roots, the corresponding coefficient vector in the group algebra of `Z/qZ` would differ from a constant function by a multiple of

\[
1+z+\cdots+z^{q-1},
\]

which is impossible because only `r<q` Fourier coefficients are present with equal nonzero coefficient.

The exceptional case `r=1` is immediate:

\[
T_{1,\sigma}f=(1-\sigma)f,
\]

which is either `0` or `2f`, never `+/-f`.

Therefore

\[
\boxed{
\text{one genuinely new support-prime step never maps an exact Legendre resonance directly to another exact Legendre resonance.}
}
\]

This holds for every odd crossing prime `q`, not merely `q=5,7`.

## 8. Consequence for the resonance graph

The finite-state classification now separates two kinds of motion.

### 8.1 Exponent motion inside a fixed support stratum

By v13.235, changing exponents changes only

\[
h=M/L\pmod q.
\]

In particular, factors `c=1 mod q` built from existing support primes preserve the signal exactly and generate infinite towers.

### 8.2 New-support motion

Adding a genuinely new prime `p` keeps the old cofactor state but changes the signal by

\[
T_{p\bmod q,\chi_D(p)}.
\]

The theorem above says that a resonant state cannot move directly to another resonant state by this support edge alone.

Therefore any appearance of a resonance on a larger support set must have the pattern

\[
\boxed{
\text{resonant state}
\xrightarrow{\text{new support prime}}
\text{nonresonant state}
\xrightarrow{\text{exponent-state motion}}
\text{possibly resonant state}.
}
\]

The original `D=-8,q=7` family illustrates this exactly:

\[
24\xrightarrow{\times5}120
\]

is nonresonant, while an exponent move inside the new support stratum gives

\[
120\xrightarrow{\times2}240,
\]

and `M=240,D=-8,q=7` is resonant according to the v13.234 audit.

So the larger-support resonance is not a direct preservation of the `M=24` Legendre mode; the support transition first leaves the resonance manifold and the finite cofactor dynamics later returns to it.

## 9. Finite directed-state formulation

For fixed `(D,q)`, a state can now be represented by

\[
\boxed{(S,h)},
\]

where `S` is the set of extra support primes and

\[
h=M/(|D|R_S)\pmod q.
\]

There are two exact edge types:

1. **existing-support exponent edge**
   \[
   (S,h)\to(S,ch),
   \qquad \operatorname{rad}(c)\subseteq \operatorname{rad}(|D|R_S);
   \]
2. **new-support edge** for `p notin S`, `p notmid Dq`
   \[
   (S,h)\to(S\cup\{p\},h),
   \]
   carrying the signal operator
   \[
   T_{p\bmod q,\chi_D(p)}.
   \]

The new-prime label itself collapses to the finite pair

\[
\boxed{(p\bmod q,\chi_D(p)).}
\]

Hence, once a bounded support alphabet is chosen, the resonance problem is an explicit finite directed graph with exact linear operators on `q`-component signal vectors.

## 10. Structural meaning

The classification problem has now been decomposed into three independent finite mechanisms:

\[
\boxed{
\text{quadratic conductor }D,
}
\]

\[
\boxed{
\text{cofactor state }h\bmod q,
}
\]

and

\[
\boxed{
\text{support-prime transition label }(p\bmod q,\chi_D(p)).
}
\]

This is the first exact operator calculus for changing the radical support of the carrier.

The result also clarifies the role of quadratic reciprocity: `chi_D(p)` controls the subtraction term, while `p mod q` controls the finite affine averaging/permutation term. The support transition therefore couples two quadratic/arithmetic data streams but does not identify them.

## 11. Guardrails

1. The operator `T_{r,sigma}` applies when `p` is genuinely new support: `p notmid Mq`.
2. Existing-support exponent changes are governed by v13.235 and must not be conflated with new-support transitions.
3. The no-direct-resonance theorem concerns one support-prime step with the same fixed `(D,q)`; a later exponent-state move can restore resonance.
4. The Fourier operator is a finite change-of-basis description, not a physical time-evolution Hamiltonian.
5. This checkpoint does not alter the audited principal Discriminant-12 v0.3.5 theorem package.

## 12. Next task

The next exact target is to construct the finite resonance graphs explicitly for the two observed crossing primes `q=5` and `q=7`.

For each relevant primitive discriminant family:

- enumerate the `h mod q` states of each support stratum;
- use `T_{r,sigma}` for every possible new-support label `(r,sigma)`;
- use multiplication by existing support residues for exponent-state motion;
- mark exactly which states equal the centered Legendre vector;
- identify minimal cycles or return paths from resonance through nonresonant support transitions back to resonance.

That should reveal whether the observed `q=5` and `q=7` families are generated by a small finite automaton, and it gives a precise framework for proving or disproving the apparent absence of `q>=11` resonances.