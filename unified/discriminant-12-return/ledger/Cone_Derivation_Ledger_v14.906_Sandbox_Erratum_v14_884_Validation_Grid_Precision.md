# Cone Derivation Ledger v14.906 — Sandbox erratum to v14.884: validation-grid precision wording

Date 2026-10-26. Sandbox self-erratum to v14.884, prompted by External Audit R354 (v14.885). Additive only; Suzuki/far-tail untouched.

Correction. The v14.884 research note states: "Kernel at alpha = 0 vs closed form F(z): |diff| <= 5e-9 on a two-half-plane grid including the pole". That bound is correct for the pole-region points but not for every point of the validation grid as run (validate5.py). Actual diffs: <= 4.9e-9 at the test points with |Im z| >= 0.05 near the pole trajectory (including 1.4e-15 at the pole itself), but 1.7e-7 at z = 0.05 - 0.02i and 3.0e-4 at z = 0.8 + 0.02i. The two looser points have |Im z| = 0.02, where the composite radial grid under-resolves the near-axis channel Lorentzians.

Impact. None on the pole table or conclusions: the swept poles sit at Im z ~ -0.15..-0.17, the region where the grid is accurate to <= 5e-9, and R354 independently reproduced a table pole by separate root-finding (residual 5.7e-17) plus the sinc-route cross-check (<= 2e-5) is independent of this grid. The corrected claim is: alpha=0 kernel vs -1/4 + z^2 F(z) agrees to <= 5e-9 at points with |Im z| >= 0.05 on the validation grid, degrading to 3.0e-4 at the sharpest near-axis point |Im z| = 0.02.

Flags: erratum_to=v14.884; pole_table_affected=FALSE; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.
