# Cone Derivation Ledger v15.600 — Lane A: dynamic null-boundary selection and harmonic-resonance no-go

**Date:** 2026-11-10. **Parents:** Paper C v1.1; Casimir Null Diamond v2.1; v15.180, v15.572–574, v15.595–599. **Status:** [D] exact Fock-operator obstruction in defined candidate class; [O] source-derived boundary interaction, odd-quarter selector, field identity. **Fresh prewrite HEAD:** 7c443ed35aa203bf574c5b77cb69d985c1c83bf2 (v15.599); v15.600/version collision search negative. Additive-only; frozen Suzuki and far-tail untouched.

## Gate 60: null target is a geometric condition, not an invariant interaction sector

In the explicit **auxiliary** doubled-occupation embedding |j,m> ↦ |n_a=2(j+m),n_b=2(j-m)>, define the null-axis destination projector P_null onto Fock states with n_a=0 or n_b=0. The exact projection identity P_null O_+ P_N selects the boundary source |N−1,1> and destination |N+2,0>, and its mirror P_null O_- P_N selects |1,N−1> ↦ |0,N+2>, where O_+=(a†)^3b, O_-=(b†)^3a (v15.598–599). For N=2 the two source states coincide while destination states are distinct; treat this separately when asserting ranks.

Check established dynamics:
1. Free harmonic Hosc=ℏ(ω_a N_a+ω_b N_b+const) satisfies [Hosc,P_null]=0 but has **no occupation-changing transitions**.
2. Schwinger J_+=a†b moves |0,N> ↦ √N |1,N−1>, interior for N>1, and K_+=a†b† moves |N,0> ↦ √(N+1)|N+1,1>, interior for every N≥0. Hence neither full transverse Schwinger Jx nor squeezing Kx preserves the null-axis subspace (nonzero [P_null,Jx] for N>1; nonzero [P_null,Kx]).
3. Quartic O_- acts on |N,0> as √[N·3!] |N−1,3>, interior for N>1; O_+ similarly on the mirror. Thus raw O_++O_-+h.c. does not preserve the null-axis subspace, and its action from interior has non-null destination channels.
4. Schwinger total number N is conserved by J, but O changes it by +2. Squeezing preserves D=N_a−N_b, but O changes D by ±4. The KS-gluing constraint D=0 has no nonvacuum null states and is not preserved by O. O preserves N parity, which does not choose odd N over even N (both sectors remain viable).

Consequently none of these **particular** existing Hamiltonian generators simultaneously realizes the boundary map and dynamically enforces its null final target. P_null is a geometrically motivated projector but remains a selected postcondition, not a dynamical theorem. This does not rule out all cone Hamiltonians or effective constrained dynamics.

## Gate 61: harmonic energy conservation cannot selectively resonate with null endpoints

For any Hosc=ℏ(ω_a N_a+ω_b N_b+const), the energy changes under O_+ and O_- are

[Hosc,O_+]=ℏ(3ω_a−ω_b) O_+,
[Hosc,O_-]=ℏ(3ω_b−ω_a) O_-.

**Both are independent of n_a,n_b.** The intended boundary process |N−1,1>→|N+2,0> and all interior O_+-allowed processes with the same (+3,−1) occupation change have exactly the same harmonic gap. Resonance against this Hamiltonian therefore cannot single out the null-axis destination. Isotropic frequencies give identical gaps 2ℏω. An engineered anharmonic H=f(N_a,N_b) *could* create occupancy-dependent detuning, but an externally chosen nonlinear spectrum is additional dynamical input.

The bare quartic boundary matrix element squared is N(N+1)(N+2), against required AM–GM c=(N+1)/4, demanding spectral amplitude factor 1/[2√(N(N+2))]. P_null alone removes extra support but cannot generate this coefficient. The projectors and normalizer in v15.598 remain chosen. No odd-quarter-specific selection, physical photon field, mass, G, or energy source is derived.

Exact arithmetic verification N=1…9, including Jx and K+ boundary leakage weights, O endpoint and representative interior amplitudes, and symbolic occupation-independent harmonic gaps, supplied in response archive `cone_null_dynamics_gates_60_61.zip`. The N=1 and N=2 coincidences/exceptions were tracked separately.

**Next gate:** test a precisely defined constrained operator family (e.g. physical asymptotic null conditions, null-edge allowed channels or actual gauge-invariant interaction) for whether it fixes BOTH support and normalization. Do not label postselection as a physical law absent such a derivation.

**HANDOFF** target external-audit; status open; type oscillator/null dynamic selector no-go; independently verify [Hosc,P_null], failure of P_null invariance under Jx, Kx and raw quartic for generic N, harmonic detuning degeneracy, N=1 and N=2 exceptions, and norm mismatch. No production files changed.
