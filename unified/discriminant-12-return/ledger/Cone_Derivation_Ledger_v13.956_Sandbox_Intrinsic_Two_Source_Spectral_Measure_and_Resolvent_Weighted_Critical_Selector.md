# Cone Derivation Ledger v13.956 — Sandbox: Intrinsic Two-Source Spectral Measure and Resolvent-Weighted Critical Selector

**Date:** 2026-10-02  
**Track:** Sandbox / untwisted Suzuki selector and critical low-energy lane  
**Status:** [D] exact matrix-valued source spectral measure; [D] exact overlap-as-resolvent-coherence identity; [D] universal parity weights at intrinsic critical scaling; [D] compactness target for the scaled source spectral state; [I] replaces fixed-rank edge-doublet selection by a source-weighted measure selector; [O] prove tightness and identify the scaled limiting measure  
**Authorization:** Jeremy, 2026-10-02 ("perfect. lets hit that gate!")  
**Parents:** v13.936–941, v13.953–955  
**Collision check:** v13.956 was absent in the live tree immediately before this write.

---

## 0. Why this is the correct repair

v13.955 proves that under RH every fixed finite number of even and odd recentered eigenvalues collapses toward zero. Hence no fixed-rank protected subspace can retain a uniform complement moat.

At the same time, the physical Jost/deficiency observable is not an unweighted spectral count. It is driven by the two source vectors

\[
e^{x},
\qquad
e^{-x}.
\]

The correct asymptotic object is therefore the **source-weighted spectral measure** of the recentered operator.

No spatial edge/bulk cutoff is needed.

---

## 1. Native normalized right/left sources [D]

Let

\[
B_a=A_a-\lambda_a I\ge0.
\]

Define

\[
\boxed{
f_{R,a}(x)
=
e^{-a}e^x,
}
\tag{1}
\]

\[
\boxed{
f_{L,a}(x)
=
e^{-a}e^{-x}.
}
\tag{2}
\]

Reflection satisfies

\[
Rf_{R,a}=f_{L,a}.
\]

The normalization is canonical from the right/left edge coordinates:

\[
x=a-\xi
\quad\Longrightarrow\quad
f_{R,a}(a-\xi)=e^{-\xi}.
\]

Thus the right source has a nontrivial fixed half-line profile without any fitted scale.

---

## 2. Exact raw source masses [D]

Direct integration gives

\[
\begin{aligned}
\|f_{R,a}\|_2^2
&=
e^{-2a}
\int_{-a}^{a}e^{2x}\,dx\\
&=
e^{-2a}\sinh(2a)\\
&=
\boxed{
\frac{1-e^{-4a}}2.
}
\end{aligned}
\tag{3}
\]

By reflection,

\[
\|f_{L,a}\|_2^2
=
\frac{1-e^{-4a}}2.
\]

The raw right/left overlap is

\[
\begin{aligned}
\langle f_{R,a},f_{L,a}\rangle
&=
e^{-2a}
\int_{-a}^{a}1\,dx\\
&=
\boxed{
2ae^{-2a}.
}
\end{aligned}
\tag{4}
\]

Therefore the unweighted source coherence is

\[
\boxed{
\chi_a^{\rm raw}
=
\frac{
\langle f_{R,a},f_{L,a}\rangle
}{
\|f_{R,a}\|_2^2
}
=
\frac{
4ae^{-2a}
}{
1-e^{-4a}
}
\sim
4ae^{-2a}.
}
\tag{5}
\]

So the bare left/right source vectors become exponentially orthogonal.

---

## 3. Matrix-valued source spectral measure [D]

Let

\[
E_a(d\lambda)
\]

be the projection-valued spectral measure of \(B_a\).

Define the \(2\times2\) positive-semidefinite matrix measure

\[
\boxed{
d\Sigma_a(\lambda)
=
\begin{pmatrix}
\langle f_{R,a},E_a(d\lambda)f_{R,a}\rangle
&
\langle f_{R,a},E_a(d\lambda)f_{L,a}\rangle
\\[1mm]
\langle f_{L,a},E_a(d\lambda)f_{R,a}\rangle
&
\langle f_{L,a},E_a(d\lambda)f_{L,a}\rangle
\end{pmatrix}.
}
\tag{6}
\]

Because \(B_a\) commutes with reflection,

