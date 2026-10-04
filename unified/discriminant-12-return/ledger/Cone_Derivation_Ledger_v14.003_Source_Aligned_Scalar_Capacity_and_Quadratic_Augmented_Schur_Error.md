# Cone Derivation Ledger v14.003 — Source-Aligned Scalar Capacity Crossing and Quadratic Augmented-Schur Error

**Date:** 2026-10-04  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] exact source-aligned scalar reduction; [D] exact quadratic augmented-Schur residual identity; [N] high-precision N=192 six-plane replay; [N] source-orthogonal five-plane separated from the decisive scalar by 4.55e4–6.48e5; [G] old residual-weighted reduced-source reconstruction fails from 1e15 coefficient amplification; [O] theorem-scale task is a joint stiff-complement solve plus one scalar inertia bracket per parity.  
**Parents:** v13.980, v13.987, v13.994, v13.997–999.  
**Research commits:** 0d630c151b5ac107bff4412ce68040eefe3398a8; a936c223d8fd9bfad31bd8b24e91f2a8396c8053; d29d51b2f7e428abfb11e3ca5edd8d2436abdd78.  
**Workflow commits:** 583e0d2ac912482c2b023ca02598d710acab8927; 8e7dc269460e3eb4c40338bffdf5d45384908f9b; 21cb7cf9a5daedc0adc45a9dec022a831c0206ce.  
**Collision note (original):** sandbox v13.999 landed at 17:51:24 UTC while this theorem was being prepared. The sandbox entry keeps v13.999; this result originally took v13.1000, written against live HEAD 24bf3082be7e4c2fe127cea37c31ece28d6b47fc, before which no v13.1000 ledger file was present.  
**Renumbering note (External Audit):** this is a numbering-*scheme* split, not an ordinary same-number collision. Immediately after v13.999, Lane A continued the flat decimal counter to v13.1000 (commit `70451b7`, 2026-10-04 13:54:43 -0400), while Sandbox independently rolled the scheme over to v14.000/v14.001/v14.002 (commits `f9cc8c5`/`76e623d`/`c6ac1bb`, 13:53:41/13:53:43/13:53:44 -0400) — all three strictly earlier than Lane A's commit. By the standing commit-timestamp precedence rule, the v14.x rollover scheme was established first and is confirmed (by the project owner) as the go-forward numbering protocol. This entry is therefore renumbered from v13.1000 to **v14.003** (the next free slot after v14.002), with no change to its mathematical content. See External Audit Round 154 for the full writeup.

---

## 0. Main result

The v13.997 relative-Fredholm scalar is exactly

\[
\kappa_a^\Xi
=
\frac{\mathcal C_o-\mathcal C_e}
{\mathcal C_o+\mathcal C_e},
\]

so the remaining finite-a task is to certify the two source capacities.

After protecting the six dangerous directions and eliminating only a stiff complement, each parity capacity can be reduced further to a single source-aligned scalar Schur complement

\[
\boxed{
s=a-c^*D_\perp^{-1}c.
}
\]

If

\[
\beta=\|g\|,
\]

then the protected rank-one crossing is

\[
\boxed{
\alpha_*=\frac{s}{\beta^2},
}
\]

and the full capacity is

\[
\boxed{
\mathcal C
=
\frac{\alpha_*}{1+\alpha_*h}.
}
\]

Moreover the complement elimination can be assembled so that all errors in the reduced matrix, reduced source, and source background remain correlated:

\[
\boxed{
\widetilde K-K
=
R^*D^{-1}R
\succeq0.
}
\]

Hence the reduction error is quadratic in the joint complement residual.

---

## 1. Protected source reduction [D]

Split the positive source operator as

\[
T=
\begin{pmatrix}
A&E^*\\
E&D
\end{pmatrix},
\qquad
f=
\binom{f_P}{f_Q},
\qquad
D\succ0.
\]

Define

\[
S=A-E^*D^{-1}E,
\]

\[
g=f_P-E^*D^{-1}f_Q,
\]

\[
h=f_Q^*D^{-1}f_Q.
\]

