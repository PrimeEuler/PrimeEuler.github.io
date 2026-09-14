# Cone Derivation Ledger v13.415 — χ12 Tail Residue Profile and Time Orientation

Date: 2026-09-14

Status labels: **[D]** exact derived, **[I]** interpretation, **[Audit]** limitation/guardrail.

## 0. Synchronization

This checkpoint was assigned only after checking the current repository head. `v13.414` had already been added concurrently and proves the exact Galois/Pell orientation identity

\[
\sigma_r(\lambda)=\lambda^{\chi_{12}(r)},
\qquad \lambda=2+\sqrt3.
\]

Thus `v13.415` is the next free ledger number.

## 1. Previous exact identity [D]

From `v13.413`,

\[
E_{12}(n)
=-\mathcal R_{12}(n)-nT_{12}(n),
\]

with

\[
T_{12}(n)=\sum_{k>n}\frac{\chi_{12}(k)}{k},
\]

and

\[
\mathcal R_{12}(n)
=\mathcal I_{12}(n)-\frac{R_{12}}{\sqrt3}n,
\qquad
R_{12}=\log(2+\sqrt3).
\]

The goal here is to resolve the bounded tail correction by the residue class of \(n\pmod{12}\).

## 2. Exact residue-class tail formula [D]

Write

\[
n=12m+r,
\qquad 0\le r\le11.
\]

For \(a\in\{1,5,7,11\}\), set

\[
J_a=m+\mathbf1_{\{a\le r\}}.
\]

Then

\[
\boxed{
T_{12}(12m+r)
=\frac1{12}
\left[
-\psi\!\left(J_1+\frac1{12}\right)
+\psi\!\left(J_5+\frac5{12}\right)
+\psi\!\left(J_7+\frac7{12}\right)
-\psi\!\left(J_{11}+\frac{11}{12}\right)
\right].
}
\]

This follows by splitting the character tail into its four unit residue classes and using zero mean of \(\chi_{12}\) over one period.

## 3. Five residue profiles [D]

Define

\[
S(r)=\sum_{a=1}^{r}\chi_{12}(a).
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

Thus the twelve residue classes collapse into five distinct boundary-tail types.

## 4. Asymptotic residue correction [D]

For fixed \(r\), the digamma expansion gives

\[
T_{12}(12m+r)
=-\frac{S(r)}{12m}+O(m^{-2}).
\]

Therefore

\[
\boxed{
nT_{12}(n)
=-S(r)+O(n^{-1})
\qquad(n\equiv r\pmod{12}).
}
\]

Equivalently,

\[
\boxed{
\lim_{\substack{n\to\infty\\n\equiv r\,(12)}}nT_{12}(n)
=-S(r).
}
\]

Hence

\[
\boxed{
\lim_{\substack{n\to\infty\\n\equiv r\,(12)}}
\bigl(E_{12}(n)+\mathcal R_{12}(n)\bigr)
=S(r).
}
\]

Explicitly,

\[
\begin{array}{c|ccccc}
r & 0 & 1,2,3,4 & 5,6 & 7,8,9,10 & 11\\
\hline
S(r)&0&+1&0&-1&0
\end{array}
\]

and therefore

\[
\boxed{
E_{12}(n)
=-\mathcal R_{12}(n)
+S(n\bmod12)
+O(n^{-1}).
}
\]

## 5. Relation to v13.414 time orientation [D/I]

`v13.414` proves

\[
\chi_{12}(r)=+1
\iff
\sigma_r(\lambda)=\lambda,
\]

and

\[
\chi_{12}(r)=-1
\iff
\sigma_r(\lambda)=\lambda^{-1}.
\]

Thus

\[
S(r)=\sum_{a\le r}\chi_{12}(a)
\]

is exactly the cumulative imbalance, inside the final incomplete mod-12 block, between orientation-preserving and orientation-reversing character values.

The same character weights the shell-displacement statistic

\[
E_{12}(n)
=-2\sum_{k\le n}\chi_{12}(k)\Delta X_k.
\]

**[I]** The finite correction left after regulator cancellation is therefore naturally read as a boundary truncation imbalance in the same sign channel that controls Pell time orientation.

**[Audit]** The carriers remain distinct. The Pell operator is not asserted to act on the integer divisor lattice; the exact common object is the character \(\chi_{12}\).

## 6. Structural conclusion

The χ12 shell-displacement channel now decomposes into three layers:

\[
\boxed{
\text{common regulator main term}
\;\longrightarrow\;
\text{exact cancellation},
}
\]

\[
\boxed{
\text{ideal-counting fluctuation}
\;\longrightarrow\;
-\mathcal R_{12}(n),
}
\]

\[
\boxed{
\text{finite residue-boundary imbalance}
\;\longrightarrow\;
S(n\bmod12)+O(n^{-1}).
}
\]

This sharpens `v13.413`: the bounded tail is not arbitrary. It has an explicit exact digamma form and converges on each residue class to the partial-sum profile of the same \(\chi_{12}\) that `v13.414` identifies as the Pell time-orientation character.

## Guardrails

- Exact digamma identity and exact `v13.413` decomposition are distinct from the residue-class asymptotic expansion.
- The values \(0,\pm1\) are partial character sums, not Pell matrices and not new V4 carriers.
- No RH/GRH or divisor-error estimate is promoted.
- No direct action on integer factor pairs is inferred.
