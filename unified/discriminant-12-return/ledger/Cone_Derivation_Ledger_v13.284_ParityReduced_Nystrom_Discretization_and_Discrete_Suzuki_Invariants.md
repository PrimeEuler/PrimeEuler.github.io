# Cone Derivation Ledger v13.284 — Parity-Reduced Nyström Discretization and Discrete Suzuki Invariants

Date: 2026-09-07

Status: EXACT HALF-INTERVAL DISCRETIZATION ARCHITECTURE + IMPLEMENTATION CHECKPOINT — GRH NOT PROVED

## 0. Synchronization and implementation state

Immediately before this write, the authoritative project README and current `master` tip were re-fetched.

The tip was

`0fd2f2d2eb0adbd3c8cf0806f75b1eea3f41714e`,

whose only new file since v13.283 is

`research-notes/suzuki_d12_fredholm_nystrom.py`.

No newer external-audit checkpoint was present.

That script implements the parity-reduced Section-8 system derived in v13.283.  It deliberately leaves the source-faithful reduced archimedean screw kernel as an injected callable; the exact Neumann kernel, D12 prime-power horizon, prime ramps, parity compression, augmented Nyström systems, characteristic function, and normalization-free characteristic ratio are implemented.

This entry records the exact discrete equations and the invariants that must be checked before any numerical finite-to-infinite claim is trusted.

---

## 1. Half-interval parity kernels

Let

\[
k_K(x,y)=g_K^{\rm red}(x-y)-\mu N_a(x,y),
\qquad
\mu=\lambda-\log 12,
\]

with

\[
k_K(-x,-y)=k_K(x,y).
\]

For `x,y in [0,a]`, define

\[
\boxed{
K_e(x,y)=k_K(x,y)+k_K(x,-y),
}
\]

and

\[
\boxed{
K_o(x,y)=k_K(x,y)-k_K(x,-y).
}
\]

If

\[
q_+=q_e+q_o,
\]

with `q_e` even and `q_o` odd, then the full-interval Fredholm equation of v13.283 is exactly equivalent to

\[
\boxed{
-\int_0^a K_e(x,y)q_e(y)\,dy
=\cosh x+B_a,
}
\]

and

\[
\boxed{
-\int_0^a K_o(x,y)q_o(y)\,dy
=\sinh x+A_a x.
}
\]

This is an exact reduction, not a discretization artifact.

At `x=0`, simultaneous reflection gives

\[
k_K(0,-y)=k_K(0,y),
\]

hence

\[
\boxed{K_o(0,y)=0.}
\]

Therefore the odd integral equation at `x=0` is identically

\[
0=0.
\]

This row contains no information and must not be used as an ordinary collocation equation.

---

## 2. Endpoint traces and the augmented unknowns

The canonical raw deficiency vector is

\[
q_+=T_{K,a}^{-1}e^x.
\]

Because the finite Friedrichs realization has the same endpoint trace inherited from the `H_0^1(-a,a)` core,

\[
q_+(\pm a)=0.
\]

In parity variables this is

\[
\boxed{q_e(a)=0,\qquad q_o(a)=0.}
\]

Odd parity also gives

\[
\boxed{q_o(0)=0.}
\]

The affine integration constants are not externally prescribed numbers.  They are solved simultaneously with the functions:

\[
\boxed{(q_e,B_a)}
\]

and

\[
\boxed{(q_o,A_a)}.
\]

This avoids attempting to recover `A_a,B_a` afterward from numerically differentiated kernel rows.

---

## 3. Gauss–Lobatto–Legendre Nyström grid

Choose polynomial degree `N>=2` and Gauss–Lobatto–Legendre nodes and weights on `[0,a]`,

\[
0=x_0<x_1<\cdots<x_N=a,
\]

\[
w_j>0.
\]

The endpoint-containing rule is useful here because the trace constraints can be imposed directly at the same unknown nodes.

