# Cone Derivation Ledger v15.1382 — On-shell hyperboloid waves activate the Weyl–EM area interaction

**Date:** 2026-11-24 Eastern. **Lane:** Gravity/Cone. **Status:** [N/PASS, leading order] the v15.1381 proposed Weyl–Maxwell–H² area-form interaction has a nonclosed curvature-contracted two-form even when **both hyperboloid coordinates satisfy the leading-order free massless field equations**, in a genuine vacuum linearized Einstein TT gravitational wave; [NEGATIVE] still a *chosen extra EFT operator* with free coefficient and independent target field, no action-derived quarter-grid coupling, finite-energy global solution or measured observable. All commits additive. **Preledger inspected HEAD:** 46f25f0cccd7fd040f252058ea0eb99c1d2d409b.

## Gate 1292 — remove the externally pinned static target objection

In local Minkowski spacetime with signature (-+++), use the on-shell vacuum TT plus gravitational wave `h_xx=epsilon cos(omega(t-z))`, `h_yy=-h_xx`; it solves the vacuum linearized Einstein equation and its first-order Weyl equals the linearized Riemann tensor. Instead of the static externally specified sigma-map from v15.1381, take **two independent massless waves**

`u=a sin[m(t-x)]`, `v=b sin[k(t-y)]`.

Then `Box u=Box v=0` exactly. These are solutions of the linearized free sigma-model field equations about the hyperboloid apex `u=v=0`. Their finite-amplitude nonlinear H² sigma equations do not necessarily hold; this gate keeps strictly the leading O(ab) target area response, where `B=du wedge dv + O(a³b,ab³)`. All curvature--sigma cross-coupling backreaction is higher order and ignored. A complete Einstein–Maxwell–H² solution requires a subsequent coupled perturbation calculation.

## Gate 1293 — geometric source does not collapse on shell

Calculate the full first-order Riemann/Weyl tensor directly from the TT metric `h_xx=h, h_yy=-h` using

`R_mu nu rho sigma=1/2(∂rho∂nu h_mu sigma+∂sigma∂mu h_nu rho−∂sigma∂nu h_mu rho−∂rho∂mu h_nu sigma)`.

Build `B_mu nu=∂mu u∂nu v−∂nu u∂mu v` at O(ab), and `K_mu nu=C_mu nu rho sigma B^{rho sigma}` using (-+++) index signs. Evaluate its exterior derivative `dK` independently for all four ordered triple components. The exact leading expressions obtained and passed are

`(dK)_{txy}=−ab epsilon k m omega² [k sin(k(t−y)) cos(m(t−x))−m sin(m(t−x)) cos(k(t−y))] cos(omega(t−z))`,

`(dK)_{txz}=+ab epsilon k m omega² [k sin(k(t−y)) cos(m(t−x))+m sin(m(t−x)) cos(k(t−y))] cos(omega(t−z))`,

`(dK)_{tyz}=+(dK)_{txz}`, and `(dK)_{xyz}=−(dK)_{txy}`.

These are generically nonzero, even though the actual gravitational wave and both independent internal waves are separately on shell at leading order. Thus the Weyl-contracted target-area two-form is **not closed even on the leading free internal and gravity mass shells**. Consequently the naive potential shift that removes bare `F·B` cannot remove `F·(C_Weyl·B)` by a local one-form with dA_shift=K. This does **not** settle the entire EFT operator-redundancy classification or determine measurable output, nor does it establish that the stated waves solve the full coupled equations.

**Actual local executed test:** `/mnt/data/cone_gate/quarter_weyl_onshell_wave_v15_1382.py`, Python SymPy, PASS all four dK triples and exactly zero Box u/Box v. **Additive GitHub source:** `research-notes/k4_quarter_hyperboloid_weyl_onshell_v15_1382.py`, SHA **46f25f0cccd7fd040f252058ea0eb99c1d2d409b**, mathematically equivalent and awaiting independent exact committed-byte replay.

## Next physical gates and audit

**Audit:** independently check the full TT Weyl/Riemann contractions and dK component signs, flat-wave wave equations, leading-order H² metric expansion and dimensional coefficient. Check whether the proposed operator is independent under integration by parts, Maxwell+sigma on-shell EOM, and allowed EFT field redefinitions beyond the simplest shift. Also verify no exact physical quarter-shell or SI scale is claimed.

**NEXT:** derive full H² sigma-model field EOM with the chosen Weyl coupling, positive energy/hyperbolicity and consistent initial data, then a conserved Maxwell source and same-event photon/clock response in a dynamically prepared target background. Compare to BOTH (a) the original Einstein–Maxwell+identical K4 baseline and (b) the standard identical **enlarged EFT** comparator. A truly quarter-grid-specific prediction would require a field/parameter selector the generic enlarged EFT does not possess. The fixed quarter value r=1/4 cancels from normalized B and still supplies no independent coupling or observable.
