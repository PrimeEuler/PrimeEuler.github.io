# Cone Derivation Ledger v13.955 — Sandbox: RH-Conditional Fixed-Rank Moat Obstruction and Source-Weighted Repair

**Date:** 2026-10-02  
**Track:** Sandbox / untwisted Suzuki selector and critical low-energy lane  
**Status:** [D] RH-conditional collapse of every fixed finite parity level; [R] rules out the fixed-rank uniform-moat hypothesis H1 of v13.954 in the RH-positive asymptotic regime; [D] explicit construction of low-energy bulk trial spaces exponentially invisible to the edge source; [O] replace spectral isolation by source-weighted spectral-measure dominance  
**Authorization:** Jeremy, 2026-10-02 ("perfect. lets hit that gate!")  
**Parents:** v13.753, v13.798, v13.923, v13.941, v13.943–944, v13.953–954  
**Collision check:** v13.955 was absent in the live tree immediately before this write.

---

## 0. Gate and verdict

v13.954 reduced the desired untwisted edge-doublet picture to a two-dimensional Feshbach problem under a fixed-rank complement moat

\[
Q_aB_aQ_a\ge gQ_a,
\qquad g>0,
\]

where

\[
B_a=A_a-\lambda_aI\ge0.
\]

The present gate tests whether such a moat can hold for the actual large-\(a\) Suzuki operator.

Under RH, the answer is **no**.

More strongly, for either parity and every fixed \(k\ge1\),

\[
\boxed{
\mu^{(\pm)}_{k,a}(B_a)
=
O(a^{-M})
\qquad
\text{for every }M>0,
}
\tag{1}
\]

where \(\mu^{(\pm)}_{k,a}(B_a)\) denotes the \(k\)-th recentered eigenvalue in the even/odd sector.

Therefore no fixed finite-rank protected space can leave a complement with a uniform positive spectral floor.

This invalidates the spectral-moat hypothesis H1 of v13.954 as an asymptotic RH mechanism.

It does **not** invalidate source-driven edge selection: the bulk near-null trial spaces used below can simultaneously have exponentially small overlap with \(e^{\pm x}\).

Thus the correct replacement is source-weighted spectral-measure dominance, not spectral isolation.

---

## 1. RH-positive zero-side form [D, conditional on RH]

Under RH, the global Weil form is

\[
\boxed{
Q_W[f]
=
\sum_\gamma
m_\gamma
|\widehat f(\gamma)|^2,
}
\tag{2}
\]

where \(\gamma\in\mathbb R\setminus\{0\}\) runs over the nontrivial zero ordinates with multiplicity \(m_\gamma\).

The localized Suzuki form on \(C_c^\infty(-a,a)\) is the restriction of \(Q_W\).

Because

\[
\Xi(0)\ne0,
\]

there is a central zero-free window

\[
\boxed{
\gamma_1:=\inf_\gamma|\gamma|>0.
}
\tag{3}
\]

The zero-counting estimate implies

\[
\boxed{
\sum_\gamma
m_\gamma|\gamma|^{-s}<\infty
\qquad(s>1).
}
\tag{4}
\]

---

## 2. Fixed finite-dimensional parity trial space [D]

Fix a parity sign

\[
\varepsilon\in\{+,-\}
\]

and an integer

\[
k\ge1.
\]

Choose a \(k\)-dimensional subspace

\[
V_k^{(\varepsilon)}
\subset
C_c^\infty(-1,1)
\]

consisting entirely of functions of parity \(\varepsilon\).

For \(a>1\), define the unitary dilation

\[
\boxed{
(U_a\phi)(x)
=
a^{-1/2}\phi(x/a).
}
\tag{5}
\]

Then

\[
U_aV_k^{(\varepsilon)}
\subset
C_c^\infty(-a,a)
\]

and parity is preserved.

Also

\[
\|U_a\phi\|_2=\|\phi\|_2.
\]

With the project Fourier convention,

\[
\boxed{
\widehat{U_a\phi}(t)
=
a^{1/2}\widehat\phi(at).
}
\tag{6}
\]

