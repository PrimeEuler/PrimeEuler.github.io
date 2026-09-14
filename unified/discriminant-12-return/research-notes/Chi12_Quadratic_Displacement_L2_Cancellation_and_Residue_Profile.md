# χ12 Quadratic Shell-Displacement: L(2) Cancellation and Residue Profile

**Status:** exact derived identities with explicit guardrails. This continues the shell-displacement hierarchy after the first-moment regulator cancellation.

Let

\[
\chi=\chi_{12},\qquad
q_k=\left\lfloor\frac nk\right\rfloor,\qquad
\delta_k=\left\{\frac nk\right\}=\frac nk-q_k.
\]

Define the quadratic twisted displacement moment

\[
Q_{12}(n):=\sum_{k\le n}\chi(k)\,\delta_k^2.
\]

Since \(\Delta X_k=-\delta_k/2\), this is equivalently

\[
Q_{12}(n)=4\sum_{k\le n}\chi(k)(\Delta X_k)^2.
\]

## 1. Exact quadratic expansion

Expanding \(\delta_k^2\) gives

\[
Q_{12}(n)
=
 n^2\sum_{k\le n}\frac{\chi(k)}{k^2}
-2n\sum_{k\le n}\frac{\chi(k)}k q_k
+\sum_{k\le n}\chi(k)q_k^2.
\]

Set

\[
A_{12}(n):=\sum_{k\le n}\frac{\chi(k)}k q_k,
\qquad
B_{12}(n):=\sum_{k\le n}\chi(k)q_k^2.
\]

Then

\[
\boxed{
Q_{12}(n)
=
 n^2 H^{(2)}_{12}(n)-2nA_{12}(n)+B_{12}(n),
}
\]

where

\[
H^{(2)}_{12}(n):=\sum_{k\le n}\frac{\chi(k)}{k^2}.
\]

## 2. Exact quotient-skeleton transforms

Because

\[
q_k=\#\{m\ge1:mk\le n\},
\]

we have

\[
\boxed{
A_{12}(n)
=
\sum_{m\le n}
H_{12}\!\left(\left\lfloor\frac nm\right\rfloor\right),
}
\]

with

\[
H_{12}(x):=\sum_{k\le x}\frac{\chi(k)}k.
\]

Also

\[
q_k^2=\sum_{j=1}^{q_k}(2j-1),
\]

so

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

Thus the quadratic shell-displacement channel is represented entirely by the reciprocal-character truncation and two quotient-skeleton transforms.

## 3. Exact value of L(2,χ12)

By residue classes,

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

Using the trigamma reflection identity

\[
\psi_1(z)+\psi_1(1-z)=\pi^2\csc^2(\pi z),
\]

we obtain

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

we get

\[
\boxed{
L(2,\chi_{12})=\frac{\pi^2}{6\sqrt3}.
}
\]

This is a new quadratic Dirichlet-series scale for the χ12 displacement hierarchy. It is distinct from the first-moment regulator

\[
L(1,\chi_{12})=\frac{\log(2+\sqrt3)}{\sqrt3}.
\]

## 4. Quadratic main-term cancellation

Define the order-two tail

\[
T^{(2)}_{12}(n):=\sum_{k>n}\frac{\chi(k)}{k^2}.
\]

Then

\[
H^{(2)}_{12}(n)
=
L(2,\chi_{12})-T^{(2)}_{12}(n),
\]

so

