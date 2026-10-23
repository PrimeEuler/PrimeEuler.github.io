# Cone Derivation Ledger v14.779 — Compact-circle physical boundary source and susceptibility

Date: 2026-10-23. Lane gravity. Parents v14.620, v14.760–761, v14.773–778. Research note: research-notes/Gravity_Compact_Phase_Boundary_Source_Action.md, committed 0019446a834e6d823905a5ea6ea99e3838917062. Live HEAD before ledger write: 0019446a834e6d823905a5ea6ea99e3838917062. Additive only, Suzuki and far-tail untouched.

## Compact phase boundary action [D, conditional mathematical model]

Consider a phase field θ(s)∈R/(2πZ) on a proper-length interval s∈[0,L], pinned at θ(0)=0, with real lift chosen near θ=0. Define static energy
\[
E_{\kappa,j}[\theta]=\frac{\kappa}{2}\int_0^L(\theta')^2ds-j\sin\theta(L), \quad \kappa>0.
\]
The boundary source is genuinely periodic and bounded; j is calibrated in energy units and κ has energy×length units.

The Euler–Lagrange equation is θ''=0, with natural boundary condition \(\kappa\theta'(L)=j\cos\theta(L)\). Writing Θ=θ(L), the near-zero stationary branch solves
\[
\frac{\kappa}{L}\Theta=j\cos\Theta.
\]
Its zero-source susceptibility and minimized-energy curvature are
\[
\boxed{\chi=\left.\frac{d\Theta}{dj}\right|_0=L/\kappa},\qquad
\boxed{\left.\frac{d^2E_{\min}}{dj^2}\right|_0=-L/\kappa}.
\]
The corresponding boundary Dirichlet-to-Neumann stiffness is κ/L.

## The selector test [D/O]

For two sectors with common circle period, one calibrated physical L and common j,
\[
\boxed{\chi_G/\chi_{\rm EM}=\kappa_{\rm EM}/\kappa_G}.
\]
Nothing in phase compactness or a common ħ fixes κ_EM/κ_G. A desired factor-four response obtained by setting κ_G=κ_EM/4 is an assumption, not the consequence of the half-grid. On a distinct closed spatial ring, integer winding m has minimum energy \(E_m=2\pi^2\kappa m^2/L\), displaying the same free stiffness despite fixed topological winding.

The compact field is a 1D effective model and has not been derived from Maxwell, Einstein-Hilbert, CFS, or Cone physical state equations. No identification between divisor-pair and Suzuki/Weil currents is made. G and the physical hierarchy remain open.

## Next falsifiable gate [O]

Derive the sector Dirichlet-to-Neumann coefficients κ_i from a single microscopic/bulk action with common source normalization and a regulator/physical wall fixed independently of G. Test whether the quarter-grid mapping forces κ_G/κ_EM under this derivation and confirm the physical response is invariant under permissible reparametrizations and probe changes.

Flags: compact_circle_source_action=DEFINED; variational_boundary_response=EXACT; stiffness_ratio_free=EXACT; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: gravity-only-variational-audit
parent: v14.779
status: open
action: Independently verify variational boundary term, small-source branch, energy curvature, and closed-ring winding formula, and check the conclusion that κ is not fixed by circle topology. Leave Suzuki and far-tail work untouched.
deliverable: scoped audit verdict.
