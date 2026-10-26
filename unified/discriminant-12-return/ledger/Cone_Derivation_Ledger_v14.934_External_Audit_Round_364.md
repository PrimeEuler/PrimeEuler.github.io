# Cone Derivation Ledger v14.934 — External Audit Round 364

**Date:** 2026-10-26
**Track:** External Audit (verification round)
**Status:** [V] Independently verified `v14.932` and `v14.933`: exact transverse and longitudinal matter-displacement mode evolution for the K4 elastic solid on the fixed, prescribed FLRW background.
**Parents:** v14.932, v14.933. This auditor's own prior entry: v14.931 (Round 363).

---

## v14.932 — Transverse elastic phonon evolution on K4 expanding background. VERIFIED by independent `sympy` re-derivation, exact match.

This extends the flat-space transverse/longitudinal phonon calculation (`v14.927`) to the actual FLRW background `a(τ)=τ/\sqrt3`, holding the metric fixed (test-field matter perturbation, not yet coupled to metric perturbations), claiming `S_\perp^2=(C/3)\int d\tau\,d^3z\,a^3[\dot\pi^2-(2\eta/(3a^2))(\partial\pi)^2]`.

I re-derived this completely independently in `sympy`, building `B^{IJ}=a^{-2}F^\top F-vv^\top` explicitly from the stated metric `g=\mathrm{diag}(1,-a^2\delta_{ij})` (confirming this is the correct pullback form, not assuming it) for a transverse perturbation `\pi_y=f(\tau,z_x)`, then expanding `\sqrt{-g}\cdot(-Cb^{2/3}(1+\eta J))=a^3\cdot L_m` to quadratic order in a bookkeeping parameter. The background (`\epsilon^0`) term reproduces `-Ca` exactly (i.e. `\rho a^3=Ca^{-2}\cdot a^3=Ca`, consistent with the already-audited `v14.924` background), and the quadratic (`\epsilon^2`) term reproduces `Ca^3\dot f^2/3-2Ca\eta f'^2/9` **exactly** — zero symbolic residual against the claimed action.

From this action I independently derived the Euler–Lagrange equation (`d/d\tau(\partial L/\partial\dot\pi)-\partial_i(\partial L/\partial\partial_i\pi)=0`) and confirmed it gives exactly `\ddot\pi_k+3H\dot\pi_k+(2\eta/3)(k^2/a^2)\pi_k=0`, which substituting `a=\tau/\sqrt3,H=1/\tau` becomes `\ddot\pi_k+(3/\tau)\dot\pi_k+(2\eta k^2/\tau^2)\pi_k=0` exactly as claimed. Plugging in the Euler trial solution `\pi=\tau^s` and solving the indicial polynomial independently in `sympy` gives `(s+1)^2=1-2\eta k^2` exactly, matching the claimed exponents `s=-1\pm\sqrt{1-2\eta k^2}`. I checked the sign claim by direct case analysis: for `k=0`, `s\in\{0,-2\}` (the stated "constant translation and `\tau^{-2}` mode"); for any `k>0,\eta>0`, whether the discriminant `1-2\eta k^2` is positive (giving two real roots, both `<0` since `\sqrt{1-2\eta k^2}<1` strictly when `k>0`) or negative (giving complex roots with `\mathrm{Re}\,s=-1<0`), `\mathrm{Re}\,s<0` holds in every case — confirming "for `\eta>0` and `k>0`, `\mathrm{Re}\,s<0`" exactly, with no exceptions. The high-`k` oscillatory `\tau^{-1}`-envelope claim follows immediately since `\mathrm{Re}\,s\to-1` for large `k`.

The entry's own scope caveat — that this is a fixed-background material-mode calculation, not a coupled gravitational vector/shift reduction, and does not resolve the already-independently-confirmed Pantheon+ observational tension — is accurate and appropriately limited.

## v14.933 — Longitudinal fixed-background phonon decay. VERIFIED by independent `sympy` re-derivation, exact match.

Companion to `v14.932` for the longitudinal sector, claiming `S_L^2=(C/3)\int a^3[\dot\pi_L^2-c_L^2a^{-2}(\partial\pi_L)^2]`, `c_L^2=-1/3+8\eta/9` (the same acoustic coefficient independently confirmed flat-space in `v14.927`), giving EOM `\ddot\pi_{L,k}+(3/\tau)\dot\pi_{L,k}+[(8\eta/3-1)k^2/\tau^2]\pi_{L,k}=0` and exponents `s=-1\pm\sqrt{1-(8\eta/3-1)k^2}`.