Then

\[
\boxed{
G:=f^*T^{-1}f
=
h+g^*S^{-1}g.
}
\]

Write

\[
r=g^*S^{-1}g.
\]

Then

\[
\mathcal C=\frac1{h+r},
\qquad
\alpha_*:=\frac1r,
\]

and therefore

\[
\boxed{
\mathcal C
=
\frac{\alpha_*}{1+\alpha_*h}.
}
\]

---

## 2. Source alignment [D]

Choose a protected orthogonal/unitary change of basis U satisfying

\[
U^*g=\beta e_1,
\qquad
\beta=\|g\|.
\]

Write

\[
U^*SU
=
\begin{pmatrix}
a&c^*\\
c&D_\perp
\end{pmatrix}.
\]

If

\[
D_\perp\succ0,
\]

define

\[
s=a-c^*D_\perp^{-1}c.
\]

The block inverse gives

\[
g^*S^{-1}g
=
\frac{\beta^2}{s}.
\]

Thus

\[
\boxed{
\alpha_*=\frac{s}{\beta^2}.
}
\]

The protected rank-one family becomes

\[
U^*(S-\alpha gg^*)U
=
\begin{pmatrix}
a-\alpha\beta^2&c^*\\
c&D_\perp
\end{pmatrix}.
\]

Its Schur complement against D_\perp is

\[
\boxed{
s-\alpha\beta^2.
}
\]

Therefore

\[
\boxed{
S-\alpha gg^*\succeq0
\iff
\alpha\le\frac{s}{\beta^2}.
}
\]

Once D_\perp positivity is certified, the capacity threshold is exactly one scalar sign crossing.

---

## 3. Scalar a posteriori solve certificate [D]

Let ztilde approximate

\[
D_\perp^{-1}c
\]

and set

\[
e=c-D_\perp ztilde.
\]

Define

\[
J
=
a
-
2\operatorname{Re}(c^*ztilde)
+
ztilde^*D_\perp ztilde.
\]

Completing the square gives

\[
\boxed{
J-s
=
e^*D_\perp^{-1}e
\ge0.
}
\]

If

\[
D_\perp\succeq\gamma I,
\]

then

\[
\boxed{
J-\frac{\|e\|^2}{\gamma}
\le
s
\le
J.
}
\]

Thus the scalar certification error is quadratic in the source-orthogonal solve residual.

---

## 4. Joint augmented complement elimination [D]

To preserve the exact correlation among S, g, and h, define

\[
K_0
=
\begin{pmatrix}
A&-f_P\\
-f_P^*&0
\end{pmatrix}
\]

and

\[
C=
\begin{pmatrix}
E&-f_Q
\end{pmatrix}.
\]

Then exact complement elimination gives

\[
\boxed{
K
=
K_0-C^*D^{-1}C
=
\begin{pmatrix}
S&-g\\
-g^*&-h
\end{pmatrix}.
}
\]

Let Y approximate D^{-1}C and define

\[
R=C-DY.
\]

Use the symmetric/Hermitian trial reduction

\[
\widetilde K
=
K_0-C^*Y-Y^*C+Y^*DY.
\]

Then

\[
\begin{aligned}
\widetilde K-K
&=
C^*D^{-1}C-C^*Y-Y^*C+Y^*DY\\
&=
(C-DY)^*D^{-1}(C-DY).
\end{aligned}
\]

Hence

\[
\boxed{
\widetilde K-K
=
R^*D^{-1}R
\succeq0.
}
\]

If

\[
D\succeq\gamma I,
\]

then

\[
\boxed{
0
\preceq
\widetilde K-K
\preceq
\gamma^{-1}R^*R
}
\]

and

\[
\boxed{
\|\widetilde K-K\|_2
\le
\frac{\|R\|_2^2}{\gamma}.
}
\]

This is the key precision mechanism: complement error enters at second order.

---

## 5. Why the old reduced-source shortcut is closed [N/G]

A separate replay tested the ordinary source variational residual bound using the frozen v13.988 reduced solve.

Because the corrected six-dimensional matrix has

