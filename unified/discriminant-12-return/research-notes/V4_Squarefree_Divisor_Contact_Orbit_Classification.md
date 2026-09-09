# V4 Squarefree Divisor-Contact Orbit Classification

## Status
Exact continuation of v13.378-v13.379. Entirely arithmetic/group-theoretic. No Casimir, null-diamond, or quarter-shift identification is used here.

## 1. Setup
Assume
\[
\gcd(n,6)=1
\]
and \(n\) is squarefree. Write
\[
n=\prod_{i=1}^{\omega(n)}p_i,
\]
with each prime residue in
\[
U(12)=\{1,5,7,11\}\cong V_4.
\]

Let
\[
C_r(n)=\#\{d\mid n:d\equiv r\pmod{12}\},
\qquad r\in\{1,5,7,11\}.
\]
Then
\[
\mathbf C(n)=(C_1,C_5,C_7,C_{11})^T
\]
is the divisor-shell contact vector on the four unit residue classes.

For each prime factor \(p_i\), selecting whether or not \(p_i\) appears in a divisor contributes the group-algebra factor
\[
1+e_{p_i\bmod 12}.
\]
Thus
\[
\boxed{
\mathbf C(n)=\mathop{*}_{p\mid n}(\delta_1+\delta_{p\bmod12}).
}
\]

## 2. Residue multiplicities
Let
\[
a_1=\#\{p\mid n:p\equiv1\pmod{12}\},
\]
\[
a_5=\#\{p\mid n:p\equiv5\pmod{12}\},
\]
\[
a_7=\#\{p\mid n:p\equiv7\pmod{12}\},
\]
\[
a_{11}=\#\{p\mid n:p\equiv11\pmod{12}\}.
\]
Then
\[
\omega(n)=a_1+a_5+a_7+a_{11}.
\]

A prime with residue \(1\) contributes
\[
\delta_1+\delta_1=2\delta_1,
\]
so each such prime simply doubles every eventual contact multiplicity. Therefore the support pattern is controlled entirely by the set
\[
S(n)=\{r\in\{5,7,11\}:a_r>0\}.
\]

Let
\[
H(n)=\langle S(n)\rangle\le V_4.
\]

## 3. Uniformity on the generated subgroup
For any nonidentity \(g\in V_4\),
\[
(\delta_1+\delta_g)*(\delta_1+\delta_g)
=2(\delta_1+\delta_g).
\]
Hence repeated prime factors from the same residue class change multiplicity but not support.

For squarefree \(n\), convolution by one factor \(\delta_1+\delta_g\) averages uniformly over the two-element subgroup \(\{1,g\}\). Once generators span a subgroup \(H\), the divisor residue distribution is uniform on \(H\).

Precisely,
\[
\boxed{
C_r(n)=
\begin{cases}
2^{\omega(n)}/|H(n)|,&r\in H(n),\\
0,&r\notin H(n).
\end{cases}
}
\]

Equivalently,
\[
\boxed{
\mathbf C(n)=2^{\omega(n)-\operatorname{rank}H(n)}\,\mathbf 1_{H(n)},
}
\]
where \(\operatorname{rank}H\in\{0,1,2\}\) as an \(\mathbf F_2\)-vector space and \(\mathbf1_H\) is the indicator vector of the subgroup.

## 4. Complete orbit classification
There are only three structural types.

### Type 0: trivial subgroup
If
\[
S(n)=\varnothing,
\]
so every prime divisor satisfies \(p\equiv1\pmod{12}\), then
\[
H=\{1\}
\]
and
\[
\boxed{
(C_1,C_5,C_7,C_{11})=(2^{\omega},0,0,0).
}
\]

### Type 1: one nontrivial generator
If exactly one of \(5,7,11\) occurs among prime residues, then \(H\) has order \(2\).

If only residue 5 occurs (besides 1):
\[
\boxed{
\mathbf C=2^{\omega-1}(1,1,0,0).
}
\]

If only residue 7 occurs:
\[
\boxed{
\mathbf C=2^{\omega-1}(1,0,1,0).
}
\]

If only residue 11 occurs:
\[
\boxed{
\mathbf C=2^{\omega-1}(1,0,0,1).
}
\]