I re-derived the full quadratic action independently in `sympy`, this time with a longitudinal perturbation `\pi_x=f(\tau,z_x)` substituted into the same `B=a^{-2}F^\top F-vv^\top` construction, and the resulting quadratic term reproduced `Ca^3\dot f^2/3-8Ca\eta f'^2/27+Caf'^2/9` **exactly**, which algebraically is exactly `(C/3)[a^3\dot f^2-a\,c_L^2\,f'^2]` with `c_L^2=8\eta/9-1/3` — zero residual against the claimed action and consistent with the already-independently-verified flat-space `c_L^2` from `v14.927`. Deriving the Euler–Lagrange equation from this action independently gives exactly the claimed EOM (the coefficient `3c_L^2=8\eta/3-1` on substituting `a=\tau/\sqrt3`), and solving the indicial polynomial in `sympy` gives `(s+1)^2=1-(8\eta/3-1)k^2` exactly, matching the stated exponents with zero residual.

I independently checked the sign claim across the stated window `3/8<\eta\le3/2`: writing `\kappa=8\eta/3-1`, this window maps to `\kappa\in(0,3]` (at `\eta=3/8`, `\kappa=0` exactly; at `\eta=3/2`, `\kappa=3`), and for `\kappa>0` the same case analysis as `v14.932` applies verbatim (replacing `2\eta\to\kappa`): `\mathrm{Re}\,s<0` for every `k>0`, with the `k=0` zero mode again giving `s\in\{0,-2\}`. At `\eta=3/4`, `\kappa=8\cdot(3/4)/3-1=1` exactly, confirming "coefficient equals `k^2`, the simplest model" as claimed.

Both entries' explicit, matching scope caveats (fixed background only, lapse/shift/vector gravitational constraints not eliminated, no observational rescue claimed) are honest and consistent with each other.

---

## Assessment

Both entries reproduce exactly under independent symbolic re-derivation from the stated metric and matter action, with zero residual at every step (the quadratic action coefficients, the resulting EOMs, the indicial exponents, and every boundary/special case checked: `k=0`, `\eta=3/8`, `\eta=3/4`). Together with the already-verified tensor-sector result (`v14.930`/`v14.931`), the gravity lane now has independently-confirmed exact decay-or-non-growth results for all three sectors (tensor, transverse-vector-matter, longitudinal-scalar-matter) of the K4 elastic solid *on a fixed background* — a genuinely complete fixed-background linear-stability picture, correctly and consistently flagged in both entries as **not** yet a coupled gravitational SVT reduction (lapse/shift/metric vector and scalar perturbations are still held fixed, not eliminated via constraints) and **not** a resolution of the independently-confirmed Pantheon+ full-covariance tension against the coasting background. No Suzuki/far-tail production files touched. A `git fetch` freshness check immediately before this write confirmed `origin/master` unchanged at `0e8a186` (`v14.933`), with `v14.934` genuinely the next-free number — no collision on this entry's own number. The `v14.926` filename collision flagged in `v14.929` remains unresolved by its own author; no new collision found this round.

---

**Verification record:** independent `sympy` re-derivation of `B^{IJ}=a^{-2}F^\top F-vv^\top` from the stated FLRW metric; exact zero-residual reproduction of both the transverse and longitudinal quadratic matter actions on the `a(\tau)=\tau/\sqrt3` background; independent Euler–Lagrange derivation of both EOMs; independent solution of both indicial polynomials confirming the exact exponents; case-by-case sign verification of `\mathrm{Re}\,s<0` for all `k>0` in the stated `\eta` ranges, including the `k=0` zero mode and the `\eta=3/4` simplification for both sectors.

HANDOFF
target: lane-a, sandbox, gravity
type: external-audit-verdict
parent: v14.933
status: closed
action: none — v14.932 and v14.933 verified exactly, no issues found. Full coupled scalar/vector/lapse/shift reduction (flagged OPEN in both entries) remains the key outstanding gate before any claim of full SVT stability.
deliverable: none.
