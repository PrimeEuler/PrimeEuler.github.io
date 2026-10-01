# Cone Derivation Ledger v13.921 — Sandbox: Gaussian Selection Theorem on the Cone Fixed Locus

**Date:** 2026-10-01
**Track:** Sandbox / compression-cone zero-ordinate lane
**Status:** [D] exact conditional selection theorem; [G] guardrails; [O] residual geometric axiom question
**Authorization:** Jeremy, 2026-10-01 ("take the next gate. watch out for ledger collisions.")
**Parents:** v13.573/574 (square fixed locus), v13.717/722 (theta/Mellin and pure Xi kernels), v13.917 (fixed-locus heat-trace resonance bridge), v13.919 (common shell measure / prime-theta bridge), v13.920 (External Audit Round 136)
**Collision check:** v13.921 was absent immediately before this write; live head was v13.920.

---

## 0. Question

v13.919 ends with the geometric-selection gate:

\[
\boxed{
\text{Does the cone geometry uniquely select the Gaussian/self-dual heat transform among all transforms of }\mu_{\rm shell}\text{?}
}
\]

The answer is:

\[
\boxed{
\textbf{YES within the canonical class of autonomous positive scalar evolutions that respect the cone's quadratic dilation and exact Poisson self-duality.}
}
\]

Self-duality by itself is not enough; semigroup structure by itself is not enough. The conjunction is load-bearing.

---

## 1. Continuous factor-exchange fixed locus and its intrinsic quadratic invariant [D]

From v13.573/574, the factor-exchange fixed locus is \(X=0\). Before imposing arithmetic integrality, write the continuous fixed line as

\[
\mathcal F
=
\{(X,Y,T)=(0,Y,|Y|):Y\in\mathbb R\}.
\]

The cone equation restricts to

\[
\boxed{
q(Y)=Y^2=T^2.
}
\]

Under the natural cone dilation

\[
D_a:Y\mapsto aY,\qquad a>0,
\]

the invariant scales as

\[
\boxed{
q(aY)=a^2q(Y).
}
\]

The arithmetic fixed lattice is the integer sample

\[
\mathcal F_{\mathbb Z}:\quad Y=m,\qquad m\in\mathbb Z.
\]

---

## 2. Canonical scalar evolution axioms [G/D]

Consider a family of positive scalar weights

\[
h_x(Y)>0,\qquad x\ge0,
\]

on the continuous fixed locus. Impose the following explicit axioms.

### A1. Autonomous semigroup [Axiom]

\[
h_0(Y)=1,
\qquad
h_{x+y}(Y)=h_x(Y)h_y(Y),
\]

with \(x\mapsto h_x(Y)\) continuous.

This is the ordinary time-homogeneous semigroup law for a diagonal heat/spectral evolution.

### A2. Root-sheet symmetry [Axiom]

\[
h_x(-Y)=h_x(Y).
\]

### A3. Cone quadratic dilation covariance [Axiom]

\[
\boxed{
h_x(aY)=h_{a^2x}(Y)
}
\]

for every \(a>0\).

This matches the intrinsic scaling \(q(aY)=a^2q(Y)\).

### A4. Nontrivial damping [Axiom]

For \(Y\ne0\), \(0<h_x(Y)<1\) for \(x>0\).

These axioms define the canonical class tested here. They are not claimed to exhaust all imaginable transforms of the shell measure.

---

## 3. Semigroup + cone covariance force the quadratic generator [D]

By A1 and continuity, for each fixed \(Y\),

\[
\boxed{
h_x(Y)=e^{-x\lambda(Y)}
}
\]

for some \(\lambda(Y)\ge0\).

A2 gives

\[
\lambda(-Y)=\lambda(Y).
\]

A3 gives

\[
e^{-x\lambda(aY)}
=
e^{-a^2x\lambda(Y)},
\]

hence

\[
\boxed{
\lambda(aY)=a^2\lambda(Y).
}
\]

For \(Y>0\), set \(a=Y\) and evaluate at \(1\):

\[
\lambda(Y)=Y^2\lambda(1).
\]

By evenness,

\[
\boxed{
\lambda(Y)=cY^2,
\qquad
c:=\lambda(1)>0.
}
\]

Therefore the only evolution in the canonical class is

\[
\boxed{
h_x(Y)=e^{-cxY^2}.
}
\]

This already proves:

\[
\boxed{
\text{semigroup + root symmetry + degree-2 cone dilation}
\Longrightarrow
\text{Gaussian family, unique up to a positive time normalization }c.
}
\]

No zeta function, explicit formula, or RH assumption enters.

---

## 4. Sampling the arithmetic fixed lattice [D]

Restrict to \(Y=m\in\mathbb Z\). The trace is

\[
\boxed{
\Theta_c(x)
=
\sum_{m\in\mathbb Z}e^{-cxm^2}.
}
\]

This is the only fixed-locus trace arising from A1–A4, up to \(c>0\).

For \(c=\pi\),

\[
\Theta_\pi(x)
=
\sum_{m\in\mathbb Z}e^{-\pi xm^2}
=
\vartheta(x),
\]

the exact theta trace used in v13.717, v13.917, and v13.919.

---

## 5. Poisson duality fixes the normalization \(c=\pi\) [D]

Use the Fourier convention

\[
\widehat f(\xi)
=
\int_{\mathbb R}f(Y)e^{-2\pi iY\xi}\,dY.
\]

For

\[
f_{c,x}(Y)=e^{-cxY^2},
\]

the Gaussian transform is

\[
\boxed{
\widehat f_{c,x}(\xi)
=
\sqrt{\frac{\pi}{cx}}\,
e^{-\pi^2\xi^2/(cx)}.
}
\]

Poisson summation therefore gives

\[
\boxed{
\Theta_c(x)
=
\sqrt{\frac{\pi}{cx}}\,
\Theta_c\!\left(\frac{\pi^2}{c^2x}\right).
}
\]

Now impose the exact Jacobi self-duality required by the completed fixed-locus construction:

\[
\boxed{
\Theta_c(x)=x^{-1/2}\Theta_c(1/x)
\qquad(x>0).
}
\]

As \(x\to\infty\),

\[
\Theta_c(x)\to1.
\]

Poisson summation gives the small-\(t\) asymptotic

\[
\Theta_c(t)
\sim
\sqrt{\frac{\pi}{ct}}
\qquad(t\downarrow0).
\]

Hence exact self-duality implies

\[
1
=
\lim_{x\to\infty}x^{-1/2}\Theta_c(1/x)
=
\sqrt{\frac{\pi}{c}}.
\]

Therefore

\[
\boxed{
c=\pi.
}
\]

Thus

\[
\boxed{
h_x(Y)=e^{-\pi xY^2}
}
\]

is uniquely selected inside the canonical class.

Equivalently, the arithmetic trace is forced to be

\[
\boxed{
\Theta(x)
=
\sum_{m\in\mathbb Z}e^{-\pi xm^2},
\qquad
\Theta(x)=x^{-1/2}\Theta(1/x).
}
\]

---

## 6. Selection theorem [D]

### Cone Fixed-Locus Gaussian Selection Theorem

Let \(h_x(Y)\) be a continuous positive nontrivial scalar evolution on the continuous factor-exchange fixed locus of the AM–GM cone. Suppose:

1. \(h_{x+y}=h_xh_y\) and \(h_0=1\);
2. \(h_x(-Y)=h_x(Y)\);
3. \(h_x(aY)=h_{a^2x}(Y)\);
4. the integer-lattice trace obeys exact Poisson/Jacobi self-duality
   \[
   \Theta(x)=x^{-1/2}\Theta(1/x).
   \]

Then necessarily

\[
\boxed{
h_x(Y)=e^{-\pi xY^2}
}
\]

and

\[
\boxed{
\Theta(x)=\sum_{m\in\mathbb Z}e^{-\pi xm^2}.
}
\]

So, within this natural autonomous/dilation-covariant/self-dual class, the cone does not merely permit the Gaussian theta kernel:

\[
\boxed{
\textbf{it selects it uniquely.}
}
\]

---

## 7. Why every hypothesis matters [D/G]

### 7.1 Self-duality alone does NOT select the Gaussian

For any \(a>0\), define

\[
g_a(Y)
=
e^{-\pi aY^2}
+
a^{-1/2}e^{-\pi Y^2/a}.
\]

Using the Gaussian Fourier transform,

\[
\widehat g_a=g_a.
\]

It is positive and even. For \(a\ne1\), it is not a single Gaussian.

Therefore:

\[
\boxed{
\text{positive + even + Fourier self-dual}
\not\Rightarrow
\text{Gaussian}.
}
\]

The semigroup and scaling axioms are load-bearing.

### 7.2 Semigroup without degree-2 cone scaling does NOT select Brownian/Gaussian evolution

Other stable convolution semigroups have characteristic multipliers of the form

\[
e^{-ct|\xi|^\alpha},
\qquad
0<\alpha\le2.
\]

Their dilation exponent is \(\alpha\), not \(2\).

The cone's fixed-locus invariant has degree exactly \(2\), so A3 selects the \(\alpha=2\) member.

### 7.3 Cone scaling without exact self-duality leaves one free constant

A1–A3 give

\[
h_x(Y)=e^{-cxY^2}
\]

with arbitrary \(c>0\).

Thus \(c=\pi\) is not fixed by the cone quadratic form alone. It is fixed by requiring the arithmetic lattice and its dual to close under the exact Jacobi involution \(x\leftrightarrow1/x\).

This is a normalization selection, not an RH statement.

---

## 8. D12 / character channel [D/I]

For a primitive character of conductor \(q\), use the conductor-normalized fixed coordinate

\[
Y_q=\frac{m}{\sqrt q}.
\]

The selected Gaussian becomes

\[
e^{-\pi xY_q^2}
=
e^{-\pi m^2x/q}.
\]

Therefore the twisted fixed-locus trace is

\[
\boxed{
\Theta_\chi(x)
=
\sum_{m\in\mathbb Z}
\chi(m)e^{-\pi m^2x/q}.
}
\]

The geometric evolution is unchanged; the character changes only the channel weights.

For \(\chi_{12}\),

\[
\Theta_{\chi_{12}}
=
\Theta_1-\Theta_5-\Theta_7+\Theta_{11},
\]

and the primitive even character has root number \(+1\), giving the self-dual relation already used in v13.748/v13.917.

This sharpens the two-axis picture:

\[
\boxed{
\text{cone quadratic geometry selects the Gaussian evolution;}
}
\]

\[
\boxed{
\text{character/orientation data select which }L\text{-channel is traced.}
}
\]

---

## 9. Relation to the zero ordinates [D/I]

v13.917 showed

\[
\Xi(w)
=
\int_{\mathbb R}\Phi(\tau)e^{w\tau}\,d\tau,
\]

where \(\Phi\) is obtained from the theta current by the shifted Casimir.

The present theorem pushes the provenance one step upstream:

\[
\boxed{
\text{fixed-locus quadratic cone geometry}
\Rightarrow
\text{unique Gaussian heat family}
\Rightarrow
\text{Jacobi theta current}
\Rightarrow
\text{Mellin completion}
\Rightarrow
\Xi
\Rightarrow
\text{zero resonances}.
}
\]

Thus the Gaussian entering the zero-ordinate construction is no longer an arbitrary compatible transform inside the stated canonical class.

---

## 10. What this closes and what remains open

### Closed [D]

The v13.919 uniqueness question is closed **within the explicit canonical class A1–A4 plus exact Jacobi self-duality**:

\[
\boxed{
\text{Gaussian/self-dual heat evolution is unique.}
}
\]

The exponent \(2\) is fixed by the cone's quadratic scaling, and the coefficient \(\pi\) is fixed by exact lattice Fourier/Poisson self-duality.

### Guardrail [G]

This is a conditional **selection theorem**, not a theorem that every conceivable transform of the cone shell measure must be Gaussian.

The remaining philosophical/geometric question is now localized to the axioms themselves:

\[
\boxed{
\text{Why must the relevant cone dynamics be an autonomous positive scalar semigroup?}
}
\]

If autonomous local heat evolution on the fixed locus is accepted as the correct dynamical class, the Gaussian selection problem is finished.

### Still open [O]

1. Derive the semigroup/autonomy axiom from a deeper cone dynamical principle rather than impose it as the admissible class.
2. No Hilbert–Pólya point-spectrum operator is constructed.
3. No RH/GRH consequence: positivity and self-duality of theta do not force all zeros onto the balanced slice.
4. Quantization of the zero resonances remains separate.

---

## 11. Result

The handoff G5 question is now substantially narrowed.

Previously:

\[
\text{Why does the cone use the Gaussian theta transform?}
\]

Now:

\[
\boxed{
\text{Once one requires autonomous positive evolution, root symmetry, cone degree-2 dilation covariance, and exact Poisson self-duality, there is no freedom left:}
}
\]

\[
\boxed{
h_x(Y)=e^{-\pi xY^2}.
}
\]

So the unresolved geometric selector is no longer the Gaussian itself. It is the single structural question of **why autonomous heat-semigroup evolution is the correct admissible dynamics on the cone fixed locus**.
