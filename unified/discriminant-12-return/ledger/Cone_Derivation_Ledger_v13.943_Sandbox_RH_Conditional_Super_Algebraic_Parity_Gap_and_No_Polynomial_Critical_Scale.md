# Cone Derivation Ledger v13.943 — Sandbox: RH-Conditional Super-Algebraic Parity-Gap Closure and No Polynomial Critical Scale

**Date:** 2026-10-02  
**Track:** Sandbox / source-faithful Suzuki critical double-scaling lane  
**Status:** [D] RH-conditional super-algebraic and stretched-exponential upper bounds on the odd recentered gap; [R] rules out any positive finite power-law asymptotic for the gap under the parity-ground hypothesis; [G] no lower bound or exact exponential rate claimed; [O] determine the true tunneling/frame scale and residue ratio  
**Authorization:** Jeremy, 2026-10-02 ("...keep going!")  
**Parents:** v13.753, v13.792, v13.935, v13.940–941  
**Collision resolution:** This content was first committed under v13.942 at 2026-10-02T14:20:39Z, but the sieve-renormalization/cone entry had independently landed v13.942 at 2026-10-02T14:20:12Z. Per the standing earlier-commit-wins rule, the cone/sieve entry keeps v13.942 and this parity-gap entry is renumbered v13.943. Mathematical content is unchanged.

---

## 0. Main result

v13.941 reduced the intrinsic overlap double scaling to the first odd recentered gap

\[
\Delta_a
=
\inf\sigma(B_a^{(-)}),
\qquad
B_a=A_a-\lambda_a I,
\]

under an even-ground / one-odd-pole regime.

A naive possibility was

\[
\Delta_a\sim C a^{-2},
\]

which would generate the familiar \(\sqrt\delta\) attenuation law.

The present entry rules out **every positive finite power law** under RH and the standing even-ground hypothesis.

For every \(M>0\),

\[
\boxed{
\Delta_a
=
O(a^{-M}).
}
\tag{1}
\]

More strongly, for every exponent

\[
0<\eta<1,
\]

there exist constants \(C_\eta,c_\eta>0\) such that

\[
\boxed{
\Delta_a
\le
C_\eta
e^{-c_\eta a^\eta}
}
\tag{2}
\]

for all sufficiently large \(a\).

Thus the parity gap is at least **super-algebraically small**, and can be bounded by arbitrarily near-exponential stretched exponentials.

No exact lower bound is proved.

The actual scale may be exponential or smaller.

---

## 1. RH zero-side representation [D, conditional on RH]

Under RH, the Weil/Suzuki quadratic form has the positive zero-side representation

\[
\boxed{
Q_W[f]
=
\sum_\gamma
m_\gamma
|\widehat f(\gamma)|^2,
}
\tag{3}
\]

where:

- \(\gamma\in\mathbb R\setminus\{0\}\) runs over the nontrivial zero ordinates;
- \(m_\gamma\ge1\) is the zero multiplicity;
- the Fourier convention is the same as in v13.753.

No simplicity assumption is needed.

The zero-counting estimate

\[
N(T)=O(T\log T)
\]

implies that for every

\[
s>1,
\]

\[
\boxed{
\sum_\gamma
m_\gamma
|\gamma|^{-s}
<
\infty.
}
\tag{4}
\]

Also, since \(\Xi(0)\ne0\), there is a positive central zero-free interval:

\[
\boxed{
\gamma_1
:=
\inf_\gamma|\gamma|
>0.
}
\tag{5}
\]

---

## 2. Odd broadening test [D]

Choose any nonzero odd function

\[
\phi\in C_c^\infty(-1,1).
\]

For \(a\ge1\), define

\[
\boxed{
f_a(x)
=
a^{-1/2}\phi(x/a).
}
\tag{6}
\]

Then:

1. \(f_a\in C_c^\infty(-a,a)\);
2. \(f_a\) is odd;
3.
   \[
   \|f_a\|_2
   =
   \|\phi\|_2;
   \]
4.
   \[
   \boxed{
   \widehat f_a(t)
   =
   a^{1/2}\widehat\phi(at).
   }
   \tag{7}
   \]

Since \(\widehat\phi\) is Schwartz, for every integer \(N\ge1\),

\[
|\widehat\phi(t)|
\le
C_N(1+|t|)^{-N}.
\]

Therefore for every zero ordinate,

\[
|\widehat f_a(\gamma)|^2
\le
C_N^2
a
(1+a|\gamma|)^{-2N}.
\]

For \(a\ge1\),

\[
(1+a|\gamma|)^{-2N}
\le
a^{-2N}|\gamma|^{-2N}.
\]

Thus from (3),

