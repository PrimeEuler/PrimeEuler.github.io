# Cone Derivation Ledger v13.492 — Complete Coordinate Classifier for A3 P/Q

## Scope

Turn the v13.491 quotient description into a complete pointwise coordinate test. For every
\[
p=(x,y,z)\in P(A_3),
\]
determine exactly whether
\[
[p]\in P/Q
\]
is
\[
0,\quad g,\quad 2g,\quad 3g,
\]
where
\[
g=[\omega_1],\qquad \omega_1=\frac12(1,1,1).
\]

---

## 1. Membership test for the weight lattice itself

In the character coordinates,
\[
\boxed{P=\mathbb Z^3\cup(\mathbb Z+\tfrac12)^3.}
\]
Thus a real triple \((x,y,z)\) lies in P if and only if either

1. all three coordinates are integers, or
2. all three coordinates are half-integers with fractional part \(1/2\).

Equivalently,
\[
\boxed{2x,2y,2z\in\mathbb Z\quad\text{and}\quad 2x\equiv2y\equiv2z\pmod2.}
\]

Mixed-parity triples such as \((1,0,1/2)\) are not in P.

---

## 2. Universal quotient classifier

For every \(p=(x,y,z)\in P\), define
\[
\boxed{\kappa(p)=-2(x+y+z)\pmod4.}
\]
Because \(p\in P\), this is always an integer modulo 4.

With the generator convention \(g=[\omega_1]\),
\[
\boxed{[p]=\kappa(p)\,g.}
\]
Therefore the complete test is
\[
\boxed{
\begin{array}{c|c}
-2(x+y+z)\pmod4&[p]\\ \hline
0&0\\
1&g\\
2&2g\\
3&3g
\end{array}}
\]

This single congruence classifies every point of P.

---

## 3. Integer-coordinate branch

Suppose
\[
p=(x,y,z)\in\mathbb Z^3.
\]
Let
\[
S=x+y+z\in\mathbb Z.
\]
Then
\[
\kappa(p)=-2S\pmod4.
\]
Hence only the even quotient classes can occur:

\[
\boxed{S\equiv0\pmod2\iff[p]=0,}
\]
\[
\boxed{S\equiv1\pmod2\iff[p]=2g.}
\]

Thus
\[
\boxed{Q=\{(x,y,z)\in\mathbb Z^3:x+y+z\text{ even}\},}
\]
while
\[
\boxed{2g+Q=\{(x,y,z)\in\mathbb Z^3:x+y+z\text{ odd}\}.}
\]

So the integral lattice \(\mathbb Z^3\) splits exactly into the two even classes:
\[
\boxed{\mathbb Z^3=Q\sqcup(2g+Q).}
\]

---

## 4. Half-integral branch

Suppose
\[
p=(x,y,z)\in(\mathbb Z+\tfrac12)^3.
\]
Write
\[
x=a+\frac12,\qquad y=b+\frac12,\qquad z=c+\frac12,
\]
with \(a,b,c\in\mathbb Z\).

Then
\[
S=x+y+z=a+b+c+\frac32,
\]
so
\[
\kappa(p)=-2(a+b+c)-3\pmod4.
\]
Let
\[
N=a+b+c.
\]
Then
\[
\boxed{\kappa(p)\equiv1-2N\pmod4.}
\]
Therefore
\[
\boxed{N\text{ even}\iff[p]=g,}
\]
\[
\boxed{N\text{ odd}\iff[p]=3g.}
\]

Equivalently:
\[
\boxed{
g+Q=\left\{(a+\tfrac12,b+\tfrac12,c+\tfrac12):a+b+c\text{ even}\right\},}
\]
\[
\boxed{
3g+Q=\left\{(a+\tfrac12,b+\tfrac12,c+\tfrac12):a+b+c\text{ odd}\right\}.}
\]

Thus the half-integral part splits exactly into the two odd classes:
\[
\boxed{(\mathbb Z+\tfrac12)^3=(g+Q)\sqcup(3g+Q).}
\]

---

## 5. Equivalent doubled-coordinate test

For computational purposes, set
\[
X=2x,\qquad Y=2y,\qquad Z=2z.
\]
For \(p\in P\), \(X,Y,Z\in\mathbb Z\) and have common parity.

The quotient formula becomes
\[
\boxed{\kappa(p)=-(X+Y+Z)\pmod4.}
\]
This is the simplest integer-arithmetic implementation.

