# Cone Derivation Ledger v13.936 — Sandbox: Unique-Trivial Ground-Recentered Weyl Limit and Cross-Edge Escape Obstruction

**Date:** 2026-10-01  
**Track:** Sandbox / source-faithful Suzuki shift-selection and cutoff-removal lane  
**Status:** [D] exact uniqueness theorem for the intrinsic recentered branch when \(\lambda_\infty>-\infty\); [D] limit is uniquely trivial \(h\to0,\ m\to i\); [R] corrects the proposed regulator-removal route of v13.935; [G] identifies cross-edge transfer as the lost arithmetic channel; [O] nontrivial renormalized transfer limit remains open  
**Authorization:** Jeremy, 2026-10-01 ("awesome lets hit it now")  
**Parents:** v13.724–725, v13.784–791, v13.857, v13.927, v13.929, v13.931, v13.935  
**Collision check:** v13.936 was absent immediately before this write.

---

## 0. Gate and verdict

v13.935 constructed the intrinsic recentered family

\[
T_{a,\delta}^{\circ}
=
A_a-\lambda_a I+\delta I,
\qquad
\delta>0,
\]

with

\[
T_{a,\delta}^{\circ}\ge \delta I
\]

for every finite \(a\), and asked whether the corresponding Weyl functions have a unique cutoff-free limit as \(a\to\infty\).

The answer is stronger than expected.

Assume only

\[
\boxed{
\lambda_\infty
:=
\lim_{a\to\infty}\lambda_a
>-\infty.
}
\tag{1}
\]

Then for every fixed \(\delta>0\),

\[
\boxed{
h_{a,\delta}^{\circ}(z)\longrightarrow0
}
\tag{2}
\]

locally uniformly on \(\mathbb C_+\), and hence

\[
\boxed{
m_{a,\delta}^{\circ}(z)\longrightarrow i
}
\tag{3}
\]

locally uniformly.

Thus the intrinsic ground-recentered branch has a **unique** large-\(a\) Weyl limit, but that limit is the content-free constant \(i\).

In particular, under RH, v13.935 gives \(\lambda_\infty=0\), so (2)–(3) hold for every fixed \(\delta>0\).

Therefore the two-stage plan

\[
a\to\infty
\quad\text{then}\quad
\delta\downarrow0
\]

cannot reach the Xi Weyl target: after the first limit the Weyl function is already identically \(i\).

The lost information is precisely the transfer between the two receding edges.

---

## 1. Exact translated \(T\)-side variational problem [D]

Let

\[
v_{a,\delta}^{\circ}
=
(T_{a,\delta}^{\circ})^{-1}e^x.
\]

Define the right-edge coordinate

\[
x=a-\xi,
\qquad
0<\xi<2a,
\]

and the normalized edge response

\[
\boxed{
u_{a,\delta}(\xi)
=
e^{-a}v_{a,\delta}^{\circ}(a-\xi).
}
\tag{4}
\]

The source transforms exactly as

\[
e^{-a}e^{a-\xi}
=
e^{-\xi}.
\]

Suzuki's localized Weil form is the restriction of the translation/reflection-invariant global Weil form. Hence on the edge core

\[
\mathcal D_a
=
C_c^\infty(0,2a),
\]

the translated recentered form is

\[
\boxed{
\mathfrak t_{a,\delta}^{\circ}[f,g]
=
Q_W[f,g]
-\lambda_a\langle f,g\rangle_2
+\delta\langle f,g\rangle_2.
}
\tag{5}
\]

No \(\bar D\), no distributional boundary delta, and no endpoint reconstruction are used.

The normalized vector (4) is the Riesz solution

\[
\boxed{
\mathfrak t_{a,\delta}^{\circ}
[u_{a,\delta},\varphi]
=
\langle e^{-\xi},\varphi\rangle_{L^2(0,2a)}
}
\tag{6}
\]

for \(\varphi\in\mathcal D_a\), extended to the finite energy completion.

This is the source-faithful \(T\)-side edge equation.

---

