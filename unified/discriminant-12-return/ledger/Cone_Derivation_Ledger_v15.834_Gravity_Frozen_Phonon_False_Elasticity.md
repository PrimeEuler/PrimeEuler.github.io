# Cone Derivation Ledger v15.834 — Gravity: frozen-phonon gauge artifact creates fictitious elastic gradient energy

**Date:** 2026-11-12 US Eastern. **Parents:** frozen original K4 solid action v14.935, v15.830 missing-shear false optical signal, v15.832 warning about the nonzero K4 solid background, and v15.833 action-level full coupled pure-gauge Ward. **Immediately prewrite live HEAD:** 094b423b49ef1bb47a9a193f83fc5cb65fec8f11; target absent. Strict additive only; protected Suzuki and gravity originals unchanged.

**Status:** [D] exact spurious elastic invariant when a coordinate transformation is applied to the metric but not to the solid phonon; [D] exact cancellation when the material scalar is correctly transformed; [N] no new elastic scale, curvature or Cone-specific force; [O] complete physical-source finite-detector gauge covariance and remote calibrated instrument.

## Gate 461 — quantitative negative control for incorrectly frozen material coordinates

Use a pure *spatial* passive coordinate transformation with zero time shift **T=0** and a transverse gauge displacement **U_y=u cos(kx)**, U_x=U_z=0. The original physical solid is isotropic and free of shear. However the pure-gauge spatial metric perturbation has **h_xy=h_yx=−∂xU_y=+uk sin(kx)**.

The correct material scalar perturbation is **π_y=−U_y**, so the internal-metric perturbation obeys

**E_ij=a²δB^ij=−h_ij+∂iπ_j+∂jπ_i=0**,

and the quadratic original K4 shear invariant is **J^(2)=tr(E_TF²)/9=0**.

Now deliberately make the inconsistent choice **π_y=0** while retaining the gauge-generated metric shear. The false strain becomes **E_wrong,xy=E_wrong,yx=−uk sin(kx)**, so the exact original invariant (not a replacement ansatz)

**J=tr(B²)/(tr B)²−1/3**

has quadratic coefficient

**J^(2)_wrong=2 u² k² sin²(kx)/9 >0** at generic x.

For **u=1/10**, **k=2**, **x=π/4**, its false value is exactly **2/225≈0.0088888889**. The spurious conformal matter action density includes

**Δℒ_false=−C a² η_s J^(2)_wrong**.

It has precisely the appearance of a physically relevant *elastic gradient energy*, despite being entirely a consequence of holding the material-coordinate field fixed during a coordinate change. At η_s≠0 this could masquerade as a new operator or a source/detector phase effect if one did not enforce the solid's Stückelberg transformation.

## Gate 462 — what is proved, and what is not

**Positive:** exact algebraic gauge-invariant subtraction removes the false internal shear; the first physically nontrivial shear sector must involve the correct combined spatial metric and phonon displacement, not either alone. This tightens the earlier v15.830 false-optical-signal gate by exhibiting the same failure mechanism directly in the **original matter action**.

**Negative:** a new stiffness, mass gap, 1/4 mesh scale, or gravitational coupling cannot be read off from this gauge-dependent (u²k²) term. The artificial amplitude u is a coordinate-generator parameter, and the entire effect disappears with consistent field transformations.

**Reproducer:** research-notes/k4_solid_frozen_phonon_false_shear_v15_834.py, additive commit **7a7c111a859ce8bc66df202fa1a0573b7b0a6aeb**. The local SymPy script was executed to PASS for exact nonlinear trace ratio expansion through ε² and the 2/225 rational witness. The committed bytes are pending independent external audit. No historical asset edits.

**HANDOFF — external audit:** rederive the original v14.935 J quadratic expansion, exact h_xy pure-gauge sign, π_y=−U_y cancellation and the false u²k² elastic energy; ensure no factor-of-two confusion between off-diagonal strain and trace(E²). Cross-check v15.833's ten-component stress transformation and the on-shell pure-gauge Einstein+solid Ward.

**NEXT:** carry the full material-coordinate transformation through the sourced physical K4 ADM lapse/shift and optical detector for a nontrivial physical mode, and construct a remote source-to-detector propagation control. Matched ordinary Einstein–Hilbert plus elastic solid remains **identical**, so no Cone-only residual is implied.