\[
RE_a(S)=E_a(S)R
\]

for every Borel set \(S\).

Hence

\[
\boxed{
d\Sigma_a(\lambda)
=
\begin{pmatrix}
d\rho_a(\lambda)&d\eta_a(\lambda)\\
d\eta_a(\lambda)&d\rho_a(\lambda)
\end{pmatrix},
}
\tag{7}
\]

with \(d\rho_a\) positive and \(d\eta_a\) real signed.

Positivity of the matrix measure is equivalent to

\[
\boxed{
d\rho_a+d\eta_a\ge0,
\qquad
d\rho_a-d\eta_a\ge0.
}
\tag{8}
\]

Thus

\[
|d\eta_a|
\le
d\rho_a
\]

in the measure sense.

The total masses are exactly

\[
\boxed{
\rho_a([0,\infty))
=
\frac{1-e^{-4a}}2,
}
\tag{9}
\]

\[
\boxed{
\eta_a([0,\infty))
=
2ae^{-2a}.
}
\tag{10}
\]

---

## 4. Resolvent matrix [D]

For \(\delta>0\), define

\[
\boxed{
\mathcal G_a(\delta)
=
\int_{[0,\infty)}
\frac{d\Sigma_a(\lambda)}
{\lambda+\delta}.
}
\tag{11}
\]

By (7),

\[
\boxed{
\mathcal G_a(\delta)
=
\begin{pmatrix}
R_a(\delta)&X_a(\delta)\\
X_a(\delta)&R_a(\delta)
\end{pmatrix},
}
\tag{12}
\]

where

\[
\boxed{
R_a(\delta)
=
\int
\frac{d\rho_a(\lambda)}
{\lambda+\delta},
}
\tag{13}
\]

\[
\boxed{
X_a(\delta)
=
\int
\frac{d\eta_a(\lambda)}
{\lambda+\delta}.
}
\tag{14}
\]

Equivalently,

\[
R_a(\delta)
=
\langle
f_{R,a},
(B_a+\delta I)^{-1}
f_{R,a}
\rangle,
\]

\[
X_a(\delta)
=
\langle
f_{R,a},
(B_a+\delta I)^{-1}
f_{L,a}
\rangle.
\]

---

## 5. Exact deficiency-overlap identity [D]

The recentered deficiency vectors are

\[
v_{a,+}^{\delta}
=
(B_a+\delta I)^{-1}e^x,
\]

\[
v_{a,-}^{\delta}
=
(B_a+\delta I)^{-1}e^{-x}.
\]

The energy-overlap parameter is

\[
\kappa_a(\delta)
=
\frac{
\langle
v_{a,+}^{\delta},
v_{a,-}^{\delta}
\rangle_{B_a+\delta}
}{
\|v_{a,+}^{\delta}\|_{B_a+\delta}^2
}.
\]

Using

\[
(B_a+\delta)v_{a,-}^{\delta}=e^{-x},
\]

\[
(B_a+\delta)v_{a,+}^{\delta}=e^{x},
\]

we obtain

\[
\kappa_a(\delta)
=
\frac{
\langle
e^{x},
(B_a+\delta I)^{-1}
e^{-x}
\rangle
}{
\langle
e^{x},
(B_a+\delta I)^{-1}
e^{x}
\rangle
}.
\]

The common factor \(e^{2a}\) cancels under the normalized sources.

Therefore

\[
\boxed{
\kappa_a(\delta)
=
\frac{
X_a(\delta)
}{
R_a(\delta)
}.
}
\tag{15}
\]

This is exact.

So the intrinsic deficiency overlap is the **resolvent-weighted right/left spectral coherence**.

---

## 6. Parity diagonalization [D]

Define normalized parity sources

\[
\boxed{
f_{+,a}
=
\frac{
f_{R,a}+f_{L,a}
}{\sqrt2},
}
\tag{16}
\]

\[
\boxed{
f_{-,a}
=
\frac{
f_{R,a}-f_{L,a}
}{\sqrt2}.
}
\tag{17}
\]

Then \(f_{+,a}\) is even and \(f_{-,a}\) is odd.

Their spectral measures are

\[
\boxed{
d\sigma_{a,+}
=
d\rho_a+d\eta_a,
}
\tag{18}
\]

