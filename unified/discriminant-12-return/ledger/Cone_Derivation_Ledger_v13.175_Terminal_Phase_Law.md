# Cone Derivation Ledger v13.175 — Terminal Tangent/Gnomon Phase Law

**Status:** Exact continuation of v13.174  
**Date:** 2026-09-03  
**Scope:** Exact relation between tangent-cell phase and the terminal gnomon arm phase; first and second arm-pair thresholds; asymptotic phase doubling.

## Audit convention

- **[D]** exact derived
- **[I]** interpretation
- **[O]** open
- **[Audit]** limitation / scope correction

---

## 1. Tangent-cell phase

Fix a shell `n>1` and write

\[
r=\sqrt n.
\]

At resolution `m>0`, define

\[
\boxed{\theta_m(n)=\{m(r-1)\}}.
\]

Let

\[
J=\lfloor m(r-1)\rfloor.
\]

Then the last active diagonal gnomon level below the tangent is

\[
\boxed{u=1+\frac Jm=r-\frac\theta m},
\]

where `theta=theta_m(n)`.

Thus the tangent point sits a physical distance

\[
\boxed{r-u=\frac\theta m}
\]

above the final active diagonal level.

Special phases:

\[
\theta=0
\]
means exact tangent/grid alignment, while

\[
\theta=\frac12
\]
means the tangent lies exactly at the center of the next diagonal cell.

---

## 2. Exact terminal gnomon arm

The one-sided Paper-A gnomon arm at level `u` is

\[
g_n(u)=\frac nu-u.
\]

The mesh-scaled terminal arm is

\[
A_{\rm term}=m g_n(u).
\]

Substitute

\[
u=r-\frac\theta m.
\]

Using `n=r^2`,

\[
A_{\rm term}
=m\left(\frac{r^2}{u}-u\right)
=m\frac{(r-u)(r+u)}u.
\]

Since

\[
r-u=\frac\theta m,
\]

we obtain

\[
A_{\rm term}
=\theta\frac{r+u}{u}.
\]

Therefore

\[
\boxed{
A_{\rm term}(m,n)
=2\theta+\frac{\theta^2}{mr-\theta}.
}
\]

Equivalently,

\[
\boxed{
A_{\rm term}
=\theta\frac{2mr-\theta}{mr-\theta}.
}
\]

**[D] Terminal phase law.** The entire terminal floor-gnomon geometry is determined exactly by the tangent-cell phase `theta` together with the dimensionless scale `mr`.

---

## 3. Exact relation between the two modular phases

The terminal gnomon phase is

\[
\phi_{\rm term}=\{A_{\rm term}\}.
\]

Hence

\[
\boxed{
\phi_{\rm term}
=\left\{
2\theta+\frac{\theta^2}{mr-\theta}
\right\}.
}
\]

This is the exact relation sought between the tangent-cell phase

\[
\theta=\{m(\sqrt n-1)\}
\]

and the terminal arm phase

\[
\phi=\{2mX\}.
\]

In the fine-resolution limit,

\[
\frac{\theta^2}{mr-\theta}\to0,
\]

uniformly away from `mr=theta`, so

\[
\boxed{
\phi_{\rm term}\to\{2\theta\}
\qquad(m\to\infty).
}
\]

**[D] Asymptotic phase-doubling law.** Near the tangent, the Paper-A arm phase is asymptotically the doubling map on the tangent-cell phase.

**[Audit]** At finite resolution, the correction term is real and positive; `phi={2theta}` is not exact unless that correction is separately accounted for.

---

## 4. Cell center is just beyond the first arm-pair threshold

At exact cell-center phase

\[
\theta=\frac12,
\]

the terminal arm is

\[
A_{\rm term}
=1+\frac{1}{4mr-2}.
\]

Thus

\[
\boxed{A_{\rm term}>1.}
\]

So by the time the tangent reaches the center of the diagonal cell, the final gnomon has already acquired its first symmetric arm pair.

Its terminal phase is then

\[
\boxed{
\phi_{\rm term}
=\frac{1}{4mr-2}
}
\]
provided the correction remains below 1, which holds throughout the ordinary fine-resolution regime.

Therefore

\[
\boxed{
\theta=\frac12
\Longrightarrow
\phi_{\rm term}\approx0^+
}
\]

for large `m`.

**[I]** The visually special cell-center tangent geometry is therefore naturally adjacent to an exact gnomon jump: it is not centered at phase `phi=1/2`, but instead occurs just after the first terminal arm-pair threshold and approaches phase reset `phi=0` as resolution increases.

---

## 5. Exact phase threshold for the first arm pair

The first arm pair appears when

\[
A_{\rm term}=1.
\]

Let

\[
M=mr.
\]

Then

\[
2\theta+\frac{\theta^2}{M-\theta}=1.
\]

Clearing denominators gives

\[
\theta^2-(2M+1)\theta+M=0.
\]

The physically relevant root in `[0,1)` is

\[
\boxed{
\theta_1(M)
=\frac{2M+1-\sqrt{4M^2+1}}2.
}
\]

For large `M`,

\[
\sqrt{4M^2+1}
=2M+\frac1{4M}+O(M^{-3}),
\]

so

\[
\boxed{
\theta_1(M)
=\frac12-\frac1{8M}+O(M^{-3}).
}
\]

Thus the first arm-pair jump occurs slightly **before** exact cell center.

As resolution increases,