Therefore:
\[
\boxed{
\begin{array}{c|c}
X+Y+Z\pmod4&[p]\\ \hline
0&0\\
3&g\\
2&2g\\
1&3g
\end{array}}
\]

Equivalently, using \(R=(X+Y+Z)\bmod4\),
\[
\boxed{[p]=(-R\bmod4)g.}
\]

---

## 6. Four-coset coordinate partition

Combining the two branches gives the complete partition
\[
\boxed{
P=C_0\sqcup C_1\sqcup C_2\sqcup C_3,
}
\]
where
\[
\boxed{C_0=Q=\{(x,y,z)\in\mathbb Z^3:x+y+z\equiv0\pmod2\},}
\]
\[
\boxed{C_2=2g+Q=\{(x,y,z)\in\mathbb Z^3:x+y+z\equiv1\pmod2\},}
\]
\[
\boxed{C_1=g+Q=\{(a+\tfrac12,b+\tfrac12,c+\tfrac12):a+b+c\equiv0\pmod2\},}
\]
\[
\boxed{C_3=3g+Q=\{(a+\tfrac12,b+\tfrac12,c+\tfrac12):a+b+c\equiv1\pmod2\}.}
\]

This is a complete coordinate classification of P/Q.

---

## 7. Representative checks

### Zero class
\[
(0,0,0):\quad X+Y+Z=0\Rightarrow[p]=0.
\]
A root such as
\[
(0,1,1):\quad X+Y+Z=4\equiv0\pmod4
\]
also lies in 0.

### Generator class g
\[
\omega_1=(1/2,1/2,1/2):\quad X+Y+Z=3
\]
so
\[
[p]=g.
\]
Likewise every minuscule tetrahedral vertex \(v_r/2\) has doubled-coordinate sum congruent to 3 mod 4.

### Order-two class 2g
\[
\omega_2=(1,0,0):\quad X+Y+Z=2
\]
so
\[
[p]=2g.
\]
Every raw character vertex \(v_r\) has odd ordinary coordinate sum, hence belongs here.

### Opposite generator class 3g
\[
\omega_3=(1/2,1/2,-1/2):\quad X+Y+Z=1
\]
so
\[
[p]=3g.
\]
Likewise the negatives of the minuscule tetrahedral vertices lie here.

---

## 8. Addition law visible in coordinates

Because
\[
\kappa(p+q)=\kappa(p)+\kappa(q)\pmod4,
\]
the coordinate classifier realizes the quotient group law directly.

In particular:
\[
g+g=2g,
\]
which is visible from
\[
(1/2,1/2,1/2)+(1/2,1/2,1/2)=(1,1,1),
\]
an integral odd-sum point.

Then
\[
2g+g=3g,
\]
and
\[
3g+g=0.
\]
Thus the four coordinate parity types form a genuine cyclic four-step addition law, not merely four unrelated parity classes.

---

## 9. Weyl invariance of the classifier

For every Weyl matrix \(M\in W(A_3)\cong S_4\),
\[
Mp-p\in Q.
\]
Hence
\[
\boxed{\kappa(Mp)=\kappa(p).}
\]

So the coordinate test is invariant under all signed-permutation matrices from the discriminant-12 character representation.

The Weyl group may change coordinate signs and permute axes, but it cannot change the quotient class.

---

## 10. Minimal algorithm

Given a real triple \((x,y,z)\):

1. Compute \(X=2x,Y=2y,Z=2z\).
2. If any of \(X,Y,Z\) is nonintegral, then \(p\notin P\).
3. If \(X,Y,Z\) do not all have the same parity, then \(p\notin P\).
4. Otherwise compute
   \[
   R=(X+Y+Z)\bmod4.
   \]
5. Return
   \[
   \boxed{[p]=(-R\bmod4)g.}
   \]

Explicitly:
\[
R=0\to0,\qquad
R=3\to g,\qquad
R=2\to2g,\qquad
R=1\to3g.
\]

This gives a complete exact classifier using only doubled integer coordinates and one mod-4 sum.

---

## 11. Guardrail

This mod-4 coordinate classifier is the discriminant-group map of the A3 root/weight lattice in the chosen character coordinates. Its appearance of modulus 4 is intrinsic to
\[
[P:Q]=\det A_3=4.
\]
No identification with the cyclotomic mod-4 lift, Pell clocks, or local ramification quotients is asserted merely from the shared modulus.