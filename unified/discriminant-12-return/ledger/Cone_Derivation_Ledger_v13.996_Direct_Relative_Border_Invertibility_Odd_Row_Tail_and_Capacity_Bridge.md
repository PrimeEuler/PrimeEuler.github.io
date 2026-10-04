# Cone Derivation Ledger v13.996 — Direct Relative-Border Invertibility, Exact ±i Row Tail, and Capacity Bridge

**Date:** 2026-10-04  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] exact \(\pm i\) observable-row reflection law; [D] explicit \(O(N^{-1/2})\) trace-norm truncation bound for the relative row; [D] exact full-border invertibility from source-level \(T_a^{-1}\) and \(F_a(-i)>0\); [D] direct rank-one Fredholm determinant formula with no complement split; [D] exact identification of that relative determinant with the v13.994 source-capacity ratio; [G] the hoped-for faster \(p_{+i}-p_{-i}\) tail cancellation does not occur; [O] outward-certify the capacity ratio in protected coordinates.  
**Parents:** v13.782, v13.791–792, v13.966, v13.994–995.  
**Research commit:** 7776f1a811d9baebab4c399501006174cbd5342e.  
**Workflow commit:** c57dd5f1d6c6a80b0920b1f58ead1085804d633f.  
**Collision check:** immediately before this write, live HEAD was c57dd5f1d6c6a80b0920b1f58ead1085804d633f; no v13.996 ledger entry was present.

---

## 0. Purpose

v13.995 established a correct relative-determinant framework for the pre-elimination projective border ratio, but left two possible hard hypotheses:

1. exact complement invertibility \(D^{-1}\);
2. invertibility of the full \(-i\) bordered operator.

It also suggested checking whether

\[
p_{Q,+i}-p_{Q,-i}
\]

has a faster remote tail than either row separately.

The present entry closes those questions more sharply.

The row difference does **not** gain a faster power. It has an exact odd-sector \(1/n\) tail.

However this does not obstruct the relative determinant. At the exact finite-\(a\) operator level, the full \(-i\) border is already invertible directly from the source-level facts

\[
T_a^{-1}\ \text{exists}
\]

and

\[
F_a(-i)>0.
\]

Therefore the rank-one Fredholm relative determinant exists **without introducing any complement \(D\)**.

Its scalar is exactly

\[
\boxed{
\frac{G_e-G_o}{G_e+G_o},
}
\]

the same quantity reformulated in v13.994 as a ratio of source-capacity inertia thresholds.

Thus the determinant lane and the capacity lane meet exactly.

---

## 1. Exact \(\pm i\) observable rows [D]

At \(a=1\), in the source-faithful Fourier basis used by the current KKT/outward machinery,

\[
p_{-i,n}
=
\langle \psi_n,e^x\rangle.
\]

Reflection gives

\[
p_{+i,n}
=
\langle \psi_n,e^{-x}\rangle.
\]

For the even spatial sector, represented by odd Fourier modes,

\[
R\psi_n=+\psi_n,
\]

so

\[
\boxed{
p_{+i,n}=p_{-i,n}
\qquad
(n\ {\rm odd}).
}
\tag{1}
\]

For the odd spatial sector, represented by even Fourier modes,

\[
R\psi_n=-\psi_n,
\]

so

\[
\boxed{
p_{+i,n}=-p_{-i,n}
\qquad
(n\ {\rm even}).
}
\tag{2}
\]

Hence

\[
\boxed{
\Delta p
:=
p_{+i}-p_{-i}
}
\]

vanishes identically on even-v and is supported entirely on odd-v.

---

## 2. Exact coefficient formula [D]

The audited source coefficient formula is

\[
p_{-i,n}
=
k_n
\frac{
e^{-1}-(-1)^n e
}{
1+k_n^2
},
\qquad
k_n=\frac{n\pi}{2}.
\tag{3}
\]

For odd \(n\),

