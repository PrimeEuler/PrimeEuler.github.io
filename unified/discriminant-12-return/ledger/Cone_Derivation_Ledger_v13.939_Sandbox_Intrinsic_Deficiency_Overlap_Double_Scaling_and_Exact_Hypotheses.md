# Cone Derivation Ledger v13.939 — Sandbox: Intrinsic Deficiency-Overlap Double Scaling and Exact Hypotheses

**Date:** 2026-10-02  
**Track:** Sandbox / source-faithful Suzuki critical double-scaling lane  
**Status:** [D] exact overlap-defined double-scaling law under explicit hypotheses; [D] existence and \(\delta_\tau(a)\to0\); [C] asymptotic power law under an additional attenuation-rate hypothesis; [G] overlap fixes the scaling window but not a unique dimensionless \(\tau\) without a convention; [O] threshold attenuation exponent remains to be derived for Suzuki's operator  
**Authorization:** Jeremy, 2026-10-02 ("Derive an intrinsic double-scaling law for δ(a) from the finite Jost/deficiency overlap, and state the exact hypotheses needed for the derivation.")  
**Parents:** v13.791, v13.929, v13.935–936, v13.938  
**Collision check:** v13.939 was absent immediately before this write.

---

## 0. Question and answer

The finite intrinsic recentered family is

\[
B_a:=A_a-\lambda_a I\ge0,
\qquad
T_{a,\delta}^{\circ}
=
B_a+\delta I,
\qquad
\delta>0.
\]

For fixed \(\delta>0\), v13.936 proves that the finite Schur/Weyl data collapse:

\[
h_{a,\delta}^{\circ}\to0,
\qquad
m_{a,\delta}^{\circ}\to i.
\]

v13.938 shows that the vanishing cross-edge amplitude contains a canonical free-propagation factor and that the normalized scattering/Jost phase survives.

The remaining question is how \(\delta\) must approach the threshold while \(a\to\infty\) so that the **deficiency overlap itself remains macroscopically nonzero**.

The exact answer is:

\[
\boxed{
\kappa_a(\delta(a))
=
e^{-\tau},
\qquad
0<\tau<\infty,
}
\tag{1}
\]

where

\[
\boxed{
\kappa_a(\delta)
:=
\frac{
\langle
v_{a,+}^{\delta},
v_{a,-}^{\delta}
\rangle_{T_{a,\delta}^{\circ}}
}{
\|v_{a,+}^{\delta}\|_{T_{a,\delta}^{\circ}}^2
}
=
h_{a,\delta}^{\circ}(i).
}
\tag{2}
\]

This gives a one-parameter family of intrinsic critical scalings.

A canonical representative is the **one-e-fold law**

\[
\boxed{
\kappa_a(\delta_1(a))=e^{-1}.
}
\tag{3}
\]

Equivalently, the finite overlap correlation length equals the full edge separation \(2a\).

No Riemann zero, no Xi target, and no fitted spectral phase enter the definition.

---

## 1. Exact finite overlap formula [D]

Let

\[
v_{a,+}^{\delta}
=
(B_a+\delta I)^{-1}e^x,
\qquad
v_{a,-}^{\delta}
=
(B_a+\delta I)^{-1}e^{-x}.
\]

Reflection invariance gives

\[
v_{a,-}^{\delta}
=
Rv_{a,+}^{\delta}.
\]

The exact finite identity of v13.791 applies to the recentered branch:

\[
\boxed{
\kappa_a(\delta)
=
h_{a,\delta}^{\circ}(i)
=
m_{a,\delta}^{\circ\,\prime}(i).
}
\tag{4}
\]

Since

\[
T_{a,\delta}^{\circ}v_{a,\pm}^{\delta}
=
e^{\pm x},
\]

the overlap can be written entirely on \(L^2(-a,a)\):

\[
\boxed{
\kappa_a(\delta)
=
\frac{
\left\langle
e^{-x},
(B_a+\delta I)^{-1}e^x
\right\rangle
}{
\left\langle
e^{x},
(B_a+\delta I)^{-1}e^x
\right\rangle
}.
}
\tag{5}
\]

Thus \(\kappa_a\) is a finite resolvent observable.

---

## 2. Exact Jost formula at the canonical base point [D]

From v13.938,

