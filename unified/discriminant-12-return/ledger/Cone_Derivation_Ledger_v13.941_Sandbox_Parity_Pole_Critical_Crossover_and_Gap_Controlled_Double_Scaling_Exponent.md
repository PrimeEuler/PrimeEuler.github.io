# Cone Derivation Ledger v13.941 — Sandbox: Parity-Pole Critical Crossover and Gap-Controlled Double-Scaling Exponent

**Date:** 2026-10-02  
**Track:** Sandbox / source-faithful Suzuki critical double-scaling lane  
**Status:** [D] exact parity spectral-measure crossover equation; [C] gap-controlled asymptotic theorem under explicit near-zero spectral hypotheses; [R] refines/supersedes the optional bulk attenuation ansatz of v13.940; [G] no claim yet that the first odd gap is \(a^{-2}\); [O] derive/certify the odd-gap closing law and residue ratio  
**Authorization:** Jeremy, 2026-10-02 ("sweeeet. good job. lets do it... keep going!")  
**Parents:** v13.791–792, v13.795, v13.935–936, v13.938, v13.940  
**Collision check:** v13.941 was absent immediately before this write.

---

## 0. Why this gate changes the target

v13.940 defined the intrinsic double-scaling window by the finite deficiency overlap

\[
\kappa_a(\delta_\tau(a))
=
e^{-\tau},
\qquad
\tau>0,
\]

and introduced the optional thermodynamic ansatz

\[
-\log\kappa_a(\delta)
=
2a\,\mu(\delta)+o(1),
\qquad
\mu(\delta)\sim c\delta^\nu.
\]

That ansatz is sufficient but stronger than needed.

The finite parity spectral theorem gives a sharper route:

\[
\boxed{
\textbf{the critical regulator is controlled directly by the near-zero parity spectrum of }
B_a:=A_a-\lambda_a I.
}
\]

The exact crossover equation is a Stieltjes-transform equation for the even and odd source spectral measures.

Under a one-even-ground / one-odd-pole regime,

\[
\boxed{
\delta_\tau(a)
\sim
x_\tau\,\Delta_a,
}
\]

where

\[
\Delta_a
=
\inf\sigma(B_a|_{\rm odd})
\]

is the first odd recentered gap and \(x_\tau\) is an explicit residue-dependent constant.

Therefore:

\[
\boxed{
\textbf{the double-scaling exponent is the closing exponent of the first odd gap.}
}
\]

A \(\sqrt\delta\) attenuation law is not assumed. It would follow only if the odd gap itself scales like \(a^{-2}\) and additional single-scale hypotheses hold.

---

## 1. Parity decomposition of the recentered operator [D]

Let

\[
B_a
=
A_a-\lambda_a I
\ge0.
\]

Reflection

\[
(Rf)(x)=f(-x)
\]

commutes with \(B_a\), so

\[
L^2(-a,a)
=
\mathcal H_a^{(+)}
\oplus
\mathcal H_a^{(-)}
\]

and

\[
B_a
=
B_a^{(+)}
\oplus
B_a^{(-)}.
\]

Write the deficiency source as

\[
e^x
=
c_a+s_a,
\]

with

\[
c_a(x)=\cosh x,
\qquad
s_a(x)=\sinh x.
\]

For \(\delta>0\), define the parity susceptibilities

\[
\boxed{
E_a(\delta)
=
\langle
c_a,
(B_a^{(+)}+\delta I)^{-1}c_a
\rangle,
}
\tag{1}
\]

\[
\boxed{
O_a(\delta)
=
\langle
s_a,
(B_a^{(-)}+\delta I)^{-1}s_a
\rangle.
}
\tag{2}
\]

Then the exact deficiency-overlap identity of v13.940 is

\[
\boxed{
\kappa_a(\delta)
=
\frac{E_a(\delta)-O_a(\delta)}
{E_a(\delta)+O_a(\delta)}.
}
\tag{3}
\]