---

## 3. Uniform Schwartz bound on the whole finite-dimensional unit sphere [D]

Because \(V_k^{(\varepsilon)}\) is finite dimensional, every Schwartz seminorm is uniformly bounded on its \(L^2\)-unit sphere.

Thus for every integer \(N\ge1\), there exists \(C_{k,N}<\infty\) such that

\[
\boxed{
|\widehat\phi(\xi)|
\le
C_{k,N}(1+|\xi|)^{-N}
}
\tag{7}
\]

for all

\[
\phi\in V_k^{(\varepsilon)},
\qquad
\|\phi\|_2=1.
\]

Therefore, using (2) and (6),

\[
\begin{aligned}
Q_W[U_a\phi]
&=
a
\sum_\gamma
m_\gamma
|\widehat\phi(a\gamma)|^2\\
&\le
C_{k,N}^2
a
\sum_\gamma
m_\gamma
(1+a|\gamma|)^{-2N}.
\end{aligned}
\]

Since \(a\ge1\),

\[
(1+a|\gamma|)^{-2N}
\le
a^{-2N}|\gamma|^{-2N}.
\]

Hence

\[
\boxed{
Q_W[U_a\phi]
\le
C_{k,N}'
a^{1-2N}.
}
\tag{8}
\]

The bound is uniform over the full unit sphere of the \(k\)-dimensional trial space.

---

## 4. Every fixed parity level collapses [D]

Let

\[
\lambda_{k,a}^{(\varepsilon)}(A_a)
\]

be the \(k\)-th min-max eigenvalue of \(A_a\) in parity sector \(\varepsilon\).

By the min-max principle and (8),

\[
\boxed{
\lambda_{k,a}^{(\varepsilon)}(A_a)
\le
C_{k,N}'a^{1-2N}.
}
\tag{9}
\]

Given any \(M>0\), choose \(N\) with

\[
2N-1\ge M.
\]

Then

\[
\boxed{
\lambda_{k,a}^{(\varepsilon)}(A_a)
=
O(a^{-M})
\qquad
\forall M>0.
}
\tag{10}
\]

Under RH,

\[
A_a\ge0,
\qquad
\lambda_a:=\inf\sigma(A_a)\ge0.
\]

The recentered parity eigenvalues are

\[
\mu_{k,a}^{(\varepsilon)}(B_a)
=
\lambda_{k,a}^{(\varepsilon)}(A_a)
-
\lambda_a.
\]

Since \(B_a\ge0\),

\[
0
\le
\mu_{k,a}^{(\varepsilon)}(B_a)
\le
\lambda_{k,a}^{(\varepsilon)}(A_a).
\]

Therefore

\[
\boxed{
\mu_{k,a}^{(\varepsilon)}(B_a)
=
O(a^{-M})
\qquad
\forall M>0.
}
\tag{11}
\]

This proves (1).

---

## 5. No fixed-rank uniform moat [D/R]

Let \(r\ge1\) be fixed.

Suppose there were rank-\(r\) projections \(P_a\) and a constant \(g>0\) such that

\[
Q_a:=I-P_a
\]

satisfied

\[
\boxed{
Q_aB_aQ_a\ge gQ_a
}
\tag{12}
\]

for all sufficiently large \(a\).

Then the min-max principle would imply

\[
\mu_{r+1,a}(B_a)\ge g.
\]

But the global version of the construction above, or either parity version with sufficiently many test functions, gives

\[
\mu_{r+1,a}(B_a)\to0.
\]

Contradiction.

Hence

\[
\boxed{
\textbf{no fixed finite-rank protected subspace admits a uniform positive complement moat.}
}
\tag{13}
\]

In particular, the two-dimensional moat hypothesis H1 of v13.954 cannot hold asymptotically under RH.

More generally, for every fixed \(g>0\), the counting function

\[
N_a(g)
=
\#\{\mu_j(B_a)<g\}
\]

satisfies

\[
\boxed{
N_a(g)\to\infty.
}
\tag{14}
\]

No growth rate in \(a\) is asserted here.

