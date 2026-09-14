# χ12 Tail Residue Profile and Pell Time-Orientation Channel

Date: 2026-09-14

Status labels: **[D]** exact derived, **[I]** interpretation, **[Audit]** limitation/guardrail.

## 1. Starting point

From the exact shell-displacement identity,

\[
E_{12}(n)
=-\mathcal R_{12}(n)-nT_{12}(n),
\]

where

\[
T_{12}(n):=\sum_{k>n}\frac{\chi_{12}(k)}{k},
\]

and

\[
\mathcal R_{12}(n)
:=\mathcal I_{12}(n)-L(1,\chi_{12})n,
\qquad
L(1,\chi_{12})=\frac{R_{12}}{\sqrt3},
\qquad
R_{12}=\log(2+\sqrt3).
\]

The previous checkpoint only needed the uniform bound \(|nT_{12}(n)|<2\). Here the tail is resolved exactly by the residue class of \(n\bmod 12\).

## 2. Exact digamma formula for the tail [D]

The primitive quadratic character modulo 12 is

\[
\chi_{12}(a)=
\begin{cases}
+1,&a\equiv1,11\pmod{12},\\
-1,&a\equiv5,7\pmod{12},\\
0,&(a,12)>1.
\end{cases}
\]

Write

\[
n=12m+r,
\qquad 0\le r\le 11.
\]

For \(a\in\{1,5,7,11\}\), define

\[
J_a(m,r):=m+\mathbf 1_{\{a\le r\}}.
\]

Then the first omitted term in residue class \(a\pmod{12}\) is \(12J_a+a\), so

\[
T_{12}(12m+r)
=\sum_{a\in\{1,5,7,11\}}\chi_{12}(a)
\sum_{j\ge J_a(m,r)}\frac1{12j+a}.
\]

Using the cancellation \(1-1-1+1=0\) and the standard digamma identity for convergent differences of harmonic tails,

\[
\boxed{
T_{12}(12m+r)
=\frac1{12}
\Bigl[
-\psi\!\left(J_1+\frac1{12}\right)
+\psi\!\left(J_5+\frac5{12}\right)
+\psi\!\left(J_7+\frac7{12}\right)
-\psi\!\left(J_{11}+\frac{11}{12}\right)
\Bigr].
}
\]

This is an exact closed form for the previously infinite tail.

## 3. Only five distinct residue profiles [D]

Because \(J_a\) changes only when \(r\) crosses one of \(1,5,7,11\), the twelve residue classes collapse into five tail types:

\[
r=0,
\]

\[
r\in\{1,2,3,4\},
\]

\[
r\in\{5,6\},
\]

\[
r\in\{7,8,9,10\},
\]

\[
r=11.
\]

Equivalently, define the within-period partial character sum

\[
S(r):=\sum_{a=1}^{r}\chi_{12}(a).
\]

Then

\[
\boxed{
S(r)=
\begin{cases}
0,&r=0,\\
+1,&r=1,2,3,4,\\
0,&r=5,6,\\
-1,&r=7,8,9,10,\\
0,&r=11.
\end{cases}}
\]

## 4. Residue-class limit of the tail correction [D]

For fixed \(r\), use

\[
\psi(m+\beta)=\log m+\frac{\beta-\tfrac12}{m}+O(m^{-2}).
\]

The logarithmic terms cancel because the character has zero mean over a period. Also

\[
\sum_{a\in\{1,5,7,11\}}\chi_{12}(a)\frac a{12}=0.
\]

The only surviving coefficient at order \(1/m\) comes from the indicators \(\mathbf1_{a\le r}\), giving

\[
T_{12}(12m+r)
=-\frac{S(r)}{12m}+O(m^{-2}).
\]

Since \(n=12m+r\),

\[
\boxed{
nT_{12}(n)=-S(r)+O(n^{-1})
\qquad(n\equiv r\pmod{12}).
}
\]

Hence

