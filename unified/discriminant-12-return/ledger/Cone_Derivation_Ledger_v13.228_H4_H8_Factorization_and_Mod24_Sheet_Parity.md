# Cone Derivation Ledger v13.228 — H4/H8 Factorization and Mod-24 Sheet Parity

Date: 2026-09-04
Status: EXACT NEW RESULT — continuation of v13.227; research branch remains open

## 0. Pre-write synchronization

Immediately before this write, the current `master` tree was re-fetched. Its tip was

`353b5c5c2a44bd7b3309aed2513b294eb47c4e62`

with v13.227 as the highest ledger checkpoint. No newer external-audit checkpoint had landed. This continuation therefore reconciles against the current branch tip before writing.

## 1. H4 already isolates the discriminant-12 mode

Order the unit residues by

\[
(1,5,7,11).
\]

The `V_4` Hadamard character table is

\[
H_4=
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix},
\qquad H_4^2=4I.
\]

The discriminant-12 character vector is exactly the fourth row/column:

\[
c_{12}=(1,-1,-1,1)^T.
\]

Therefore

\[
\boxed{H_4c_{12}=(0,0,0,4)^T.}
\]

So in the finite `V_4` Fourier basis, the string sign pattern is already a pure single character channel. Nothing further has to be discovered spectrally at the four-state level.

## 2. Unit-restricted 12-point DFT kernel

Let

\[
K_{12}(m,r)=e^{2\pi i mr/12},
\qquad m,r\in U(12).
\]

This is the unit-to-unit block of the ordinary 12-point DFT. Since the entry depends only on the product `mr` in the abelian group `U(12)`, the `H_4` character basis diagonalizes this block.

With character order

\[
(\chi_0,\chi_{-4},\chi_{-3},\chi_{12}),
\]

one obtains

\[
\boxed{
\frac14 H_4 K_{12} H_4
=
\operatorname{diag}(0,\,2i,\,0,\,2\sqrt3).
}
\]

The final eigenvalue reproduces the Gauss-sum result of v13.227:

\[
\boxed{K_{12}c_{12}=2\sqrt3\,c_{12}.}
\]

The zero and modified eigenvalues in the other channels are consistent with the conductor/imprimitivity distinctions already audited in v13.225.

## 3. Exact direct-product structure of U(24)

The mod-24 unit group is

\[
U(24)=\{1,5,7,11,13,17,19,23\}\cong C_2^3.
\]

The subset

\[
A=\{1,5,7,11\}
\]

is itself a subgroup of `U(24)` and maps isomorphically to `U(12)`. The kernel of reduction modulo 12 is

\[
B=\{1,13\}\cong C_2.
\]

Because the group is abelian and `A cap B={1}`,

\[
\boxed{U(24)=A\times B\cong U(12)\times C_2.}
\]

Every element can be written uniquely as

\[
r=a\,13^\varepsilon,
\qquad a\in A,\quad \varepsilon\in\{0,1\}.
\]

Since `a` is odd,

\[
a13\equiv a+12\pmod{24},
\]

so this is exactly the two-sheet lift found in v13.226.

## 4. The chi12 mode is sheet-even

Lift the discriminant-12 character from `U(12)` to `U(24)` by

\[
\widetilde\chi_{12}(a13^\varepsilon)=\chi_{12}(a).
\]

Thus the mode is independent of the sheet bit `epsilon`:

\[
\boxed{\widetilde\chi_{12}=\chi_{12}\otimes 1_B.}
\]

In the ordered residue list

\[
(1,5,7,11,13,17,19,23),
\]

its values are

\[
\boxed{(1,-1,-1,1,1,-1,-1,1).}
\]

Hence the extra mod-24 Boolean coordinate factors cleanly from the existing discriminant-12 mode.

## 5. H8 factorization

Choose the product ordering `(a,epsilon)` on `A x B`. Then the Walsh-Hadamard transform factors as

\[
\boxed{H_8=H_4\otimes H_2}
\]

up to the corresponding ordering convention, with

\[
H_2=\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]

Since

\[
H_4c_{12}=4e_{\chi_{12}},
\qquad
H_2(1,1)^T=(2,0)^T,
\]

