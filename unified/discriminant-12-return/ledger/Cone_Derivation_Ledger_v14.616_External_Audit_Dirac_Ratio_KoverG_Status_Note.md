# Cone Derivation Ledger v14.616 — External Audit: Dirac's Ratio as K/G (Status Clarification; No Open Item Resolved)

**Date:** 2026-10-19
**Track:** External Audit (exploratory status note, authorized by Jeremy in conversation; not a verification round, not Lane A/Sandbox content)
**Parents:** v14.550 (Sandbox: diameter-secant machine and the gravity road — origin of the two open $G$ items), v14.615 (live HEAD at deposit).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `c340b96...` (v14.615), matching local HEAD; live ledger max was v14.615. v14.616 is next-free.

## 1. What was computed

During a side conversation with Jeremy (not part of the discriminant-12-return certification chain), this auditor made the standard decomposition of Dirac's force ratio explicit and verified it numerically:

\[
\text{Dirac's ratio} = \frac{e^2}{4\pi\varepsilon_0\,G\,m_p m_e} = \frac{K}{G},
\qquad
K \equiv \frac{e^2}{4\pi\varepsilon_0\,m_p m_e}.
\]

Using SI 2019 constants (`mpmath`, 30 dps): $K = 1.51417270434952820659674967929\times10^{30}$ (units $\mathrm{N\,m^2}$), and $K/G$ reproduces the direct evaluation of Dirac's ratio ($2.26866143917643529\times10^{39}$) to every digit checked. $e$ and $\varepsilon_0$ are exact or effectively exact under SI 2019; $K$'s relative uncertainty is set by $m_p$, $m_e$ ($\sim 3\times10^{-10}$ each), roughly $10^5\times$ tighter than $G$'s CODATA relative uncertainty ($2.2\times10^{-5}$). Propagating this: essentially all of Dirac's ratio's own measurement uncertainty is attributable to $G$ alone, so only its leading $\sim$5 significant figures ($2.2687\times10^{39}$) are physically meaningful.

A related dead end was also checked and closed off: substituting the SI 2019 Kibble-balance mass-realization formula ($m = hf_1f_2/gv$) into $\alpha_G = Gm^2/\hbar c$ to try to introduce $G$-independent dimensional content is circular — the Kibble balance calibrates mass against *local* $g$, not universal $G$, so no new information enters.

## 2. What this is **not**

This is a restatement and quantification of something v14.550 §3 already said ("$G$ is dimensionful; no geometry outputs kilograms; the only legitimate targets are dimensionless"), not new structure. It does **not** touch either of v14.550's two open items, which remain exactly as open as before:

- **(i) hierarchy generator** — nothing here produces the rapidity $\psi\approx45$ or explains $G$'s value; $G$ is still a bare external input on the right-hand side.
- **(ii) factorised observable** — $K$ is ordinary hydrogen-scale electrostatics-over-mass with no cone/Wigner factor in it; it is not an instance of (cone factor) $\times$ (gravitational coupling).

The open-item count for $G$ in this project is unchanged: **two**, not one.

## 3. Scope flags (honest)

`answers_lane_a_handoff = false`; `papers_modified = false`; `certified_objects_modified = false`; `new_physics_claim = false`; `G_derived = false`; `hierarchy_generator_found = false`; `factorised_G_observable_exists = false`; `open_item_count_change = false` (still 2, per v14.550 §3).

## 4. Disposition

Status-clarification note only. The live open items in the main discriminant-12-return chain remain unchanged: Sandbox's far-residual construction/certification (v14.585 actions 3-4), and, in the separate $G$-exploration side-thread, v14.550's two named items (hierarchy generator; factorised observable), neither touched by this note.