\[
p_{-i,n}
=
\frac{
4\pi n\cosh 1
}{
4+\pi^2n^2
},
\]

and by (1),

\[
\boxed{
\Delta p_n=0.
}
\tag{4}
\]

For even \(n\),

\[
p_{-i,n}
=
-\frac{
4\pi n\sinh 1
}{
4+\pi^2n^2
}.
\]

Using (2),

\[
\boxed{
\Delta p_n
=
\frac{
8\pi n\sinh 1
}{
4+\pi^2n^2
}
=
\frac{
8\sinh 1
}{
\pi n
}
\frac1{
1+4/(\pi^2n^2)
}.
}
\tag{5}
\]

Therefore

\[
\boxed{
\Delta p_n
=
\frac{
8\sinh 1
}{
\pi n
}
-
\frac{
32\sinh 1
}{
\pi^3n^3
}
+
O(n^{-5})
}
\qquad
(n\ {\rm even}).
\tag{6}
\]

The leading constant is

\[
\boxed{
\lim_{\substack{n\to\infty\\n\ {\rm even}}}
n\Delta p_n
=
\frac{8\sinh 1}{\pi}
\approx
2.992625265534507.
}
\tag{7}
\]

The CI replay agrees with the exact formula to

\[
2.78\times10^{-17}
\]

on the first twenty odd-sector modes, and the even-sector difference is exactly zero.

---

## 3. Explicit \(\ell^2\) tail bound [D]

Let \(N\) be even and truncate after mode \(N\).

The remaining relative row occupies

\[
n=N+2,N+4,\dots.
\]

Set

\[
A=\frac{8\sinh1}{\pi}.
\]

From (5),

\[
|\Delta p_n|
=
\frac{A}{n}
\frac1{1+4/(\pi^2n^2)}.
\]

For the same-parity harmonic tail,

\[
\frac1{2(N+2)}
\le
\sum_{\substack{n>N\\n\ {\rm even}}}
\frac1{n^2}
\le
\frac1{2N}.
\tag{8}
\]

Since the correction factor in (5) increases monotonically to \(1\),

\[
\boxed{
\frac{A}{
1+4/[\pi^2(N+2)^2]
}
\frac1{\sqrt{2(N+2)}}
\le
\|\Delta p_{>N}\|_2
\le
\frac{A}{\sqrt{2N}}.
}
\tag{9}
\]

Thus

\[
\boxed{
\|\Delta p_{>N}\|_2
=
\frac{
4\sqrt2\,\sinh1
}{
\pi
}
N^{-1/2}
+
o(N^{-1/2}).
}
\tag{10}
\]

Numerically,

\[
\boxed{
\frac{
4\sqrt2\,\sinh1
}{
\pi
}
\approx
2.1161056188096423.
}
\tag{11}
\]

At \(N=10^6\), the certified two-sided interval for

\[
\sqrt N\,\|\Delta p_{>N}\|_2
\]

is

\[
2.1161035027
\le
\sqrt N\,\|\Delta p_{>N}\|_2
\le
2.1161056188.
\]

Hence the faster-tail suggestion in v13.995 §5 is ruled out:

\[
\boxed{
\textbf{the relative row has a genuine }N^{-1/2}\textbf{ truncation norm, not }N^{-3/2}.
}
\]

---

## 4. The relative perturbation is nevertheless trace class [D]

Write the full source-level \(-i\) border abstractly on

\[
\mathcal H\oplus\mathbb C
\]

as

\[
\boxed{
\mathfrak B_-
=
\begin{pmatrix}
T_a & b\\
-p_-^* & 0
\end{pmatrix},
}
\tag{12}
\]

where

\[
b=e^x,
\qquad
p_-=e^x
\]

under the Riesz identification.

Likewise,

\[
\mathfrak B_+
=
\begin{pmatrix}
T_a & b\\
-p_+^* & 0
\end{pmatrix}.
\]

