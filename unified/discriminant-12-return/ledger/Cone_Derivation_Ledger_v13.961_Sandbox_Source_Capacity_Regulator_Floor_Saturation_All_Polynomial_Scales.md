# Cone Derivation Ledger v13.961 — Sandbox: RH-Conditional Source-Capacity Regulator-Floor Saturation at Every Polynomial Scale

**Date:** 2026-10-02  
**Track:** Sandbox / untwisted Suzuki source-capacity and source-RG lane  
**Status:** [D] RH-conditional construction of zero-aware source-normalized even/odd trial families; [D] exact regulator-floor lower bound; [D] matching logarithmic capacity exponent at every fixed polynomial regulator scale; [R] sharpens the interpretation of v13.959 — \(N^{-1}\) is distinguished inside the zero-blind class but physical source capacities do not select a unique power exponent; [O] determine subexponential/constant parity asymptotics and the physical first-crossing location  
**Authorization:** Jeremy, 2026-10-02 ("lets try and get those closed!")  
**Parents:** v13.947, v13.958–960  
**Collision check:** v13.961 was absent in the live tree immediately before this write.

---

## 0. Main result

Let

\[
N_a=e^{2a}
\]

and let

\[
\mathcal C_{a,\pm}(\delta)
=
\inf_{\langle f_{\pm,a},g\rangle=1}
\left[
\langle g,B_a^{(\pm)}g\rangle
+
\delta\|g\|_2^2
\right]
\]

be the parity source capacities of v13.958, where

\[
B_a=A_a-\lambda_a I\ge0,
\]

\[
f_{+,a}=\sqrt2\,e^{-a}\cosh x,
\qquad
f_{-,a}=\sqrt2\,e^{-a}\sinh x.
\]

Assume RH.

Then for every fixed

\[
\beta>0
\]

and every fixed

\[
c>0,
\]

\[
\boxed{
\mathcal C_{a,\pm}
\!\left(
cN_a^{-\beta}
\right)
=
N_a^{-\beta+o(1)}.
}
\tag{1}
\]

The \(o(1)\) is in the logarithmic exponent as \(a\to\infty\), and can be taken uniformly for \(c\) in compact subsets of \((0,\infty)\).

Equivalently,

\[
\boxed{
\lim_{a\to\infty}
\frac{
\log
\mathcal C_{a,\pm}(cN_a^{-\beta})
}{
\log N_a
}
=
-\beta.
}
\tag{2}
\]

Thus the physical source capacities saturate the regulator-floor exponent at **every fixed polynomial regulator scale**.

Consequently, exponent matching alone cannot determine the physical critical exponent \(\beta\).

---

## 1. Universal regulator-floor lower bound [D]

For either parity, if

\[
\langle f_{\pm,a},g\rangle=1,
\]

then Cauchy–Schwarz gives

\[
\|g\|_2^2
\ge
\frac1{\|f_{\pm,a}\|_2^2}.
\]

Since

\[
B_a\ge0,
\]

\[
\boxed{
\mathcal C_{a,\pm}(\delta)
\ge
\frac{\delta}{\|f_{\pm,a}\|_2^2}.
}
\tag{3}
\]

From v13.956,

\[
\|f_{\pm,a}\|_2^2
=
M_{\pm,a}
=
\frac{1-e^{-4a}}2
\pm
2ae^{-2a},
\]

so

\[
M_{\pm,a}\to\frac12.
\]

Therefore for

\[
\delta=cN_a^{-\beta},
\]

\[
\boxed{
\mathcal C_{a,\pm}(cN_a^{-\beta})
\ge
(2c+o(1))
N_a^{-\beta}.
}
\tag{4}
\]

This bound is unconditional.

The matching upper exponent below is RH-conditional.

---

## 2. Zero ordinates and a fixed Gevrey smoothing density [D, conditional on RH]

Assume RH and enumerate the positive zero ordinates

\[
0<\gamma_1\le\gamma_2\le\cdots
\]

with multiplicity.

Fix

\[
0<\eta<1.
\]

Choose once and for all an even nonnegative compactly supported Gevrey probability density

\[
\rho\in C_c^\infty(-L,L),
\qquad
\int\rho=1,
\]

whose Fourier transform