\[
Q_W[f_a]
\le
C_N^2
a^{1-2N}
\sum_\gamma
m_\gamma|\gamma|^{-2N}.
\]

Using (4),

\[
\boxed{
Q_W[f_a]
\le
C_N'
a^{1-2N}.
}
\tag{8}
\]

Dividing by the fixed norm gives

\[
\boxed{
\lambda_a^{(-)}
\le
C_N''
a^{1-2N},
}
\tag{9}
\]

where

\[
\lambda_a^{(-)}
:=
\inf_{\substack{0\ne f\in C_c^\infty(-a,a)\\f\ {\rm odd}}}
\frac{Q_W[f]}{\|f\|_2^2}.
\]

Since \(N\) is arbitrary, for every \(M>0\),

\[
\boxed{
\lambda_a^{(-)}
=
O(a^{-M}).
}
\tag{10}
\]

---

## 3. Recentered odd gap [D]

Assume the standing ground-channel hypothesis from v13.940–941:

\[
\boxed{
\lambda_a
=
\lambda_a^{(+)}
}
\tag{H1}
\]

for sufficiently large \(a\); i.e. the global finite-interval ground state lies in the even sector.

Under RH,

\[
\lambda_a\ge0.
\]

The recentered odd gap is

\[
\boxed{
\Delta_a
=
\lambda_a^{(-)}
-
\lambda_a.
}
\tag{11}
\]

Therefore

\[
0
\le
\Delta_a
\le
\lambda_a^{(-)}.
\]

Combining with (10),

\[
\boxed{
\Delta_a
=
O(a^{-M})
\qquad
\text{for every }M>0.
}
\tag{12}
\]

This proves the super-algebraic bound (1).

---

## 4. No positive finite power-law asymptotic [D]

Suppose for contradiction that for some

\[
C>0,
\qquad
p>0,
\]

one had

\[
\Delta_a
\sim
C a^{-p}.
\]

Choose

\[
M>p.
\]

Equation (12) gives

\[
\Delta_a
=
O(a^{-M}),
\]

which is incompatible with a positive asymptotic constant multiplying \(a^{-p}\).

Hence:

\[
\boxed{
\textbf{under RH + the even-ground hypothesis, }
\Delta_a\not\sim C a^{-p}
\textbf{ for every finite }p>0,\ C>0.
}
\tag{13}
\]

In particular,

\[
\boxed{
\Delta_a\not\sim C a^{-2}.
}
\tag{14}
\]

Thus the quadratic-gap specialization of v13.941 cannot be the correct RH asymptotic regime.

---

## 5. Gevrey refinement: near-exponential upper bounds [D/classical]

The Schwartz argument can be sharpened.

Fix

\[
0<\eta<1.
\]

Let

\[
s=\eta^{-1}>1.
\]

There exists a nonzero odd compactly supported Gevrey-\(s\) function

\[
\phi_\eta\in C_c^\infty(-1,1)
\]

whose Fourier transform satisfies

\[
\boxed{
|\widehat\phi_\eta(t)|
\le
C_\eta
e^{-c_\eta |t|^\eta}.
}
\tag{15}
\]

Use the same dilation

\[
f_{a,\eta}(x)
=
a^{-1/2}\phi_\eta(x/a).
\]

Then

\[
|\widehat f_{a,\eta}(\gamma)|^2
\le
C_\eta^2
a
e^{-2c_\eta(a|\gamma|)^\eta}.
\]

Since

\[
|\gamma|\ge\gamma_1>0,
\]

and for \(a\ge1\),

\[
a^\eta|\gamma|^\eta
\ge
\frac12 a^\eta\gamma_1^\eta
+
\frac12|\gamma|^\eta,
\]

we obtain

\[
e^{-2c_\eta(a|\gamma|)^\eta}
\le
e^{-c_\eta a^\eta\gamma_1^\eta}
e^{-c_\eta|\gamma|^\eta}.
\]

The zero-counting estimate implies

\[
\sum_\gamma
m_\gamma
e^{-c_\eta|\gamma|^\eta}
<
\infty.
\]

Hence

