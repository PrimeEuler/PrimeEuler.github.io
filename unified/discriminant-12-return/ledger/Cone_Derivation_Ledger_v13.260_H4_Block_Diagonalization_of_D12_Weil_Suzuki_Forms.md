# Cone Derivation Ledger v13.260 — H4 Block Diagonalization of D12 Weil-Suzuki Forms

Date: 2026-09-05
Status: EXACT NEW STRUCTURAL RESULT + OPERATOR-LEVEL PACKAGING — continuation of v13.258 and external audit v13.259; RH/GRH frontier remains open

## 0. Synchronization and audit reconciliation

Immediately before this write, the authoritative project README, current `master` tip, v13.258, and the newly-landed external audit v13.259 were re-fetched.

The current tip before this write was

`2c68fb3aefda2823ecb5ea56669ef9505038f1f0`

with `v13.259` as the highest ledger checkpoint.

External audit round 8 is CLOSED and found no mathematical error in v13.254-v13.258. In particular, it independently confirmed the D12 coefficient bridge and the screw-function additivity used below. Its scope note remains active: precise archimedean constants from Suzuki are source-established and were not independently checked symbol-for-symbol.

A current-source check also confirms that Masatoshi Suzuki's *Weil's quadratic form via the screw function*, arXiv:2606.09096, has a revised v2 dated 2026-08-17. The paper explicitly develops the passage from Weil's distributional quadratic form to continuous kernels built from the screw function. The present entry uses only the linearity of that kernel construction and the already-established D12 screw decomposition.

## 1. The H4 character table

Order the residue classes and quadratic characters as

\[
G=U(12)=\{1,5,7,11\},
\]

and

\[
\widehat G=
\{\chi_0,\chi_{-4},\chi_{-3},\chi_{12}\}.
\]

With the ordering above,

\[
H_4=
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix},
\qquad
H_4^2=4I.
\]

Define the normalized Walsh transform

\[
\boxed{U:=\frac12H_4.}
\]

Then

\[
\boxed{U^*=U=U^{-1}.}
\]

Thus `U` is an exact real unitary identification between residue-class coordinates and character coordinates.

## 2. Unit-shell prime-power ramps

For each unit residue `r in G`, define

\[
\boxed{
W_r(t)
:=
\sum_{\substack{n\le e^t\\ n\equiv r\ (12)}}
\frac{\Lambda(n)}{\sqrt n}
(t-\log n).
}
\]

Collect them into

\[
W(t)=
\begin{pmatrix}
W_1(t)\\W_5(t)\\W_7(t)\\W_{11}(t)
\end{pmatrix}.
\]

For the four characters modulo 12, define the corresponding imprimitive/unit-shell arithmetic ramps

\[
R_D^{(12)}(t)
:=
\sum_{r\in G}\chi_D(r)W_r(t).
\]

Then exactly

\[
\boxed{
R^{(12)}(t)=H_4W(t).
}
\]

This is the arithmetic H4 transform already implicit in v13.256, now promoted to the operator construction below.

## 3. The V4 group-circulant arithmetic kernel

Because every element of `G` has order two, `r^{-1}=r`.

Define the `4 x 4` matrix-valued arithmetic ramp

\[
\boxed{
\mathbb W(t)_{a,b}:=W_{ab^{-1}}(t),
\qquad a,b\in G.
}
\]

This is the group-circulant matrix for convolution on the finite group `G`.

The standard finite-group Fourier theorem gives

\[
\boxed{
U\,\mathbb W(t)\,U^*
=
\operatorname{diag}
\bigl(
R_0^{(12)}(t),
R_{-4}^{(12)}(t),
R_{-3}^{(12)}(t),
R_{12}^{(12)}(t)
\bigr).
}
\]

This is not merely a vector identity. It says:

\[
\boxed{
\text{H4 exactly diagonalizes the V4 arithmetic convolution operator.}
}
\]

The four scalar character ramps are its eigenchannels.

## 4. Primitive-channel local corrections are confined to 2 and 3

The H4 transform above uses characters modulo 12 and therefore deletes prime powers supported at `2` and `3`.

For the primitive analytic objects used in RH/GRH, write the correction ramps

\[
C_p^{\pm}(t)
:=
\sum_{\substack{k\ge1\\p^k\le e^t}}
\frac{(\pm1)^k\log p}{p^{k/2}}
(t-k\log p).
\]

