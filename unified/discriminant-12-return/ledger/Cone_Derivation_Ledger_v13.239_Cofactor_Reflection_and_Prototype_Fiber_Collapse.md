# Cone Derivation Ledger v13.239 — Cofactor Reflection and Prototype-Fiber Collapse

Date: 2026-09-05
Status: EXACT NEW RESULT + FINITE CLASSIFICATION OF CURRENT RESONANCE STRATA — continuation of v13.238; research branch remains open

## 0. Pre-write synchronization

Immediately before this write, the authoritative README and current `master` tip were re-fetched. The tip remained

`78da06bbe4a0ea121951e03c633a74d03ce7c020`

with v13.238 as the highest ledger checkpoint. No newer external-audit checkpoint had landed after v13.237. This entry extends the reconciled research branch and does not revise the audited principal v0.3.5 paper.

## 1. Fixed-support formal fiber

Let

\[
\chi_D(n)=\left(\frac Dn\right)
\]

be a primitive nonprincipal quadratic Kronecker character of conductor `d=|D|`. Fix an extra-prime support set `S`, put

\[
R_S=\prod_{p\in S}p,
\qquad
L=dR_S,
\]

and define the periodic zero-extended support weight

\[
W(n)=\chi_D(n)\prod_{p\in S}{\bf1}_{p\nmid n}.
\]

For `h=1,...,q-1`, define the fixed-support pushforward

\[
P_h(t)=\sum_{0\le n<Lh\atop n\equiv t\,(q)}W(n),
\]

and the associated formal fiber signal

\[
\boxed{f_h(k)=P_h(-Lhk).}
\]

When `h` is represented by an exponent multiplier using only primes already dividing `L`, this is the actual carrier signal of v13.235/v13.238. For other residue classes it is best regarded as the canonical fixed-support formal fiber state; it does **not** mean that an arbitrary integer representative introducing a new prime remains in the same support stratum.

This guardrail makes the decorated-fiber notation precise.

## 2. Cofactor-reflection theorem

The support weight has period `L` and zero mean over one period:

\[
\sum_{a=0}^{L-1}W(a)=0.
\]

Fix `1\le h\le q-1`. For each `t mod q`, the total contribution over the complete interval `[0,qL)` vanishes:

\[
\sum_{0\le n<qL\atop n\equiv t\,(q)}W(n)=0,
\]

because the CRT identifies the `L` terms in the fiber with every residue modulo `L` exactly once.

Hence

\[
P_{q-h}(t)
=-\sum_{L(q-h)\le n<qL\atop n\equiv t\,(q)}W(n).
\]

Set `n=qL-m`. Then the tail is transformed to `1\le m\le Lh`. Since `W` is periodic modulo `L`,

\[
W(qL-m)=W(-m)=\chi_D(-1)W(m).
\]

The endpoint replacement from `m=1,...,Lh` to `m=0,...,Lh-1` is harmless because both `W(0)` and `W(Lh)` vanish: the conductor `d` divides `L`.

The congruence `n=t mod q` becomes `m=-t mod q`. Therefore

\[
\boxed{
P_{q-h}(t)=-\chi_D(-1)P_h(-t).
}
\]

Now evaluate at `t=-L(q-h)k\equiv Lhk mod q`:

\[
\begin{aligned}
f_{q-h}(k)
&=P_{q-h}(Lhk)\\
&=-\chi_D(-1)P_h(-Lhk)\\
&=-\chi_D(-1)f_h(k).
\end{aligned}
\]

Thus the exact cofactor-reflection law is

\[
\boxed{
f_{q-h}=-\chi_D(-1)f_h.
}
\]

This is distinct from the block-time reflection `k->-1-k` of v13.234. The present theorem reflects the **cofactor label** `h->q-h`.

## 3. Consequence under the resonance parity rule

For any exact Legendre-resonant stratum, v13.234 proved

\[
\chi_D(-1)=\left(\frac{-1}{q}\right).
\]

Therefore

\[
\boxed{
f_{q-h}=-\left(\frac{-1}{q}\right)f_h.}
\]

So:

- if `q=1 mod 4`, then `f_{q-h}=-f_h`;
- if `q=3 mod 4`, then `f_{q-h}=f_h`.

In particular:

\[
q=5:\quad f_{5-h}=-f_h,
\]

while

\[
q=7:\quad f_{7-h}=f_h.
\]

Thus the formal cofactor fiber reduces projectively from `q-1` labels to only `(q-1)/2` labels.

For the two observed crossing primes this means:

\[
\boxed{q=5:\ 2\text{ projective cofactor states},}
\]

\[
\boxed{q=7:\ 3\text{ projective cofactor states}.}
\]

## 4. Prototype q=5 fiber

Take the basic resonant stratum

\[
(D,S,q)=(8,\varnothing,5).
\]

Its complete fixed-support fiber is

\[
\begin{array}{c|c}
h&f_h\\
\hline
1&(-1,1,0,1,-1)\\
2&(0,1,-2,1,0)\\
3&(0,-1,2,-1,0)\\
4&(1,-1,0,-1,1)
\end{array}
\]

and indeed

\[
f_4=-f_1,
\qquad
f_3=-f_2.
\]

Writing the centered Legendre vector as

\[
\ell_5=(-1,1,0,1,-1),
\]

the resonant set is

\[
\boxed{\mathcal R=\{1,4\},}
\]

with opposite resonance signs at the reflected cofactor labels.

## 5. Prototype q=7 fiber

Take the original discriminant-12-adjacent resonance stratum

\[
(D,S,q)=(-8,\{3\},7).
\]

Its complete fixed-support fiber is

\[
\begin{array}{c|c}
h&f_h\\
\hline
1&(-1,1,1,0,-1,-1,1)\\
2&(0,1,-2,0,2,-1,0)\\
3&(1,-2,1,0,-1,2,-1)\\
4&(1,-2,1,0,-1,2,-1)\\
5&(0,1,-2,0,2,-1,0)\\
6&(-1,1,1,0,-1,-1,1)
\end{array}
\]

so

\[
f_6=f_1,
\qquad
f_5=f_2,
\qquad
f_4=f_3.
\]

For

\[
\ell_7=(1,-1,-1,0,1,1,-1),
\]

we have

\[
f_1=f_6=-\ell_7,
\]

and therefore

\[
\boxed{\mathcal R=\{1,6\}.}
\]

The other two projective cofactor classes carry the two nonresonant prototype shapes shown above.

## 6. Fiber-equivalence relation

For fixed `q`, define an equivalence on decorated formal fibers by

\[
\boxed{
\Phi'\sim\Phi
\iff
\exists u\in\mathbf F_q^\times,\ \delta\in\{\pm1\}
\text{ such that }
\Phi'(h)=\delta\Phi(uh)
\text{ for every }h.
}
\]

This allows only:

1. a multiplicative relabelling of the cofactor coordinate `h`;
2. one global signal sign.

It does **not** relabel the block variable `k` and does not change the crossing prime.

If `\Phi'\sim\Phi`, then the resonant subset transforms exactly as

