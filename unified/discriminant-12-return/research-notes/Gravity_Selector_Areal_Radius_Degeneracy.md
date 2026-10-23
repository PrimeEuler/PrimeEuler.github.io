# Gravity selector test: areal-radius canonical map and cancellation of G

Date 2026-10-23. Parents v14.696, v14.731–739. Gravity-lane self-work; Suzuki sandbox not used.

## Canonical areal-radius map [D]

Taub–NUT areal radius \(R=\sqrt{r^2+l^2}\) implies \(p_R=p_r\,dr/dR=p_r R/r\) to preserve \(p_rdr=p_RdR\). Using the metric-derived TN radial HJ with \(\Sigma=r^2+l^2\), \(f=(r^2-2mr-l^2)/\Sigma\), \(s=2\varepsilon l\),
\[
p_r^2=\varepsilon^2/f^2-1/f-(J^2-s^2)/(\Sigma f).
\]
Symbolic expansion after canonical momentum transformation, and expressing the inverse-radius powers in R (since \(1/r=1/R+O(R^{-3})\)), gives
\[
p_R^2=(\varepsilon^2-1)
+\frac{2m(2\varepsilon^2-1)}R
+\frac{-J^2+(9\varepsilon^2-3)l^2+(12\varepsilon^2-4)m^2}{R^2}
+O(R^{-3}).
\]
Hence matching the standard MIC radial momentum at fixed E,κ,J leaves \(\Delta_R=(9\varepsilon^2-3)l^2+(12\varepsilon^2-4)m^2\), generically nonzero. This is NOT a global canonical no-go: another nontrivial symplectic/time transformation could modify the comparison. It refutes the narrower hypothesis that merely choosing the geometrically natural areal radius automatically erases the radial mismatch.

## A selector obstruction from the exact coupling product [D]

With \(\widetilde M=c^2l/G\),
\[
\alpha_G(\mu)=G\mu^2/(\hbar c),\quad
\alpha_G(\widetilde M)=G\widetilde M^2/(\hbar c).
\]
Consequently
\[
\alpha_G(\mu)\alpha_G(\widetilde M)
=(\mu cl/\hbar)^2=n^2/16,
\quad \partial_G(\alpha_G(\mu)\alpha_G(\widetilde M))|_{\mu,l}=0.
\]
The lattice fixes the product while the individual couplings remain unconstrained; varying G at fixed geometric μ,l changes the allocation of the product but not the lattice or the TN geometric action. The radius mismatch also depends on geometric m,l,ε,J, not G independently when those geometric lengths are held fixed. Reexpressing m=GM/c² introduces G together with a freely specified source mass and therefore does not constitute selection of G.

More generally parameterize positive couplings on the gravitational n-th rung by \(\alpha_1=(|n|/4)e^\psi,\ \alpha_2=(|n|/4)e^{-\psi}\). The pair constraint is independent of ψ. A physical selector must determine ψ (and anchor the physical mass/length conversion) using a separate dynamical or boundary principle. Analogously the EM half-lattice fixes a product, not the fine-structure constant alone. A shared lattice is not a coupling-hierarchy law.

## What a viable selector must satisfy [testable requirements]

1. Supply a physically specified, non-arbitrary boundary or action principle that breaks the continuous pair-rescaling degeneracy; avoid selecting ψ by tuning a parameter to the observed alpha or G.
2. Predict a dimensionless ratio without using the target coupling covertly in its inputs. State an independently measurable quantity or falsifiable outcome.
3. Survive changes of radial coordinates and gauge/Misner-patch representation; a coordinate coefficient by itself is not a selector.
4. Respect distinct EM internal U(1) and TN timelike-fibration global constraints; if periodic TN time is required, state its causality assumptions.
5. Distinguish an initial-condition hypothesis (v14.696), an EFT matching/renormalization condition, and an independently derived spectral/boundary eigenvalue. Only the latter two can become predictive with specified UV/IR inputs.

**Verdict:** angular/common monopole period lattice VERIFIED; areal-radius map changes but does not generically remove radial mismatch; neither selects G or the alpha/alpha_G hierarchy. The selector remains OPEN with explicit one-parameter degeneracy and falsifiable requirements. No new sandbox assignment and no Suzuki objects touched.
