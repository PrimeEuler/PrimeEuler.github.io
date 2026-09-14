# Cone Derivation Ledger v13.420 — χ12 Quadratic Displacement, L(2) Cancellation, and Residue Profile

Date: 2026-09-14

Status labels: **[D]** exact derived, **[I]** interpretation, **[Audit]** limitation/guardrail.

## 0. Synchronization note

This checkpoint was written after checking the current repository head. Concurrent audit/Suzuki work has produced several version-collision repairs through v13.419, so this entry deliberately uses v13.420. The shell-displacement first-moment identities from v13.413 and the χ12 Pell-time-orientation result from v13.414 remain in force.

## 1. Quadratic twisted shell-displacement moment [D]

Let

\[
\chi=\chi_{12},\qquad
q_k=\left\lfloor\frac nk\right\rfloor,
\qquad
\delta_k=\left\{\frac nk\right\}.
\]

Define

\[
\boxed{
Q_{12}(n):=\sum_{k\le n}\chi(k)\delta_k^2.
}
\]

Since the exact shell displacement satisfies

\[
\Delta X_k=-\frac12\delta_k,
\]

we also have

\[
\boxed{
Q_{12}(n)=4\sum_{k\le n}\chi(k)(\Delta X_k)^2.
}
\]

Thus Q12 is the χ12-weighted quadratic shell-displacement energy.

## 2. Exact expansion and quotient-skeleton transforms [D]

From

\[
\delta_k=\frac nk-q_k,
\]

we obtain

\[
Q_{12}(n)
=
 n^2\sum_{k\le n}\frac{\chi(k)}{k^2}
-2n\sum_{k\le n}\frac{\chi(k)}k q_k
+\sum_{k\le n}\chi(k)q_k^2.
\]

Define

\[
A_{12}(n):=\sum_{k\le n}\frac{\chi(k)}k q_k,
\qquad
B_{12}(n):=\sum_{k\le n}\chi(k)q_k^2.
\]

Then

\[
\boxed{
Q_{12}(n)=n^2H^{(2)}_{12}(n)-2nA_{12}(n)+B_{12}(n),
}
\]

where

\[
H^{(2)}_{12}(n):=\sum_{k\le n}\frac{\chi(k)}{k^2}.
\]

Two exact quotient-skeleton rewritings are

\[
\boxed{
A_{12}(n)=\sum_{m\le n}H_{12}\!\left(\left\lfloor\frac nm\right\rfloor\right),
}
\]

where

\[
H_{12}(x):=\sum_{k\le x}\frac{\chi(k)}k,
\]

and, because \(q^2=\sum_{j=1}^{q}(2j-1)\),

\[
\boxed{
B_{12}(n)
=
\sum_{j\le n}(2j-1)
S_{12}\!\left(\left\lfloor\frac nj\right\rfloor\right),
}
\]

where

\[
S_{12}(x):=\sum_{k\le x}\chi(k).
\]

## 3. Exact quadratic Dirichlet constant [D]

The χ12 Dirichlet series at s=2 is

\[
L(2,\chi_{12})
=
\sum_{m\ge0}
\left[
\frac1{(12m+1)^2}
-\frac1{(12m+5)^2}
-\frac1{(12m+7)^2}
+\frac1{(12m+11)^2}
\right].
\]

Using trigamma reflection,

\[
\psi_1(z)+\psi_1(1-z)=\pi^2\csc^2(\pi z),
\]

one gets

\[
L(2,\chi_{12})
=
\frac{\pi^2}{144}
\left[
\csc^2\frac\pi{12}
-
\csc^2\frac{5\pi}{12}
\right].
\]

Since

\[
\csc^2\frac\pi{12}=8+4\sqrt3,
\qquad
\csc^2\frac{5\pi}{12}=8-4\sqrt3,
\]

we obtain

\[
\boxed{
L(2,\chi_{12})=\frac{\pi^2}{6\sqrt3}.
}
\]

This is distinct from the first-moment regulator scale

\[
L(1,\chi_{12})=\frac{\log(2+\sqrt3)}{\sqrt3}.
\]

## 4. Exact quadratic cancellation [D]

Let

\[
T^{(2)}_{12}(n):=\sum_{k>n}\frac{\chi(k)}{k^2}.
\]

Then

\[
H^{(2)}_{12}(n)
=
L(2,\chi_{12})-T^{(2)}_{12}(n).
\]

Define the quadratic quotient-skeleton remainder

\[
\boxed{
\mathcal R^{(2)}_{12}(n)
:=
2nA_{12}(n)-B_{12}(n)
-\frac{\pi^2}{6\sqrt3}n^2.
}
\]

Substitution gives the exact identity

\[
\boxed{
Q_{12}(n)
=
-\mathcal R^{(2)}_{12}(n)
-n^2T^{(2)}_{12}(n).
}
\]

Therefore the quadratic Dirichlet main term is not itself the shell-displacement observable. It cancels against the quotient-skeleton terms.

Because \(|\delta_k|<1\) and χ12 is supported only on residue classes coprime to 6,

