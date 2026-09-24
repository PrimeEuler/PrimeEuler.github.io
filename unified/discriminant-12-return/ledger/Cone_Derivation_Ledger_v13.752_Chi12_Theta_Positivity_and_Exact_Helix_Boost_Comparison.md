# Cone Derivation Ledger v13.752 — Chi12 Theta Positivity and Exact Helix/Boost Comparison

Date: 2026-09-24

Status: [D] exact derivation, [I] interpretation, [N] obstruction/non-equivalence, [G] guardrail.

## 0. Synchronization

The live ledger was rechecked after v13.751 (External Audit Round 90). No collision was present. Round 90 explicitly identified the two gates treated here: (i) positivity of the chi12 theta kernel and (ii) the exact relation between the original nested-circle/all-frequency helix picture and the later \((r,u)\) boost-Fourier geometry.

## 1. Exact eta identity for the chi12 theta [D]

Use
\[
\vartheta_{\chi}(x)
=
\sum_{n\in\mathbf Z}\chi_{12}(n)
e^{-\pi n^2x/12}.
\]
Because chi12 is even and vanishes at zero,
\[
\vartheta_\chi(x)
=
2\sum_{n\ge1}\chi_{12}(n)e^{-\pi n^2x/12}.
\]

Euler's pentagonal/eta theta identity is
\[
\eta(\tau)
=
\sum_{n\ge1}\chi_{12}(n)e^{\pi i n^2\tau/12}.
\]
Setting \(\tau=ix\), \(x>0\), gives
\[
\boxed{\vartheta_\chi(x)=2\eta(ix)}.
\]

From the Dedekind product,
\[
\eta(ix)
=
e^{-\pi x/12}
\prod_{m\ge1}(1-e^{-2\pi mx}).
\]
Every factor is strictly positive for \(x>0\). Therefore
\[
\boxed{\vartheta_{\chi_{12}}(x)>0\qquad(x>0)}.
\]

This closes the open positivity gate in v13.748 §14.

## 2. Positive chi12 and Dedekind kernels [D]

The centered character kernel was
\[
K_\chi(r)
=
e^{|r|/2}\vartheta_\chi(e^{2|r|}).
\]
Hence
\[
\boxed{
K_\chi(r)
=
2e^{|r|/2}\eta(ie^{2|r|})>0
\qquad(r\in\mathbf R).
}
\]

v13.722 established
\[
\Phi(r)>0.
\]
The Dedekind kernel from v13.748 is
\[
\Phi_K=\Phi*K_\chi.
\]
Thus for every real \(r\),
\[
\Phi_K(r)
=
\int_{\mathbf R}\Phi(r-v)K_\chi(v)\,dv>0,
\]
because the integrand is everywhere positive. Therefore
\[
\boxed{\Phi_K(r)>0\qquad(r\in\mathbf R)}.
\]

Together with evenness,
\[
\boxed{
\Xi_K(w)
=
\int_{\mathbf R}\Phi_K(r)e^{wr}\,dr,
\qquad
\Phi_K(r)>0,\quad
\Phi_K(-r)=\Phi_K(r).
}
\]

This is now a proved-positive even bilateral kernel for the centered completed Dedekind function of \(\mathbf Q(\sqrt3)\), not merely a numerically suggested one.

## 3. Exact Euclidean nested-circle coordinate on the cone [D]

For the cone
\[
X^2+Y^2=T^2,\qquad T>0,
\]
a horizontal slice \(T=\rho\) is the Euclidean circle
\[
X^2+Y^2=\rho^2.
\]
Write
\[
\boxed{
X=\rho\cos\theta,\qquad
Y=\rho\sin\theta.
}
\]
For the positive-factor sheet \(Y>0\), \(0<\theta<\pi\).

The arithmetic boost parametrization is
\[
(T,X,Y)=e^{r/2}(\cosh u,\sinh u,1).
\]
Since \(T=e^{r/2}\cosh u\),
\[
\frac XT=\tanh u,\qquad
\frac YT=\operatorname{sech}u.
\]
Therefore the exact conversion between Euclidean circle angle and Lorentz rapidity is
\[
\boxed{
\cos\theta=\tanh u,\qquad
\sin\theta=\operatorname{sech}u.
}
\]
Equivalently,
\[
\boxed{
u=\operatorname{artanh}(\cos\theta)
=\log\cot\frac{\theta}{2}.
}
\]

Thus the original nested circles and the later boost coordinate live on the same cone and are related exactly, but by a nonlinear reparametrization.

## 4. Exact comparison of the two all-frequency families [D/N]

The literal Euclidean angular Fourier family on a circle is
\[
\boxed{e^{im\theta}},\qquad m\in\mathbf Z
\]
(or \(e^{i\omega\theta}\) if a continuous angular frequency is allowed).

The later boost spectral family is
\[
\boxed{e^{i\tau u}},\qquad \tau\in\mathbf R.
\]