## 2. Canonical limiting edge energy space [D]

Assume (1).

Put

\[
\varepsilon_a
=
\lambda_a-\lambda_\infty
\ge0,
\qquad
\varepsilon_a\downarrow0.
\tag{7}
\]

On

\[
\mathcal D_\infty
=
C_c^\infty(0,\infty),
\]

define

\[
\boxed{
\mathfrak t_{\infty,\delta}^{\circ}[f,g]
=
Q_W[f,g]
-\lambda_\infty\langle f,g\rangle_2
+\delta\langle f,g\rangle_2.
}
\tag{8}
\]

Since \(\lambda_\infty\) is the global Rayleigh bottom from v13.935,

\[
Q_W[f]-\lambda_\infty\|f\|_2^2\ge0,
\]

so

\[
\boxed{
\mathfrak t_{\infty,\delta}^{\circ}[f]
\ge
\delta\|f\|_2^2.
}
\tag{9}
\]

Let

\[
\mathcal H_{\infty,\delta}^{R}
\]

be the Hilbert completion of \(\mathcal D_\infty\) in the norm induced by (8).

No claim is made that (8) is a closable quadratic form on ordinary \(L^2(0,\infty)\). The abstract energy completion exists regardless.

Equation (9) gives a canonical continuous map

\[
\boxed{
J_\delta:
\mathcal H_{\infty,\delta}^{R}
\longrightarrow
L^2(0,\infty),
\qquad
\|J_\delta f\|_2
\le
\delta^{-1/2}\|f\|_{\infty,\delta}.
}
\tag{10}
\]

The map may have a nontrivial completion kernel when the Weil spectral measure has singular mass. That possibility is retained rather than silently discarded.

---

## 3. Finite and limiting norms become asymptotically identical [D]

For \(f\in\mathcal D_a\),

\[
\begin{aligned}
\mathfrak t_{\infty,\delta}^{\circ}[f]
-
\mathfrak t_{a,\delta}^{\circ}[f]
&=
(\lambda_a-\lambda_\infty)\|f\|_2^2\\
&=
\varepsilon_a\|f\|_2^2.
\end{aligned}
\]

Thus

\[
\boxed{
\|f\|_{a,\delta}^2
\le
\|f\|_{\infty,\delta}^2
=
\|f\|_{a,\delta}^2
+
\varepsilon_a\|f\|_2^2.
}
\tag{11}
\]

Since

\[
\|f\|_{a,\delta}^2
\ge
\delta\|f\|_2^2,
\]

we have

\[
\boxed{
\|f\|_{\infty,\delta}^2
\le
\left(1+\frac{\varepsilon_a}{\delta}\right)
\|f\|_{a,\delta}^2.
}
\tag{12}
\]

Therefore the finite and limiting energy norms on \(\mathcal D_a\) are equivalent, with distortion tending to \(1\).

Let

\[
V_a
=
\overline{\mathcal D_a}^{\,\mathcal H_{\infty,\delta}^{R}}.
\]

Then

\[
V_a\subset V_b
\qquad(a<b),
\]

and

\[
\overline{\bigcup_{a>0}V_a}
=
\mathcal H_{\infty,\delta}^{R}.
\tag{13}
\]

---

## 4. Unique right-edge Riesz limit [D]

The functional

\[
\ell(f)
=
\langle e^{-\xi},J_\delta f\rangle_{L^2(0,\infty)}
\]

is bounded on \(\mathcal H_{\infty,\delta}^{R}\) by (10).

Let

\[
u_{\infty,\delta}\in\mathcal H_{\infty,\delta}^{R}
\]

be its unique Riesz vector:

\[
\boxed{
\mathfrak t_{\infty,\delta}^{\circ}
[u_{\infty,\delta},\varphi]
=
\langle e^{-\xi},\varphi\rangle
}
\tag{14}
\]

for all \(\varphi\in\mathcal H_{\infty,\delta}^{R}\).

Let \(w_{a,\delta}\in V_a\) be the Riesz/Galerkin solution using the **limiting** inner product:

\[
\mathfrak t_{\infty,\delta}^{\circ}
[w_{a,\delta},\varphi]
=
\ell(\varphi),
\qquad
\varphi\in V_a.
\tag{15}
\]

Because \(V_a\uparrow\mathcal H_{\infty,\delta}^{R}\),

\[
\boxed{
w_{a,\delta}
\longrightarrow
u_{\infty,\delta}
}
\tag{16}
\]

strongly in \(\mathcal H_{\infty,\delta}^{R}\).

Now compare \(w_{a,\delta}\) with the true finite solution \(u_{a,\delta}\).

On \(V_a\),

\[
\langle f,g\rangle_{\infty,\delta}
=
\langle f,g\rangle_{a,\delta}
+
\varepsilon_a\langle J_\delta f,J_\delta g\rangle_2.
\tag{17}
\]

Subtracting (6) and (15) gives

\[
\langle u_{a,\delta}-w_{a,\delta},\varphi\rangle_{\infty,\delta}
=
\varepsilon_a
\langle J_\delta u_{a,\delta},J_\delta\varphi\rangle_2.
\tag{18}
\]

Set

\[
\varphi=u_{a,\delta}-w_{a,\delta}.
\]

The finite coercivity and Riesz equation give

\[
\|J_\delta u_{a,\delta}\|_2
\le
\frac{\|e^{-\xi}\|_2}{\delta}.
\tag{19}
\]

Using (10),

\[
\boxed{
\|u_{a,\delta}-w_{a,\delta}\|_{\infty,\delta}
\le
\frac{\varepsilon_a}{\delta^{3/2}}
\|e^{-\xi}\|_2.
}
\tag{20}
\]

Since \(\varepsilon_a\to0\),

\[
\boxed{
u_{a,\delta}
\longrightarrow
u_{\infty,\delta}
}
\tag{21}
\]

strongly in \(\mathcal H_{\infty,\delta}^{R}\).

By (10),

\[
\boxed{
J_\delta u_{a,\delta}
\longrightarrow
J_\delta u_{\infty,\delta}
}
\tag{22}
\]

strongly in \(L^2(0,\infty)\).

Thus the right-edge profile is uniquely selected.

---

## 5. The denominator has a unique nonzero limit [D]

Define

\[
D_{a,\delta}(z)
=
\int_0^{2a}
u_{a,\delta}(\xi)e^{iz\xi}\,d\xi,
\qquad
z\in\mathbb C_+.
\tag{23}
\]

Because

\[
e^{iz\xi}\in L^2(0,\infty)
\quad
(\operatorname{Im}z>0),
\]

(22) gives

\[
\boxed{
D_{a,\delta}(z)
\longrightarrow
D_{\infty,\delta}(z)
:=
\int_0^\infty
(J_\delta u_{\infty,\delta})(\xi)e^{iz\xi}\,d\xi
}
\tag{24}
\]

locally uniformly on \(\mathbb C_+\).

At \(z=i\),

\[
D_{\infty,\delta}(i)
=
\langle e^{-\xi},J_\delta u_{\infty,\delta}\rangle.
\]

By the Riesz identity (14),

\[
\boxed{
D_{\infty,\delta}(i)
=
\|u_{\infty,\delta}\|_{\infty,\delta}^2
>0.
}
\tag{25}
\]

Hence \(D_{\infty,\delta}\) is not identically zero.

---

## 6. Exact two-edge formula for the Schur quotient [D]

The finite transform is

\[
F_{a,\delta}^{\circ}(z)
=
\int_{-a}^{a}
v_{a,\delta}^{\circ}(x)e^{izx}\,dx.
\]

Using

\[
x=a-\xi,
\qquad
v_{a,\delta}^{\circ}(a-\xi)
=
e^a u_{a,\delta}(\xi),
\]

we obtain

\[
F_{a,\delta}^{\circ}(z)
=
e^ae^{iaz}
\int_0^{2a}
u_{a,\delta}(\xi)e^{-iz\xi}\,d\xi,
\tag{26}
\]

