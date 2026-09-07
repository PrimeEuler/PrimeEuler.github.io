# Cone Derivation Ledger v13.283 — D12 Fredholm Reflection Reduction and Canonical Deficiency Normalization

Date: 2026-09-07

Status: EXACT SECTION-8 REDUCTION + CANONICAL PHASE FIXING + ONE-EQUATION D12 FREDHOLM SYSTEM — GRH NOT PROVED

## 0. Synchronization and source state

Immediately before this write, the authoritative project README and current `master` tip were re-fetched. The tip was

`d1002b93191f90637c327622c5e2a4e36215966e`,

with `v13.282` the highest checkpoint and no newer external-audit entry present.

For Suzuki-source statements this checkpoint uses the current arXiv v2 HTML for Masatoshi Suzuki, “Weil's quadratic form via the screw function,” arXiv:2606.09096v2. In Section 8.3 Suzuki writes the continuous-kernel Fredholm equation

\[
\int_{-a}^{a}k(x,y)(-v_{\pm}(y))\,dy
=
C_{\pm}e^{\pm x}+A_{\pm}x+B_{\pm},
\]

with

\[
A_{\pm}
=
\int_{-a}^{a}k_x(0,y)(-v_{\pm}(y))\,dy
\mp C_{\pm},
\]

\[
B_{\pm}
=
\int_{-a}^{a}k(0,y)(-v_{\pm}(y))\,dy
-C_{\pm}.
\]

Suzuki explicitly warns that this first-kind Fredholm equation is a formal twice-integrated version of the differentiated equation and is not literally the same operator equation as `S_a u_\pm=C_\pm \bar D e_{\pm i}`. That guardrail is retained below.

---

## 1. D12 kernel symmetry

For the D12 continuous-kernel system from v13.282, after absorbing the conductor into

\[
\mu=\lambda-\log 12,
\]

write

\[
k_K(x,y)
=
g_K^{\rm red}(x-y)-\mu N_a(x,y).
\]

The reduced screw kernel is even,

\[
g_K^{\rm red}(-t)=g_K^{\rm red}(t),
\]

and the Neumann kernel satisfies

\[
N_a(-x,-y)=N_a(x,y).
\]

Therefore

\[
\boxed{k_K(-x,-y)=k_K(x,y).}
\]

At `x=0` this implies

\[
\boxed{k_K(0,-y)=k_K(0,y)}
\]

and differentiating the simultaneous-reflection identity in `x` gives

\[
\boxed{k_{K,x}(0,-y)=-k_{K,x}(0,y).}
\]

Thus the zeroth-row kernel is even in `y`, while its `x`-derivative row is odd.

---

## 2. Reflection relation for the deficiency vectors

Let

\[
R f(x)=f(-x).
\]

The finite D12 operator commutes with `R`, hence so does

\[
T_{K,a}=A_{K,a}-\lambda I.
\]

Suppose

\[
T_{K,a}v_+=C_+e^x,
\qquad
T_{K,a}v_-=C_-e^{-x}.
\]

Since `RT_{K,a}=T_{K,a}R`,

\[
T_{K,a}(Rv_+)=C_+e^{-x}.
\]

Because the `-i` deficiency space is one-dimensional, there is a phase `\alpha_a` such that

\[
\boxed{v_-=e^{i\alpha_a}Rv_+.}
\]

Applying `T_{K,a}` gives at once

\[
\boxed{C_-=e^{i\alpha_a}C_+.}
\]

This recovers the phase-covariant statement of v13.279 in the Section-8 variables.

---

## 3. Exact reflection laws for the affine integration constants

Define

\[
I_+
:=
\int_{-a}^{a}k_{K,x}(0,y)(-v_+(y))\,dy,
\]

\[
J_+
:=
\int_{-a}^{a}k_K(0,y)(-v_+(y))\,dy.
\]

Then

\[
A_+=I_+-C_+,
\qquad
B_+=J_+-C_+.
\]

For the minus vector, use

