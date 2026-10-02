# Cone Derivation Ledger v13.937 — Sandbox: Canonical Jost Normalization of Cross-Edge Transfer and Scattering-Phase Quantization

**Date:** 2026-10-02  
**Track:** Sandbox / source-faithful Suzuki cross-edge normalization lane  
**Status:** [D] exact free-propagation factorization and Jost normalization; [D] Hardy-space convergence and a.e. scattering limit; [D] exact finite quantization law; [G] half-plane Jost normalization is not yet Suzuki's conjectural global entire normalization; [O] critical double-scaling / global stitching remains open  
**Authorization:** Jeremy, 2026-10-02 ("cool lets take the next gate and Normalize the cross-edge transfer")  
**Parents:** v13.724–725, v13.784–791, v13.927, v13.929, v13.931, v13.935–936  
**Collision check:** v13.937 was absent immediately before this write.

---

## 0. Gate and result

v13.936 proved that for the intrinsic ground-recentered branch

\[
T_{a,\delta}^{\circ}
=
A_a-\lambda_a I+\delta I,
\qquad
\delta>0,
\]

the unrenormalized Schur/Weyl data satisfy

\[
h_{a,\delta}^{\circ}\to0,
\qquad
m_{a,\delta}^{\circ}\to i
\]

whenever

\[
\lambda_\infty:=\lim_{a\to\infty}\lambda_a>-\infty.
\]

The mechanism was exact: the driven right-edge profile converges strongly, while the same profile evaluated at the opposite edge recedes to infinity.

The present gate asks whether the vanishing cross-edge transfer admits an intrinsic normalization.

It does.

The transfer has an **exact universal propagation factor**

\[
e^{2iaz}
\]

coming solely from traversing the geometric distance \(2a\).

Removing this factor gives the canonical Jost transform.

The resulting normalized object:

- uses no zeta zero;
- uses no fitted scalar;
- uses no arbitrary cutoff phase;
- is determined entirely by the interval geometry and the source-faithful edge response;
- converges to a nonzero analytic function in the reflected half-plane;
- yields a unimodular real-axis scattering matrix;
- separates the finite eigenvalue condition into free-flight phase plus scattering phase.

---

## 1. Source-faithful right-edge response [D]

Fix

\[
\delta>0
\]

and assume

\[
\lambda_\infty>-\infty.
\]

Let

\[
v_{a,+}^{\circ}
=
(T_{a,\delta}^{\circ})^{-1}e^x.
\]

Because the localized Weil form and the recentered operator are real and reflection invariant,

\[
R T_{a,\delta}^{\circ}R
=
T_{a,\delta}^{\circ},
\qquad
(Rf)(x)=f(-x).
\]

Hence

\[
\boxed{
v_{a,-}^{\circ}
=
(T_{a,\delta}^{\circ})^{-1}e^{-x}
=
Rv_{a,+}^{\circ}.
}
\tag{1}
\]

The two deficiency source vectors therefore have equal energy norm automatically, so no independent relative amplitude normalization is needed.

Define the right-edge coordinate

\[
x=a-\xi
\]

and the normalized response

\[
\boxed{
u_{a,\delta}(\xi)
=
e^{-a}v_{a,+}^{\circ}(a-\xi),
\qquad
0<\xi<2a.
}
\tag{2}
\]

By v13.936,

\[
\boxed{
u_{a,\delta}
\longrightarrow
u_{\infty,\delta}
}
\tag{3}
\]

strongly in the canonical recentered edge-energy completion and, through the continuous energy-to-\(L^2\) map, strongly in

\[
L^2(0,\infty).
\]

The limiting vector is nonzero.

---

## 2. The right Jost transform [D]

Define

\[
\boxed{
D_{a,\delta}(z)
=
\int_0^{2a}
u_{a,\delta}(\xi)e^{iz\xi}\,d\xi,
\qquad
z\in\mathbb C.
}
\tag{4}
\]

Since \(u_{a,\delta}\) is real,