and

\[
F_{a,\delta}^{\circ}(-z)
=
e^ae^{-iaz}
D_{a,\delta}(z).
\tag{27}
\]

Therefore

\[
h_{a,\delta}^{\circ}(z)
=
e^{2iaz}
\frac{
\int_0^{2a}u_{a,\delta}(\xi)e^{-iz\xi}\,d\xi
}{
D_{a,\delta}(z)
}.
\tag{28}
\]

Set

\[
\eta=2a-\xi.
\]

Then

\[
e^{2iaz}e^{-iz(2a-\eta)}
=
e^{iz\eta}.
\]

Hence the numerator is exactly

\[
\boxed{
N_{a,\delta}(z)
=
\int_0^{2a}
u_{a,\delta}(2a-\eta)e^{iz\eta}\,d\eta.
}
\tag{29}
\]

Thus

\[
\boxed{
h_{a,\delta}^{\circ}(z)
=
\frac{N_{a,\delta}(z)}
{D_{a,\delta}(z)}.
}
\tag{30}
\]

The denominator is the right-edge transform.

The numerator is the **opposite-edge transfer amplitude** of the same right-edge-driven solution.

---

## 7. Strong \(L^2\) tightness kills the opposite-edge transfer [D]

Fix a compact set

\[
K\Subset\mathbb C_+.
\]

Let

\[
y_0
=
\inf_{z\in K}\operatorname{Im}z
>0.
\]

From (22), the \(L^2\) family \(u_{a,\delta}\) is strongly convergent and therefore tight.

For fixed \(R>0\),

\[
\int_0^R
|u_{a,\delta}(2a-\eta)|^2\,d\eta
=
\int_{2a-R}^{2a}
|u_{a,\delta}(\xi)|^2\,d\xi.
\]

Using strong \(L^2\) convergence to \(u_{\infty,\delta}\),

\[
\boxed{
\int_{2a-R}^{2a}
|u_{a,\delta}(\xi)|^2\,d\xi
\longrightarrow0
}
\tag{31}
\]

for every fixed \(R\).

Split (29):

\[
N_{a,\delta}
=
\int_0^R
+
\int_R^{2a}.
\]

For the first piece, Cauchy–Schwarz and (31) give

\[
\sup_{z\in K}
\left|
\int_0^R
u_{a,\delta}(2a-\eta)e^{iz\eta}\,d\eta
\right|
\longrightarrow0.
\tag{32}
\]

For the tail,

\[
\left|
\int_R^{2a}
u_{a,\delta}(2a-\eta)e^{iz\eta}\,d\eta
\right|
\le
\|u_{a,\delta}\|_2
\left(
\int_R^\infty e^{-2y_0\eta}\,d\eta
\right)^{1/2}.
\]

The finite Riesz bound gives

\[
\sup_a\|u_{a,\delta}\|_2
\le
\frac{\|e^{-\xi}\|_2}{\delta}.
\]

Therefore

\[
\boxed{
\sup_a\sup_{z\in K}
\left|
\int_R^{2a}
u_{a,\delta}(2a-\eta)e^{iz\eta}\,d\eta
\right|
\le
C_{\delta,K}e^{-y_0R}.
}
\tag{33}
\]

First send \(a\to\infty\), then \(R\to\infty\).

Thus

\[
\boxed{
N_{a,\delta}(z)\longrightarrow0
}
\tag{34}
\]

locally uniformly on \(\mathbb C_+\).

---

## 8. The Schur limit is uniquely zero [D]

By (25), there is a neighborhood \(U\ni i\) on which

\[
D_{\infty,\delta}(z)\ne0.
\]

Using (24), (30), and (34),

\[
\boxed{
h_{a,\delta}^{\circ}(z)\to0
}
\tag{35}
\]

uniformly on compact subsets of \(U\).

But every \(h_{a,\delta}^{\circ}\) is Schur:

\[
|h_{a,\delta}^{\circ}(z)|\le1.
\]

Hence the family is normal on \(\mathbb C_+\).