Then the primitive arithmetic ramps satisfy

\[
\boxed{
R^{\rm prim}(t)
=
H_4W(t)+E(t),
}
\]

with

\[
\boxed{
E(t)=
\begin{pmatrix}
C_2^+(t)+C_3^+(t)\\
C_3^-(t)\\
C_2^-(t)\\
0
\end{pmatrix}.
}
\]

The entries correspond respectively to

\[
\zeta,\quad
L(s,\chi_{-4}),\quad
L(s,\chi_{-3}),\quad
L(s,\chi_{12}).
\]

Thus the exact failure of the bare U(12) shell to equal the four primitive channels is completely localized at the two nonunit primes:

\[
\boxed{
\text{primitive H4 defect} = \text{local Euler data at }2,3.
}
\]

In particular, the discriminant-12 channel itself has no correction:

\[
\boxed{E_{12}(t)=0.}
\]

That makes the D12 row the unique member of the H4 bank whose primitive arithmetic ramp is literally the unit-shell H4 transform with no finite-prime repair.

## 5. Full screw functions in character basis

Let

\[
\Phi_D(t):=-g_D(t)
\]

be the primitive completed screw function in each analytic channel, including its pole/conductor/gamma term.

Write

\[
\Phi_D(t)=A_D(t)-R_D^{\rm prim}(t),
\]

where `A_D` denotes the corresponding archimedean/pole contribution.

Collect

\[
\Phi_{\rm char}(t)=
\begin{pmatrix}
\Phi_0(t)\\
\Phi_{-4}(t)\\
\Phi_{-3}(t)\\
\Phi_{12}(t)
\end{pmatrix},
\qquad
A(t)=
\begin{pmatrix}
A_0(t)\\A_{-4}(t)\\A_{-3}(t)\\A_{12}(t)
\end{pmatrix}.
\]

Then

\[
\boxed{
\Phi_{\rm char}(t)
=
A(t)-H_4W(t)-E(t).
}
\]

The arithmetic bulk is therefore diagonalized by H4, while the conductor/parity information is carried by diagonal character-space archimedean terms and the explicit local defect `E`.

This separation is exact:

\[
\boxed{
\text{finite V4 bulk}
+
\text{local }\{2,3\}\text{ defect}
+
\text{archimedean completion}.
}
\]

## 6. Matrix-valued full screw function in residue coordinates

Define the diagonal character-space matrix

\[
\mathbb\Phi_{\rm char}(t)
:=
\operatorname{diag}
\bigl(
\Phi_0(t),
\Phi_{-4}(t),
\Phi_{-3}(t),
\Phi_{12}(t)
\bigr).
\]

Transfer it to residue coordinates by

\[
\boxed{
\mathbb\Phi_{\rm res}(t)
:=
U^*\mathbb\Phi_{\rm char}(t)U.
}
\]

Then automatically but nontrivially as an operator identity,

\[
\boxed{
U\mathbb\Phi_{\rm res}(t)U^*
=
\mathbb\Phi_{\rm char}(t).
}
\]

The residue-basis matrix has the exact decomposition

\[
\boxed{
\mathbb\Phi_{\rm res}
=
\mathbb A_{\rm res}
-
\mathbb W
-
\mathbb E_{\rm res},
}
\]

where

\[
\mathbb A_{\rm res}
:=U^*\operatorname{diag}(A_D)U,
\]

and

\[
\mathbb E_{\rm res}
:=U^*\operatorname{diag}(E_D)U.
\]

Thus the raw V4 group-circulant arithmetic operator appears literally as the non-archimedean bulk of the completed matrix screw function.

## 7. Continuous Suzuki kernel: pointwise H4 diagonalization

For any scalar screw function `g`, define Suzuki's continuous two-variable kernel

\[
\boxed{
G_g(t,u)
:=
g(t-u)-g(t)-g(-u)+g(0).
}
\]

The map

\[
g\longmapsto G_g
\]

is linear.

Therefore, for the four primitive channels define

\[
\mathbb G_{\rm char}(t,u)
:=
\operatorname{diag}
\bigl(
G_{g_0}(t,u),
G_{g_{-4}}(t,u),
G_{g_{-3}}(t,u),
G_{g_{12}}(t,u)
\bigr),
\]

and transfer to residue coordinates:

\[
\boxed{
\mathbb G_{\rm res}(t,u)
:=U^*\mathbb G_{\rm char}(t,u)U.
}
\]

