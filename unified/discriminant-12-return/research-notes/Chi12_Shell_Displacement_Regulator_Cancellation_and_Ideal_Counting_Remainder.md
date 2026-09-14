# The χ12 Shell-Displacement Channel, Regulator Cancellation, and the Ideal-Counting Remainder

Status labels: **[D]** exact derived identity; **[I]** interpretation; **[Audit]** scope/guardrail.

## 1. Setup

Let

\[
q_k=\left\lfloor\frac nk\right\rfloor,
\qquad
\delta_k(n)=\left\{\frac nk\right\},
\qquad
\Delta X_k:=X_k-X_k^{(0)}=-\frac12\delta_k(n).
\]

For the real primitive quadratic character modulo 12,

\[
\chi_{12}(k)=
\begin{cases}
+1,&k\equiv1,11\pmod{12},\\
-1,&k\equiv5,7\pmod{12},\\
0,&(k,12)>1,
\end{cases}
\]

define the first shell-displacement character moment

\[
E_{12}(n)
:=\sum_{k\le n}\chi_{12}(k)\delta_k(n)
=-2\sum_{k\le n}\chi_{12}(k)\Delta X_k.
\]

The Pell-return thread gives the exact regulator identity

\[
R_{12}=\log(2+\sqrt3),
\qquad
L(1,\chi_{12})=\frac{R_{12}}{\sqrt3}.
\]

The purpose of this note is to determine exactly how that regulator enters the shell-displacement channel.

## 2. Exact divisor-convolution form [D]

Since

\[
\delta_k(n)=\frac nk-\left\lfloor\frac nk\right\rfloor,
\]

we have

\[
E_{12}(n)
=
n\sum_{k\le n}\frac{\chi_{12}(k)}k
-
\sum_{k\le n}\chi_{12}(k)\left\lfloor\frac nk\right\rfloor.
\]

Rearranging the floor term,

\[
\sum_{k\le n}\chi_{12}(k)\left\lfloor\frac nk\right\rfloor
=
\sum_{km\le n}\chi_{12}(k)
=
\sum_{j\le n}\sum_{d\mid j}\chi_{12}(d).
\]

Define

\[
a_{12}(j):=(1*\chi_{12})(j)=\sum_{d\mid j}\chi_{12}(d),
\]

and its summatory function

\[
\mathcal I_{12}(n):=\sum_{j\le n}a_{12}(j).
\]

Then

\[
\boxed{
E_{12}(n)
=
n\sum_{k\le n}\frac{\chi_{12}(k)}k
-
\mathcal I_{12}(n).
}
\]

The Dirichlet series of \(a_{12}\) is

\[
\sum_{m\ge1}\frac{a_{12}(m)}{m^s}
=
\zeta(s)L(s,\chi_{12}),
\]

so \(\mathcal I_{12}\) is exactly the ideal-counting summatory function associated with \(\mathbf Q(\sqrt3)\).

## 3. Exact regulator cancellation [D]

Write

\[
L_{12}:=L(1,\chi_{12})=\frac{R_{12}}{\sqrt3}
\]

and define the tail

\[
T_{12}(n):=\sum_{k>n}\frac{\chi_{12}(k)}k.
\]

Then

\[
\sum_{k\le n}\frac{\chi_{12}(k)}k
=L_{12}-T_{12}(n).
\]

Also define the ideal-counting remainder after removal of the regulator main term,

\[
\mathcal R_{12}(n)
:=
\mathcal I_{12}(n)-L_{12}n.
\]

Substituting into the exact displacement formula gives

\[
E_{12}(n)
=
n(L_{12}-T_{12}(n))-
(L_{12}n+\mathcal R_{12}(n)).
\]

Therefore the two regulator main terms cancel identically:

\[
\boxed{
E_{12}(n)
=
-\mathcal R_{12}(n)-nT_{12}(n).
}
\]

Equivalently, in shell-displacement coordinates,

\[
\boxed{
\sum_{k\le n}\chi_{12}(k)\Delta X_k
=
\frac12\left(\mathcal R_{12}(n)+nT_{12}(n)\right).
}
\]

This is the exact regulator bridge. The regulator does not survive as a raw linear term in \(E_{12}\); it is the common main term of two different finite truncations and cancels between them.

## 4. Uniformly bounded truncation correction [D]

