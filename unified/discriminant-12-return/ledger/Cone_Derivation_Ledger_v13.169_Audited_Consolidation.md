# Cone Project — Derivation Ledger v13.169

**Version:** 13.169 — audited consolidation continuation  
**Date:** 2026-09-03  
**Consolidates:** v13.127 audited baseline together with the audited/corrected developments through v13.169.  
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

---

# PART XXVII. SOURCE PARAMETER VERSUS DYNAMIC SHEAR

## 82. The proposed equality is not a flow identity

**[D/Audit]** For fixed source parameter \(\theta>1\), the audited small-\(t\)
asymptotic is

\[
q_\theta(t):=\log m_\theta(t)
=
\frac{(4\pi t)^\theta}{\Gamma(\theta+1)}
+O(t^{\theta+1}),
\]

and hence

\[
\sigma_\theta(t)
=
m_\theta(t)+m_\theta(t)^{-1}-2
=
\frac{(4\pi t)^{2\theta}}{\Gamma(\theta+1)^2}
+O(t^{2\theta+1}).
\]

Therefore

\[
\boxed{
\lim_{t\downarrow0}\sigma_\theta(t)=0.
}
\]

Since \(\theta>0\) is fixed and nonzero,

\[
\boxed{
\sigma_\theta(t)=\theta
}
\]

cannot hold identically along the determinant flow.  The equality is
necessarily a level-crossing condition in \(t\), not a source identity.

This resolves the main logical ambiguity in §§32--33 and Priority B.

## 83. Exact target value for arbitrary \(\theta\)

**[D]** The matching equation

\[
\sigma=m+m^{-1}-2=\theta
\]

is equivalent to

\[
m^2-(\theta+2)m+1=0.
\]

Its reciprocal roots are

\[
\boxed{
m_\pm(\theta)
=
\frac{\theta+2\pm\sqrt{\theta^2+4\theta}}{2}.
}
\]

On the positive hyperbolic branch \(m\ge1\), the target is

\[
\boxed{
m_{\rm tar}(\theta)
=
\frac{\theta+2+\sqrt{\theta^2+4\theta}}{2}.
}
\]

Equivalently, writing \(m=e^q\),

\[
\boxed{
q_{\rm tar}(\theta)
=
\operatorname{arcosh}\!\left(1+\frac\theta2\right)
=
2\operatorname{arsinh}\!\left(\frac{\sqrt\theta}{2}\right).
}
\]

At \(\theta=2\),

\[
m_{\rm tar}(2)=2+\sqrt3,
\qquad
q_{\rm tar}(2)=\log(2+\sqrt3).
\]

Thus the Pell unit is the exact \(\theta=2\) member of a universal target
curve; it is not produced by a general identity \(m_\theta(t)=m_{\rm tar}(\theta)\).

## 84. Canonical scalar matching formulation

**[D/I]** The determinant transfer supplies the intrinsic scalar

\[
K_\sigma H_\sigma=\frac\sigma2 I.
\]

The source coefficient expansion independently supplies

\[
\alpha_\theta=\frac\theta2.
\]

Therefore the most economical bridge is the scalar matching equation

\[
\boxed{
K_{\sigma_\theta(t)}H_{\sigma_\theta(t)}
=
\alpha_\theta I.
}
\]

It is exactly equivalent to

\[
\boxed{\sigma_\theta(t)=\theta.}
\]

Both sides are canonical after their respective normalizations have been
fixed: the left side is a centered-Cayley invariant of the dynamic transfer,
and the right side is the first scalar channel in Suzuki's source expansion.

**Audit:** their equality is a natural comparison condition, but no source
theorem currently forces the determinant trajectory to be evaluated at that
condition.  “Canonical quantities can be compared” is weaker than “the source
canonically identifies them.”

## 85. The apparent three-channel agreement has rank one

**[D/Audit]** The source scalars satisfy identically

\[
\beta_\theta=2\alpha_\theta,
\qquad
-A_1(\theta)=\alpha_\theta+\beta_\theta=3\alpha_\theta.
\]

On the dynamic side,

\[
2K_\sigma H_\sigma=\sigma I,
\qquad
3K_\sigma H_\sigma=\frac{3\sigma}{2}I.
\]

Consequently the three equations

\[
K_\sigma H_\sigma=\alpha_\theta I,
\]

\[
2K_\sigma H_\sigma=\beta_\theta I,
\]

and

\[
3K_\sigma H_\sigma=-A_1(\theta)I
\]

are all the same single equation \(\sigma=\theta\).

Hence

\[
\boxed{
\text{the coefficient triple supplies one matching condition, not three
independent confirmations.}
}
\]

This removes a potential overcounting of evidence while preserving the exact
scalar correspondence.

## 86. The certified \(\theta=2\) result is a unique matching time

**[D + N-cert]** Define

\[
F_\theta(t)=\sigma_\theta(t)-\theta.
\]

For \(\theta=2\),

\[
F_2(0)=-2.
\]

The certified inequality

\[
m_2(1/5)>2+\sqrt3
\]

implies

\[
F_2(1/5)>0.
\]

The certified strict increase of \(m_2\) on the crossing interval implies
strict increase of \(\sigma_2\), because for \(m>1\),

\[
\frac{d\sigma}{dm}=1-m^{-2}>0.
\]

Therefore

\[
\boxed{
\exists!\,t_*\in(0,1/5):
K_{\sigma_2(t_*)}H_{\sigma_2(t_*)}=\alpha_2 I=I.
}
\]

Numerically,

\[
t_*\approx0.1916605.
\]

The certified theorem is thus best named the **unique first-channel matching
crossing** of the \(\theta=2\) determinant flow.

## 87. Why self-reciprocity selects \(2\) only after matching

**[D/Audit]** Centered-Cayley self-reciprocity is the state-space condition

\[
K_\sigma=H_\sigma^{-1},
\]

which is equivalent to

\[
\sigma=2.
\]

Source matching is the separate condition

\[
\sigma=\theta.
\]

Their intersection is

\[
\boxed{
\sigma=\theta=2.
}
\]

Therefore the exact logical chain is

\[
\boxed{
\text{source matching}
+
\text{centered-Cayley self-reciprocity}
\Longrightarrow
\theta=2.
}
\]

Self-reciprocity alone selects the dynamic conjugacy class \(\sigma=2\), not
the source-family parameter.  The parameter \(\theta=2\) follows only after
the independent matching condition is imposed.

## 88. A matching curve, not a parameter identity

**[D/O]** For any \(\theta\) for which the positive determinant flow reaches
\(m_{\rm tar}(\theta)\), define a matching time