Their difference is

\[
\boxed{
\mathfrak B_+-\mathfrak B_-
=
\begin{pmatrix}
0&0\\
-\Delta p^*&0
\end{pmatrix}.
}
\tag{13}
\]

This has rank one.

Therefore it is trace class independently of any faster asymptotic cancellation.

For a Fourier truncation \(P_N\), the omitted rank-one perturbation has trace norm exactly

\[
\boxed{
\|
(\mathfrak B_+-\mathfrak B_-)
-
P_N(\mathfrak B_+-\mathfrak B_-)P_N
\|_1
=
\|\Delta p_{>N}\|_2.
}
\tag{14}
\]

Thus (9) is an explicit trace-norm truncation certificate.

---

## 5. Full-border invertibility does not require complement invertibility [D]

v13.782 extracts directly from Suzuki's source equation that for

\[
\lambda<\lambda_a,
\]

\[
\boxed{
T_a=A_a-\lambda I
}
\]

is invertible on \(L^2(-a,a)\).

Let

\[
w=T_a^{-1}b.
\]

From v13.791,

\[
\boxed{
F_a(-i)
=
\langle b,T_a^{-1}b\rangle
=
\langle w,T_aw\rangle
>0.
}
\tag{15}
\]

Consider

\[
\mathfrak B_-
\binom{x}{c}
=
\binom{y}{\eta}.
\]

The first row gives

\[
x=T_a^{-1}y-cT_a^{-1}b.
\]

Substitute into the second row:

\[
-\langle b,T_a^{-1}y\rangle
+
cF_a(-i)
=
\eta.
\]

Therefore

\[
\boxed{
c
=
\frac{
\eta+\langle b,T_a^{-1}y\rangle
}{
F_a(-i)
},
}
\tag{16}
\]

and

\[
\boxed{
x
=
T_a^{-1}y
-
\frac{
T_a^{-1}b
}{
F_a(-i)
}
\left[
\eta+\langle b,T_a^{-1}y\rangle
\right].
}
\tag{17}
\]

Hence

\[
\boxed{
\mathfrak B_-^{-1}
}
\]

exists and is bounded whenever \(T_a^{-1}\) is bounded and \(F_a(-i)\neq0\).

For the source-level Suzuki regime \(\lambda<\lambda_a\), both are already established.

Therefore the v13.995 hypothesis that the full \(-i\) border be separately assumed invertible is unnecessary.

More importantly, **no complement block \(D\) appears anywhere in this argument.**

Thus exact complement invertibility is not required to define the direct full relative determinant.

---

## 6. Exact rank-one Fredholm determinant [D]

Since

\[
\mathfrak B_-^{-1}
\]

is bounded and

\[
\mathfrak B_+-\mathfrak B_-
\]

is rank one,

\[
\boxed{
K_{\rm rel}
:=
\mathfrak B_-^{-1}
(\mathfrak B_+-\mathfrak B_-)
\in\mathfrak S_1.
}
\tag{18}
\]

Therefore the ordinary Fredholm determinant

\[
\boxed{
\det_{\rm F}(I+K_{\rm rel})
}
\tag{19}
\]

exists.

No determinant of \(T_a\), no determinant of a complement \(D\), and no regularized bulk determinant is required.

This is exactly the relative rank-one determinant category identified in v13.995 from the v13.661 lineage.

---

## 7. Direct evaluation of the relative determinant [D]

Let

\[
e_{\rm bdry}
=
\binom{0}{1}.
\]

From (16)–(17) with \(y=0,\eta=1\),

\[
\boxed{
\mathfrak B_-^{-1}e_{\rm bdry}
=
\binom{
-w/F_a(-i)
}{
1/F_a(-i)
}.
}
\tag{20}
\]

The rank-one perturbation (13) applies the functional

\[
-\Delta p^*
\]

to the Hilbert-space component.