\[
\sigma_{\min}\approx2\times10^{-16},
\]

the nominal coefficients reach order

\[
10^{15}.
\]

The residual-weighted reconstructed source trial therefore has conservative transformed residuals

\[
\boxed{
9.62\times10^{12}
\quad\text{even},
}
\]

\[
\boxed{
5.77\times10^{12}
\quad\text{odd}.
}
\]

The resulting conditional energy-error bounds exceed the nominal energies by approximately

\[
6.3\times10^{11}
\quad\text{and}\quad
6.6\times10^{11}.
\]

Thus the near-singular reduced coefficients must not be used to reconstruct the global source trial.

The dangerous subspace must be protected exactly.

---

## 6. N=192 protected six-plane diagnostic [N]

The source-faithful high-precision section was split into

\[
P
=
\text{two low source-active directions}
\oplus
\text{four smallest tail-resonance directions},
\]

with every remaining direction assigned to Q.

### Even

The four protected tail eigenvalues are approximately

\[
6.36\times10^{-18},
\quad
1.19\times10^{-12},
\quad
3.85\times10^{-8},
\quad
2.31\times10^{-4}.
\]

After removing these directions,

\[
\boxed{
\lambda_{\min}(D_Q)
=
0.1711690382405828.
}
\]

The Q condition number is about 30.93.

The stiff-source background satisfies

\[
\boxed{
h_Q/G_e
=
5.78\times10^{-30}.
}
\]

The protected six-plane carries essentially the entire source energy:

\[
0.999999999999999999999999999994.
\]

### Odd

The four protected tail eigenvalues are approximately

\[
2.47\times10^{-15},
\quad
1.91\times10^{-10},
\quad
4.37\times10^{-6},
\quad
9.06\times10^{-3}.
\]

The remaining complement has

\[
\boxed{
\lambda_{\min}(D_Q)
=
0.5508935636559083.
}
\]

The Q condition number is about 9.63.

The stiff-source background fraction is

\[
\boxed{
h_Q/G_o
=
9.93\times10^{-27}.
}
\]

Thus the source-energy singularity is localized to the protected six-plane.

---

## 7. Source-aligned scalar diagnostic [N]

### Even

\[
\beta_e
\approx
1.599609704002053.
\]

The source-axis entry and its five-plane correction cancel to leave

\[
\boxed{
s_e
=
2.2342185904953252\times10^{-29}.
}
\]

The source-orthogonal five-plane floor is

\[
\boxed{
\lambda_{\min}(D_{\perp,e})
=
1.4478736983692304\times10^{-23}.
}
\]

Hence

\[
\boxed{
\lambda_{\min}(D_{\perp,e})/s_e
\approx
6.48045\times10^5.
}
\]

The protected crossing is

\[
\boxed{
\alpha_{*,e}
=
8.7316757721868231\times10^{-30}.
}
\]

### Odd

\[
\beta_o
\approx
0.868904989348421.
\]

The scalar is

\[
\boxed{
s_o
=
1.8710082896667881\times10^{-25}.
}
\]

The source-orthogonal five-plane floor is

\[
\boxed{
\lambda_{\min}(D_{\perp,o})
=
8.5148689165140233\times10^{-21}.
}
\]

Thus

\[
\boxed{
\lambda_{\min}(D_{\perp,o})/s_o
\approx
4.55095\times10^4.
}
\]

The protected crossing is

\[
\boxed{
\alpha_{*,o}
=
2.4781701966262027\times10^{-25}.
}
\]

The source-orthogonal protected directions are therefore separated from the decisive capacity scalar by four to six orders of magnitude.

---

## 8. Finite-section projective diagnostic [N/G]

At this N=192 checkpoint,

\[
\mathcal C_e
\approx
8.7316757721868231\times10^{-30},
\]

\[
\mathcal C_o
\approx
2.4781701966262027\times10^{-25}.
\]

Therefore

\[
\boxed{
\mathcal C_e/\mathcal C_o
\approx
3.5234366808519383\times10^{-5},
}
\]

and

