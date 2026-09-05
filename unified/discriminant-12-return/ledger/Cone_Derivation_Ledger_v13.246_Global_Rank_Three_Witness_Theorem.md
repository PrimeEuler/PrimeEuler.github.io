# Cone Derivation Ledger v13.246 — Global Rank-Three Legendre Witness Theorem

Date: 2026-09-05
Status: EXACT NEW RESULT — continuation of v13.245; research branch remains open

## 0. Pre-write synchronization

Immediately before this write, the authoritative project README, current `master` tip, and v13.245 were re-fetched. The tip remained

`5420de4271e879366658dfcc35f1320a36bc10bb`

with v13.245 as the highest ledger checkpoint. No newer external-audit checkpoint had landed. This entry extends the reconciled research branch and does not revise the audited principal v0.3.5 paper.

## 1. Question

v13.245 reduced the low-dimensional closure problem to the three universal vectors

\[
\ell_q,
\qquad
T_{2,-1}\ell_q,
\qquad
T_{3,-1}\ell_q,
\]

and verified by exact finite audit that they have rank three for every prime `11<=q<100`.

The present entry proves the all-prime theorem exactly.

## 2. Recentered coordinate

Let

\[
a=(q-1)/2,
\qquad
n=k-a,
\]

so that

\[
\ell_q(k)=\chi(n),
\]

where `\chi` is the quadratic character modulo `q` extended by `\chi(0)=0`.

For the two support operators with `sigma=-1`, direct substitution gives

\[
T_{2,-1}\ell_q
=\chi(n)+\chi(2)X(n),
\]

with

\[
\boxed{
X(n)=\chi(4n-1)+\chi(4n+1),
}
\]

and

\[
T_{3,-1}\ell_q
=(1+\chi(3))\chi(n)+Y(n),
\]

with

\[
\boxed{
Y(n)=\chi(3n-1)+\chi(3n+1).
}
\]

Since `\chi(2)=+-1`, the linear change of generators between

\[
\{\ell_q,T_{2,-1}\ell_q,T_{3,-1}\ell_q\}
\]

and

\[
\boxed{\{\chi,X,Y\}}
\]

is invertible over `Q`. Therefore the two triples have the same rank.

## 3. Quadratic-character correlation identity

For nonproportional affine linear forms

\[
L_1(n)=an+b,
\qquad
L_2(n)=cn+d,
\]

with `ac != 0`, the product is a quadratic polynomial with nonzero discriminant, and the standard quadratic-character sum gives

\[
\boxed{
\sum_{n\in\mathbf F_q}\chi(L_1(n)L_2(n))=-\chi(ac).
}
\]

If the forms are proportional, the sum is instead `\chi(ac)(q-1)`.

The only exceptional proportionality relevant below occurs at `q=7`: a root of one of `4n+-1` coincides with a root of one of `3n+-1` exactly when

\[
1/4=-1/3,
\]

which is equivalent to `q=7`.

Thus for every prime `q!=2,3,7`, all mixed `X-Y` pairs are nonproportional.

## 4. Exact Gram matrix for q != 7

Use the inner product

\[
\langle f,g\rangle=\sum_{n\in\mathbf F_q}f(n)g(n).
\]

We have

\[
\langle\chi,\chi\rangle=q-1.
\]

For `X`, each square contributes `q-1`, while the cross term

\[
\sum_n\chi((4n-1)(4n+1))=-1.
\]

Hence

\[
\boxed{\langle X,X\rangle=2(q-2).}
\]

Similarly,

\[
\boxed{\langle Y,Y\rangle=2(q-2).}
\]

The mixed products with `\chi` are

\[
\boxed{\langle\chi,X\rangle=-2,}
\]

and

\[
\boxed{\langle\chi,Y\rangle=-2\chi(3).}
\]

For `q!=7`, all four pairs between `4n+-1` and `3n+-1` are nonproportional. Their leading-coefficient product is `12`, so each contributes

\[
-\chi(12)=-\chi(3).
\]

Therefore

\[
\boxed{\langle X,Y\rangle=-4\chi(3).}
\]

Thus, writing `epsilon=chi(3)`, the Gram matrix is

\[
\boxed{
G_q=
\begin{pmatrix}
q-1 & -2 & -2\epsilon\\
-2 & 2(q-2) & -4\epsilon\\
-2\epsilon & -4\epsilon & 2(q-2)
\end{pmatrix}.
}
\]

## 5. Determinant collapse

Since `\epsilon^2=1`, direct expansion gives the unexpectedly simple identity

\[
\boxed{\det G_q=4q^2(q-5).}
\]

Therefore, for every prime

\[
q>5,
\qquad
q\ne7,
\]

we have

\[
\det G_q>0.
\]

Hence `\chi,X,Y` are linearly independent over `Q`, and therefore so are

\[
\ell_q,
\qquad
T_{2,-1}\ell_q,
\qquad
T_{3,-1}\ell_q.
\]

This proves the global witness theorem:

