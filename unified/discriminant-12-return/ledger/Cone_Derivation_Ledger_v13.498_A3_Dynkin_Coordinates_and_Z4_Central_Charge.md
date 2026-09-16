# Cone Derivation Ledger v13.498 — A3 Dynkin Coordinates and the Z/4 Central Charge

## Scope

Continue the exact A3 lattice branch after v13.495 by translating the coordinate classifier for
\[
P/Q\cong\mathbb Z/4
\]
into fundamental-weight (Dynkin-label) coordinates. This gives an intrinsic representation-theoretic form of the same quotient classifier.

No identification with the cyclotomic mod-4 lift, Pell clocks, or local ramification is asserted here.

---

## 1. Fundamental weights in character coordinates

Use the simple roots
\[
\alpha_1=(0,1,1),\qquad
\alpha_2=(1,-1,0),\qquad
\alpha_3=(0,1,-1),
\]
and fundamental weights
\[
\omega_1=\left(\frac12,\frac12,\frac12\right),\qquad
\omega_2=(1,0,0),\qquad
\omega_3=\left(\frac12,\frac12,-\frac12\right).
\]
They satisfy
\[
\omega_i\cdot\alpha_j=\delta_{ij}.
\]

Every weight has unique Dynkin coordinates
\[
\lambda=m_1\omega_1+m_2\omega_2+m_3\omega_3,
\qquad m_i\in\mathbb Z.
\]

Writing \(\lambda=(x,y,z)\), direct expansion gives
\[
\boxed{x=\frac{m_1+m_3}{2}+m_2,}
\]
\[
\boxed{y=\frac{m_1+m_3}{2},}
\]
\[
\boxed{z=\frac{m_1-m_3}{2}.}
\]
Conversely,
\[
\boxed{m_1=y+z,\qquad m_2=x-y,\qquad m_3=y-z.}
\]

---

## 2. Quotient classes of the fundamental weights

Let
\[
g=[\omega_1]\in P/Q.
\]
From the previous lattice audit,
\[
[\omega_1]=g,
\qquad
[\omega_2]=2g,
\qquad
[\omega_3]=3g=-g.
\]
Therefore
\[
\boxed{
[\lambda]=(m_1+2m_2+3m_3)g\pmod4.
}
\]
Equivalently,
\[
\boxed{
[\lambda]=(m_1+2m_2-m_3)g\pmod4.
}
\]

Define the Dynkin-coordinate charge
\[
\boxed{q(\lambda):=m_1+2m_2+3m_3\pmod4.}
\]
Then
\[
\boxed{P/Q\cong\mathbb Z/4,\qquad [\lambda]\longleftrightarrow q(\lambda).}
\]

---

## 3. Agreement with the character-coordinate classifier

The earlier coordinate classifier was
\[
\kappa(x,y,z)=-2(x+y+z)\pmod4.
\]
Substitute the Dynkin-coordinate expansion:
\[
x+y+z
=\left(\frac{m_1+m_3}{2}+m_2\right)
+\frac{m_1+m_3}{2}
+\frac{m_1-m_3}{2}.
\]
Thus
\[
-2(x+y+z)
=-3m_1-2m_2-m_3.
\]
Modulo 4,
\[
-3m_1-2m_2-m_3
\equiv m_1+2m_2+3m_3.
\]
Hence
\[
\boxed{
\kappa(\lambda)=q(\lambda)\pmod4.
}
\]
So the coordinate parity classifier and the Dynkin-label classifier are exactly the same quotient map.

---

## 4. Complete Dynkin-label class test

For any
\[
\lambda=m_1\omega_1+m_2\omega_2+m_3\omega_3,
\]
we have
\[
\boxed{
\begin{array}{c|c}
m_1+2m_2+3m_3\pmod4&[\lambda]\\ \hline
0&0\\
1&g\\
2&2g\\
3&3g
\end{array}}
\]

This is a complete test for the discriminant class of every A3 weight.

---

## 5. Distinguished weights

The fundamental representations give the three nonzero classes immediately:
\[
\omega_1:(m_1,m_2,m_3)=(1,0,0),\qquad q=1,
\]
\[
\omega_2:(0,1,0),\qquad q=2,
\]
\[
\omega_3:(0,0,1),\qquad q=3.
\]
Thus
\[
\boxed{
\omega_1\leftrightarrow g,\qquad
\omega_2\leftrightarrow2g,\qquad
\omega_3\leftrightarrow3g.
}
\]