\[
Q_{12}(n)
=
\frac{\pi^2}{6\sqrt3}n^2
-2nA_{12}(n)+B_{12}(n)
-n^2T^{(2)}_{12}(n).
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

Then exactly

\[
\boxed{
Q_{12}(n)
=
-\mathcal R^{(2)}_{12}(n)
-n^2T^{(2)}_{12}(n).
}
\]

Thus the raw \(n^2L(2,\chi_{12})\) term is not the quadratic displacement signal. It cancels against the quotient-skeleton terms, just as the linear regulator main term cancels in the first χ12 moment.

Because \(|\delta_k|<1\) and \(\chi\) vanishes off the unit classes,

\[
|Q_{12}(n)|\le \#\{k\le n:(k,6)=1\}=\frac n3+O(1).
\]

Hence the three formally quadratic pieces above cancel to at most linear size.

## 5. Tail bound

The partial sums \(S_{12}(x)\) satisfy \(|S_{12}(x)|\le1\). Summation by parts therefore gives

\[
\boxed{
|T^{(2)}_{12}(n)|\le \frac{2}{(n+1)^2}.
}
\]

Consequently

\[
\boxed{
|n^2T^{(2)}_{12}(n)|<2.
}
\]

So the quadratic displacement moment differs from the negative quadratic skeleton remainder by a uniformly bounded amount:

\[
\boxed{
|Q_{12}(n)+\mathcal R^{(2)}_{12}(n)|<2.
}
\]

## 6. Residue-class limit of the quadratic tail

Write

\[
n=12m+r,\qquad 0\le r\le11,
\]

and define the same partial character profile as in the first-moment tail analysis:

\[
S(r):=\sum_{a=1}^{r}\chi_{12}(a).
\]

The values are

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

Because each complete future period has zero χ12-sum, the incomplete boundary block supplies the leading tail term. For fixed \(r\),

\[
\boxed{
 n^2T^{(2)}_{12}(n)
=-S(r)+O(n^{-1}).
}
\]

Therefore

\[
\boxed{
Q_{12}(n)
=
-\mathcal R^{(2)}_{12}(n)
+S(r)
+O(n^{-1}),
\qquad n\equiv r\pmod{12}.
}
\]

The same five-level residue profile that appeared in the first χ12 displacement moment therefore survives in the quadratic channel.

## 7. Relation to Pell time orientation

The concurrent Pell-thread result proves

\[
\sigma_r(\lambda)=\lambda^{\chi_{12}(r)},
\qquad \lambda=2+\sqrt3.
\]

Thus the same χ12 signs have an exact operator interpretation on the Pell unit:

- \(\chi_{12}=+1\): preserve Pell-time orientation;
- \(\chi_{12}=-1\): reverse Pell-time orientation.

The quadratic displacement channel weights **energies** \((\Delta X_k)^2\) by this same sign character. Hence

\[
Q_{12}(n)=4\sum_k\chi_{12}(k)(\Delta X_k)^2
\]

measures the imbalance of shell-displacement energy between the two Pell-time-orientation sign sectors.

This is an exact common character, not an identification of the two carriers.

## 8. Guardrails

1. \(L(2,\chi_{12})=\pi^2/(6\sqrt3)\) is distinct from the regulator quantity \(L(1,\chi_{12})=R_{12}/\sqrt3\).
2. The quadratic Dirichlet-series constant cancels from the observable main term after quotient-skeleton subtraction; do not identify \(Q_{12}\) with \(n^2L(2,\chi_{12})\).
3. Pell time orientation and shell-displacement energy are distinct carriers linked by the same χ12 character.
4. No Pell action on the integer divisor lattice is inferred.
5. The common residue profile \(S(r)\) arises from truncation of a mean-zero periodic character and should not be confused with the scalar Pell half-return \(7I\).

## 9. Structural comparison with the first moment

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

For both orders,

\[
 n^jT^{(j)}_{12}(n)
=-S(n\bmod12)+O(n^{-1}),
\]

for \(j=1,2\). Thus the same periodic orientation profile rides on top of two different field constants after the corresponding main-term cancellations.

**Checkpoint conclusion:** The quadratic χ12 shell-displacement channel introduces the exact constant \(L(2,\chi_{12})=\pi^2/(6\sqrt3)\), but that quadratic main term cancels against the quotient-skeleton transforms. The surviving observable is the negative quadratic skeleton remainder plus the same five-level mod-12 boundary profile already seen at first order. This extends the regulator/displacement picture into a genuine moment hierarchy while keeping the distinct arithmetic constants and carriers separate.