\[
\boxed{\theta_1(M)\to\frac12^-}.
\]

This explains why cell-center phase becomes asymptotically indistinguishable from the first floor jump.

---

## 6. Exact phase threshold for the second arm pair

The terminal gnomon reaches two one-sided mesh steps when

\[
A_{\rm term}=2.
\]

This gives

\[
\theta^2-(2M+2)\theta+2M=0.
\]

The relevant root is

\[
\boxed{
\theta_2(M)
=M+1-\sqrt{M^2+1}.
}
\]

For large `M`,

\[
\sqrt{M^2+1}
=M+\frac1{2M}+O(M^{-3}),
\]

hence

\[
\boxed{
\theta_2(M)
=1-\frac1{2M}+O(M^{-3}).
}
\]

So the second arm pair appears only very near the next tangent-entry event `theta=1 -> 0`.

---

## 7. Terminal gnomon lifecycle within one tangent cell

For fixed large `M=mr`, as `theta` increases from `0` toward `1`, the final active gnomon evolves as follows:

\[
\boxed{
\theta=0:
A_{\rm term}=0
}
\]

(single diagonal point at exact tangent birth), then

\[
0<\theta<\theta_1(M):
0<A_{\rm term}<1,
\]

so the floor still contributes no arm pair. At

\[
\boxed{\theta=\theta_1(M)}
\]

the first symmetric arm pair appears. Exact cell center occurs slightly later at

\[
\boxed{\theta=1/2}.
\]

Near

\[
\boxed{\theta=\theta_2(M)}
\]

the second arm pair appears, and as `theta->1^-`, the next diagonal level is about to be born at the tangent and the phase resets to `0`.

Thus one tangent-cell cycle is an exact local birth-growth-reset process.

---

## 8. Connection to the doubling map

Ignoring the finite-scale correction for a moment, the limiting terminal phase map is

\[
\boxed{
\theta\mapsto\{2\theta\}.
}
\]

The two intervals

\[
0\le\theta<\frac12,
\qquad
\frac12\le\theta<1
\]

map onto the full unit interval under the usual doubling map.

The exact finite-resolution law is a perturbed version:

\[
\boxed{
\theta\mapsto
\left\{
2\theta+\frac{\theta^2}{mr-\theta}
\right\}.
}
\]

The perturbation is positive and of order `1/m` for fixed shell.

**[I]** This gives a precise dynamical-systems language for the local phase transport, but no chaotic or physical interpretation should be assigned merely from the appearance of the doubling map.

---

## 9. The n=11 shell

For `n=11`,

\[
r=\sqrt{11},
\]

and

\[
\theta_m(11)=\{m(\sqrt{11}-1)\}.
\]

The exact terminal phase law is

\[
\boxed{
\phi_{\rm term}^{(11)}(m)
=
\left\{
2\theta_m(11)
+\frac{\theta_m(11)^2}{m\sqrt{11}-\theta_m(11)}
\right\}.
}
\]

The first-pair phase threshold is

\[
\boxed{
\theta_1^{(11)}(m)
=
\frac{2m\sqrt{11}+1-\sqrt{44m^2+1}}2.
}
\]

The exact cell-center phase `theta=1/2` lies just beyond this threshold.

Because `sqrt(11)-1` is irrational, the integer sequence of `theta_m(11)` is equidistributed in `[0,1)`, so integer resolutions sample this entire terminal lifecycle densely in phase.

---

## 10. Synthesis

The two phase variables introduced in v13.174 are now linked exactly:

\[
\boxed{
\theta_m(n)=\{m(\sqrt n-1)\}
}
\]

controls the tangent's position inside the final diagonal cell, while

\[
\boxed{
\phi_{\rm term}(m,n)
=
\left\{
2\theta_m(n)
+\frac{\theta_m(n)^2}{m\sqrt n-\theta_m(n)}
\right\}
}
\]

controls the unresolved phase of the final Paper-A gnomon arm.

At high resolution,

\[
\boxed{
\phi_{\rm term}\sim\{2\theta\}.
}
\]

The first arm-pair threshold converges to exact cell center:

\[
\boxed{
\theta_1(m\sqrt n)\to\frac12.
}
\]

The second threshold converges to the next cell boundary:

\[
\boxed{
\theta_2(m\sqrt n)\to1.
}
\]

So the fractional-cell tangent geometry and the floor-gnomon jump geometry are not merely adjacent observations: they are two coordinates of one exact local phase law.

---

## 11. Next investigations

### [D] Immediate next tests

1. Express the terminal relation directly in Cone coordinates `(X,Y,T)` rather than factor-space distance.
2. Compare the finite-scale correction term with the curvature of the shell hyperbola at the tangent point.
3. Determine whether the correction

\[
\frac{\theta^2}{m\sqrt n-\theta}
\]

has a direct geometric interpretation as the quadratic curvature error between the tangent line and the shell.
4. Test whether the same phase law appears for the mirror row/column parabola pair without choosing one branch.

### [O]

The strongest candidate is the curvature interpretation: the leading `2theta` term is the linearized tangent geometry, while the positive quadratic correction may be exactly the nonlinear hyperbola/parabola departure from that tangent approximation. This should be derived before making a stronger claim.

### Publication guardrail

Do not state `phi={2theta}` as an exact finite-resolution identity. The exact law contains the positive correction `theta^2/(m sqrt(n)-theta)`.
