# Cone Project — Derivation Ledger v13.163

**Version:** 13.163 — audited consolidation continuation  
**Date:** 2026-09-03  
**Consolidates:** v13.127 audited baseline together with the audited/corrected developments through v13.163.  
**Purpose:** establish a single current research baseline, remove superseded claims, separate exact results from interpretation, and expose the remaining high-value proof hinges.

---

# 0. Status convention

- **[S] Source-established** — explicitly supported by an audited source/manuscript.
- **[D] Derived** — exact algebraic/analytic consequence established in the project.
- **[N-cert] Certified numerical/computer-assisted result** — finite computation with an explicit rigorous enclosure/certificate.
- **[I] Interpretation** — structurally motivated identification not yet independently forced.
- **[O] Open** — requires proof, source bridge, normalization theorem, or further computation.
- **[Audit]** — correction, limitation, or scope statement.
- **[Superseded]** — do not reuse except historically.

This ledger deliberately distinguishes:
\[
\boxed{\text{exact equivalence}\neq\text{structural analogy}\neq\text{RH evidence}.}
\]

---

# PART I. FOUNDATIONAL CONE AND BOOLEAN/V4 GEOMETRY

## 1. Factor cone

**[S/D]**

For nonnegative factor coordinates \(u,v\),
\[
X=\frac{u-v}{2},\qquad
Y=\sqrt{uv},\qquad
T=\frac{u+v}{2},
\]
hence
\[
\boxed{T^2-X^2-Y^2=0.}
\]

The inverse null coordinates are
\[
u=T+X,\qquad v=T-X.
\]

This remains the foundational geometric object of Papers A–C.

---

## 2. Elementary factor cell

**[D]**

For bits
\[
(\epsilon_1,\epsilon_2)\in\{0,1\}^2,
\]
define centered shell increments
\[
x=\epsilon_1-\epsilon_2,\qquad
t=\epsilon_1+\epsilon_2-1.
\]

At physical spacing \(\delta\),
\[
\Delta X=\frac{\delta}{2}x,\qquad
\Delta T=\frac{\delta}{2}t.
\]

Then
\[
\boxed{
\Delta T^2-\Delta X^2
=
\frac{\delta^2}{4}\widetilde\chi_{12}.
}
\]

Equal-bit states are positive/noncompact; unequal-bit states are
negative/compact.

The four cell states form a Boolean torsor for \(V_4\).

---

## 3. Shell \(V_4\)

**[D]**

Define
\[
W:(x,t)\mapsto(-x,-t),
\qquad
S:(x,t)\mapsto(t,x).
\]

Then
\[
W^2=S^2=I,\qquad WS=SW,
\]
so
\[
\langle W,S\rangle\cong V_4.
\]

The elementary bit flips
\[
F_1:(\epsilon_1,\epsilon_2)\mapsto(1-\epsilon_1,\epsilon_2),
\]
\[
F_2:(\epsilon_1,\epsilon_2)\mapsto(\epsilon_1,1-\epsilon_2)
\]
act as
\[
F_1:(x,t)\mapsto(-t,-x),
\qquad
F_2:(x,t)\mapsto(t,x),
\]
and therefore
\[
\boxed{
S=F_2,\qquad
W=F_1F_2,\qquad
WS=F_1.
}
\]

---

## 4. Complex shell coordinate

**[D]**

Let
\[
z=t+ix,\qquad
w=e^{-i\pi/4}z.
\]

Then
\[
W:w\mapsto-w,
\qquad
S:w\mapsto\bar w,
\qquad
WS:w\mapsto-\bar w.
\]

With
\[
s=\frac12+w,
\]
the orbit is
\[
\boxed{
\{s,1-s,\bar s,1-\bar s\}.
}
\]

Thus the standard zeta quartet action is exactly the shell \(V_4\) action
after this coordinate change.

The fixed locus of
\[
s\mapsto1-\bar s
\]
is
\[
\Re s=\frac12,
\]
corresponding to the shell null line \(t=-x\).

**Audit:** this is an exact coordinate/action equivalence. It is not, by
itself, evidence for RH.

---

# PART II. MOD-12 AND CYCLOTOMIC \(V_4\)

## 5. Quadratic residues and units mod \(12\)

**[D]**

\[
QR(12)=\{0,1,4,9\},
\qquad
U(12)=\{1,5,7,11\}.
\]

The map
\[
\Phi(r)=2r-1
\]
is a bijection
\[
QR(12)\to U(12).
\]

CRT identifies the four idempotent states with the Boolean cell:
\[
00\leftrightarrow0,\qquad
10\leftrightarrow4,\qquad
01\leftrightarrow9,\qquad
11\leftrightarrow1.
\]

Transporting multiplication on \(U(12)\) back to the Boolean cell gives
\[
\boxed{
T_5=F_1,\qquad
T_7=F_2,\qquad
T_{11}=F_1F_2.
}
\]

Thus the direct CRT labeling is
\[
(\rho,\kappa,\rho\kappa)
\mapsto
(T_{11},T_7,T_5).
\]

---

## 6. Cyclotomic field and complex-compatible labeling

**[D]**

Let
\[
K=\mathbb Q(i,\sqrt3)=\mathbb Q(\zeta_{12}).
\]

Its quadratic subfields are
\[
\mathbb Q(i),\qquad
\mathbb Q(\sqrt{-3}),\qquad
\mathbb Q(\sqrt3)
\]
with discriminants
\[
-4,\qquad -3,\qquad 12.
\]

For
\[
T_a(\zeta_{12})=\zeta_{12}^a,\qquad a\in U(12),
\]
the actions on \(i,\sqrt3\) are
\[
\begin{array}{c|cc}
 & i & \sqrt3\\ \hline
T_5 & i &-\sqrt3\\
T_7 &-i&-\sqrt3\\
T_{11}&-i&\sqrt3
\end{array}.
\]

Because \(T_{11}\) is actual complex conjugation, compatibility with the
distinguished analytic complex structure gives
\[
\boxed{
\rho\mapsto T_5,\qquad
\kappa\mapsto T_{11},\qquad
\rho\kappa\mapsto T_7.
}
\]

This differs from the direct CRT labeling by an order-three automorphism of
\(V_4\).  The distinction is real and must not be hidden by a basis change.

**Naming convention:** call this relabeling automorphism
\(\vartheta\), not \(\theta\), to avoid collision with Suzuki's continuous
parameter.

---

## 7. Character transport

**[D]**

The direct CRT cell Lorentz sign corresponds to \(\chi_{12}\).

Under the order-three relabeling,
\[
\boxed{
\chi_{12}\circ\vartheta^{-1}=\chi_{-4}.
}
\]

Thus the direct cell labeling and the complex-compatible Galois labeling
carry different nontrivial characters. This is a labeling distinction, not
a contradiction.

---

# PART III. SUZUKI / DE BRANGES OPERATOR STRUCTURE

## 8. Source facts retained from v13.127

**[S]**

