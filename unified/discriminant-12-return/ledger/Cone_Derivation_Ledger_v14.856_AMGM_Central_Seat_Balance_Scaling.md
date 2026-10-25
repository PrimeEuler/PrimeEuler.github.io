# Cone Derivation Ledger v14.856 — AM–GM central-seat balance and half/quarter scaling

Date 2026-10-25. Gravity lane. Parents v13.177, v14.767 and v14.827–836; external audit liveness through v14.855. Research note research-notes/AMGM_Parabolic_Central_Seat_Balance_Scaling.md at da92952b5be1645c5cf6f0d01b28277dd8c51578. Live prewrite HEAD da92952b5be1645c5cf6f0d01b28277dd8c51578. Additive only; no Suzuki/far-tail edits.

[D] Opposing parabola row/column at factor scale u are \(Y²=u²±2uX\) with vertices \(X=∓u/2\), intersecting at balanced seat (X,Y)=(0,u). On fixed AM \(T=u\), let X=δ, x=u+δ, y=u-δ; then the AM–GM deficit \(\Delta_u=u-\sqrt{u²-\delta²}\) is positive off seat, has first derivative zero at 0 and second derivative \(1/u\).

[D/I] A **chosen** restoring energy \(E_u=A(u)\Delta_u\), with positive independently specified scale A(u), yields force \(F_\delta=-A(u)\delta/\sqrt{u²-\delta²}\) and stiffness \(k_{\rm seat}=A(u)/u\). Consequently u=1/2 versus u=1 gives raw stiffness ratio \(2A(1/2)/A(1)\), not a universally selected 2 or 4. With a fixed energy E_* normalized by E_u=E_*[1-\sqrt{1-(δ/u)²}], the raw ratio is 4, but the normalized curvature with respect to ξ=δ/u is exactly 1 in both grids. This is dilation covariance, NOT a generated EM/G coupling distinction.

[O] The AM–GM deficit provides an intrinsically balanced geometric scalar but it is not a physical potential without a field/action that fixes A(u). The fixed-T displacement is distinct from motion along individual fixed-factor parabolas. No elastic modulus, Newton G, or hierarchy has been derived.

Flags: parabola_vertices=EXACT; seat_intersection=EXACT; AMGM_balance_gap=EXACT; physical_stiffness=ACTION_DEPENDENT; normalized_sector_difference=NONE; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: gravity-central-seat-scaling-review
parent: v14.856
status: open
action: Verify row/column vertices versus seat, fixed-T gap and derivatives, scale-normalized stiffness ratios, and that potential-energy assumption is explicitly conditional. Do not modify Suzuki/far-tail.
deliverable: scoped verdict.