Let \(h_*\) be any subsequential locally uniform limit.

Equation (35) gives

\[
h_*=0
\]

on the nonempty open set \(U\).

By the identity theorem,

\[
\boxed{
h_*\equiv0
\quad\text{on }\mathbb C_+.
}
\tag{36}
\]

Every subsequential limit is the same, so the entire family converges:

\[
\boxed{
h_{a,\delta}^{\circ}\longrightarrow0
}
\tag{37}
\]

locally uniformly on \(\mathbb C_+\).

The Cayley data satisfy

\[
s_{a,\delta}^{\circ}
=
\phi_i h_{a,\delta}^{\circ}
\longrightarrow0,
\]

therefore

\[
\boxed{
m_{a,\delta}^{\circ}
=
i\frac{1+s_{a,\delta}^{\circ}}
{1-s_{a,\delta}^{\circ}}
\longrightarrow i.
}
\tag{38}
\]

This proves the theorem stated in §0.

---

## 9. Under RH the regulated route is permanently trivial [D/G]

v13.935 proves

\[
\mathrm{RH}
\iff
\lambda_\infty=0.
\]

Therefore under RH the hypothesis (1) is satisfied.

For **every fixed**

\[
\delta>0,
\]

we have

\[
\boxed{
m_{\infty,\delta}^{\circ}(z)
\equiv i.
}
\tag{39}
\]

Consequently

\[
\boxed{
\lim_{\delta\downarrow0}
m_{\infty,\delta}^{\circ}(z)
=
i.
}
\tag{40}
\]

This is not the Xi Weyl target