---

## 6. Same obstruction separately in both parity sectors [D]

Equation (11) holds independently for

\[
\varepsilon=+
\]

and

\[
\varepsilon=-.
\]

Thus for every fixed \(k\),

\[
\boxed{
\mu^{(+)}_{k,a}(B_a)\to0,
\qquad
\mu^{(-)}_{k,a}(B_a)\to0.
}
\tag{15}
\]

So the asymptotic low-energy sector is not one isolated even/odd doublet.

There are arbitrarily many collapsing modes in each parity sector.

This is consistent with the earlier finite-cutoff protected ladders seen in v13.798 and removes any temptation to interpret those ladders as numerical accidents.

---

## 7. The moat-killing trial spaces can be edge-source invisible [D]

The failure of a spectral moat does not imply failure of edge-source selection.

Fix

\[
0<\eta<1.
\]

Choose the finite-dimensional trial space more narrowly:

\[
V_k^{(\varepsilon)}
\subset
C_c^\infty(-1+\eta,1-\eta).
\]

Then

\[
U_aV_k^{(\varepsilon)}
\]

is supported in

\[
[-(1-\eta)a,(1-\eta)a].
\]

For a normalized \(\phi\in V_k^{(\varepsilon)}\),

\[
\begin{aligned}
|\langle U_a\phi,e^x\rangle|
&\le
a^{-1/2}
\int_{-(1-\eta)a}^{(1-\eta)a}
|\phi(x/a)|e^x\,dx\\
&\le
C_k
a^{1/2}
e^{(1-\eta)a}.
\end{aligned}
\]

Meanwhile

\[
\|e^x\|_{L^2(-a,a)}
=
\left(\sinh(2a)\right)^{1/2}
\sim
2^{-1/2}e^a.
\]

Hence uniformly on the unit sphere,

\[
\boxed{
\frac{
|\langle U_a\phi,e^x\rangle|
}{
\|e^x\|_2
}
\le
C_k'
a^{1/2}e^{-\eta a}.
}
\tag{16}
\]

Similarly,

\[
\boxed{
\frac{
|\langle U_a\phi,e^{-x}\rangle|
}{
\|e^{-x}\|_2
}
\le
C_k'
a^{1/2}e^{-\eta a}.
}
\tag{17}
\]

Thus one can construct arbitrarily large fixed-dimensional families that are simultaneously:

- super-algebraically low energy;
- exponentially weakly coupled to the normalized edge sources.

This is the central repair clue.

---

## 8. Consequence for the source/Jost selector [D/I]

The physical Jost/Weyl observable is not an unweighted count of low eigenvalues.

It is built from the source vectors

\[
e^{\pm x}.
\]

Therefore the existence of many near-null bulk modes does not by itself destroy source-channel selection.

What fails is only the hard spectral isolation assumption.

The correct object is the source spectral measure.

Define

\[
d\sigma_{a,+}(\lambda)
=
d\langle
\cosh,
E_{B_a^{(+)}}(\lambda)
\cosh
\rangle,
\]

\[
d\sigma_{a,-}(\lambda)
=
d\langle
\sinh,
E_{B_a^{(-)}}(\lambda)
\sinh
\rangle.
\]

Then the exact susceptibilities are

\[
\boxed{
E_a(\delta)
=
\int_{[0,\infty)}
\frac{d\sigma_{a,+}(\lambda)}
{\lambda+\delta},
}
\tag{18}
\]

\[
\boxed{
O_a(\delta)
=
\int_{[0,\infty)}
\frac{d\sigma_{a,-}(\lambda)}
{\lambda+\delta}.
}
\tag{19}
\]

And the exact overlap selector remains

\[
\boxed{
\kappa_a(\delta)
=
\frac{E_a(\delta)-O_a(\delta)}
{E_a(\delta)+O_a(\delta)}.
}
\tag{20}
\]

Thus the right replacement for a spectral moat is a statement about which part of \(\sigma_{a,\pm}\) carries the source weight in the critical window.

---

## 9. Source-weighted dominance criterion [C]