Let

\[
S_{12}(m):=\sum_{k\le m}\chi_{12}(k).
\]

Over one period modulo 12 the cumulative values are

\[
1,1,1,1,0,0,-1,-1,-1,-1,0,0,
\]

so

\[
\boxed{|S_{12}(m)|\le1\quad\text{for all }m.}
\]

By summation by parts,

\[
T_{12}(n)
=
-\frac{S_{12}(n)}{n+1}
+
\sum_{m=n+1}^{\infty}
\frac{S_{12}(m)}{m(m+1)}.
\]

Hence

\[
|T_{12}(n)|
\le
\frac1{n+1}
+
\sum_{m=n+1}^{\infty}\frac1{m(m+1)}
=
\frac{2}{n+1}.
\]

Therefore

\[
\boxed{
|nT_{12}(n)|<2.
}
\]

Combining with the exact cancellation identity,

\[
\boxed{
\left|E_{12}(n)+\mathcal R_{12}(n)\right|<2.
}
\]

This is a strong exact comparison: the first \(\chi_{12}\) shell-displacement moment differs from the negative ideal-counting remainder by a uniformly bounded quantity.

## 5. Interpretation [I]

The same real-quadratic regulator

\[
R_{12}=\log(2+\sqrt3)
\]

enters two already-established structures:

1. the primitive rapidity step of the discriminant-12 Pell/Cone return;
2. the linear main term \(L(1,\chi_{12})n=(R_{12}/\sqrt3)n\) of the \(\chi_{12}\) ideal-counting summatory function.

The shell-displacement channel does not add a third independent regulator term. Instead it measures the mismatch between:

- the truncated reciprocal character sum \(n\sum_{k\le n}\chi_{12}(k)/k\), and
- the truncated ideal-counting convolution \(\mathcal I_{12}(n)\).

Their common regulator contribution cancels exactly.

Thus the exact chain is

\[
\boxed{
\text{Cone shell displacement}
\longrightarrow
E_{12}(n)
\longleftrightarrow
-\mathcal R_{12}(n)
\text{ up to a bounded tail}
}
\]

rather than a claim of the form \(E_{12}\sim nR_{12}\).

## 6. Relation to the V4 channels [D/I]

The identity is special to the \(\chi_{12}\) channel only in the arithmetic constant being used. For any nonprincipal Dirichlet character \(\chi\), one has formally

\[
E_\chi(n)
=
n\sum_{k\le n}\frac{\chi(k)}k
-
\sum_{j\le n}(1*\chi)(j).
\]

Whenever \(L(1,\chi)\) is introduced and the corresponding summatory main term is separated,

\[
E_\chi(n)
=
-\mathcal R_\chi(n)-nT_\chi(n).
\]

What makes \(\chi_{12}\) structurally distinguished in this project is that

\[
L(1,\chi_{12})=\frac{\log(2+\sqrt3)}{\sqrt3}
\]

contains exactly the same regulator as the canonical Pell return.

## 7. Guardrails [Audit]

- This does **not** show that the Pell matrix acts on the integer divisor lattice.
- This does **not** identify the cyclic Pell return with the V4 action.
- This does **not** imply \(E_{12}(n)\) is asymptotic to \(nR_{12}\); the linear regulator term cancels exactly.
- No RH/GRH or divisor-error bound is inferred here.
- The bounded tail statement uses only periodicity and the exact bound \(|S_{12}|\le1\).

## 8. Next exact targets

1. Derive an exact residue-class formula for \(T_{12}(n)\) as a function of \(n\bmod12\), e.g. via digamma differences or period blocks.
2. Compare the quadratic displacement channel \(Q_{12}(n)=\sum\chi_{12}(k)\delta_k(n)^2\) with a corresponding second-order convolution/remainder object.
3. Place the first-moment identity beside the V4 contact-distribution Parseval energy to separate zero-set Fourier energy from displacement-amplitude Fourier energy.

---

**Checkpoint conclusion.** The regulator bridge is exact but subtractive: the same \(R_{12}=\log(2+\sqrt3)\) appears in both finite objects underlying \(E_{12}\), and their linear regulator terms cancel. The surviving shell-displacement statistic is the negative \(\chi_{12}\) ideal-counting remainder plus a uniformly bounded character-tail correction.