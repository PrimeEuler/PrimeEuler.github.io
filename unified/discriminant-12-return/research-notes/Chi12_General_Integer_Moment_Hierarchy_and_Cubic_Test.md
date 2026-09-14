# χ12 General Integer-Moment Hierarchy and Cubic Test

Status: exact derivation checkpoint. This note extends the first- and second-moment shell-displacement identities to every positive integer moment. The common residue-boundary profile is proved for all fixed integer moments. Interpretive remarks remain separate from the exact algebra.

Let

\[
\delta_k(n)=\left\{\frac nk\right\},\qquad q_k=\left\lfloor\frac nk\right\rfloor,
\]

and for integer \(j\ge1\) define the χ12-weighted moment

\[
M_j(n)=\sum_{k\le n}\chi_{12}(k)\,\delta_k(n)^j.
\]

Since

\[
\delta_k(n)=\frac nk-q_k,
\]

binomial expansion gives the exact identity

\[
M_j(n)
=
\sum_{\ell=0}^{j}
(-1)^\ell\binom{j}{\ell}
 n^{j-\ell}
\sum_{k\le n}
\frac{\chi_{12}(k)q_k^\ell}{k^{j-\ell}}.
\]

Define

\[
C_{j,\ell}(n)
:=
\sum_{k\le n}
\frac{\chi_{12}(k)q_k^\ell}{k^{j-\ell}},
\qquad 0\le \ell\le j.
\]

Then \(C_{j,0}=H_j^{(\chi)}(n):=\sum_{k\le n}\chi_{12}(k)/k^j\), and

\[
\boxed{
M_j(n)
=
\sum_{\ell=0}^{j}
(-1)^\ell\binom{j}{\ell}
 n^{j-\ell}C_{j,\ell}(n).
}
\]

Let

\[
L_j:=L(j,\chi_{12}),
\qquad
T_j(n):=\sum_{k>n}\frac{\chi_{12}(k)}{k^j}.
\]

Thus

\[
C_{j,0}(n)=L_j-T_j(n).
\]

Define the j-th quotient-skeleton remainder

\[
\boxed{
\mathcal R_j(n)
:=
\sum_{\ell=1}^{j}
(-1)^{\ell+1}\binom{j}{\ell}
 n^{j-\ell}C_{j,\ell}(n)
-
L_j n^j.
}
\]

Substituting \(C_{j,0}=L_j-T_j\) gives the general exact moment identity

\[
\boxed{
M_j(n)
=
-\mathcal R_j(n)-n^jT_j(n).
}
\]

This simultaneously recovers:

- j=1: the χ12 first shell-displacement moment and ideal-counting remainder;
- j=2: the quadratic displacement-energy identity;
- all higher integer moments with the same tail architecture.

## Quotient-block transform for every skeleton term

For \(\ell\ge1\), use

\[
q_k^\ell
=
\sum_{m=1}^{q_k}\left(m^\ell-(m-1)^\ell\right).
\]

Interchanging sums gives

\[
\boxed{
C_{j,\ell}(n)
=
\sum_{m\le n}
\left(m^\ell-(m-1)^\ell\right)
H_{j-\ell}^{(\chi)}\!\left(\left\lfloor\frac nm\right\rfloor\right),
}
\]

where

\[
H_s^{(\chi)}(N):=\sum_{k\le N}\frac{\chi_{12}(k)}{k^s},
\]

with \(H_0^{(\chi)}(N)=\sum_{k\le N}\chi_{12}(k)\).

So every integer shell-displacement moment is controlled by a finite hierarchy of χ12 partial reciprocal sums sampled on the quotient skeleton.

## Universal residue-boundary profile

Write

\[
n=12m+r,\qquad 0\le r\le11,
\]

and

\[
S(r):=\sum_{a=1}^{r}\chi_{12}(a).
\]

For χ12,

\[
S(r)=
\begin{cases}
0,&r=0,\\
1,&r=1,2,3,4,\\
0,&r=5,6,\\
-1,&r=7,8,9,10,\\
0,&r=11.
\end{cases}
\]

Because χ12 is periodic of mean zero and its period-12 partial-sum profile also has zero average over a full period, summation by parts gives, for every fixed integer \(j\ge1\),

\[
\boxed{
n^jT_j(n)=-S(r)+O(n^{-1})
\qquad(n\equiv r\pmod{12}).
}
\]

Therefore the full hierarchy satisfies

\[
\boxed{
M_j(n)
=
-\mathcal R_j(n)
+S(n\bmod12)
+O(n^{-1}).
}
\]

Thus the same five-level boundary profile survives at every positive integer moment. What changes with j is the analytic main scale \(L(j,\chi_{12})\) and the internal quotient-skeleton remainder \(\mathcal R_j\), not the terminal residue profile.

## Cubic test j=3

For

\[
M_3(n)=\sum_{k\le n}\chi_{12}(k)\delta_k(n)^3,
\]

define

\[
A_3(n):=C_{3,1}(n)
=
\sum_{k\le n}\frac{\chi_{12}(k)q_k}{k^2},
\]

\[
B_3(n):=C_{3,2}(n)
=
\sum_{k\le n}\frac{\chi_{12}(k)q_k^2}{k},
\]

\[
C_3(n):=C_{3,3}(n)
=
\sum_{k\le n}\chi_{12}(k)q_k^3.
\]

Then

\[
\boxed{
M_3(n)
=
n^3H_3^{(\chi)}(n)
-3n^2A_3(n)
+3nB_3(n)
-C_3(n).
}
\]

Let

\[
L_3=L(3,\chi_{12}).
\]

The cubic skeleton remainder is

\[
\boxed{
\mathcal R_3(n)
=
3n^2A_3(n)-3nB_3(n)+C_3(n)-L_3n^3.
}
\]

Hence

\[
\boxed{
M_3(n)
=
-\mathcal R_3(n)-n^3T_3(n).
}
\]

and, along \(n\equiv r\pmod{12}\),

\[
\boxed{
M_3(n)
=
-\mathcal R_3(n)+S(r)+O(n^{-1}).
}
\]

The cubic Dirichlet constant admits the exact Hurwitz-zeta form

\[
\boxed{
L(3,\chi_{12})
=
\frac1{12^3}
\left[
\zeta\!\left(3,\frac1{12}\right)
-
\zeta\!\left(3,\frac5{12}\right)
-
\zeta\!\left(3,\frac7{12}\right)
+
\zeta\!\left(3,\frac{11}{12}\right)
\right].
}
\]

Numerically,

\[
L(3,\chi_{12})\approx0.9900400194381598.
\]

Unlike \(L(1,\chi_{12})=\log(2+\sqrt3)/\sqrt3\) and the parity-matched even value \(L(2,\chi_{12})=\pi^2/(6\sqrt3)\), the cubic value is an opposite-parity special value for this even character. No reduction to the regulator or a simple algebraic multiple of \(\pi^3\) is asserted here.

## Structural interpretation

The exact hierarchy is

\[
\text{χ12 displacement moment of order }j
\longleftrightarrow
L(j,\chi_{12})n^j
\text{ versus quotient-skeleton cancellation}
\longleftrightarrow
\mathcal R_j(n)
\]

with the same terminal mod-12 boundary correction

\[
S(n\bmod12)
\]

for every fixed integer \(j\ge1\).

The carrier guardrail remains in force: χ12 also acts as the Pell-time orientation character on the real quadratic unit, but the shell-displacement moment and the Pell operator remain distinct constructions sharing the same arithmetic character.