Let the source spectral measures be decomposed into a candidate edge part and a bulk part,

\[
\sigma_{a,\pm}
=
\sigma_{a,\pm}^{\rm edge}
+
\sigma_{a,\pm}^{\rm bulk}.
\]

For a critical regulator \(\delta_a\downarrow0\), define

\[
E_{a}^{\rm bulk}(\delta_a)
=
\int
\frac{d\sigma_{a,+}^{\rm bulk}(\lambda)}
{\lambda+\delta_a},
\]

\[
O_{a}^{\rm bulk}(\delta_a)
=
\int
\frac{d\sigma_{a,-}^{\rm bulk}(\lambda)}
{\lambda+\delta_a}.
\]

A source-driven edge reduction is valid if

\[
\boxed{
E_{a}^{\rm bulk}(\delta_a)
=
o\!\left(
E_{a}^{\rm edge}(\delta_a)
\right),
}
\tag{Hsw+}
\]

and

\[
\boxed{
O_{a}^{\rm bulk}(\delta_a)
=
o\!\left(
O_{a}^{\rm edge}(\delta_a)
\right).
}
\tag{Hsw-}
\]

These are weighted Stieltjes conditions.

They allow arbitrarily many low complement eigenvalues.

Only their source residues must be negligible.

Under Hsw±, the exact overlap is asymptotically determined by the edge spectral measures alone.

---

## 10. Relation to v13.941 [R/I]

v13.941 already contained the correct general framework:

\[
G_-(x_\tau)
=
q_\tau
\left[
\frac r{x_\tau}
+
G_+(x_\tau)
\right].
\]

Its one-odd-pole specialization was explicitly conditional.

The present result shows why the **general rescaled spectral-measure formulation is the structurally correct asymptotic object**.

The one-pole model cannot be justified by a hard spectral moat, because no such fixed-rank moat exists under RH.

It could still hold source-weightedly if all other collapsing modes have asymptotically negligible source residues.

That question remains open.

---

## 11. Correction to v13.954 [R]

The exact algebraic statement of v13.954 remains valid:

if a two-dimensional almost-invariant edge plane has a uniform complement moat, reflection forces the \(2\times2\) Feshbach normal form.

What is ruled out is using that fixed-rank moat as the actual RH asymptotic mechanism for Suzuki's operator.

Thus the next physical target is **not**

\[
Q_aB_aQ_a\ge gQ_a.
\]

It is

\[
\boxed{
\textbf{source-weighted decoupling of the growing near-null bulk from }e^{\pm x}.
}
\tag{21}
\]

---

## 12. Next gate [O]

The source-faithful right-edge Riesz/Jost profile from v13.936–938 remains canonical.

The next nonredundant tasks are:

1. define an intrinsic edge/bulk decomposition of the source spectral measures \(\sigma_{a,\pm}\);
2. prove Hsw± in the overlap-defined critical window;
3. determine the rescaled edge spectral measures;
4. only then ask whether they collapse to a two-pole doublet or retain a nontrivial continuum/cluster;
5. compute the renormalized cross-edge source coupling from that measure-level limit.

The selector has moved from

\[
\text{isolated eigenstate}
\]

to

\[
\boxed{
\textbf{source-weighted low-energy spectral measure.}
}
\]

---

## 13. Result

Under RH, for every fixed parity and every fixed \(k\),

\[
\boxed{
\mu^{(\pm)}_{k,a}(B_a)
=
O(a^{-M})
\quad
\forall M>0.
}
\]

Therefore:

\[
\boxed{
\textbf{no fixed finite-rank low-energy subspace can have a uniform positive complement moat.}
}
\]

At the same time, the low-energy bulk trial spaces can satisfy

\[
\boxed{
\frac{
|\langle f,e^{\pm x}\rangle|
}{
\|e^{\pm x}\|_2
}
\le
C a^{1/2}e^{-\eta a},
}
\]

so spectral crowding and edge-source selection are compatible.

The correct next object is the source-weighted Stieltjes spectral measure, not a fixed-rank Feshbach doublet.