\[
t_\theta
=
\inf\{t>0:\sigma_\theta(t)=\theta\}.
\]

Where strict monotonicity holds, this crossing is unique.  Under sufficient
joint smoothness in \((\theta,t)\) and transversality

\[
\partial_t\sigma_\theta(t_\theta)\ne0,
\]

the implicit-function theorem gives a local matching curve, with

\[
\boxed{
t_\theta'
=
\frac{1-\partial_\theta\sigma_\theta(t_\theta)}
{\partial_t\sigma_\theta(t_\theta)}.
}
\]

Only the point \((\theta,t)=(2,t_*)\) is presently certified.  Establishing a
larger matching curve requires new uniform control of the \(\theta\)-dependent
kernel and must not be inferred from the \(\theta=2\) calculation.

## 89. Source-side status after the audit

**[Audit]** Priority B now separates into a resolved statement and a remaining
interpretive question.

Resolved exactly:

\[
\boxed{
\sigma_\theta(t)=\theta
\text{ is a distinguished crossing condition, not an identity of the flow.}
}
\]

Resolved at \(\theta=2\): the crossing exists uniquely in the certified
interval and coincides with the unique self-reciprocal dynamic class.

Still open: whether the source construction contains an additional principle
that instructs us to select the first-channel matching locus.  Candidate
principles may involve a normalized monodromy, transfer/cumulant matching, or
a variational condition, but none has yet been derived.

The safe statement is:

> Suzuki's \(\theta=2\) determinant flow has a unique certified time at which
> its centered-Cayley scalar equals the source first channel.  At that same
> time the dynamic transfer is self-reciprocal, and the exact
> discriminant-\(12\) arithmetic package follows.

## 90. Consequence for the project architecture

The two former main gaps have now changed status:

\[
\begin{array}{c|c}
\text{former gap}&\text{v13.164 result}\\ \hline
\mathfrak p_2/2\mathfrak p_2\to\text{Boolean cell}
&
\text{exact up to factor exchange; return maps to }P\\
\theta\stackrel{?}{=}\sigma_\theta(t)
&
\text{not an identity; exact scalar matching locus}
\end{array}
\]

The remaining conceptual hinge is no longer an algebraic identification.  It
is a **selection principle**: why should the physical/source construction
choose the matching time \(t_\theta\)?

This is a much narrower and more honest target than attempting to prove a
global equality between a family parameter and a dynamical state variable.

## 91. v13.164 checkpoint

The dynamic trace defect begins at zero:

\[
\sigma_\theta(t)
=
\frac{(4\pi t)^{2\theta}}{\Gamma(\theta+1)^2}
+O(t^{2\theta+1}),
\]

so it cannot identically equal the fixed source parameter \(\theta\).

The correct bridge is the level-matching equation

\[
\boxed{
K_\sigma H_\sigma=\alpha_\theta I
\iff
\sigma=\theta.
}
\]

At \(\theta=2\), the certified flow crosses this level exactly once:

\[
\boxed{
m_2(t_*)=2+\sqrt3,
\qquad
\sigma_2(t_*)=2,
\qquad
K_2=H_2^{-1}.
}
\]

The coefficient relations involving \(\alpha_\theta\), \(\beta_\theta\), and
\(A_1(\theta)\) are three forms of this one condition, not independent
evidence.

Priority B is therefore resolved at the algebraic/audit level: the observed
equality is a distinguished unique crossing, not a flow identity.  What
remains open is the source-internal principle, if any, that selects that
crossing.

The next high-value target is Priority C: determine whether the denominator
\(2\) in the integral cyclotomic gluing

\[
\mathcal Z=\frac{H+iI}{2}
\]

is canonically the same two-adic/centering mechanism as the original
half-step and quarter-shift structures, or only a numerically similar
normalization.

---

---

# PART XXVIII. DYADIC CYCLOTOMIC GLUING AND THE QUARTER

## 92. Three half-operations must be distinguished

**[Audit]** The project contains three exact appearances of a half:

\[
\begin{array}{c|c|c}
\text{construction}&\text{half-operation}&\text{ambient object}\\ \hline
\text{factor cell}&(p,q)\mapsto(p+\tfrac12,q+\tfrac12)
&\text{affine lattice cell}\\
\text{rank-one Casimir}&j\mapsto j+\tfrac12
&\text{weight coordinate}\\
\text{cyclotomic closure}&(H,iI)\mapsto\tfrac12(H+iI)
&\text{order in a number field}
\end{array}
\]

Each produces a quarter after a quadratic operation, but they are not
automatically the same map.  A literal identification requires an
intertwiner between the corresponding affine, representation, and arithmetic
lattices.

The purpose of Priority C is therefore not to merge the three constructions
by numerical equality, but to determine the exact common structure and the
remaining obstruction.

## 93. The cyclotomic denominator represents an index-four closure

**[D]** Let

\[
F=\mathbb Q(\sqrt3),
\qquad
K=F(i)=\mathbb Q(\zeta_{12}),
\]

and define the naive product order

\[
\mathcal O_0=\mathbb Z[\sqrt3,i].
\]

The maximal order has integral basis

\[
\boxed{
1,\quad
\zeta_{12}=\frac{\sqrt3+i}{2},\quad
\zeta_{12}^2=\frac{1+i\sqrt3}{2},\quad
i.
}
\]

Relative to the product basis

\[
1,\sqrt3,i,i\sqrt3,
\]

the change-of-basis determinant has absolute value \(1/4\).  Hence

\[
\boxed{
[\mathcal O_K:\mathcal O_0]=4.
}
\]

The denominator \(2\) does not describe a single index-two enlargement.
There are two independent coupled parity channels, and together they produce
an index-four integral closure.

## 94. Exact parity description of the integral closure

**[D]** Every element of \(\mathcal O_K=\mathbb Z[\zeta_{12}]\) can be written

\[
\frac{A+B\sqrt3+i(C+D\sqrt3)}{2},
\qquad A,B,C,D\in\mathbb Z,
\]

subject exactly to

\[
\boxed{
A\equiv D\pmod2,
\qquad
B\equiv C\pmod2.
}
\]

Indeed, for

\[
n_0+n_1\zeta_{12}+n_2\zeta_{12}^2+n_3i,
\]

the numerator coordinates are

\[
A=2n_0+n_2,
\quad
B=n_1,
\quad
C=n_1+2n_3,
\quad
D=n_2.
\]

Conversely, the two parity conditions reconstruct integral \(n_0,n_3\).

Modulo the product order, the allowed numerator parities form the four-word
code

\[
\boxed{
\mathcal C_{m glue}
=
\{(d,b,b,d):b,d\in\mathbb F_2\}
\cong(\mathbb F_2)^2.
}
\]

