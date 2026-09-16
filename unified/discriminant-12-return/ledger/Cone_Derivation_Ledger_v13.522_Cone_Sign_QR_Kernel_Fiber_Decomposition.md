# Cone Derivation Ledger v13.522 — Cone Sign, QR Kernel, and Complete Fiber Decomposition

**Status:** exact finite algebra. This entry corrects a tempting but false statement: intrinsic cone sign does **not** exchange the two points within each QR fiber. The QR-kernel involution does. No Suzuki spectral consequence.

## 1. Carrier and notation

Let
\[
V=\mathbf F_2^2=\{00,10,01,11\}
\]
with labels
\[
00\leftrightarrow1,\quad10\leftrightarrow5,\quad01\leftrightarrow7,\quad11\leftrightarrow11.
\]
Set
\[
h:=11\in V.
\]
The signed carrier is
\[
G=V\times\mathbf F_2.
\]
Write a signed state as \((v,c)\).

The QR fold is
\[
\boxed{P(v,c)=v+ch.}
\]
The intrinsic cone-sign involution is
\[
\boxed{S(v,c)=(v,c+1).}
\]
The downstairs half-turn is
\[
\boxed{T_h(v)=v+h.}
\]
The QR-kernel involution is
\[
\boxed{K(v,c)=(v+h,c+1).}
\]
In \(\mathbf F_2^3\) coordinates,
\[
S=001,\qquad T_h=110,\qquad K=111.
\]
Thus
\[
\boxed{K=T_h^{\uparrow}S=S T_h^{\uparrow}},
\]
where \(T_h^{\uparrow}(v,c)=(v+h,c)\).

## 2. Complete fiber decomposition of P

For \(q\in V\), solve
\[
P(v,c)=q.
\]
If \(c=0\), then \(v=q\). If \(c=1\), then \(v=q+h\). Hence
\[
\boxed{P^{-1}(q)=\{(q,0),(q+h,1)\}.}
\]
Explicitly,
\[
\boxed{
\begin{aligned}
P^{-1}(1)&=\{(1,0),(11,1)\},\\
P^{-1}(5)&=\{(5,0),(7,1)\},\\
P^{-1}(7)&=\{(7,0),(5,1)\},\\
P^{-1}(11)&=\{(11,0),(1,1)\}.
\end{aligned}}
\]
In signed-residue notation these are
\[
\boxed{\{1,-11\},\quad\{5,-7\},\quad\{7,-5\},\quad\{11,-1\}.}
\]

## 3. K exchanges the two points inside every fiber

For every \((v,c)\),
\[
P(K(v,c))
=P(v+h,c+1)
=v+h+(c+1)h
=v+ch
=P(v,c).
\]
Therefore
\[
\boxed{P\circ K=P.}
\]
Since \(K\) has no fixed point on \(G\), each two-element fiber is exactly one K-orbit.

Pointwise:
\[
(1,0)\leftrightarrow(11,1),
\]
\[
(5,0)\leftrightarrow(7,1),
\]
\[
(7,0)\leftrightarrow(5,1),
\]
\[
(11,0)\leftrightarrow(1,1).
\]
Thus
\[
\boxed{G/\langle K\rangle\cong V,}
\]
with quotient map P.

## 4. S exchanges fibers, not points within a fiber

For intrinsic cone sign,
\[
P(S(v,c))=P(v,c+1)=v+(c+1)h=P(v,c)+h.
\]
Hence
\[
\boxed{P\circ S=T_h\circ P.}
\]
So
\[
\boxed{S:P^{-1}(q)\to P^{-1}(q+h).}
\]
Explicitly,
\[
P^{-1}(1)\leftrightarrow P^{-1}(11),
\]
\[
P^{-1}(5)\leftrightarrow P^{-1}(7).
\]
This corrects the false statement that S exchanges the two members of each P-fiber.

## 5. Full eight-state action table

