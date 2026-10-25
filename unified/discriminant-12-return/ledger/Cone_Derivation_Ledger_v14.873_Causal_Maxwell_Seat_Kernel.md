# Cone Derivation Ledger v14.873 — Causal Maxwell seat kernel and resonance test

Date 2026-10-25. Parents v14.870–872. Research note research-notes/Retarded_Maxwell_Seat_Kernel_Pole_Test.md commit 5f54cacc56a23743a2dcb902105b0e273d6fa4a1. Live prewrite HEAD 5f54cacc56a23743a2dcb902105b0e273d6fa4a1. Additive only, Suzuki/far-tail untouched.

[D under regulated source] The overlapping ±q Gaussian blobs in the *balanced seat* model yield at first order ρ(k)=-ig kx δ e^(-a²k²/2), J(k)=g δdot e^(-a²k²/2)xhat, g=2qR/u. Coulomb electrostatic energy =g²δ²/(48π^(3/2)ε0a³), and seat curvature k_C=g²/(24π^(3/2)ε0a³)>0. This does not contradict v14.870's *nonoverlapping* opposite charges, whose potential has negative second derivative and nonzero first derivative at finite separation.

[D] Exact frozen-orbit transverse retarded kernel M_T(z)=μ0g²/(3π²)∫0∞ dk k²e^(-a²k²)/[k²-(z/c)²], Im z>0, with M_T(0)=μ0g²/(6π^(3/2)a)>0 and Im M_T(ω+i0)=μ0g² ω exp[-(aω/c)²]/(6πc) for ω>0. This is a causal field response and radiative spectral loss, not a universal mass coefficient. The low-frequency dipole radiation term agrees the power g²δddot²/(6π ε0c³).

[D/O] A frozen low-frequency frequency estimate k_C/M_T(0)=c²/(4a²) corresponds to ωa/c=1/2, outside parametrically low-frequency expansion: no controlled small-frequency normal mode has been derived. Physical resonance requires zeros of the full causal response with source supports and coupled mechanics included.

[D formal] Full rotating first-order source ρ1=-ig kx f_a e^(-ik·c(t))δ and J1=g f_a e^(-ik·c(t))[δdot xhat−ikx v(t)δ], with c(t)=R(0,cosΩt,sinΩt), obey Fourier continuity exactly. Maxwell retarded action generates a period-T Floquet kernel K_nm(ω) coupling ω+nΩ channels, not a proven constant inertia for finite Ω. Floquet matrix not numerically diagonalized at this gate. Net pair charge zero; no Coulomb monopole, Higgs identity, or gravity law deduced.

Flags: balanced_electrostatic_seat_curvature=POSITIVE_REGULATED; frozen_retarded_kernel=EXACT_IN_MODEL; quasistatic_inertia=POSITIVE; retarded_radiative_spectral_density=POSITIVE; low_frequency_pole=CANNOT_CERTIFY; finite_Larmor_Floquet_kernel=FORMAL_NOT_DIAGONALIZED; gravity_monopole=OPEN; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: retarded-maxwell-bicone-seat
parent: v14.873
status: open
action: Check Fourier integral factors, Gauss/static field curvature, retarded analytic prescription and imaginary spectral part, leading dipole radiation, naive pole outside asymptotic domain, and rotating-source continuity/Floquet qualifications. No Suzuki/far-tail changes.
deliverable: scoped independent verdict.
