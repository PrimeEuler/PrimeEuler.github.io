# Cone Derivation Ledger v13.959 — Sandbox: Zero-Blind Source-Capacity Balance and the Distinguished \(N^{-1}\) Regulator Scale

**Date:** 2026-10-02  
**Track:** Sandbox / untwisted Suzuki source-capacity and cone-RG lane  
**Status:** [D] exact source-capacity variational formulation reused from v13.958; [C] RH-conditional zero-blind source-capacity upper bounds from the Klein–Gordon/Chebyshev family; [D] exact balance law \(\Omega=\beta\) for \(\delta=N^{-\beta}\); [I] canonical unit stopband \(\Omega=1\) uniquely balances at \(\delta=N^{-1}\); [G] this selects a distinguished variational scale but does not yet prove the physical crossing satisfies \(N\delta_\tau\to C_\tau\); [O] prove noncollapse and parity-ratio convergence of the physical source capacities at this scale  
**Authorization:** Jeremy, 2026-10-02 ("perfect hit it!!!!")  
**Parents:** v13.950, v13.958  
**Collision check:** v13.959 was absent in the live tree immediately before this write.

---

## 0. Purpose

v13.958 proves that the universal source matrix and the exact zero-blind stopband exponent do not by themselves force

\[
N_a\delta_\tau(a)\to C_\tau.
\]

Nevertheless, the zero-blind Klein–Gordon/Chebyshev extremal does identify a **distinguished source-capacity scale**.

The balancing law is exact:

\[
\boxed{
\Omega=\beta
}
\]

when

\[
\delta=N_a^{-\beta}=e^{-2\beta a}.
\]

Therefore the canonical unit stopband \(\Omega=1\), already selected by the normalized deficiency point \(z=i\), picks

\[
\boxed{
\delta=e^{-2a}=N_a^{-1}.
}
\]

This is a variational scale-selection theorem, not yet a physical source-RG convergence theorem.

---

## 1. Source capacities [D]

Let

\[
B_a=A_a-\lambda_aI\ge0
\]

and let the normalized parity sources be

\[
f_{+,a}
=
\frac{f_{R,a}+f_{L,a}}{\sqrt2},
\]

\[
f_{-,a}
=
\frac{f_{R,a}-f_{L,a}}{\sqrt2},
\]

with

\[
f_{R,a}=e^{-a}e^x,
\qquad
f_{L,a}=e^{-a}e^{-x}.
\]

For \(\delta>0\), define

\[
\boxed{
\mathcal C_{a,\pm}(\delta)
=
\inf_{\langle f_{\pm,a},g\rangle=1}
\left[
\langle g,B_a^{(\pm)}g\rangle
+
\delta\|g\|_2^2
\right].
}
\tag{1}
\]

As in v13.958,

\[
\boxed{
\mathcal C_{a,\pm}(\delta)
=
\frac1{G_{a,\pm}(\delta)}.
}
\tag{2}
\]

The critical overlap condition is

\[
\boxed{
\frac{
\mathcal C_{a,+}(\delta_\tau)
}{
\mathcal C_{a,-}(\delta_\tau)
}
=
q_\tau,
\qquad
q_\tau=\tanh(\tau/2).
}
\tag{3}
\]

---

## 2. Zero-blind Klein–Gordon filter [D]

For \(\Omega>0\), v13.950 constructs the positive compact-support characteristic function

\[
\boxed{
F_{a,\Omega}(z)
=
\frac{
\cosh\!\left(
a\sqrt{\Omega^2-z^2}
\right)
}{
\cosh(a\Omega)
}.
}
\tag{4}
\]

After convolution with one fixed even nonnegative \(C_c^\infty\) probability mollifier, one obtains smooth even probability densities supported in \([-a+O(1),a+O(1)]\).

The fixed \(O(1)\) support adjustment does not affect any exponential rate below.

For the smoothed family, all real-stopband estimates retain their exponent:

\[
\sup_{|t|\ge\Omega}
|F_{a,\Omega}^{\rm sm}(t)|
\le
C_\Omega e^{-a\Omega}.
\tag{5}
\]

The smoothing factor also gives sufficient decay in \(t\) to make all RH zero sums finite.

---

## 3. Value at the physical source point \(z=-i\) [D]

At the right-edge source point,

\[
z=-i,
\]

we have

\[
\Omega^2-z^2
=
\Omega^2+1.
\]

