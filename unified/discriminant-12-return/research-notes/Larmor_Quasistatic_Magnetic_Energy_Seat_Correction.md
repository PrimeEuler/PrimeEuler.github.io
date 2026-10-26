# Finite-Larmor rotation: quasistatic Gaussian transverse magnetic energy

Date 2026-10-25. Parent v14.871–874, external audit v14.875; v14.876 liveness. Additive only.

Define g=2qR/u and δ=uξ. First-order exact-in-Ω conserved source from v14.872:
rho1(k,t)=-i g δ k_x f_a(k)e^{-ik·c(t)},
J1(k,t)=g f_a(k)e^{-ik·c(t)}[δdot e_x-iδ k_x v(t)],
where c=R(0,cos Ωt,sin Ωt), v=cdot=ΩR(0,-sin Ωt,cos Ωt), f_a(k)=e^{-a²k²/2}. The common c phase drops out of equal-time magnetic field energy.

Within the *instantaneous magnetostatic approximation only*, transverse magnetic energy is
EB,qs=μ0/2∫ d³k/(2π)³ J1*·(I-khat khat)J1/k².
Cross term between δdot e_x and -iδ kx v vanishes pointwise after taking real part (both real-valued δ,δdot; transverse projector real). At v·ex=0:
∫ exp(-a²k²)(1-kx²/k²)/k² d³k/(2π)³=1/(6π^(3/2)a).
∫exp(-a²k²)[kx²/k²][v·P_T v]d³k/(2π)³
= v² (1/3-1/15)∫exp(-a²k²)d³k/(2π)³
=v²/(30π^(3/2)a³).
Therefore
EB,qs=(1/2)M_T(0)δdot²+(1/2) kB,Ω δ²,
M_T(0)=μ0g²/(6π^(3/2)a),
kB,Ω=μ0g² Ω²R²/(30π^(3/2)a³).
With kE=g²/(24π^(3/2)ε0a³) from v14.873,
kB,Ω/kE=(4/5)(ΩR/c)².
No angular-averaged cross term and no O(Ω) term in this equal-time magnetic-energy expansion.

Critical distinction: This positive magnetostatic ENERGY curvature cannot be promoted to a physical restoring FORCE for a prescribed rotating source without deriving an action and accounting for the external drive/constraints. At finite Ω the retardation expansion requires Ωa/c≪1 and velocity ΩR/c≪1, in addition to seat-signal frequency ωa/c≪1. The Gaussian overlaps/cancels at δ=0; Ω does not create a genuine charge monopole. Regulator width and charge assignment remain inputs, and gravity/Higgs/physical mass are not derived.

Next gate: use conserved rho and J in frequency-resolved full Maxwell action; Floquet harmonics depend on R/a, Ωa/c; distinguish diagonal kernel and off-diagonal mixing, exclude claims of a certified pole without numerical convergence.