Then for every pair `(t,u)`,

\[
\boxed{
U\mathbb G_{\rm res}(t,u)U^*
=
\mathbb G_{\rm char}(t,u).
}
\]

So H4 diagonalization survives the passage

\[
\boxed{
\text{prime-power coefficients}
\to
\text{screw functions}
\to
\text{continuous two-variable kernels}.
}
\]

This is the operator-level bridge sought after v13.258.

## 8. Direct-sum Weil/Suzuki quadratic form

Let `\mathcal H` denote a common test-function Hilbert space on which the four channel forms are defined, and let

\[
\mathcal H_{V4}=\mathcal H\otimes\mathbf C^4.
\]

For

\[
f=(f_1,f_5,f_7,f_{11})\in\mathcal H_{V4},
\]

write

\[
\widehat f:=Uf.
\]

Let `Q_D` denote the scalar Weil/Suzuki quadratic form in channel `D`.

Define the V4 packaged form by

\[
\boxed{
Q_{V4}[f]
:=
\sum_{D\in\{0,-4,-3,12\}}
Q_D[\widehat f_D].
}
\]

Equivalently, in residue coordinates it is the matrix-kernel form associated with `\mathbb G_res` (or with the corresponding differentiated Weil kernel, depending on the chosen Suzuki realization).

Since `U` is unitary,

\[
\boxed{
Q_{V4}\ge0
\iff
Q_D\ge0\text{ for every character channel }D.
}
\]

This is the exact block-diagonalization theorem:

\[
\boxed{
\text{H4 diagonalizes the four-channel Weil/Suzuki form into the four quadratic-character sectors.}
}
\]

This statement is linear-algebraic/operator-theoretic. It does not assert any of the four forms is positive.

## 9. GRH packaging — precise guardrail

Whenever the hypotheses of the relevant Weil/Suzuki positivity theorem are satisfied separately for the four primitive analytic objects, the direct-sum statement gives

\[
Q_{V4}\ge0
\iff
\bigl[
Q_0\ge0,
Q_{-4}\ge0,
Q_{-3}\ge0,
Q_{12}\ge0
\bigr].
\]

Consequently, under those already-source-established equivalences, positivity of the packaged V4 form is equivalent to the simultaneous RH/GRH statements for

\[
\boxed{
\zeta(s),
\quad
L(s,\chi_{-4}),
\quad
L(s,\chi_{-3}),
\quad
L(s,\chi_{12}).
}
\]

Guardrail:

\[
\boxed{
\text{This is a simultaneous packaging of known criteria, not a new proof of any GRH case.}
}
\]

The new content is that the project's exact H4/V4 shell is the internal Fourier transform that block-diagonalizes the corresponding four-channel arithmetic/continuous operator.

## 10. The discriminant-12 two-sector block

The field

\[
K=\mathbf Q(\sqrt3)
\]

uses exactly the principal and discriminant-12 sectors:

\[
\zeta_K=\zeta L(s,\chi_{12}).
\]

At screw and quadratic-form level,

\[
\boxed{
g_K=g_0+g_{12},}
\]

and

\[
\boxed{
Q_K[h]=Q_0[h]+Q_{12}[h].
}
\]

This is the scalar same-test-function sum emphasized in v13.258.

Now observe an exact H4 geometry.

Let `e_D` denote character-basis unit vectors and `e_r` residue-basis unit vectors. Because `U=H4/2` is symmetric,

\[
\boxed{
U(e_0+e_{12})=e_1+e_{11},
}
\]

while

\[
\boxed{
U(e_0-e_{12})=e_5+e_7.
}
\]

Thus the principal/quadratic pair has a direct residue-space meaning:

\[
\boxed{
\begin{aligned}
\text{principal}+\chi_{12}
&\longleftrightarrow
\{1,11\},\\
\text{principal}-\chi_{12}
&\longleftrightarrow
\{5,7\}.
\end{aligned}
}
\]

These are exactly the split and inert unit classes for `\mathbf Q(\sqrt3)`.

Therefore the H4 transform does not merely label the D12 analytic sector. It converts the two-character decomposition into the split/inert residue decomposition of the quadratic field.

This is the strongest structural statement in this entry:

\[
\boxed{
\text{D12 principal/quadratic operator block}
\stackrel{H4}{\longleftrightarrow}
\text{split/inert residue block}.
}
\]