Therefore

\[
\boxed{
F_{a,\Omega}(-i)
=
\frac{
\cosh\!\left(
a\sqrt{\Omega^2+1}
\right)
}{
\cosh(a\Omega)
}.
}
\tag{6}
\]

Define

\[
\boxed{
s_\Omega
=
\sqrt{1+\Omega^2},
}
\tag{7}
\]

and

\[
\boxed{
d_\Omega
=
1+\Omega-s_\Omega.
}
\tag{8}
\]

Since

\[
s_\Omega<1+\Omega,
\]

we have

\[
d_\Omega>0.
\]

The normalized even source is

\[
f_{+,a}
=
\sqrt2\,e^{-a}\cosh x.
\]

For the positive even trial density \(p_{a,\Omega}\),

\[
\langle
f_{+,a},
p_{a,\Omega}
\rangle
=
\sqrt2\,e^{-a}
\int
p_{a,\Omega}(x)\cosh x\,dx.
\]

The moment-generating function is \(F_{a,\Omega}(-i)\), up to the fixed nonzero smoothing factor.

Hence

\[
\boxed{
|\langle
f_{+,a},
p_{a,\Omega}
\rangle|
\asymp
e^{-a d_\Omega}.
}
\tag{9}
\]

---

## 4. Odd trial has the same source-overlap exponent [D]

Let

\[
g_{a,\Omega}^{(-)}
=
p_{a,\Omega}'.
\]

It is odd.

Because the smoothed density is compactly supported,

\[
\begin{aligned}
\langle
f_{-,a},
g_{a,\Omega}^{(-)}
\rangle
&=
\sqrt2\,e^{-a}
\int
\sinh x\,
p_{a,\Omega}'(x)\,dx\\
&=
-\sqrt2\,e^{-a}
\int
\cosh x\,
p_{a,\Omega}(x)\,dx.
\end{aligned}
\]

Therefore

\[
\boxed{
|\langle
f_{-,a},
g_{a,\Omega}^{(-)}
\rangle|
\asymp
e^{-a d_\Omega}.
}
\tag{10}
\]

So the even positive filter and its odd derivative have the **same normalized source-overlap exponent**.

This is the key parity symmetry of the zero-blind capacity construction.

---

## 5. Uniform \(L^2\) norm control [D]

Because each smoothed trial is obtained by convolving a probability measure with one fixed \(C_c^\infty\) mollifier, Young's inequality gives

\[
\boxed{
\|p_{a,\Omega}\|_2
\le
C_\Omega,
}
\tag{11}
\]

uniformly in \(a\).

Likewise,

\[
\boxed{
\|p_{a,\Omega}'\|_2
\le
C_\Omega',
}
\tag{12}
\]

uniformly in \(a\).

Thus the only exponential factors in the source-normalized capacities come from:

- stopband energy suppression;
- source-overlap normalization;
- regulator scaling.

---

## 6. RH-conditional Weil-energy bounds [C]

Assume RH and choose

\[
0<\Omega\le\gamma_1.
\]

Then every nontrivial zero ordinate lies in the stopband:

\[
|\gamma|\ge\gamma_1\ge\Omega.
\]

For the even trial,

\[
Q_W[p_{a,\Omega}]
=
\sum_\gamma
m_\gamma
|\widehat p_{a,\Omega}(\gamma)|^2.
\]

Using (5) and the fixed smoothing tail,

\[
\boxed{
Q_W[p_{a,\Omega}]
\le
C_\Omega e^{-2a\Omega}.
}
\tag{13}
\]

For the odd derivative,