Thus

\[
\boxed{
\mathcal O_K/\mathcal O_0
\cong(\mathbb Z/2\mathbb Z)^2.
}
\]

The cyclotomic half-sum therefore carries a genuine four-state Boolean
gluing structure, not merely a visual midpoint analogy.

## 95. Two half-generators and one ring generator

**[D]** Additively, the two nontrivial half-directions may be represented by

\[
\zeta_{12}
=
\frac{\sqrt3+i}{2},
\qquad
\zeta_{12}^2
=
\frac{1+i\sqrt3}{2}.
\]

Their residue classes generate

\[
\mathcal O_K/\mathcal O_0\cong(\mathbb F_2)^2.
\]

Multiplicatively, however, the single primitive element \(\zeta_{12}\)
generates the whole ring because its square supplies the second additive
half-direction.

This resolves an apparent tension:

\[
\boxed{
\text{one cyclotomic ring generator}
\quad\text{but}\quad
\text{two independent additive parity gluings}.
}
\]

The index \(4\) is therefore fully compatible with adjoining the single
element \((\sqrt3+i)/2\).

## 96. The quarter is forced by relative-norm normalization

**[D]** At the discriminant-(12\) point,

\[
H^2=3I,
\qquad
(iI)^2=-I.
\]

Therefore

\[
(H+iI)(H-iI)=H^2+I=4I.
\]

For

\[
\mathcal Z=\frac{H+iI}{2},
\qquad
\mathcal Z^{-1}=\frac{H-iI}{2},
\]

we obtain

\[
\boxed{
\mathcal Z\mathcal Z^{-1}
=
\frac{H^2+I}{4}
=I.
}
\]

Thus the denominator-square

\[
\boxed{\frac14}
\]

is forced: it converts the relative norm \(4\) of the numerator into the
unit norm of the primitive twelfth root.

In scalar form,

\[
\left|\frac{\sqrt3+i}{2}\right|^2
=
\frac{3+1}{4}=1.
\]

This is an exact arithmetic realization of the general pattern

\[
\boxed{
\text{half-normalization}
\longrightarrow
\text{quarter in the quadratic invariant}.
}
\]

## 97. What is genuinely common with the Casimir quarter

**[D/I]** The Casimir completion is

\[
j(j+1)+\frac14
=
\left(j+\frac12\right)^2.
\]

The cyclotomic normalization is

\[
\frac{H^2+I}{4}=I
\qquad(H^2=3I).
\]

Both are instances of a half-coordinate becoming a quarter under a quadratic
operation.  Both also remove a cross-term or norm defect by passing from an
uncentered/incomplete expression to a normalized square or unit.

The exact shared abstraction is therefore:

\[
\boxed{
\text{a dyadic affine shift or gluing element whose quadratic refinement
contains }\frac14.
}
\]

But the quadratic forms differ:

- the Casimir quarter belongs to the rank-one weight polynomial;
- the cyclotomic quarter belongs to the relative norm from \(K/F\);
- the factor-cell quarter belongs to the centered Lorentz displacement.

No equality of operators or lattices follows from the common scalar.

## 98. The gluing quotient is Boolean but not the Galois (V_4)

**[D/Audit]** The additive quotient

\[
\mathcal O_K/\mathcal O_0\cong(\mathbb F_2)^2
\]

has four elements.  Nevertheless the cyclotomic Galois action becomes
trivial on this quotient.

Indeed, modulo \(\mathcal O_0\),

\[
T_a(\zeta_{12})=\zeta_{12}^a
\equiv\zeta_{12}
\qquad(a=1,5,7,11),
\]

and similarly

\[
T_a(\zeta_{12}^2)\equiv\zeta_{12}^2.
\]

The signs and integral translations distinguishing the four Galois
automorphisms disappear modulo the exponent-two gluing quotient.

Hence

\[
\boxed{
\text{four additive gluing classes}
\neq
\text{four nontrivial Galois actions}.
}
\]

This is the same kind of layer distinction already required for the Boolean
translation \(V_4\), the cyclotomic Galois \(V_4\), and the ramified factor
exchange.

## 99. Relation to the ramified Boolean return

**[D/I/O]** Two natural dyadic four-state spaces now occur:

\[
\mathcal O_K/\mathcal O_0
\cong(\mathbb F_2)^2,
\]

and

\[
\mathfrak p_2/2\mathfrak p_2
\cong(\mathbb F_2)^2.
\]

The first records the two parity obstructions repaired by integral
cyclotomic gluing.  The second records the ramified reduction of the Pell
return lattice and carries the nontrivial factor-exchange transvection found
in v13.163.

Their equality of cardinality and characteristic is exact but does not alone
supply a canonical isomorphism.  In particular:

\[
\boxed{
\text{Galois acts trivially on the gluing quotient},
\qquad
\bar g\text{ acts nontrivially on the ideal quotient}.
}
\]

Any future identification must explain this action mismatch, rather than
matching the two four-point sets arbitrarily.

## 100. Priority C audit verdict

Priority C has a mixed but sharp answer.

Exact positive result:

\[
\boxed{
\frac12(H+iI)
\text{ is the integral two-adic gluing element, and }
\frac14
\text{ is forced by its unit norm.}
}
\]

The integral closure has a canonical Boolean parity code

\[
\boxed{
\mathcal C_{\rm glue}
=
\{(d,b,b,d)\}
\cong(\mathbb F_2)^2.
}
\]

Scope limitation:

\[
\boxed{
\text{cyclotomic gluing quarter}
\neq
\text{Casimir or cell quarter as a literal operator identity}.
}
\]

What is common is the dyadic quadratic-refinement mechanism.  What remains
unproved is a canonical intertwiner identifying the three underlying
lattices and their quadratic forms.

Thus the earlier phrase “the same integral gluing mechanism” is too strong
if interpreted literally, but correct at the abstract level