\[
R(t)=\widehat\rho(t)
\]

satisfies

\[
\boxed{
|R(t)|
\le
C e^{-c|t|^\eta}.
}
\tag{5}
\]

Also

\[
R(-i)
=
\int\rho(x)e^x\,dx
>0.
\]

---

## 3. Exact zero-annihilating Bernoulli factors [D]

For

\[
j\ge2,
\]

define the minimal positive annihilating displacement

\[
\boxed{
\ell_j
=
\frac{\pi}{2\gamma_j}.
}
\tag{6}
\]

Let

\[
\nu_j
=
\frac12
\left(
\delta_{+\ell_j}
+
\delta_{-\ell_j}
\right).
\]

Then

\[
\widehat\nu_j(t)
=
\cos(\ell_j t),
\]

and

\[
\boxed{
\widehat\nu_j(\gamma_j)=0.
}
\tag{7}
\]

The support cost through \(M\) is

\[
\boxed{
A_M
=
\sum_{j=2}^{M}\ell_j.
}
\tag{8}
\]

By Riemann–von Mangoldt,

\[
\gamma_j\asymp\frac{j}{\log j},
\]

so

\[
\boxed{
A_M
=
O((\log M)^2).
}
\tag{9}
\]

Also

\[
\sum_{j=2}^{\infty}\ell_j^2<\infty.
\]

Hence

\[
\boxed{
1
\le
\prod_{j=2}^{M}\cosh(\ell_j)
\le
C_\infty<\infty
}
\tag{10}
\]

uniformly in \(M\).

---

## 4. One large source-aligned annihilating displacement [D]

The first zero can be annihilated at any displacement

\[
\boxed{
\ell_{1,k}
=
\frac{
\pi/2+k\pi
}{
\gamma_1},
\qquad
k\in\mathbb N_0.
}
\tag{11}
\]

The spacing is

\[
\frac{\pi}{\gamma_1}.
\]

For \(a\) large and \(M=M(a)\) chosen below, select \(k=k(a)\) so that

\[
\boxed{
a-L-A_M-\frac{\pi}{\gamma_1}
\le
\ell_{1,a}
\le
a-L-A_M.
}
\tag{12}
\]

Then the full convolution support remains inside

\[
[-a,a].
\]

Define

\[
\nu_{1,a}
=
\frac12
\left(
\delta_{+\ell_{1,a}}
+
\delta_{-\ell_{1,a}}
\right).
\]

It still satisfies

\[
\widehat\nu_{1,a}(\gamma_1)=0.
\]

The role of the large branch is crucial: it preserves an exponentially large \(e^x\)-moment while annihilating the first zero exactly.

---

## 5. Smooth even zero-aware probability trial [D]

Set

\[
\boxed{
p_a
=
\rho
*
\nu_{1,a}
*
\nu_2
*
\cdots
*
\nu_{M(a)}.
}
\tag{13}
\]

Then:

- \(p_a\ge0\);
- \(p_a\) is even;
- \(p_a\in C_c^\infty(-a,a)\);
- \(\int p_a=1\).

Its Fourier transform is

\[
\boxed{
P_a(t)
=
R(t)
\cos(\ell_{1,a}t)
\prod_{j=2}^{M(a)}
\cos(\ell_j t).
}
\tag{14}
\]

Therefore

\[
\boxed{
P_a(\gamma_j)=0
\qquad
1\le j\le M(a).
}
\tag{15}
\]

For every remaining zero,

\[
\boxed{
|P_a(\gamma_j)|
\le
|R(\gamma_j)|
\le
C e^{-c\gamma_j^\eta}.
}
\tag{16}
\]

---

## 6. Choice of the annihilation depth [D]

Choose a fixed exponent

\[
K>\frac1\eta
\]

and set

\[
\boxed{
M(a)
=
\lceil a^K\rceil.
}
\tag{17}
\]

Then

\[
A_{M(a)}
=
O((\log a)^2)
=
o(a).
\tag{18}
\]

Also

\[
\gamma_{M(a)}
\gg
\frac{
a^K
}{
\log a
}.
\]

Hence

\[
\boxed{
\gamma_{M(a)}^\eta
\gg
\frac{
a^{K\eta}
}{
(\log a)^\eta
}
\gg a.
}
\tag{19}
\]