\[
\boxed{
\lim_{\substack{n\to\infty\\ n\equiv r\,(12)}}nT_{12}(n)
=-S(r).
}
\]

The limits are therefore

\[
\boxed{
\begin{array}{c|c}
r & \lim nT_{12}(n)\\
\hline
0 & 0\\
1,2,3,4 & -1\\
5,6 & 0\\
7,8,9,10 & +1\\
11 & 0
\end{array}}
\]

## 5. Exact consequence for the shell-displacement/ideal-counting comparison [D]

Since

\[
E_{12}(n)+\mathcal R_{12}(n)=-nT_{12}(n),
\]

we obtain

\[
\boxed{
E_{12}(n)+\mathcal R_{12}(n)
=S(r)+O(n^{-1})
\qquad(n\equiv r\pmod{12}).
}
\]

Therefore

\[
\boxed{
\lim_{\substack{n\to\infty\\ n\equiv r\,(12)}}
\bigl(E_{12}(n)+\mathcal R_{12}(n)\bigr)
=S(r).
}
\]

Explicitly,

\[
\boxed{
\begin{array}{c|c}
r & \lim(E_{12}+\mathcal R_{12})\\
\hline
0 & 0\\
1,2,3,4 & +1\\
5,6 & 0\\
7,8,9,10 & -1\\
11 & 0
\end{array}}
\]

So the bounded correction from the previous checkpoint is not unstructured: it converges, on every residue class modulo 12, to the within-period partial sum of \(\chi_{12}\).

## 6. Connection to the v13.414 Pell time-orientation result [D/I]

The concurrent ledger checkpoint v13.414 proves the exact operator identity

\[
\sigma_r(\lambda)=\lambda^{\chi_{12}(r)},
\qquad
\lambda=2+\sqrt3.
\]

Thus the signs of \(\chi_{12}\) distinguish Pell-time orientation:

\[
\chi_{12}=+1
\quad\Longleftrightarrow\quad
\lambda\mapsto\lambda,
\]

\[
\chi_{12}=-1
\quad\Longleftrightarrow\quad
\lambda\mapsto\lambda^{-1}.
\]

The same sign sequence weights the shell-displacement statistic

\[
E_{12}(n)
=-2\sum_{k\le n}\chi_{12}(k)\Delta X_k.
\]

The residue-profile correction

\[
S(r)=\sum_{a\le r}\chi_{12}(a)
\]

therefore has an exact combinatorial reading as the cumulative imbalance, inside the final incomplete mod-12 block, between time-orientation-preserving and time-orientation-reversing character values.

**[I]** This gives a useful interpretation of the bounded correction: it is the boundary imbalance left by truncating a zero-mean orientation character partway through its period.

**[Audit]** This does not mean the Pell operator acts on the divisor lattice or that the shell-displacement sum is a Pell orbit. The exact common structure is the character \(\chi_{12}\), not a shared carrier.

## 7. Structural summary

The regulator cancellation and the residue-profile correction now separate cleanly:

\[
\boxed{
E_{12}(n)
=-\mathcal R_{12}(n)-nT_{12}(n),
}
\]

with

\[
\boxed{
nT_{12}(n)=-S(n\bmod12)+O(n^{-1}).}
\]

Hence

\[
\boxed{
E_{12}(n)
=-\mathcal R_{12}(n)
+S(n\bmod12)
+O(n^{-1}).
}
\]

The regulator \(R_{12}\) controls the common linear main term that cancels; the remaining large-scale fluctuation is the negative ideal-counting remainder; and the finite truncation mismatch has an explicit periodic boundary profile determined by the same \(\chi_{12}\) that v13.414 identifies as Pell time orientation.

## Guardrails

- The digamma formula is an exact tail identity; the residue-profile formula with \(O(n^{-1})\) is asymptotic along fixed residue classes.
- The values \(\pm1,0\) here are partial character sums, not new V4 group elements or Pell matrices.
- No RH/GRH or divisor-error bound is asserted.
- No direct Pell action on integer factor pairs is inferred.
