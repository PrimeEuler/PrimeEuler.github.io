# Cone Derivation Ledger v13.495 — Tetrahedral and A3 Root P/Q Classification Table

## Scope

Apply the exact v13.492 coordinate classifier
\[
\kappa(x,y,z)=-2(x+y+z)\pmod4
\]
to the four minuscule tetrahedral vertices, their four negatives, and all twelve oriented A3 roots.

Use
\[
g=[\omega_1],\qquad \omega_1=\frac12(1,1,1),
\]
so
\[
[p]=\kappa(p)g.
\]
Equivalently, for doubled coordinates \((X,Y,Z)=(2x,2y,2z)\),
\[
\kappa(p)=-(X+Y+Z)\pmod4.
\]

Here “tetrahedral vertices” means the primitive/minuscule tetrahedron
\[
\mu_r=v_r/2.
\]
For completeness the raw doubled character vertices \(v_r\) are also tabulated separately.

---

## 1. Four minuscule tetrahedral vertices

The four primitive tetrahedral weights are
\[
\mu_1=\frac12(1,1,1),
\quad
\mu_5=\frac12(1,-1,-1),
\quad
\mu_7=\frac12(-1,1,-1),
\quad
\mu_{11}=\frac12(-1,-1,1).
\]

Their complete classification is
\[
\boxed{
\begin{array}{c|c|c|c|c}
\text{point}&(x,y,z)&(X,Y,Z)&X+Y+Z\pmod4&[p]\\ \hline
\mu_1&(1/2,1/2,1/2)&(1,1,1)&3&g\\
\mu_5&(1/2,-1/2,-1/2)&(1,-1,-1)&3&g\\
\mu_7&(-1/2,1/2,-1/2)&(-1,1,-1)&3&g\\
\mu_{11}&(-1/2,-1/2,1/2)&(-1,-1,1)&3&g
\end{array}}
\]

Thus
\[
\boxed{\mu_r\in g+Q\quad\text{for all }r.}
\]
This is also immediate from
\[
\mu_r-\mu_s\in Q.
\]

---

## 2. The four opposite tetrahedral vertices

Negating gives
\[
-\mu_1=\frac12(-1,-1,-1),
\]
\[
-\mu_5=\frac12(-1,1,1),
\]
\[
-\mu_7=\frac12(1,-1,1),
\]
\[
-\mu_{11}=\frac12(1,1,-1).
\]

Their classification is
\[
\boxed{
\begin{array}{c|c|c|c|c}
\text{point}&(x,y,z)&(X,Y,Z)&X+Y+Z\pmod4&[p]\\ \hline
-\mu_1&(-1/2,-1/2,-1/2)&(-1,-1,-1)&1&3g\\
-\mu_5&(-1/2,1/2,1/2)&(-1,1,1)&1&3g\\
-\mu_7&(1/2,-1/2,1/2)&(1,-1,1)&1&3g\\
-\mu_{11}&(1/2,1/2,-1/2)&(1,1,-1)&1&3g
\end{array}}
\]

Hence
\[
\boxed{-\mu_r\in3g+Q\quad\text{for all }r.}
\]
As expected,
\[
[-\mu_r]=-[\mu_r]=-g=3g.
\]

---

## 3. The six positive A3 roots

Use the v13.489 simple-root convention
\[
\alpha_1=(0,1,1),
\quad
\alpha_2=(1,-1,0),
\quad
\alpha_3=(0,1,-1).
\]
The six positive roots are
\[
\alpha_1,
\alpha_2,
\alpha_3,
\alpha_1+\alpha_2,
\alpha_2+\alpha_3,
\alpha_1+\alpha_2+\alpha_3.
\]
Explicitly:
\[
(0,1,1),
(1,-1,0),
(0,1,-1),
(1,0,1),
(1,0,-1),
(1,1,0).
\]

Classification:
\[
\boxed{
\begin{array}{c|c|c|c|c}
\text{root}&(x,y,z)&(X,Y,Z)&X+Y+Z\pmod4&[\alpha]\\ \hline
\alpha_1&(0,1,1)&(0,2,2)&0&0\\
\alpha_2&(1,-1,0)&(2,-2,0)&0&0\\
\alpha_3&(0,1,-1)&(0,2,-2)&0&0\\
\alpha_1+\alpha_2&(1,0,1)&(2,0,2)&0&0\\
\alpha_2+\alpha_3&(1,0,-1)&(2,0,-2)&0&0\\
\alpha_1+\alpha_2+\alpha_3&(1,1,0)&(2,2,0)&0&0
\end{array}}
\]