If `P_N` is the Legendre polynomial on `[-1,1]`, the unscaled Lobatto weights are

\[
\boxed{
\omega_j=
\frac{2}{N(N+1)P_N(t_j)^2},
}
\]

where `t_0=-1`, `t_N=1`, and the interior nodes are the zeros of `P_N'`.

After mapping to `[0,a]`,

\[
\boxed{w_j=\frac a2\omega_j.}
\]

The implementation uses exactly this construction through `numpy.polynomial.legendre.Legendre` and does not require SciPy.

---

## 4. Even augmented matrix

Let

\[
q_j^{(e)}\approx q_e(x_j).
\]

Collocation at all `N+1` nodes gives

\[
-\sum_{j=0}^{N}w_jK_e(x_i,x_j)q_j^{(e)}-B_a
=\cosh x_i,
\qquad 0\le i\le N.
\]

Append the endpoint equation

\[
q_N^{(e)}=0.
\]

The unknown vector is

\[
\boxed{
u_e=(q_0^{(e)},\ldots,q_N^{(e)},B_a)^T.}
\]

Thus the even matrix is square of size `(N+2)x(N+2)`:

\[
\boxed{
M_e=
\begin{pmatrix}
-[w_jK_e(x_i,x_j)] & -\mathbf 1\\
0\ \cdots\ 0\ 1 & 0
\end{pmatrix}.
}
\]

The right side is

\[
\boxed{
b_e=(\cosh x_0,\ldots,\cosh x_N,0)^T.}
\]

---

## 5. Odd augmented matrix and the null `x=0` row

Let

\[
q_j^{(o)}\approx q_o(x_j).
\]

Because the `x=0` equation is identically zero, collocate only at

\[
x_1,\ldots,x_N.
\]

Then

\[
-\sum_{j=0}^{N}w_jK_o(x_i,x_j)q_j^{(o)}-A_ax_i
=\sinh x_i,
\qquad 1\le i\le N.
\]

Append

\[
q_0^{(o)}=0,
\qquad
q_N^{(o)}=0.
\]

The unknown vector is

\[
\boxed{
u_o=(q_0^{(o)},\ldots,q_N^{(o)},A_a)^T.}
\]

There are `N` nontrivial collocation rows plus two trace rows, hence again a square `(N+2)x(N+2)` system.

This exact row count is important.  Keeping the `x=0` integral row would insert a zero row and make the discrete system spuriously singular.

---

## 6. Why least squares / SVD is the default solver

Suzuki's Section-8 equation is a Fredholm equation of the first kind.  Such discretizations can be strongly ill-conditioned even when the underlying finite operator problem is well defined.

Therefore the prototype solves

\[
M_e\nu_e=b_e,
\qquad
M_o\nu_o=b_o
\]

with an SVD-backed least-squares solve rather than assuming ordinary dense inversion is numerically trustworthy.

For every run, record

\[
\boxed{\kappa_e=\operatorname{cond}_2(M_e),
\qquad
\kappa_o=\operatorname{cond}_2(M_o).}
\]

Also record the discrete residuals

\[
\boxed{
r_e=\|M_e\nu_e-b_e\|_\infty,
\qquad
r_o=\|M_o\nu_o-b_o\|_\infty.}
\]

A small residual alone is not evidence of a stable continuum approximation when the condition number is large.  Convergence in `N`, stability under `rcond`, and the continuum residual tests below are all required.

---

## 7. Exact finite D12 arithmetic assembly

The arithmetic coefficient is

\[
\boxed{b_K(n)=\Lambda(n)(1+\chi_{12}(n)).}
\]

For prime powers,

\[
b_K(p^m)=\log p\,[1+\chi_{12}(p)^m],
\]

with `chi12(p)=0` for the ramified primes `2,3`.

The exact finite prime horizon is

\[
\boxed{n\le e^{2a}.}
\]

