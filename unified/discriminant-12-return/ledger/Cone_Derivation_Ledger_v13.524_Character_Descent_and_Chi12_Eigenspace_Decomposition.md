# Cone Derivation Ledger v13.524 — Character Descent and the χ12 Eigenspace Decomposition

**Status:** exact finite Fourier/representation algebra, continuing the independently audited v13.522 fiber decomposition. No Pell-to-QR causation and no Suzuki spectral consequence are asserted.

## 1. Setup

Let
\[
V=\mathbf F_2^2,
\qquad h=11=(1,1),
\qquad G=V\times\mathbf F_2.
\]
Use
\[
P(v,c)=v+ch,
\qquad
S(v,c)=(v,c+1),
\qquad
K(v,c)=(v+h,c+1).
\]
Then
\[
PS=T_hP,
\qquad
PK=P.
\]
The K-orbits are exactly the two-point fibers of P.

## 2. Pullback of quotient characters

For \(\chi\in V^\vee\), define
\[
P^*\chi(v,c)=\chi(P(v,c))=\chi(v+ch).
\]
Since characters are multiplicative on the additive F2-vector space,
\[
\boxed{P^*\chi(v,c)=\chi(v)\chi(h)^c.}
\]
Because \(PK=P\),
\[
K^*P^*\chi=P^*\chi.
\]
Thus every pulled-back quotient character is K-even, exactly as required for a function descending to \(G/\langle K\rangle\).

## 3. Cone-sign action on pulled-back characters

Apply S:
\[
S^*P^*\chi(v,c)
=P^*\chi(v,c+1)
=\chi(v)\chi(h)^{c+1}.
\]
Hence
\[
\boxed{S^*P^*\chi=\chi(h)P^*\chi.}
\]
Therefore the quotient character basis diagonalizes intrinsic cone sign.

For the ordered V4 character basis
\[
\mathcal C=(1,\chi_{-4},\chi_{-3},\chi_{12}),
\]
the values at h=11 are
\[
1(11)=+1,
\qquad
\chi_{-4}(11)=-1,
\qquad
\chi_{-3}(11)=-1,
\qquad
\chi_{12}(11)=+1.
\]
So on the K-even quotient-character subspace,
\[
\boxed{[S^*]_{P^*\mathcal C}=\operatorname{diag}(1,-1,-1,1).}
\]
Equivalently,
\[
\boxed{
\mathcal H_{K+}
=
\underbrace{\operatorname{span}\{P^*1,P^*\chi_{12}\}}_{S=+1}
\oplus
\underbrace{\operatorname{span}\{P^*\chi_{-4},P^*\chi_{-3}\}}_{S=-1}.
}
\]

## 4. Full character table of the signed cube

Identify \(G^\vee\cong\mathbf F_2^3\). For \(\lambda=(p,q,s)\), write
\[
\psi_{pqs}(a,b,c)=(-1)^{pa+qb+sc}.
\]
The deck involution K is translation by 111, so
\[
K^*\psi_{pqs}=(-1)^{p+q+s}\psi_{pqs}.
\]
The cone-sign involution S is translation by 001, so
\[
S^*\psi_{pqs}=(-1)^s\psi_{pqs}.
\]
Thus every signed-cube character has a pair of exact parity eigenvalues
\[
\boxed{(\varepsilon_K,\varepsilon_S)=((-1)^{p+q+s},(-1)^s).}
\]

The four simultaneous sectors are therefore
\[
\boxed{
\begin{array}{c|c|c}
(\varepsilon_K,\varepsilon_S)&\text{condition}&\text{characters}\\ \hline
(+,+)&p+q+s=0,\ s=0&000,110\\
(+,-)&p+q+s=0,\ s=1&101,011\\
(-,+)&p+q+s=1,\ s=0&100,010\\
(-,-)&p+q+s=1,\ s=1&001,111
\end{array}}
\]
Each sector has dimension 2 in the function space on G.

## 5. Identification of the K-even plane

The K-even characters are precisely
\[
K^\perp=\{000,110,101,011\}.
\]
Using the established identifications,
\[
000=1,
\qquad
110=\chi_{12},
\]
\[
101=\sigma\chi_{-3},
\qquad
011=\sigma\chi_{-4},
\]
where
\[
\sigma=(-1)^c=\psi_{001}.
\]
Therefore
\[
\boxed{
K^\perp
=
\underbrace{\{1,\chi_{12}\}}_{S\text{-even}}
\sqcup
\underbrace{\{\sigma\chi_{-3},\sigma\chi_{-4}\}}_{S\text{-odd}}.
}
\]
This recovers the v13.515 quotient-dual plane and now resolves it internally by cone-sign parity.

