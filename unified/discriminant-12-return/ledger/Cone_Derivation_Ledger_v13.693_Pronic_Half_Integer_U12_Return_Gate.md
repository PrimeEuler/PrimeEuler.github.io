# Cone Derivation Ledger v13.693 — Pronic Half-Integer Completion and the U(12) Return Gate

Date: 2026-09-23

Status labels: **[S]** source-established, **[D]** exact derived, **[I]** interpretation, **[N]** limitation.

## 1. Synchronization

Immediately before this write the live head was v13.692, commit \`866761d2e700f77adc259e536c00c6319548c00d\`. Repository search found no prior checkpoint containing the exact pronic-to-\(U(12)\) characterization below.

This continues v13.692 and tests the project-owner observation that the pronics \(6\) and \(12\) share the same \(+1/4\) half-integer completion.

## 2. Universal pronic half-integer completion [D]

Let
\[
P_m=m(m+1).
\]
Then
\[
\boxed{
P_m+\frac14=\left(m+\frac12\right)^2
}
\]
and therefore
\[
\boxed{
\sqrt{P_m+\frac14}=m+\frac12.
}
\]
Equivalently,
\[
\boxed{
4P_m+1=(2m+1)^2.
}
\]

Thus every pronic has an exact half-integer completed radius, and its doubled radius is the odd integer
\[
r_m:=2m+1.
\]

## 3. The consecutive pronics 6 and 12 produce the central D12 labels 5 and 7 [D]

The two consecutive pronics
\[
P_2=2\cdot3=6,\qquad
P_3=3\cdot4=12
\]
satisfy
\[
6+\frac14=\frac{25}{4}=\left(\frac52\right)^2,
\]
\[
12+\frac14=\frac{49}{4}=\left(\frac72\right)^2.
\]
Hence
\[
\boxed{
\sqrt{6+\frac14}=\frac52,\qquad
\sqrt{12+\frac14}=\frac72.
}
\]

But v13.692 established that the emphasized D12 shells \(K=5,7\) have cone coordinates
\[
T=\frac K2=\frac52,\frac72.
\]
Therefore the two central unit-shell coordinates are exactly the completed half-integer radii of the consecutive pronics \(6\) and \(12\):
\[
\boxed{
P_2=6\longmapsto T=\frac52\longmapsto K=5,
}
\]
\[
\boxed{
P_3=12\longmapsto T=\frac72\longmapsto K=7.
}
\]

Their midpoint is
\[
\frac12\left(\frac52+\frac72\right)=3,
\]
i.e. the \(K=6\) center. Thus the visible \(5,6,7\) shell triple is exactly
\[
\boxed{
2\sqrt{P_2+\frac14},\quad
2\cdot3,\quad
2\sqrt{P_3+\frac14}
=
5,6,7.
}
\]

## 4. Exact characterization of U(12) by pronic completion [D]

The preceding example extends periodically.

For
\[
r_m=2m+1,
\]
we have
\[
r_m^2-1=4m(m+1)=4P_m.
\]

Now
\[
r_m\in U(12)
\]
iff \(r_m\) is odd and not divisible by \(3\). Oddness is automatic. Also
\[
2m+1\equiv0\pmod3
\iff
m\equiv1\pmod3.
\]
On the other hand, because \(P_m=m(m+1)\) is always even,
\[
6\mid P_m
\iff
3\mid m(m+1)
\iff
m\not\equiv1\pmod3.
\]
Therefore
\[
\boxed{
r_m=2m+1\in U(12)
\iff
6\mid P_m.
}
\]

Modulo \(6\), the admissible indices are
\[
m\equiv0,2,3,5\pmod6,
\]
and their completed odd radii are
\[
2m+1\equiv1,5,7,11\pmod{12}.
\]
Hence
\[
\boxed{
\{\,2m+1\bmod12:6\mid m(m+1)\,\}
=
U(12)=\{1,5,7,11\}.
}
\]

This is an exact pronic realization of the entire four-state D12 unit carrier.

## 5. Equivalent discriminant / mod-24 formulation [D]

Since
\[
4P_m+1=r_m^2,
\]
the pronic quadratic
\[
z^2-z-P_m=0
\]
has discriminant
\[
\boxed{\Delta_m=1+4P_m=r_m^2.}
\]

If \(6\mid P_m\), then
\[
4P_m\equiv0\pmod{24},
\]
so
\[
\boxed{r_m^2\equiv1\pmod{24}.}
\]

Conversely, for odd \(r\),
\[
r^2\equiv1\pmod{24}
\]
implies
\[
P=\frac{r^2-1}{4}
\]
is divisible by \(6\), and \(P=((r-1)/2)((r+1)/2)\) is pronic.

Thus:
\[
\boxed{
6\mid P_m
\iff
(2m+1)^2\equiv1\pmod{24}.
}
\]

Reduction of these odd square roots modulo \(12\) gives exactly \(U(12)\).

[N] There are eight roots of \(r^2\equiv1\pmod{24}\); reduction mod \(12\) identifies opposite lifts and leaves the four \(U(12)\) classes. The statement is therefore a carrier realization, not a claim that \(U(12)\) itself has eight elements.

## 6. The central 35–36–37 RMS cell [D]

For the centered half-cell
\[
A=3,\qquad D=\frac12,
\]
the geometric and RMS squares are
\[
G^2=A^2-D^2=\frac{35}{4},
\qquad
Q^2=A^2+D^2=\frac{37}{4}.
\]
Therefore
\[
\boxed{
(2G)^2=35,\qquad
(2A)^2=36,\qquad
(2Q)^2=37.
}
\]

Modulo \(12\),
\[
35\equiv11,\qquad36\equiv0,\qquad37\equiv1.
\]
Thus the RMS completion produces the symmetric residue pair
\[
\boxed{\{11,1\}=L_{\chi_{12},+}}
\]
from v13.678, while the adjacent completed-pronic shell pair is
\[
\boxed{\{5,7\}=L_{\chi_{12},-}}.
\]

So the centered construction now realizes both fibers of the \(\chi_{12}\) quotient:
\[
\boxed{
\{5,7\}\xrightarrow{\chi_{12}}-1,
\qquad
\{11,1\}\xrightarrow{\chi_{12}}+1.
}
\]

This is stronger than the v13.692 centered-pair result: the RMS side supplies the complementary \(\chi_{12}\) fiber.

## 7. Relation to the D12 return mechanism [D/I]

[S] The established D12 return thread already identifies:

- \(U(12)=\{1,5,7,11\}\) as the four-state unit/Galois carrier;
- \(\chi_{12}\) as the Pell time-orientation character;
- \(R_{12}=\log(2+\sqrt3)\) as the primitive Pell/Cone rapidity step;
- the \(\chi_{12}\) shell-displacement channel with the ideal-counting Dirichlet series \(\zeta(s)L(s,\chi_{12})\).

[D] The pronic completion now supplies an exact independent realization of the same finite carrier:
\[
\boxed{
P_m\ \text{pronic},\quad 6\mid P_m
\quad\Longleftrightarrow\quad
2\sqrt{P_m+\frac14}\bmod12\in U(12).
}
\]

[D] In the central cell,
\[
P_2=6,\quad P_3=12
\]
map specifically to the \(\chi_{12}=-1\) pair \(\{5,7\}\), while the RMS-centered squares map to the complementary \(\chi_{12}=+1\) pair \(\{11,1\}\).

[I] This is sufficient to say that the half-integer/pronic completion is part of the **finite D12 return carrier mechanism**: it constructs the same \(U(12)\) carrier and, in the central RMS cell, geometrically separates the two \(\chi_{12}\) fibers.

[N] It does not by itself derive the Pell regulator \(2+\sqrt3\), the analytic continuation of \(L(s,\chi_{12})\), or the full return dynamics. Those remain additional structures on the carrier.

## 8. Interaction with the mod-1/2 divisor and Casimir threads [D]

The same half-coordinate now has four exact roles:
\[
\boxed{
\begin{array}{rcl}
P_m+\frac14&=&(m+\frac12)^2
\quad\text{(pronic/Casimir completion)},\\[1mm]
\Delta X,\Delta T&=&\pm\frac12
\quad\text{(null-diamond/transition cell)},\\[1mm]
2((-X_k)\bmod\frac12)&=&\{n/k\}
\quad\text{(divisor discretization)},\\[1mm]
2\sqrt{P_m+\frac14}\bmod12&\in&U(12)
\quad\text{when }6\mid P_m
\quad\text{(D12 carrier)}.
\end{array}}
\]

The common object is therefore not merely the number \(1/2\), but the intrinsic half-lattice of the factor-cone coordinates.

## 9. Gate result

\[
\boxed{\textbf{PASS: }6\textbf{ and }12\textbf{ are consecutive pronics whose }+\frac14\textbf{ completions are exactly }(5/2)^2,(7/2)^2.}
\]

\[
\boxed{\textbf{PASS: pronics divisible by }6\textbf{ produce exactly }U(12)\textbf{ under doubled half-integer completion mod }12.}
\]

\[
\boxed{\textbf{PASS: the centered RMS cell supplies the complementary }\chi_{12}\textbf{ fiber }\{1,11\}.}
\]

\[
\boxed{\textbf{SCOPE: this establishes the finite carrier/character part of the D12 return mechanism, not yet the Pell regulator or analytic }L\textbf{-function dynamics.}}
\]

## 10. Next exact tests

1. Determine whether the pronic index shift \(m\mapsto m+1\), transported through \(r=2m+1\), has a canonical action on the \(U(12)\) / AG(2,2) carrier after the ramified classes \(3,9\) are removed.
2. Compare the mod-\(24\) square-root lift \(r^2\equiv1\pmod{24}\) with the project's established \(U(24)\) character-dual / \(C_2^3\) intertwiner, rather than treating the appearance of \(24\) as accidental.
3. Test whether the RMS pair \(35,37\) has an exact interpretation in the existing Pell/cyclotomic return matrices beyond its proven \(\chi_{12}\) fiber placement.
