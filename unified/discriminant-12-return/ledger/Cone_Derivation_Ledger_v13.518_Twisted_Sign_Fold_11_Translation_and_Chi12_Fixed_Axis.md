# Cone Derivation Ledger v13.518 — Twisted Sign Fold, 11-Translation, and the χ12 Fixed Axis

**Status:** exact finite algebra derived from the signed cone carrier of v13.517 and the QR quotient of v13.515. This entry explains structurally why χ12 is the unique nonprincipal original V4 character surviving the QR fold. No Suzuki spectral claim.

## 1. Two involution directions in the signed cube

Use
\[
G=\mathbf F_2^3,
\qquad
(a,b,c)\longleftrightarrow 5^a7^b(-1)^c\pmod{24}.
\]
The intrinsic cone sign direction is
\[
s=001,
\]
while the QR-kernel direction is
\[
k=111.
\]
Their difference/product in the elementary abelian group is
\[
\boxed{s+k=110.}
\]
But
\[
110\longleftrightarrow5\cdot7=35\equiv11\pmod{24}.
\]
Therefore
\[
\boxed{k=s+h,\qquad h=110\leftrightarrow11.}
\]

So the QR-kernel involution is not unrelated to cone sign. It is exactly cone sign composed with translation by the positive V4 element 11.

---

## 2. QR quotient as a twisted sign fold

Write a signed state as
\[
(v,c),\qquad v=(a,b)\in\mathbf F_2^2,
\]
and let
\[
h=(1,1)\leftrightarrow11.
\]
The QR quotient map is
\[
P(v,c)=v+ch.
\]
Indeed,
\[
P(a,b,c)=(a+c,b+c).
\]
Hence
\[
P(v,0)=v,
\]
while
\[
\boxed{P(v,1)=v+h.}
\]
Thus the positive sheet is identified directly with the quotient V4, whereas the negative sheet is first translated by 11 and then folded onto it.

Equivalently the kernel relation is
\[
(v,c)\sim(v+h,c+1).
\]
Therefore the exact QR fold is
\[
\boxed{(v,+)\sim(v+h,-),\qquad h=11.}
\]
This is a **twisted sign fold**: sign reversal alone is not killed; sign reversal followed by the V4 half-turn 11 is killed.

In residue labels the four fibers are exactly
\[
\boxed{
\{1,-11\},\quad
\{5,-7\},\quad
\{7,-5\},\quad
\{11,-1\}.
}
\]

---

## 3. Why χ12 survives: direct character proof

Consider an original mod-12 character \(\chi\) pulled back to the signed cube without a sheet twist, so it depends only on \(v\).

Such a character descends through the twisted fold iff it is constant on each kernel fiber:
\[
\chi(v)=\chi(v+h).
\]
Since \(\chi(v+h)=\chi(v)\chi(h)\), this is equivalent to
\[
\boxed{\chi(h)=1.}
\]
For \(h=11\),
\[
\chi_{-4}(11)=-1,
\qquad
\chi_{-3}(11)=-1,
\qquad
\boxed{\chi_{12}(11)=+1.}
\]
Therefore among the three nonprincipal original V4 characters, exactly one is invariant under the 11-translation:
\[
\boxed{\chi_{12}.}
\]
Including the principal character,
\[
\boxed{\{\chi\in V_4^\vee:\chi(11)=1\}=\{1,\chi_{12}\}.}
\]
This gives a direct two-dimensional V4 explanation of the v13.515 Fourier result
\[
P_0\cap K^\perp=\{1,\chi_{12}\}.
\]

Thus χ12 survival is not merely an observed intersection of two H4 planes: it is forced by the fact that the QR fold differs from intrinsic cone sign by the positive V4 element 11.

---

## 4. Fourier action of the 11-translation

In the nonprincipal character basis
\[
(\chi_{-4},\chi_{-3},\chi_{12}),
\]
translation by \(r\in V_4\) acts diagonally by
\[
D_r=\operatorname{diag}(\chi_{-4}(r),\chi_{-3}(r),\chi_{12}(r)).
\]
For \(r=11\),
\[
\boxed{D_{11}=\operatorname{diag}(-1,-1,+1).}
\]
Hence the 11-translation is a 180-degree rotation in the character tetrahedron around the χ12 axis.

Its fixed subspace in the nonprincipal 3-space is exactly
\[
\boxed{\operatorname{Fix}(D_{11})=\mathbf R\,\chi_{12}.}
\]
This is the geometric reason the QR twisted fold singles out the χ12 character axis.

---

## 5. Action on tetrahedral vertices

Translation by 11 in V4 permutes the four labels as
\[
1\leftrightarrow11,
\qquad
5\leftrightarrow7.
\]
Thus as an S4 permutation it is
\[
\boxed{(1\ 11)(5\ 7),}
\]
a double transposition.

This is precisely the χ12 perfect matching found in v13.513:
\[
\boxed{\{1,11\}\sqcup\{5,7\}.}
\]

Therefore three previously separate descriptions are exactly the same object:
\[
\boxed{
11\in V_4
\quad\longleftrightarrow\quad
(1\ 11)(5\ 7)\in S_4
\quad\longleftrightarrow\quad
D_{11}=\operatorname{diag}(-1,-1,1)
\quad\longleftrightarrow\quad
\chi_{12}\text{ fixed axis}.
}
\]

---

## 6. Root geometry of the fixed axis