## 6. Relation to the original mod-12 character plane

The original unsheared mod-12 character plane is
\[
P_0=\{000,100,010,110\}
=\{1,\chi_{-3},\chi_{-4},\chi_{12}\}.
\]
Its intersection with the quotient-dual plane is
\[
\boxed{P_0\cap K^\perp=\{000,110\}=\{1,\chi_{12}\}.}
\]
But the simultaneous parity calculation gives a sharper statement:
\[
\boxed{P_0\cap K^\perp=(K\text{-even})\cap(S\text{-even}).}
\]
Inside the nonprincipal three-space this becomes the one-dimensional line
\[
\boxed{\mathbf R\chi_{12}.}
\]

Thus the χ12 selection can be expressed without comparing the two planes geometrically: it is the unique nonprincipal original V4 character that is simultaneously invariant under the QR deck transformation and even under intrinsic cone sign after pullback through P.

## 7. Fourier projector factorization

Because S and K are commuting translations on the abelian cube G, their projectors commute:
\[
\Pi_K^\pm=\frac12(I\pm K^*),
\qquad
\Pi_S^\pm=\frac12(I\pm S^*).
\]
Hence
\[
\boxed{\Pi_K^{\varepsilon_K}\Pi_S^{\varepsilon_S}
=\Pi_S^{\varepsilon_S}\Pi_K^{\varepsilon_K}}
\]
projects onto the corresponding two-dimensional simultaneous sector.

In particular,
\[
\boxed{\Pi_K^+\Pi_S^+}
\]
has Fourier support exactly
\[
\boxed{\{1,\chi_{12}\}.}
\]
After removing the principal component,
\[
\boxed{(I-\Pi_{\mathbf1})\Pi_K^+\Pi_S^+}
\]
is the rank-one projector onto the χ12 line.

This is an exact projector formula for the distinguished character:
\[
\boxed{
\Pi_{\chi_{12}}
=(I-\Pi_{\mathbf1})\Pi_K^+\Pi_S^+
}
\]
when restricted to the original mod-12 character sector.

## 8. Downstairs tetrahedral interpretation

The identity
\[
PS=T_{11}P
\]
means that on quotient functions, cone sign is represented by the V4 element 11. In the standard tetrahedral character representation,
\[
D_{11}=\operatorname{diag}(-1,-1,+1)
\]
on
\[
W=\operatorname{span}\{\chi_{-4},\chi_{-3},\chi_{12}\}.
\]
Therefore
\[
\boxed{W^{T_{11}}=\mathbf R\chi_{12}.}
\]
This is the same rank-one nonprincipal subspace selected by the simultaneous projector above.

Hence the following descriptions are exactly equivalent within the finite carrier:
\[
\boxed{
\begin{aligned}
\mathbf R\chi_{12}
&=\text{nonprincipal }(K=+1,S=+1)\text{ Fourier sector}\\
&=\text{fixed line of }T_{11}\text{ on the tetrahedral standard representation}\\
&=\text{axis dual to the perfect matching }\{1,11\}\sqcup\{5,7\}.
\end{aligned}}
\]

## 9. Independent Pell characterization

Separately, the established discriminant-12 Galois/Pell law is
\[
\sigma_r(\lambda^n)=\lambda^{\chi_{12}(r)n}.
\]
Thus χ12 is also the Pell time-orientation character.

The finite-carrier work now supplies an internal mechanism selecting the same character, but this entry does **not** identify the Pell time involution with S, K, or P. The exact statement remains an independently compatible characterization.

## 10. Guardrails

1. S is cone sign; K is the QR deck involution. They commute but are not equal.
2. The rank-one χ12 projector is an exact statement in the finite Fourier/character carrier; it is not a Suzuki spectral projector.
3. The equality of the finite-carrier selected character with the Pell orientation character is exact at the character-label level, but no causal/dynamical map from Pell to the QR fold has been proved.
4. The prime-2 tangent-frame ambiguity from v13.497 remains unaffected.