\[
D_{a,\delta}^{\#}(z)
:=
\overline{D_{a,\delta}(\bar z)}
=
D_{a,\delta}(-z).
\tag{5}
\]

For the limit vector,

\[
\boxed{
D_{\infty,\delta}(z)
=
\int_0^\infty
u_{\infty,\delta}(\xi)e^{iz\xi}\,d\xi,
\qquad
z\in\mathbb C_+.
}
\tag{6}
\]

This is a Hardy \(H^2(\mathbb C_+)\) function.

The Paley–Wiener/Plancherel isometry gives

\[
\sup_{y>0}
\int_{\mathbb R}
|D_{a,\delta}(t+iy)-D_{\infty,\delta}(t+iy)|^2dt
=
2\pi
\|u_{a,\delta}-u_{\infty,\delta}\|_2^2,
\tag{7}
\]

after zero-extending \(u_{a,\delta}\) outside \((0,2a)\).

Therefore

\[
\boxed{
D_{a,\delta}
\to
D_{\infty,\delta}
\quad
\text{in }H^2(\mathbb C_+),
}
\tag{8}
\]

and in particular locally uniformly in \(\mathbb C_+\).

From v13.936,

\[
\boxed{
D_{\infty,\delta}(i)
=
\|u_{\infty,\delta}\|_{\infty,\delta}^2
>0,
}
\tag{9}
\]

so the limiting Jost function is nontrivial.

---

## 3. Exact cross-edge transfer factorization [D]

v13.936 defined the opposite-edge transfer amplitude

\[
\boxed{
N_{a,\delta}(z)
=
\int_0^{2a}
u_{a,\delta}(2a-\eta)e^{iz\eta}\,d\eta.
}
\tag{10}
\]

Set

\[
\xi=2a-\eta.
\]

Then

\[
\begin{aligned}
N_{a,\delta}(z)
&=
\int_0^{2a}
u_{a,\delta}(\xi)e^{iz(2a-\xi)}\,d\xi\\
&=
e^{2iaz}
\int_0^{2a}
u_{a,\delta}(\xi)e^{-iz\xi}\,d\xi.
\end{aligned}
\]

Thus

\[
\boxed{
N_{a,\delta}(z)
=
e^{2iaz}
D_{a,\delta}^{\#}(z).
}
\tag{11}
\]

This is exact.

The vanishing in \(\mathbb C_+\) proved in v13.936 is therefore the product of:

1. the free propagation factor
   \[
   e^{2iaz},
   \]
   which decays as \(e^{-2a\,\Im z}\) in \(\mathbb C_+\);

2. the reflected Jost transform
   \[
   D_{a,\delta}^{\#}(z).
   \]

The distance \(2a\) is exactly the separation between the two edges.

---

## 4. Canonical Jost normalization [D]

Define the normalized cross-edge transfer

\[
\boxed{
\widetilde N_{a,\delta}(z)
:=
e^{-2iaz}N_{a,\delta}(z).
}
\tag{12}
\]

Then by (11),

\[
\boxed{
\widetilde N_{a,\delta}(z)
=
D_{a,\delta}^{\#}(z).
}
\tag{13}
\]

No arbitrary scale remains.

For

\[
z\in\mathbb C_-,
\]

we have \(\bar z\in\mathbb C_+\), so (8) implies

\[
\boxed{
\widetilde N_{a,\delta}(z)
\longrightarrow
D_{\infty,\delta}^{\#}(z)
:=
\overline{D_{\infty,\delta}(\bar z)}
}
\tag{14}
\]

locally uniformly on \(\mathbb C_-\).

At the canonical reflected deficiency point,

\[
\boxed{
D_{\infty,\delta}^{\#}(-i)
=
D_{\infty,\delta}(i)
>0.
}
\tag{15}
\]

Therefore the normalized cross-edge transfer has a genuine nonzero cutoff-free limit.

This closes the normalization gate at the Jost level.

---

## 5. Exact factorization of the Schur function [D]

The finite Fourier transform of the right deficiency vector is

\[
F_{a,+}^{\circ}(z)
=
\int_{-a}^{a}
v_{a,+}^{\circ}(x)e^{izx}\,dx.
\]

Using \(x=a-\xi\),

\[
\boxed{
F_{a,+}^{\circ}(z)
=
e^a e^{iaz}
D_{a,\delta}^{\#}(z).
}
\tag{16}
\]

Reflection (1) gives

\[
\boxed{
F_{a,-}^{\circ}(z)
=
F_{a,+}^{\circ}(-z)
=
e^a e^{-iaz}
D_{a,\delta}(z).
}
\tag{17}
\]

Hence the finite Schur quotient is

\[
\boxed{
h_{a,\delta}^{\circ}(z)
=
e^{2iaz}
\frac{D_{a,\delta}^{\#}(z)}
{D_{a,\delta}(z)}.
}
\tag{18}
\]

Equation (18) is the exact free-flight/Jost factorization.

The factor responsible for the trivial compact-open limit is now isolated explicitly.

---

## 6. Real-axis scattering matrix [D]

For real \(t\),

\[
D_{a,\delta}^{\#}(t)
=
\overline{D_{a,\delta}(t)}.
\]

Define, wherever the denominator is nonzero,

\[
\boxed{
\mathcal S_{a,\delta}(t)
:=
e^{-2iat}
h_{a,\delta}^{\circ}(t)
=
\frac{\overline{D_{a,\delta}(t)}}
{D_{a,\delta}(t)}.
}
\tag{19}
\]

Therefore

\[
\boxed{
|\mathcal S_{a,\delta}(t)|=1.
}
\tag{20}
\]

This is the canonical one-channel scattering matrix associated with the finite cross-edge problem after removing free propagation.

Write

\[
D_{a,\delta}(t)
=
|D_{a,\delta}(t)|
e^{i\varphi_{a,\delta}(t)}.
\]

Then

\[
\boxed{
\mathcal S_{a,\delta}(t)
=
e^{-2i\varphi_{a,\delta}(t)}.
}
\tag{21}
\]

Thus the entire nontrivial normalized cross-edge datum on the spectral axis is a phase shift.

---

## 7. Cutoff-free scattering limit [D]

By the \(H^2\) convergence (8), the non-tangential boundary values satisfy

\[
D_{a,\delta}
\to
D_{\infty,\delta}
\]

in \(L^2_{\rm loc}(\mathbb R)\), in fact in the full \(H^2\) boundary norm.

Because \(D_{\infty,\delta}\) is a nonzero \(H^2\) function, its boundary values cannot vanish on a set of positive Lebesgue measure.

Hence

\[
\boxed{
\mathcal S_{\infty,\delta}(t)
:=
\frac{\overline{D_{\infty,\delta}(t)}}
{D_{\infty,\delta}(t)}
}
\tag{22}
\]

is defined for almost every \(t\in\mathbb R\) and satisfies

\[
\boxed{
|\mathcal S_{\infty,\delta}(t)|=1
\quad\text{a.e.}
}
\tag{23}
\]

Moreover,

\[
\boxed{
\mathcal S_{a,\delta}
\longrightarrow
\mathcal S_{\infty,\delta}
}
\tag{24}
\]

locally in measure on \(\mathbb R\).

Every subsequence contains a further subsequence converging almost everywhere to the same \(\mathcal S_{\infty,\delta}\).

Thus the normalized scattering limit is unique.

---

## 8. Exact finite quantization law for \(\theta=\pi\) [D]

Choose the reflection-compatible equal-normalization deficiency vectors

\[
v_\pm=v_{a,\pm}^{\circ}.
\]

Suzuki's \(\theta=\pi\) characteristic is

\[
\boxed{
W_{a,\delta}^{\circ}(\pi;z)
=
(z-i)F_{a,+}^{\circ}(z)
-
(z+i)F_{a,-}^{\circ}(z).
}
\tag{25}
\]

Using (16)–(17),

\[
\boxed{
W_{a,\delta}^{\circ}(\pi;z)
=
e^a
\left[
(z-i)e^{iaz}D_{a,\delta}^{\#}(z)
-
(z+i)e^{-iaz}D_{a,\delta}(z)
\right].
}
\tag{26}
\]

For a real spectral point \(t\) with \(D_{a,\delta}(t)\neq0\),

\[
W_{a,\delta}^{\circ}(\pi;t)=0
\]

is equivalent to

\[
\boxed{
e^{2iat}
\mathcal S_{a,\delta}(t)
=
\frac{t+i}{t-i}.
}
\tag{27}
\]

Using (21),

\[
e^{2i(at-\varphi_{a,\delta}(t))}
=
\frac{t+i}{t-i}.
\]

Since

\[
\frac{t+i}{t-i}
=
e^{2i\arg(t+i)}
\]

with a continuous branch chosen between crossings, the eigenvalue condition is

\[
\boxed{
a t
-
\varphi_{a,\delta}(t)
-
\arg(t+i)
\in
\pi\mathbb Z.
}
\tag{28}
\]

This is the exact box-plus-scattering quantization law.

The three terms have distinct roles:

\[
\boxed{
\begin{array}{rcl}
a t
&=&
\text{free flight across a half interval},\\[1mm]
-\varphi_{a,\delta}(t)
&=&
\text{intrinsic Weil/Jost scattering phase},\\[1mm]
-\arg(t+i)
&=&
\text{fixed }\theta=\pi\text{ deficiency-boundary phase}.
\end{array}
}
\tag{29}
\]

No zero ordinate is inserted anywhere in this decomposition.

---

## 9. Canonical half-plane normalization of Suzuki's characteristic [D]

Equation (26) also identifies a natural exponential normalization of the characteristic itself.

Define the right-Jost characteristic

\[
\boxed{
\mathcal W_{a,\delta}^{+}(z)
:=
e^{-a+iaz}
W_{a,\delta}^{\circ}(\pi;z).
}
\tag{30}
\]

Then

\[
\mathcal W_{a,\delta}^{+}(z)
=
(z-i)N_{a,\delta}(z)
-
(z+i)D_{a,\delta}(z).
\tag{31}
\]

By v13.936 and (8),

\[
\boxed{
\mathcal W_{a,\delta}^{+}(z)
\longrightarrow
-(z+i)D_{\infty,\delta}(z)
}
\tag{32}
\]

locally uniformly on \(\mathbb C_+\).

This limit is nonzero because of (9).

Similarly define

\[
\boxed{
\mathcal W_{a,\delta}^{-}(z)
:=
e^{-a-iaz}
W_{a,\delta}^{\circ}(\pi;z).
}
\tag{33}
\]

Then

\[
\boxed{
\mathcal W_{a,\delta}^{-}(z)
\longrightarrow
(z-i)D_{\infty,\delta}^{\#}(z)
}
\tag{34}
\]

locally uniformly on \(\mathbb C_-\).

Therefore the finite characteristic has a canonical **Jost pair** of half-plane normalizations.

---

## 10. Why there are two normalizations [D/I]

The two factors

\[
e^{-a+iaz},
\qquad
e^{-a-iaz}
\]

are not arbitrary competitors.

They correspond to choosing which edge is regarded as the incoming/reference edge.

The right normalization retains the right-edge Jost denominator and suppresses the receding left-edge channel in \(\mathbb C_+\).

The left normalization does the reflected operation in \(\mathbb C_-\).

The ratio of the two free factors is exactly

\[
\boxed{
e^{2iaz},
}
\]

the cross-interval propagation factor already isolated in (11).

Thus the finite characteristic is naturally a two-Jost-function object.

---

## 11. Relation to Suzuki's unspecified exponential normalization [G/P]

The repository's source baseline remains the archived Suzuki v2 PDF.

The current public arXiv version is now v3 (September 23, 2026). The later version still writes the conjectural limit with an unspecified nonvanishing exponential factor

\[
e^{\phi(a,z)}W(a,\theta;z)
\]

and explicitly says that this factor is included to allow a possible normalization in the limit.

Its later finite-de-Branges discussion also observes that the finite reproducing kernel may develop singularities as \(a\to\infty\), and states that understanding those singularities is necessary to determine the precise limiting normalization.

The present derivation does **not** import v3 as a replacement source baseline.

It gives an independent source-faithful finite identity:

\[
\boxed{
\phi_+(a,z)=-a+iaz
}
\]

is the canonical right-Jost normalization for the intrinsic recentered branch, while

\[
\boxed{
\phi_-(a,z)=-a-iaz
}
\]

is the reflected left-Jost normalization.

These give nonzero half-plane limits.

They do **not** yet give Suzuki's desired single entire compact-uniform limit

\[
\frac{\xi(1/2-iz)}
{\xi(1/2-iz)+\xi'(1/2-iz)}.
\]

---

## 12. Fixed-\(\delta\) interpretation [D/G]

At fixed \(\delta>0\), the normalized scattering phase survives the cutoff:

\[
\mathcal S_{a,\delta}
\to
\mathcal S_{\infty,\delta}.
\]

But the unnormalized eigenvalue condition still contains the free phase

\[
e^{2iat}.
\]

Thus the finite spectrum retains an increasingly rapid box phase as \(a\to\infty\).

This explains simultaneously:

1. why the Schur function tends to zero in \(\mathbb C_+\);
2. why its real-axis boundary values remain unimodular;
3. why the normalized scattering phase can have a nontrivial limit;
4. why a fixed positive regulator \(\delta\) is not expected to converge directly to a discrete Xi spectrum.

The arithmetic survives as a **phase shift**, not as an unrenormalized point-spectrum limit.

---

## 13. Critical consequence: the regulator must scale with the cutoff [I/O]

v13.936 showed that

\[
a\to\infty
\quad\text{at fixed }\delta>0
\]

kills the cross-edge transfer.

The present entry shows that after removing the universal free propagation, a nontrivial Jost/scattering datum survives.

Therefore any route to the Xi characteristic must be a **critical double-scaling problem**, not the sequential limit

\[
a\to\infty
\quad\text{then}\quad
\delta\downarrow0.
\]

One must study

\[
\boxed{
a\to\infty,
\qquad
\delta=\delta(a)\downarrow0
}
\tag{35}
\]

with the regulator approaching the spectral threshold quickly enough that the cross-edge channel remains macroscopically coupled.

This is the finite-size/scattering analogue of tuning to criticality.

No particular law \(\delta(a)\) is asserted here.

Choosing one by fitting Xi or its zeros would be circular.

---

## 14. What is closed [D]

The cross-edge normalization gate is closed:

\[
\boxed{
N_{a,\delta}(z)
=
e^{2iaz}D_{a,\delta}^{\#}(z).
}
\]

The canonical deshifted transfer is

\[
\boxed{
\widetilde N_{a,\delta}(z)
=
e^{-2iaz}N_{a,\delta}(z)
=
D_{a,\delta}^{\#}(z),
}
\]

and it has the nonzero limit

\[
\boxed{
D_{\infty,\delta}^{\#}
}
\]

locally uniformly in \(\mathbb C_-\).

On the spectral axis, the canonical normalized transfer is the scattering matrix

\[
\boxed{
\mathcal S_{\infty,\delta}(t)
=
\frac{\overline{D_{\infty,\delta}(t)}}
{D_{\infty,\delta}(t)},
\qquad
|\mathcal S_{\infty,\delta}(t)|=1
\text{ a.e.}
}
\]

The finite \(\theta=\pi\) eigenvalues obey the exact quantization law

\[
\boxed{
at-\arg D_{a,\delta}(t)-\arg(t+i)\in\pi\mathbb Z.
}
\]

And the characteristic itself has the canonical Jost pair

\[
\boxed{
e^{-a\pm iaz}W_{a,\delta}^{\circ}(\pi;z)
}
\]

with nonzero limits in the corresponding half-planes.

---

## 15. Next nonredundant gate [O]

The auxiliary amplitude/propagation normalization is no longer open.

The remaining problem is critical scaling:

\[
\boxed{
\textbf{derive an intrinsic law }\delta(a)\downarrow0
\textbf{ from finite Suzuki/Weil geometry such that the cross-edge transmission remains nontrivial.}
}
\]

A valid law must be defined without using:

- Riemann zero ordinates;
- the Xi target;
- a fitted spectral phase.

Natural source-faithful candidates to test next are:

1. **fixed transmission normalization**
   using a finite deficiency-overlap invariant;

2. **correlation-length matching**
   defined by the recentered edge resolvent itself;

3. **finite de Branges kernel normalization**
   using intrinsic diagonal/off-diagonal reproducing-kernel ratios;

4. **Wronskian/Jost flux normalization**
   extracted directly from the two finite edge channels.

That is now the precise route toward a nontrivial global characteristic.