\[
\boxed{
d\sigma_{a,-}
=
d\rho_a-d\eta_a.
}
\tag{19}
\]

Their resolvent quadratic forms are

\[
\boxed{
G_{a,+}(\delta)
=
R_a(\delta)+X_a(\delta),
}
\tag{20}
\]

\[
\boxed{
G_{a,-}(\delta)
=
R_a(\delta)-X_a(\delta).
}
\tag{21}
\]

Since

\[
\cosh x
=
\frac{e^a}{\sqrt2}f_{+,a},
\]

\[
\sinh x
=
\frac{e^a}{\sqrt2}f_{-,a},
\]

the v13.940 parity susceptibilities satisfy

\[
E_a(\delta)
=
\frac{e^{2a}}2G_{a,+}(\delta),
\]

\[
O_a(\delta)
=
\frac{e^{2a}}2G_{a,-}(\delta).
\]

Thus

\[
\kappa_a
=
\frac{E_a-O_a}{E_a+O_a}
=
\frac{X_a}{R_a},
\]

in agreement with (15).

---

## 7. Universal critical parity fractions [D]

At the intrinsic double-scaling point of v13.940,

\[
\boxed{
\kappa_a(\delta_\tau(a))
=
e^{-\tau}.
}
\tag{22}
\]

Hence

\[
X_a(\delta_\tau)
=
e^{-\tau}R_a(\delta_\tau).
\]

Therefore

\[
G_{a,+}(\delta_\tau)
=
(1+e^{-\tau})R_a(\delta_\tau),
\]

\[
G_{a,-}(\delta_\tau)
=
(1-e^{-\tau})R_a(\delta_\tau).
\]

The normalized parity fractions of the source-resolvent response are therefore exactly

\[
\boxed{
w_+(\tau)
=
\frac{1+e^{-\tau}}2,
}
\tag{23}
\]

\[
\boxed{
w_-(\tau)
=
\frac{1-e^{-\tau}}2.
}
\tag{24}
\]

These are independent of:

- the number of low modes;
- any one-pole approximation;
- any spectral moat;
- RH;
- the detailed distribution of source residues.

For the one-e-fold convention \(\tau=1\),

\[
w_+(1)
=
\frac{1+e^{-1}}2
\approx0.6839397,
\]

\[
w_-(1)
=
\frac{1-e^{-1}}2
\approx0.3160603.
\]

So the intrinsic critical selector fixes a universal **source-weighted parity mixture**, not necessarily an isolated even/odd eigenpair.

---

## 8. Resolvent amplification of exponentially small raw coherence [D/I]

The raw source coherence from (5) is

\[
\chi_a^{\rm raw}
\sim
4ae^{-2a}.
\]

At the critical regulator,

\[
\chi_a^{\rm resolvent}
=
\kappa_a(\delta_\tau)
=
e^{-\tau}.
\]

Therefore the ratio of resolvent coherence to raw coherence is

\[
\boxed{
\frac{
\chi_a^{\rm resolvent}
}{
\chi_a^{\rm raw}
}
=
\frac{
e^{-\tau}(1-e^{-4a})
}{
4ae^{-2a}
}
\sim
\frac{e^{2a-\tau}}{4a}.
}
\tag{25}
\]

Thus the critical resolvent amplifies an exponentially small bare left/right overlap into an order-one coherence.

This is an exact quantitative statement of low-energy selection.

It does not identify which individual low eigenmodes carry that amplification.

---

## 9. Canonical resolvent-weighted critical matrix state [D]

At

\[
\delta_a:=\delta_\tau(a),
\]

define the matrix-valued measure

\[
\boxed{
d\Pi_{a,\tau}(\lambda)
=
\frac1{R_a(\delta_a)}
\frac{
d\Sigma_a(\lambda)
}{
\lambda+\delta_a
}.
}
\tag{26}
\]

It is positive semidefinite.

Its total mass matrix is exactly

\[
\boxed{
\Pi_{a,\tau}([0,\infty))
=
\begin{pmatrix}
1&e^{-\tau}\\
e^{-\tau}&1
\end{pmatrix}.
}
\tag{27}
\]

In the parity basis the total matrix is diagonal:

\[
\boxed{
\operatorname{diag}
\left(
1+e^{-\tau},
1-e^{-\tau}
\right).
}
\tag{28}
\]

