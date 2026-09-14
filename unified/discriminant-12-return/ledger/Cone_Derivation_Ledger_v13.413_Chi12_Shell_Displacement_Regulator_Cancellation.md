# Cone Derivation Ledger v13.413 — χ12 Shell Displacement, Regulator Cancellation, and Ideal-Counting Remainder

Date: 2026-09-14

Status labels: **[S]** source-established, **[D]** exact derived, **[I]** interpretation, **[Audit]** correction/limitation.

## Provenance

This checkpoint continues v13.410 after the Pell-return updates now renumbered v13.411-v13.412 by External Audit Round 27. Round 27 independently reverified the v13.410 shell-displacement identities and the v13.411-v13.412 Pell/CRT identities. The present result uses those verified ingredients but derives a new exact χ12 relation.

Companion note:

`research-notes/Chi12_Shell_Displacement_Regulator_Cancellation_and_Ideal_Counting_Remainder.md`

## 1. Shell-displacement character moment [D]

For

\[
\Delta X_k:=X_k-X_k^{(0)}=-\frac12\left\{\frac nk\right\},
\]

define

\[
E_{12}(n)
:=\sum_{k\le n}\chi_{12}(k)\left\{\frac nk\right\}
=-2\sum_{k\le n}\chi_{12}(k)\Delta X_k.
\]

Using

\[
\left\{\frac nk\right\}
=\frac nk-\left\lfloor\frac nk\right\rfloor,
\]

one obtains

\[
\boxed{
E_{12}(n)
=
n\sum_{k\le n}\frac{\chi_{12}(k)}k
-
\mathcal I_{12}(n),
}
\]

where

\[
\mathcal I_{12}(n)
:=\sum_{m\le n}(1*\chi_{12})(m)
=
\sum_{m\le n}\sum_{d\mid m}\chi_{12}(d).
\]

The Dirichlet series is

\[
\sum_{m\ge1}\frac{(1*\chi_{12})(m)}{m^s}
=\zeta(s)L(s,\chi_{12}),
\]

so \(\mathcal I_{12}\) is the corresponding real-quadratic ideal-counting summatory function.

## 2. Exact regulator cancellation [D]

From v13.411,

\[
R_{12}=\log(2+\sqrt3),
\qquad
L(1,\chi_{12})=\frac{R_{12}}{\sqrt3}.
\]

Set

\[
L_{12}:=L(1,\chi_{12}),
\qquad
T_{12}(n):=\sum_{k>n}\frac{\chi_{12}(k)}k,
\]

and define

\[
\mathcal R_{12}(n)
:=
\mathcal I_{12}(n)-L_{12}n.
\]

Then

\[
\sum_{k\le n}\frac{\chi_{12}(k)}k
=L_{12}-T_{12}(n),
\]

so the regulator main terms cancel identically:

\[
\boxed{
E_{12}(n)
=
-\mathcal R_{12}(n)-nT_{12}(n).
}
\]

Equivalently,

\[
\boxed{
\sum_{k\le n}\chi_{12}(k)\Delta X_k
=
\frac12\left(\mathcal R_{12}(n)+nT_{12}(n)\right).
}
\]

Thus the χ12 shell-displacement channel does not contain an uncancelled linear \(nR_{12}/\sqrt3\) term.

## 3. Uniform boundedness of the truncation correction [D]

For

\[
S_{12}(m):=\sum_{k\le m}\chi_{12}(k),
\]

the exact period-12 cumulative values imply

\[
\boxed{|S_{12}(m)|\le1.}
\]

Summation by parts yields

\[
T_{12}(n)
=
-\frac{S_{12}(n)}{n+1}
+
\sum_{m=n+1}^{\infty}\frac{S_{12}(m)}{m(m+1)}.
\]

Therefore

\[
|T_{12}(n)|\le\frac{2}{n+1},
\]

and hence

\[
\boxed{|nT_{12}(n)|<2.}
\]

Combining with the cancellation identity gives the quantitative bridge

\[
\boxed{
\left|E_{12}(n)+\mathcal R_{12}(n)\right|<2.
}
\]

So the first χ12 shell-displacement moment differs from the negative ideal-counting remainder by a uniformly bounded term.

## 4. Structural interpretation [I]

The same regulator

\[
R_{12}=\log(2+\sqrt3)
\]

has two established roles:

1. primitive rapidity step of the discriminant-12 Pell/Cone return;
2. linear coefficient \(L(1,\chi_{12})=R_{12}/\sqrt3\) in the χ12 ideal-counting summatory main term.

The shell-displacement channel measures the mismatch between two finite truncations carrying that same main term:

\[
n\sum_{k\le n}\frac{\chi_{12}(k)}k
\quad\text{and}\quad
\mathcal I_{12}(n).
\]

The common linear regulator term cancels, leaving the ideal-counting remainder plus a bounded character-tail correction.

## 5. Audit guardrails

- No claim that the Pell matrix acts on the integer divisor lattice.
- No identification of the Pell cyclic return with the V4 action.
- No claim \(E_{12}(n)\sim nR_{12}\); the linear regulator term cancels exactly.
- No RH/GRH or divisor-error estimate is inferred.
- The bound \(<2\) uses only periodicity and \(|S_{12}|\le1\).

## 6. Next exact targets

1. Resolve \(T_{12}(n)\) explicitly by \(n\bmod12\), eliminating the remaining infinite-tail notation.
2. Test whether the quadratic displacement channel
   \[
   Q_{12}(n)=\sum_{k\le n}\chi_{12}(k)\left\{\frac nk\right\}^2
   \]
   admits an analogous second-order convolution decomposition.
3. Compare the displacement-energy V4 Parseval decomposition with the contact-distribution L2 Parseval decomposition without conflating their carriers.

---

**Checkpoint conclusion.** The Pell regulator enters the χ12 shell-displacement channel only through two equal linear main terms that cancel exactly. What remains is the negative χ12 ideal-counting remainder plus a uniformly bounded tail correction:

\[
\boxed{
E_{12}(n)=-\mathcal R_{12}(n)-nT_{12}(n),
\qquad
|E_{12}(n)+\mathcal R_{12}(n)|<2.
}
\]