The root lattice consists exactly of the zero-charge weights:
\[
\boxed{
Q=\{\lambda\in P:q(\lambda)=0\}.
}
\]

---

## 6. Minuscule tetrahedra in Dynkin language

The four primitive tetrahedral vertices are the Weyl orbit
\[
\{\mu_r\}=W(A_3)\cdot\omega_1.
\]
Because the Weyl group acts trivially on P/Q,
\[
q(\mu_r)=1\pmod4
\]
for all four vertices.

Their negatives form
\[
\{-\mu_r\}=W(A_3)\cdot\omega_3,
\]
and
\[
q(-\mu_r)=3\pmod4.
\]

Thus the two opposite tetrahedra are exactly the two dual minuscule classes
\[
\boxed{g\quad\text{and}\quad -g=3g.}
\]

---

## 7. The six-weight orbit of omega_2

The Weyl orbit of
\[
\omega_2=(1,0,0)
\]
is
\[
W(A_3)\cdot\omega_2
=\{\pm e_1,\pm e_2,\pm e_3\}.
\]
Every point has quotient charge 2:
\[
\boxed{q=2\pmod4.}
\]
This is the six-weight orbit of the second fundamental representation (the exterior-square representation in type A3).

This is important geometrically: the class 2g contains both the four raw character vertices \(v_r=2\mu_r\) and the six-point orbit \(W\cdot\omega_2\). Therefore a P/Q class does not determine a Weyl orbit.

---

## 8. SU(4) interpretation

For the simply connected compact group of type A3,
\[
SU(4),
\]
one has the standard identification
\[
P/Q\cong Z(SU(4))\cong\mathbb Z/4.
\]
For a highest weight with Dynkin labels
\[
(m_1,m_2,m_3),
\]
the central character is determined by
\[
\boxed{m_1+2m_2+3m_3\pmod4.}
\]

Equivalently, if the representation is indexed by a Young diagram, this is the number of boxes modulo 4.

Thus the exact character-coordinate classifier discovered in this discriminant-12 A3 geometry is the usual A3/SU(4) central-charge classifier written in the coordinates naturally supplied by the three quadratic characters.

---

## 9. Representation table

\[
\boxed{
\begin{array}{c|c|c|c|c}
\text{highest weight}&\text{Dynkin labels}&\dim& q\pmod4&P/Q\\ \hline
0&(0,0,0)&1&0&0\\
\omega_1&(1,0,0)&4&1&g\\
\omega_2&(0,1,0)&6&2&2g\\
\omega_3&(0,0,1)&4&3&3g
\end{array}}
\]

The dimensions 4,6,4 match the cardinalities of the corresponding minuscule/fundamental weight orbits:
\[
4,\quad6,\quad4.
\]
The root system itself has 12 roots and occupies the neutral class 0.

---

## 10. Structural summary

The A3 branch now has three exactly equivalent descriptions of the same Z/4 quotient:

1. Character coordinates:
\[
\kappa(x,y,z)=-2(x+y+z)\pmod4.
\]

2. Doubled coordinates:
\[
\kappa=-(X+Y+Z)\pmod4.
\]

3. Dynkin labels:
\[
\boxed{q=m_1+2m_2+3m_3\pmod4.}
\]

The distinguished finite configurations are
\[
\boxed{
\begin{array}{c|c|c}
q&\text{distinguished orbit}&\text{size}\\ \hline
0&\Phi(A_3)&12\\
1&W\cdot\omega_1&4\\
2&W\cdot\omega_2&6\\
3&W\cdot\omega_3&4
\end{array}}
\]
with the separate raw character tetrahedron \(\{v_r\}\) also lying in q=2 but forming a different four-point Weyl orbit.

---

## 11. Guardrail

The appearance of Z/4 here is intrinsic to the A3 discriminant group
\[
P/Q,
\]
or equivalently the center of simply connected type A3. It is not, by itself, evidence that this Z/4 is canonically the cyclotomic mod-4 lift, a Pell clock, or a ramified local quotient. Any such bridge requires an independent exact map.