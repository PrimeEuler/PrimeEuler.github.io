# Cone Derivation Ledger v14.944 — Spherical radial flux and conserved-source obstruction

Date 2026-10-26. Parents v14.818, 820–821, 919–921, 941, Lane A 942–943 read-only. Research note research-notes/K4_Radial_Flux_Conservation_and_Noether_Source_Gate.md commit 70a6020cd057eda857045a961f52c55484a9c482. Prewrite HEAD 70a6020cd057eda857045a961f52c55484a9c482. Owner per-gate ledger protocol; additive gravity only, Suzuki quarter weld parked; protected Suzuki/far-tail untouched.

[D] In four-factor Hessian FLRW mathematical metric ds²=dτ²−a²(dχ²+χ²dΩ²), a=τ/√3, sqrt−g=a³χ²sinθ. For a spherically symmetric conserved current, ∇μJμ=0 ⇔ ∂τ(a³χ²Jτ)+∂χ(a³χ²Jχ)=0. Under simplifying purely spatial radial flow Jτ=0, conservation yields a³χ²Jχ=C(τ) and orthonormal radial current Jhatχ=aJχ=Φ(τ)/(4πR²) where R=aχ, Φ=4πC. This is a mathematical flux field, not an independent future-timelike causal matter number current: Jτ=0 is spacelike unless vanishing. Conservation does not fix Φ or require time constancy.

[D] Causal illustrative outgoing null current with u=η−χ, dη=dτ/a: Jτ=N f(u)/(4πa³χ²), Jχ=Jτ/a, satisfies ∇J=0 exactly away from origin and JμJμ=0. Point-source normalization N and profile f remain external. With *additional* Maxwell field equations and charge Q, physical electric field obeys Ehatχ=Q/(4πε0R²) for radial isolated charge on each FLRW slice (Gauss law); neither Maxwell gauge action nor Q follows just from AM-GM cone. On null lightfront R_light=τ ln(τ/τe), inverse-area geometric factor is [4πτ²ln²(τ/τe)]^-1. Distinguish spherical wavefront area from enclosed 3-ball volume, and null pulse flux from a time-stationary radial spatial current.

[I/O] Key answer: YES, spherical geometry + imposed local conservation yields inverse-square radial dilution. NO, this is not uniquely derived gravitational source: many charges/currents exist, Noether symmetry and field dynamics not yet derived from factor product, and the amplitude remains arbitrary. Shape-volume π/6 is not a coupling constant. The previously known observational coasting tension and full SVT matter-gravity constraint remain.

Flags: radial_covariant_conservation=EXACT; inverse_square_geometric_dilution=DERIVED; null_pulse_current=EXPLICIT; independent_factor_Noether_charge=NOT_DERIVED; Newton_G=NOT_DERIVED; physical_metric_selection=OPEN; Suzuki_quarter=PARKED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: k4-radial-flux-current-physical-source
parent: v14.944
status: open
action: Verify conserved-current divergence, normalization and a factors in physical orthonormal radial component, verify null-current conservation and central-charge Gauss law; distinguish spatial-flux ansatz from causal timelike/null current and ask whether AM-GM selects a conserved Noether charge.
deliverable: scoped audit verdict.

NEXT: test log-shape translations and common product dilation as Noether symmetries of an explicit candidate action; decide whether a conserved physical source amplitude is derived or remains free.
