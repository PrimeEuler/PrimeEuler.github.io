# Cone Derivation Ledger v14.722 — Gravity lane executes its own pending sandbox calculation; reserve Suzuki compute

**Date:** 2026-10-22 EDT. **Parents:** v14.716/v14.718/v14.720/v14.721. **Operational directive:** user requests that all sandbox compute remain dedicated to the ongoing Suzuki certificates. Effective immediately, **do not assign, dispatch, or queue new gravity work to the sandbox**. Handle all unclosed gravity tasks within the dedicated gravity lane; existing handoffs are not licenses to compete for Suzuki compute.

**Live HEAD/collision:** before filing this entry, \`master\` SHA \`d92fe40c4bb867c4db55dbb4dbd71a2e1dd4e870\`, v14.722 free. Additive only; no papers, far-tail, or existing ledger entries modified.

## Completed locally [D/N]

The v14.721 open sandbox-labeled task (small-\(\Theta\) expansion and normalized quadrature) is executed here. New reproducible deposits:
- \`research-notes/gravity_small_theta_normalized.py\`
- \`research-notes/Gravity_Self_Executed_Small_Theta_Handoff.md\`

For Maxwellian longitudinal diffusion, define \(D_*=(2\mathcal K/(3\sqrt\pi))\sqrt{\Theta T/\mu}\). At fixed \(0<e<1\), with \(q=\sqrt{1-e^2}\), use the exact Kepler moment \(\langle v^4\rangle=(\mu/T)^2(4/q-3)\). Then
\[
\boxed{\bar a_{T,e^2}=-\frac{96}{5}\frac{D_*T^2}{\mu}q(1-q)\Theta+O_e(D_*\Theta^2).}
\]
The first finite-temperature cross-covariance term is strictly negative, order \(\Theta^{3/2}\) with fixed \(\mathcal K,T,\mu\); expansion not uniform at extreme eccentricity. Independent fully normalized quadrature at \(e=\sqrt{2/3}\) yields exact/leading ratios 0.99734 (\(\Theta=.001\)), 0.97389 (.01), 0.90165 (.04), and agrees qualitatively for other e.

## Outstanding gravity gates, to be performed here and not handed off

(1) Source-faithful full BPS hard-jump/killed and bound-preserving forward generator; the Fokker–Planck diffusion **cannot** substitute for finite jumps at escape. (2) Finite-\(\Theta\) survivor-conditioned density and any limiting/quasi-stationary law once a valid boundary prescription is specified. (3) A physically derived rotor/gravitational coupling, if any, rather than inserting bath-shape moments into \(\Xi\).

These are **not closed** by a numerical expansion. No new audit/sandbox work is assigned by this entry; the audit may independently read if it chooses but no compute-consuming handoff is requested.

**Flags:** \`sandbox_gravity_handoffs=PAUSED_USER_DIRECTIVE\`; \`gravity_work=SELF_EXECUTE\`; \`small_theta_handoff=CLOSED_LOCAL\`; \`BPS_QSD=OPEN\`; \`Xi_novelty=false\`; \`G_derived=false\`; \`far_tail_touched=false\`; \`papers_modified=false\`.
