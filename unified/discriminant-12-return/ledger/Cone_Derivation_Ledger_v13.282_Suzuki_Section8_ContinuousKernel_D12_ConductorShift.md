# Cone Derivation Ledger v13.282 — Suzuki Section 8 Continuous-Kernel Transfer and the Exact D12 Conductor Shift

Date: 2026-09-07

Status: PRIMARY-SOURCE RECONCILIATION + EXACT SECTION-8 TRANSFER + EXACT CONDUCTOR-SHIFT REDUCTION — GRH NOT PROVED

## 0. Synchronization and external-audit reconciliation

Immediately before this write, the authoritative project README and current `master` tip were re-fetched.

A new checkpoint had landed:

`v13.281 — External Audit Round 12`, commit

`c799459df1c4a416597293a23ed02b1203797a23`.

That audit verified the internally checkable reflection/parity/de Branges algebra in `v13.278–v13.280`, but correctly flagged a serious reliability problem: the attribution of Suzuki's Corollary 1.6 target had flipped repeatedly between

\[
\frac{\xi}{\xi+\xi'}
\]

and

\[
z^2\frac{\xi}{\xi'}.
\]

The auditor's environment could not access the primary arXiv source, so it left the citation unresolved.

For this checkpoint the current primary source was opened directly:

Masatoshi Suzuki, “Weil's quadratic form via the screw function,” arXiv:2606.09096v2.

The current arXiv HTML explicitly states at Corollary 1.6, equation (1.12):

\[
\boxed{
\lim_{a\to\infty}e^{\phi(a,z)}W(a,\theta;z)
=
\frac{\xi(1/2-iz)}{\xi(1/2-iz)+\xi'(1/2-iz)}
}
\]

uniformly on compact subsets of `C`.

The source text immediately before the corollary describes the target as “the reciprocal of one plus its logarithmic derivative,” and Section 7.8 derives the same expression from

\[
E(z)=\xi(1/2-iz)+\xi'(1/2-iz).
\]

Therefore the source state used from this checkpoint onward is

\[
\boxed{\xi/(\xi+\xi')}
\]

for Suzuki v2.

This entry deliberately does **not** call that fact “definitive” or “conclusive”; it records the exact current primary-source equation and line of derivation so that any later source revision can be checked against a concrete equation number.

---

## 1. Suzuki's exact Section-8 reduction

Suzuki's Section 8 replaces the unbounded finite Weil operator `A_a` by a compact integral-operator formulation with continuous kernels.

Let

\[
D=i\frac{d}{dx}:H_0^1(-a,a)\to L_0^2(-a,a),
\]

where

\[
L_0^2(-a,a)=\left\{u\in L^2(-a,a):\int_{-a}^a u(x)\,dx=0\right\}.
\]

Suzuki uses the continuous screw-kernel operator `G_a` and the exact identity

\[
Q_W(v)=Q_G(Dv).
\]

The inverse Neumann Laplacian

\[
K_a:=(-\Delta_N)^{-1}
\]

acts on `L_0^2(-a,a)` and has continuous kernel

\[
\boxed{
N_a(x,y)
=
\frac{x^2+y^2}{4a}-\frac{|x-y|}{2}+\frac{a}{6}.
}
\]

For

\[
u=Dv,
\]

Suzuki proves the exact quadratic-form identity

\[
\boxed{
\|v\|_2^2
=
\langle K_a u,u\rangle_2.
}
\]

If

\[
T_a=A_a-\lambda I,
\qquad \lambda<\lambda_a,
\]

then Section 8 defines

\[
\boxed{
S_a:=G_a-\lambda K_a
}
\]

and obtains

\[
\boxed{
\|u\|_{S_a}^2
=
\|v\|_{T_a}^2,
\qquad u=Dv.
}
\]

Thus `D` extends to an isometric isomorphism

\[
\boxed{
\bar D:\mathcal H(T_a)\overset{\sim}{\longrightarrow}\mathcal H(S_a).
}
\]

The transferred first-order differential operator on `\mathcal H(S_a)` is unitarily equivalent to Suzuki's original finite operator on `\mathcal H(T_a)`, so the deficiency indices remain `(1,1)` and all self-adjoint extensions have the same spectra.

This is source-established in Suzuki Section 8.2–8.3.

---

## 2. D12 continuous-kernel transfer

For

\[
K=\mathbb Q(\sqrt3),
\]

let `A_{K,a}` be the finite D12 Weil operator constructed in the preceding checkpoints, and let `G_{K,a}` denote its Section-8 continuous-kernel counterpart on `L_0^2(-a,a)`.

Define

\[
T_{K,a}=A_{K,a}-\lambda I,
\qquad
S_{K,a}=G_{K,a}-\lambda K_a.
\]

Because the D12 form satisfies the same exact factorization through `D`,

\[
Q_{W,K}(v)=Q_{G,K}(Dv),
\]

the same calculation gives

\[
\boxed{
\langle S_{K,a}u,u\rangle
=
\langle T_{K,a}v,v\rangle,
\qquad u=Dv.
}
\]

Hence

\[
\boxed{
\bar D:\mathcal H(T_{K,a})\overset{\sim}{\longrightarrow}\mathcal H(S_{K,a})
}
\]

is an isometry, and the first-order D12 self-adjoint extension problem can be studied entirely in the continuous-kernel space.

No GRH is used in this finite-volume transfer.

---

## 3. Exact D12 finite prime kernel

From the earlier screw decomposition, the field von Mangoldt coefficient is

\[
\boxed{
b_K(n)=\Lambda(n)(1+\chi_{12}(n))\ge0.
}
\]

For one prime power `n`, with

\[
v_n=\log n,
\qquad
c_n=\frac{b_K(n)}{\sqrt n},
\]

the continuous screw contribution is the ramp

\[
\boxed{
g_n(t)=c_n(|t|-v_n)_+.
}
\]

Indeed,

\[
g_n''(t)
=
c_n\bigl(\delta(t-v_n)+\delta(t+v_n)\bigr),
\]

and applying `D^*G D` gives exactly the previously derived symmetric truncated-shift operator

\[
-c_n(S_{a,v_n}+S_{a,v_n}^*).
\]

On the interval `[-a,a]` one has `|x-y|\le2a`, so only

\[
\boxed{n\le e^{2a}}
\]

can occur.

Therefore the complete D12 arithmetic contribution to the continuous kernel is the **finite** sum

\[
\boxed{
 g^{\rm prime}_{K,a}(t)
 =
 \sum_{\log n\le2a}
 \frac{b_K(n)}{\sqrt n}
 (|t|-\log n)_+,
 \qquad |t|\le2a.
}
\]

This is the exact continuous-kernel version of the finite prime horizon from `v13.266`.

The kernel is continuous and piecewise linear, with all arithmetic nonsmoothness confined to the finitely many points

\[
|t|=\log n\le2a.
\]

Thus the finite arithmetic operator is numerically accessible without ever differentiating the kernel into distributions.

---

## 4. Exact conductor transport into the Neumann kernel

`v13.276` derived the D12 conductor contribution on the `A`/`B` side:

\[
\boxed{
B_{\rm cond}=(\log12)I.
}
\]

Let

\[
u=Dv.
\]

Then Suzuki's Section-8 identity gives

\[
\|v\|_2^2
=
\langle K_a u,u\rangle_2.
\]

Therefore

\[
\langle B_{\rm cond}v,v\rangle
=(\log12)\|v\|_2^2
=(\log12)\langle K_a u,u\rangle.
\]

Hence the corresponding continuous-kernel operator is exactly

\[
\boxed{
G_{\rm cond}=(\log12)K_a.
}
\]

Equivalently, at kernel level,

\[
\boxed{
 g_{\rm cond}^{(a)}(x,y)
 =
 (\log12)N_a(x,y).
}
\]

This is an exact operator identity on `L_0^2(-a,a)`, not merely a quadratic-form heuristic.

---

## 5. The conductor is a pure generalized-eigenvalue shift

Write

\[
G_{K,a}=G^{\rm red}_{K,a}+(\log12)K_a.
\]

Then

\[
S_{K,a}
=G_{K,a}-\lambda K_a
=G^{\rm red}_{K,a}-(\lambda-\log12)K_a.
\]

Define the shifted spectral parameter

\[
\boxed{
\mu:=\lambda-\log12.
}
\]

Then

\[
\boxed{
S_{K,a}
=G^{\rm red}_{K,a}-\mu K_a.
}
\]

Likewise, on the unbounded side,

\[
A_{K,a}=A^{\rm red}_{K,a}+(\log12)I
\]

implies

\[
\boxed{
T_{K,a}=A^{\rm red}_{K,a}-\mu I.
}
\]

Therefore the conductor `12` does **not** create a new finite eigenfunction geometry. It only translates the generalized eigenvalue parameter:

\[
\boxed{
G_{K,a}u=\lambda K_a u
\iff
G^{\rm red}_{K,a}u=(\lambda-\log12)K_a u.
}
\]

Consequences:

1. generalized eigenfunctions are unchanged by the conductor scalar;
2. the entire generalized spectrum is translated by `+log 12`;
3. the deficiency vectors determined by `T_{K,a}^{-1}` depend on the conductor only through the shifted choice `\mu=\lambda-\log12`;
4. any normalized characteristic ratio that eliminates a scalar normalization should be insensitive to the conductor shift itself.

The conductor remains arithmetically meaningful in the completed zeta function, but in Suzuki's **finite Section-8 generalized-eigenvalue formulation** it is spectrally elementary.

---

## 6. D12 Fredholm first-kind equations

Suzuki writes

\[
k(x,y)=g(x-y)-\lambda N_a(x,y)
\]

and shows that the finite deficiency-vector equations are formally equivalent to ordinary Fredholm equations of the first kind with continuous kernel.

For D12 define

\[
\boxed{
k_K(x,y)
:=
g_K(x-y)-\lambda N_a(x,y).
}
\]

After removing the conductor shift,

\[
\boxed{
k_K(x,y)
=
g^{\rm red}_K(x-y)-\mu N_a(x,y),
\qquad
\mu=\lambda-\log12.
}
\]

If

\[
T_{K,a}v_{\pm}=C_{\pm}e^{\pm x},
\]

then Suzuki's Section-8 calculation transfers to

\[
\int_{-a}^{a}
\bigl(-\partial_x^2k_K(x,y)\bigr)
 v_{\pm}(y)\,dy
=C_{\pm}e^{\pm x},
\]

and, after twice integrating in `x`, to

\[
\boxed{
\int_{-a}^{a}
k_K(x,y)(-v_{\pm}(y))\,dy
=
C_{\pm}e^{\pm x}+A_{\pm}x+B_{\pm}.
}
\]

The constants `A_\pm,B_\pm` encode the two integrations and are determined by the kernel and the solution exactly as in Suzuki equation (8.5).

This is the direct D12 analogue of Suzuki's proposed numerical route.

---

## 7. Why this is a better computational object

The unbounded operator `A_{K,a}` contains distributional second derivatives of the screw kernel.

The Section-8 pair

\[
(G_{K,a},K_a)
\]

instead consists of compact operators with continuous kernels.

The D12 generalized eigenvalue problem is

\[
\boxed{
G_{K,a}u=\lambda K_a u.
}
\]

Its spectrum is the same generalized spectrum carried by the finite `A_{K,a}` problem, while the deficiency equations can be written with the continuous kernel `k_K` above.

The prime part is particularly simple:

\[
\sum_{\log n\le2a}
\frac{b_K(n)}{\sqrt n}
(|x-y|-\log n)_+.
\]

Thus every fixed `a` gives a finite arithmetic kernel whose exact breakpoints are known in advance.

A warning remains: Fredholm equations of the first kind can be numerically ill-conditioned. So the continuous-kernel formulation is structurally cleaner, but not automatically numerically stable. The generalized eigenvalue pair `(G_{K,a},K_a)` may be a better computational starting point than directly inverting the first-kind equation.

---

## 8. Relation to Suzuki's current Corollary 1.6 target

The primary source states

\[
R_K(z)
:=
\frac{\xi_K(1/2-iz)}
{\xi_K(1/2-iz)+\xi_K'(1/2-iz)}.
\]

Suzuki's Section 8 says, in the Riemann case, that the finite deficiency vectors can be computed from the continuous Fredholm equation and their Fourier transforms inserted into the finite characteristic

\[
W(a,\theta;z).
\]

Therefore the D12 finite-to-infinite frontier can now be phrased without the unbounded operator:

\[
\boxed{
\text{solve the finite continuous-kernel D12 deficiency equations}
\Longrightarrow
W_K(a,\pi;z)
\stackrel{?}{\longrightarrow}
\text{const}\cdot R_K(z).
}
\]

After normalization at a fixed reference point `z_*`, the scalar disappears:

\[
\boxed{
\frac{W_K(a,\pi;z)}{W_K(a,\pi;z_*)}
\stackrel{?}{\longrightarrow}
\frac{R_K(z)}{R_K(z_*)}.
}
\]

The conductor shift does not complicate this finite problem; it is absorbed exactly by

\[
\lambda\mapsto\lambda-\log12.
\]

---

## 9. Exact/open status

### Exact / source-established

- Suzuki Section 8 passes from `A_a` to the continuous-kernel operator `G_a`.
- `K_a=(-\Delta_N)^{-1}` has the explicit Neumann kernel `N_a(x,y)`.
- `D` gives an isometry between the `T_a` and `S_a` energy spaces.
- finite first-order extension spectra are preserved under this transfer.
- the finite deficiency equations admit the first-kind Fredholm formulation.
- current Suzuki v2 Corollary 1.6 uses `xi/(xi+xi')`.

### Exact project derivations

- the D12 prime kernel is the finite ramp sum with coefficients `b_K(n)/sqrt(n)`.
- the conductor contribution transports exactly as
  \[
  (\log12)I\mapsto(\log12)K_a.
  \]
- therefore the conductor is exactly removed by the generalized spectral shift
  \[
  \mu=\lambda-\log12.
  \]

### Open

- proving the D12 analogue of Suzuki's finite-to-infinite convergence;
- proving that the canonical finite phase tends to / equals the de Branges phase needed for the D12 infinite model;
- controlling the lower-bound parameter `\lambda` uniformly as `a\to\infty`;
- proving convergence of the continuous-kernel deficiency vectors or their Fourier transforms to the D12 de Branges deficiency functions;
- deriving GRH from this route.

No RH/GRH conclusion is claimed.

---

## 10. Next target

The next highest-value step is no longer abstract operator theory.

It is to exploit the explicit continuous kernel and derive a **finite D12 integral-equation normalization theorem**.

Concretely:

1. write `g_K^{red}` explicitly as archimedean/pole plus the finite prime-ramp sum;
2. impose the reflection relation on the first-kind equations for `v_+` and `v_-`;
3. reduce the two equations to one real equation whenever the canonical phase permits;
4. identify the exact normalization constants `C_\pm,A_\pm,B_\pm` from boundary conditions rather than leaving them free;
5. obtain a normalized finite characteristic directly from the continuous solution;
6. compare this normalized characteristic with
   \[
   \Xi_K/E_K.
   \]

The most important new structural fact of this checkpoint is

\[
\boxed{
\text{D12 conductor }12
\text{ is a pure }(+\log12)\text{ generalized-eigenvalue shift in Suzuki Section 8.}
}
\]

That removes one entire field-specific complication before the finite-to-infinite analysis begins.