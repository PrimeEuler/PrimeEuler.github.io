# Cone Derivation Ledger v13.517 — Signed Cone–V4 Carrier and Corrected Commuting Diagram

**Status:** exact finite/geometric organization of previously established structures, with explicit correction of the conceptual hierarchy used in recent exploratory discussion. No new Suzuki spectral claim.

## 0. Correction

Recent discussion described the passage from the four positive labels \(r\in\{1,5,7,11\}\) to the eight signed labels \(\{\pm1,\pm5,\pm7,\pm11\}\) as though sign were merely an auxiliary algebraic extension added after the cone geometry.

That description is not faithful to the established cone picture represented in `figures/mod12_v4_cone_triple.png`.

The cone construction is already organized as a signed geometry. The finite signed carrier does not invent this sign structure; it algebraically records a sign pairing already present in the cone/factor geometry.

Accordingly the corrected conceptual hierarchy is
\[
\boxed{
\text{signed cone geometry}
\longrightarrow
\text{signed finite carrier}
\longrightarrow
\text{Fourier/character coordinates}
\longrightarrow
A_3/S_4.
}
\]

The precise algebraic statements below distinguish what is exact from what remains only a compatibility.

---

## 1. Split cone / factor-line coordinates

For a factor ratio/state parameter \(r\), use
\[
X=\frac{r-1}{2},\qquad T=\frac{r+1}{2}.
\]
Then
\[
T-X=1,\qquad T+X=r,
\]
and therefore
\[
\boxed{T^2-X^2=r.}
\]

This is the split quadratic-form relation underlying the cone/factor-line view.

Under sign reversal
\[
r\mapsto-r,
\]
one obtains
\[
X(-r)=\frac{-r-1}{2}=-T(r),
\]
\[
T(-r)=\frac{-r+1}{2}=-X(r).
\]
Hence
\[
\boxed{r\mapsto-r\quad\Longleftrightarrow\quad(X,T)\mapsto(-T,-X).}
\]
The split form changes sign:
\[
T'^2-X'^2=-r.
\]

Thus sign reversal is represented intrinsically in the same \((X,T)\) geometry by the coordinate involution
\[
S(X,T)=(-T,-X),\qquad S^2=1.
\]

This is the algebraic content of the signed cone pairing used in the mod-12 V4 cone figure.

---

## 2. Positive V4 carrier

The four distinguished mod-12 states are
\[
U(12)=\{1,5,7,11\}\cong V_4.
\]
Write
\[
r=5^a7^b\pmod{12},\qquad(a,b)\in\mathbf F_2^2.
\]
Then
\[
1\leftrightarrow00,\quad
5\leftrightarrow10,\quad
7\leftrightarrow01,\quad
11\leftrightarrow11.
\]

Their factor-line coordinates are
\[
\boxed{
\begin{array}{c|c|c}
r&X=(r-1)/2&T=(r+1)/2\\ \hline
1&0&1\\
5&2&3\\
7&3&4\\
11&5&6
\end{array}}
\]
with \(T^2-X^2=r\) in every row.

---

## 3. Signed carrier

Adjoin the intrinsic cone sign bit \(c\in\mathbf F_2\):
\[
r(a,b,c)=5^a7^b(-1)^c\pmod{24}.
\]
Then the eight signed states form
\[
\boxed{G\cong U(24)\cong\mathbf F_2^3\cong V_4\times C_2.}
\]

The sign involution is addition of
\[
e_s=(0,0,1),
\]
so
\[
(a,b,c)\mapsto(a,b,c+1)
\]
corresponds to
\[
r\mapsto-r
\]
and geometrically to
\[
\boxed{(X,T)\mapsto(-T,-X).}
\]

Thus the \(C_2\) sign coordinate in the finite carrier is the direct algebraic encoding of the signed cone involution.

---

## 4. Important distinction: sign direction versus QR-kernel direction

The exact QR quotient of v13.515 uses
\[
P(a,b,c)=(a+c,b+c).
\]
Its kernel is
\[
K=\langle111\rangle.
\]

This must not be confused with the intrinsic sign direction
\[
\langle001\rangle.
\]

Therefore the signed cone involution and the QR reduction kernel are two different involutions in the same signed cube:
\[
\boxed{
\text{cone sign}=001,\qquad
\text{QR kernel}=111.
}
\]

This distinction is binding.

---

## 5. Fourier dual of the positive V4 carrier

The three nonprincipal quadratic characters are
\[
\chi_{-3},\qquad\chi_{-4},\qquad\chi_{12}=\chi_{-3}\chi_{-4}.
\]
The Hadamard transform identifies the regular V4 state basis with the character basis
\[
\{1,\chi_{-4},\chi_{-3},\chi_{12}\}.
\]

Define the raw character vector
\[
\boxed{v_r=(\chi_{-4}(r),\chi_{-3}(r),\chi_{12}(r)).}
\]
Explicitly,
\[
v_1=(1,1,1),
\]
\[
v_5=(1,-1,-1),
\]
\[
v_7=(-1,1,-1),
\]
\[
v_{11}=(-1,-1,1).
\]
These are the vertices of a regular tetrahedron centered at the origin.

Thus the tetrahedron is not a later unrelated decoration: it is the three-dimensional nonprincipal Fourier/character realization of the original four-state V4 carrier.

---

## 6. Minuscule normalization and A3

Set
\[
\mu_r=\frac12v_r.
\]
Then
\[
\{\mu_r\}=W(A_3)\cdot\omega_1
\]
is the four-weight minuscule orbit of type A3.

Differences are roots:
\[
\boxed{\alpha_{r,s}=\mu_r-\mu_s\in\Phi(A_3).}
\]
The twelve oriented tetrahedral edges give all twelve roots.