\[
\boxed{
\text{half-element}
\longmapsto
\text{quarter-normalized quadratic invariant}.
}

## 101. Revised architecture of the half/quarter sector

The project now has the following audited hierarchy:

\[
\begin{array}{c|c|c}
\text{layer}&\text{exact statement}&\text{status of cross-layer map}\\ \hline
\text{factor cell}
&\delta/2\mapsto\delta^2/4
&\text{normalization match}\\
\text{rank-one representation}
&j+1/2\mapsto j(j+1)+1/4
&\text{shared shifted-square form}\\
\text{cyclotomic order}
&(H+iI)/2\mapsto(H^2+I)/4=I
&\text{exact two-adic gluing}\\
\text{ramified ideal}
&\bar q_{12}=\epsilon_1\oplus\epsilon_2
&\text{exact Boolean return up to exchange}
\end{array}
\]

The numerical quarter is no longer merely recurrent.  It has three exact
quadratic realizations.  The audit still forbids collapsing them into one
universal scalar operator.

## 102. v13.165 checkpoint

The cyclotomic half-element

\[
\mathcal Z=\frac{H+iI}{2}
\]

is integral because it repairs two coupled parity defects in the product
order.  Additively,

\[
\boxed{
\mathcal O_{\mathbb Q(\zeta_{12})}/
\mathbb Z[\sqrt3,i]
\cong(\mathbb F_2)^2.
}
\]

Its quarter is forced by

\[
\boxed{
(H+iI)(H-iI)=4I.
}
\]

Therefore the cyclotomic construction and the earlier half-step/Casimir
constructions share a precise dyadic quadratic-refinement pattern.  They do
not yet share a literal lattice or operator identification.

Priority C is resolved to the strongest presently defensible level:

\[
\boxed{
\text{exact common mechanism type, but no canonical cross-layer
intertwiner.}
}
\]

With Priorities A--C now sharply resolved or narrowed, the next high-value
task is architectural: formulate the minimal theorem package suitable for a
new unified paper, separate the theorem sequence from the certified
\(\theta=2\) computation, and determine exactly which existing Papers A--C
and companion notes should be revised rather than overloaded.

---

---

# PART XXIX. PUBLICATION ARCHITECTURE

## 103. Editorial separation principle

**[Audit/editorial]** The new arithmetic chain should not be inserted wholesale
into Papers A--C.  Those papers have a clean foundational progression:

\[
\boxed{
\text{Paper A: geometry}
\longrightarrow
\text{Paper B: classical dynamics}
\longrightarrow
\text{Paper C: representation/quantization}.
}
\]

The discriminant-\(12\) package begins only after imposing the distinguished
dynamic class \(\sigma=2\).  Its natural subject is therefore a fourth
**conceptual layer**, not a retrospective replacement of the first three.

The certified Suzuki calculation is another distinct layer: it realizes the
distinguished class inside one analytic determinant flow, but it is not needed
to prove the downstream algebraic theorems.

Accordingly, publication should separate

\[
\boxed{
\text{universal algebraic theorem package}
}
\]

from

\[
\boxed{
\text{computer-assisted }\theta=2\text{ realization theorem}.
}
\]

## 104. Proposed principal paper

**[I/editorial]** A natural standalone title is

> **The Discriminant-12 Return: From Centered Cayley Geometry to Pell,
> Cyclotomic, and Boolean Structure.**

Its central input is a hyperbolic integral return in the unique
self-reciprocal centered-Cayley class.  Its central output is the exact chain

\[
\boxed{
\sigma=2
\to
\mathbb Q(\sqrt3)
\to
\mathfrak p_2
\to
\mathbb Q(\zeta_{12})
\to
\text{ramified Boolean factor exchange}.
}
\]

The paper should be written so that its main algebraic theorem does not depend
on zeta zeros, RH, numerical evidence, or the Fredholm certificate.

## 105. Minimal theorem package I: universal centered-Cayley algebra

**[D]** The first theorem requires only \(g\in SL_2\) with

\[
\tau=\operatorname{tr}g,
\qquad
H=g-\frac\tau2I,
\qquad
K=(g-I)(g+I)^{-1}.
\]

Then

\[
\boxed{
K=\frac{2}{\tau+2}H,
\qquad
KH=\frac{\tau-2}{2}I.
}
\]

For the shear normalization \(\tau=\sigma+2\),

\[
\boxed{KH=\frac\sigma2I.}
\]

Therefore

\[
\boxed{
K=H^{-1}iff\sigma=2.
}
\]

This theorem is the universal entry point.  It explains why the value \(2\)
is selected before any number field is introduced.

## 106. Minimal theorem package II: the integral return and real quadratic order

**[D]** At \(\sigma=2\), choose the primitive positive integral representative

\[
g_{12}=
\begin{pmatrix}
3&1\\
2&1
\end{pmatrix},
\qquad
H_{12}=g_{12}-2I.
\]

Then

\[
\boxed{
H_{12}^2=3I,
\qquad
\mathbb Z[H_{12}]cong\mathcal O_{\mathbb Q(\sqrt3)}.
}
\]

On

\[
\mathfrak p_2=(2,\sqrt3-1),
\]

the centered generator and return act as

\[
\boxed{
H_{12}=\times\sqrt3,
\qquad
g_{12}=\times(2+\sqrt3).
}
\]

The primitive norm form

\[
q_{12}(x,y)=2x^2-2xy-y^2
\]

has discriminant \(12\), is preserved by \(g_{12}\), and becomes the Lorentz
form after

\[
(U,V)=(2x-y,\sqrt3y).
\]

This should be presented as one theorem with arithmetic, quadratic-form, and
Lorentz corollaries.

## 107. Minimal theorem package III: cyclotomic integral closure

**[D]** Adjoining the analytic complex structure gives

\[
\mathcal Z=\frac{H_{12}+iI}{2}.
\]

Then

\[
\boxed{
\Phi_{12}(\mathcal Z)=0,
\qquad
\mathbb Q(\mathcal Z)=\mathbb Q(\zeta_{12}),
}
\]

and

\[
\boxed{
g_{12}=-i(I+\mathcal Z)(I-\mathcal Z)^{-1}.
}
\]

The integral-closure theorem should include the exact parity description

\[
\mathcal O_K
=
\left\{
\frac{A+B\sqrt3+i(C+D\sqrt3)}2:
A\equiv D, B\equiv C\pmod2
\right\},
\]

and

\[
\boxed{
\mathcal O_K/\mathbb Z[\sqrt3,i]
\cong(\mathbb F_2)^2.
}
\]

This makes both the denominator \(2\) and the associated quarter-normalization
mathematically necessary rather than decorative.

## 108. Minimal theorem package IV: narrow class and Boolean return

**[D]** The ideal \(\mathfrak p_2\) is ordinarily principal but represents the
unique nontrivial narrow class.  In the narrow Hilbert class field

\[
\mathbb Q(\zeta_{12})=H^+_{\mathbb Q(\sqrt3)},
\]

Artin reciprocity gives

\[
\boxed{
[\mathfrak p_2]\longmapsto T_{11}.
}
\]

Separately, reduction of the return gives

\[
\bar g(x,y)=(x+y,y),
\qquad
\bar q_{12}(x,y)=y.
\]

Under

\[
\Phi(x,y)=(x,x+y),
\]

these become

\[
\boxed{
\bar q_{12}=\epsilon_1\oplus\epsilon_2,
\qquad
\Phi\bar g\Phi^{-1}
:(\epsilon_1,\epsilon_2)\mapsto(\epsilon_2,\epsilon_1).
}
\]

The theorem must explicitly state that factor exchange lies in the dihedral
extension of the Boolean translation \(V_4\), not in that translation group
itself.

## 109. Optional realization theorem: the certified Suzuki crossing

**[D + N-cert/editorial]** The analytic realization should be a separate
theorem or companion note:

\[
\boxed{
\exists!\,t_*\in(0,1/5):
m_2(t_*)=2+\sqrt3.
}
\]

Equivalently,

\[
\boxed{
\sigma_2(t_*)=2,
\qquad
K_2(t_*)=H_2(t_*)^{-1}.
}
\]

The proof depends on the repaired kernel approximation, contraction bounds,
positivity, and finite certificate.  It should not interrupt the conceptual
paper's main proof sequence.

Recommended companion title:

> **A Certified Discriminant-12 Crossing in Suzuki's First Determinant
> Chamber.**

The source-matching statement must retain the v13.164 qualification:
\(\sigma_\theta(t)=\theta\) is a level condition, not an identity of the
flow.

## 110. Exact revision scope for Papers A--C

**[Audit/editorial]**

### Paper A

Keep the conic theorem, factorization application, and divisor-summatory
geometry intact.  Recommended changes are minimal:

1. retain the corrected companion citation to the band-area note;
2. add one closing sentence that the factor-coordinate cell also supports a
   Boolean/XOR reduction developed elsewhere;
3. do not introduce Suzuki, Pell ideals, cyclotomic fields, or RH.

### Paper B

This is the only foundational paper that should receive a substantive new
mathematical section.  Add:

1. the trace-defect coordinate \(\sigma=\operatorname{tr}g-2\);
2. the centered generator \(H\) and Cayley transform \(K\);
3. the identity \(KH=\sigma I/2\);
4. the uniqueness of \(\sigma=2\) under \(K=H^{-1}\);
5. a short pointer to the discriminant-\(12\) arithmetic sequel.

Also repair the two stale Paper-A references already identified in v13.126:
the revised Figure 1 example and the proposition number for eccentricity.

Stop Paper B before the number-field development.  Its job is to produce the
distinguished dynamic class, not to contain the arithmetic sequel.

### Paper C

Keep the \(SU(2)\), \(SU(1,1)\), Gaussian obstruction, and revival results as
the core.  Add only:

1. the audited Weyl/quarter completion
   \(j(j+1)=(j+1/2)^2-1/4\);
2. the warning that this is not a universal operator \(+\tfrac14I\);
3. a brief comparison with the \(k=1/2\) Laguerre jet module;
4. a pointer to the arithmetic sequel.

Do not identify the finite \(SU(2)\) representation with the infinite
\(SU(1,1)\) jet tower; only their centered Cartan ladders agree on the first
\(N\) levels.

## 111. Scope for the companion notes

**[Audit/editorial]**

### Null-cone/Casimir note

Revise this note to become the authoritative taxonomy of the quarter:

- factor-cell midpoint square;
- compact/noncompact shifted Casimir;
- primitive null-edge midpoint;
- cyclotomic relative-norm normalization.

Add the exact Boolean-return theorem from v13.163, including the factor-exchange
and \(D_8\) correction.  State explicitly that the four quarters share a
mechanism type but not a universal operator.

### Band-area note

Keep it separate and modest.  Its next revision should:

- replace “consecutive” by “consecutive same-parity” anti-diagonals;
- distinguish the exact finite-\(j\) value
  \[
  \gamma_j=\frac1{4\sqrt2}\sqrt{\frac{j+1}{j}}
  \]
  from its asymptotic limit;
- state that the area is induced by the ambient Euclidean metric, not the
  degenerate Lorentz metric on the null cone;
- repair the boundary and cell-label conventions recorded in v13.126.

Do not add the discriminant-\(12\) arithmetic chain to this note.

### Suzuki/Clark/Berry material

The large canonical-system, Cauchy, Clark, Fisher, Berry, and endpoint-metric
block should remain a separate future analytic paper.  Only the certified
determinant crossing is needed for the discriminant-\(12\) sequel.

## 112. Dependency order for the new paper

**[D/editorial]** The proof order should be

\[
\boxed{
\begin{array}{c}
\text{centered-Cayley identity}\\
\Downarrow\\
\text{unique self-reciprocal class }\sigma=2\\
\Downarrow\\
\text{integral return }g_{12}\text{ and }H^2=3I\\
\Downarrow\\
\mathbb Q(\sqrt3),\ \mathfrak p_2,\ q_{12},\ \text{Lorentz boost}\\
\Downarrow\\
\mathcal Z=(H+iI)/2,\ \mathbb Q(\zeta_{12}),\ \text{integral gluing}\\
\Downarrow\\
\text{narrow Artin class and ramified Boolean return}.
\end{array}
}
\]

The certified Suzuki crossing may appear after this sequence as a realization
theorem, or in a companion paper referenced from the introduction and final
section.

This order prevents the downstream exact algebra from appearing conditional
on the analytic certificate.

## 113. Claims matrix for publication

**[Audit/editorial]**

\[
\begin{array}{c|c|c}
\text{claim}&\text{status}&\text{placement}\\ \hline
K=H^{-1}\iff\sigma=2
&\text{exact universal}&\text{main paper}\\
H_{12}^2=3I
&\text{exact integral representative}&\text{main paper}\\
g_{12}=\times(2+\sqrt3)
&\text{exact ideal action}&\text{main paper}\\
\Phi_{12}(\mathcal Z)=0
&\text{exact cyclotomic closure}&\text{main paper}\\
[\mathfrak p_2]\mapsto T_{11}
&\text{exact narrow Artin map}&\text{main paper}\\
\bar g\leftrightarrow\text{factor exchange}
&\text{exact up to factor order}&\text{main paper}\\
m_2(t_*)=2+\sqrt3
&\text{certified numerical theorem}&\text{companion/appendix}\\
\sigma_\theta(t)=\theta
&\text{matching condition, not identity}&\text{discussion only}\\
\text{RH consequence}
&\text{none established}&\text{explicit exclusion}
\end{array}
\]

## 114. Proposed abstract-level claim

**[I/editorial draft]** A defensible abstract-level statement for the new
principal paper is:

> We show that the unique hyperbolic \(SL_2\) conjugacy class whose centered
> generator is inverse to its Cayley transform has trace defect \(2\).  Its
> primitive integral return generates the maximal order of
> \(\mathbb Q(\sqrt3)\), acts by the fundamental unit \(2+\sqrt3\) on the
> ramified prime above \(2\), preserves a discriminant-\(12\) Lorentz norm
> form, and admits a canonical integral cyclotomic completion to a primitive
> twelfth root.  The same ramified return reduces to factor exchange on a
> four-state Boolean quotient, with its degenerate norm becoming XOR parity.

This statement contains no source-identification hypothesis and no RH claim.

## 115. v13.166 checkpoint

The current results should be published in two layers.

### Algebraic principal paper

\[
\boxed{
\text{centered Cayley}
\to
\sigma=2
\to
\Delta=12
\to
\text{Pell/Lorentz}
\to
\text{cyclotomic gluing}
\to
\text{Boolean exchange}.
}
\]

### Certified analytic companion

\[
\boxed{
\theta=2\text{ Suzuki flow}
\to
\exists!\,t_*:\sigma_2(t_*)=2.
}
\]

Paper B should receive the universal centered-Cayley theorem and then point to
the arithmetic sequel.  Papers A and C need only narrow synchronization and
scope improvements.  The null-cone note should own the quarter taxonomy; the
band-area note should remain an explicitly Euclidean semiclassical
comparison.  The large Suzuki/Clark/Berry block belongs in a later analytic
paper.

This architecture keeps every theorem close to the hypotheses that actually
prove it and prevents the exact arithmetic completion from being mistaken for
either numerical evidence or an RH argument.

The next step is no longer another audit.  It is to draft the theorem-first
outline—or the actual opening sections—of **The Discriminant-12 Return**.

---

**End of v13.166 audited consolidation continuation.**

---

# PART XXX. NULL-DIAMOND COMPANION INTEGRATION

## 116. Editorial action completed

**[Audit/editorial]** The standalone null-diamond companion has been revised
in accordance with the publication architecture fixed in Part XXIX.  Its
original theorem core is preserved:

\[
M_F^2=\frac{\delta^2}{4},
\qquad
R^2=C+M_F^2,
\qquad
A_\pm^2=\sigma(R^2-Z_\pm^2),
\]

with \(\sigma=+1\) for \(SU(2)\) and \(\sigma=-1\) for \(SU(1,1)\).

The revision adds two deliberately bounded sections:

1. **cyclotomic normalization: a fourth quarter;**
2. **the ramified Boolean return.**

The note now owns the quarter taxonomy and the finite return theorem, while
the complete Pell, narrow-class, centered-Cayley, and Suzuki proofs remain in
their designated principal or analytic papers.

## 117. The cyclotomic quarter inserted into the taxonomy

**[D/exact]** For

\[
g_{12}=\begin{pmatrix}3&1\\2&1\end{pmatrix},
\qquad
H=g_{12}-2I
=\begin{pmatrix}1&1\\2&-1\end{pmatrix},
\]

one has

\[
H^2=3I.
\]

After adjoining \(i\), define

\[
\mathcal Z=\frac{H+iI}{2}.
\]

Then

\[
\boxed{
\mathcal Z\overline{\mathcal Z}
=\frac{(H+iI)(H-iI)}4
=\frac{H^2+I}{4}
=I.
}
\]

Thus the denominator \(2\) is forced by relative-norm normalization: the
quadratic operation turns the half into the required quarter.  The eigenvalues

\[
\frac{\sqrt3+i}{2},
\qquad
\frac{-\sqrt3+i}{2}
\]

are primitive twelfth roots, so

\[
\Phi_{12}(\mathcal Z)=0.
\]

At the integral level,

\[
K=\mathbb Q(\sqrt3,i)=\mathbb Q(\zeta_{12}),
\qquad
\mathcal O_0=\mathbb Z[\sqrt3,i],
\qquad
\mathcal O_K/\mathcal O_0\cong(\mathbb F_2)^2.
\]

The revised note therefore records four quarter mechanisms:

\[
\boxed{
\begin{array}{c|c}
\text{layer}&\text{quadratic quarter}\ \hline
\text{factor cell}&(\delta/2)^2\\
\text{rank-one ladder}&j(j+1)+1/4=(j+1/2)^2\\
\text{primitive null edge}&M_F^2=\delta^2/4\\
\text{cyclotomic closure}&(H^2+I)/4=I
\end{array}
}
\]

**[Audit guardrail]** These are instances of a common dyadic mechanism type.
They are not one universal operator identity, and the cyclotomic relative norm
is not identified with the Lorentz norm or a Casimir.

## 118. The ramified Boolean return inserted in corrected form

**[D/exact]** Reduction of the integral return modulo \(2\) gives

\[
\overline g_{12}
=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\qquad
(x,y)\longmapsto(x+y,y).
\]

The relabeling

\[
\Phi(x,y)=(\varepsilon_1,\varepsilon_2)=(x,x+y)
\]

conjugates this transvection to factor exchange:

\[
\boxed{
\Phi\overline g_{12}\Phi^{-1}
(\varepsilon_1,\varepsilon_2)
=(\varepsilon_2,\varepsilon_1).
}
\]

The reduced degenerate norm becomes

\[
\boxed{
\overline q_{12}=y
=\varepsilon_1+\varepsilon_2
=\varepsilon_1\mathbin{\mathrm{xor}}\varepsilon_2.
}
\]

Consequently, if \(V_4^{\rm tr}\) denotes the Boolean translation group,
then adjoining the returned factor exchange gives

\[
\boxed{
V_4^{\rm tr}\rtimes C_2\cong D_8.
}
\]

The return is therefore an affine reflection, not a nonzero Boolean
translation.  This preserves the cycle-type correction from v13.163.

## 119. Four-state spaces and symmetry layers remain distinct

**[Audit]** The revised note records both finite four-state spaces

\[
\mathcal O_K/\mathcal O_0\cong(\mathbb F_2)^2,
\qquad
\mathfrak p_2/2\mathfrak p_2\cong(\mathbb F_2)^2,
\]

but explicitly refuses a canonical identification based only on equal
cardinality and characteristic.  It likewise distinguishes

\[
\begin{array}{c|c}
V_4^{\rm tr}&\text{Boolean translations},\\
C_2&\text{ramified factor exchange},\\
\operatorname{Gal}(\mathbb Q(\zeta_{12})/\mathbb Q)\cong V_4
&\text{cyclotomic sign actions}.
\end{array}
\]

The first two generate \(D_8\).  The third is a field-symmetry group and must
not be substituted for either Boolean layer.

## 120. Scope boundary after revision

**[Audit/editorial]** The companion note now carries exactly the material
needed to bridge Paper C to the discriminant-12 principal paper:

\[
\boxed{
\text{Paper C}
\longrightarrow
\text{null-diamond quarter taxonomy}
\longrightarrow
\text{discriminant-12 arithmetic completion}.
}
\]

It does **not** absorb:

1. the proof that the centered-Cayley self-reciprocal class forces
   \(\sigma=2\);
2. the full Pell-ideal or narrow-class calculation;
3. the certified Suzuki determinant crossing;
4. the Clark/Cauchy/Fisher/Berry construction;
5. any assertion about the Riemann hypothesis.

These exclusions keep the note a genuine bridge theorem rather than a second
version of the principal paper.

## 121. v13.167 checkpoint

The null-diamond companion is now synchronized with the audited arithmetic
developments through v13.166.  Its stable final claim is

\[
\boxed{
\begin{gathered}
\text{The factor-cell, Casimir, and primitive-null-edge quarters are}\
\text{exact realizations inside the common factor-cone quadratic geometry.}\\[1mm]
\text{The cyclotomic quarter is an exact relative-norm normalization}\
\text{sharing the same dyadic mechanism type, but not the same operator.}\\[1mm]
\text{The discriminant-12 return acts on the ramified Boolean quotient}\
\text{as factor exchange, its reduced norm is XOR, and the full affine}\
\text{symmetry is }D_8\text{ rather than the translation }V_4.
\end{gathered}
}
\]

The next principal writing task remains the theorem-first opening of
**The Discriminant-12 Return**.  The revised companion can now be cited from
that paper without importing its full derivation.

---

**End of v13.167 audited consolidation continuation.**

---

# PART XXXI. THE DISCRIMINANT-12 RETURN — THEOREM-FIRST OPENING

## 122. Principal-paper draft initiated

**[Editorial/completed]** A new standalone paper has been opened under the
audited title

> **The Discriminant-12 Return: From Centered Cayley Geometry to Pell,
> Cyclotomic, and Boolean Structure.**

Draft v0.1 currently contains:

1. an abstract stating the complete algebraic chain;
2. an introduction with explicit scope exclusions;
3. the full discriminant-(12) return theorem;
4. complete proofs of the centered-Cayley package;
5. complete proofs of the primitive integral/Pell--Lorentz package;
6. a bounded roadmap for the cyclotomic and Boolean proof packages.

The paper begins from universal (SL_2) algebra.  Neither the Suzuki crossing
nor any numerical certificate appears as a hypothesis.

## 123. Universal entry theorem fixed in publication form

**[D/exact]** For (g\in SL_2(\mathbb Q)), with

\[
\tau=\operatorname{tr}g,
\qquad
H=g-\frac\tau2I,
\qquad
K=(g-I)(g+I)^{-1},
\]

Cayley--Hamilton gives

\[
H^2=\left(\frac{\tau^2}{4}-1\right)I
\]

and the exact centered-Cayley identities

\[
\boxed{
K=\frac{2}{\tau+2}H,
\qquad
KH=\frac{\tau-2}{2}I.
}
\]

Under the shear normalization

\[
\tau=\sigma+2,
\]

hyperbolicity makes (H) invertible and therefore

\[
\boxed{
K=H^{-1}
\iff
KH=I
\iff
\sigma=2.
}
\]

This is now the first proved theorem of the paper.  It selects (2) before
any number field, lattice, determinant flow, or zeta-theoretic structure is
introduced.

## 124. Period-([1,2]) integral representative

**[D/exact]** With

\[
A_a=\begin{pmatrix}a&1\\1&0\end{pmatrix},
\]

the even period ([1,2]) gives

\[
g_{12}=A_1A_2
=\begin{pmatrix}3&1\\2&1\end{pmatrix}.
\]

This wording avoids claiming uniqueness among all positive integral matrices
of trace (4).  The exact data are

\[
\det g_{12}=1,
\qquad
\operatorname{tr}g_{12}=4,
\]

\[
\chi_{g_{12}}(X)=X^2-4X+1,
\qquad
\Delta_{g_{12}}=12,
\]

and

\[
\operatorname{spec}(g_{12})=\{2+\sqrt3,2-\sqrt3\}.
\]

The manuscript calls (Delta_{g_{12}}) the **characteristic discriminant**,
not generically the field discriminant.

## 125. Real quadratic order and ramified ideal action

**[D/exact]** Centering gives

\[
H_{12}=g_{12}-2I
=\begin{pmatrix}1&1\\2&-1\end{pmatrix},
\qquad
H_{12}^2=3I.
\]

Hence

\[
\mathbb Z[H_{12}]
\cong
\mathbb Z[\sqrt3]
=\mathcal O_{\mathbb Q(\sqrt3)}.
\]

For the ramified ideal

\[
\mathfrak p_2=(2,\sqrt3-1),
\]

use the ordered basis

\[
e_1=2,
\qquad
e_2=\sqrt3-1.
\]

The relations

\[
\sqrt3e_1=e_1+2e_2,
\qquad
\sqrt3e_2=e_1-e_2
\]

show directly that

\[
\boxed{
H_{12}=\times\sqrt3,
\qquad
g_{12}=\times(2+\sqrt3)
}
\]

on this lattice.

## 126. Pell--Lorentz package proved

**[D/exact]** For

\[
\alpha=xe_1+ye_2=(2x-y)+y\sqrt3,
\]

the field norm is

\[
N(\alpha)
=(2x-y)^2-3y^2
=2q_{12}(x,y),
\]

where

\[
\boxed{
q_{12}(x,y)=2x^2-2xy-y^2.
}
\]

The form is primitive, has binary-form discriminant (12), and is preserved
by (g_{12}).  With

\[
(U,V)=(2x-y,\sqrt3,y),
\]

it becomes

\[
\boxed{2q_{12}=U^2-V^2.}
\]

The return is therefore multiplication by the norm-one unit (2+\sqrt3), or
equivalently a discrete hyperbolic Lorentz boost.  The publication draft
explicitly says **discrete orbit**, not closed orbit.

Every scalar coordinate of (g_{12}^nv) obeys

\[
a_{n+2}=4a_{n+1}-a_n,
\]

but the initial values remain determined by (v).  Thus trace fixes the
recurrence law, not the initial data.

## 127. Main theorem status after the opening draft

The theorem is stated as a six-part result.  Proof status is now:

\[
\begin{array}{c|c}
\text{package}&\text{draft status}\\ \hline
\text{centered Cayley}&\text{proved in full}\\
\text{self-reciprocal selection }\sigma=2&\text{proved in full}\\
\text{integral return and real order}&\text{proved in full}\\
\text{ramified ideal action}&\text{proved in full}\\
\text{Pell--Lorentz norm form}&\text{proved in full}\\
\text{cyclotomic integral closure}&\text{stated; proof section next}\\
\text{narrow class/Artin map}&\text{stated; proof section later}\\
\text{ramified Boolean return}&\text{stated; proof section next}
\end{array}
\]

The paper is therefore no longer an outline.  Its universal and real-quadratic
first movement is a complete six-page compiled draft.

## 128. Scope guardrails carried into the manuscript

**[Audit]** Draft v0.1 explicitly preserves the following exclusions:

1. no zeta zero or RH hypothesis;
2. no claim that the Suzuki source parameter is identically the dynamic shear;
3. no use of the certified Fredholm crossing in the algebraic proof;
4. no identification of a discrete Lorentz orbit with a closed orbit;
5. no identification of the Boolean translation (V_4), factor exchange,
   and cyclotomic Galois (V_4);
6. no claim that equal four-state quotients are canonically isomorphic.

The analytic realization remains a separate companion result.

## 129. v13.168 checkpoint

The principal paper now begins from a universal theorem and reaches the exact
arithmetic Lorentz return without speculative bridges:

\[
\boxed{
\begin{gathered}
K=H^{-1}
\iff
\sigma=2
\iff
\tau=4,\\
g_{12}=A_1A_2,
\qquad
\Delta_{g_{12}}=12,
\qquad
H_{12}^2=3I,\\
H_{12}=\times\sqrt3,
\qquad
g_{12}=\times(2+\sqrt3),\\
2q_{12}=U^2-V^2.
\end{gathered}
}
\]

The next writing block is now precise: prove the cyclotomic polynomial,
Cayley recovery, maximal-order parity description, and index-four gluing;
then prove the ramified Boolean reduction and its (D_8) symmetry correction.

---

**End of v13.168 audited consolidation continuation.**

---

# PART XXXII. THE GEOMETRIC MOD-12 UNIT SHELL

## 130. Paper-A cone realization of the four unit residues

**[D/exact]** Let

\[
U(12)=(\mathbb Z/12\mathbb Z)^\times=\{1,5,7,11\}.
\]

For each (r\in U(12)), take the factor pair ((r,1)) and its mirror
((1,r)).  Under the Paper-A coordinates

\[
T=\frac{x+y}{2},
\qquad
X=\frac{x-y}{2},
\qquad
Y=\sqrt{xy},
\]

one obtains

\[
\boxed{
T_r=\frac{r+1}{2},
\qquad
X_r=\pm\frac{r-1}{2},
\qquad
Y_r=\sqrt r,
\qquad
T_r^2-X_r^2=r.
}
\]

The values are

\[
\begin{array}{c|cccc}
r&1&5&7&11\\ \hline
T_r&1&3&4&6\\
|X_r|&0&2&3&5\\
Y_r&\sqrt1&\sqrt5&\sqrt7&\sqrt{11}.
\end{array}
\]

The outer residue (r=11) is represented by ((11,1)) and ((1,11)), hence
lies exactly on the Paper-A anti-diagonal

\[
x+y=12,
\qquad T=6.
\]

The four units are therefore not merely abstract labels: they occupy a
canonical row-one/column-one shell inside the existing multiplication-table
cone geometry.

## 131. Exact (V_4) content and its limitation

**[D/exact]** Each unit is self-inverse:

\[
1^2\equiv5^2\equiv7^2\equiv11^2\equiv1\pmod{12}.
\]

Consequently

\[
\boxed{U(12)\cong C_2\times C_2=V_4.}
\]

Under the cyclotomic identification,

\[
r:\zeta_{12}\longmapsto\zeta_{12}^{,r},
\]

the same labels index

\[
\operatorname{Gal}(\mathbb Q(\zeta_{12})/\mathbb Q).
\]

**[Audit guardrail]** The factor cone embeds the four residue labels but does
not supply their modular multiplication law.  Geometric adjacency in the
figure is not group multiplication.

## 132. Layer distinction sharpened by the figure

The new figure joins previously separate visual and arithmetic descriptions,
but it also makes the required distinctions easier to state:

\[
\begin{array}{c|c}
12\text{ as modulus}&U(12)\text{ and Dirichlet/cyclotomic labels}\\
\Delta_{g_{12}}=12&\text{characteristic discriminant of the return}\\
\operatorname{Gal}(\mathbb Q(\zeta_{12})/\mathbb Q)\cong V_4
&\text{cyclotomic sign actions}\\
V_4^{\rm tr}&\text{Boolean translations}\\
C_2\subset D_8&\text{ramified factor exchange}.
\end{array}
\]

These structures are compatible in the selected discriminant-(12) return,
but none is defined merely by the existence of the others.

## 133. Publication placement resolved

**[Editorial/completed]** The full three-panel image now appears in v0.2 of
**The Discriminant-12 Return**, between the Pell--Lorentz proof and the
cyclotomic completion.  This is its strongest logical placement:

\[
\boxed{
\text{Paper-A factor cone}
\longrightarrow
U(12)\cong V_4
\longrightarrow
\mathbb Q(\zeta_{12}).
}
\]

The Null Diamond companion remains focused on edge centering and the quarter
taxonomy.  It may cite the geometric unit shell, but the full figure is not
duplicated there.

## 134. Figure-source audit

**[Audit/completed]** The supplied generator was made repository-portable:

1. the hard-coded `/home/claude/latex_v2/` output path was removed;
2. output is written beside the script as
   `mod12_v4_cone_triple.png`;
3. the stale theorem-number comment was replaced by a description of the
   exact unit-shell formulas;
4. the caption remains in LaTeX rather than being burned into the pixels.

The image is treated as a reproducible paper asset, with both PNG and Python
source retained.

## 135. v13.169 checkpoint

The project now has an explicit geometric bridge from its original factor
cone to the mod-(12) arithmetic:

\[
\boxed{
r\in\{1,5,7,11\}
\longmapsto
\left(
\frac{r-1}{2},\sqrt r,\frac{r+1}{2}
\right),
\qquad
T^2-X^2=r.
}
\]

The (r=11) point closes on the visible (x+y=12) shell of Paper A, while
the four labels carry the exact multiplication group (U(12)\cong V_4).
This bridge is exact at the level of the embedding and the modular label set;
the group operation remains arithmetic rather than geometric adjacency.

The next proof task remains the cyclotomic package:

\[
\Phi_{12}(\mathcal Z)=0,
\qquad
g_{12}=-i(I+\mathcal Z)(I-\mathcal Z)^{-1},
\qquad
\mathcal O_K/\mathbb Z[\sqrt3,i]\cong(\mathbb F_2)^2.
\]

---

**End of v13.169 audited consolidation continuation.**