Every positive root lies in Q.

---

## 4. The six negative A3 roots

Negating the six positive roots gives
\[
(0,-1,-1),
(-1,1,0),
(0,-1,1),
(-1,0,-1),
(-1,0,1),
(-1,-1,0).
\]

Classification:
\[
\boxed{
\begin{array}{c|c|c|c|c}
\text{root}&(x,y,z)&(X,Y,Z)&X+Y+Z\pmod4&[\alpha]\\ \hline
-\alpha_1&(0,-1,-1)&(0,-2,-2)&0&0\\
-\alpha_2&(-1,1,0)&(-2,2,0)&0&0\\
-\alpha_3&(0,-1,1)&(0,-2,2)&0&0\\
-(\alpha_1+\alpha_2)&(-1,0,-1)&(-2,0,-2)&0&0\\
-(\alpha_2+\alpha_3)&(-1,0,1)&(-2,0,2)&0&0\\
-(\alpha_1+\alpha_2+\alpha_3)&(-1,-1,0)&(-2,-2,0)&0&0
\end{array}}
\]

Thus
\[
\boxed{\Phi(A_3)\subset Q,}
\]
as required for a root system.

---

## 5. Raw doubled character tetrahedron

The original character-sign vectors are
\[
v_r=2\mu_r.
\]
They are
\[
v_1=(1,1,1),
\quad
v_5=(1,-1,-1),
\quad
v_7=(-1,1,-1),
\quad
v_{11}=(-1,-1,1).
\]

Their classification is
\[
\boxed{
\begin{array}{c|c|c|c|c}
\text{point}&(x,y,z)&(X,Y,Z)&X+Y+Z\pmod4&[p]\\ \hline
v_1&(1,1,1)&(2,2,2)&2&2g\\
v_5&(1,-1,-1)&(2,-2,-2)&2&2g\\
v_7&(-1,1,-1)&(-2,2,-2)&2&2g\\
v_{11}&(-1,-1,1)&(-2,-2,2)&2&2g
\end{array}}
\]

So
\[
\boxed{v_r\in2g+Q.}
\]
Because \(2g=-2g\), their negatives also lie in the same order-two coset.

---

## 6. Complete distinguished-point summary

The full classification is therefore
\[
\boxed{
\begin{array}{c|c|c|c}
\text{distinguished set}&\text{number of points}&P/Q\text{ class}&\text{coordinate type}\\ \hline
\Phi(A_3)&12&0&\text{integral, even sum}\\
\{\mu_r\}&4&g&\text{half-integral generator tetrahedron}\\
\{v_r\}&4&2g&\text{integral, odd-sum doubled tetrahedron}\\
\{-\mu_r\}&4&3g&\text{half-integral opposite tetrahedron}
\end{array}}
\]

Thus all four quotient classes have a natural finite distinguished configuration in the character-coordinate geometry:
\[
\boxed{
0\leftrightarrow12\text{ roots},\qquad
g\leftrightarrow4\text{ minuscule vertices},\qquad
2g\leftrightarrow4\text{ doubled character vertices},\qquad
3g\leftrightarrow4\text{ opposite minuscule vertices}.
}
\]

---

## 7. Edge-difference check

For distinct tetrahedral labels r,s,
\[
\alpha_{r,s}=\mu_r-\mu_s.
\]
Since
\[
[\mu_r]=[\mu_s]=g,
\]
we get immediately
\[
[\alpha_{r,s}]=g-g=0.
\]
This quotient argument explains all twelve root classifications simultaneously.

In raw character coordinates,
\[
v_r-v_s=2\alpha_{r,s},
\]
and both raw vertices lie in 2g, so again
\[
[v_r-v_s]=2g-2g=0.
\]

---

## 8. Negation on P/Q

Negation induces
\[
k g\mapsto-k g.
\]
Thus
\[
0\mapsto0,
\qquad
g\leftrightarrow3g,
\qquad2g\mapsto2g.
\]

This is visible geometrically:
- roots occur in ± pairs inside class 0;
- the minuscule tetrahedron and its negative occupy the two opposite generator classes g and 3g;
- the raw doubled tetrahedron and its negative both occupy the unique order-two class 2g.

Note that this negation automorphism is not the Weyl action on P/Q: the Weyl group acts trivially on the quotient, while ambient central inversion exchanges g and 3g.

---

## 9. Guardrail

This classification is exact A3 lattice arithmetic in the discriminant-12 character coordinates. The four quotient classes and their distinguished configurations should not be identified with Pell/cyclotomic/local ramification states without a separately established canonical map.