Using the exact coordinate change,
\[
\boxed{
e^{i\tau u}
=
\exp\!\left(i\tau\log\cot\frac\theta2\right)
=
\left(\cot\frac\theta2\right)^{i\tau}.
}
\]

Therefore:

[N] A constant-frequency boost mode is **not** a constant angular-frequency mode on the nested Euclidean circles.

Indeed,
\[
\frac{d\theta}{du}=-\operatorname{sech}u=-\sin\theta,
\]
so uniform translation in \(u\) produces nonuniform angular motion in \(\theta\).

This is the exact boundary between the original visual helix picture and the later arithmetic spectral geometry.

## 5. What is literally realized from the original prompt [D/I]

The original prompt proposed:
\[
e^{i\pi t}
\to
\text{one-frequency 3D helix}
\to
\text{nested circles/all frequencies}
\to
\text{screw function}.
\]

The following portions now have literal mathematical realizations:

1. **Nested circles on the cone [D].** Horizontal sections \(T=\rho\) are exactly circles \(X^2+Y^2=\rho^2\).

2. **An all-frequency spectral family [D].** The boost fiber carries the complete Fourier family \(e^{i\tau u}\).

3. **Pairing under cone reflection [D].** \(u\mapsto-u\) sends \(\tau\mapsto-\tau\), producing the exact two-state carrier
\[
V_\tau\simeq\mathbf1\oplus\chi_{12}.
\]

4. **Screw-current endpoint [D].** Independently, the Suzuki lane proves
\[
\mathscr W=-g'',\qquad
Q_{\rm Suz}[DF]=Q_{\rm Weil}[F].
\]

The following stronger identification is false without reparametrization:

[N]
\[
e^{im\theta}\neq e^{i\tau u}
\]
as constant-frequency families under a linear identification of \(\theta\) and \(u\).

Instead the exact bridge is the nonlinear map
\[
u=\log\cot(\theta/2).
\]

## 6. Geometric helix versus arithmetic boost orbit [D/N]

A standard Euclidean helix over nested circles has a linear angular law
\[
\theta(t)=\omega t+\theta_0
\]
together with an axial/radial law.

A Pell/boost orbit has
\[
u(t)=u_0+bt.
\]
In circle angle this becomes
\[
\boxed{
\theta(t)
=
2\arctan(e^{-u_0-bt}),
}
\]
which is not linear in \(t\).

For the discrete Pell return,
\[
u_n=u_0+nR_{12},
\]
so
\[
\boxed{
\theta_n
=
2\arctan(e^{-u_0}\varepsilon^{-n}),
\qquad
\varepsilon=2+\sqrt3.
}
\]

Thus a Pell orbit, viewed in the original Euclidean circle angle, is a geometrically compressed winding toward a cone generator rather than a uniform Euclidean helix.

[I] The original helix intuition correctly identified a frequency-bearing fibered structure on the cone, but the arithmetic dynamics selects Lorentz rapidity as the additive coordinate, not Euclidean polar angle.

## 7. Consequence for the screw interpretation [I/G]

Suzuki's screw function is naturally translation-based in an additive real variable. The cone's rapidity \(u\) is likewise additive under boosts:
\[
u\mapsto u+b.
\]
This makes the later boost-Fourier realization structurally closer to the analytic screw formalism than the literal Euclidean angle \(\theta\), whose boost evolution is nonlinear.

[G] This is a structural compatibility statement, not a proof that Suzuki's screw variable is identical to the cone boost variable. The exact established screw/Weil current remains the separate scale-current identity from v13.744–747.

## 8. Closed and open gates

**Closed here:**
\[
\boxed{\vartheta_{\chi_{12}}(x)=2\eta(ix)>0}
\]
and hence
\[
\boxed{K_\chi>0,\qquad \Phi_K>0}.
\]

Also closed:
\[
\boxed{
\cos\theta=\tanh u,\quad
\sin\theta=\operatorname{sech}u,\quad
u=\log\cot(\theta/2)
}
\]
as the exact nested-circle/boost coordinate bridge.

**Remaining open comparison gate:** determine whether the original multi-helix picture admits a natural reparametrized helix/screw embedding in which \(u\), rather than \(\theta\), is the uniform phase coordinate, and whether that representation can be connected directly to Suzuki's screw kernel before projection to the common scale current.

---

**Checkpoint conclusion.** Two substantial gates close simultaneously. The primitive chi12 theta kernel is exactly twice the Dedekind eta function on the positive imaginary axis, so the centered Dedekind kernel for \(\mathbf Q(\sqrt3)\) is rigorously positive. Separately, the original nested-circle geometry and the later boost-Fourier geometry are now connected by the exact nonlinear map \(u=\log\cot(\theta/2)\). The original all-frequency helix intuition is therefore neither merely analogy nor literally identical to the boost spectrum: it is an exact cone geometry whose natural arithmetic spectral coordinate is a nonlinear rapidity reparametrization of the Euclidean circle angle.
