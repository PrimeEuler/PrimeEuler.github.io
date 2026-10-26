# Source-support sensitivity of the retarded Maxwell seat resonance

Date 2026-10-26. Parents v14.873–884; v14.885 external audit verifies v14.884, noting one isolated off-path reproducibility precision caveat. Gravity/bicone side lane only.

## Field-only frozen anchor [D]
With z=aω/c, D_EM(z)=-1/4+z²F(z), F(z)=1+i√π z exp(-z²)erfc(-iz), retarded continuation, the damped complex root is z0=0.4108337143730426322−0.1700926343728675801 i. Direct mpmath findroot, 30-digit precision.

## Explicit additional mechanical support [I/D]
Let M0=μ0g²/(6π^(3/2)a), kscale=M0c²/a². Include an independent positive mechanical support stiffness k_s and bare inertia m_s. In the sign convention D_EM=-k_EM/kscale+z² M_EM/M0, the normalized inverse response is
D_total(z)=D_EM(z)-κ_s+μ_s z²,
κ_s=k_s/kscale, μ_s=m_s/M0.
These are NEW physical parameters NOT supplied by SU(2), Coulomb, or the reflected-circle source model.

Exact numerical continuation with mpmath yields:
(κ_s,μ_s)=(0,0): z=0.4108337143730426−0.1700926343728676i;
(0.02,0): z=0.4215089571158286−0.1805220758401746i;
(0,0.10): z=0.40971142617118397−0.15498837510757932i;
(0.02,0.10): z=0.4211006776030383−0.16525104623228716i.
All are poles of this specified FROZEN-ORBIT composite response and all remain damped. Model example, not fitted physical data.
At z0, D_EM'(z0)=0.9421742758359790+0.9003551996224992i; linear sensitivities dz/dκ_s=1/D_EM'=0.5547645326116870−0.5301409137496258i; dz/dμ_s=−z0²/D_EM'=−0.0034931233904817+0.1516753672929012i. These independently corroborate the small finite parameter shifts.

## Static instability criterion and what is NOT known [D/O]
At Ω_L=0, D_total(0)=−1/4−κ_s <0 for any κ_s≥0; thus adding positive support stiffness cannot create a zero-frequency static mode in the frozen model. At finite Ω_L, the Sandbox v14.884 quasistatic rotation correction is D_EM(0;α,β)+1/4≈(αβ)²/5 for α→0, where αβ=Ω_LR/c. Formal extrapolation to D(0)=0 would require (αβ)²≈5/4+5κ_s, exceeding subluminal αβ<1 even at κ_s=0; HOWEVER the expansion is only controlled for small α and cannot rule out a zero at high rotation. One must numerically compute D_EM(0;α,β) and assess ΩR/c<1 across the parameter domain; do not claim global exclusion or a critical threshold from low-order expansion.

Audit reminder: v14.885 independently verified v14.884's α=0 limit, continuity, quasistatic coefficient and pole spot checks. One unrelated off-path validator point was 3e-4 rather than advertised 5e-9; no claim of complete cross-plane numerical certification. No Higgs/G, universal inertia or gravitational coupling derived.

Reproducer:
\`\`\`python
import mpmath as mp
mp.mp.dps=30
F=lambda z: 1+1j*mp.sqrt(mp.pi)*z*mp.exp(-z*z)*mp.erfc(-1j*z)
D=lambda z: -mp.mpf('0.25')+z*z*F(z)
z0=mp.findroot(D,(0.41-0.17j,0.42-0.16j))
for ks,ms in [(0,0),(.02,0),(0,.1),(.02,.1)]:
 root=mp.findroot(lambda z:D(z)-ks+ms*z*z,(z0,z0+.005))
 print(ks,ms,root,abs(D(root)-ks+ms*root*root))
\`\`\`
