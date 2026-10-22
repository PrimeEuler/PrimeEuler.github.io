# Cone Derivation Ledger v14.710 — Gravity: high-speed Jacobi bath, distinct drift zero and ensemble statistics

**Date:** 2026-10-22 EDT; **lane:** gravity; **parents:** v14.705–709, especially v14.708.
**Collision check:** live \`master\` at allocation \`cec3547f649cf7bd6f4fb34b6fce20874a6f571e\`, reflecting the most recent dedicated-gravity producer correction. v14.709 already deposited by the sandbox, so next-free gravity entry is v14.710. No far-tail objects, papers, or certified resources modified.
**Producer:** \`research-notes/gravity_bath_jacobi_gram.py\` (amended assertion to compare like coordinates). **Proof note:** \`research-notes/Gravity_Bath_Jacobi_Gram_Stationarity.md\`.

## Source-exact derivation [D]

Reading actual deposited EFT v3.4, rather than the generic family used as the v14.708 robustness test, gives its independently matched Hamilton–Modak high-speed drift and diffusion for \(\varepsilon=e^2\):
\[
A_\varepsilon=C(1-2\varepsilon),\qquad
D_\varepsilon=2C\varepsilon(1-\varepsilon).
\]
The full Itô generator, \({\cal L}f=A_\varepsilon f'+\tfrac12 D_\varepsilon f''\), has the exactly normalized zero-current stationary density **\(\pi(\varepsilon)=1\)** on \((0,1)\) under the no-flux boundary model.

For \(q=\sqrt{1-\varepsilon}\), \({\cal L}q=-C(3q^2-1)/(4q)\). Its drift zero \(q^2=1/3\) or \(e^2=2/3\) is **not the full stochastic equilibrium**; it is a first-moment drift balance while diffusion persists. Stationary moments are \(E_\pi(e^2)=1/2\), \(E_\pi(q)=2/3\). The last provides another mathematically sound appearance of \(2/3\), but as an *ensemble average* of a different function.

The exact v14.701–708 phase Gram functional, conditional on matching physical eccentricity, is \(W(e)=\tfrac23(1-\rho^2)=4e/[3(1+e)]\). Propagating it with the **same** bath generator yields
\[
\boxed{\mathcal LW=-\frac{C(e^2+2e-1)}{3e(1+e)^2}},
\]
whose local zero is \(e=\sqrt2-1\), not the q drift zero \(e=\sqrt{2/3}\). In particular \(\mathcal LW/C=-12+29\sqrt6/6\simeq-0.1607995765\) at the latter. Its stationary ensemble average is exactly
\[
\boxed{\mathbb E_\pi W=\frac{8\ln2-4}{3}\simeq0.5150591482,}
\]
whereas the static value at the q-drift zero is \((4\sqrt6-8)/3\simeq0.5993196570\).

## Verdict / corrections [D/I]

The archive's hot-bath \(e^2=2/3\) is genuinely derived, with independent known encounter-theory antecedent, but the colloquial label "hot-bath attractor" must **not** be read as a deterministic universal eccentricity or full stochastic population equilibrium. The idealized high-speed shape diffusion has a broad stationary law. Distinguish drift-zero, observable drift-zero, and stationary ensemble means.

The Gram functional is not a validated torque observable or Hilbert-state transition; Favard obstruction v14.703 and external audit v14.704 stand. No parameter-free deviation from \(\Xi=(1-R\Phi''/\Phi')/3\) has been derived. No G measured or derived, no physical separatrix or apex-seat identification promoted.

## Audit and sandbox handoffs

**Audit:** independently reconstruct the Jacobi generator, zero-flux stationary measure, W drift and exact log-two moment; check boundary Feller classification and coupling of orbital scale T to C before extrapolating from frozen-T to the full EFT.

**Sandbox:** use the *actual* finite-temperature Maxwellian and BPS bound/killed generators in EFT v3.4 to evaluate steady/quasi-steady eccentricity moments, if defined, with explicit survival conditioning. Compare against the high-speed Jacobi idealization. Independently seek an instrument-defined measurement rule connecting this process to \(\Xi\); report negative results as negative. No far-tail writes.

**Flags:** \`far_tail_touched=false\`; \`G_derived=false\`; \`papers_modified=false\`; \`stationary_eps_density=UNIFORM_IDEALIZED_JACOBI\`; \`drift_zero_is_population_equilibrium=false\`; \`new_gravity_observable=false\`; \`separatrix_physics=OPEN\`; \`apex_seat=OPEN\`.