\[
v_-(y)=e^{i\alpha_a}v_+(-y).
\]

Because `k_{K,x}(0,y)` is odd,

\[
\int k_{K,x}(0,y)(-v_-(y))\,dy
=
-e^{i\alpha_a}I_+.
\]

Hence

\[
A_-
=
-e^{i\alpha_a}I_+ + e^{i\alpha_a}C_+
=
-e^{i\alpha_a}(I_+-C_+),
\]

so

\[
\boxed{A_-=-e^{i\alpha_a}A_+.}
\]

Because `k_K(0,y)` is even,

\[
\int k_K(0,y)(-v_-(y))\,dy
=
e^{i\alpha_a}J_+.
\]

Therefore

\[
B_-
=
e^{i\alpha_a}(J_+-C_+),
\]

and

\[
\boxed{B_-=e^{i\alpha_a}B_+.}
\]

The complete affine data transform as

\[
\boxed{
(C_-,A_-,B_-)
=
e^{i\alpha_a}(C_+,-A_+,B_+).
}
\]

This is an exact consequence of reflection symmetry and Suzuki's own formulas for `A_\pm,B_\pm`.

---

## 4. The two Fredholm equations are one reflected equation

Write

\[
C:=C_+,
\qquad
A:=A_+,
\qquad
B:=B_+.
\]

The plus equation is

\[
\boxed{
\int_{-a}^{a}k_K(x,y)(-v_+(y))\,dy
=
Ce^x+Ax+B.
}
\]

Replacing `x` by `-x`, using simultaneous reflection of `k_K`, and multiplying by `e^{i\alpha_a}` gives exactly the minus equation

\[
\int_{-a}^{a}k_K(x,y)(-v_-(y))\,dy
=
C_-e^{-x}+A_-x+B_-.
\]

Therefore the finite D12 Section-8 deficiency problem contains only **one independent Fredholm equation**.

Once `v_+` is known,

\[
\boxed{v_-(x)=e^{i\alpha_a}v_+(-x)}
\]

and all minus-side affine constants follow automatically.

---

## 5. Canonical real deficiency basis removes the phase

The phase `\alpha_a` is a basis artifact if one begins with abstract normalized deficiency vectors. In the present D12 setting there is a canonical way to eliminate it.

Because `T_{K,a}` is real, self-adjoint and strictly positive after choosing `\lambda<\inf\sigma(A_{K,a})`, define the raw vectors

\[
q_+
:=
T_{K,a}^{-1}e^x,
\qquad
q_-
:=
T_{K,a}^{-1}e^{-x}.
\]

They are uniquely defined and real. Reflection gives

\[
q_-=Rq_+.
\]

Moreover reflection is unitary in the D12 energy space, hence

\[
\|q_-\|_{T_{K,a}}=
\|q_+\|_{T_{K,a}}.
\]

Therefore if Suzuki's deficiency vectors are normalized to equal unit norm, one may choose the **same positive scalar** `c_a` on both sides:

\[
v_+=c_a q_+,
\qquad
v_-=c_a q_-.
\]

Then

\[
\boxed{v_-=Rv_+}
\]

with no residual phase, and

\[
\boxed{C_+=C_-=c_a>0.}
\]

Thus, while v13.279 correctly warned that equal norm alone does not fix the phase abstractly, the D12 resolvent equations provide an additional canonical real structure that **does** fix it.

This is not a contradiction with v13.279: it is an extra normalization convention supplied by the explicit equations `T^{-1}e^{\pm x}`.

---

## 6. Scale-free canonical choice `C=1`

For computation it is even simpler to work with the raw vectors themselves:

\[
\boxed{q_+=T_{K,a}^{-1}e^x,\qquad q_-=Rq_+.}
\]

Then

\[
C_+=C_-=1.
\]

The single Fredholm equation becomes

\[
\boxed{
\int_{-a}^{a}k_K(x,y)(-q_+(y))\,dy
=
e^x+A_ax+B_a.
}
\]

where

