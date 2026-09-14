# Cone Derivation Ledger v13.422 — χ12 General Integer-Moment Hierarchy

Date: 2026-09-14

Status labels: **[D]** exact derived; **[I]** interpretation; **[Audit]** guardrail.

## 0. Synchronization

Checked the repository head immediately before writing. The newest numbered ledger entry was v13.421 (`Cyclotomic V4 Character Projectors`), so v13.422 was free at creation time.

This checkpoint extends v13.413 (first χ12 displacement moment), v13.415 (residue-tail profile), and v13.420 (quadratic χ12 displacement energy) to every positive integer moment.

## 1. General χ12 displacement moment [D]

Let

\[
\delta_k(n)=\left\{\frac nk\right\},
\qquad
q_k=\left\lfloor\frac nk\right\rfloor,
\]

and for integer \(j\ge1\),

\[
M_j(n):=\sum_{k\le n}\chi_{12}(k)\delta_k(n)^j.
\]

Because

\[
\delta_k(n)=\frac nk-q_k,
\]

binomial expansion gives

\[
\boxed{
M_j(n)=
\sum_{\ell=0}^{j}
(-1)^\ell\binom{j}{\ell}n^{j-\ell}C_{j,\ell}(n),
}
\]

where

\[
C_{j,\ell}(n)
:=
\sum_{k\le n}
\frac{\chi_{12}(k)q_k^\ell}{k^{j-\ell}}.
\]

For \(\ell=0\),

\[
C_{j,0}(n)=\sum_{k\le n}\frac{\chi_{12}(k)}{k^j}.
\]

## 2. Dirichlet main scale and exact cancellation form [D]

Write

\[
L_j:=L(j,\chi_{12}),
\qquad
T_j(n):=\sum_{k>n}\frac{\chi_{12}(k)}{k^j}.
\]

Then

\[
C_{j,0}(n)=L_j-T_j(n).
\]

Define

\[
\boxed{
\mathcal R_j(n)
:=
\sum_{\ell=1}^{j}
(-1)^{\ell+1}\binom{j}{\ell}
 n^{j-\ell}C_{j,\ell}(n)
-
L_jn^j.
}
\]

Then the full moment identity is

\[
\boxed{
M_j(n)=-\mathcal R_j(n)-n^jT_j(n).
}
\]

Thus the first- and second-moment cancellations were not isolated accidents: they are the first two cases of a general exact binomial cancellation architecture.

## 3. Quotient-skeleton transform [D]

For \(\ell\ge1\),

\[
q_k^\ell
=
\sum_{m=1}^{q_k}\left(m^\ell-(m-1)^\ell\right).
\]

Hence

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
H_s^{(\chi)}(N)
:=
\sum_{k\le N}\frac{\chi_{12}(k)}{k^s},
\]

and \(H_0^{(\chi)}(N)=\sum_{k\le N}\chi_{12}(k)\).

So the j-th shell-displacement moment is controlled by a finite hierarchy of χ12 reciprocal partial sums sampled on the quotient skeleton.

## 4. Universal residue-boundary law [D]

Write

\[
n=12m+r,
\qquad0\le r\le11,
\]

and

\[
S(r):=\sum_{a=1}^{r}\chi_{12}(a).
\]

Explicitly,

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

For every fixed integer \(j\ge1\), summation by parts using periodicity and zero mean gives

\[
\boxed{
n^jT_j(n)=-S(r)+O(n^{-1})
\qquad(n\equiv r\pmod{12}).
}
\]

Therefore

\[
\boxed{
M_j(n)=-\mathcal R_j(n)+S(n\bmod12)+O(n^{-1}).
}
\]

The same five-level boundary profile survives for every positive integer moment.

## 5. Cubic test [D]

For \(j=3\), define

\[
A_3(n):=\sum_{k\le n}\frac{\chi_{12}(k)q_k}{k^2},
\]

\[
B_3(n):=\sum_{k\le n}\frac{\chi_{12}(k)q_k^2}{k},
\]

\[
C_3(n):=\sum_{k\le n}\chi_{12}(k)q_k^3.
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

With

\[
L_3=L(3,\chi_{12}),
\]

define

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
M_3(n)=-\mathcal R_3(n)-n^3T_3(n),
}
\]

and along each residue class,

\[
\boxed{
M_3(n)=-\mathcal R_3(n)+S(r)+O(n^{-1}).
}
\]

## 6. Cubic Dirichlet constant [D/Audit]

The exact Hurwitz-zeta representation is

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

**[Audit]** χ12 is even, while \(3\) has opposite parity. No claim is made that this value reduces to the regulator or to a simple algebraic multiple of \(\pi^3\). The safe exact representation is the Dirichlet/Hurwitz-zeta value above.

## 7. Structural synthesis [I]

The exact hierarchy is now

\[
\boxed{
\text{moment order }j
\longrightarrow
L(j,\chi_{12})n^j
\longrightarrow
\text{quotient-skeleton cancellation}
\longrightarrow
\mathcal R_j(n)
\longrightarrow
S(n\bmod12).
}
\]

The analytic constant changes with j, but the terminal residue boundary law does not.

The previously established Pell-time-orientation interpretation of χ12 remains a separate carrier-level fact: the same character weights the shell-displacement moments and acts on the real quadratic Pell unit by orientation preservation/reversal. No Pell action on the integer divisor lattice is inferred.

---

Checkpoint conclusion: The first and second χ12 displacement moments extend to a full exact integer-moment hierarchy. Every fixed j has a Dirichlet main scale \(L(j,\chi_{12})n^j\), an exact finite quotient-skeleton remainder, and the same five-level mod-12 boundary profile. The cubic case confirms the architecture while introducing an opposite-parity special value \(L(3,\chi_{12})\), showing that higher moments genuinely probe new analytic constants rather than merely powers of the Pell regulator.