Hence the rank-one Fredholm determinant is

\[
\begin{aligned}
\det_{\rm F}(I+K_{\rm rel})
&=
1+
\frac{
\langle \Delta p,w\rangle
}{
F_a(-i)
}\\
&=
\frac{
F_a(-i)+\langle \Delta p,T_a^{-1}b\rangle
}{
F_a(-i)
}.
\end{aligned}
\]

But

\[
p_+=p_-+\Delta p,
\]

so

\[
F_a(i)
=
F_a(-i)
+
\langle\Delta p,T_a^{-1}b\rangle.
\]

Therefore

\[
\boxed{
\det_{\rm F}(I+K_{\rm rel})
=
\frac{
F_a(i)
}{
F_a(-i)
}
=
\kappa_a^\Xi.
}
\tag{21}
\]

This is an exact infinite-dimensional finite-\(a\) relative Fredholm determinant identity.

---

## 8. Parity reduction of the rank-one determinant [D]

Write

\[
b=e^x=\cosh x+\sinh x.
\]

Because \(T_a\) commutes with reflection,

\[
T_a^{-1}b
=
(T_a^{(+)})^{-1}\cosh
+
(T_a^{(-)})^{-1}\sinh.
\]

Define

\[
\boxed{
G_e
=
\langle
\cosh,
(T_a^{(+)})^{-1}\cosh
\rangle,
}
\tag{22}
\]

\[
\boxed{
G_o
=
\langle
\sinh,
(T_a^{(-)})^{-1}\sinh
\rangle.
}
\tag{23}
\]

Then

\[
F_a(-i)=G_e+G_o.
\]

Also

\[
\Delta p=e^{-x}-e^x=-2\sinh x,
\]

so

\[
\boxed{
\langle
\Delta p,T_a^{-1}b
\rangle
=
-2G_o.
}
\tag{24}
\]

Equation (21) therefore becomes

\[
\boxed{
\det_{\rm F}(I+K_{\rm rel})
=
1-
\frac{2G_o}{G_e+G_o}
=
\frac{G_e-G_o}{G_e+G_o}.
}
\tag{25}
\]

This is exactly the deficiency-overlap scalar of v13.791–792 and v13.966.

---

## 9. Exact bridge to the v13.994 capacity threshold [D]

Define the parity capacities

\[
\mathcal C_e=G_e^{-1},
\qquad
\mathcal C_o=G_o^{-1}.
\]

Then (25) is

\[
\boxed{
\det_{\rm F}(I+K_{\rm rel})
=
\frac{
\mathcal C_o-\mathcal C_e
}{
\mathcal C_o+\mathcal C_e
}.
}
\tag{26}
\]

Equivalently, with

\[
q_a^\Xi
=
\frac{
\mathcal C_e
}{
\mathcal C_o
}
=
\frac{G_o}{G_e},
\]

\[
\boxed{
\det_{\rm F}(I+K_{\rm rel})
=
\frac{1-q_a^\Xi}{1+q_a^\Xi}.
}
\tag{27}
\]

Thus the v13.995 relative determinant and the v13.994 rank-one source-capacity crossing are not merely compatible approaches.

They are the same scalar expressed in two exact languages:

\[
\boxed{
\text{relative rank-one Fredholm determinant}
\iff
\text{odd source fraction}
\iff
\text{ratio of parity capacity thresholds}.
}
\tag{28}
\]

---

## 10. Consequence for the v13.995 hypotheses [R/G]

The v13.995 relative-determinant theorem introduced:

- (H1) exact complement \(D\) invertibility;
- (H4) full \(-i\) border invertibility.

The present result sharpens their roles.

### Full direct relative determinant

For the exact source-level operator, neither is an independent obstacle.

The direct border invertibility follows from

\[
T_a^{-1}
\]

and

\[
F_a(-i)>0.
\]

No complement split is needed.

### Reduced/Feshbach representation

