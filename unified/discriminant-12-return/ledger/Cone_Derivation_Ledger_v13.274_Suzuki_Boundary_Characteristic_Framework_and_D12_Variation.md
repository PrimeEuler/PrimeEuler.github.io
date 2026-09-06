# Cone Derivation Ledger v13.274 — Suzuki Boundary Characteristic Framework and D12 Variation

Date: 2026-09-06

Status: SOURCE-AUDITED SUZUKI v2 ALIGNMENT + EXACT BOUNDARY VARIATION FORMULA + D12 CONDITIONAL TRANSFER TARGET — RH/GRH NOT PROVED

## 0. Synchronization and source correction

Immediately before this write, the authoritative README, current `master` tip, and highest ledger checkpoint were re-fetched. The tip remained

`14ed96aad19f21cb019ea4e96942d5c6aa81bb85`,

with v13.273 the highest project checkpoint and no newer external-audit entry present.

This entry deliberately uses Suzuki's framework as the primary reference rather than inventing a parallel operator formalism.

The current source is Masatoshi Suzuki, “Weil's quadratic form via the screw function,” arXiv:2606.09096v2, revised August 17, 2026. The current v2 statement of Corollary 1.6 is

\[
\boxed{
\lim_{a\to\infty}e^{\phi(a,z)}W(a,\theta;z)
=
\frac{\xi(1/2-iz)}{\xi(1/2-iz)+\xi'(1/2-iz)}
}
\]

uniformly on compact sets, for a suitable choice of `theta(a)` and normalization `phi(a,z)`.

This supersedes earlier project prose that described Suzuki's conjectural boundary target as `z^2 xi/xi'`. The project's independent squared-coordinate/Stieltjes derivations remain mathematically separate, but that older attribution is not the current v2 Suzuki formula and must not be used as the source target going forward.

Suzuki explicitly notes that `theta=pi` is plausibly the natural choice.

---

## 1. Suzuki's finite-interval framework, kept intact

For the Riemann case Suzuki starts from the localized Weil quadratic form `Q_W^a` and its associated self-adjoint operator `A_a`.

He defines the continuous screw-kernel operator

\[
G_a=P_aGP_a
\]

on the zero-mean subspace, with

\[
P_a u
=
 u-
 \frac1{2a}\int_{-a}^a u(y)\,dy,
\]

and the symmetric differential-integral operator

\[
\boxed{
B_a=D^*G_aD,
\qquad
\mathfrak D(B_a)=H_0^1(-a,a).
}
\]

His Theorem 1.1 identifies `A_a` as the Friedrichs extension of `B_a`.

For any

\[
\lambda<\lambda_a:=\inf\sigma(A_a),
\]

he sets

\[
T_a=A_a-\lambda I>0
\]

and completes `C_c^\infty(-a,a)` in the norm

\[
\|v\|_{T_a}^2=\langle T_av,v\rangle.
\]

The first-order operator

\[
\boxed{
\mathscr D_a=i\frac d{dx}
}
\]

on that Hilbert space has deficiency indices

\[
\boxed{(1,1).}
\]

If `v_+` and `v_-` span the deficiency spaces and are normalized to equal `T_a`-norm, then Suzuki proves

\[
\boxed{
(T_av_+)(x)=e^{x},
\qquad
(T_av_-)(x)=e^{-x}.
}
\]

More generally, the adjoint eigenfunction `v_z` is characterized by

\[
\boxed{
(T_av_z)(x)=e^{-izx}.
}
\]

This is the exact structural point needed by the D12 program: the boundary spectral data are obtained by applying the inverse positive Weil-form operator to exponential forcing terms.

---

## 2. Suzuki's characteristic entire function

For `theta in [0,2pi)`, Suzuki's Theorem 1.5 defines

\[
\boxed{
W(a,\theta;z)
=
(z-i)\int_{-a}^{a}v_+(a,x)e^{izx}\,dx
+
 e^{i\theta}(z+i)\int_{-a}^{a}v_-(a,x)e^{izx}\,dx.
}
\]

This function is entire in `z`.

Its zeros are exactly the eigenvalues of the self-adjoint extension `\overline{\mathscr D}_{a,\theta}`, and therefore

\[
\boxed{
\operatorname{Zeros}W(a,\theta;\cdot)\subset\mathbb R
}
\]

unconditionally for every finite `a`.

The finite spectral reality is therefore not an approximation and does not require RH.

This is the source framework the project should preserve.

---

## 3. Why the boundary object escapes the v13.273 Fredholm no-go

v13.273 proved that an additive self-adjoint perturbation cannot have an exact Euler logarithm as an ordinary Fredholm determinant because

\[
\log\det(I+\varepsilon K)
=
\varepsilon\operatorname{Tr}K
-
\frac{\varepsilon^2}{2}\operatorname{Tr}(K^2)+\cdots
\]

has nonzero quadratic cumulants for nonzero self-adjoint `K`.

Suzuki's `W(a,theta;z)` is structurally different.

It is built from

\[
v_\pm=T_a^{-1}e^{\pm x}
\]

and then from their Fourier transforms.

Thus the arithmetic enters through the **inverse** of the full localized Weil-form operator before the characteristic function is formed.

This nonlinear dependence is exactly what the bulk Fredholm ansatz lacked.

The v13.273 no-go therefore does not apply to Suzuki's boundary characteristic function.

---

## 4. D12 field-channel input

For

\[
K=\mathbb Q(\sqrt3),
\qquad
\zeta_K(s)=\zeta(s)L(s,\chi_{12}),
\]

the non-archimedean logarithmic-derivative coefficients are

\[
\boxed{
b_K(n)=\Lambda(n)(1+\chi_{12}(n))\ge0.
}
\]

From v13.273 the finite prime contribution to the localized `D^*GD` form is exactly

\[
\boxed{
V_{K,a}
=
-\sum_{\log n\le2a}
\frac{b_K(n)}{\sqrt n}
\left(S_{a,\log n}+S_{a,\log n}^*\right).
}
\]

No schematic normalization remains here.

The D12 extension target is therefore to construct the full localized Dedekind Weil operator

\[
A_{K,a}
\]

with the same Suzuki architecture, choose

\[
T_{K,a}=A_{K,a}-\lambda I>0,
\]

and define

\[
\boxed{
v_{K,\pm}=T_{K,a}^{-1}e^{\pm x}.
}
\]

This D12 transfer is not yet source-established by Suzuki; it is the project extension to the completed Dedekind zeta function. The algebraic factorization and explicit-formula coefficients are exact, but the full finite-interval operator theorem must be carried through carefully for the field channel.

---

## 5. Exact single-prime variation of Suzuki's boundary data

This is the main new calculation.

Fix one prime-power ramp at

\[
v=\log n,
\qquad
c=\frac{b_K(n)}{\sqrt n},
\]

with perturbation

\[
V_n=-c(S_{a,v}+S_{a,v}^*).
\]

Let

\[
T_\varepsilon=T_0+\varepsilon V_n
\]

and

\[
v_{\pm,\varepsilon}=T_\varepsilon^{-1}e^{\pm x}.
\]

The resolvent derivative identity gives

\[
\boxed{
\frac{d}{d\varepsilon}T_\varepsilon^{-1}\Big|_{0}
=-T_0^{-1}V_nT_0^{-1}.
}
\]

Hence

\[
\boxed{
\delta v_\pm
:=
\frac{d}{d\varepsilon}v_{\pm,\varepsilon}\Big|_0
=
-T_0^{-1}V_n v_\pm.
}
\]

Since `V_n=-c(S+S^*)`,

\[
\boxed{
\delta v_\pm
=
c\,T_0^{-1}(S_{a,v}+S_{a,v}^*)v_\pm.
}
\]

Now define the Suzuki characteristic function

\[
W_\varepsilon(a,\theta;z)
=(z-i)\widehat{v_{+,\varepsilon}}(z)
+e^{i\theta}(z+i)\widehat{v_{-,\varepsilon}}(z).
\]

Differentiating gives the exact one-prime boundary response

\[
\boxed{
\begin{aligned}
\delta W(a,\theta;z)
=c\Big[&(z-i)
\widehat{T_0^{-1}(S_{a,v}+S_{a,v}^*)v_+}(z)
\\
&+e^{i\theta}(z+i)
\widehat{T_0^{-1}(S_{a,v}+S_{a,v}^*)v_-}(z)
\Big].
\end{aligned}
}
\]

Away from zeros of `W`,

\[
\boxed{
\delta\log W
=
\frac{\delta W}{W}.
}
\]

This is the exact replacement for the failed bulk trace diagnostic.

There is no universal factor `2a-v` in this formula. The truncated shift is first filtered through the nonlocal inverse `T_0^{-1}` and then through the deficiency-vector/Fourier boundary functional.

Thus Suzuki's boundary architecture has precisely the missing mechanism that the naive bulk trace did not have.

This does not yet prove that the response equals the Euler coefficient; it proves that the overlap obstruction is not structurally forced at the boundary level.

---

## 6. Real-axis pairing form

For real `z`, Suzuki's adjoint eigenvector satisfies

\[
T_0v_z=e^{-izx}.
\]

Using self-adjointness of `T_0^{-1}`, the Fourier factor in the variation can be rewritten as a matrix element involving `v_z`.

Up to the fixed inner-product convention,

\[
\boxed{
\widehat{T_0^{-1}V_nv_\pm}(z)
=
\langle V_nv_\pm,v_z\rangle.
}
\]

Therefore the one-prime boundary response is controlled by the three deficiency/adjoint eigenvectors

\[
\boxed{
v_+,\ v_-,\ v_z}
\]

rather than by the raw geometric length of the overlap interval.

Substituting the exact shift operator gives matrix elements of the form

\[
\langle S_{a,v}v_\pm,v_z\rangle
+
\langle S_{a,v}^*v_\pm,v_z\rangle.
\]

This is the finite-volume quantity to compare against the D12 Euler weight.

---

## 7. Current Suzuki v2 infinite-volume target

Let

\[
\Xi_K(z):=\xi_K(1/2-iz),
\]

where `xi_K` is the completed entire Dedekind xi-function.

The direct D12 analogue of Suzuki's current v2 boundary target is

\[
\boxed{
R_K(z)
:=
\frac{\xi_K(1/2-iz)}
{\xi_K(1/2-iz)+\xi_K'(1/2-iz)}.
}
\]

Equivalently, with

\[
E_K(z)
:=
\xi_K(1/2-iz)+\xi_K'(1/2-iz),
\]

we have

\[
R_K(z)=\frac{\Xi_K(z)}{E_K(z)}.
\]

This is presently a **D12 transfer target**, not a Suzuki theorem for `zeta_K`.

The proposed finite-volume convergence statement is

\[
\boxed{
e^{\phi_K(a,z)}W_K(a,\theta(a);z)
\longrightarrow
R_K(z).
}
\]

The natural first choice to test is

\[
\boxed{\theta(a)=\pi,}
\]

in direct analogy with Suzuki's v2 discussion.

---

## 8. De Branges structure behind Suzuki's choice

Suzuki's 2025 paper “On the Hilbert space derived from the Weil distribution” identifies, under RH, the completed Weil Hilbert space with a de Branges space.

In the 2026 paper the relevant Hermite–Biehler function is

\[
\boxed{
E(z)
=
\xi(1/2-iz)+\xi'(1/2-iz).
}
\]

Its reproducing kernel is written as

\[
K(w,z)
=
\frac{E(z)\overline{E(w)}-E^\sharp(z)\overline{E^\sharp(w)}}
{2\pi i(\bar w-z)}.
\]

Suzuki then identifies the deficiency vectors with reproducing kernels at `\mp i`.

For general `theta`, the boundary form reduces to

\[
C_\theta E(z)-\overline{C_\theta}E^\sharp(z),
\]

and at

\[
\theta=\pi
\]

this collapses to a constant multiple of

\[
\xi(1/2-iz).
\]

That is the exact source reason `theta=pi` is special.

For D12, the corresponding high-value theorem to seek is therefore not an arbitrary spectral determinant identity but a **Dedekind de Branges identification** with

\[
E_K(z)
=
\xi_K(1/2-iz)+\xi_K'(1/2-iz).
\]

If that transfer is valid under GRH, the same boundary geometry becomes available for `K=Q(sqrt3)`.

---

## 9. A weaker sufficient convergence criterion than Suzuki's global compact convergence

Suzuki states a global compact-uniform convergence criterion.

For the D12 project we can isolate a weaker sufficient condition that avoids asking for more than is needed to force the zeros onto the real axis.

Let `gamma_0` be a zero of

\[
\Xi_K(z)=\xi_K(1/2-iz).
\]

Near such a zero, even if it has multiplicity `m`,

\[
\frac{\xi_K}{\xi_K+\xi_K'}
\]

has a zero at the same point: if

\[
\xi_K(s)=c(s-s_0)^m+\cdots,
\]

then

\[
\frac{\xi_K(s)}{\xi_K(s)+\xi_K'(s)}
\sim
\frac{s-s_0}{m}.
\]

Therefore every nontrivial zero of `xi_K` is a zero of `R_K`.

Suppose that for every zero `gamma_0` there exists a neighborhood `U_{gamma_0}` on which

\[
\boxed{
e^{\phi_K(a,z)}W_K(a,\theta(a);z)
\to R_K(z)
}
\]

locally uniformly and `R_K` is analytic there.

Because the exponential normalization is nonvanishing, every finite approximant has exactly the same zeros as `W_K`, hence only real zeros.

Hurwitz's theorem then forces every zero `gamma_0` of `R_K`, hence every zero of `Xi_K`, to lie on the real axis.

Thus

\[
\boxed{
\text{local convergence only near the zeros of }\Xi_K
\Longrightarrow
\mathrm{GRH}(\zeta_K).
}
\]

This is strictly weaker than demanding one global compact-uniform identity across the entire complex plane.

It is therefore the preferred D12 convergence target.

---

## 10. Relationship to the earlier squared-coordinate/Stieltjes branch

The project already derived independently

\[
\Psi_K(w)=\xi_K(1/2+\sqrt w)
\]

and

\[
\mathcal S_K(w)=2\Psi_K'(w)/\Psi_K(w).
\]

Those formulas remain valid.

They provide a zero-geometry/Stieltjes reformulation of GRH after the square map.

Suzuki's actual finite boundary characteristic function, however, is presently tied to

\[
\boxed{
R_K(z)=\frac{\Xi_K(z)}{E_K(z)},
}
\]

not directly to `Psi_K` or `2 Psi_K'/Psi_K`.

The correct architecture is therefore now two complementary layers:

\[
\boxed{
\text{Suzuki finite boundary functions }W_K(a,\theta;z)
\to
R_K(z)
}
\]

for finite-to-infinite spectral reality, and

\[
\boxed{
\Xi_K(z)
\to
\Psi_K(w)
\to
\text{Stieltjes / Laguerre-Pólya zero geometry}
}
\]

for the global characterization of what real spectral reality means after squaring.

They should not be conflated.

---

## 11. Next exact tasks

The next work should stay as close to Suzuki as possible:

1. Construct the D12/Dedekind analogue of Suzuki's localized Weil form `Q_W^a` and verify lower boundedness/closedness in the precise finite interval setting.
2. Prove that its associated operator `A_{K,a}` is the Friedrichs extension of `D^*G_{K,a}D` exactly as in Suzuki Theorem 1.1.
3. Prove the D12 minimal derivative operator has deficiency indices `(1,1)` using Suzuki's argument, with
   \[
   T_{K,a}v_{K,\pm}=e^{\pm x}.
   \]
4. Define
   \[
   W_K(a,\theta;z)
   \]
   exactly in Suzuki's form and establish real zeros for every finite `a`.
5. Compute the exact prime-by-prime variation using the formula of Section 5 above and test `theta=pi` first.
6. Audit whether Suzuki's 2025 de Branges construction extends from `xi` to the degree-two Dedekind `xi_K` under GRH, with
   \[
   E_K(z)=\xi_K(1/2-iz)+\xi_K'(1/2-iz).
   \]
7. Aim for local convergence near each zero rather than an unnecessarily stronger global identity.

The central target is now

\[
\boxed{
W_K(a,\pi;z)
\quad\text{from finite D12 Weil geometry}
\quad\Longrightarrow\quad
\frac{\xi_K(1/2-iz)}{\xi_K(1/2-iz)+\xi_K'(1/2-iz)}.
}
\]

This is the closest current project formulation to Suzuki's own 2026 operator program.

---

## 12. Guardrails

- No RH/GRH result is claimed.
- Suzuki's Theorems 1.1 and 1.5 are source-established for the Riemann zeta Weil form; the Dedekind/D12 transfer is project work still to be proved.
- The current v2 Corollary 1.6 target is `xi/(xi+xi')`; older project wording using `z^2 xi/xi'` is superseded as a source attribution.
- The additive-Fredholm no-go of v13.273 remains valid but does not apply to Suzuki's inverse-form/deficiency-vector characteristic function.
- The H4/V4 block structure remains exact at the arithmetic and quadratic-form level, but a scalar D12 deficiency-space theorem still requires construction of the field-channel finite operator.