\[
Q_W[f_{a,\eta}]
\le
C_\eta'
a
e^{-c_\eta' a^\eta}.
\]

Absorbing the polynomial factor into a slightly weaker exponential gives constants

\[
C_\eta'',c_\eta''>0
\]

such that

\[
\boxed{
\lambda_a^{(-)}
\le
C_\eta''
e^{-c_\eta''a^\eta}.
}
\tag{16}
\]

By (11),

\[
\boxed{
\Delta_a
\le
C_\eta''
e^{-c_\eta''a^\eta}.
}
\tag{17}
\]

This holds for every fixed

\[
0<\eta<1.
\]

---

## 6. Interpretation: a sampling/frame problem, not a box Laplacian [I]

Under RH,

\[
Q_W[f]
=
\sum_\gamma
m_\gamma
|\widehat f(\gamma)|^2.
\]

For

\[
\operatorname{supp}f\subset(-a,a),
\]

the Fourier transform belongs to a Paley–Wiener class of exponential type \(a\).

Thus the finite Suzuki operator is, at the form level, a sampling/frame operator for the Paley–Wiener function at the zero ordinates.

The small eigenvalues arise because a type-\(a\) Fourier transform can become increasingly concentrated in the central frequency window containing no zero ordinates.

This is qualitatively different from ordinary finite-box kinetic energy, where

\[
\lambda_{\rm gap}\sim a^{-2}.
\]

The natural language is instead:

\[
\boxed{
\textbf{Paley–Wiener concentration / tunneling through the zero-sampling set.}
}
\]

This explains why a stretched-exponential or exponential finite-size scale is natural.

---

## 7. Consequence for the intrinsic regulator [C]

Under the one-pole crossover hypotheses of v13.941,

\[
\delta_\tau(a)
\sim
x_\tau\Delta_a,
\qquad
x_\tau
=
\frac{q_\tau r}{1-q_\tau r}.
\]

Therefore, under RH and the same one-pole hypotheses,

\[
\boxed{
\delta_\tau(a)
=
O(a^{-M})
\quad
\text{for every }M>0,
}
\tag{18}
\]

and more strongly, for every

\[
0<\eta<1,
\]

\[
\boxed{
\delta_\tau(a)
\le
C_{\eta,\tau}
e^{-c_{\eta,\tau}a^\eta}
}
\tag{19}
\]

for sufficiently large \(a\).

Thus the intrinsic regulator must approach threshold much faster than any polynomial scale.

---

## 8. Consequence for v13.940's optional attenuation ansatz [R/G]

v13.940's optional model

\[
\mu(\delta)\sim c\delta^\nu
\]

would imply a polynomial critical regulator

\[
\delta_\tau(a)\asymp a^{-1/\nu}.
\]

Equations (18)–(19) show that, under RH plus the one-pole crossover regime, **no finite positive \(\nu\)** can describe the true asymptotic critical scale.

Therefore:

\[
\boxed{
\textbf{the finite-power attenuation ansatz is not compatible with the RH sampling regime.}
}
\tag{20}
\]

This does not invalidate the exact overlap law of v13.940.

It only removes the optional power-law specialization.

The correct attenuation may have an essential-singularity/tunneling form, for example schematically

\[
\mu(\delta)
\sim
\frac{1}{|\log\delta|^\alpha}
\]

or another non-power law.

No particular form is asserted here.

---

## 9. What is not proved [G]

The present result is an **upper bound**.

It does not establish:

- an exponential lower bound for \(\Delta_a\);
- a matching stretched-exponential asymptotic;
- a unique tunneling exponent;
- dominance of the first odd pole;
- the residue ratio \(r_a\to r\);
- an unconditional version independent of RH.

In particular, the gap could close faster than every bound constructed here.

---

## 10. Next nonredundant gate [O]

The correct next question is no longer

\[
\Delta_a\stackrel{?}{\sim}Ca^{-p}.
\]

It is:

\[
\boxed{
\textbf{what is the sharp concentration/tunneling scale of the even and odd Paley–Wiener sampling minima?}
}
\]

Operationally:

1. rewrite the RH-specialized even and odd finite forms explicitly as Paley–Wiener sampling operators at \(\{\gamma\}\);
2. identify the central zero-free interval
   \[
   (-\gamma_1,\gamma_1);
   \]
3. compare the lowest even/odd sampling eigenvalues with time-frequency concentration extremals;
4. determine whether
   \[
   \log\Delta_a
   \]
   is asymptotically linear in \(a\), stretched-linear, or governed by another scale;
5. separately track the source residues
   \[
   \alpha_a,\beta_a.
   \]

That is the correct threshold-exponent problem after v13.941.

---

## 11. Result

Under RH and the even-ground hypothesis,

\[
\boxed{
\Delta_a
=
O(a^{-M})
\quad
\forall M>0.
}
\]

More strongly,

\[
\boxed{
\forall\,0<\eta<1,\qquad
\Delta_a
\le
C_\eta e^{-c_\eta a^\eta}.
}
\]

Hence no positive finite power law, including \(a^{-2}\), can be the asymptotic parity-gap scale.

Under the one-pole deficiency-overlap crossover,

\[
\boxed{
\delta_\tau(a)
\sim x_\tau\Delta_a
}
\]

inherits the same super-algebraic critical scale.

The finite-size problem has therefore moved from ordinary gap scaling to a Paley–Wiener concentration/tunneling problem.