## 11. Prime powers and why the split projection is exact

For unit residues modulo 12,

\[
r^2=1.
\]

Hence an inert prime `p\equiv5,7 (12)` satisfies

\[
p^{2k}\equiv1\pmod{12},
\qquad
p^{2k+1}\equiv p\pmod{12}.
\]

At the same time,

\[
1+\chi_{12}(p^k)
=
1+(-1)^k.
\]

Thus odd inert powers cancel from the Dedekind logarithmic derivative while even inert powers return to the `r=1` split residue class and contribute with weight two.

So the residue-side H4 projection and the quadratic-field Euler-factor behavior agree exactly at every prime power, not only at primes.

This corrects the potential temptation to interpret the split block as a prime-only projection.

## 12. Relation to Suzuki's 2026 Weil-kernel paper

Suzuki's current arXiv v2 of *Weil's quadratic form via the screw function* states that the screw-function integral operator with continuous kernel `g(x-y)` is directly related to Weil's quadratic form after differentiation of test functions, and develops the continuous-kernel realization without assuming RH.

The present result is compatible with that framework because every operation used here is linear in the screw kernel and the H4 transform acts only on the finite internal V4 coordinate.

Therefore the finite transform and the continuous operator commute:

\[
\boxed{
(H4\text{ on internal residue space})
\circ
(\text{Suzuki continuous-kernel construction})
=
(\text{Suzuki construction})
\circ
(H4\text{ on internal residue space}).
}
\]

That commuting-square statement is exact.

## 13. What is genuinely new here

The earlier entries established:

\[
a_{12}
\to
\Lambda(1+\chi_{12})
\to
\Phi_K,
\]

and

\[
\Phi_K=\Phi_\zeta+\Phi_{12}.
\]

The present entry upgrades the finite V4 structure itself to operator level:

\[
\boxed{
\begin{array}{ccc}
\text{residue prime-power channels}
&\xrightarrow{H4}&
\text{Dirichlet-character channels}\\
\downarrow&&\downarrow\\
\text{matrix screw kernel}
&\xrightarrow{H4}&
\text{diagonal scalar screw kernels}\\
\downarrow&&\downarrow\\
\text{matrix Weil form}
&\xrightarrow{H4}&
\text{direct sum of scalar Weil forms}.
\end{array}
}
\]

The D12 field occupies the `{0,12}` character block, which H4 identifies with the `{1,11}` versus `{5,7}` split/inert decomposition.

This gives the mod-12 shell a genuine functional-analytic role rather than merely a finite combinatorial analogy.

## 14. Guardrails

1. No RH or GRH statement is proved here.
2. The bare unit-shell H4 transform gives imprimitive mod-12 arithmetic channels; primitive channels require the explicit local corrections at 2 and 3 listed above.
3. The archimedean gamma/conductor terms differ between channels and must not be replaced by one universal scalar term.
4. Positivity of the Dedekind scalar sum `Q_K=Q_0+Q_12` alone does not imply positivity of either summand. Componentwise equivalence only holds for the lifted direct-sum V4 form where channel test functions may vary independently.
5. The new operator diagonalization is exact finite Fourier analysis on `U(12)` combined with the linearity of Suzuki's kernel construction; it is not evidence by itself that one channel controls another.
6. The exact Suzuki archimedean constants remain source-established pending the line-by-line source audit suggested by v13.259.

## 15. Next high-value target

The H4 block-diagonalization problem is now solved at the structural level.

The next useful step should not be another layer of finite bookkeeping. It should focus on the D12 two-sector block itself:

\[
\boxed{
Q_K=Q_0+Q_{12}.
}
\]

The most valuable question is whether the explicit D12 divisor/hyperbola coefficient structure permits a decomposition

\[
\boxed{
Q_K=Q_{\rm manifestly\ positive}+Q_{\rm controlled\ defect}
}
\]

or an analogous decomposition for `\Phi_K`, with the defect isolated in a term that can be tied to the split/inert V4 imbalance.

Equivalently, investigate whether the exact map

\[
a_{12}
\longrightarrow
(a_{12}\log)*a_{12}^{-1}
\longrightarrow
\mathbb G_{\{0,12\}}
\]

has a special positivity, complete-monotonicity, or operator-order property that is absent for a generic quadratic character.

That is now the shortest route from the project's own arithmetic geometry to Suzuki's Weil-positivity frontier.