\[
\boxed{
A_a
=
\int_{-a}^{a}k_{K,x}(0,y)(-q_+(y))\,dy-1,
}
\]

\[
\boxed{
B_a
=
\int_{-a}^{a}k_K(0,y)(-q_+(y))\,dy-1.
}
\]

The reflected solution is

\[
q_-(x)=q_+(-x),
\]

with affine data

\[
\boxed{A_-=-A_a,\qquad B_-=B_a.}
\]

Any later unit-energy normalization multiplies both deficiency vectors by the same scalar and therefore does not affect normalized characteristic-function ratios.

---

## 7. Even/odd decomposition of the one Fredholm equation

Write

\[
q_+=q_e+q_o,
\]

with

\[
q_e(x)=\frac{q_+(x)+q_+(-x)}2,
\qquad
q_o(x)=\frac{q_+(x)-q_+(-x)}2.
\]

Because the integral operator with kernel `k_K(x,y)` commutes with reflection, its even and odd sectors decouple.

Taking the even part of

\[
\int k_K(x,y)(-q_+(y))\,dy=e^x+A_ax+B_a
\]

gives

\[
\boxed{
\int_{-a}^{a}k_K(x,y)(-q_e(y))\,dy
=
\cosh x+B_a.
}
\]

Taking the odd part gives

\[
\boxed{
\int_{-a}^{a}k_K(x,y)(-q_o(y))\,dy
=
\sinh x+A_ax.
}
\]

Thus the single complex-looking deficiency problem becomes two **real parity-separated Fredholm equations**.

This is especially useful numerically:

- the even solve carries only the scalar nuisance parameter `B_a`;
- the odd solve carries only `A_a`;
- the two equations can be discretized independently;
- reflection symmetry is enforced exactly rather than approximately.

---

## 8. Endpoint conditions close the augmented numerical system

Because

\[
q_+=T_{K,a}^{-1}e^x
\]

lies in the operator domain of the Friedrichs realization, it lies in the form domain inherited from `H_0^1(-a,a)`. Hence its trace satisfies

\[
q_+(\pm a)=0.
\]

Consequently

\[
q_e(a)=q_e(-a)=0,
\qquad
q_o(a)=q_o(-a)=0.
\]

By parity these reduce to one endpoint condition for each sector:

\[
\boxed{q_e(a)=0,\qquad q_o(a)=0.}
\]

Therefore a natural augmented numerical formulation is:

### even sector
solve simultaneously for `q_e` and `B_a`:

\[
\int k_K(x,y)(-q_e(y))\,dy=\cosh x+B_a,
\qquad
q_e(a)=0;
\]

### odd sector
solve simultaneously for `q_o` and `A_a`:

\[
\int k_K(x,y)(-q_o(y))\,dy=\sinh x+A_ax,
\qquad
q_o(a)=0.
\]

Then

\[
q_+=q_e+q_o,
\qquad
q_-=q_e-q_o.
\]

This gives a concrete one-sided D12 implementation of Suzuki's Section-8 numerical suggestion.

Guardrail: because Suzuki's equation (8.5) is only formally obtained by integrating the differentiated equation twice, a rigorous numerical implementation should verify the recovered solution against the differentiated equation or the original operator equation, not rely on the first-kind equation alone.

---

## 9. Characteristic function in the canonical reflection basis

Define the raw Fourier transform

\[
F_a(z)
:=
\int_{-a}^{a}q_+(x)e^{izx}\,dx.
\]

Since `q_-=Rq_+`,

\[
\int_{-a}^{a}q_-(x)e^{izx}\,dx=F_a(-z).
\]

The raw characteristic family is therefore

\[
\boxed{
W^{\rm raw}_{K,a}(\theta;z)
=
(z-i)F_a(z)
+
e^{i\theta}(z+i)F_a(-z).
}
\]

If the normalized deficiency vectors are `v_\pm=c_a q_\pm`, then

\[
W_{K,a}(\theta;z)
=
c_a W^{\rm raw}_{K,a}(\theta;z).
\]

