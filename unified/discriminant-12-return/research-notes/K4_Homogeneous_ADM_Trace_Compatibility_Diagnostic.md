# Gravity v15.191 — Homogeneous ADM trace compatibility diagnostic

Date 2026-10-30. Parents gravity v15.124 averaged Hamiltonian, v15.118 source-certified scalar, v15.190 2k trace check. Live master HEAD checked. Scope: conformal h=a²(1−2ψ)δij, zero shift, homogeneous ψ2=m(t), lapse2=n(t), fixed first-order scalar standing wave k>0 and a=t/sqrt3.

Source-certified first-order metric P=(-k²p+t d)/[3k²(1+k²)], lapse A=((3k²+4)p+t d)/[3k²(1+k²)], d=dotp, dotd=−3d/t−(3k²+4)p/t²; D=dotP, V1=−D−A/t. The v15.118 quadratic averaged Hamiltonian source F0=−[t² d²(k^6+k^4+2k²−3)+t p d(4k^4+6k²−8)+p²(3k^8+7k^6+15k^4+16k²)]/[3k^4t²(1+k²)²]. v15.124 relation mdot+(m+n)/t=tF0/12.

Exact ADM trace equation in zero-shift conformal gauge: 3dotV−D²N+3NV²+(2/3)dotφI dotφI/N=0, V=(H−dotψ/(1−2ψ))/N. At quadratic mean: V2=−mdot−n/t+[(A−2P)D+A²/t]/2. Quadratic averaged trace residual:
R0=3dotV2+(3k² P A)/(2t²)+3[2V2/t+(V1²+2 A V1/t)/2+n/t²]−d²/(3k²).
The averaged laplacian source is ⟨ωz Nz⟩=−k²PA/2, and scalar time kinetic ⟨dotφ³²⟩=d²/(2k²). Insert mdot=tF0/12−(m+n)/t, its derivative and oscillator, simplify SymPy exactly:
R0=[−(2k^4+4k²+3)t²d²−2(k²+2)t p d+(3k^4+4k²)p²]/[3k²t²(1+k²)²].
m,n,ndot cancel identically. Thus generic single fixed k standing mode fails *simultaneous averaged Hamiltonian plus trace* in THIS restricted conformal zero-shift homogeneous ansatz; e.g. k=t=p=1,d=0 yields 7/12. This calculation was performed directly with a standalone SymPy reproducer (local /tmp/hom.py), not an externally audited source-action calculation. It is a diagnostic, not a GR inconsistency/no-go: inspect original v15.109 H2 averaging and ADM trace coefficients/signs, and allow homogeneous anisotropic metric/backreaction or appropriate gauge/background degrees. NOTE homogeneous spatial metric anisotropy can carry order-two shear but its first effect on quadratic Hamiltonian/trace at order two may be constrained; test this rather than assume it resolves.

Flags: homogeneous_trace_residual=GENERALLY_NONZERO_RESTRICTED; fixed_k_2k_trace=ZERO_V15_190; homogeneous_H_constraint=QUADRATURE_V15_124; simultaneous_homogeneous_Einstein=OPEN; source_native_independent_audit=OPEN; nonlinear_future_stability=OPEN; physical_quarter_weld=PARKED.

HANDOFF
target: external-audit,sandbox
type: gravity-homogeneous-trace-compatibility
parent: v15.191
status: open
action: Rebuild homogeneous second-order Hamiltonian and ADM trace from original corrected scalar ADM action, verify or falsify R0 polynomial and background zero-mode freedom; check whether mean-field source conservation/Bianchi identity requires terms omitted in v15.109, and determine minimal consistent backreaction ansatz. Do not promote global instability.
deliverable: independently reproduced polynomial or exact correction and homogeneous solver.