The χ12-perfect matching consists of the opposite tetrahedral edges
\[
1-11,
\qquad
5-7.
\]
Their roots are
\[
\alpha_{1,11}=(1,1,0),
\qquad
\alpha_{5,7}=(1,-1,0).
\]
Both satisfy
\[
\alpha\cdot e_{12}=0,
\qquad e_{12}=(0,0,1).
\]
Hence these two opposite edge directions span the plane perpendicular to the χ12 axis, while the double transposition rotates that plane by π and fixes the χ12 axis.

Explicitly,
\[
D_{11}(x,y,z)=(-x,-y,z).
\]
So the tetrahedral matching selected by the twisted sign fold is exactly the pair of opposite edges lying in the χ12-perpendicular root plane.

---

## 7. The three V4 elements and the three axes

The same statement holds cyclically for all three nonidentity V4 translations:
\[
\boxed{
\begin{array}{c|c|c|c}
r&D_r&\text{fixed character axis}&\text{double transposition}\\ \hline
5&\operatorname{diag}(+1,-1,-1)&\chi_{-4}&(1\ 5)(7\ 11)\\
7&\operatorname{diag}(-1,+1,-1)&\chi_{-3}&(1\ 7)(5\ 11)\\
11&\operatorname{diag}(-1,-1,+1)&\chi_{12}&(1\ 11)(5\ 7)
\end{array}}
\]
Thus the three nonidentity elements of the original V4, the three double transpositions in the normal Klein four of S4, the three perfect matchings of the tetrahedron, and the three nonprincipal character axes are canonically paired by Fourier duality.

The QR construction specifically chooses the third row because
\[
\boxed{k=s+11.}
\]

---

## 8. A sharper commuting diagram

Let \(S\) denote intrinsic cone sign and \(T_{11}\) translation by the positive V4 element 11. Then the QR-kernel involution is
\[
\boxed{K=S\,T_{11}=T_{11}S}
\]
because the signed carrier is abelian.

Hence the quotient may be depicted as
\[
\boxed{
\begin{array}{ccc}
(v,+)&\xrightarrow{S}&(v,-)\\
\downarrow P&&\downarrow P\\
v&\xrightarrow{T_{11}}&v+11
\end{array}}
}
\]
which commutes:
\[
P\circ S=T_{11}\circ P.
\]
Indeed,
\[
P(v,c+1)=v+(c+1)h=P(v,c)+h.
\]
Thus intrinsic cone sign descends under the QR fold not to the identity, but to the positive-sheet V4 translation by 11.

This is stronger and more precise than merely saying that the signed cone and QR quotient use the same eight-state carrier.

---

## 9. Fourier-dual commuting diagram

Under H4 Fourier duality, state translation \(T_{11}\) becomes multiplication by the diagonal character matrix
\[
D_{11}=\operatorname{diag}(1,-1,-1,+1)
\]
on the full character basis
\[
(1,\chi_{-4},\chi_{-3},\chi_{12}).
\]
Therefore
\[
\boxed{
\operatorname{Fix}(D_{11})
=\operatorname{span}\{1,\chi_{12}\}.
}
\]
This is exactly the original-character subspace that descends unchanged through the QR quotient.

So the v13.515 annihilator calculation and the v13.513 tetrahedral axis calculation are now linked by the explicit identity
\[
\boxed{111=001+110.}
\]
In words:
\[
\boxed{
\text{QR kernel}
=
\text{cone sign}
+
\text{11-translation},
}
\]
and Fourier duality converts the 11-translation into the χ12 fixed axis.

---

## 10. Pell comparison

Independently,
\[
\sigma_r(\lambda^n)=\lambda^{\chi_{12}(r)n}.
\]
Therefore the same χ12 axis now has three exact descriptions:

1. Pell time-orientation character;
2. fixed nonprincipal Fourier axis of the 11-translation;
3. unique nonprincipal original V4 character descending unchanged through the QR twisted sign fold.

Equivalently,
\[
\boxed{
\chi_{12}
\leftrightarrow
11\in V_4
\leftrightarrow
(1\ 11)(5\ 7)
\leftrightarrow
\{1,11\}\sqcup\{5,7\}.
}
\]

This is an exact common finite-carrier statement. It still does not assert that Pell dynamics generates the QR quotient.

---

## 11. Main conclusion

The signed-cone correction of v13.517 exposes an additional exact structure that was hidden when the sign bit was treated as auxiliary:

\[
\boxed{
\text{intrinsic cone sign }001
\quad\text{and}\quad
\text{QR kernel }111
\quad\text{differ by}\quad
110\leftrightarrow11\in V_4.
}
\]

That difference element is exactly the V4 half-turn whose tetrahedral action is the χ12 double transposition and whose Fourier fixed axis is χ12.

Therefore the χ12 survival found in v13.515 is structurally explained inside the signed cone–V4 carrier itself.

---

## 12. Guardrails

1. The identity \(111=001+110\) and all consequences above are exact finite algebra.
2. The commuting relation \(P\circ S=T_{11}\circ P\) is exact.
3. The χ12 fixed-axis statement is exact Fourier/tetrahedral geometry.
4. This does not identify the QR-kernel involution with cone sign; they remain distinct and differ by 11.
5. No Pell-to-QR dynamical derivation is asserted.
6. No prime-2 tangent-frame ambiguity from v13.497 is resolved by this result.
7. No Suzuki spectral/index consequence or RH/GRH statement is asserted.