### Type 2: full V4
Any two distinct nonidentity elements of \(V_4\) generate all of \(V_4\). Therefore if at least two of \(5,7,11\) occur among the prime factors,
\[
H=V_4
\]
and
\[
\boxed{
(C_1,C_5,C_7,C_{11})=2^{\omega-2}(1,1,1,1).
}
\]

Thus every unit residue class receives exactly one quarter of all divisors in the full-rank squarefree case.

Important normalization guardrail: the fraction \(1/4\) here is simply \(1/|V_4|\), i.e. uniform distribution over a four-element finite group. It is unrelated to any Casimir or mixed-cell quarter.

## 5. Character-side interpretation
The four character sums are
\[
D_\chi(n)=\sum_{d\mid n}\chi(d).
\]
For squarefree \(n\),
\[
D_\chi(n)=\prod_{p\mid n}(1+\chi(p)).
\]
Hence
\[
D_\chi(n)=
\begin{cases}
2^{\omega(n)},&\chi(p)=+1\text{ for every }p\mid n,\\
0,&\text{otherwise}.
\end{cases}
\]

This is exactly the annihilator-subgroup statement:
\[
\boxed{
D_\chi(n)\neq0
\iff
\chi|_{H(n)}\equiv1.
}
\]

Therefore the set of surviving character channels is the annihilator
\[
H(n)^\perp\subset\widehat{V_4}.
\]
Since
\[
|H|\,|H^\perp|=4,
\]
we have the exact dual rank relation
\[
\boxed{
\operatorname{rank}H+\operatorname{rank}H^\perp=2.
}
\]

Consequences:
- Type 0: all four character channels survive.
- Type 1: exactly two channels survive: the trivial channel and the unique nontrivial character whose kernel is that order-2 subgroup.
- Type 2: only the trivial channel survives.

This gives a clean support/character duality for squarefree divisor contacts.

## 6. Explicit character table check
Using columns \((1,5,7,11)\),
\[
H_4=
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix},
\]
with rows \((1,\chi_{-4},\chi_{-3},\chi_{12})\).

For the three rank-1 subgroups:

\[
\{1,5\}=\ker\chi_{-4},
\]
so the surviving channels are \(1\) and \(\chi_{-4}\).

\[
\{1,7\}=\ker\chi_{-3},
\]
so the surviving channels are \(1\) and \(\chi_{-3}\).

\[
\{1,11\}=\ker\chi_{12},
\]
so the surviving channels are \(1\) and \(\chi_{12}\).

If the prime residues generate all of \(V_4\), every nontrivial character is negative on at least one prime residue, hence every nontrivial divisor-character sum vanishes.

## 7. Contact-vector entropy is subgroup rank
Because the divisor contacts are uniform on \(H\), the normalized contact distribution has Shannon entropy
\[
\mathcal H(n)=\log_2|H(n)|.
\]
Thus in the squarefree coprime-to-6 case,
\[
\boxed{
\mathcal H(n)=\operatorname{rank}H(n)\in\{0,1,2\}.
}
\]
This is only a finite-group description of residue spread; no analytic-number-theory significance is asserted.

## 8. Examples
### Prime \(p\equiv5\pmod{12}\)
\[
\mathbf C=(1,1,0,0).
\]

### Product \(pq\), both \(\equiv5\pmod{12}\)
\[
\mathbf C=(2,2,0,0).
\]
The support remains the same order-2 subgroup.

### \(p\equiv5\), \(q\equiv7\pmod{12}\)
The residues \(5,7\) generate \(V_4\), so
\[
\mathbf C=(1,1,1,1).
\]

### Add any number of primes \(\equiv1\pmod{12}\)
They multiply all entries by a common factor \(2^{a_1}\) without changing the orbit type.

## 9. Guardrails
- This classification assumes squarefree \(n\) and \(\gcd(n,6)=1\).
- The group-theoretic \(1/4\) in the full-rank contact distribution is \(1/|V_4|\), not a cross-context quarter invariant.
- Character-channel vanishing here is cancellation/orthogonality, not a shell-contact zero criterion for individual columns.
- The classification concerns residue classes of actual divisors, not factor cells or oscillator states.
- No primality criterion beyond ordinary divisor-count facts is claimed.