Equivalently,

\[
\boxed{
\frac{O_a(\delta)}{E_a(\delta)}
=
\frac{1-\kappa_a(\delta)}
{1+\kappa_a(\delta)}.
}
\tag{4}
\]

At the intrinsic level

\[
\kappa_a(\delta_\tau(a))
=
e^{-\tau},
\]

define

\[
\boxed{
q_\tau
:=
\frac{1-e^{-\tau}}
{1+e^{-\tau}}
=
\tanh\!\left(\frac{\tau}{2}\right).
}
\tag{5}
\]

Then the critical regulator is characterized exactly by

\[
\boxed{
O_a(\delta_\tau(a))
=
q_\tau
E_a(\delta_\tau(a)).
}
\tag{6}
\]

This equation is the starting point for the threshold exponent.

---

## 2. Exact source spectral measures [D]

Let

\[
P_{0,a}^{(+)}
=
\mathbf 1_{\{0\}}(B_a^{(+)}).
\]

Under the ground-channel hypothesis of v13.940,

\[
P_{0,a}^{(+)}c_a\ne0.
\]

Define the even ground residue

\[
\boxed{
\alpha_a
:=
\|P_{0,a}^{(+)}c_a\|_2^2
>0.
}
\tag{7}
\]

Let \(\mu_{a,+}\) be the positive spectral measure of \(c_a\) for \(B_a^{(+)}\) with the zero atom removed:

\[
\mu_{a,+}(S)
=
\langle
c_a,
\mathbf 1_S(B_a^{(+)})
(1-P_{0,a}^{(+)})
c_a
\rangle,
\qquad
S\subset(0,\infty).
\]

Let \(\mu_{a,-}\) be the odd source spectral measure

\[
\mu_{a,-}(S)
=
\langle
s_a,
\mathbf 1_S(B_a^{(-)})
s_a
\rangle,
\qquad
S\subset(0,\infty).
\]

Then the spectral theorem gives the exact Stieltjes representations

\[
\boxed{
E_a(\delta)
=
\frac{\alpha_a}{\delta}
+
\int_{(0,\infty)}
\frac{d\mu_{a,+}(\lambda)}
{\lambda+\delta},
}
\tag{8}
\]

\[
\boxed{
O_a(\delta)
=
\int_{(0,\infty)}
\frac{d\mu_{a,-}(\lambda)}
{\lambda+\delta}.
}
\tag{9}
\]

Therefore the exact critical equation is

\[
\boxed{
\int_{(0,\infty)}
\frac{d\mu_{a,-}(\lambda)}
{\lambda+\delta_\tau}
=
q_\tau
\left[
\frac{\alpha_a}{\delta_\tau}
+
\int_{(0,\infty)}
\frac{d\mu_{a,+}(\lambda)}
{\lambda+\delta_\tau}
\right].
}
\tag{10}
\]

No infinite-volume attenuation hypothesis is used.

---

## 3. General rescaled spectral-measure crossover [C]

Choose a positive critical energy scale

\[
\Delta_a\downarrow0
\]

and a positive source-residue scale

\[
\beta_a>0.
\]

Define

\[
r_a
=
\frac{\alpha_a}{\beta_a}.
\]

Push the positive spectral measures to the scaled variable

\[
t=\frac{\lambda}{\Delta_a}
\]

and normalize their mass by \(\beta_a\):

\[
\boxed{
\nu_{a,\pm}(S)
=
\frac{1}{\beta_a}
\mu_{a,\pm}(\Delta_a S).
}
\tag{11}
\]

For

\[
\delta=x\Delta_a,
\qquad x>0,
\]

equations (8)–(9) become

\[
\boxed{
E_a(x\Delta_a)
=
\frac{\beta_a}{\Delta_a}
\left[
\frac{r_a}{x}
+
G_{a,+}(x)
\right],
}
\tag{12}
\]