Thus the intrinsic critical scaling canonically normalizes the source spectral measure.

No edge/bulk cutoff and no individual eigenvalue labeling enter.

---

## 10. Dimensionless critical rescaling [D/O]

Push the critical matrix state to the dimensionless variable

\[
u
=
\frac{\lambda}{\delta_a}.
\]

Define

\[
\boxed{
\widetilde\Pi_{a,\tau}(S)
=
\Pi_{a,\tau}(\delta_a S),
\qquad
S\subset[0,\infty).
}
\tag{29}
\]

The total matrix remains (27).

Because the diagonal total masses are fixed, the family is weak-* precompact on the one-point compactification

\[
[0,\infty].
\]

Hence every sequence \(a_n\to\infty\) has a subsequence along which

\[
\boxed{
\widetilde\Pi_{a_n,\tau}
\Longrightarrow
\widetilde\Pi_{\infty,\tau}
}
\tag{30}
\]

as a positive matrix-valued measure on \([0,\infty]\).

The limiting total mass is still

\[
\boxed{
\begin{pmatrix}
1&e^{-\tau}\\
e^{-\tau}&1
\end{pmatrix}.
}
\tag{31}
\]

The only remaining compactness issue is whether mass escapes to

\[
u=\infty.
\]

If one proves tightness on \([0,\infty)\), then the critical selector has a genuine dimensionless source spectral profile.

---

## 11. Correct replacement for the one-pole/doublet picture [I/R]

v13.941's one-pole crossover and v13.953's edge-doublet crossover remain valid conditional reductions.

But v13.955 shows that fixed-rank spectral isolation cannot be the general RH asymptotic mechanism.

The present entry gives the structurally correct replacement:

\[
\boxed{
\textbf{the selected object is the critical resolvent-weighted two-source spectral measure } \widetilde\Pi_{a,\tau}.
}
\tag{32}
\]

A two-pole edge doublet is now one possible special limiting form of this matrix measure.

It is not assumed.

If the limit instead has several atoms or a continuous component, the exact overlap selector still remains valid.

---

## 12. Interaction with the zero-blind cone/sieve scale [O]

v13.950 gives the exact zero-blind arithmetic scale

\[
e^{-2a}
=
N_a^{-1}
\]

at canonical unit stopband normalization.

The natural next test is therefore not

\[
e^{2a}\Delta_a\to C
\]

for a single eigenvalue.

It is whether the overlap-defined regulator satisfies

\[
\boxed{
N_a\delta_\tau(a)
}
\]

with a finite nonzero limit, and whether the scaled source spectral state

\[
\widetilde\Pi_{a,\tau}
\]

has a unique tight limit under that normalization.

That question remains open.

---

## 13. Next gate [O]

The next nonredundant tasks are now exact:

1. prove or disprove
   \[
   N_a\delta_\tau(a)\to C_\tau\in(0,\infty);
   \]

2. establish tightness of
   \[
   \widetilde\Pi_{a,\tau}
   \]
   on \([0,\infty)\);

3. determine whether the limit is:
   - a two-atom reflection doublet;
   - a finite cluster;
   - or a genuine source-weighted continuum;

4. identify the renormalized cross-edge/Jost observable directly from the limiting matrix measure.

This is the correct source-faithful selection problem after the fixed-rank moat obstruction.

---

## 14. Result

The exact untwisted selector can be written without any isolated-state hypothesis.

Let

\[
d\Sigma_a
=
\begin{pmatrix}
d\rho_a&d\eta_a\\
d\eta_a&d\rho_a
\end{pmatrix}
\]

be the native right/left source spectral measure of the recentered Suzuki operator.

Then

\[
\boxed{
\kappa_a(\delta)
=
\frac{
\int(\lambda+\delta)^{-1}d\eta_a
}{
\int(\lambda+\delta)^{-1}d\rho_a
}.
}
\]

At the intrinsic scaling point

\[
\kappa_a=e^{-\tau},
\]

the resolvent-weighted critical state has universal total matrix

\[
\boxed{
\begin{pmatrix}
1&e^{-\tau}\\
e^{-\tau}&1
\end{pmatrix}.
}
\]

Thus the selector is fundamentally a **source-weighted low-energy matrix measure**.

The next question is its dimensionless scaling limit, not the isolation of one even/odd doublet.