\[
\boxed{
q\ge11\text{ prime}
\Longrightarrow
\operatorname{rank}_{\mathbf Q}
[\ell_q,T_{2,-1}\ell_q,T_{3,-1}\ell_q]=3.
}
\]

No finite search and no quadratic-reciprocity case split is needed.

## 6. Exceptional primes 5 and 7

At `q=5`, the same Gram determinant formula gives zero:

\[
4q^2(q-5)=0.
\]

This is exactly the Gaussian rank-two case of v13.244.

At `q=7`, the generic `X-Y` correlation formula is invalid because one affine-root pairing becomes proportional. Direct evaluation gives rank two, exactly the Eisenstein case of v13.243.

Thus, among odd primes `q>=5`,

\[
\boxed{
\operatorname{rank}
[\ell_q,T_{2,-1}\ell_q,T_{3,-1}\ell_q]
=2
\iff
q\in\{5,7\}.
}
\]

## 7. Global classification of rank-two universal Legendre closure

Recall from v13.245

\[
V_q=\operatorname{span}_{\mathbf Q}
\{T_{r,\sigma}\ell_q:r\in\mathbf F_q^\times,\ \sigma=+-1\}.
\]

The three witness vectors lie in `V_q` (and `\ell_q` itself is obtained from the local alphabet by a trivial linear combination), so the preceding theorem implies

\[
q\ge11
\Longrightarrow
\boxed{\dim_{\mathbf Q}V_q\ge3.}
\]

Combined with the exact calculations

\[
\dim V_5=2,
\qquad
\dim V_7=2,
\]

we obtain the global classification:

\[
\boxed{
\dim_{\mathbf Q}V_q\le2
\iff
q\in\{5,7\}
}
\]

for every odd prime `q>=5`.

Equivalently:

\[
\boxed{
\text{The Gaussian and Eisenstein cases are the only rank-two universal centered-Legendre support closures.}
}
\]

## 8. Structural meaning of the determinant

The factorization

\[
\det G_q=4q^2(q-5)
\]

is stronger than the expected residue-class argument. The dependence on `\chi(3)` cancels completely.

Thus the obstruction is not controlled by a delicate congruence class of `q`; it is a global positive-definiteness phenomenon. Once `q` exceeds 5, the only possible failure of the generic Gram calculation is the geometric affine-root collision at `q=7`.

This gives a compact conceptual classification:

\[
\boxed{
q=5:\text{ Gram degeneracy},
\qquad
q=7:\text{ affine-root collision},
\qquad
q\ge11:\text{ strict rank-three positivity}.
}
\]

The two exceptional crossing primes are exceptional for two different exact reasons.

## 9. What this proves and what it does not

This proves globally that the q=5/q=7 Gaussian-Eisenstein mechanism cannot occur at any prime `q>=11`.

It does **not** yet prove that an isolated exact Legendre resonance is impossible for `q>=11`. A hypothetical isolated resonance need not make the complete universal support alphabet close on a rank-two plane.

Therefore the correct implication is

\[
\boxed{
q\ge11
\Longrightarrow
\text{no rank-two universal support closure},
}
\]

not yet

\[
q\ge11
\Longrightarrow
\text{no exact resonance}.
\]

The latter remains the deeper global target.

## 10. Next theorem target

The natural next question is now much sharper. Any hypothetical `q>=11` resonance must live in a support fiber of rational dimension at least three under the local operators.

The next attack should combine the exact Legendre autocorrelation

\[
A(0)=q-1,
\qquad
A(h)=-1\ (h\ne0),
\]

with the carrier pushforward/collision-energy identities of v13.234 and the higher-dimensional universal-span obstruction proved here.

The aim is to determine whether the exact two-level Legendre autocorrelation itself forces a low-dimensional support closure. If so, the present theorem would upgrade immediately to

\[
\boxed{
q\ge11\Longrightarrow\text{no exact Legendre resonance}.
}
\]

That implication is not asserted yet.

## 11. Guardrails

1. The Gram computation is exact for every prime `q!=2,3,7`.
2. The all-prime rank-three theorem is exact for every prime `q>=11`.
3. `q=5` and `q=7` are checked separately and both have rank two.
4. The universal rank-two closure classification is now global, not computational-window evidence.
5. No global `q>=11` no-resonance theorem is claimed yet.
6. The principal Discriminant-12 v0.3.5 theorem package is unchanged.

## 12. Checkpoint

The research chain has advanced from finite evidence to a closed theorem:

\[
\boxed{
\text{centered Legendre target}
\to
\{\chi,X,Y\}
\to
\text{quadratic-character Gram matrix}
\to
\det G_q=4q^2(q-5)
\to
\text{global rank-two classification}.
}
\]

Thus

\[
\boxed{
q=5\text{ and }q=7
\text{ are the only odd primes supporting the universal rank-two mechanism.}
}
\]

This replaces the `q<100` evidence of v13.245 with an exact all-prime theorem.