\[
-C_\infty\frac{\Xi'(z)}{\Xi(z)}.
\]

Therefore the two-step architecture proposed at the end of v13.935,

\[
a\to\infty
\quad\text{at fixed }\delta>0,
\qquad
\delta\downarrow0,
\]

is **not** a route to the Xi carrier.

The finite ground recentering itself remains valid and canonical; what fails is the expectation that its cutoff-free limit retains the arithmetic cross-edge data.

---

## 10. Why the arithmetic disappears [D/I]

The right-edge response is uniquely tight:

\[
u_{a,\delta}
\to
u_{\infty,\delta}.
\]

The Weyl quotient, however, compares two different macroscopic locations.

From (30):

- \(D_{a,\delta}\) probes the driven right edge;
- \(N_{a,\delta}\) probes the opposite edge at distance \(2a\).

The intrinsic recentered energy completion controls the local edge profile and makes it \(L^2\)-tight.

That exact tightness forces

\[
N_{a,\delta}\to0.
\]

Thus the nontrivial finite Weyl function is a **cross-edge transfer observable**, not a local bulk/edge observable.

The arithmetic information needed for the Xi target lives in the asymptotic size and phase of the vanishing transfer channel.

Taking the unrenormalized limit throws that information away.

---

## 11. Relation to the old \(S\)-side edge obstruction [D/G]

v13.724–725 derived the \(S\)-side edge kernel

\[
g(\xi-\eta)-\lambda\min(\xi,\eta)
\]

and the distributional compensated source

\[
i(e^{-\xi}-\delta_0).
\]

v13.857 later showed that the \(\delta_0\) profile cannot be promoted naively into the negative-order edge-energy dual.

The present theorem bypasses that problem entirely by staying on the \(T\)-side:

\[
e^{-a}e^x
\mapsto
e^{-\xi}\in L^2(0,\infty).
\]

So the unique-triviality conclusion is not caused by the old boundary-delta obstruction.

It is a separate and stronger phenomenon:

\[
\boxed{
\text{right-edge compactness }+\text{ opposite-edge recession}
\Longrightarrow
\text{zero transfer}.
}
\tag{41}
\]

---

## 12. Ordinary \(L^2\) strong-resolvent limits are also the wrong carrier [G]

There is a complementary warning.

Under RH the global Weil form has the zero-side representation

\[
Q_W[f]
=
\sum_\gamma
m_\gamma|\widehat f(\gamma)|^2.
\]

The pure zero contribution is not closable as a quadratic form on ordinary \(L^2(\mathbb R,dx)\).

Indeed fix one zero ordinate \(\gamma_0\), choose \(\varphi\in C_c^\infty\) with

\[
\int\varphi\ne0,
\]

and set

\[
f_R(x)
=
R^{-1}
e^{i\gamma_0x}
\varphi(x/R).
\]

Then

\[
\|f_R\|_2^2
=
R^{-1}\|\varphi\|_2^2
\to0,
\]

while

\[
\widehat f_R(\gamma_0)
=
\widehat\varphi(0)
\]

is constant.

By rapid decay of \(\widehat\varphi\) and zero counting, the contributions at other ordinates vanish after pairing differences, so the zero-side form fails the closability criterion.

Thus an ordinary \(L^2\) Mosco/strong-resolvent limit cannot retain the singular zero carrier faithfully.

The abstract energy completion in §2 is the correct object for the right-edge Riesz problem, but even that completion makes the unrenormalized cross-edge Weyl transfer vanish.

---

## 13. Correction to the strategic endpoint of v13.935 [R]

v13.935 correctly established:

- nested \(\lambda_a\);
- the intrinsic recentered family;
- uniform coercivity;
- the exact threshold equivalence
  \[
  \mathrm{RH}\iff\lambda_\infty=0.
  \]

Those results stand.

What is superseded is only the proposed next architecture that hoped a unique fixed-\(\delta\) limit might then be continued by \(\delta\downarrow0\) to the Xi branch.

The present theorem shows:

\[
\boxed{
\text{fixed-}\delta\text{ uniqueness holds, but the unique limit is }m\equiv i.
}
\]

Hence regulator removal after cutoff removal remains trivial.

---

## 14. New nonredundant gate [O]

The project should no longer seek an **unrenormalized** cutoff-free Weyl limit of the recentered family.

The next object must retain the asymptotic cross-edge transfer before it vanishes.

Define

\[
N_{a,\delta}(z)
=
\int_0^{2a}
u_{a,\delta}(2a-\eta)e^{iz\eta}\,d\eta.
\]

The open problem is to find an intrinsic normalization

\[
\mathcal R_{a,\delta}(z)
\]

derived from the finite Suzuki geometry, not fitted to Xi, such that

\[
\boxed{
\mathcal R_{a,\delta}(z)N_{a,\delta}(z)
}
\tag{42}
\]

has a nonzero locally uniform limit.

This is now the exact place where Suzuki's own normalization

\[
e^{\phi(a,z)}
\]

in the conjectural limit of \(W(a,\theta;z)\) belongs conceptually.

The likely correct language is:

\[
\boxed{
\textbf{cross-edge scattering / Jost normalization, not bulk resolvent convergence.}
}
\]

A successful normalization must be determined from finite boundary transfer, reflection symmetry, Wronskian/characteristic data, or another source-faithful invariant.

It may not be chosen using the Riemann zeros or the desired Xi limit.

---

## 15. Result

Assuming only

\[
\lambda_\infty>-\infty,
\]

the intrinsic ground-recentered branch is completely classified:

\[
\boxed{
h_{a,\delta}^{\circ}\to0,
\qquad
m_{a,\delta}^{\circ}\to i
\quad
(\delta>0\text{ fixed}).
}
\]

Thus:

\[
\boxed{
\textbf{uniqueness is closed, but it closes to the trivial Weyl carrier.}
}
\]

Under RH this holds for every \(\delta>0\), so

\[
a\to\infty
\quad\text{then}\quad
\delta\downarrow0
\]

cannot produce the Xi Weyl function.

The finite arithmetic information survives only in the **rate and phase at which the opposite-edge transfer amplitude tends to zero**.

Therefore the next gate is sharply localized:

\[
\boxed{
\textbf{derive the canonical renormalization of the vanishing cross-edge transfer amplitude.}
}
\]

That is the first remaining route capable of producing a nontrivial cutoff-free characteristic without reintroducing arbitrary cutoff data.