The implemented continuous arithmetic screw contribution is

\[
\boxed{
g^{\rm prime}_{K,a}(t)
=
\sum_{\log n\le2a}
\frac{b_K(n)}{\sqrt n}
(|t|-\log n)_+.}
\]

The code enumerates prime powers up to the exact horizon and refuses to silently truncate if that horizon exceeds an explicit safety ceiling.

This is preferable to summing all integers and testing `Lambda(n)` numerically.

---

## 8. Exact conductor handling in the code

The inverse Neumann kernel is

\[
\boxed{
N_a(x,y)
=
\frac{x^2+y^2}{4a}
-rac{|x-y|}{2}
+rac a6.
}
\]

The discriminant conductor contribution has already been reduced in v13.282 to

\[
(\log12)K_a.
\]

Therefore the implementation never adds a second standalone conductor kernel.  It uses

\[
\boxed{
\mu=\lambda-\log12
}
\]

and assembles

\[
\boxed{
k_K(x,y)=g_K^{\rm red}(x-y)-\mu N_a(x,y).}
\]

This prevents double-counting the field conductor.

---

## 9. Characteristic function directly from parity data

Define

\[
F_+(z)=\int_{-a}^{a}q_+(x)e^{izx}\,dx.
\]

Using

\[
q_+=q_e+q_o,
\]

one obtains the exact half-interval representation

\[
\boxed{
F_+(z)
=2\int_0^a
\left[q_e(x)\cos(zx)+i q_o(x)\sin(zx)\right]dx.
}
\]

For the canonical real reflected basis,

\[
q_-(x)=q_+(-x),
\]

so

\[
\boxed{
F_-(z)=F_+(-z)
=2\int_0^a
\left[q_e(x)\cos(zx)-i q_o(x)\sin(zx)\right]dx.
}
\]

Thus Suzuki's finite characteristic is obtained without reconstructing a separate minus solve:

\[
\boxed{
W_{K,a}^{\rm raw}(\theta;z)
=(z-i)F_+(z)
+e^{i\theta}(z+i)F_-(z).
}
\]

The code evaluates the two half-interval integrals with the same Lobatto weights.

---

## 10. Normalization cancels exactly

If Suzuki's equal-energy normalized deficiency vectors are

\[
v_\pm=c_aq_\pm,
\]

then

\[
W_{K,a}(\theta;z)=c_aW_{K,a}^{\rm raw}(\theta;z).
\]

Hence at any reference point `z_*` with nonzero characteristic,

\[
\boxed{
\frac{W_{K,a}(\theta;z)}{W_{K,a}(\theta;z_*)}
=
\frac{W_{K,a}^{\rm raw}(\theta;z)}
{W_{K,a}^{\rm raw}(\theta;z_*)}.
}
\]

The unknown deficiency-vector normalization therefore disappears from the finite-to-infinite comparison.

This is the preferred numerical observable.

---

## 11. Mandatory finite-`a` invariants

A computed solution is not accepted merely because the linear solve returned numbers.  Before interpreting a characteristic function, verify:

### 11.1 Endpoint/parity constraints

\[
\boxed{
q_e(a)=0,
\qquad
q_o(0)=0,
\qquad
q_o(a)=0.
}
\]

### 11.2 Reflection reconstruction

The reconstructed full vectors must satisfy

\[
\boxed{q_-(x)=q_+(-x).}
\]

In half-interval samples this means

\[
q_-(x)=q_e(x)-q_o(x).
\]

### 11.3 Affine reflection laws

With the canonical real basis,

\[
\boxed{C_-=C_+=1,
\qquad
A_-=-A_+,
\qquad
B_-=B_+.}
\]

### 11.4 Collocation residuals and condition numbers

Both `r_e,r_o` and `kappa_e,kappa_o` must be reported.

### 11.5 Degree convergence

Repeat at increasing degrees

\[
N,\ 2N,\ 4N
\]