\[
|Q_{12}(n)|\le \#\{k\le n:(k,6)=1\}=\frac n3+O(1).
\]

Hence the formally quadratic pieces cancel down to at most linear size.

## 5. Uniform tail control [D]

The χ12 partial sums satisfy

\[
|S_{12}(x)|\le1.
\]

Summation by parts yields

\[
\boxed{
|T^{(2)}_{12}(n)|\le\frac{2}{(n+1)^2}.
}
\]

Therefore

\[
\boxed{
|n^2T^{(2)}_{12}(n)|<2,
}
\]

and

\[
\boxed{
|Q_{12}(n)+\mathcal R^{(2)}_{12}(n)|<2.
}
\]

This exactly parallels the bounded first-moment correction in v13.413.

## 6. Residue-class profile [D]

Write

\[
n=12m+r,\qquad 0\le r\le11,
\]

and define

\[
S(r):=\sum_{a=1}^{r}\chi_{12}(a).
\]

Then

\[
S(r)=
\begin{cases}
0,&r=0,\\
+1,&r=1,2,3,4,\\
0,&r=5,6,\\
-1,&r=7,8,9,10,\\
0,&r=11.
\end{cases}
\]

For fixed residue class r, complete future χ12 periods cancel, while the incomplete boundary block gives the leading tail term. Hence

\[
\boxed{
 n^2T^{(2)}_{12}(n)
=-S(r)+O(n^{-1}).
}
\]

Consequently

\[
\boxed{
Q_{12}(n)
=
-\mathcal R^{(2)}_{12}(n)
+S(r)+O(n^{-1}),
\qquad n\equiv r\pmod{12}.
}
\]

The same five-level periodic boundary profile found in the first moment reappears at second order.

## 7. First- versus second-moment hierarchy [D/I]

First moment:

\[
E_{12}(n)
=-\mathcal R^{(1)}_{12}(n)-nT^{(1)}_{12}(n),
\qquad
L(1,\chi_{12})=\frac{R_{12}}{\sqrt3}.
\]

Second moment:

\[
Q_{12}(n)
=-\mathcal R^{(2)}_{12}(n)-n^2T^{(2)}_{12}(n),
\qquad
L(2,\chi_{12})=\frac{\pi^2}{6\sqrt3}.
\]

For both j=1 and j=2,

\[
\boxed{
 n^jT^{(j)}_{12}(n)
=-S(n\bmod12)+O(n^{-1}).
}
\]

Thus two distinct field constants govern the corresponding reciprocal-character truncations, but the same mod-12 orientation profile survives after main-term cancellation.

## 8. Pell-time-orientation bridge [D/I]

The concurrent Pell result gives

\[
\boxed{
\sigma_r(\lambda)=\lambda^{\chi_{12}(r)},
\qquad \lambda=2+\sqrt3.
}
\]

So χ12 is the exact sign character for Pell-time orientation. Therefore

\[
Q_{12}(n)=4\sum_k\chi_{12}(k)(\Delta X_k)^2
\]

can be interpreted as the signed imbalance of shell-displacement energy between the two χ12 orientation sectors.

**[Audit]** This is a shared character on distinct carriers. It does not imply that the Pell matrix acts on the divisor staircase or that shell-displacement energy is a Pell invariant.

## 9. Guardrails [Audit]

- Do not identify \(L(2,\chi_{12})\) with the regulator. The regulator occurs at s=1; the quadratic constant is \(\pi^2/(6\sqrt3)\).
- Do not identify Q12 with \(n^2L(2,\chi_{12})\); that main term cancels.
- The common residue profile S(r) is a periodic truncation effect of the mean-zero χ12 character, not the scalar Pell half-return 7I.
- The first- and second-moment remainders are distinct arithmetic objects.
- No Suzuki/RH consequence is claimed. Concurrent audit work has independently found that the χ12/cone structure does not sharpen the current odd-sector positivity certificate.

## 10. Next target

The exact pattern suggests testing the general integer moment

\[
M_j(n):=\sum_{k\le n}\chi_{12}(k)\delta_k^j
\]

for j>=1. The likely structural question is whether every integer j admits

\[
M_j(n)
=-\mathcal R^{(j)}_{12}(n)-n^jT^{(j)}_{12}(n)
\]

with

\[
L(j,\chi_{12})
\]

as the reciprocal-character scale and the same boundary law

\[
n^jT^{(j)}_{12}(n)=-S(n\bmod12)+O(n^{-1}).
\]

This should be derived rather than assumed.

---

**Checkpoint conclusion.** The χ12 quadratic shell-displacement channel introduces the exact new constant \(L(2,\chi_{12})=\pi^2/(6\sqrt3)\). Its formally quadratic main term cancels against exact quotient-skeleton transforms, leaving the negative quadratic remainder plus a uniformly bounded tail. Along each mod-12 residue class that tail converges to the same five-level χ12 boundary profile as in the first moment. This establishes a genuine first/second-moment hierarchy while keeping regulator, quadratic Dirichlet scale, Pell orientation, and shell-displacement carriers distinct.
