# Cone Derivation Ledger v13.491 — A3 Discriminant Group P/Q and Weyl Action

## Scope

Continue the exact A3 character-coordinate lattice analysis after v13.487 and External Audit Round 37 (v13.490). Compute
\[
P/Q\cong\mathbb Z/4,
\]
give explicit representatives for all four cosets in the coordinates
\[
(\chi_{-4},\chi_{-3},\chi_{12}),
\]
and determine the action of the Weyl group
\[
W(A_3)\cong S_4
\]
on the quotient.

Guardrail from v13.490: the corrected reflection-axis labeling is
\[
F\text{ fixes }\chi_{-4},\qquad AF\text{ fixes }\chi_{-3},\qquad A^2F\text{ fixes }\chi_{12}.
\]
The quotient calculation below does not depend on that labeling, but all downstream references use the audited convention.

---

## 1. Root and weight lattices

From v13.487,
\[
Q=Q(A_3)=\{(x,y,z)\in\mathbb Z^3:x+y+z\equiv0\pmod2\},
\]
while
\[
P=P(A_3)=\mathbb Z^3\cup\left(\mathbb Z+\frac12\right)^3.
\]

Use the simple roots
\[
\alpha_1=(0,1,1),\quad
\alpha_2=(1,-1,0),\quad
\alpha_3=(0,1,-1),
\]
and fundamental weights
\[
\omega_1=\frac12(1,1,1),\qquad
\omega_2=(1,0,0),\qquad
\omega_3=\frac12(1,1,-1).
\]

Since
\[
[P:Q]=\det C_{A_3}=4,
\]
the quotient has four elements.

---

## 2. A concrete quotient coordinate

Every point of P is either integral or all-half-integral. Define
\[
\nu:P\to\mathbb Z/4
\]
by
\[
\boxed{\nu(x,y,z)=2(x+y+z)\pmod4.}
\]
Because \(x+y+z\in\frac12\mathbb Z\), the right side is an integer modulo 4.

For a root-lattice point \(q\in Q\), its coordinate sum is even, so
\[
\nu(q)=0.
\]
Conversely, if \(\nu(p)=0\), then \(p\) cannot be genuinely half-integral, because three half-integers have half-integral sum and hence \(2\sum p_i\) is odd. Thus \(p\in\mathbb Z^3\), and \(2\sum p_i\equiv0\pmod4\) means \(\sum p_i\) is even, hence \(p\in Q\).

Therefore
\[
\boxed{\ker\nu=Q.}
\]
Moreover
\[
\nu(\omega_1)=2\cdot\frac32=3\pmod4.
\]
Thus \(\nu\) is onto and induces an explicit isomorphism
\[
\boxed{P/Q\xrightarrow{\sim}\mathbb Z/4.}
\]

If one wants \([\omega_1]\) to correspond to \(1\in\mathbb Z/4\), use instead
\[
\boxed{\kappa=-\nu= -2(x+y+z)\pmod4.}
\]
Then
\[
\kappa(\omega_1)=1.
\]
We use this generator convention below.

---

## 3. Representatives for all four cosets

With generator
\[
g=[\omega_1],
\]
we have
\[
P/Q=\{0,g,2g,3g\}.
\]
A convenient representative table is

\[
\boxed{
\begin{array}{c|c|c|c}
\mathbb Z/4&\text{representative}&\text{coordinate type}&\kappa\\ \hline
0&(0,0,0)&\text{integral, even sum}&0\\
1&\omega_1=\frac12(1,1,1)&\text{half-integral}&1\\
2&\omega_2=(1,0,0)&\text{integral, odd sum}&2\\
3&\omega_3=\frac12(1,1,-1)&\text{half-integral}&3
\end{array}}
\]

Indeed,
\[
2\omega_1=(1,1,1),
\]
and
\[
2\omega_1-\omega_2=(0,1,1)=\alpha_1\in Q,
\]
so
\[
\boxed{[\omega_2]=2[\omega_1].}
\]
Also
\[
\omega_3+\omega_1=(1,1,0)\in Q,
\]
so
\[
\boxed{[\omega_3]=-[\omega_1]=3[\omega_1].}
\]
Thus \([\omega_1]\) has exact order four.

---

## 4. Intrinsic description of the four cosets

The quotient classes have a simple coordinate description:

\[
\boxed{Q=\{z\in\mathbb Z^3:\sum z_i\text{ even}\}.}
\]

\[
\boxed{2g+Q=\{z\in\mathbb Z^3:\sum z_i\text{ odd}\}.}
\]

The two remaining classes are the all-half-integral points, separated by \(\kappa\):
\[
\boxed{g+Q=\{p\in(\mathbb Z+\tfrac12)^3:\kappa(p)=1\},}
\]
\[
\boxed{3g+Q=\{p\in(\mathbb Z+\tfrac12)^3:\kappa(p)=3\}.}
\]

Equivalently, writing
\[
p=(a/2,b/2,c/2),\qquad a,b,c\text{ odd},
\]
we have
\[
\kappa(p)=-(a+b+c)\pmod4.
\]

---

## 5. Location of the tetrahedral vertices

The raw character vertices are
\[
v_1=(1,1,1),\quad
v_5=(1,-1,-1),\quad
v_7=(-1,1,-1),\quad
v_{11}=(-1,-1,1).
\]
Every one is integral with odd coordinate sum. Therefore
\[
\boxed{[v_r]=2g=[\omega_2]\qquad(r=1,5,7,11).}
\]
So all four raw character-sign vertices occupy the unique order-two coset
\[
\boxed{2g+Q.}
\]

