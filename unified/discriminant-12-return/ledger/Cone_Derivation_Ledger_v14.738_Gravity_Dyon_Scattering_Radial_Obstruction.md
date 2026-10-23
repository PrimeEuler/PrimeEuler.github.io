# Cone Derivation Ledger v14.738 — Gravity scattering: fixed-radius MIC/Taub–NUT radial-action mismatch

**Date:** 2026-10-22 EDT. **Lane:** dedicated gravity. **Parents:** v14.731–737, including independent external audit R339 at v14.737.
**Live HEAD/collision:** immediately before write \`9fdba67804eb5d41f33fadaf6f69c2a457bc3503\`; recursive tree shows v14.738 free. No Suzuki sandbox, far-tail, or paper writes.
**Additive research deposits:** \`research-notes/Gravity_Dyon_Scattering_Asymptotic_Gate.md\`, \`research-notes/gravity_dyon_scattering_asymptotics.py\`.

## Tested [D, exact symbolic]
For the timelike Taub–NUT metric with \(\Sigma=r^2+l^2,\ f=(r^2-2mr-l^2)/\Sigma\), \(\varepsilon=-p_t\), \(s=2\varepsilon l\), and the *full common angular Casimir* \(J^2\), the v14.734–736 radial HJ gives
\[
p_{r,\rm TN}^2=\varepsilon^2/f^2-1/f-(J^2-s^2)/(\Sigma f).
\]
The standard flat MIC–Kepler model, WITH the Zwanziger term required for its established parabolic separability, has
\[
p_{r,\rm MIC}^2=2E+2\kappa/r-J^2/r^2.
\]
Direct symbolic large-r series:
\[
\boxed{
p_{r,\rm TN}^2=\varepsilon^2-1+
\frac{2m(2\varepsilon^2-1)}r+
\frac{-J^2+(8\varepsilon^2-2)l^2+(12\varepsilon^2-4)m^2}{r^2}
+O(r^{-3}).}
\]
Matching constant and 1/r sets \(E=(\varepsilon^2-1)/2\), \(\kappa=m(2\varepsilon^2-1)\). The 1/r² coefficient still generically differs by \((8\varepsilon^2-2)l^2+(12\varepsilon^2-4)m^2\), even when m=0 but l nonzero.

**Precise verdict:** the angular Casimir and monopole offset are shared, but this simple same-r, same-p_r standard-MIC identification is **obstructed at inverse-square order**. This is NOT a no-go theorem for any symplectic transform or clock reparameterization: such a map could alter the comparison and must be explicitly constructed and tested on an invariant. Physical scattering maps require consistent asymptotic angle/gauge-bundle conventions because TN asymptotics differ from flat MIC. No unjustified global scattering equality or unification of couplings.

**Next gravity-only gate:** derive canonical radial-action derivative/scattering-angle comparison, or construct a valid explicit nontrivial mapping; keep energy- and gauge-normalization conventions fixed. No global boost symmetry, novel G or Xi signal claimed.

**Flags:** \`common_angular_worldline=PASS\`; \`fixed_radius_full_radial_identification=FAIL_GENERIC\`; \`general_symplectic_equivalence=OPEN\`; \`Suzuki_sandbox_reserved=true\`; \`sandbox_handoff=NONE\`; \`G_derived=false\`; \`far_tail_touched=false\`.