\[
\widehat{p_{a,\Omega}'}(\gamma)
=
i\gamma
\widehat p_{a,\Omega}(\gamma),
\]

and the smoothing gives enough decay to absorb the factor \(\gamma^2\), so

\[
\boxed{
Q_W[p_{a,\Omega}']
\le
C_\Omega' e^{-2a\Omega}.
}
\tag{14}
\]

Since

\[
B_a=A_a-\lambda_aI
\]

and under RH

\[
0\le B_a\le A_a
\]

at the quadratic-form level after recentering,

\[
\boxed{
\langle
g,B_ag
\rangle
\le
Q_W[g].
}
\tag{15}
\]

Thus (13)–(14) are valid upper bounds for the recentered energy in the capacity trials.

---

## 7. Even and odd source-capacity upper bounds [C]

Normalize the even trial by its source overlap.

From (9), (11), and (13),

\[
\mathcal C_{a,+}(\delta)
\le
C_\Omega
\left[
e^{-2a(\Omega-d_\Omega)}
+
\delta
e^{2ad_\Omega}
\right].
\tag{16}
\]

Likewise, using (10), (12), and (14),

\[
\boxed{
\mathcal C_{a,-}(\delta)
\le
C_\Omega'
\left[
e^{-2a(\Omega-d_\Omega)}
+
\delta
e^{2ad_\Omega}
\right].
}
\tag{17}
\]

Now

\[
\Omega-d_\Omega
=
\Omega-
\left(
1+\Omega-s_\Omega
\right)
=
s_\Omega-1.
\]

Therefore

\[
\boxed{
\mathcal C_{a,\pm}(\delta)
\le
C_{\Omega,\pm}
\left[
e^{-2a(s_\Omega-1)}
+
\delta e^{2ad_\Omega}
\right].
}
\tag{18}
\]

---

## 8. Regulator exponent \(\beta\) [D/C]

Write the regulator as

\[
\boxed{
\delta
=
N_a^{-\beta}
=
e^{-2\beta a},
\qquad
\beta>0.
}
\tag{19}
\]

Then the two terms in (18) have exponential rates

\[
\boxed{
r_E(\Omega)
=
s_\Omega-1
=
\sqrt{1+\Omega^2}-1,
}
\tag{20}
\]

and

\[
\boxed{
r_\delta(\Omega,\beta)
=
\beta-d_\Omega
=
\beta-1-\Omega+\sqrt{1+\Omega^2}.
}
\tag{21}
\]

The capacity upper bound is controlled by the slower-decaying term.

To optimize the zero-blind trial at fixed \(\beta\), balance the two rates:

\[
r_E(\Omega)
=
r_\delta(\Omega,\beta).
\]

Substitution gives

\[
\sqrt{1+\Omega^2}-1
=
\beta-1-\Omega+\sqrt{1+\Omega^2}.
\]

Everything cancels except

\[
\boxed{
\Omega=\beta.
}
\tag{22}
\]

This balance law is exact.

---

## 9. Optimized zero-blind source-capacity exponent [C]

Set

\[
\Omega=\beta
\]

and assume

\[
0<\beta\le\gamma_1.
\]

Then

\[
r_E(\beta)
=
r_\delta(\beta,\beta)
=
\sqrt{1+\beta^2}-1.
\]

Define

\[
\boxed{
r(\beta)
=
\sqrt{1+\beta^2}-1.
}
\tag{23}
\]

Equations (16)–(18) give

\[
\boxed{
\mathcal C_{a,\pm}(N_a^{-\beta})
\le
C_{\beta,\pm}
N_a^{-r(\beta)}.
}
\tag{24}
\]

Thus the zero-blind source-capacity trial has a relativistic/Klein–Gordon exponent

\[
\boxed{
r(\beta)
=
\sqrt{1+\beta^2}-1.
}
\]

This is a direct consequence of evaluating the stopband extremal at the imaginary source point \(z=i\).

---

## 10. Canonical unit scale [D/I]

The native Schur/Weyl normalization fixes the distinguished imaginary point

\[
z=i.
\]

The zero-blind stopband theorem v13.950 has canonical unit threshold

\[
\Omega=1.
\]

By the exact balance law

\[
\Omega=\beta,
\]

the unit stopband therefore selects

\[
\boxed{
\beta=1.
}
\]

Hence

\[
\boxed{
\delta
=
N_a^{-1}
=
e^{-2a}
}
\tag{25}
\]

is the unique regulator exponent that balances the two zero-blind source-capacity costs at the canonical unit normalization.

At this scale,

\[
\boxed{
r(1)
=
\sqrt2-1.
}
\tag{26}
\]

Therefore

\[
\boxed{
\mathcal C_{a,\pm}(N_a^{-1})
\le
C_\pm
N_a^{-(\sqrt2-1)}.
}
\tag{27}
\]

---

## 11. Universal lower bound from the regulator term [D]

For any admissible \(g\) satisfying

\[
\langle
f_{\pm,a},g
\rangle
=
1,
\]

Cauchy–Schwarz gives

\[
1
\le
\|f_{\pm,a}\|_2
\|g\|_2.
\]

Hence

\[
\|g\|_2^2
\ge
\frac1{\|f_{\pm,a}\|_2^2}.
\]

Because \(B_a\ge0\),

\[
\mathcal C_{a,\pm}(\delta)
\ge
\frac{\delta}{\|f_{\pm,a}\|_2^2}.
\]

The exact source norms satisfy

\[
\|f_{\pm,a}\|_2^2
=
M_{\pm,a}
\to
\frac12.
\]

Thus for

\[
\delta=N_a^{-\beta},
\]

\[
\boxed{
\mathcal C_{a,\pm}(N_a^{-\beta})
\ge
(2+o(1))
N_a^{-\beta}.
}
\tag{28}
\]

Combining (24) and (28),

\[
\boxed{
(2+o(1))N_a^{-\beta}
\le
\mathcal C_{a,\pm}(N_a^{-\beta})
\le
C_{\beta,\pm}
N_a^{-r(\beta)}.
}
\tag{29}
\]

Since

\[
r(\beta)<\beta
\qquad
(\beta>0),
\]

there remains a genuine gap between the universal lower bound and the zero-blind trial upper bound.

This is precisely where zero-aware spectral structure can further reduce the physical capacities.

---

## 12. What the balance theorem does and does not prove [G]

The exact relation

\[
\boxed{
\Omega=\beta
}
\]

proves:

- the zero-blind stopband scale and regulator scale are canonically paired;
- the unit stopband \(\Omega=1\) singles out \(N^{-1}\);
- the source point \(z=i\) creates the Klein–Gordon exponent
  \[
  \sqrt{1+\beta^2}-1.
  \]

It does **not** prove:

\[
N_a\delta_\tau(a)\to C_\tau.
\]

v13.958 shows that the physical crossing scale still depends on the actual source spectral ratio

\[
\Phi_a(c)
=
\frac{
G_{a,-}(c/N_a)
}{
G_{a,+}(c/N_a)
}.
\]

Thus:

\[
\boxed{
\textbf{\(N^{-1}\) is now an intrinsic zero-blind source-capacity scale, but physical scale selection still requires source-RG convergence.}
}
\tag{30}
\]

---

## 13. Natural capacity-RG normalization [I/O]

At the canonical scale

\[
\delta=\frac{c}{N_a},
\]

the zero-blind trial suggests the normalization

\[
\boxed{
\mathfrak C_{a,\pm}(c)
=
N_a^{\sqrt2-1}
\mathcal C_{a,\pm}(c/N_a).
}
\tag{31}
\]

If one could prove

\[
\mathfrak C_{a,\pm}(c)
\to
\mathfrak C_\pm(c)
\in(0,\infty)
\]

locally uniformly for \(c>0\), then

\[
\Phi_a(c)
=
\frac{
G_{a,-}(c/N_a)
}{
G_{a,+}(c/N_a)
}
=
\frac{
\mathcal C_{a,+}(c/N_a)
}{
\mathcal C_{a,-}(c/N_a)
}
\]

would converge to

\[
\boxed{
\Phi(c)
=
\frac{
\mathfrak C_+(c)
}{
\mathfrak C_-(c)
}.
}
\tag{32}
\]

Then v13.958 would imply

\[
N_a\delta_\tau(a)\to C_\tau
\]

at the first crossing

\[
\Phi(C_\tau)=q_\tau.
\]

Thus the next target can be stated as a **capacity-RG noncollapse theorem**.

---

## 14. Result

The source-capacity version of the cone/Jost scaling has an exact balance law.

For regulator exponent

\[
\delta=N^{-\beta},
\]

the zero-blind stopband extremal with threshold \(\Omega\) balances its source-normalized energy and regulator costs exactly when

\[
\boxed{
\Omega=\beta.
}
\]

The optimized zero-blind source-capacity exponent is

\[
\boxed{
r(\beta)
=
\sqrt{1+\beta^2}-1.
}
\]

At the canonical unit normalization,

\[
\boxed{
\Omega=1
\Longrightarrow
\beta=1
\Longrightarrow
\delta=N^{-1},
}
\]

with

\[
\boxed{
\mathcal C_{a,\pm}(N^{-1})
\lesssim
N^{-(\sqrt2-1)}.
}
\]

This makes \(N^{-1}\) the unique balanced zero-blind source scale.

The remaining physical theorem is the noncollapse and convergence of the actual parity source-capacity ratio at this scale.