or another nested sequence and compare:

\[
q_e,\ q_o,\ A_a,\ B_a,
\]

and normalized characteristic values at a fixed grid of `z`.

A single-grid result has no evidentiary status.

---

## 12. New numerical issue: the prime ramps create moving kink points

The prime contribution is continuous but only piecewise linear.  For fixed collocation point `x`, a term

\[
(|x-y|-v)_+
\]

changes derivative when

\[
y=x\pm v.
\]

The reflected half-kernel also introduces kinks from

\[
(|x+y|-v)_+,
\]

which occur at

\[
y=v-x.
\]

Therefore the integrand in a Nyström row has `x`-dependent breakpoints.

A single global Gauss-Lobatto rule does **not** see these breakpoints explicitly.  It remains a valid exploratory quadrature, but its convergence is generally algebraic rather than the spectral convergence one might expect for a globally smooth kernel.

This yields the next important implementation improvement:

\[
\boxed{
\text{breakpoint-aware product integration / panel quadrature.}
}
\]

For each row `x_i`, split the `y` integration at every point in `[0,a]` of the form

\[
\boxed{
|x_i\pm \log n|
}
\]

that corresponds to an actual ramp transition, together with the archimedean kernel's own nonsmooth points if any.

This preserves the exact arithmetic kink geometry instead of asking a global polynomial quadrature to approximate it indirectly.

---

## 13. Continuum residual, not only first-kind residual

Suzuki explicitly warns that the integrated first-kind equation is not literally the transferred operator equation.

Therefore a production computation must test the differentiated equation as well.

Away from the finite set of prime breakpoints,

\[
|x-y|=\log n,
\]

twice differentiating the integrated equation in `x` should recover the original Section-8 deficiency equation.

Operationally, after obtaining `q_+`, evaluate an independent residual on points not used for collocation and not near the kink set.

The preferred diagnostic is

\[
\boxed{
\mathcal E_{\rm diff}(x)
=
\text{differentiated-kernel LHS}
-	ext{Suzuki deficiency RHS},
}
\]

with its sup norm recorded on a safe test grid.

This prevents a numerically excellent solution of the twice-integrated equation from being mistaken for a verified solution of the original operator equation.

---

## 14. What the prototype does and does not establish

The current script establishes a reproducible implementation architecture for:

1. exact D12 prime-power enumeration on the finite horizon;
2. exact prime-ramp kernel assembly;
3. exact conductor absorption through `mu=lambda-log12`;
4. exact parity compression;
5. endpoint-aware augmented Nyström systems;
6. SVD/condition-number diagnostics;
7. one-solve reconstruction of both deficiency vectors;
8. normalization-free finite Suzuki characteristic ratios.

It does **not** yet contain the final source-faithful reduced archimedean screw kernel.  The placeholder `zero_arch_reduced` in the executable smoke test is explicitly marked as nonphysical and must never be used for a D12 spectral conclusion.

It also does not yet implement breakpoint-aware quadrature or the differentiated continuum residual.

No RH/GRH conclusion is claimed.

---

## 15. Next target

The next high-value step is now sharply defined:

\[
\boxed{
\text{insert Suzuki's exact archimedean continuous screw kernel and validate the solver against his Riemann case first.}
}
\]

The order should be:

1. extract the exact Section-8/earlier screw-function formula for Suzuki's Riemann continuous kernel `g_zeta(t)`;
2. reproduce his one-field finite kernel with the current parity/Nyström machinery;
3. implement row-wise breakpoint-aware quadrature for the prime ramps;
4. verify the differentiated deficiency residual;
5. only then form the D12 reduced archimedean kernel, which should be two real gamma contributions plus the already-separated pole term, with the conductor handled solely by `mu`;
6. compare normalized finite D12 characteristics as `a` and `N` increase.

This provides a source-faithful calibration step before any novel D12 finite-volume numerics are interpreted.