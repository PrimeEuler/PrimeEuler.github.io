# Cone Derivation Ledger v13.965 — Sandbox: Xi Scalar as Centered Spectral-Shift Phase and Low-Height Interlacing Observable

**Date:** 2026-10-02  
**Track:** Sandbox / no-twist Suzuki Xi scalar lane  
**Status:** [D] exact centered spectral-shift formula for the scalar; [D] exact real-axis sign-phase formula; [D] uniform \(O(T^{-2})\) truncation bound from odd symmetry; [D] finite interlacing sum formula under the observed simple/interlacing regime; [N] independent 19-interval Xi-target check with rigorous phase-tail enclosure; [O] prove local convergence of the finite fixed-pair sign/interlacing pattern  
**Authorization:** Jeremy, 2026-10-02 ("yep. lets hit that scalar")  
**Parents:** v13.661, v13.684, v13.791–793, v13.966  
**Research artifact:** \`research-notes/xi_scalar_spectral_shift_check.py\`, commit \`3c57914e77057f17900c445b6412e0d50669adb6\`  
**Collision check:** v13.965 was absent immediately before this write. Note: this entry's parent was originally written and labeled v13.964; that entry was renumbered to v13.966 by the external audit thread to resolve a collision with "External Audit Round 147" (see that entry's header). References below have been updated accordingly.

---

## 0. Goal

v13.966 reduced the no-twist Xi scalar to the one-point rank-one resolvent trace

\[
\boxed{
\kappa_a^\Xi
=
-i\,
\operatorname{Tr}
\left[
(H_{a,0}-i)^{-1}
-
(H_{a,\pi}-i)^{-1}
\right].
}
\]

The present entry removes even the resolvent amplitudes.

The scalar depends only on the **real-axis phase/interlacing pattern** of the fixed extension pair.

---

## 1. Ordered-pair perturbation determinant [D]

Use the canonical normalized determinant

\[
\boxed{
\Delta_a(z)
=
\Delta_{0/\pi}^{(a)}(z;i)
=
\frac{m_a(z)}{m_a(i)}
=
\frac{m_a(z)}{i}.
}
\tag{1}
\]

Because

\[
m_a(i)=i,
\]

\[
\Delta_a(i)=1.
\]

From v13.966,

\[
\boxed{
\left.
\partial_z\log\Delta_a(z)
\right|_{z=i}
=
-i\kappa_a^\Xi.
}
\tag{2}
\]

---

## 2. Centered spectral-shift normalization [D]

For a rank-one self-adjoint extension pair, the perturbation determinant admits a spectral-shift representation.

The usual spectral shift is defined only up to an additive integer constant.

Because derivative observables are insensitive to constants, choose the **centered** normalization

\[
\widehat\xi_a(t)
\]

so that

\[
\boxed{
|\widehat\xi_a(t)|
\le
\frac12
}
\tag{3}
\]

almost everywhere.

Then

\[
\boxed{
\partial_z\log\Delta_a(z)
=
\int_{\mathbb R}
\frac{
\widehat\xi_a(t)
}{
(t-z)^2
}\,dt.
}
\tag{4}
\]

Any constant shift in \(\widehat\xi_a\) leaves (4) unchanged because

\[
\int_{\mathbb R}\frac{dt}{(t-z)^2}=0
\qquad
(z\in\mathbb C_+).
\]

---

## 3. Reflection symmetry makes the centered phase odd [D]

For the finite reflection-symmetric Suzuki pair,

\[
W_{a,0}(-z)
=
-W_{a,0}(z),
\]

while

\[
W_{a,\pi}(-z)
=
W_{a,\pi}(z).
\]

Since

\[
\frac{W_{a,0}}{W_{a,\pi}}
=
i\,m_a,
\]

we obtain

\[
\boxed{
m_a(-z)
=
-m_a(z).
}
\tag{5}
\]

On the real axis away from poles and zeros,

\[
m_a(t)\in\mathbb R.
\]

Since

\[
\Delta_a(t)
=
-i\,m_a(t),
\]

the centered boundary phase may be chosen as

\[
\boxed{
\widehat\xi_a(t)
=
-\frac12
\operatorname{sgn}m_a(t).
}
\tag{6}
\]

Therefore

\[
\boxed{
\widehat\xi_a(-t)
=
-\widehat\xi_a(t).
}
\tag{7}
\]

This oddness is the key to the improved tail bound.

---

## 4. Exact sign-phase formula for \(\kappa_a^\Xi\) [D]

Evaluate (4) at

\[
z=i.
\]

Using (2),

\[
-i\kappa_a^\Xi
=
\int_{\mathbb R}
\frac{
\widehat\xi_a(t)
}{
(t-i)^2
}\,dt.
\]

Pair the positive and negative half-lines using (7):

\[
\begin{aligned}
-i\kappa_a^\Xi
&=
\int_0^\infty
\widehat\xi_a(t)
\left[
\frac1{(t-i)^2}
-
\frac1{(t+i)^2}
\right]dt\\
&=
4i
\int_0^\infty
\widehat\xi_a(t)
\frac{t}{(1+t^2)^2}\,dt.
\end{aligned}
\]

Using (6),

\[
\boxed{
\kappa_a^\Xi
=
2
\int_0^\infty
\operatorname{sgn}m_a(t)
\frac{t}{(1+t^2)^2}\,dt.
}
\tag{8}
\]

This is exact.

The magnitude of \(m_a(t)\) has disappeared completely.

Only its sign/interlacing pattern remains.

---

## 5. Uniform finite-window truncation bound [D]

Define

\[
\boxed{
\kappa_a^\Xi(T)
=
2
\int_0^T
\operatorname{sgn}m_a(t)
\frac{t}{(1+t^2)^2}\,dt.
}
\tag{9}
\]

Since

\[
|\operatorname{sgn}m_a(t)|
\le1,
\]

\[
\begin{aligned}
|
\kappa_a^\Xi
-
\kappa_a^\Xi(T)
|
&\le
2
\int_T^\infty
\frac{t}{(1+t^2)^2}\,dt\\
&=
\frac1{1+T^2}.
\end{aligned}
\]

Hence

\[
\boxed{
|
\kappa_a^\Xi
-
\kappa_a^\Xi(T)
|
\le
\frac1{1+T^2}.
}
\tag{10}
\]

The bound is uniform in \(a\).

This is much stronger than the generic \(O(T^{-1})\) rank-one spectral-shift tail because reflection symmetry centers the phase and cancels the leading tail.

---

## 6. Immediate scalar convergence theorem [D/C]

Suppose that for every finite

\[
T>0,
\]

\[
\boxed{
\operatorname{sgn}m_a(t)
\longrightarrow
\operatorname{sgn}m_\infty(t)
}
\tag{Hsign}
\]

for almost every

\[
t\in(0,T)
\]

away from limiting zeros and poles.

Then dominated convergence in (9) gives

\[
\kappa_a^\Xi(T)
\to
\kappa_\infty^\Xi(T)
\]

for each fixed \(T\).

Using the uniform tail bound (10),

\[
\boxed{
\kappa_a^\Xi
\longrightarrow
\kappa_\Xi.
}
\tag{11}
\]

Therefore the Xi scalar requires only **local real-axis sign/interlacing convergence**.

No local-uniform convergence of \(m_a\) in \(\mathbb C_+\) is needed.

---

## 7. Equivalent local spectral-shift convergence criterion [D/C]

More invariantly, it is sufficient that

\[
\boxed{
\widehat\xi_a
\to
\widehat\xi_\infty
}
\tag{Hssf}
\]

weakly in \(L^1_{\rm loc}\), or weak-* in \(L^\infty_{\rm loc}\), on the real axis.

Since

\[
|\widehat\xi_a|
\le\frac12
\]

uniformly, local phase convergence plus (10) implies the scalar limit.

Thus the minimal real-axis scalar theorem is:

\[
\boxed{
\textbf{local convergence of the centered spectral shift for the fixed }(0,\pi)\textbf{ extension pair.}
}
\tag{12}
\]

---

## 8. Finite interlacing-sum formula [D/C]

Assume on a finite positive window that the fixed extension spectra are simple and interlace in the standard pattern.

Write:

- poles of \(m_a\) / \(\theta=\pi\) eigenvalues:
  \[
  \beta_{j,a}>0;
  \]
- zeros of \(m_a\) / \(\theta=0\) eigenvalues:
  \[
  \alpha_{j,a}>0.
  \]

Suppose

\[
m_a(t)>0
\]

near \(t=0^+\) and the negative sign intervals are

\[
(\beta_{j,a},\alpha_{j,a}).
\]

Since

\[
2
\int_0^\infty
\frac{t}{(1+t^2)^2}\,dt
=
1,
\]

each negative interval flips the sign and subtracts twice its positive-background contribution.

Therefore

\[
\boxed{
\kappa_a^\Xi
=
1
-
2
\sum_{j\ge1}
\left[
\frac1{1+\beta_{j,a}^2}
-
\frac1{1+\alpha_{j,a}^2}
\right].
}
\tag{13}
\]

For a partial sum through a completed interval ending at \(\alpha_{M,a}\),

\[
\boxed{
\left|
\kappa_a^\Xi
-
\left\{
1
-
2
\sum_{j=1}^{M}
\left[
\frac1{1+\beta_{j,a}^2}
-
\frac1{1+\alpha_{j,a}^2}
\right]
\right\}
\right|
\le
\frac1{1+\alpha_{M,a}^2}.
}
\tag{14}
\]

This gives a direct fixed-pair spectral certification scheme.

No source-resolvent inversion is required once the two interlacing spectra are certified.

---

## 9. Infinite Xi specialization [D/C]

For the Xi target, under the real-zero/de Branges regime,

\[
m_\infty(t)
=
-C_\infty
\frac{
\Xi'(t)
}{
\Xi(t)
},
\qquad
C_\infty>0.
\]

Let

\[
\gamma_j>0
\]

be positive Xi zeros and let

\[
\alpha_j
\]

denote the following positive critical points where

\[
\Xi'(\alpha_j)=0.
\]

On the numerically observed first intervals,

\[
m_\infty(t)>0
\]

on

\[
(0,\gamma_1),
\]

and the negative sign intervals are

\[
(\gamma_j,\alpha_j).
\]

Thus

\[
\boxed{
\kappa_\Xi
=
1
-
2
\sum_{j\ge1}
\left[
\frac1{1+\gamma_j^2}
-
\frac1{1+\alpha_j^2}
\right].
}
\tag{15}
\]

The fully invariant theorem remains the spectral-shift formula (8); equation (15) is the simple/interlacing realization of it.

---

## 10. Independent numerical Xi check [N]

The committed reproducer

\[
\texttt{xi\_scalar\_spectral\_shift\_check.py}
\]

uses:

\[
\Xi(t)
=
\xi(1/2+it),
\]

mpmath zeta-zero ordinates, and independently solves

\[
\Xi'(t)=0
\]

between consecutive positive zeros.

The exact derivative target is evaluated independently as

\[
\kappa_\Xi
=
\frac{\xi''(3/2)}{\xi'(3/2)}
-
\frac{\xi'(3/2)}{\xi(3/2)}.
\]

Selected partial sums are:

\[
\begin{array}{c|c}
M&
\kappa_\Xi^{(M)}
\\ \hline
1&
0.9982389679935265651
\\
2&
0.9978108423927056131
\\
3&
0.9975121119111339324
\\
4&
0.9974021417289742678
\\
5&
0.9972691784073492
\\
10&
0.9970440935008936
\\
15&
0.9969579971819076
\\
19&
0.9969216708895561
\end{array}
\tag{16}
\]

The exact derivative target is

\[
\boxed{
\kappa_\Xi
\approx
0.9968019520324009035.
}
\tag{17}
\]

After the nineteenth completed negative interval, the final critical point is approximately

\[
\alpha_{19}
\approx
76.22544.
\]

Therefore the rigorous phase-tail bound from (14) is approximately

\[
\boxed{
\frac1{1+\alpha_{19}^2}
\approx
1.72\times10^{-4}.
}
\tag{18}
\]

The exact target lies inside this enclosure.

This numerically confirms the spectral-shift formula without using the derivative expression to construct the partial sum.

---

## 11. Practical certification consequence [D/I]

To certify

\[
\kappa_a^\Xi
\]

to tolerance \(\varepsilon\), it is enough to know the sign/interlacing pattern through

\[
\boxed{
T
\ge
\sqrt{\varepsilon^{-1}-1}.
}
\tag{19}
\]

Examples:

\[
\varepsilon=10^{-3}
\quad\Longrightarrow\quad
T\gtrsim31.6,
\]

\[
\varepsilon=10^{-4}
\quad\Longrightarrow\quad
T\gtrsim100.
\]

Thus the scalar convergence problem is genuinely **low-height**.

This is materially easier than controlling a full infinite Weyl function or the complete near-null source-resolvent spectrum.

---

## 12. Correct next finite-\(a\) gate [O]

The next computation should no longer begin from

\[
A_a^{-1}
\]

or separately huge parity energies.

Instead, for increasing \(a\), certify the two fixed self-adjoint extension spectra on a bounded real window:

\[
W_{a,\pi}(t)=0,
\qquad
W_{a,0}(t)=0.
\]

Then:

1. verify their interlacing/sign pattern;
2. construct
   \[
   \operatorname{sgn}m_a(t);
   \]
3. integrate (9), or use the endpoint sum (13);
4. append the universal tail enclosure (10);
5. compare directly with
   \[
   \kappa_\Xi.
   \]

This avoids the unstable common scale of the two source-resolvent quadratic forms.

---

## 13. Result

The no-twist Xi scalar is exactly the centered spectral-shift phase moment

\[
\boxed{
\kappa_a^\Xi
=
2
\int_0^\infty
\operatorname{sgn}m_a(t)
\frac{t}{(1+t^2)^2}\,dt.
}
\]

Its finite-height truncation satisfies the uniform bound

\[
\boxed{
|
\kappa_a^\Xi-\kappa_a^\Xi(T)
|
\le
\frac1{1+T^2}.
}
\]

Therefore:

\[
\boxed{
\textbf{local fixed-pair interlacing convergence is sufficient for the Xi scalar limit.}
}
\]

This is strictly weaker than full Weyl convergence and gives a practical low-height certification route.