Root reflection in \(\alpha_{r,s}\) acts on the tetrahedron as the transposition
\[
(r\ s).
\]
Hence
\[
\boxed{W(A_3)\cong S_4.}
\]

Therefore the exact chain is
\[
\boxed{
V_4\text{ state carrier}
\xrightarrow{\text{Fourier characters}}
\text{tetrahedron}
\xrightarrow{\times1/2}
\text{minuscule }A_3\text{ weights}
\xrightarrow{\text{differences}}
\Phi(A_3).
}
\]

---

## 7. Three perfect matchings = three character axes

The six unoriented tetrahedral edges split into the three perfect matchings
\[
\chi_{-4}:\quad\{1,5\}\sqcup\{7,11\},
\]
\[
\chi_{-3}:\quad\{1,7\}\sqcup\{5,11\},
\]
\[
\boxed{\chi_{12}:\quad\{1,11\}\sqcup\{5,7\}.}
\]

For each character axis, the corresponding two root pairs are exactly those with zero coordinate along that axis.

So the three nonprincipal Fourier directions of V4 are geometrically visible as the three opposite-edge pairings of the tetrahedron.

---

## 8. Signed H8 carrier and QR quotient

For
\[
G=\mathbf F_2^3,
\]
the full signed Fourier transform is the \(H_8\) character table.

The QR quotient of v13.515 is
\[
P:G\to\mathbf F_2^2,
\qquad
P(a,b,c)=(a+c,b+c),
\]
with
\[
K=\ker P=\langle111\rangle.
\]
Its Fourier-dual surviving plane is
\[
K^\perp=\{000,110,101,011\}.
\]

The original mod-12 character plane is
\[
P_0=\{1,\chi_{-3},\chi_{-4},\chi_{12}\}.
\]
The exact intersection is
\[
\boxed{P_0\cap K^\perp=\{1,\chi_{12}\}.}
\]
Thus \(\chi_{12}\) is the unique nonprincipal original V4 character unchanged by the QR quotient.

---

## 9. Pell compatibility

Independently, for the discriminant-12 Pell unit
\[
\lambda=2+\sqrt3,
\]
the Galois action is
\[
\boxed{\sigma_r(\lambda^n)=\lambda^{\chi_{12}(r)n}.}
\]
Therefore \(\chi_{12}\) is the Pell time-orientation character.

Combining exact but independently derived statements:
\[
\boxed{
\chi_{12}
=\text{Pell time-orientation character}
=\text{unique unchanged nonprincipal QR/Fourier character}.
}
\]
Within the tetrahedral Fourier realization of V4, this same axis corresponds to
\[
\boxed{\{1,11\}\sqcup\{5,7\}.}
\]

No claim is made here that Pell dynamics induces the QR quotient.

---

## 10. Corrected commuting finite-carrier diagram

The exact structural organization can be displayed as

\[
\boxed{
\begin{array}{ccccc}
&&G=U(24)\cong V_4\times C_2&&\\
&\nearrow&&\searrow P&\\
\text{signed cone/factor geometry}&&&&G/K\cong V_4\\
&\searrow&&\nearrow\text{pullback}&\\
&&U(12)\cong V_4&&
\end{array}}
\]

with the qualifications:

- the left diagonal records the intrinsic cone sign involution \(001\);
- the quotient arrow \(P\) kills the distinct direction \(111\);
- the lower V4 is the positive mod-12 carrier;
- the right V4 is the QR quotient carrier and is not identified with the lower V4 by ordinary QR multiplication.

Fourier duality then gives
\[
\boxed{
\begin{array}{ccc}
V_4\text{ states}&\xrightarrow{H_4}&V_4^\vee\text{ characters}\\
&&\downarrow\text{ nonprincipal part}\\
&&\mathbb R^3\ni v_r\\
&&\downarrow\times1/2\\
&&\mu_r\text{ minuscule tetrahedron}\\
&&\downarrow\text{ differences}\\
&&\Phi(A_3),\quad W(A_3)\cong S_4.
\end{array}}
\]

For the signed carrier, v13.515 gives the exact normalized intertwining
\[
\mathcal F_8\mathcal P=R\mathcal F_4,
\qquad
\mathcal F_8R=\mathcal P\mathcal F_4,
\]
so quotienting the signed state carrier and restricting to its annihilator are Fourier-dual operations.

---

## 11. What is now unified

The following are not merely analogous; they are linked by explicit maps:

1. signed cone/factor involution \(r\mapsto-r\), \((X,T)\mapsto(-T,-X)\);
2. signed finite carrier \(U(24)\cong V_4\times C_2\);
3. positive mod-12 carrier \(U(12)\cong V_4\);
4. H4 character decomposition of that V4;
5. character-sign tetrahedron \(v_r\);
6. minuscule A3 weight tetrahedron \(\mu_r=v_r/2\);
7. A3 roots as oriented edge differences;
8. S4 as the Weyl/permutation group of the tetrahedron;
9. three quadratic characters as the three perfect matchings;
10. \(\chi_{12}\) as both Pell time orientation and the unique unchanged nonprincipal character of the independently defined QR quotient.

This is the corrected common finite-carrier picture.

---

## 12. Guardrails

1. The signed cone geometry is prior to, not created by, the U(24) encoding.
2. The intrinsic cone sign direction \(001\) is not the QR-kernel direction \(111\).
3. Negative signed states are part of the signed split cone/factor geometry; statements requiring the positive real AM-GM sheet must still impose the appropriate positivity condition.
4. The prime-2 tangent pointwise identification audited in v13.497 remains a chosen-coordinate issue and is not repaired merely by this signed-carrier diagram.
5. No Pell-to-QR dynamical map is asserted.
6. No Suzuki spectral/index consequence is asserted.
7. No moonshine/Monster connection is asserted.