Their halves
\[
\mu_r=v_r/2
\]
are the four minuscule weights. Each lies in the generator coset
\[
\boxed{[\mu_r]=g=[\omega_1].}
\]
Indeed pairwise differences are roots:
\[
\mu_r-\mu_s\in Q.
\]

The negatives \(-\mu_r\) lie in
\[
\boxed{-g=3g=[\omega_3],}
\]
which is the opposite minuscule orbit.

Thus the tetrahedral geometry sits in the quotient as
\[
\boxed{
\begin{array}{ccl}
g&:&\text{minuscule tetrahedron }\{\mu_r\},\\
2g&:&\text{raw doubled character tetrahedron }\{v_r\},\\
3g&:&\text{opposite minuscule tetrahedron }\{-\mu_r\},\\
0&:&\text{root lattice }Q.
\end{array}}
\]

---

## 6. Weyl reflections act trivially on P/Q

For any root \(\alpha\) and weight \(\lambda\), because A3 is simply laced,
\[
s_\alpha(\lambda)=\lambda-(\lambda,\alpha)\alpha.
\]
By definition of the weight lattice,
\[
(\lambda,\alpha)\in\mathbb Z,
\]
so
\[
s_\alpha(\lambda)-\lambda\in Q.
\]
Therefore every root reflection acts trivially modulo Q:
\[
\boxed{[s_\alpha(\lambda)]=[\lambda]\in P/Q.}
\]
Since Weyl reflections generate \(W(A_3)\),
\[
\boxed{W(A_3)\text{ acts trivially on }P/Q.}
\]

Thus the homomorphism
\[
W(A_3)\to\operatorname{Aut}(P/Q)\cong\operatorname{Aut}(\mathbb Z/4)\cong C_2
\]
is the trivial homomorphism.

This is an important distinction: the Weyl group permutes weights very nontrivially inside each coset, but it does not permute the four quotient classes.

---

## 7. Direct verification with the character-coordinate matrices

The v13.483/v13.488 signed-permutation matrices are generated by the V4 sign flips and S3 coordinate permutations. Each is a Weyl matrix preserving Q and P.

For any \(M\in W(A_3)\) and \(p\in P\),
\[
\boxed{Mp-p\in Q.}
\]

Examples:

For the coordinate-swap reflection
\[
P_F(x,y,z)=(x,z,y),
\]
we have
\[
P_F\omega_1=\omega_1,
\]
so the generator class is visibly fixed.

For
\[
D_5=\operatorname{diag}(1,-1,-1),
\]
\[
D_5\omega_1=\frac12(1,-1,-1)=\mu_5,
\]
and
\[
D_5\omega_1-\omega_1=(0,-1,-1)=-\alpha_1\in Q.
\]
Hence
\[
[D_5\omega_1]=[\omega_1].
\]

Since \([\omega_1]\) generates P/Q, this already forces every group element generated by these Weyl matrices to act as identity on the quotient.

---

## 8. Weyl orbits versus quotient classes

The quotient class and Weyl orbit are different notions.

The class \(g+Q\) is infinite, but contains the four-element minuscule orbit
\[
W\cdot\omega_1=\{\mu_1,\mu_5,\mu_7,\mu_{11}\}.
\]

The class \(3g+Q\) contains the dual/opposite minuscule orbit
\[
W\cdot\omega_3=\{-\mu_1,-\mu_5,-\mu_7,-\mu_{11}\}.
\]

The class \(2g+Q\) contains the doubled tetrahedron \(\{v_r\}\), but that four-point set is not the full Weyl orbit of a generic representative of the coset; it is the orbit of \(v_1=2\omega_1\) under the standard S4 action.

The zero class contains the root system
\[
\Phi(A_3)\subset Q,
\]
whose twelve roots form a single Weyl orbit.

Hence the quotient stratification is Weyl-invariant while each stratum contains its own finite distinguished orbits.

---

## 9. Exact quotient picture

We obtain the compact diagram
\[
\boxed{
P/Q\cong\mathbb Z/4
=\{0,g,2g,3g\},\qquad g=[\omega_1].
}
\]
with
\[
\boxed{
\begin{array}{c|c|c}
\text{class}&\text{representative}&\text{distinguished A3 object}\\ \hline
0&0&12\text{ roots }\Phi\subset Q\\
g&\frac12(1,1,1)&4\text{ minuscule weights }\mu_r\\
2g&(1,0,0)&4\text{ raw character vertices }v_r\\
3g&\frac12(1,1,-1)&4\text{ opposite minuscule weights }-\mu_r
\end{array}}
\]

and
\[
\boxed{w\cdot k g=k g\qquad\forall w\in W(A_3),\ k\in\mathbb Z/4.}
\]

---

## 10. Interpretation and guardrail

The discriminant group here is the standard A3 lattice quotient. The striking character-coordinate feature is that the raw discriminant-12 sign tetrahedron lands exactly in its unique order-two class, while halving it gives the generator minuscule class.

This is an exact lattice/representation statement:
\[
\boxed{
\text{character signs }v_r\in2g+Q,
\qquad
v_r/2\in g+Q,
\qquad
(v_r-v_s)/2\in Q.
}
\]

No identification is asserted here between the abstract cyclic discriminant group \(P/Q\cong\mathbb Z/4\) and the previously studied Pell/cyclotomic clocks or local ramification filtrations. Any such comparison remains exploratory and requires a separately constructed canonical map.