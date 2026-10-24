# Cone FLRW with propagating spin-2: relaxed constraint baseline

2026-10-24. Gravity lane. Parents v14.821–825. Protected Suzuki/far-tail untouched.

## Unconstrained metric and Cone background [D]
Remove the exact multiplier equation g=h(X) of v14.825. Keep the diffeomorphism-invariant Einstein + three comoving scalar fluid action from v14.822:
\[
S[g,\phi]=\int d^4x\sqrt{-g}[R/(2\kappa)-Cb^{2/3}],\quad b=\sqrt{\det(-g^{\mu\nu}\partial_\mu\phi^I\partial_\nu\phi^J)},\quad \kappa,C>0.
\]
Four positive AM–GM factor fields X^A may serve as *reference coordinates* for the chosen FLRW background via its k=4 Hessian metric h(X), but no equation g=h(X) is imposed, and the X fields are not propagating dynamical fields of this baseline action. They therefore do not select the metric. Choose \(\phi^I=z^I\), κC=1, and background metric g=dτ²-(τ²/3)d\mathbf z² with τ=√3 exp(r/2) and z the three factor-shape coordinates. This background is an exact solution as in v14.822, and locally isometric to h(X).

## Linear spin-2 sector [D]
Set g_ij=-a(τ)²(δij+γij), ∂iγij=0, γii=0 and a=τ/√3. With standard tensor perturbation conventions, and no TT anisotropic stress in the perfect-fluid source, expansion to quadratic order (with matter perturbations properly constrained) yields
\[
S_{TT}^{(2)}=\frac1{8\kappa}\int dτ\,d³z\,a³[\dotγ_{ij}\dotγ_{ij}-a^{-2}\partial_kγ_{ij}\partial_kγ_{ij}].
\]
For κ>0 this contains two positive-kinetic tensor helicities with luminal principal propagation and no tensor mass term. Their EOM are
\[
\ddotγ_{ij}+3H\dotγ_{ij}-a^{-2}\nabla²γ_{ij}=0,\quad H=1/τ.
\]
In conformal time η, a'=a c, with c=sqrt(κC/3) (and for κC=1, c=1/√3). For Fourier modes μ=aγ, \(\mu_q''+(q²-c²)\mu_q=0\). Long-wavelength growing μ does NOT by itself imply ghost kinetic energy; γ has a constant and decaying solution at q=0. Independent tensor dynamics thus survive.

## Selection/stability limits [O]
This is a *relaxed background correspondence*, not a dynamical theory of AM–GM factor fields; it evades the frozen-graviton problem by not constraining the metric to equal their Hessian. Full scalar/vector sector stability of the unusual w=-1/3 comoving-fluid action is not established. In fact the barotropic adiabatic sound speed c_s²=dp/dρ=w=-1/3 is negative, suggesting a short-scale longitudinal gradient instability for the simple perfect-fluid model, even while the tensor sector is well behaved. Hence do NOT label this full theory healthy. The factor-coordinate identification remains conditional; κ and C selected independently/matched; no Newton G prediction.

Next: derive the longitudinal scalar quadratic action and its dispersion; seek stable elastic/anisotropic media or constrained field actions with w=-1/3 background but c_s²>=0 while preserving positive tensor kinetic energy.
