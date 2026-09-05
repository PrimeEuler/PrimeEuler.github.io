# Cone Derivation Ledger v13.241 — Determinantal-Divisor No-Return Theorem

Date: 2026-09-05
Status: EXACT NEW RESULT — continuation of v13.240; research branch remains open

## 0. Pre-write synchronization

Immediately before this write, the authoritative project README, current `master` tip, and v13.240 were re-fetched. The tip remained

`60d6b9abc97a073779fe9b6f811527622cf706a1`

with v13.240 as the highest ledger checkpoint. No newer external-audit checkpoint had landed after v13.237. This entry extends the reconciled research branch and does not revise the audited principal v0.3.5 paper.

## 1. Question left by v13.240

v13.240 classified the one-step prototype-preserving support labels at `q=7` and found the exact preserving alphabet

\[
\mathcal A_7^{\rm pres}
=
\{(2,-1),(3,-1),(4,-1),(5,-1)\}.
\]

It left open the possibility that a support word could leave the prototype sector through a nonpreserving label and later return after additional support-prime adjunctions.

The present entry proves that this cannot happen.

The same invariant also strengthens the `q=5` statement: starting from the basic `D=8` prototype, no nonempty support-prime word can ever return to its decorated-fiber equivalence class.

## 2. Fiber matrix

For a fixed crossing prime `q`, write a decorated fiber as

\[
\Phi=(f_h)_{h\in\mathbf F_q^\times},
\qquad
f_h\in\mathbf Z^q.
\]

Arrange the signal vectors as columns of the integer matrix

\[
\boxed{
F_\Phi
=
\begin{bmatrix}
|&&|\\
f_1&\cdots&f_{q-1}\\
|&&|
\end{bmatrix}
\in M_{q\times(q-1)}(\mathbf Z).
}
\]

The support operator `T_{r,\sigma}` is an integer linear operator on `\mathbf Z^q`, so there is an integer matrix `A_{r,\sigma}` with

\[
F_{T_{r,\sigma}\Phi}=A_{r,\sigma}F_\Phi.
\]

## 3. Second determinantal divisor

For any integer matrix `F` of rank at least two, define its second determinantal divisor

\[
\boxed{
\Delta_2(F)
:=
\gcd\{\text{all }2\times2\text{ minors of }F\}.
}
\]

If `\operatorname{rank}F<2`, set

\[
\Delta_2(F)=0.
\]

This is the second Smith determinantal divisor. It measures the integral content of the rank-two exterior lattice carried by the columns.

For the two prototypes of v13.239, the fiber matrices both have rank two and

\[
\boxed{\Delta_2(F_{\Phi_5})=1,
\qquad
\Delta_2(F_{\Phi_7})=1.}
\]

## 4. Monotonic divisibility under integer signal operators

Let `A` be any integer matrix and `F` any integer matrix. By the Cauchy--Binet formula, every `2\times2` minor of `AF` is an integer linear combination of the `2\times2` minors of `F`.

Therefore

\[
\boxed{
\Delta_2(F)\mid\Delta_2(AF)
}
\]

whenever the right side is nonzero; if the rank drops below two, `\Delta_2(AF)=0` and rank can never be restored by later left multiplication.

Thus along any support word

\[
F_0\mapsto F_1\mapsto\cdots\mapsto F_m
\]

we have a one-way divisibility obstruction:

\[
\boxed{
\Delta_2(F_0)\mid\Delta_2(F_1)\mid\cdots
}
\]

until a possible rank drop, after which return to a rank-two prototype is impossible.

In particular, once `\Delta_2` becomes a proper multiple of 1, it can never return to 1 under further integer support operators.

## 5. Invariance under decorated-fiber equivalence

The v13.239 equivalence relation is

\[
\Phi'(h)=\delta\Phi(uh),
\qquad
u:=u\in\mathbf F_q^\times,
\qquad
\delta\in\{\pm1\}.
\]

On the fiber matrix this is only a column permutation together with a global sign:

\[
F_{\Phi'}=\delta F_\Phi P_u,
\]

where `P_u` is a permutation matrix.

Hence

\[
\boxed{
\Delta_2(F_{\Phi'})=\Delta_2(F_\Phi).
}
\]

Therefore `\Delta_2=1` is a necessary invariant of the entire prototype equivalence class.

## 6. Exact q=7 table

Use the original prototype

\[
\Phi_*=\Phi_{-8,\{3\},7}.
\]

Direct exact evaluation of all twelve support labels gives:

\[
\begin{array}{c|c|c|c}
(r,\sigma)&\operatorname{rank}&\Delta_2&\text{prototype preserving?}\\
\hline
(1,+1)&0&0&\text{no}\\
(1,-1)&2&4&\text{no}\\
(2,+1)&2&3&\text{no}\\
(2,-1)&2&1&\text{yes}\\
(3,+1)&2&3&\text{no}\\
(3,-1)&2&1&\text{yes}\\
(4,+1)&2&3&\text{no}\\
(4,-1)&2&1&\text{yes}\\
(5,+1)&2&3&\text{no}\\
(5,-1)&2&1&\text{yes}\\
(6,+1)&0&0&\text{no}\\
(6,-1)&2&4&\text{no}
\end{array}
\]

Thus the `\Delta_2=1` labels are exactly the four labels already identified in v13.240:

\[
\boxed{
\Delta_2(T_{r,\sigma}\Phi_*)=1
\iff
(r,\sigma)\in\mathcal A_7^{\rm pres}.
}
\]

Every nonpreserving label does one of three irreversible things:

1. `r=\pm1,\sigma=+1`: collapses the fiber to rank zero;
2. `r=\pm1,\sigma=-1`: raises `\Delta_2` from 1 to 4;
3. `r\in\{2,3,4,5\},\sigma=+1`: raises `\Delta_2` from 1 to 3.

## 7. q=7 no-return theorem

Suppose a support word begins at `\Phi_*` and contains at least one nonpreserving letter. Let the first nonpreserving letter occur at step `j`.

Before step `j`, the fiber is prototype-equivalent by v13.240, hence has

\[
\Delta_2=1.
\]

At step `j`, the preceding table shows that either rank drops below two, or `\Delta_2` becomes 3 or 4.

Later support operators are integer matrices. Therefore rank cannot recover after collapse, and a positive determinantal divisor can only become a multiple of its previous value.

Hence no later state can have `\Delta_2=1`.

But every prototype-equivalent fiber has `\Delta_2=1`. Therefore:

\[
\boxed{
\text{A q=7 support word returns to the prototype class}
\iff
\text{every letter lies in }\mathcal A_7^{\rm pres}.
}
\]

Equivalently,

\[
\boxed{
\text{there are no leave-and-return words at q=7.}
}
\]

This closes the return-word problem posed in v13.240.

## 8. Consequence: the C6 sector is isolated

v13.240 proved that words entirely inside `\mathcal A_7^{\rm pres}` act on signed projective phase by

\[
(u,\delta)\mapsto(r^{-1}u,-\delta)
\]

and generate

\[
\left(\mathbf F_7^\times/\{\pm1\}\right)\times C_2
\cong C_6.
\]

The no-return theorem now strengthens the interpretation:

\[
\boxed{
C_6
\text{ is not merely a closed preserving quotient; it is an isolated recurrent component of the q=7 prototype orbit.}
}
\]

Any nonpreserving support letter exits this component permanently.

The full support graph may still be infinite outside this component, but none of those exterior states can return to the prototype class.

## 9. Exact q=5 table

For the basic prototype

\[
\Phi_5=\Phi_{8,\varnothing,5},
\]

the eight labels give:

\[
\begin{array}{c|c|c}
(r,\sigma)&\operatorname{rank}&\Delta_2\\
\hline
(1,+1)&0&0\\
(1,-1)&2&4\\
(2,+1)&2&2\\
(2,-1)&2&2\\
(3,+1)&2&2\\
(3,-1)&2&2\\
(4,+1)&2&4\\
(4,-1)&0&0
\end{array}
\]

Thus every single support-prime label immediately either destroys rank two or makes `\Delta_2` a proper multiple of 1.

Therefore:

\[
\boxed{
\text{Starting from the basic q=5, D=8 prototype, no nonempty support word can ever return to the prototype class.}
}
\]

This strengthens v13.240 from a one-step statement to an all-word theorem.

It also explains why the other q=5 prototype-equivalent strata in v13.239 cannot be reached from the `D=8` prototype by support growth at fixed primitive character: they belong to different primitive-discriminant branches.

## 10. Structural meaning of the invariant

The decorated prototype has a primitive rank-two lattice in signal space:

\[
\Delta_2=1.
\]

A nonpreserving support transition introduces an irreversible integral index:

\[
1\longrightarrow2,3,4,\ldots
\]

or collapses the rank.

The support semigroup therefore has a natural arithmetic filtration by determinantal divisors. Prototype equivalence lives in the primitive layer, and the q=7 preserving alphabet is exactly the part of the support alphabet that remains in that primitive layer.

This is stronger than an amplitude-bound argument: it is an exact integral-lattice obstruction, independent of numerical size.

## 11. Relation to the integer operator on the reflection subspace

For q=7 and `D=-8`, every crossing signal obeys the centered antisymmetry

\[
f(-1-k)=-f(k).
\]

Writing such a signal as

\[
(a,b,c,0,-c,-b,-a),
\]

the support operators restrict to integer `3\times3` matrices. In these coordinates:

- the preserving labels `(2,-1),(5,-1)` share one determinant-2 matrix;
- the preserving labels `(3,-1),(4,-1)` share another determinant-2 matrix;
- `(1,-1),(6,-1)` act as `2I`;
- the `\sigma=+1` operators are singular.

The determinantal-divisor proof does not require choosing this coordinate model, but the model makes the arithmetic mechanism transparent: the prototype fiber spans a primitive rank-two sublattice, preserving letters move that lattice unimodularly inside its projective class, while nonpreserving letters introduce index or rank loss.

## 12. Guardrails

1. `\Delta_2` is an invariant of the decorated-fiber equivalence used in v13.239; it is not claimed to classify all exterior support states.
2. The no-return theorem concerns support-prime operator words at fixed crossing prime and fixed primitive character branch.
3. The q=7 theorem applies to the prototype class generated from `D=-8`; other primitive characters may have their own determinantal-divisor tables.
4. The q=5 theorem is for the basic `D=8` prototype; the existence of prototype-equivalent fibers for `D=13,17` does not contradict it because changing primitive discriminant is not a support-prime transition.
5. The finite `C_6` quotient remains a quotient of decorated fibers, not a finite model of the entire support graph.
6. No principal-paper theorem is revised by this checkpoint.

## 13. Checkpoint

The q=7 prototype support dynamics are now completely classified with respect to return:

\[
\boxed{
\text{prototype}
\xrightarrow{\text{preserving word}}
C_6\text{ phase orbit}
}
\]

and

\[
\boxed{
\text{prototype}
\xrightarrow{\text{any nonpreserving letter}}
\text{permanent exit from the prototype class}.
}
\]

For q=5,

\[
\boxed{
\text{every nonempty support word from the basic D=8 prototype is a permanent exit.}
}
\]

The next natural problem is to classify the exterior layers by `\Delta_2` and determine whether their determinantal-divisor growth is unbounded under repeated support adjunctions. That would decide whether the full operator orbit is necessarily infinite even after quotienting by cofactor rephasing and global sign.