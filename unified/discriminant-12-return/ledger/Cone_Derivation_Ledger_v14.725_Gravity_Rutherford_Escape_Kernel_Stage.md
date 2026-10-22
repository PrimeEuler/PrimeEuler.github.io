# Cone Derivation Ledger v14.725 — Gravity Rutherford escape geometry and source audit; sandbox reserved for Suzuki

**Date:** 2026-10-22 EDT. **Lane:** gravity. **Parents:** v14.723 (killed/censored operator), v14.724 (external audit R336), EFT v3.4.
**Live HEAD/collision:** immediately before ledger write \`master\` SHA \`133142faaeadad25bd7bdee9102dba0f78ed0a49\`. Recursive tree lists no v14.725. All writes additive, no far-tail or paper modification. **No sandbox handoff**.

## Independent results

**Audit status:** v14.724 independently verified the finite-temperature 3D joint generator (v14.720), strict covariance sign theorem (v14.721), and small-Theta coefficient -96/5 (v14.722), and accepted the v14.723 killed/censored and survivor identities. These checks have now returned; no new gravity work was sent to the Suzuki sandbox.

**Hard-escape angular reconstruction [D]:** For equal-mass Rutherford scattering, with incoming test/bath velocities v,w, V=(v+w)/2, g=v−w, outgoing \(v'=V+\frac{|g|}{2}\hat g'\), and escape iff \(|v'|^2\ge2\mu/r\), the outgoing energy is \(a+b\cos\phi\) at fixed polar scattering angle. Hence the escaped azimuthal fraction is exactly \(\pi^{-1}\arccos[(2\mu/r-a)/b]\) when the threshold lies between a±b, and 0 or 1 outside. The Rutherford angle factor is \(2\pi\int\sin\theta\,\sin^{-4}(\theta/2)P_{\rm esc}(\theta)d\theta\) with explicit cutoff. Full expressions and precise scope in \`research-notes/Gravity_Rutherford_Escape_Kernel_Stage.md\`.

**Producer [N]:** \`research-notes/gravity_rutherford_escape_kinematics.py\` was executed locally. For μ=r=1, v=(0,0.8,0), w=(0,3,0), escaping collisions require \(\theta>\theta_0=0.830317885457...\); the conditional Rutherford angular escape factor has the exact closed form
\[
4\pi[\csc^2(\theta_0/2)-1]=64.679848750378...
\]
and is numerically invariant for cutoff \(\theta_{\min}=0.01,0.05,0.10,0.50<\theta_0\) to better than 1e−7. The incoming test particle is bound. This establishes a **nontrivial cutoff-independent conditional collision example**, not independence for every Maxwellian-averaged bath state.

## Honest remaining limits

The source EFT has local, numerically estimated BPS matched fold corrections and a fold-local escape hazard, but a full global collision and soft-matching coefficient field is not deposited. This gate reconstructs the exact equal-mass **collision angular geometry** and conditional escape factor; a source-matched Maxwellian-averaged numerical survivor QSD remains open. It would be misleading to infer the global QSD from the fold-local correction numbers.

The bath changes orbit distributions and potentially noise but does **not** supply an additional potential \(\Phi\), torque coupling, or correction to the static rank-1/rank-2 \(\Xi\) ratio. Hence no G and no new gravitational field law derived.

**Future work is assigned only to this gravity lane**: Maxwellian velocity and orbit averaging of the hard hazard with a specified cutoff and matched soft field if available, then survivor-normalized forward equation and numerical convergence. No new sandbox work while Suzuki is active.

**Flags:** \`Suzuki_compute_reserved=true\`; \`gravity_sandbox_handoffs=NONE\`; \`G_derived=false\`; \`Xi_new_signal=false\`; \`conditional_hard_escape_kernel=CONSTRUCTED_TESTED\`; \`global_BPS_QSD=OPEN\`; \`far_tail_touched=false\`; \`papers_modified=false\`.