we obtain

\[
\boxed{
H_8(\chi_{12}\otimes1)
=8\,e_{(\chi_{12},\mathrm{even\ sheet})}.
}
\]

Thus the mod-24 lift of the discriminant-12 pattern remains a single pure Walsh character, with trivial character on the new sheet bit.

This answers the immediate question posed in v13.227: **yes, the mod-24 sheet bit factors exactly and cleanly from the existing discriminant-12 mode.**

## 6. Ordinary 24-point DFT detects the sheet parity differently

Now regard the same lifted function as a 24-periodic function on all residues, extended by zero off `U(24)`. Since

\[
\widetilde\chi_{12}(r+12)=\widetilde\chi_{12}(r),
\]

it has period 12 inside the 24-point array.

Its unnormalized 24-point DFT is

\[
\widehat{\widetilde\chi}_{12}(m)
=
\sum_{r\bmod24}
\widetilde\chi_{12}(r)e^{2\pi i mr/24}.
\]

Split `r=a+12epsilon` with `a in U(12)` and `epsilon in {0,1}`:

\[
\widehat{\widetilde\chi}_{12}(m)
=
\sum_{a\in U(12)}\chi_{12}(a)e^{2\pi i ma/24}
\sum_{\varepsilon=0}^1(-1)^{m\varepsilon}.
\]

The sheet sum is

\[
1+(-1)^m.
\]

Therefore

\[
\boxed{
\widehat{\widetilde\chi}_{12}(m)=0
\quad\text{for odd }m.
}
\]

For `m=2k`,

\[
\widehat{\widetilde\chi}_{12}(2k)
=2\sum_{a\in U(12)}\chi_{12}(a)e^{2\pi i ka/12}
=2\sqrt{12}\,\chi_{12}(k).
\]

Hence

\[
\boxed{
\widehat{\widetilde\chi}_{12}(2k)
=4\sqrt3\,\chi_{12}(k).
}
\]

The nonzero 24-point Fourier frequencies are therefore

\[
\boxed{m\in\{2,10,14,22\}=2U(12),}
\]

with the same sign pattern `(+,-,-,+)`.

## 7. Interpretation

There are now two exact transforms with complementary behavior:

1. **Walsh/Hadamard on the unit group:** the mode remains inside `U(24)` and is the pure character `chi12 tensor sheet-even`.
2. **Ordinary cyclic DFT on 24 positions:** sheet-evenness forces all odd frequencies to vanish and moves the spectral support to the doubled set `2U(12)`.

Thus the extra mod-24 sheet bit is not merely decorative. It appears as an exact parity selector in ordinary frequency space:

\[
\boxed{
\text{sheet-even}\Longrightarrow\text{even Fourier frequencies only}.
}
\]

The same discriminant-12 four-sign pattern survives on those even frequencies.

## 8. Current intertwining diagram

The branch now supports the exact diagram

\[
\boxed{
\begin{array}{ccc}
U(12) & \xrightarrow{\text{lift}} & U(24)=U(12)\times C_2\\
\chi_{12} & \mapsto & \chi_{12}\otimes1\\
H_4\downarrow && \downarrow H_8=H_4\otimes H_2\\
\text{one pure channel} & \mapsto & \text{one pure sheet-even channel}
\end{array}}
\]

while the ordinary cyclic DFT gives

\[
\boxed{
\mathrm{DFT}_{12}(\chi_{12})
=\sqrt{12}\,\chi_{12},
}
\]

and

\[
\boxed{
\mathrm{DFT}_{24}(\widetilde\chi_{12})
\text{ is supported on }2U(12)
\text{ with the same }(+,-,-,+)\text{ signs}.
}
\]

This is now an explicit finite transform-level intertwining structure, not only a visual analogy.

## 9. Next task

The next useful calculation is to place the divisor prime-selector increments from v13.225 into this factored `H_8` basis and determine how the post-`2,3` sieve crossings from v13.226 act on the sheet-even `chi_12` channel versus the sheet-odd channels.

Do not revise the audited principal v0.3.5 source from this checkpoint alone.