\[
\boxed{
O_a(x\Delta_a)
=
\frac{\beta_a}{\Delta_a}
G_{a,-}(x),
}
\tag{13}
\]

where

\[
\boxed{
G_{a,\pm}(x)
=
\int_{(0,\infty)}
\frac{d\nu_{a,\pm}(t)}
{t+x}.
}
\tag{14}
\]

Assume:

\[
\boxed{
r_a\to r\in(0,\infty),
}
\tag{H1}
\]

and the rescaled Stieltjes transforms converge locally uniformly on \(x>0\):

\[
\boxed{
G_{a,\pm}(x)\to G_\pm(x).
}
\tag{H2}
\]

Then any critical scaling

\[
\frac{\delta_\tau(a)}{\Delta_a}\to x_\tau
\]

must satisfy the limiting crossover equation

\[
\boxed{
G_-(x_\tau)
=
q_\tau
\left[
\frac{r}{x_\tau}
+
G_+(x_\tau)
\right].
}
\tag{15}
\]

If (15) has a unique positive solution and the crossing is transversal, then

\[
\boxed{
\frac{\delta_\tau(a)}{\Delta_a}
\longrightarrow
x_\tau.
}
\tag{16}
\]

This is the general finite spectral-measure double-scaling theorem.

---

## 4. One-odd-pole dominance [C]

Let

\[
\Delta_a
=
\inf\sigma(B_a^{(-)}).
\]

Assume this is a simple odd eigenvalue with normalized eigenvector

\[
\psi_{1,a}^{(-)}.
\]

Define its source residue

\[
\boxed{
\beta_a
=
|\langle
\psi_{1,a}^{(-)},
s_a
\rangle|^2.
}
\tag{17}
\]

The single-odd-pole hypothesis is

\[
\boxed{
\nu_{a,-}
\Longrightarrow
\delta_1
}
\tag{H3}
\]

at the level of Stieltjes transforms, i.e.

\[
\boxed{
G_{a,-}(x)
\longrightarrow
\frac{1}{1+x}
}
\tag{18}
\]

locally uniformly for \(x>0\).

The even-remainder-negligibility hypothesis is

\[
\boxed{
G_{a,+}(x)\longrightarrow0
}
\tag{H4}
\]

locally uniformly for \(x>0\).

Finally assume

\[
\boxed{
r_a=\frac{\alpha_a}{\beta_a}
\longrightarrow
r\in(0,\infty).
}
\tag{H5}
\]

Then (15) becomes

\[
\frac{1}{1+x_\tau}
=
q_\tau
\frac{r}{x_\tau}.
\]

Hence

\[
x_\tau
=
q_\tau r(1+x_\tau),
\]

so

\[
\boxed{
x_\tau
=
\frac{q_\tau r}
{1-q_\tau r},
}
\tag{19}
\]

provided

\[
\boxed{
q_\tau r<1.
}
\tag{H6}
\]

Therefore

\[
\boxed{
\delta_\tau(a)
\sim
\frac{q_\tau r}
{1-q_\tau r}
\,
\Delta_a.
}
\tag{20}
\]

This is the sharp finite parity-pole law.

---

## 5. Exact interpretation of the condition \(q_\tau r<1\) [D/I]

In the two-pole model,

\[
\frac{O}{E}
\approx
\frac{1}{r}
\frac{x}{1+x}.
\]

As

\[
x\to\infty,
\]

the maximal ratio available within this one-scale approximation is

\[
\frac{1}{r}.
\]

Therefore the target

\[
q_\tau
\]

can be reached on this scale exactly when

\[
q_\tau<\frac1r,
\]

equivalently

\[
q_\tau r<1.
\]

If

\[
q_\tau r\ge1,
\]

the first-crossing regulator still exists by v13.940 under its hypotheses, but it does not lie in the single-odd-pole \(\Delta_a\) window.

Then at least one of the following must contribute:

- higher odd modes;
- positive even modes;
- another smaller/larger spectral scale.

Thus failure of (H6) is diagnostic, not a contradiction.

---

## 6. More elementary pole-expansion form [C]

The same result can be written without rescaled measures.

Suppose in the critical window

\[
\boxed{
E_a(\delta)
=
\frac{\alpha_a}{\delta}
+
R_{a,+}(\delta),
}
\tag{21}
\]

\[
\boxed{
O_a(\delta)
=
\frac{\beta_a}{\Delta_a+\delta}
+
R_{a,-}(\delta),
}
\tag{22}
\]

with

\[
\boxed{
\frac{\Delta_a}{\beta_a}
R_{a,\pm}(x\Delta_a)
\to0
}
\tag{H7}
\]

locally uniformly for \(x>0\).

Then the exact equation

\[
O_a=q_\tau E_a
\]

gives

\[
\frac{\beta_a}{\Delta_a+\delta}
=
q_\tau
\frac{\alpha_a}{\delta}
+
o\!\left(\frac{\beta_a}{\Delta_a}\right).
\]

If

\[
\alpha_a/\beta_a\to r,
\]

then (20) follows.

---

## 7. The critical exponent is the odd-gap exponent [D/C]

Assume the one-pole hypotheses above and suppose

\[
\boxed{
\Delta_a
\sim
C\,a^{-p}L(a),
}
\tag{23}
\]

where

\[
C>0,
\qquad
p>0,
\]

and \(L\) is slowly varying or simply \(L(a)\to1\).

Then from (20),

\[
\boxed{
\delta_\tau(a)
\sim
\frac{q_\tau r}
{1-q_\tau r}
C\,a^{-p}L(a).
}
\tag{24}
\]

Therefore

\[
\boxed{
\textbf{the double-scaling exponent is }p,
}
\]

the closing exponent of the first odd recentered gap.

No separate attenuation exponent needs to be postulated.

---

## 8. Relation to the \(\mu(\delta)\) ansatz of v13.940 [R/G]

v13.940 introduced the optional stronger hypothesis

\[
\mu(\delta)\sim c\delta^\nu
\]

which would imply

\[
\delta_\tau(a)\asymp a^{-1/\nu}.
\]

Under the present one-pole theorem,

\[
\delta_\tau(a)\asymp a^{-p},
\]

so if both descriptions are simultaneously valid,

\[
\boxed{
\nu=\frac1p.
}
\tag{25}
\]

In particular,

\[
p=2
\quad\Longleftrightarrow\quad
\nu=\frac12.
\]

However, there is an important refinement.

The finite crossover coefficient

\[
x_\tau
=
\frac{q_\tau r}{1-q_\tau r}
\]

is not generically proportional to a fixed power of \(\tau\).

Therefore the existence of one \(\tau\)-independent thermodynamic function \(\mu(\delta)\) with a uniform law across the whole crossover family is an additional scaling assumption.

It is not automatic from the finite parity spectrum.

Hence:

\[
\boxed{
\textbf{v13.940's H3/H4 are optional stronger hypotheses, not prerequisites for the double-scaling exponent.}
}
\]

The finite parity-pole theorem is the sharper current route.

---

## 9. Quadratic-gap specialization [C/G]

If future analysis or certified numerics establishes

\[
\boxed{
\Delta_a
\sim
\frac{C}{a^2},
}
\tag{26}
\]

then

\[
\boxed{
\delta_\tau(a)
\sim
\frac{q_\tau r}
{1-q_\tau r}
\frac{C}{a^2}.
}
\tag{27}
\]

This is the \(a^{-2}\) critical law.

If one additionally insists on a bulk attenuation representation, then its threshold exponent would be

\[
\boxed{
\nu=\frac12.
}
\]

But at present

\[
\boxed{
\textbf{the project has not proved }\Delta_a\sim C a^{-2}\textbf{ for Suzuki's recentered odd sector.}
}
\]

So no \(\sqrt\delta\) claim is promoted.

---

## 10. Why the old Galerkin numbers do not determine \(p\) [G]

v13.795 observed extremely small parity-block Ritz eigenvalues already at

\[
a=0.5,\ 1,
\]

and severe near-null conditioning.

Those computations were designed as fixed-\(a\) form-core diagnostics, not as a certified large-\(a\) study of the recentered parity gap.

The displayed minima also changed rapidly with Galerkin dimension.

Therefore they cannot be used to infer

\[
\Delta_a\sim C a^{-p}.
\]

The exponent \(p\) requires either:

1. an analytic finite-size theorem for the odd sector, or
2. a source-faithful protected-subspace computation across a controlled sequence of \(a\)-values with certified discretization error.

---

## 11. Exact hypotheses for the one-pole law

The derivation of (20) needs exactly the following.

### Finite structural hypotheses [already in the project]

- \(B_a=A_a-\lambda_a I\ge0\) is self-adjoint with compact resolvent.
- \(B_a\) commutes with reflection.
- The zero spectral channel seen by \(\cosh x\) is even.
- The overlap is defined from the source-faithful recentered deficiency vectors.

### Near-zero spectral hypotheses [new]

\[
\boxed{
\text{(P1) }\Delta_a:=\inf\sigma(B_a^{(-)})\downarrow0.
}
\]

\[
\boxed{
\text{(P2) the first odd eigenvalue is source-visible: }
\beta_a>0.
}
\]

\[
\boxed{
\text{(P3) }\alpha_a/\beta_a\to r\in(0,\infty).
}
\]

\[
\boxed{
\text{(P4) the first odd pole dominates the rescaled odd Stieltjes transform.}
}
\]

\[
\boxed{
\text{(P5) the positive even remainder is negligible on the }\Delta_a\text{ scale.}
}
\]

\[
\boxed{
\text{(P6) }q_\tau r<1.
}
\]

Under P1–P6,

\[
\boxed{
\delta_\tau(a)
\sim
\frac{q_\tau r}{1-q_\tau r}
\Delta_a.
}
\]

No RH assumption enters this finite recentered statement.

---

## 12. Next analytical gate [O]

The threshold exponent problem has now been reduced to a concrete finite spectral problem.

The next quantities to determine are

\[
\boxed{
\Delta_a
=
\inf\sigma(B_a^{(-)})
}
\]

and

\[
\boxed{
r_a
=
\frac{
\|P_{0,a}^{(+)}\cosh\|^2
}{
|\langle\psi_{1,a}^{(-)},\sinh\rangle|^2
}.
}
\]

The priority order is:

1. prove or numerically certify whether
   \[
   \Delta_a
   \asymp
   a^{-p}
   \]
   and determine \(p\);

2. determine whether
   \[
   r_a\to r\in(0,\infty);
   \]

3. verify single-odd-pole dominance and even-remainder negligibility.

If all three close, the intrinsic double-scaling law is explicit with no fitted Xi input.

---

## 13. Result

The regulator critical exponent is no longer an abstract attenuation parameter.

The exact finite overlap equation is

\[
\boxed{
O_a(\delta_\tau)
=
\tanh(\tau/2)\,
E_a(\delta_\tau).
}
\]

The parity spectral theorem reduces this to the near-zero Stieltjes crossover.

Under one-even-ground / one-odd-pole dominance,

\[
\boxed{
\delta_\tau(a)
\sim
\frac{
\tanh(\tau/2)\,r
}{
1-\tanh(\tau/2)\,r
}
\Delta_a.
}
\]

Therefore

\[
\boxed{
\textbf{the intrinsic double-scaling exponent equals the closing exponent of the first odd recentered spectral gap.}
}
\]

The next nonredundant gate is not to assume \(\sqrt\delta\).

It is to determine the actual asymptotic law of

\[
\Delta_a.
\]