\[
h_{a,\delta}^{\circ}(z)
=
e^{2iaz}
\frac{D_{a,\delta}^{\#}(z)}
{D_{a,\delta}(z)}.
\]

At

\[
z=i,
\]

the free propagation factor is

\[
e^{2ia i}=e^{-2a}.
\]

Since the right-edge response is real,

\[
D_{a,\delta}^{\#}(i)
=
D_{a,\delta}(-i).
\]

Therefore

\[
\boxed{
\kappa_a(\delta)
=
e^{-2a}
\frac{D_{a,\delta}(-i)}
{D_{a,\delta}(i)}.
}
\tag{6}
\]

The double-scaling condition (1) is exactly

\[
\boxed{
\frac{D_{a,\delta(a)}(-i)}
{D_{a,\delta(a)}(i)}
=
e^{2a-\tau}.
}
\tag{7}
\]

Thus the regulator is tuned until the intrinsic Jost amplification cancels all but a fixed fraction \(e^{-\tau}\) of the geometric cross-edge attenuation.

---

## 3. Parity-channel form [D]

Write

\[
e^x
=
\cosh x+\sinh x.
\]

Because \(B_a\) commutes with reflection, its resolvent preserves parity.

Define the even and odd susceptibilities

\[
\boxed{
E_a(\delta)
=
\left\langle
\cosh x,
(B_a+\delta I)^{-1}\cosh x
\right\rangle,
}
\tag{8}
\]

\[
\boxed{
O_a(\delta)
=
\left\langle
\sinh x,
(B_a+\delta I)^{-1}\sinh x
\right\rangle.
}
\tag{9}
\]

Cross terms vanish.

Hence

\[
\boxed{
\kappa_a(\delta)
=
\frac{E_a(\delta)-O_a(\delta)}
{E_a(\delta)+O_a(\delta)}.
}
\tag{10}
\]

Equivalently,

\[
\boxed{
\frac{O_a(\delta)}{E_a(\delta)}
=
\frac{1-\kappa_a(\delta)}
{1+\kappa_a(\delta)}.
}
\tag{11}
\]

On the critical scaling (1),

\[
\boxed{
\frac{O_a(\delta_\tau(a))}
{E_a(\delta_\tau(a))}
=
\tanh\!\left(\frac{\tau}{2}\right).
}
\tag{12}
\]

So the same double-scaling law can be read as a fixed intrinsic ratio of odd to even deficiency susceptibility.

---

## 4. Large-\(\delta\) endpoint [D]

For fixed finite \(a\),

\[
\delta(B_a+\delta I)^{-1}
\longrightarrow
I
\]

strongly as

\[
\delta\to\infty.
\]

Therefore from (5),

\[
\lim_{\delta\to\infty}
\kappa_a(\delta)
=
\frac{
\langle e^{-x},e^x\rangle
}{
\langle e^x,e^x\rangle
}.
\]

Now

\[
\langle e^{-x},e^x\rangle
=
2a,
\]

while

\[
\langle e^x,e^x\rangle
=
\int_{-a}^{a}e^{2x}dx
=
\sinh(2a).
\]

Thus

\[
\boxed{
\kappa_a(\infty)
:=
\lim_{\delta\to\infty}\kappa_a(\delta)
=
\frac{2a}{\sinh(2a)}.
}
\tag{13}
\]

In particular,

\[
\boxed{
\kappa_a(\infty)
\sim
4a\,e^{-2a}.
}
\tag{14}
\]

For every fixed \(\tau>0\),

\[
\kappa_a(\infty)<e^{-\tau}
\]

for all sufficiently large \(a\).

---

## 5. Threshold endpoint and exact ground-channel hypothesis [D/C]

Let

\[
P_{0,a}
=
\mathbf 1_{\{0\}}(B_a)
\]

be the spectral projection onto the finite recentered ground eigenspace.

The exact hypothesis needed at the threshold is:

\[
\boxed{
P_{0,a}e^x\neq0,
\qquad
P_{0,a}e^{-x}
=
P_{0,a}e^x.
}
\tag{H1}
\]

This says that the ground spectral channel is reflection-even and is actually seen by the deficiency source.

A sufficient, simpler hypothesis is:

\[
\boxed{
\ker B_a
\text{ is one-dimensional, spanned by a reflection-even }\psi_{0,a},
\quad
\langle\psi_{0,a},e^x\rangle\neq0.
}
\tag{H1'}
\]

Because \(0\) is an isolated eigenvalue at finite \(a\), the resolvent has

\[
(B_a+\delta I)^{-1}
=
\delta^{-1}P_{0,a}
+
R_{a,\delta}^{\perp},
\]

with \(R_{a,\delta}^{\perp}\) bounded as \(\delta\downarrow0\).

Using (H1) in (5),

\[
\boxed{
\lim_{\delta\downarrow0}
\kappa_a(\delta)
=
1.
}
\tag{15}
\]

No simplicity assumption is needed if (H1) itself holds.

---

## 6. Continuity in the regulator [D]

For every finite \(a\),

\[
\delta\mapsto(B_a+\delta I)^{-1}
\]

is norm analytic for \(\delta>0\).

Therefore

\[
\boxed{
\delta\mapsto\kappa_a(\delta)
}
\]

is continuous on \((0,\infty)\).

Under (H1), equation (15) gives a continuous extension to

\[
\delta=0
\]

with

\[
\kappa_a(0)=1.
\]

No monotonicity in \(\delta\) is asserted or required.

Indeed, from the parity representation (10), monotonicity would require additional information comparing the even and odd spectral measures.

---

## 7. First-crossing definition of the intrinsic scale [D]

Fix

\[
\tau>0.
\]

For sufficiently large \(a\), (13)–(15) give

\[
\kappa_a(0)=1>e^{-\tau},
\]

and

\[
\kappa_a(\infty)<e^{-\tau}.
\]

Define the **first-crossing regulator**

\[
\boxed{
\delta_\tau(a)
:=
\inf
\left\{
\delta>0:
\kappa_a(\delta)\le e^{-\tau}
\right\}.
}
\tag{16}
\]

Continuity implies

\[
\boxed{
0<\delta_\tau(a)<\infty,
}
\tag{17}
\]

and

\[
\boxed{
\kappa_a(\delta_\tau(a))
=
e^{-\tau}.
}
\tag{18}
\]

This definition is unique even if \(\kappa_a(\delta)\) is not globally monotone.

If one additionally proves strict decrease through the crossing, then \(\delta_\tau(a)\) is the unique ordinary solution of (18).

---

## 8. The regulator necessarily tends to the threshold [D]

The second structural hypothesis is the finite-floor condition

\[
\boxed{
\lambda_\infty
:=
\lim_{a\to\infty}\lambda_a
>-\infty.
}
\tag{H2}
\]

Under (H2), v13.936 proves that for every fixed

\[
\varepsilon>0,
\]

\[
\boxed{
\kappa_a(\varepsilon)
=
h_{a,\varepsilon}^{\circ}(i)
\longrightarrow0.
}
\tag{19}
\]

Fix any \(\varepsilon>0\).

For sufficiently large \(a\),

\[
\kappa_a(\varepsilon)
<
e^{-\tau}.
\]

Since

\[
\kappa_a(0)=1>e^{-\tau},
\]

the first crossing must occur before \(\varepsilon\):

\[
0<\delta_\tau(a)<\varepsilon.
\]

Because \(\varepsilon>0\) was arbitrary,

\[
\boxed{
\delta_\tau(a)\longrightarrow0.
}
\tag{20}
\]

Thus (16) is a genuine intrinsic double scaling:

\[
\boxed{
a\to\infty,
\qquad
\delta_\tau(a)\downarrow0.
}
\]

---

## 9. Exact finite-size attenuation law [D]

Whenever

\[
0<\kappa_a(\delta)<1,
\]

define the finite overlap attenuation rate

\[
\boxed{
\mu_a(\delta)
:=
-\frac{1}{2a}
\log\kappa_a(\delta).
}
\tag{21}
\]

Equivalently define the overlap correlation length

\[
\boxed{
\ell_a(\delta)
:=
\frac{1}{\mu_a(\delta)}
=
\frac{2a}
{-\log\kappa_a(\delta)}.
}
\tag{22}
\]

The first-crossing law (18) becomes the exact identity

\[
\boxed{
2a\,\mu_a(\delta_\tau(a))
=
\tau.
}
\tag{23}
\]

Equivalently,

\[
\boxed{
\ell_a(\delta_\tau(a))
=
\frac{2a}{\tau}.
}
\tag{24}
\]

Thus the critical scaling is precisely the regime in which the correlation length is proportional to the edge separation.

For the one-e-fold convention

\[
\tau=1,
\]

\[
\boxed{
\ell_a(\delta_1(a))
=
2a.
}
\tag{25}
\]

This is the canonical representative used when a single law rather than the full scaling family is desired.

---

## 10. What is intrinsic and what is conventional [G]

The finite data determine the **scaling window**

\[
2a\,\mu_a(\delta)=O(1)
\]

intrinsically.

They do not select one particular positive dimensionless number \(\tau\).

Different fixed choices

\[
\tau\in(0,\infty)
\]

pick different points inside the same critical window.

Choosing

\[
\tau=1
\]

is the standard one-e-fold convention, analogous to defining a correlation length by decay to \(e^{-1}\).

This is a normalization convention, not additional arithmetic input.

No choice of \(\tau\) may be made by fitting Riemann zero data or the Xi target.

The scaling exponent derived below is independent of fixed \(\tau\).

---

## 11. Thermodynamic attenuation hypothesis [C]

To convert the exact implicit law (23) into an explicit asymptotic formula for \(\delta_\tau(a)\), one needs additional information not presently proved for Suzuki's operator.

The required hypothesis is a **uniform critical-window attenuation law**.

Assume there exists

\[
\mu:(0,\delta_0]\to(0,\infty)
\]

such that:

\[
\boxed{
\mu(\delta)\downarrow0
\qquad(\delta\downarrow0),
}
\tag{H3a}
\]

\[
\boxed{
\mu
\text{ is continuous and strictly increasing near }0,
}
\tag{H3b}
\]

and, uniformly along the critical window containing \(\delta_\tau(a)\),

\[
\boxed{
-\log\kappa_a(\delta)
=
2a\,\mu(\delta)
+
r_a(\delta),
\qquad
r_a(\delta)\to0.
}
\tag{H3c}
\]

Equivalently,

\[
\boxed{
\mu_a(\delta)
=
\mu(\delta)
+
o(a^{-1})
}
\]

in that window.

Then at the intrinsic scaling point,

\[
\tau
=
-\log\kappa_a(\delta_\tau(a))
=
2a\mu(\delta_\tau(a))
+
o(1).
\]

Therefore

\[
\boxed{
\mu(\delta_\tau(a))
=
\frac{\tau}{2a}
+
o(a^{-1}).
}
\tag{26}
\]

This is the asymptotic double-scaling equation.

---

## 12. Power-law threshold and explicit scaling exponent [C]

Assume in addition that the infinite attenuation rate has the threshold asymptotic

\[
\boxed{
\mu(\delta)
=
c\,\delta^\nu(1+o(1)),
\qquad
c>0,
\quad
\nu>0.
}
\tag{H4}
\]

Then (26) gives

\[
c\,\delta_\tau(a)^\nu
\sim
\frac{\tau}{2a}.
\]

Hence

\[
\boxed{
\delta_\tau(a)
\sim
\left(
\frac{\tau}{2ca}
\right)^{1/\nu}.
}
\tag{27}
\]

Thus the double-scaling exponent is

\[
\boxed{
\delta(a)\asymp a^{-1/\nu}.
}
\]

The choice of fixed \(\tau\) changes only the multiplicative constant:

\[
\delta_{\tau_1}(a)
/
\delta_{\tau_2}(a)
\to
\left(
\frac{\tau_1}{\tau_2}
\right)^{1/\nu}.
\]

It does not change the universality exponent.

---

## 13. Quadratic-threshold special case [C/G]

If the edge attenuation has a nondegenerate quadratic threshold,

\[
\boxed{
\mu(\delta)
\sim
c\sqrt{\delta},
}
\tag{H4q}
\]

then

\[
\nu=\frac12
\]

and

\[
\boxed{
\delta_\tau(a)
\sim
\frac{\tau^2}
{4c^2a^2}.
}
\tag{28}
\]

For the one-e-fold convention,

\[
\boxed{
\delta_1(a)
\sim
\frac{1}
{4c^2a^2}.
}
\tag{29}
\]

Important guardrail:

\[
\boxed{
\textbf{the }\sqrt{\delta}\textbf{ threshold law has not yet been proved for Suzuki's recentered Weil/Jost operator.}
}
\]

Equation (28) is therefore a conditional specialization, not the current unconditional result.

Deriving the threshold exponent \(\nu\) is the next analytical gate.

---

## 14. Optional transversality hypothesis [C]

The first-crossing definition (16) requires no monotonicity.

If one wants \(\delta_\tau(a)\) to depend smoothly on \(a\), or wants to differentiate the scaling law, add the local transversality condition

\[
\boxed{
\partial_\delta\kappa_a(\delta_\tau(a))<0.
}
\tag{H5}
\]

Then the implicit-function theorem gives local smooth dependence on any continuously varying finite-size parameter.

This is not needed for existence, uniqueness by first crossing, or the conclusion \(\delta_\tau(a)\to0\).

---

## 15. Exact hypothesis ledger

The derivation has three distinct levels.

### Level I — exact finite overlap/Jost identities [already established]

Needed:

1. \(A_a\) self-adjoint and reflection invariant;
2. \(\lambda_a=\inf\sigma(A_a)\);
3. \(B_a=A_a-\lambda_a I\ge0\);
4. Suzuki deficiency sources
   \[
   v_\pm=(B_a+\delta)^{-1}e^{\pm x};
   \]
5. the v13.791 overlap identity;
6. the v13.938 Jost factorization.

These are project-established finite identities.

### Level II — existence of the intrinsic double scaling [H1 + H2]

Needed:

\[
\boxed{
\text{(H1) ground-channel alignment}
}
\]

so that

\[
\kappa_a(0+)=1,
\]

and

\[
\boxed{
\text{(H2) }\lambda_\infty>-\infty
}
\]

so that v13.936 supplies

\[
\kappa_a(\delta)\to0
\]

for every fixed \(\delta>0\).

Then the first-crossing law exists and

\[
\boxed{
\delta_\tau(a)\to0.
}
\]

No monotonicity assumption is needed.

### Level III — explicit asymptotic power law [H3 + H4]

Needed:

\[
\boxed{
\text{(H3) uniform critical-window attenuation exponent}
}
\]

and

\[
\boxed{
\text{(H4) threshold regular variation/power law.}
}
\]

Then

\[
\boxed{
\delta_\tau(a)
\sim
\left(
\frac{\tau}{2ca}
\right)^{1/\nu}.
}
\]

The special \(a^{-2}\) law additionally requires the unproved quadratic threshold hypothesis (H4q).

---

## 16. Relation to RH [G]

No RH statement follows from defining \(\delta_\tau(a)\).

The finite recentered construction exists independently of the absolute value of the global threshold.

However, v13.935 proved

\[
\mathrm{RH}
\iff
\lambda_\infty=0.
\]

Thus under RH, hypothesis (H2) is certainly satisfied and the double-scaling regulator approaches Suzuki's absolute \(\lambda=0\) threshold:

\[
\lambda_{a,\delta_\tau(a)}^{\circ}
=
\lambda_a-\delta_\tau(a)
\longrightarrow0.
\]

Without RH, if

\[
-\infty<\lambda_\infty<0,
\]

the same intrinsic double scaling exists but approaches the shifted absolute threshold

\[
\lambda_\infty.
\]

So the overlap law itself does not assume the conclusion of the Xi branch.

---

## 17. Result

The finite Jost/deficiency overlap supplies an intrinsic finite-size correlation length:

\[
\boxed{
\ell_a(\delta)
=
\frac{2a}
{-\log\kappa_a(\delta)}.
}
\]

The critical double-scaling window is exactly

\[
\boxed{
\ell_a(\delta(a))
\asymp a.
}
\]

Equivalently,

\[
\boxed{
\kappa_a(\delta_\tau(a))
=
e^{-\tau},
\qquad
\delta_\tau(a)\to0.
}
\]

A canonical one-e-fold representative is

\[
\boxed{
\kappa_a(\delta_1(a))
=
e^{-1},
\qquad
\ell_a(\delta_1(a))
=
2a.
}
\]

At the Jost level this is

\[
\boxed{
\frac{D_{a,\delta_1(a)}(-i)}
{D_{a,\delta_1(a)}(i)}
=
e^{2a-1}.
}
\]

Under a uniform attenuation law

\[
\mu(\delta)\sim c\delta^\nu,
\]

the scaling becomes

\[
\boxed{
\delta_\tau(a)
\sim
\left(
\frac{\tau}{2ca}
\right)^{1/\nu}.
}
\]

The only genuinely new analytic quantity still missing is the threshold attenuation exponent \(\nu\) (and coefficient \(c\)) for Suzuki's recentered edge/Jost problem.

That is the next nonredundant gate.