For a Hermite–Biehler function \(E\),
\[
E^\#(z)=\overline{E(\bar z)},
\]
\[
A=\frac{E+E^\#}{2},
\qquad
B=\frac{i(E-E^\#)}2.
\]

Multiplication
\[
Mf(z)=zf(z)
\]
is a closed symmetric operator with deficiency indices \((1,1)\) in the
relevant de Branges setting.

For Suzuki's canonical systems,
\[
E_a(-z)=E_a^\#(z),
\]
with
\[
A_a(-z)=A_a(z),
\qquad
B_a(-z)=-B_a(z).
\]

Suzuki's canonical system has Hamiltonian
\[
H_{\rm can}(a)
=
\begin{pmatrix}
m(a)^{-2}&0\\
0&m(a)^2
\end{pmatrix},
\]
and
\[
m(a)
=
\frac{\det(1+H_{\omega,a})}
{\det(1-H_{\omega,a})}.
\]

For finite compression in the source-established range,
\(H_{\omega,a}\) is compact self-adjoint and strictly contractive under the
published hypotheses.

**Domain caution retained from v13.127:** the published unconditional
contraction statements do not automatically extend into every
RH-sensitive small-\(\omega\) regime.

---

## 9. Operator \(V_4\)

**[D]**

Define
\[
Rf(z)=f(-z),
\qquad
Jf(z)=f^\#(z).
\]

Then
\[
R^2=J^2=I,\qquad RJ=JR,
\]
with \(R\) unitary and \(J\) antiunitary.

Their complex types are
\[
R(if)=iRf,
\qquad
J(if)=-iJf.
\]

For multiplication,
\[
RMR^{-1}=-M,
\qquad
JMJ^{-1}=M,
\qquad
RJM(RJ)^{-1}=-M.
\]

Therefore
\[
\begin{array}{c|cc}
 & i & M\\ \hline
1&+&+\\
R&+&-\\
J&-&+\\
RJ&-&-
\end{array}.
\]

This matches the cyclotomic Galois signatures exactly:
\[
\boxed{
R\leftrightarrow T_5,\qquad
J\leftrightarrow T_{11},\qquad
RJ\leftrightarrow T_7.
}
\]

---

## 10. Real representation intertwiner

**[D]**

Let
\[
K_{\mathbb R}
=
\operatorname{span}_{\mathbb R}\{1,i,\sqrt3,i\sqrt3\},
\]
and
\[
\mathcal O_M
=
\operatorname{span}_{\mathbb R}\{I,iI,M,iM\}.
\]

Define
\[
\Psi(1)=I,\quad
\Psi(i)=iI,\quad
\Psi(\sqrt3)=M,\quad
\Psi(i\sqrt3)=iM.
\]

Then \(\Psi\) intertwines the two \(V_4\) representations.

**Audit:** this is a real representation intertwiner, not a field or algebra
homomorphism; in general \(M^2\neq3I\).

---

## 11. Self-adjoint sign / Clifford amplification

**[D, under the parity-compatible extension already audited]**

For the \(A\)-extension \(M_A\), \(0\notin\sigma(M_A)\) because \(A(0)=1\).

Define
\[
\Gamma=\operatorname{sgn}(M_A).
\]

Then
\[
\Gamma^2=I,
\]
and
\[
R\Gamma R^{-1}=-\Gamma.
\]

Hence
\[
R\Gamma=-\Gamma R.
\]

With
\[
P_\pm=\frac12(I\pm\Gamma),
\]
\(R\) exchanges the two sign sectors.

Thus
\[
\mathcal H\cong\mathbb C^2\otimes\mathcal K
\]
with
\[
\Gamma=\sigma_z\otimes I,
\qquad
R=\sigma_x\otimes I.
\]

This is the Hilbert-space amplification of the same irreducible real
two-generator Clifford module that later appears in the discriminant-\(12\)
return.

---

# PART IV. DISCRIMINANT-12 RETURN

## 12. Return and centered generator

**[D]**

The period-two return is
\[
\boxed{
g_{12}
=
\begin{pmatrix}
3&1\\
2&1
\end{pmatrix},
}
\]
with
\[
\operatorname{tr}g_{12}=4,
\qquad
\det g_{12}=1,
\qquad
\Delta=4^2-4=12.
\]

Define
\[
\boxed{
H_{12}=g_{12}-2I
=
\begin{pmatrix}
1&1\\
2&-1
\end{pmatrix}.
}
\]

Then
\[
\boxed{H_{12}^2=3I.}
\]

More generally, for \(g\in SL_2\),
\[
H_g=g-\frac{\operatorname{tr}g}{2}I
\]
satisfies
\[
\boxed{
H_g^2=\frac{\Delta_g}{4}I.
}
\]

Therefore
\[
\boxed{
\mathbb Q[H_{12}]\cong\mathbb Q(\sqrt3).
}
\]

---

## 13. Return reversal

**[D]**

For \(g\in SL_2\),
\[
g^{-1}=(\operatorname{tr}g)I-g.
\]

Hence
\[
H_{g^{-1}}=-H_g.
\]

For \(g_{12}\),
\[
g_{12}=2I+H_{12},
\qquad
g_{12}^{-1}=2I-H_{12}.
\]

An explicit rational involution is
\[
C=
\begin{pmatrix}
1&0\\
-2&-1
\end{pmatrix},
\qquad
C^2=I,
\]
with
\[
CH_{12}C^{-1}=-H_{12},
\qquad
Cg_{12}C^{-1}=g_{12}^{-1}.
\]

Normalize
\[
\varepsilon_{12}=\frac{H_{12}}{\sqrt3}.
\]

Then
\[
\varepsilon_{12}^2=I,
\qquad
C\varepsilon_{12}=-\varepsilon_{12}C.
\]

Thus the return side realizes
\[
\mathrm{Cl}_{2,0}(\mathbb R)\cong M_2(\mathbb R).
\]

---

## 14. Positive metric and regulator

**[D]**

The positive metric, unique up to scalar under the audited conditions making
\(H_{12}\) and \(C\) self-adjoint, is
\[
\boxed{
G=
\begin{pmatrix}
4&1\\
1&1
\end{pmatrix},
\qquad
\det G=3.
}
\]

The expanding and contracting eigenvalues are
\[
\lambda_\pm=2\pm\sqrt3.
\]

Define
\[
R_{12}=\log(2+\sqrt3).
\]

Then
\[
\cosh R_{12}=2,
\qquad
\sinh R_{12}=\sqrt3,
\]
and
\[
\boxed{
g_{12}=e^{R_{12}\varepsilon_{12}}.
}
\]

---

# PART V. SUZUKI \(\theta\)-FAMILY AND THE FIRST CHAMBER

## 15. Source coefficient family

**[S]**

Suzuki's asymptotic coefficient factor is
\[
w^\theta
e^{-\theta\psi(w)-\theta/w}
e^{-2\theta/(2w-3)}
=
1+\sum_{n\ge1}A_n(\theta)w^{-n}.
\]

The first coefficients are
\[
\boxed{
A_1(\theta)=-\frac{3\theta}{2},
}
\]
\[
A_2(\theta)=\frac{\theta(27\theta-34)}{24}.
\]

At \(\theta=2\),
\[
A_1(2)=-3,\qquad A_2(2)=\frac53.
\]

The two first-order scalar contributions identified in the source expansion
are
\[
\boxed{
\alpha_\theta=\frac{\theta}{2},
\qquad
\beta_\theta=\theta,
}
\]
whose sum is
\[
\frac{3\theta}{2}=-A_1(\theta).
\]

**Audit:** identifying these two scalar channels with literal upper/lower
unipotent \(SL_2\) shears remains **[I]**.

---

## 16. First arithmetic chamber

**[S/D]**

The theta kernel has the form
\[
K_\theta(x)
=
\sum_{n\ge1}
\frac{\lambda_\theta(n)}{\sqrt n}
g_\theta(x-\log n),
\]
with
\[
g_\theta(x)=0\qquad(x<0).
\]

Therefore for
\[
0<x<\log2,
\]
only \(n=1\) contributes:
\[
\boxed{
K_\theta(x)=g_\theta(x).
}
\]

The local source asymptotic is
\[
\boxed{
g_\theta(x)
=
\frac{(2\pi)^\theta}{\Gamma(\theta)}
x^{\theta-1}
+O(x^\theta).
}
\]

---

# PART VI. COEFFICIENT AUDIT AND CERTIFICATE REPAIR

## 17. Critical correction: \(p_n\neq A_n(2)\)

**[Audit / Supersedes earlier wording]**

The coefficients used in the original hardening calculation came from
\[
F_0(u)
=
\exp\!\left(
-u+\frac{u^2}{6}-\frac{u^4}{60}
-\frac{2u}{1-\frac32u}
\right)
=
\sum_{n\ge0}p_nu^n.
\]

They are not Suzuki's exact coefficients \(A_n(2)\).

They agree only through \(n=5\). At \(n=6\),
\[
A_6(2)=\frac{80027}{45360},
\qquad
p_6=\frac{11381}{6480},
\]
and
\[
\boxed{
A_6(2)-p_6=\frac1{126}.
}
\]

All statements calling the \(p_n\) the “Suzuki degree-40 coefficients” are
superseded.

---

## 18. Exact custom-model recursion

**[D]**

If
\[
\log F_0(u)=\sum_{n\ge1}e_nu^n,
\]
then
\[
p_0=1,
\qquad
\boxed{
np_n=\sum_{k=1}^n k e_kp_{n-k}.
}
\]

Thus the custom coefficient model is exact and reproducible; only its old
source label was wrong.

---

## 19. DLMF-controlled repair

**[S/D]**

Retaining \(B_2,B_4\) in the digamma expansion gives a complex remainder
bound
\[
\boxed{
|\delta\log F(w)|
\le
\frac{16\sqrt2}{252}|w|^{-6}
=
0.0897913372935\ldots |w|^{-6}.
}
\]

On the fixed contour \(\Re w=4\), this yields a rigorous inverse-transform
error for the custom model.

The resulting physical first-chamber uniform bound is
\[
\boxed{
|g_2(x)-g_{0,40}(x)|<0.003643,
\qquad
0\le x\le\log2.
}
\]

The omitted \(p_n\), \(n\ge40\), tail is negligible at this scale.

---

# PART VII. CERTIFIED \(\theta=2\) CROSSING

## 20. Positivity through \(x=.4\)

**[D / certificate replay]**

A restored lower kernel gives
\[
g_2(x)>0
\qquad
(0<x\le0.4).
\]

This supports the positive-Neumann argument used in the crossing certificate.

---

## 21. Exact finite crossing certificate

**[D + N-cert]**

At
\[
t=\frac15,
\]
the exact finite certificate gives
\[
\boxed{
m_2(1/5)>3.786007338662927\ldots
}
\]
and therefore
\[
\boxed{
m_2(1/5)>2+\sqrt3.
}
\]

Since
\[
m_2(0)=1
\]
and \(m_2\) is continuous,
\[
\boxed{
\exists\,t_*\in(0,1/5):
m_2(t_*)=2+\sqrt3.
}
\]

On the certified positive/contraction region the determinant ratio is
strictly increasing, so
\[
\boxed{
\exists!\,t_*\in(0,1/5):
m_2(t_*)=2+\sqrt3.
}
\]

Numerically,
\[
\boxed{
t_*\approx0.1916605
}
\qquad\text{[N-cert]}.
\]

---

# PART VIII. FULL FIRST-CHAMBER CONTRACTION

## 22. Exact polynomial/Galerkin certificate

**[D / computer-assisted exact arithmetic]**

Work on the rational enlargement
\[
T_0=\frac{347}{1000},
\qquad
2T_0=0.694>\log2.
\]

The custom finite kernel is replaced by an exact rational polynomial with
physical uniform replacement error
\[
\boxed{
<6\times10^{-9}.
}
\]

A 24-mode Legendre block is certified by exact rational
\(LDL^\top\):
\[
\boxed{
\|P_{24}K_{\rm poly}P_{24}\|<0.09951
}
\]
in normalized units.

The exact Hilbert–Schmidt projection tail satisfies
\[
\boxed{
\|K_{\rm poly}-P_{24}K_{\rm poly}P_{24}\|_{\rm HS}<0.00149.
}
\]

Restoring \(\pi^2\), transform error, and polynomial replacement gives
\[
\boxed{
\|K_2[t]\|
<
0.999398246164
<1
}
\]
for every
\[
\boxed{
0<t<\frac{\log2}{2}.
}
\]

This is the audited full first-chamber contraction theorem.

---

## 23. Local norm sharpening

**[D / certificates]**

Useful certified local bounds include

\[
t\le0.24:
\quad
\|K_2[t]\|<0.84178434288,
\]

\[
t\le0.28:
\quad
\|K_2[t]\|<0.93090578336,
\]

\[
t\le0.285:
\quad
\|K_2[t]\|<0.93943041342,
\]

\[
t\le0.29:
\quad
\|K_2[t]\|<0.94785634348,
\]

\[
t\le0.295:
\quad
\|K_2[t]\|<0.95539397354,
\]

\[
t\le0.30:
\quad
\|K_2[t]\|<0.962832903600,
\]

\[
t\le0.305:
\quad
\|K_2[t]\|<0.96938353366,
\]

and the sharpened rank-24 bound
\[
\boxed{
t\le0.31:
\quad
\|K_2[t]\|<0.96847244372.
}
\]

A weaker rank-18 \(t=.31\) bound is superseded by the rank-24 result.

The \(t=.32\) certificate
\[
\|K_2[t]\|<0.98607442384
\]
also remains available.

---

# PART IX. MONOTONICITY AUDIT

## 24. Kernel positivity through \(0.51\)

**[D]**

The repaired custom-model enclosure proves
\[
\boxed{
g_2(x)>0
\qquad
(0<x\le0.51).
}
\]

Hence
\[
\boxed{
m_2'(t)>0
\qquad
(0<t\le0.255).
}
\]

---

## 25. Residual lemma correction

**[Audit / Superseded]**

The old generic residual lemma omitted the boundary residual \(r(t)\).

For
\[
u=(I-K^2)^{-1}k,
\qquad
r=k-(I-K^2)v,
\]
the correct identity is
\[
u(t)
=
v(t)+r(t)+(K^2(u-v))(t).
\]

Thus the correct generic lower bound contains
\[
-|r(t)|.
\]

Old statements using the residual estimate without this term are
superseded.

The crossing theorem is unaffected.

---

## 26. Correct finite-Neumann tail bound

**[D]**

For
\[
v_m=\sum_{j=0}^mK^{2j}k,
\]
one has
\[
u-v_m=\sum_{j=m+1}^\infty K^{2j}k.
\]

With \(\|K\|\le\rho<1\),
\[
\boxed{
|(u-v_m)(t)|
\le
\frac{\rho^{2m+1}}{1-\rho^2}
\|k_t\|_2^2.
}
\]

This is the preferred monotonicity tail estimate.

---

## 27. Certified monotonicity frontier

**[D]**

Successive slab certificates close
\[
(0,.255],\quad
[.255,.28],\quad
[.28,.29],\quad
[.29,.30].
\]

Therefore the current theorem is
\[
\boxed{
m_2'(t)>0
\qquad
(0<t\le0.30).
}
\]

The strip
\[
(.30,\log2/2)
\]
is not currently certified monotone.

**Strategic audit:** full-chamber monotonicity is no longer required for the
already-proved existence and uniqueness of the crossing \(t_*\). Further
mechanical extension is therefore lower priority unless needed downstream.

---

# PART X. DETERMINANT TRANSFER AND SHEAR COORDINATE

## 28. Canonical determinant transfer

**[D]**

Define
\[
T_\theta(t)
=
\begin{pmatrix}
m_\theta(t)&0\\
0&m_\theta(t)^{-1}
\end{pmatrix}.
\]

Its intrinsic trace-defect/shear coordinate is
\[
\boxed{
\sigma_\theta(t)
=
m_\theta(t)+m_\theta(t)^{-1}-2.
}
\]

Every hyperbolic determinant transfer is conjugate to
\[
G_\sigma=
\begin{pmatrix}
1+\sigma&1\\
\sigma&1
\end{pmatrix}.
\]

For \(m=e^q\),
\[
\boxed{
\sigma=4\sinh^2(q/2).
}
\]

At the certified crossing,
\[
m_2(t_*)=2+\sqrt3,
\]
so
\[
\boxed{
\sigma_2(t_*)=2.
}
\]

---

## 29. Small-\(t\) source-to-global asymptotic

**[D]**

From the source-local kernel asymptotic,
\[
\operatorname{Tr}K_{\theta,t}
=
\frac{(4\pi)^\theta}{2\Gamma(\theta+1)}t^\theta
+O(t^{\theta+1}).
\]

Hence
\[
q_\theta(t):=\log m_\theta(t)
=
\boxed{
\frac{(4\pi t)^\theta}{\Gamma(\theta+1)}
+O(t^{\theta+1})
}
\]
for the audited \(\theta>1\) local regime.

Therefore
\[
\boxed{
\sigma_\theta(t)
=
\frac{(4\pi t)^{2\theta}}
{\Gamma(\theta+1)^2}
+
O(t^{2\theta+1}).
}
\]

**Consequence:** generic small-\(t\) Fredholm growth does not itself select
\(\theta=2\).

---

# PART XI. CAYLEY SELF-RECIPROCITY

## 30. Universal centered-Cayley identity

**[D]**

For \(g\in SL_2\), let
\[
\tau=\operatorname{tr}g,
\qquad
H=g-\frac{\tau}{2}I,
\]
and
\[
K=(g-I)(g+I)^{-1}.
\]

Then
\[
\boxed{
K=\frac{2}{\tau+2}H
}
\]
and
\[
\boxed{
KH=\frac{\tau-2}{2}I.
}
\]

In shear coordinates \(\tau=\sigma+2\),
\[
\boxed{
K_\sigma H_\sigma=\frac{\sigma}{2}I.
}
\]

---

## 31. Unique self-reciprocal shear

**[D]**

The condition
\[
K_\sigma=H_\sigma^{-1}
\]
is equivalent to
\[
K_\sigma H_\sigma=I.
\]

Therefore
\[
\frac{\sigma}{2}=1,
\]
and
\[
\boxed{
K_\sigma=H_\sigma^{-1}
\iff
\sigma=2.
}
\]

Thus \(\sigma=2\) is the unique centered-Cayley self-reciprocal
hyperbolic conjugacy class in this normalization.

At \(t=t_*\),
\[
\boxed{
K_{2,t_*}=H_{2,t_*}^{-1}.
}
\]

---

## 32. Source first channel and Cayley product

**[D after target identification / source comparison]**

If the target shear is set to
\[
\sigma=\theta,
\]
then
\[
K_\theta H_\theta=\frac{\theta}{2}I.
\]

This reproduces the source scalar channel
\[
\alpha_\theta=\theta/2.
\]

Also
\[
\beta_\theta=\theta=2K_\theta H_\theta
\]
at the scalar level, so
\[
\boxed{
-A_1(\theta)I=3K_\theta H_\theta.
}
\]

At \(\theta=2\), self-reciprocity gives
\[
-A_1(2)I=3I,
\]
while
\[
H_2^2=3I.
\]

Hence
\[
\boxed{
-A_1(2)I=H_2^2=3I.
}
\]

This makes the old “source cumulant = Casimir” equality a consequence of
Cayley self-reciprocity once the target identification is made.

---

## 33. Critical unresolved target identification

**[I/O]**

The source-internal necessity of
\[
\boxed{
\sigma_\theta(t)=\theta
}
\]
has not been derived.

Likewise, the literal identification
\[
(\theta/2,\theta)\rightsquigarrow(U,L)
\]
as two source-side opposite unipotent shears remains **[I]**.

These must not be presented as source theorems.

The exact statement is instead:

> If the dynamic determinant trace defect is identified with the source
> parameter, \(\sigma=\theta\), then centered-Cayley self-reciprocity selects
> \(\theta=2\) uniquely.

---

# PART XII. DISCRIMINANT-12 CYCLOTOMIC GLUING

## 34. Maximal real quadratic order

**[D]**

Since
\[
H_{12}^2=3I,
\]
the order
\[
\mathbb Z[H_{12}]
\]
has discriminant \(12\).

Because
\[
\mathcal O_{\mathbb Q(\sqrt3)}=\mathbb Z[\sqrt3],
\]
we have
\[
\boxed{
\mathbb Z[H_{12}]
\cong
\mathcal O_{\mathbb Q(\sqrt3)}.
}
\]

Thus the matrix discriminant and the arithmetic field/order discriminant are
the same integer \(12\).

---

## 35. Primitive twelfth-root operator

**[D]**

Adjoin the analytic complex structure \(iI\) and define
\[
\boxed{
\mathcal Z=\frac{H_{12}+iI}{2}.
}
\]

Then
\[
\mathcal Z^{-1}=\frac{H_{12}-iI}{2},
\]
so
\[
\boxed{
H_{12}=\mathcal Z+\mathcal Z^{-1},
\qquad
iI=\mathcal Z-\mathcal Z^{-1}.
}
\]

Moreover
\[
\boxed{
\mathcal Z^3=iI,
\qquad
\mathcal Z^6=-I,
\qquad
\mathcal Z^{12}=I.
}
\]

And
\[
\boxed{
\Phi_{12}(\mathcal Z)
=
\mathcal Z^4-\mathcal Z^2+I
=0.
}
\]

Therefore
\[
\boxed{
\mathcal Z\leftrightarrow
\zeta_{12}
=
\frac{\sqrt3+i}{2}.
}
\]

---

## 36. Integral gluing

**[D]**

The naive product order
\[
\mathbb Z[iI,H_{12}]
\]
has discriminant
\[
2304.
\]

The cyclotomic field has discriminant
\[
144.
\]

Hence
\[
\boxed{
[\mathcal O_{\mathbb Q(\zeta_{12})}:
\mathbb Z[iI,H_{12}]]=4.
}
\]

The half-element
\[
\boxed{
\mathcal Z=\frac{H_{12}+iI}{2}
}
\]
supplies the missing integral closure.

This is the exact arithmetic reason the half-sum is natural in the
real/complex gluing.

---

## 37. Galois power action

**[D]**

The complex-compatible \(V_4\) acts on the single generator by
\[
\boxed{
T_a(\mathcal Z)=\mathcal Z^a,
\qquad
a\in\{1,5,7,11\}.
}
\]

Explicitly,
\[
T_5(\mathcal Z)=\mathcal Z^5,
\qquad
T_7(\mathcal Z)=\mathcal Z^7,
\qquad
T_{11}(\mathcal Z)=\mathcal Z^{11}.
\]

Thus the earlier operator/Galois \(V_4\) is ordinary cyclotomic power action
on \(\mathcal Z\).

---

# PART XIII. CYCLOTOMIC CAYLEY RETURN

## 38. Hyperbolic return as Cayley image of \(\mathcal Z\)

**[D]**

Define
\[
\mathscr C(Z)
=
-i(I+Z)(I-Z)^{-1}.
\]

Then
\[
\boxed{
\mathscr C(\mathcal Z)
=
2I+H_{12}
=
g_{12}.
}
\]

Equivalently,
\[
\boxed{
g_{12}
=
-i(I+\mathcal Z)(I-\mathcal Z)^{-1}.
}
\]

The inverse relation is
\[
\boxed{
\mathcal Z
=
(g_{12}+iI)(g_{12}-iI)^{-1}.
}
\]

Thus the primitive cyclotomic generator and hyperbolic return are related by
one exact rational transformation.

---

## 39. Fundamental unit as cyclotomic unit

**[D]**

In the scalar realization,
\[
\boxed{
2+\sqrt3
=
-i\frac{1+\zeta_{12}}{1-\zeta_{12}}
=
\cot\frac{\pi}{12}.
}
\]

Therefore
\[
2+\sqrt3
\]
is simultaneously

1. the expanding eigenvalue of \(g_{12}\);
2. the fundamental totally positive Pell unit of \(\mathbb Q(\sqrt3)\);
3. an explicit cyclotomic unit;
4. the certified Suzuki determinant target \(m_2(t_*)\).

Thus
\[
\boxed{
m_2(t_*)
=
\lambda_+(g_{12})
=
2+\sqrt3
=
-i\frac{1+\zeta_{12}}{1-\zeta_{12}}.
}
\]

---

## 40. Regulator / circular-hyperbolic half-angle bridge

**[D]**

\[
R_{12}
=
\log(2+\sqrt3)
=
\boxed{
\log\cot\frac{\pi}{12}.
}
\]

Also
\[
\boxed{
\tanh\frac{R_{12}}2
=
\frac1{\sqrt3}
=
\tan\frac{\pi}{6}.
}
\]

Thus the order-\(12\) circular angle and discriminant-\(12\) hyperbolic
rapidity are related exactly by the Cayley half-angle transform.

---

## 41. Galois action on the return

**[D]**

Because
\[
g_{12}=2I+H_{12},
\qquad
g_{12}^{-1}=2I-H_{12},
\]
we have
\[
\boxed{
T_5(g_{12})=g_{12}^{-1},
}
\]
\[
\boxed{
T_{11}(g_{12})=g_{12},
}
\]
\[
\boxed{
T_7(g_{12})=g_{12}^{-1}.
}
\]

Under
\[
R\leftrightarrow T_5,\qquad
J\leftrightarrow T_{11},\qquad
RJ\leftrightarrow T_7,
\]
the same sign character controls Suzuki spectral sign, real quadratic
conjugation, and return reversal.

---

# PART XIV. PELL IDEAL REALIZATION

## 42. Return as multiplication by \(2+\sqrt3\)

**[D]**

Let
\[
F=\mathbb Q(\sqrt3),
\qquad
\varepsilon=2+\sqrt3.
\]

On the standard basis \(\{1,\sqrt3\}\), multiplication by \(\varepsilon\)
has matrix
\[
M_\varepsilon
=
\begin{pmatrix}
2&3\\
1&2
\end{pmatrix}.
\]

Let
\[
P=
\begin{pmatrix}
2&-1\\
0&1
\end{pmatrix}.
\]

Its columns represent
\[
2,\qquad \sqrt3-1.
\]

Then
\[
M_\varepsilon P=Pg_{12},
\]
so
\[
\boxed{
g_{12}=P^{-1}M_\varepsilon P.
}
\]

Therefore \(g_{12}\) is literally multiplication by the fundamental unit on
the lattice with basis
\[
\{2,\sqrt3-1\}.
\]

---

## 43. Ramified prime above \(2\)

**[D]**

Define
\[
\boxed{
\mathfrak p_2=(2,\sqrt3-1).
}
\]

Then
\[
N(\mathfrak p_2)=2,
\]
and
\[
\boxed{
\mathfrak p_2^2=(2).
}
\]

Thus \(\mathfrak p_2\) is the unique ramified prime above \(2\) in
\(\mathbb Q(\sqrt3)\).

Moreover
\[
\boxed{
\mathfrak p_2=(1+\sqrt3).
}
\]

On this ideal,
\[
\boxed{
g_{12}\leftrightarrow\times(2+\sqrt3),
\qquad
H_{12}\leftrightarrow\times\sqrt3.
}
\]

---

## 44. Arithmetic Galois reverser

**[D]**

Real quadratic conjugation acts on the ideal basis
\[
\{2,\sqrt3-1\}
\]
by
\[
Q=
\begin{pmatrix}
1&-1\\
0&-1
\end{pmatrix}.
\]

Then
\[
Q^2=I,
\qquad
QH_{12}Q^{-1}=-H_{12},
\]
and
\[
\boxed{
Qg_{12}Q^{-1}=g_{12}^{-1}.
}
\]

Thus return reversal is literal real quadratic Galois conjugation on the
return lattice.

---

# PART XV. NARROW HILBERT CLASS FIELD

## 45. Relative cyclotomic polynomial

**[D]**

Over
\[
F=\mathbb Q(\sqrt3),
\]
the generator \(\mathcal Z=\zeta_{12}\) satisfies
\[
\boxed{
\mathcal Z^2-\sqrt3\,\mathcal Z+1=0.
}
\]

At operator level,
\[
\boxed{
\mathcal Z^2-H_{12}\mathcal Z+I=0.
}
\]

The relative polynomial discriminant is
\[
3-4=-1,
\]
a unit.

Hence
\[
\boxed{
K/F=
\mathbb Q(\zeta_{12})/\mathbb Q(\sqrt3)
}
\]
is unramified at every finite prime.

The absolute discriminants confirm
\[
144=12^2.
\]

---

## 46. Ordinary and narrow class numbers

**[D]**

The Minkowski bound is
\[
\frac12\sqrt{12}=\sqrt3<2,
\]
so
\[
\boxed{
h(\mathbb Q(\sqrt3))=1.
}
\]

A norm-\(-1\) unit would solve
\[
x^2-3y^2=-1.
\]

Modulo \(3\), this would require
\[
x^2\equiv2\pmod3,
\]
impossible.

Hence there is no unit of norm \(-1\), and
\[
\boxed{
h^+(\mathbb Q(\sqrt3))=2.
}
\]

Therefore
\[
\boxed{
\mathbb Q(\zeta_{12})
=
H_F^+,
}
\]
the narrow Hilbert class field of \(F=\mathbb Q(\sqrt3)\).

---

## 47. The return ideal as the nontrivial narrow class

**[D]**

Although
\[
\mathfrak p_2=(1+\sqrt3)
\]
is principal ordinarily,
\[
N(1+\sqrt3)=-2.
\]

Because no unit has norm \(-1\), no generator of \(\mathfrak p_2\) is totally
positive.

Thus
\[
\boxed{
[\mathfrak p_2]
}
\]
is the unique nontrivial class in
\[
\mathrm{Cl}^+(F).
\]

Artin reciprocity therefore sends it to the unique nontrivial element of
\[
\mathrm{Gal}(K/F),
\]
namely the automorphism fixing \(\sqrt3\) and sending \(i\mapsto-i\):
\[
\boxed{
\operatorname{Art}_{K/F}(\mathfrak p_2)=T_{11}.
}
\]

With the Suzuki labeling,
\[
\boxed{
[\mathfrak p_2]
\longleftrightarrow
T_{11}
\longleftrightarrow
J.
}
\]

Since the Artin element is nontrivial and \(K/F\) is unramified,
\[
\boxed{
\mathfrak p_2\text{ is inert in }K/F.
}
\]

---

# PART XVI. ARITHMETIC LIGHT CONE

## 48. Norm form on \(\mathfrak p_2\)

**[D]**

For
\[
\alpha=2x+(\sqrt3-1)y
=
(2x-y)+\sqrt3\,y,
\]
\[
N_{F/\mathbb Q}(\alpha)
=
4x^2-4xy-2y^2.
\]

Define the primitive form
\[
\boxed{
q_{12}(x,y)=2x^2-2xy-y^2.
}
\]

Then
\[
N(\alpha)=2q_{12}(x,y).
\]

Its discriminant is
\[
\boxed{
(-2)^2-4(2)(-1)=12.
}
\]

Thus the same \(12\) is

- the matrix discriminant of \(g_{12}\);
- the field discriminant of \(\mathbb Q(\sqrt3)\);
- the discriminant of the primitive norm form on the return lattice.

---

## 49. Integral Lorentz invariance

**[D]**

Let
\[
S_{12}
=
\begin{pmatrix}
2&-1\\
-1&-1
\end{pmatrix}.
\]

Then
\[
q_{12}(v)=v^TS_{12}v
\]
and
\[
\boxed{
g_{12}^TS_{12}g_{12}=S_{12}.
}
\]

Hence
\[
\boxed{
g_{12}\in SO(q_{12},\mathbb Z).
}
\]

---

## 50. Null rays equal eigenlines

**[D]**

The null equation
\[
q_{12}(x,y)=0
\]
has slopes
\[
\boxed{
\frac yx=-1\pm\sqrt3.
}
\]

These are exactly the two eigenlines of \(g_{12}\).

Thus
\[
\boxed{
\text{stable/unstable eigendirections}
=
\text{arithmetic null rays}.
}
\]

---

## 51. Exact Lorentz coordinates

**[D]**

Set
\[
U=2x-y,
\qquad
V=\sqrt3\,y.
\]

Then
\[
\boxed{
2q_{12}=U^2-V^2.
}
\]

Under the same change of basis,
\[
\boxed{
g_{12}
\sim
\begin{pmatrix}
2&\sqrt3\\
\sqrt3&2
\end{pmatrix}
=
\begin{pmatrix}
\cosh R_{12}&\sinh R_{12}\\
\sinh R_{12}&\cosh R_{12}
\end{pmatrix}.
}
\]

Therefore the Pell-unit action and the Cone's \(1+1\) Lorentz boost are
literally the same return in two coordinate systems.

In null coordinates
\[
\xi_\pm=U\pm V,
\]
\[
\boxed{
\xi_\pm\mapsto(2\pm\sqrt3)\xi_\pm
=
e^{\pm R_{12}}\xi_\pm.
}
\]

---

# PART XVII. RAMIFIED MOD-2 SHADOW

## 52. Norm form modulo \(2\)

**[D]**

Modulo \(2\),
\[
q_{12}(x,y)
=
2x^2-2xy-y^2
\equiv
y^2
\equiv y.
\]

Thus the discriminant-\(12\) Lorentz form degenerates at the ramified prime,
with radical/null line
\[
\boxed{y=0.}
\]

---

## 53. Return modulo \(2\)

**[D]**

\[
g_{12}
=
\begin{pmatrix}
3&1\\
2&1
\end{pmatrix}
\equiv
\boxed{
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}
}
\pmod2.
\]

Hence on
\[
\mathfrak p_2/2\mathfrak p_2
\cong(\mathbb F_2)^2,
\]
\[
\boxed{
(x,y)\mapsto(x+y,y).
}
\]

This is a nontrivial unipotent transvection, and
\[
\bar g_{12}^{\,2}=I.
\]

So the infinite-order hyperbolic return collapses at the ramified binary
boundary to an involutive Boolean shear.

---

## 54. Return and reversal coincide modulo \(2\)

**[D]**

The real Galois reverser
\[
Q=
\begin{pmatrix}
1&-1\\
0&-1
\end{pmatrix}
\]
satisfies
\[
\boxed{
Q\equiv g_{12}\pmod2.
}
\]

Thus on the binary quotient,
\[
\boxed{
\text{return}=\text{return reversal}.
}
\]

This is compatible with
\[
QgQ^{-1}=g^{-1}
\]
because
\[
\bar g^{-1}=\bar g
\]
in characteristic \(2\).

---

## 55. Boolean-cell bridge status

**[I/O]**

The arithmetic construction independently produces the natural four-point
state space
\[
\mathfrak p_2/2\mathfrak p_2\cong(\mathbb F_2)^2
\]
with an involutive shear.

The original factor cell is also a four-point Boolean torsor.

However, a canonical coordinate identification
\[
\boxed{
\mathfrak p_2/2\mathfrak p_2
\stackrel{?}{\cong}
\{(\epsilon_1,\epsilon_2)\}
}
\]
has not yet been derived.

This is now one of the cleanest remaining exact-bridge problems.

---

# PART XVIII. v13.127 ENDPOINT / ZERO-MEASURE RESULTS RETAINED

## 56. Arithmetic Fredholm Cone coordinates

**[D, retained]**

For the two positive endpoint resolvent channels
\[
q_\pm\ge0,
\]
set
\[
u=q_-,
\qquad
v=q_+.
\]

Then
\[
T_A=\frac{q_-+q_+}{2},
\qquad
X_A=\frac{q_--q_+}{2},
\qquad
Y_A=\sqrt{q_-q_+},
\]
and identically
\[
\boxed{
T_A^2-X_A^2-Y_A^2=0.
}
\]

This remains an exact arithmetic realization of the factor-to-Cone map.

The scalar endpoint weights are canonical; identification with a particular
quartet residue basis still requires the embedding map.

---

## 57. Endpoint phase/Clark versus metric multiplicity

**[Audit result retained from v13.127]**

The endpoint observables separate into linear and quadratic multiplicity
layers.

Phase winding and centered Clark mass converge to
\[
\boxed{
\sum_\gamma m_\gamma\delta_\gamma.
}
\]

The naturally renormalized shell metric converges, under the stated RH and
geometric continuation hypotheses, to
\[
\boxed{
(P_a*\nu_2)(y)\,dy,
\qquad
\nu_2=\sum_\gamma m_\gamma^2\delta_\gamma.
}
\]

Thus

\[
\boxed{
\begin{array}{c|c}
\text{observable}&\text{zero multiplicity}\\ \hline
\text{phase/Clark}&m_\gamma\\
\text{metric energy}&m_\gamma^2
\end{array}
}
\]

and these should not be forced into one normalization.

---

## 58. Poisson smoothing interpretation

**[D/I retained]**

With
\[
\widehat P_a(\xi)=e^{-a|\xi|},
\]
the metric endpoint measure is the Poisson-semigroup regularization
\[
\boxed{
P_a*\nu_2=e^{-a|D|}\nu_2.
}
\]

At simple zeros this smoothing is injective, but inverse recovery is
exponentially unstable and must be interpreted on a controlled test-function
class.

This remains a promising explicit-formula route, but no unconditional RH
conclusion follows from it.

---

# PART XIX. SUPERSEDED OR DOWNGRADED CLAIMS

## 59. Do not reuse the following without qualification

### 59.1 Custom coefficients

**[Superseded]**
\[
p_n=A_n(2)
\]
is false in general.

Correct:
\[
p_n=A_n(2)\quad(n\le5),
\]
then they diverge.

### 59.2 Generic residual boundary lemma

**[Superseded]**

Any bound omitting the boundary residual term \(r(t)\) is incomplete.

Use the corrected residual identity or, preferably, the finite even-Neumann
tail bound.

### 59.3 Literal source-channel shears

**[I]**

Do not claim Suzuki derives
\[
(\theta/2,\theta)
\]
as literal opposite \(SL_2\) shears.

The scalar channel decomposition is source-supported; the matrix assignment
is not.

### 59.4 Source-forced target \(\sigma=\theta\)

**[I/O]**

Do not claim Suzuki's formulas presently force
\[
\sigma_\theta(t)=\theta.
\]

### 59.5 Full first-chamber monotonicity

**[O]**

Current theorem:
\[
m_2'(t)>0
\quad(0<t\le0.30).
\]

Do not extend this to the chamber wall without a new certificate.

### 59.6 Boolean quotient identity

**[I]**

The arithmetic quotient
\[
\mathfrak p_2/2\mathfrak p_2
\]
is a natural four-state binary object, but is not yet canonically identified
with the original factor cell.

### 59.7 RH implications

**[Audit]**

The \(V_4\), critical-line fixed locus, cyclotomic field, discriminant \(12\),
Fredholm crossing, and arithmetic light-cone structures do not constitute an
RH proof.

Any RH-sensitive extension must retain the domain/circularity cautions from
v13.127.

---

# PART XX. CURRENT THEOREM MAP

## 60. Exact geometric/operator spine

\[
\boxed{
\text{factor cell}
\to
\text{Cone}
\to
V_4
\to
\text{complex quartet action}
}
\]

and independently

\[
\boxed{
(R,J,RJ)
\leftrightarrow
(T_5,T_{11},T_7).
}
\]

These are exact representation/action statements.

---

## 61. Exact \(\theta=2\) certified dynamic spine

The source/certificate chain establishes
\[
\boxed{
m_2(0)=1,
\qquad
m_2(1/5)>2+\sqrt3,
}
\]
and strict increase on the required crossing interval, hence
\[
\boxed{
\exists!\,t_*\in(0,1/5):
m_2(t_*)=2+\sqrt3.
}
\]

Equivalently,
\[
\boxed{
\sigma_2(t_*)=2.
}
\]

At this crossing,
\[
\boxed{
K=H^{-1}.
}
\]

---

## 62. Exact discriminant-\(12\) arithmetic spine

\[
\boxed{
\sigma=2
\to
\operatorname{tr}=4
\to
\Delta=12
\to
H_{12}^2=3I.
}
\]

Then
\[
\boxed{
\mathbb Z[H_{12}]
\cong
\mathcal O_{\mathbb Q(\sqrt3)}.
}
\]

On
\[
\boxed{
\mathfrak p_2=(2,\sqrt3-1),
}
\]
\[
\boxed{
H_{12}=\times\sqrt3,
\qquad
g_{12}=\times(2+\sqrt3).
}
\]

The primitive norm form is
\[
\boxed{
q_{12}(x,y)=2x^2-2xy-y^2,
}
\]
and
\[
\boxed{
g_{12}\in SO(q_{12},\mathbb Z).
}
\]

After
\[
(U,V)=(2x-y,\sqrt3 y),
\]
\[
\boxed{
2q_{12}=U^2-V^2
}
\]
and \(g_{12}\) is the pure Lorentz boost of rapidity
\[
R_{12}=\log(2+\sqrt3).
\]

---

## 63. Exact cyclotomic completion

\[
\boxed{
\mathcal Z=\frac{H_{12}+iI}{2}
}
\]
satisfies
\[
\boxed{
\Phi_{12}(\mathcal Z)=0,
\qquad
\mathcal Z^{12}=I.
}
\]

Thus
\[
\boxed{
\mathbb Q(\mathcal Z)
\cong
\mathbb Q(\zeta_{12}).
}
\]

The hyperbolic return is
\[
\boxed{
g_{12}
=
-i(I+\mathcal Z)(I-\mathcal Z)^{-1}.
}
\]

And
\[
\boxed{
2+\sqrt3
=
-i\frac{1+\zeta_{12}}{1-\zeta_{12}}
=
\cot\frac{\pi}{12}.
}
\]

Furthermore
\[
\boxed{
\mathbb Q(\zeta_{12})
=
H_{\mathbb Q(\sqrt3)}^+.
}
\]

---

## 64. Exact narrow-class / Suzuki conjugation bridge

\[
\boxed{
[\mathfrak p_2]
\in
\mathrm{Cl}^+(\mathbb Q(\sqrt3))
}
\]
is the unique nontrivial narrow class.

Artin reciprocity gives
\[
\boxed{
[\mathfrak p_2]
\mapsto
T_{11}
\leftrightarrow
J.
}
\]

Thus the same ideal that carries the Pell/Lorentz return also carries the
narrow-class element corresponding to the antiunitary Suzuki conjugation.

---

## 65. Ramified binary shadow

\[
\boxed{
\mathfrak p_2/2\mathfrak p_2
\cong
(\mathbb F_2)^2
}
\]
and
\[
\boxed{
\bar g_{12}
=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
}
\]

Thus the arithmetic return reduces to a Boolean involutive shear.

This is the current candidate for closing the loop back to the original
factor cell.

---

# PART XXI. THE MAIN STRUCTURAL GAP

## 66. What is already exact versus what is not

A large downstream chain is now exact:

\[
\boxed{
\sigma=2
\to
\Delta=12
\to
\mathbb Q(\sqrt3)
\to
\mathfrak p_2
\to
q_{12}
\to
\text{Lorentz boost}
}
\]

and

\[
\boxed{
H_{12}+iI
\to
\zeta_{12}
\to
H_F^+
\to
V_4.
}
\]

The certified Suzuki flow also reaches
\[
\boxed{\sigma_2(t_*)=2.}
\]

What is not yet exact is the upstream parameter-selection bridge
\[
\boxed{
\theta
\stackrel{?}{=}
\sigma_\theta(t).
}
\]

Therefore the project should not say “Suzuki forces \(\theta=2\)” in the
strong source-theorem sense.

The defensible current statement is:

> The \(\theta=2\) Suzuki determinant flow is rigorously shown to hit the
> unique centered-Cayley self-reciprocal shear class \(\sigma=2\). Once that
> class is reached, the entire discriminant-\(12\), Pell, Lorentz,
> cyclotomic, narrow-class, and \(V_4\) arithmetic package follows exactly.

---

# PART XXII. HIGH-VALUE OPEN PROBLEMS

## 67. Priority A — close the Boolean loop

**[O]**

Determine whether there is a canonical identification
\[
\mathfrak p_2/2\mathfrak p_2
\cong
\{(\epsilon_1,\epsilon_2)\}
\]
that transports the arithmetic transvection and cyclotomic/narrow
involutions to the original cell generators
\[
F_1,F_2.
\]

A successful result would close
\[
\boxed{
\text{Boolean cell}
\to
\text{Cone}
\to
\Delta=12
\to
\text{Pell ideal}
\to
\text{cyclotomic }V_4
\to
\text{Boolean cell}.
}
\]

---

## 68. Priority B — source-internal meaning of \(\sigma=\theta\)

**[O]**

Seek a source-side invariant whose natural value is both

- Suzuki's parameter \(\theta\), and
- the determinant transfer trace defect
  \[
  \sigma=m+m^{-1}-2.
  \]

Possible routes include transfer matrices, continued fractions, canonical
system monodromy, or a normalized first-cumulant/Cayley invariant.

Do not force a literal opposite-shear interpretation unless the source
provides a canonical \(2\times2\) factorization.

---

## 69. Priority C — relate the ramified ideal to the original quarter/half shifts

**[O/I]**

The integral cyclotomic closure requires
\[
\frac{H+iI}{2}.
\]

The project independently contains canonical half-centering and quarter-shift
structures.

Investigate whether these are manifestations of the same integral gluing
mechanism.

At present this is suggestive, not proved.

---

## 70. Priority D — paper integration

**[O editorial]**

The new exact arithmetic chain is strong enough to affect Papers B/C and the
null-cone/band-area material.

Recommended future paper architecture:

1. foundational factor/Cone geometry;
2. exact \(V_4\) action and labeling distinction;
3. discriminant-\(12\) centered return;
4. Pell ideal and arithmetic norm cone;
5. cyclotomic integral gluing and Cayley return;
6. Suzuki operator \(V_4\) representation;
7. certified \(\theta=2\) determinant crossing;
8. explicit statement of the remaining upstream identification gap.

Avoid presenting the arithmetic completion as evidence for RH.

---

# PART XXIII. CURRENT NUMERICAL/CERTIFICATE INDEX

## 71. Core certified values

\[
\boxed{
t_*\approx0.1916605
}
\]
with
\[
\boxed{
m_2(t_*)=2+\sqrt3.
}
\]

At \(t=1/5\),
\[
\boxed{
m_2(1/5)>3.786007338662927.
}
\]

Full first chamber:
\[
\boxed{
\|K_2[t]\|<0.999398246164<1,
\quad
0<t<\log2/2.
}
\]

Kernel positivity:
\[
\boxed{
g_2(x)>0,
\quad
0<x\le0.51.
}
\]

Monotonicity:
\[
\boxed{
m_2'(t)>0,
\quad
0<t\le0.30.
}
\]

These should be treated separately:
full-chamber contraction is proved farther than full-chamber monotonicity.

---

# PART XXIV. DO-NOT-ACCIDENTALLY-CLAIM LIST

## 72. Publication guardrails

Do **not** claim:

1. that the shell \(V_4\) proves RH;
2. that Suzuki's published contraction theorem directly covers every
   RH-sensitive small-\(\omega\) quartet regime;
3. that the custom \(p_n\) are Suzuki's \(A_n(2)\);
4. that the old residual lemma without \(r(t)\) is valid;
5. that full first-chamber monotonicity is proved;
6. that Suzuki literally derives two opposite unipotent shears;
7. that the source itself forces \(\sigma_\theta(t)=\theta\);
8. that the arithmetic binary quotient has already been canonically
   identified with the original Boolean cell;
9. that the class-field/cyclotomic completion has any direct implication for
   zeta zero location.

Do claim, with the appropriate hypotheses/status:

1. exact Cone/Boolean \(V_4\) geometry;
2. exact Suzuki operator \(V_4\) representation;
3. exact complex-compatible Galois matching;
4. certified \(\theta=2\) first-chamber crossing;
5. exact full first-chamber contraction;
6. exact centered-Cayley self-reciprocity at \(\sigma=2\);
7. exact discriminant-\(12\) quadratic order;
8. exact Pell-ideal realization of \(g_{12}\);
9. exact arithmetic norm light cone and Lorentz boost;
10. exact primitive \(12\)th-root operator \(\mathcal Z\);
11. exact cyclotomic Cayley transform of the return;
12. exact narrow Hilbert class-field description;
13. exact Artin identification
    \[
    [\mathfrak p_2]\leftrightarrow T_{11}\leftrightarrow J;
    \]
14. exact ramified mod-\(2\) transvection.

---

# PART XXV. v13.162 CHECKPOINT

## 73. Consolidated structural statement

The project now contains an exact downstream arithmetic-geometric package
centered on the certified \(\theta=2\) determinant crossing.

At the certified point
\[
t_*\in(0,1/5),
\]
\[
m_2(t_*)=2+\sqrt3
\]
and therefore
\[
\sigma_2(t_*)=2.
\]

The value \(\sigma=2\) is exactly the unique centered-Cayley
self-reciprocal class:
\[
K=H^{-1}.
\]

Its monic return is
\[
g_{12}
=
\begin{pmatrix}
3&1\\
2&1
\end{pmatrix},
\]
with
\[
\Delta=12,
\qquad
H_{12}^2=3I.
\]

The centered generator produces the maximal real quadratic order
\[
\mathcal O_{\mathbb Q(\sqrt3)}.
\]

On the ramified ideal
\[
\mathfrak p_2=(2,\sqrt3-1),
\]
the return is literal multiplication by
\[
2+\sqrt3.
\]

The associated primitive norm form
\[
q_{12}=2x^2-2xy-y^2
\]
is a discriminant-\(12\) arithmetic light cone, and the return is its integral
Lorentz boost.

Adjoining the analytic complex structure through
\[
\mathcal Z=\frac{H_{12}+iI}{2}
\]
produces a primitive twelfth root:
\[
\Phi_{12}(\mathcal Z)=0.
\]

The return is the Cayley image of this cyclotomic generator:
\[
g_{12}
=
-i(I+\mathcal Z)(I-\mathcal Z)^{-1}.
\]

The cyclotomic field is the narrow Hilbert class field
\[
\mathbb Q(\zeta_{12})
=
H_{\mathbb Q(\sqrt3)}^+,
\]
and the unique nontrivial narrow class
\[
[\mathfrak p_2]
\]
maps by Artin reciprocity to
\[
T_{11},
\]
which is exactly the Suzuki antiunitary conjugation element \(J\).

Finally, reducing the same return lattice at the ramified prime produces
\[
\mathfrak p_2/2\mathfrak p_2
\cong(\mathbb F_2)^2
\]
with Boolean transvection
\[
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
\]

Thus the current exact downstream spine is

\[
\boxed{
\begin{aligned}
&\sigma=2
\to
\Delta=12
\to
H^2=3I
\to
\mathbb Q(\sqrt3)
\to
\mathfrak p_2
\to
q_{12}
\to
\text{Lorentz boost},\\
&\hspace{22mm}
\downarrow\\
&\mathcal Z=\frac{H+iI}{2}
\to
\mathbb Q(\zeta_{12})
=
H_F^+
\to
V_4
\to
(\mathbb F_2)^2.
\end{aligned}
}
\]

The two principal unclosed bridges are now sharply isolated:

\[
\boxed{
\text{source parameter }\theta
\stackrel{?}{\longrightarrow}
\text{dynamic shear }\sigma
}
\]

and

\[
\boxed{
\mathfrak p_2/2\mathfrak p_2
\stackrel{?}{\longrightarrow}
\text{original Boolean factor cell}.
}
\]

Everything between those two bridges is substantially more rigid and exact
than it appeared at v13.127.

---

---

# PART XXVI. THE RAMIFIED BOOLEAN RETURN

## 74. The cycle-type obstruction

**[D/Audit]** Let

\[
V_2=\mathfrak p_2/2\mathfrak p_2\cong(\mathbb F_2)^2
\]

and let the reduced arithmetic return be

\[
\bar g(x,y)=(x+y,y).
\]

As a permutation of the four points, \(\bar g\) fixes the line \(y=0\):

\[
(0,0)\mapsto(0,0),
\qquad
(1,0)\mapsto(1,0),
\]

and exchanges

\[
(0,1)\longleftrightarrow(1,1).
\]

Its cycle type is therefore

\[
\boxed{1^2,2^1.}
\]

By contrast, every nonidentity element of the translation torsor generated by
the bit flips \(F_1,F_2\) has no fixed points and cycle type

\[
\boxed{2^2.}
\]

Cycle type is invariant under every bijective relabeling.  Consequently there
is no identification of the four state sets for which

\[
\boxed{
\bar g=F_1,
\qquad
\bar g=F_2,
\qquad\text{or}\qquad
\bar g=F_1F_2.
}
\]

Thus the original formulation of Priority A—transporting the arithmetic
transvection to a nontrivial generator of the Boolean translation \(V_4\)—is
impossible.  This is a structural obstruction, not a missing choice of basis.

## 75. The correct Boolean involution is factor exchange

**[D]** The factor cell has another natural symmetry:

\[
P:(\epsilon_1,\epsilon_2)mapsto(\epsilon_2,\epsilon_1).
\]

It fixes the equal-bit states

\[
(0,0),\qquad(1,1)
\]

and exchanges the unequal-bit pair

\[
(0,1)\longleftrightarrow(1,0).
\]

Hence \(P\) has the same cycle type \(1^2 2^1\) as \(\bar g\).

Using the ideal basis

\[
e=2,
\qquad
f=\sqrt3-1,
\]

write a class of \(V_2\) as \((x,y)=xe+yf\).  Define

\[
\boxed{
\Phi(x,y)=(\epsilon_1,\epsilon_2)=(x,x+y).
}
\]

Then

\[
\begin{array}{c|c}
V_2&\text{factor cell}\\ \hline
0&(0,0)\\
e&(1,1)\\
f&(0,1)\\
e+f&(1,0)
\end{array}
\]

and direct substitution gives

\[
\boxed{
\Phi\bar g\Phi^{-1}=P.
}
\]

Indeed,

\[
\Phi(x+y,y)=(x+y,x)=P(x,x+y).
\]

The ramified arithmetic return therefore comes back to the Boolean cell as
**factor exchange**, not as a bit translation.

## 76. The reduced norm form becomes XOR parity

**[D]** Section 52 gives

\[
\bar q_{12}(x,y)=y.
\]

Under \(\Phi\),

\[
y=\epsilon_1+\epsilon_2
=
\epsilon_1\oplus\epsilon_2.
\]

Therefore

\[
\boxed{
\bar q_{12}
=
\epsilon_1\oplus\epsilon_2.
}
\]

The radical line \(y=0\) maps exactly to the equal-bit sector,

\[
\{0,e\}
\stackrel{\Phi}{\longmapsto}
\{(0,0),(1,1)\},
\]

while its complementary coset maps to the unequal-bit sector,

\[
\{f,e+f\}
\stackrel{\Phi}{\longmapsto}
\{(0,1),(1,0)\}.
\]

This is the strongest part of the bridge.  The degenerate arithmetic norm does
not merely supply a four-point set; it recovers the Boolean equality/XOR
partition that underlies the compact/noncompact sign split of the original
cell.

Characteristic two forgets the real sign itself, but retains the parity flag:

\[
\boxed{
\text{equal bits}\leftrightarrow \bar q_{12}=0,
\qquad
\text{unequal bits}\leftrightarrow \bar q_{12}=1.
}
\]

## 77. Canonicity and the remaining twofold ambiguity

**[D/Audit]** Requiring all three properties

1. \(0\mapsto(0,0)\);
2. \(\bar q_{12}\mapsto\epsilon_1\oplus\epsilon_2\);
3. \(\bar g\mapsto P\);

determines \(\Phi\) up to postcomposition by \(P\).  Equivalently, the two
allowed maps differ only by interchanging the two factor labels.

This is exactly the unavoidable symmetry of an unordered factor pair.  Hence:

\[
\boxed{
\text{for unordered factors, the bridge is canonical};
}
\]

\[
\boxed{
\text{for ordered factors, one orientation choice remains}.
}
\]

No stronger labeling should be claimed unless an upstream construction
distinguishes the first factor from the second.

## 78. The Boolean symmetry group must be enlarged

**[D/I]** The translations \(F_1,F_2\) generate the regular Klein four group

\[
V_4^{\rm tr}\cong(\mathbb F_2)^2.
\]

Factor exchange satisfies

\[
PF_1P^{-1}=F_2,
\qquad
PF_2P^{-1}=F_1.
\]

Therefore

\[
\boxed{
\langle F_1,F_2,P\rangle
=
V_4^{\rm tr}\rtimes C_2
\cong D_8.
}
\]

The arithmetic transvection occupies the stabilizer/reflection part of this
affine symmetry group, not its translation subgroup.  The corrected return
diagram is therefore

\[
\boxed{
\text{Boolean cell}
\to
\text{Cone/arithmetic return}
\to
\mathfrak p_2/2\mathfrak p_2
\xrightarrow{\ \Phi\ }
\text{Boolean factor exchange}.
}
\]

The original translation \(V_4\) and the returned reflection together form a
natural dihedral completion.  They must not be identified elementwise.

## 79. Effect on the cyclotomic and narrow-class bridge

**[Audit/I/O]** The conclusions

\[
[\mathfrak p_2]\longleftrightarrow T_{11}\longleftrightarrow J
\]

and

\[
\operatorname{Gal}(\mathbb Q(\zeta_{12})/\mathbb Q)\cong V_4
\]

remain exact.  What changes is the proposed last arrow back to the original
cell: the reduced Pell return is not one of the three nontrivial translations
of that cell.

The arithmetic quotient now carries two conceptually different symmetry
layers:

\[
\boxed{
\begin{array}{ccl}
\text{cyclotomic }V_4&:&\text{field/Galois sign actions},\\
\text{ramified return }\bar g&:&\text{factor-exchange reflection}.
\end{array}
}
\]

A future theorem may embed both layers into a common affine action, but the
present audit does not identify the Artin element itself with \(P\).  Equality
of their order or their appearance in the same arithmetic package is
insufficient.

## 80. Priority A resolved in corrected form

The original strong target

\[
\bar g\stackrel{?}{\longleftrightarrow}F_i
\]

has a definitive negative answer by cycle type.  The corrected target has an
exact positive answer:

\[
\boxed{
(V_2,\bar q_{12},\bar g)
\cong
\bigl((\mathbb F_2)^2,
\epsilon_1\oplus\epsilon_2,
P\bigr)
}
\]

canonically up to exchange of the two factor labels.

Thus the Boolean loop closes at the level of

\[
\boxed{
\text{state space}
+
\text{equality/XOR partition}
+
\text{factor-exchange involution},
}
\]

but not as an identification of the arithmetic return with the translation
generators \(F_1,F_2\).

## 81. v13.163 checkpoint

The ramified discriminant-(12\) lattice returns to the original Boolean cell
more rigidly than §55 established, but differently than §67 anticipated.

With

\[
\Phi(x,y)=(x,x+y),
\]

one has simultaneously

\[
\boxed{
\bar q_{12}=y
\longleftrightarrow
\epsilon_1\oplus\epsilon_2,
}
\]

and

\[
\boxed{
\bar g:(x,y)\mapsto(x+y,y)
\longleftrightarrow
P:(\epsilon_1,\epsilon_2)\mapsto(\epsilon_2,\epsilon_1).
}
\]

The equal-bit states are the radical/fixed line; the unequal-bit states are
the exchanged coset.  The identification is unique up to the physically
expected exchange of factor labels.

This resolves the highest-priority Boolean bridge while imposing a necessary
scope correction: the returned involution belongs to the dihedral extension

\[
V_4^{\rm tr}\rtimes C_2\cong D_8,
\]

not to the translation \(V_4\) itself.

The next highest-value target is now Priority B: determine whether the source
determinant flow contains a canonical invariant equating Suzuki's parameter
\(\theta\) with the dynamic trace defect

\[
\sigma=m+m^{-1}-2,
\]

or prove that the observed equality at \(\theta=2\) is a distinguished
crossing rather than an identity.

---

**End of v13.163 audited consolidation continuation.**
