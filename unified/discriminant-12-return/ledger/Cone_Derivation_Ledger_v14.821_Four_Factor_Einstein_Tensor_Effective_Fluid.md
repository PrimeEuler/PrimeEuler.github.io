# Cone Derivation Ledger v14.821 — Four-factor Einstein tensor and conditional FLRW fluid

Date 2026-10-24. Gravity/combinatorics lane. Parents v14.818–820. Research note research-notes/Four_Factor_Einstein_Tensor_Effective_Fluid.md (commit 80a040461b615880f3889c534515ddd15a62a82a). Prewrite live HEAD 80a040461b615880f3889c534515ddd15a62a82a; latest ledger v14.820. Additive only, Suzuki/far-tail untouched.

## Exact Einstein tensor [D]
For k=4, \(ds²=e^r(dt²-d\mathbf z²)\), \(t=(\sqrt3/2)r\), and v14.820 Ric_tt=0, Ric_ij=2δij/3, scalar R=-2e^{-r}. Hence
\[
\boxed{G_{\mu\nu}=\operatorname{diag}(1,-1/3,-1/3,-1/3)}
\]
in conformal coordinates. In the orthonormal frame this is \(G_{\hat a\hat b}=e^{-r}\operatorname{diag}(1,-1/3,-1/3,-1/3)\).

## Conditional fluid source and energy conditions [D/O]
If, and only if, one interprets these factor coordinates as physical spacetime and imposes Einstein equations \(G_{\mu\nu}=\kappa T_{\mu\nu}\) with Λ=0 and independent κ>0, then effective perfect-fluid energy density and pressure are
\[
\rho=e^{-r}/\kappa,\qquad p=-\rho/3.
\]
Null, weak and dominant energy conditions hold; strong energy condition is saturated (\(\rho+3p=0\)). κ includes the independently unspecified Newton coupling. Thus w=-1/3 is an exact *conditional effective-source characterization*, not a physical derivation of G or an identification with observed cosmology.

Writing \(\tau=\sqrt3e^{r/2}>0\) gives
\[
ds²=d\tau²-\frac{\tau²}{3}d\mathbf z²,
\quad a(\tau)=\tau/\sqrt3,\quad H=1/\tau,
\]
a spatially flat, linearly expanding FLRW metric in the mathematical model. It is not de Sitter; it has curvature divergence as τ→0 and no established identification with cosmological data.

## Next discriminating gate [O]
Determine whether a physically motivated action actually derives the k=4 factor Hessian metric and the corresponding w=-1/3 source, with covariant physical coordinate/unit assignments; do not infer κ from a metric reverse-engineered via Einstein equations. Audit should independently verify Christoffel/Ricci, Einstein tensor, conservation and energy-condition signs.

Flags: Einstein_tensor_k4=EXACT; conditional_perfect_fluid_w=-1/3; FLRW_linear_expansion=EXACT_MATHEMATICAL; observed_GR_solution=NOT_ESTABLISHED; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: gravity-curvature-source-review
parent: v14.821
status: open
action: Independently verify Einstein tensor, orthonormal-frame conversion, FLRW cosmic-time rewrite, equation-of-state and energy conditions; verify no physical G or cosmology claimed.
deliverable: scoped audit verdict without Suzuki/far-tail changes.
