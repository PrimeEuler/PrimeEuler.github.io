# Cone Derivation Ledger v14.957 — K4 homothety, dilation-current trace and coasting-source obstruction

Date 2026-10-26. Parent v14.956. Research note research-notes/K4_Homothetic_Dilation_Trace_Current.md commit 84eb39629fa70d5d5699f1b020b0530f112ec087. Prewrite live HEAD 84eb39629fa70d5d5699f1b020b0530f112ec087. Owner per-gate ledger. Additive gravity only; Suzuki quarter physical weld PARKED, protected Suzuki/far-tail untouched.

[D] K4 product-Hessian FLRW g=dτ²−τ²/3 Σdzi² has exact homothetic H=τ∂τ with L_Hg=2g. In product-scale coordinates τ=√3√P4, H=2P4∂P4=2∂r where r=ln P4. It rescales P4; unlike shape reciprocal scaling it does NOT preserve product. H is conformal Killing, not Killing.

[D] For symmetric ∇μT^{μν}=0, Dμ=T^{μν}Hν obeys ∇μDμ=Tμ{}μ. Traceless matter such as classical source-free Maxwell in four spacetime dimensions has conserved dilation current. Its integrated charge Q_H=∫a³τ Tττ d³z is still initial/boundary data, not fixed by the 1/4 Casimir or the factor product. For radiation ρrad∝a^-4 this is constant on fixed comoving volume given vanishing boundary flux.

[D / obstruction] K4 effective coasting fluid required under additionally postulated Einstein equations has p=−ρ/3, trace Tμ{}μ=ρ−3p=2ρ≠0. Hence this supporting source does NOT possess the above strictly conserved homothetic stress current: ∇·D=2ρ. No inference that radiation's tracefree Noether current supplies the actual gravitational coasting source. With Maxwell sources, Maxwell stress alone not separately covariantly conserved.

[O] Study physically principled trace improvements or compensators for coasting stress, without arbitrary cancellation, and check if any locally conserved scalar current retains gravitational physical meaning. Existing Pantheon+ coasting tension and independent full-SVT matter-gravity constraint remain open.

Flags: K4_homothety=EXACT; homothetic_trace_identity=EXACT; traceless_matter_dilation_current=CONDITIONAL_CONSERVED; K4_coasting_effective_fluid_trace=2rho; coasting_source_dilation_conserved=FALSE; conserved_charge_normalization=NOT_FIXED; Newton_G=NOT_DERIVED; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: k4-homothety-dilation-trace-current
parent: v14.957
status: open
action: Independently verify homothetic Lie derivative, stress current trace identity, τ/P4 scaling factors, radiation charge, and coasting-fluid trace obstruction. Distinguish conformal matter from source of Einstein coasting metric.
deliverable: scoped verdict.

NEXT: test improved dilation currents or coasting-source trace compensation with explicit covariant action and on-shell conservation; verify no charge quantization inserted. Keep Sandbox full SVT separate.
