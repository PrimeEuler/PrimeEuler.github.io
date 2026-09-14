# Cone Derivation Ledger v13.410 — Shell-Displacement Moment Hierarchy and V4 Energy

Date: 2026-09-13

Status labels: **[D]** exact derived, **[I]** interpretation, **[Audit]** limitation/guardrail.

## 1. Exact bridge from shell coordinate to fractional divisor defect

For

\[
q_k=\left\lfloor\frac nk\right\rfloor,
\qquad
r_k=n-kq_k,
\qquad
\delta_k(n)=\left\{\frac nk\right\}=\frac{r_k}{k},
\]

the Paper-A fixed shell `Y=sqrt(n)` at the column `u=k` has

\[
X_k=\frac12\left(k-\frac nk\right).
\]

Define the quotient skeleton

\[
X_k^{(0)}=\frac{k-q_k}{2}.
\]

Then **[D]**

\[
\boxed{
\Delta X_k:=X_k-X_k^{(0)}
=-\frac12\delta_k(n)
=-\frac{r_k}{2k}.
}
\]

Hence

\[
\boxed{
\Delta X_k=0
\iff
k\mid n.
}
\]

This is an exact geometric carrier for the fractional divisor defect: the true real-shell coordinate differs from the quotient half-lattice skeleton by exactly half the negative fractional defect.

## 2. Full moment hierarchy

For `alpha>0`,

\[
\mathcal S_\alpha(n)=\sum_{k\nmid n}\delta_k(n)^\alpha.
\]

**[D]**

\[
\boxed{
\mathcal S_\alpha(n)
=2^\alpha\sum_{k\nmid n}(-\Delta X_k)^\alpha.
}
\]

At first order,

\[
\boxed{
\mathcal S_1(n)=nH_n-D(n)
=-2\sum_{k=1}^n\Delta X_k.
}
\]

At second order,

\[
\boxed{
\mathcal S_2(n)
=4\sum_{k=1}^n(\Delta X_k)^2.
}
\]

Define the shell-displacement energy

\[
\boxed{
\mathcal E_X(n):=\sum_{k=1}^n(\Delta X_k)^2
=\frac14\mathcal S_2(n).
}
\]

Since `0<=delta_k<1`,

\[
\boxed{
4\mathcal E_X(n)=\mathcal S_2(n)
\le \mathcal S_1(n)
\le n-\tau(n).
}
\]

Thus

\[
\boxed{
\mathcal E_X(n)
\le \frac14(nH_n-D(n))
\le \frac14(n-\tau(n)).
}
\]

## 3. Character-weighted displacement channels

For an arithmetic character/weight `chi`,

\[
\mathcal S_{\alpha,\chi}(n)
=\sum_{k\nmid n}\chi(k)\delta_k(n)^\alpha.
\]

**[D]**

\[
\boxed{
\mathcal S_{\alpha,\chi}(n)
=2^\alpha\sum_{k\nmid n}\chi(k)(-\Delta X_k)^\alpha.
}
\]

In particular,

\[
\boxed{
E_\chi(n):=\mathcal S_{1,\chi}(n)
=-2\sum_{k=1}^n\chi(k)\Delta X_k,
}
\]

and define the quadratic displacement channel

\[
\boxed{
Q_\chi(n):=\mathcal S_{2,\chi}(n)
=4\sum_{k=1}^n\chi(k)(\Delta X_k)^2.
}
\]

`Q_1>=0`; nonprincipal real-character channels are signed residue-sector energy imbalances and need not be positive.

## 4. V4 residue-energy Hadamard decomposition

For unit residues `r in {1,5,7,11}`, define

\[
\mathcal E_r(n)
=\sum_{\substack{k\le n\\k\equiv r\pmod{12}}}(\Delta X_k)^2.
\]

For the four real mod-12 characters, the exact transform is

\[
\boxed{
\frac14
\begin{pmatrix}
Q_1^\times\\Q_{-4}\\Q_{-3}\\Q_{12}
\end{pmatrix}
=
H_4
\begin{pmatrix}
\mathcal E_1\\\mathcal E_5\\\mathcal E_7\\\mathcal E_{11}
\end{pmatrix}.
}
\]

Therefore

\[
\boxed{
\begin{pmatrix}
\mathcal E_1\\\mathcal E_5\\\mathcal E_7\\\mathcal E_{11}
\end{pmatrix}
=
\frac1{16}H_4
\begin{pmatrix}
Q_1^\times\\Q_{-4}\\Q_{-3}\\Q_{12}
\end{pmatrix}.
}
\]

Equivalently, if

\[
\widetilde Q_\chi:=\sum_k\chi(k)(\Delta X_k)^2=Q_\chi/4,
\]

then the transform/inverse use the ordinary `H_4` and `(1/4)H_4` pair.

**[Audit]** The `1/16` above is purely the product of displacement-square scaling (`Q=4\widetilde Q`) and inverse-Hadamard normalization (`1/4`). It has no Casimir/null-diamond interpretation.

## 5. Prime-exponent interpretation and limitation

For

\[
n=\prod_p p^{e_p},
\]

the prime exponents determine the zero-displacement set exactly:

\[
\Delta X_k=0\iff k\mid n.
\]

When `gcd(n,6)=1`, the contact character spectrum is

\[
D_\chi(n)
=\sum_{d\mid n}\chi(d)
=\prod_{p^{e_p}\parallel n}
(1+\chi(p)+\cdots+\chi(p)^{e_p}).
\]

Hence

\[
\boxed{
D_\chi(n)=0
\iff
\exists p^{e_p}\parallel n:\chi(p)=-1,\ e_p\text{ odd}.
}
\]

But the positive displacement moments depend on

\[
\Delta X_k=-\frac{n\bmod k}{2k}.
\]

Therefore **[Audit]** `E_chi` and `Q_chi` do not in general inherit an Euler-product factorization from the prime exponents of `n`. Prime exponents control the zero set; Euclidean remainders control nonzero amplitudes.

## 6. Support endpoint

For each character,

\[
\boxed{
\lim_{\alpha\to0^+}\mathcal S_{\alpha,\chi}(n)
=\sum_{k\nmid n}\chi(k)
=P_\chi(n)-D_\chi(n),
}
\]

where

\[
P_\chi(n)=\sum_{k=1}^n\chi(k).
\]

Thus the shell-displacement family has an exact three-level structure:

- `alpha -> 0+`: displaced support/contact complement, with multiplicative prime-exponent information through `D_chi`;
- `alpha=1`: signed first shell displacement `E_chi`;
- `alpha=2`: quadratic shell-displacement energy `Q_chi`.

## 7. Structural interpretation

**[I]** This gives a clean interface between the continuous cone shell and discrete arithmetic without conflating their carriers:

\[
\boxed{
\text{continuous shell sample}
\to
\Delta X_k
\to
\delta_k
\to
\mathcal S_{\alpha,\chi}.
}
\]

The divisor set is exactly the zero locus of `Delta X`; V4 characters resolve both its contact balance (`D_chi`) and the amplitude moments of its complement (`E_chi`, `Q_chi`).

## 8. Guardrails

- `Delta X_k` is a shell-to-quotient-skeleton coordinate displacement, not a displacement off the cone shell itself.
- `D_chi=0` does not imply `E_chi=0` or `Q_chi=0`.
- Prime-exponent multiplicativity applies to contact/zero-set data, not generally to the positive displacement amplitudes.
- Every Hadamard quarter factor here is group-Fourier normalization only.

Companion note:

`research-notes/Shell_Displacement_Moment_Hierarchy_and_V4_Energy.md`