\[
\boxed{
\mathcal R_{\Phi'}=u^{-1}\mathcal R_{\Phi}.
}
\]

The global sign `delta` changes the `+/-` resonance label but not membership in the resonant subset.

## 7. Exact collapse of all current q=5 resonance strata

The expanded audit of v13.234 contains three distinct `q=5` support strata among the resonant examples:

\[
(D,S)=(8,\varnothing),\ (17,\varnothing),\ (13,\varnothing).
\]

Exact evaluation of all four cofactor states gives:

- `(8,empty)` = the prototype exactly;
- `(17,empty)` = the prototype exactly;
- `(13,empty)` satisfies
  \[
  \Phi_{13}(h)=-\Phi_8(2h).
  \]

Equivalently one may use `u=3,delta=+1` for the last row.

Therefore

\[
\boxed{
\text{all q=5 support strata represented in the current 33-resonance table lie in one decorated-fiber equivalence class.}
}
\]

Their resonance pair is merely moved multiplicatively among the two projective cofactor classes.

## 8. Exact collapse of all current q=7 resonance strata

The 28 `q=7` resonant carriers in v13.234 occupy 22 distinct `(D,S)` support strata. Exact evaluation of all six cofactor states shows that **every one** is equivalent to the prototype

\[
\Phi_*:=\Phi_{-8,\{3\},7}.
\]

A canonical set of equivalence representatives is:

\[
\begin{array}{c|c|c|c}
D&S&u&\delta\\
\hline
-11&\{2,3\}&3&-1\\
-11&\{2,5\}&1&+1\\
-11&\{3\}&1&+1\\
-15&\{19\}&1&+1\\
-15&\{2\}&1&+1\\
-3&\{19\}&2&+1\\
-3&\{2,19\}&1&-1\\
-3&\{2,37\}&1&-1\\
-3&\{31\}&1&-1\\
-3&\{5,19\}&1&-1\\
-3&\{67\}&1&-1\\
-3&\{73\}&1&-1\\
-4&\{17\}&3&-1\\
-4&\{3,17\}&1&+1\\
-4&\{3,5\}&2&-1\\
-4&\{37\}&1&+1\\
-4&\{5\}&1&+1\\
-4&\{61\}&1&+1\\
-8&\{11\}&1&+1\\
-8&\{17\}&1&+1\\
-8&\{3,5\}&3&-1\\
-8&\{3\}&1&+1
\end{array}
\]

where each row means

\[
\boxed{
\Phi_{D,S,7}(h)=\delta\Phi_*(uh).
}
\]

Thus

\[
\boxed{
\text{all 22 q=7 support strata occurring in the current 33-resonance table collapse to one prototype decorated fiber.}
}
\]

This is an exact finite classification of the **currently observed resonant strata**, not a theorem that every possible q=7 support set has prototype type.

## 9. What the collapse means

The expanded resonance list looked arithmetically heterogeneous:

\[
D=-3,-4,-8,-11,-15
\]

with many different support sets. At the level of the complete six-state cofactor fiber, however, every observed q=7 resonant support stratum contains exactly the same three projective signal shapes, up to cofactor multiplication and global sign.

Likewise all current q=5 resonant strata contain exactly the same two projective signal shapes.

So the current data exhibit a much stronger compression than the raw `(M,D)` table suggests:

\[
\boxed{
\text{33 resonant carriers}
\longrightarrow
\begin{cases}
1\text{ prototype decorated-fiber class at }q=5,\\
1\text{ prototype decorated-fiber class at }q=7.
\end{cases}
}
\]

This is precisely the kind of quotient structure anticipated in v13.238, but only on the finite family currently certified by the search.

## 10. Relation to resonance-return paths

For the original q=7 prototype, the resonance pair is `h=+/-1`. For the enlarged support `(-8,{3,5})`, the equivalence

\[
\Phi_{-8,\{3,5\},7}(h)=-\Phi_*(3h)
\]

moves the resonance pair to

\[
3h=\pm1
\iff
h=\pm5=\{2,5\}.
\]

Hence

\[
\boxed{\mathcal R_{-8,\{3,5\},7}=\{2,5\},}
\]

which gives the exact v13.238 return

\[
24\to120\to240
\]

because the post-adjunction state starts at `h=1` and one exponent increment of `2` reaches the resonant state `h=2`.

Thus the prototype equivalence records the resonance-return location directly.

## 11. New exact reduction of the classification problem

For a support stratum that is prototype-equivalent, the full `q-1`-state resonance test is unnecessary once `(u,delta)` is known. The resonance subset is transported from the prototype by

\[
\mathcal R=u^{-1}\mathcal R_*.
\]

For q=7,

\[
\mathcal R_*=\{1,6\},
\]

so every observed resonant stratum has a resonance pair of the form

\[
\boxed{\{u^{-1},-u^{-1}\}.}
\]

For q=5 the same formula holds, with the reflected pair carrying opposite signal signs.

This converts the known return problem from comparing full vectors to identifying one multiplicative cofactor phase `u`.

## 12. Guardrails

1. The cofactor-reflection theorem is exact for every fixed-support formal fiber with primitive nonprincipal `chi_D` and `(q,L)=1`.
2. The decorated fiber on all `h in F_q^*` is a canonical formal extension; actual exponent reachability remains restricted to the subgroup/coset `H_S(q)` of v13.238.
3. The one-prototype collapse is proved here only for the distinct support strata represented in the current finite 33-resonance table.
4. No claim is made yet that arbitrary new support histories at q=5 or q=7 remain in the prototype class.
5. The equivalence permits cofactor relabelling and global signal sign only; it does not identify different block-coordinate dynamics indiscriminately.
6. The audited principal v0.3.5 theorem package is unchanged.

## 13. Next task

The next exact question is whether prototype equivalence is **closed under support-prime adjunction followed by cofactor rephasing**.

Starting from a prototype fiber `Phi`, apply a new-support operator `T_{r,sigma}` and then compute the full cofactor fiber of the enlarged stratum. Determine for which local labels `(r,sigma)` the enlarged fiber is again equivalent to `Phi`, and identify the induced multiplier `u` on the resonance pair.

For q=5 and q=7 this is a finite operator-alphabet calculation. If the prototype class is closed under a precisely characterized subset of support labels, that would produce a genuine finite quotient automaton **for the resonant prototype sector**, without making the false claim that the entire global support graph is finite.