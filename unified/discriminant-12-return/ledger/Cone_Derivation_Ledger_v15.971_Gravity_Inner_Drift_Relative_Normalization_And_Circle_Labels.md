# Cone Derivation Ledger v15.971 — Inner kinetic drift: ratio normalization and naming of three distinct circles

**Date:** 2026-11-14 Eastern. **Gravity lane.** **Owner observation:** outer n+1 transition circle seems EM; "1/2 Casimir" Jzy convergence appears observable; the inner "1/4 Casimir circle" drift in v15.970 was unexpectedly large. **Parents:** v15.900 conditional radial rotor control; v15.924 and Paper C fixed outer Schwinger null circle; v15.934 exact inner/EM Casimir/outer three-circle distinction; v15.951 common diameter; v15.955 (reissued v15.968) transverse Jxy exact state midpoint; v15.969 formal Casimir-to-kinetic hypothesis; v15.970 three inertial circle stress tests. **Live HEAD immediately prewrite:** 101333b5ed54146efc4309257764205a4d77554a; target absent; additive-only, no Suzuki/Audit/Sandbox changes.

**Crucial terminology:** The **outer** circle radius R_o=D/2 is the fixed Schwinger transition shell and geometrical null-section; the **intermediate** radius R_C,EM=sqrt(D²−1)/2 is the genuine EM SU2 Casimir-radius construction; the **inner** radius R_i=sqrt(D−1) is a product/chord/rest-circle proposal for the primitive pair (D−1,1), and is **not itself the odd-quarter gravity Casimir operator**. For the shared-D quarter endpoint pair (D−1/2,1/2), the product/chord radius is R_i,q=sqrt(D/2−1/4). The **separately chosen** geometric quarter Casimir circle has radius sqrt(D²−1/4)/2, which is again distinct from the **formal odd-quarter label** C_q=(2D−1)(2D+3)/16. Do not conflate these.

**Notation:** No indexed repository definition of a distinct "Jzy Casimir" is found. Known objects are Jz, Jy, Jx²+Jy², and total J². If Jzy means a specific generator combination, its definition is still required before assigning an observable. Existing exact identity Jx²+Jy²=J²−Jz² describes a state-dependent transverse *moment*, not an additional central Casimir.

## Gate 752 — decompose the three absolute conditional kinetic profiles

Use the explicitly **hypothetical** common-mass, common-length thin-ring relation E=ℏ² C/(2Mℓ_*² R²), with EM **C_e=(D²−1)/4** and **formal**, not physically derived, quarter **C_q=(2D−1)(2D+3)/16**. Let normalized energies e=(2Mℓ_*²/ℏ²)E_e, g=(2Mℓ_*²/ℏ²)E_q. For D≥2:

- **Shared outer inertia** R_e²=R_q²=D²/4: e=(D²−1)/D², g=(2D−1)(2D+3)/(4D²). Difference g−e=(4D+1)/(4D²), ratio g/e=(2D−1)(2D+3)/[4(D−1)(D+1)] →1.
- **Separate geometric Casimir-radius inertia** R_e²=(D²−1)/4, R_q²=(D²−1/4)/4: e=1, g=(2D+3)/(2D+1). Difference g−e=2/(2D+1), ratio g/e→1. The e=1 is tautologically built from choosing inertia proportional to C_e, not a derived physical kinetic metric.
- **Separate inner product/chord inertia** R_e²=D−1, R_q²=D/2−1/4: e=(D+1)/4, g=(2D+3)/4. Difference g−e=(D+2)/4 grows linearly but the **relative ratio** g/e=(2D+3)/(D+1)→2, not infinity.

These are three *different imposed mechanical models*, each with independent candidate radii derived from the same static Cone construction. The striking inner *absolute* difference arises because C_e and C_q grow O(D²) while the inner inertias grow only O(D). In the outer and Casimir-circle hypotheses inertias instead scale O(D²). No physical gravitational Casimir evolution or measured energy drift was observed.

## Gate 753 — why Jxy remains the correct established observable comparator

The quarter-interleaved row midpoint at fixed D reproduces the **EM transverse moment** Jx²+Jy² exactly after subtracting the EM +1/4 centered-edge correction, as proved in v15.955. This is a direct standard SU2 operator correspondence, not a new central quantum invariant and not an identification of the product/chord circle with the gravity Casimir. The 1/2 geometric vertex and 1/4 geometric vertex are mesh **coordinates**, while the EM Casimir completion +1/4 and formal odd-quarter Casimir labels are algebraically distinct items. The user may be referring to another Jz/Jy combination; do not silently assign a new Jzy operator.

**Verdict:** The surprise is resolved by normalized scaling of the conditional kinetic model: the inner gap's linear growth is driven by the **chosen inertia radius**; relative ratio saturates at 2. This supports neither a runaway gravity Casimir nor a field-selected inertia. No new physical observable, dynamic kinetic term or gravitational Casimir is obtained.

**Reproducer:** `research-notes/k4_kinetic_drift_relative_ratios_v15_971.py`, commit **101333b5ed54146efc4309257764205a4d77554a**. Exact symbolic formulas and asymptotic limits checked locally using SymPy; script deposited additively. **Independent Audit pending.**

**NEXT:** If a physical connection makes outer ring an EM transition spectrum and quarter sector an independently measured kinetic response, build an explicit physical operator with a kinetic coefficient and determine whether the measured observable corresponds to inner product circle, geometric Casimir circle, or transverse Jxy moment. Compare dimensionless energy **ratios**, not only differences, with ordinary rotor controls. Without a field-derived action, do not relabel these circles as physical.