Exact \(D^{-1}\) is still required if one wants to pass through the protected/complement Schur representation and identify the reduced border.

Therefore:

\[
\boxed{
\textbf{exact complement invertibility is a reduction hypothesis, not a determinant-existence hypothesis.}
}
\tag{29}
\]

This removes a major structural obstacle from the relative-determinant lane.

---

## 11. What the \(N^{-1/2}\) row tail does and does not imply [G]

Equation (9) gives an explicit approximation rate for the **rank-one perturbation row**.

It does not by itself prove

\[
\det_{\rm F}(I+K_{{\rm rel},N})
\to
\det_{\rm F}(I+K_{\rm rel}),
\]

because one must also control the relevant action of the base inverse

\[
\mathfrak B_-^{-1}.
\]

But (25) shows that evaluating that action is exactly the same as evaluating the odd source fraction

\[
\frac{G_o}{G_e+G_o}.
\]

Therefore there is no reason to certify a large border inverse numerically.

The strongest existing proof technology is precisely v13.994:

\[
G_p^{-1}
=
\mathcal C_p
=
\text{rank-one loss-of-positivity threshold}.
\]

The correct consumer is the capacity ratio.

---

## 12. Next proof gate [O]

The determinant-category question is structurally closed at exact finite \(a\).

The remaining numerical proof problem is now:

\[
\boxed{
\textbf{certify }q_a^\Xi=\frac{\mathcal C_e}{\mathcal C_o}
\textbf{ by protected-core inertia crossings.}
}
\]

Specifically, adapt the theorem-scale M3999/4000 outward machinery as prescribed in v13.994:

1. freeze the dangerous low source-carrying block;
2. leave only the stiff remote complement;
3. insert the rank-one source perturbation;
4. normalize each protected capacity crossing to \(O(1)\);
5. certify lower/upper crossing brackets in each parity by opposite inertia;
6. propagate the two threshold intervals through
   \[
   \kappa
   =
   \frac{\mathcal C_o-\mathcal C_e}
   {\mathcal C_o+\mathcal C_e}.
   \]

No global source inverse and no whole-border singular-value bound is required.

---

## 13. Result

The sandbox v13.995 suggestion of a faster relative-row tail is false:

\[
\boxed{
\|\Delta p_{>N}\|_2
\sim
\frac{
4\sqrt2\,\sinh1
}{
\pi
}
N^{-1/2}.
}
\]

But the stronger operator theorem holds.

For Suzuki's exact source-level finite-\(a\) problem,

\[
\boxed{
\mathfrak B_-^{-1}
\text{ exists directly from }
T_a^{-1}
\text{ and }
F_a(-i)>0,
}
\]

and

\[
\boxed{
\kappa_a^\Xi
=
\det_{\rm F}
\left[
I+
\mathfrak B_-^{-1}
(\mathfrak B_+-\mathfrak B_-)
\right].
}
\]

The perturbation is rank one and trace class.

Moreover,

\[
\boxed{
\kappa_a^\Xi
=
\frac{G_e-G_o}{G_e+G_o}
=
\frac{
\mathcal C_o-\mathcal C_e
}{
\mathcal C_o+\mathcal C_e
}.
}
\]

Thus the relative-determinant lane and the protected-capacity/inertia lane are exactly the same projective observable.

The proof target is now the protected capacity ratio, not any unstable inverse.

---

HANDOFF
target: sandbox
type: audit
parent: v13.996
status: open
action: Audit the operator-domain argument that the full minus-i border is boundedly invertible from source-level T_a^{-1} and F_a(-i)>0, and audit the resulting direct rank-one Fredholm determinant identity without assuming complement D invertibility.
deliverable: theorem-or-obstruction
constraints: Do not rebuild KKT; distinguish the exact finite-a Hilbert-space relative determinant from any a-to-infinity convergence claim; check v13.782 and v13.791 source assumptions explicitly.