\[
\begin{array}{c|c|c|c|c|c}
(v,c)&P(v,c)&S(v,c)&P(S(v,c))&K(v,c)&P(K(v,c))\\ \hline
(1,0)&1&(1,1)&11&(11,1)&1\\
(5,0)&5&(5,1)&7&(7,1)&5\\
(7,0)&7&(7,1)&5&(5,1)&7\\
(11,0)&11&(11,1)&1&(1,1)&11\\
(1,1)&11&(1,0)&1&(11,0)&11\\
(5,1)&7&(5,0)&5&(7,0)&7\\
(7,1)&5&(7,0)&7&(5,0)&5\\
(11,1)&1&(11,0)&11&(1,0)&1
\end{array}
\]
Every row verifies simultaneously
\[
\boxed{PS=T_hP,\qquad PK=P.}
\]

## 6. Two commuting diagrams

Cone sign descends to the 11 half-turn:
\[
\boxed{
\begin{array}{ccc}
G&\xrightarrow{S}&G\\
\downarrow P&&\downarrow P\\
V&\xrightarrow{T_h}&V.
\end{array}}
\]

The QR-kernel involution is vertical/fiberwise:
\[
\boxed{
\begin{array}{ccc}
G&\xrightarrow{K}&G\\
\downarrow P&&\downarrow P\\
V&\xrightarrow{\mathrm{id}}&V.
\end{array}}
\]

Thus the two involutions have sharply different quotient behavior:
\[
\boxed{
S=001:\text{ moves between fibers},
\qquad
K=111:\text{ moves within fibers}.
}
\]
Their difference is the positive-sheet element
\[
\boxed{K+S=110=h=11.}
\]

## 7. Character-level consequence

Let \(\chi\in V^\vee\). Pull it back along P:
\[
P^*\chi(v,c)=\chi(v+ch)=\chi(v)\chi(h)^c.
\]
Under cone sign,
\[
S^*P^*\chi(v,c)
=P^*\chi(v,c+1)
=\chi(h)P^*\chi(v,c).
\]
Therefore the pullback character is S-even iff
\[
\chi(h)=+1,
\]
and S-odd iff
\[
\chi(h)=-1.
\]
For \(h=11\),
\[
\chi_{-4}(11)=-1,\qquad
\chi_{-3}(11)=-1,\qquad
\chi_{12}(11)=+1.
\]
Hence
\[
\boxed{
S^*P^*(1)=P^*(1),\qquad
S^*P^*(\chi_{12})=P^*(\chi_{12}),
}
\]
while
\[
\boxed{
S^*P^*(\chi_{-4})=-P^*(\chi_{-4}),\qquad
S^*P^*(\chi_{-3})=-P^*(\chi_{-3}).
}
\]
Thus the previously established QR-surviving pair
\[
\{1,\chi_{12}\}
\]
is exactly the S-even part of the pulled-back quotient character space.

This gives a precise character-level form of the signed-cone statement: after the twisted fold P, intrinsic cone sign is diagonalized by the quotient characters, and its unique nonprincipal +1 eigendirection is \(\chi_{12}\).

## 8. A3/S4 realization

The element \(h=11\) acts on the tetrahedral vertices by
\[
\boxed{T_h=(1\ 11)(5\ 7).}
\]
In character coordinates \((\chi_{-4},\chi_{-3},\chi_{12})\),
\[
\boxed{D_{11}=\operatorname{diag}(-1,-1,+1).}
\]
Therefore the quotient image of intrinsic cone sign has
\[
\boxed{\mathbf R\chi_{12}}
\]
as its unique nonprincipal fixed axis.

The complete exact chain is now
\[
\boxed{
S\text{ (cone sign)}
\xrightarrow{\ P\ }
T_{11}
=(1\ 11)(5\ 7)
\xrightarrow{\text{character rep.}}
\operatorname{diag}(-1,-1,+1)
\xrightarrow{}
\chi_{12}\text{ fixed axis}.
}
\]
Meanwhile K is precisely the deck transformation of the two-to-one quotient P.

## 9. Guardrails

1. S and K must never be conflated: S is intrinsic cone sign; K is the QR-kernel/deck involution.
2. The identity \(K=S+110\) is in the additive \(\mathbf F_2^3\) carrier coordinates.
3. This exact finite mechanism explains the \(\chi_{12}\) fixed/surviving direction for the QR fold, but does not prove that Pell dynamics induces P.
4. The Pell identity \(\sigma_r(\lambda^n)=\lambda^{\chi_{12}(r)n}\) remains an independently established characterization of \(\chi_{12}\).
5. No Suzuki spectral/index consequence is asserted.