Thus the surviving zero tail is suppressed faster than every prescribed exponential \(e^{-Ca}\).

---

## 7. Super-exponentially small Weil energy [D, conditional on RH]

Under RH,

\[
Q_W[g]
=
\sum_\gamma
m_\gamma
|\widehat g(\gamma)|^2.
\]

Using (15)–(19) and zero counting,

\[
\boxed{
Q_W[p_a]
\le
\exp[-\omega(a)],
}
\tag{20}
\]

where

\[
\boxed{
\frac{\omega(a)}a\to\infty.
}
\tag{21}
\]

For the odd derivative,

\[
\widehat{p_a'}(\gamma)
=
i\gamma P_a(\gamma).
\]

The extra polynomial factor is absorbed by the Gevrey tail, so

\[
\boxed{
Q_W[p_a']
\le
\exp[-\omega_1(a)],
\qquad
\frac{\omega_1(a)}a\to\infty.
}
\tag{22}
\]

Because under RH

\[
\lambda_a\ge0
\]

and

\[
B_a=A_a-\lambda_a I,
\]

\[
0\le
\langle g,B_ag\rangle
\le
Q_W[g].
\tag{23}
\]

Thus the same upper bounds hold for the recentered energy.

---

## 8. Source overlap is only subexponentially small [D]

At the imaginary source point,

\[
P_a(-i)
=
R(-i)
\cosh(\ell_{1,a})
\prod_{j=2}^{M(a)}
\cosh(\ell_j).
\]

Using (10) and (12),

\[
\boxed{
P_a(-i)
\ge
c_0
\exp\!\left[
a-A_{M(a)}-C_0
\right].
}
\tag{24}
\]

The normalized even source is

\[
f_{+,a}
=
\sqrt2 e^{-a}\cosh x.
\]

Since \(p_a\) is even,

\[
\langle f_{+,a},p_a\rangle
=
\sqrt2e^{-a}P_a(-i).
\]

Therefore

\[
\boxed{
|\langle f_{+,a},p_a\rangle|
\ge
c_1
e^{-A_{M(a)}}.
}
\tag{25}
\]

Because

\[
A_{M(a)}=O((\log a)^2),
\]

the inverse squared source-overlap cost is

\[
\boxed{
|\langle f_{+,a},p_a\rangle|^{-2}
\le
\exp[O((\log a)^2)]
=
N_a^{o(1)}.
}
\tag{26}
\]

---

## 9. Odd source has the same overlap [D]

Let

\[
g_a=p_a'.
\]

Then \(g_a\) is odd and compactly supported.

Integration by parts gives

\[
\begin{aligned}
\langle f_{-,a},g_a\rangle
&=
\sqrt2e^{-a}
\int
\sinh x\,p_a'(x)\,dx\\
&=
-\sqrt2e^{-a}
\int
\cosh x\,p_a(x)\,dx.
\end{aligned}
\]

Therefore

\[
\boxed{
|\langle f_{-,a},p_a'\rangle|
=
|\langle f_{+,a},p_a\rangle|.
}
\tag{27}
\]

So the same source-normalization cost applies in both parities.

---

## 10. Uniform \(L^2\) control [D]

Convolution by a probability measure is an \(L^2\)-contraction.

Hence

\[
\boxed{
\|p_a\|_2
\le
\|\rho\|_2,
}
\tag{28}
\]

and because differentiation may be placed on the fixed smooth factor,

\[
\boxed{
\|p_a'\|_2
\le
\|\rho'\|_2.
}
\tag{29}
\]

After normalizing to unit source overlap, both squared norms are at most

\[
\boxed{
N_a^{o(1)}.
}
\tag{30}
\]

---

## 11. Matching source-capacity upper exponent [D/C]

Fix

\[
\beta>0,
\qquad
c>0,
\]

and set

\[
\delta_a=cN_a^{-\beta}.
\]

Normalize \(p_a\) and \(p_a'\) to satisfy the corresponding unit source constraints.

The recentered energy terms are, by §§7–9,

\[
o(N_a^{-\beta}),
\]

because their decay is super-exponential in \(a\) even after the \(N_a^{o(1)}\) source-normalization cost.

The regulator terms satisfy

\[
\delta_a
\|g\|_2^2
\le
N_a^{-\beta+o(1)}.
\]

Therefore

\[
\boxed{
\mathcal C_{a,+}(cN_a^{-\beta})
\le
N_a^{-\beta+o(1)},
}
\tag{31}
\]

\[
\boxed{
\mathcal C_{a,-}(cN_a^{-\beta})
\le
N_a^{-\beta+o(1)}.
}
\tag{32}
\]

Together with (4),

\[
\boxed{
\mathcal C_{a,\pm}(cN_a^{-\beta})
=
N_a^{-\beta+o(1)}.
}
\tag{33}
\]

This proves the main theorem.

---

## 12. Uniformity in the finite scale parameter [D]

If

\[
c\in[c_0,c_1]
\Subset(0,\infty),
\]

the lower bound (4) and the upper construction above are uniform in \(c\).

Thus

\[
\boxed{
\sup_{c\in[c_0,c_1]}
\left|
\frac{
\log
\mathcal C_{a,\pm}(cN_a^{-\beta})
}{
\log N_a
}
+
\beta
\right|
\to0.
}
\tag{34}
\]

So the regulator-floor exponent is stable throughout every compact \(c\)-window.

---

## 13. Consequence for the parity ratio [D/I]

Because

\[
G_{a,\pm}(\delta)
=
\mathcal C_{a,\pm}(\delta)^{-1},
\]

for every fixed \(\beta>0\),

\[
\boxed{
G_{a,\pm}(cN_a^{-\beta})
=
N_a^{\beta+o(1)}.
}
\tag{35}
\]

Hence

\[
\boxed{
\frac{
G_{a,-}(cN_a^{-\beta})
}{
G_{a,+}(cN_a^{-\beta})
}
=
N_a^{o(1)}.
}
\tag{36}
\]

Thus both parity channels have the same logarithmic exponent at every fixed polynomial scale.

The critical first crossing

\[
G_{a,-}/G_{a,+}=q_\tau
\]

is therefore controlled entirely by the **subexponential and constant-level parity structure**.

Power-exponent matching cannot select the crossing.

---

## 14. Correction/refinement of v13.959 [R]

v13.959 proves an exact and useful zero-blind balance law:

\[
\Omega=\beta.
\]

At canonical \(\Omega=1\), this distinguishes

\[
\delta=N^{-1}
\]

inside the zero-blind Klein–Gordon/Chebyshev trial class.

That theorem stands.

The present result shows that the unrestricted physical source capacities can use arithmetic/zero-aware trial directions and beat the zero-blind capacity exponent down to the regulator floor, up to subexponential factors.

Therefore:

\[
\boxed{
\textbf{\(N^{-1}\) is a canonical zero-blind source scale, but not a physical capacity exponent selected by leading-order variational asymptotics.}
}
\tag{37}
\]

The actual physical first crossing still requires the source-RG ratio of v13.958.

---

## 15. What is now closed

Under RH, for every fixed \(\beta>0\),

\[
\boxed{
\mathcal C_{a,+}(N^{-\beta})
\text{ and }
\mathcal C_{a,-}(N^{-\beta})
}
\]

have the same exact logarithmic exponent

\[
-\beta.
\]

Thus:

\[
\boxed{
\textbf{no fixed polynomial exponent can be selected from the separate parity-capacity decay rates.}
}
\]

The scale-selection information lives one order deeper:

\[
\boxed{
\text{subexponential prefactors and the parity Stieltjes ratio.}
}
\]

---

## 16. Next nonredundant gate [O]

The remaining physical problem is now unambiguously a **relative** asymptotic problem.

The next quantities to study are

\[
\boxed{
\frac{
\mathcal C_{a,+}(c/N_a)
}{
\mathcal C_{a,-}(c/N_a)
}
}
\]

and, more generally,

\[
\boxed{
\frac{
\mathcal C_{a,+}(cN_a^{-\beta})
}{
\mathcal C_{a,-}(cN_a^{-\beta})
}.
}
\]

The leading power \(N^{-\beta}\) cancels identically in logarithmic scale.

A physical \(N^{-1}\) theorem must therefore come from a genuine parity-dependent next-order asymptotic or a source-RG fixed-point identity — not from the common capacity exponent.