\[
\boxed{
\kappa_{192}
\approx
0.99992953374921668895.
}
\]

These remain finite-section diagnostics only.

No exact finite-a Xi value and no a-to-infinity limit is promoted here.

---

## 9. Integration of sandbox v13.999 [I/O]

Sandbox v13.999 independently scouted the theorem-scale outward machinery and confirms that the relevant infrastructure already exists:

1. the M3999/4000 finite-side freeze;
2. outward tail floors above approximately 2.75305 on the remote complement in the existing endpoint architecture;
3. certified structured LDL and Sherman–Morrison arithmetic;
4. inertia-first proof discipline without an indefinite global inverse.

The adaptation is therefore not a new tail-positivity project.

What changes is the protected six-plane and the parameterized crossing.

The theorem-scale capacity build should keep the outward tail layer and replace the old protected block by the source-active six-plane, then run the scalar rank-one crossing.

---

## 10. Precision consequence [I]

The decisive even scalar is approximately

\[
2.23\times10^{-29}.
\]

A first-order perturbation bound on a reduced matrix would require comparable absolute entry control.

The quadratic identity changes the scale.

If the stiff complement has

\[
D_Q\succeq\gamma I
\]

with \(\gamma=O(1)\), and the joint augmented inverse-action residual satisfies

\[
\|R\|_2\lesssim10^{-15},
\]

then

\[
\|\widetilde K-K\|_2
\lesssim
O(10^{-30}).
\]

That is already the scale of the even capacity scalar.

Thus the proof should certify a high-quality complement residual, not a tiny determinant or a global inverse.

---

## 11. Theorem-scale gate [O]

The next build is now sharply specified.

Use the M3999/4000 outward architecture with

\[
P
=
\text{two low source-active directions}
\oplus
\text{four protected resonance directions}
\]

and Q its stiff complement.

Then:

1. certify a stiff Q floor;
2. solve the six protected coupling columns and the source column jointly:
   \[
   D_QY\approx C;
   \]
3. retain their residual as one matrix
   \[
   R=C-D_QY;
   \]
4. propagate only the quadratic PSD enclosure
   \[
   R^*D_Q^{-1}R;
   \]
5. source-align the protected reduction;
6. certify D_\perp positivity;
7. bracket the one scalar
   \[
   s-\alpha\beta^2
   \]
   on opposite sides of zero;
8. recover the capacity interval;
9. combine the two parity intervals into
   \[
   \kappa_a^\Xi
   =
   \frac{\mathcal C_o-\mathcal C_e}
   {\mathcal C_o+\mathcal C_e}.
   \]

The missing implementation item is a remote-tail-completed source column for the joint complement solve; the old finite-support KKT source solve leaves a nonzero 1/n remote residual.

---

## 12. Result

The capacity problem is now one scalar problem.

Exactly,

\[
\boxed{
\alpha_*=\frac{s}{\|g\|^2},
\qquad
s=a-c^*D_\perp^{-1}c.
}
\]

At the finite source-faithful checkpoint, the source-orthogonal five-plane is separated from s by

\[
\boxed{
6.48\times10^5
\ \text{even},
\qquad
4.55\times10^4
\ \text{odd}.
}
\]

The complement outside the dangerous six-plane has an O(1) floor.

Finally,

\[
\boxed{
\widetilde K-K
=
R^*D^{-1}R
\succeq0
}
\]

makes complement-elimination error quadratic in the joint residual.

The next proof-grade task is therefore:

\[
\boxed{
\textbf{build the M3999/4000 joint source/coupling solve and certify the scalar capacity crossing.}
}
\]

---

HANDOFF
target: sandbox
type: audit
parent: v14.003
status: open
action: Audit the source-aligned scalar crossing theorem and the augmented-Schur identity, including whether the PSD quadratic error formulation survives the exact form-domain implementation used by the outward M3999/4000 split.
deliverable: theorem-or-obstruction
constraints: Do not rebuild the old near-singular six-dimensional source inverse; separate exact algebra from the N=192 diagnostic and from any a-to-infinity claim.