Hence for any reference point `z_*` away from zeros,

\[
\boxed{
\frac{W_{K,a}(\theta;z)}{W_{K,a}(\theta;z_*)}
=
\frac{W^{\rm raw}_{K,a}(\theta;z)}
{W^{\rm raw}_{K,a}(\theta;z_*)}.
}
\]

The unknown deficiency normalization cancels identically.

Thus the Section-8 computation can use the simple canonical equations with `C=1` and never separately compute the energy normalization `c_a` if the research target is a normalized characteristic-function limit.

---

## 10. D12 prime/conductor structure of the actual numerical kernel

Combining with v13.282, the kernel entering the two parity equations is

\[
\boxed{
k_K(x,y)
=
g_{K}^{\rm arch,red}(x-y)
+
\sum_{\log n\le 2a}
\frac{b_K(n)}{\sqrt n}
\bigl(|x-y|-\log n\bigr)_+
-
\mu N_a(x,y),
}
\]

where

\[
b_K(n)=\Lambda(n)(1+\chi_{12}(n)),
\qquad
\mu=\lambda-\log12.
\]

Every arithmetic contribution is continuous and piecewise linear in `|x-y|`, and only prime powers satisfying

\[
\log n\le2a
\]

appear.

Therefore the numerical problem is finite-arithmetic at every fixed `a`, exact in the conductor shift, and parity-reduced before discretization.

---

## 11. What is proved and what remains open

### Exact / derived here

\[
k_K(-x,-y)=k_K(x,y),
\]

\[
(C_-,A_-,B_-)
=
e^{i\alpha_a}(C_+,-A_+,B_+),
\]

and hence the two Suzuki Fredholm equations are one reflected equation.

The explicit resolvent normalization

\[
q_\pm=T_{K,a}^{-1}e^{\pm x}
\]

fixes the deficiency phase canonically and yields

\[
q_-=Rq_+,
\qquad C_+=C_-=1.
\]

The Fredholm equation splits exactly into the two real parity sectors

\[
K_a^{\rm Fred}q_e=-(\cosh x+B_a),
\]

\[
K_a^{\rm Fred}q_o=-(\sinh x+A_ax),
\]

with the common-sign convention determined by the displayed integral equations above.

### Source-established from Suzuki

Section 8.3 gives the equations (8.4)–(8.5), the formulas for `A_\pm,B_\pm`, the continuous first-kind Fredholm interpretation, and the warning that (8.5) is not literally the same as the operator equation in the transferred `S_a` space.

### Still open

1. rigorous finite-to-infinite convergence of the D12 characteristic functions;
2. proof that the D12 infinite Weil-energy space is the de Branges space generated by the proposed `E_K`;
3. convergence of the finite Fredholm solutions `q_{\pm,a}` to the corresponding infinite deficiency functions;
4. quantitative control of the ill-conditioning inherent in the first-kind Fredholm equation;
5. GRH for `\zeta_{\mathbb Q(\sqrt3)}`.

No GRH conclusion is claimed.

---

## 12. Next target

The next highest-value step is now computationally and analytically specific:

\[
\boxed{
\text{construct the D12 parity-reduced Nystr\"om/Galerkin discretization of the Section-8 kernel and verify it against the differentiated equation.}
}
\]

Before trusting any large-`a` spectral experiment, the implementation should test four exact invariants at finite `a`:

1. reflection: `q_-(x)=q_+(-x)`;
2. endpoint traces: `q_e(a)=q_o(a)=0`;
3. affine constants: `A_-=-A_+`, `B_-=B_+`;
4. differentiated residual: differentiating the recovered Fredholm equation twice reproduces the `D^*GD` deficiency equation away from the finitely many prime breakpoints.

Once those checks pass, one can form

\[
W^{\rm raw}_{K,a}(\pi;z)
\]

or the appropriate Suzuki boundary phase and compare its normalized ratio directly with the current primary-source target, without any unknown deficiency-vector scale.