# Cone Derivation Ledger v15.601 — Lane A: primitive-null-edge and additive gauge-selection tests for the cross-shell quartic

**Date:** 2026-11-10. **Parents:** Casimir Null Diamond v2.1, Paper C v1.1, v15.180, v15.595–600; audit v15.597 confirms v15.595–596. **Status:** [D] exact geometry/algebra and scoped no-go; [C] illustrative charge-conserving interaction; [O] physical identification and natural boundary-only coupling. **Prewrite HEAD:** d9ef99db8511bff11b46a7efbabd84afad0d813b. Version v15.601 collision check clean. Additive-only; Suzuki lane production untouched.

## Gate 62 — primitive null-edge test

Under the deliberately chosen doubled-occupation Fock embedding |j,m> ↔ |n_a=2(j+m),n_b=2(j−m)>, write N=4j and consider the upper open source (N−1,1) and next-shell null destination (N+2,0). Their *real square-root spinors* are ψ_s=(sqrt(N−1),1) and ψ_t=(sqrt(N+2),0). Their determinant squared is N+2. By the exact determinant-Lorentz theorem in Casimir Null Diamond v2.1, the midpoint Lorentz norm squared is (N+2)/4, **not** the unimodular value 1/4 for any N≥1.

Most of these square-root spinors are not even integral primitive representatives, hence a Farey-adjacency interpretation is unwarranted. This is a scoped failure of the *natural doubled-number encoding* to make the proposed jump a primitive null edge, not a universal claim about all geometric lifts or a denial that its target is null.

A strict condition P_null|physical>=|physical> on both source and destination would exclude the source (N−1,1) for N>1, even though the destination (N+2,0) is null. The N=1 source (0,1) is an exceptional null-axis source. A final-state P_null projection is instead a postselection unless dynamics or a Gauss constraint is independently derived.

## Gate 63 — additive gauge charge and harmonic resonance

For phase charges q_a,q_b of the two Fock modes, the quartic O+=(a†)^3 b carries charge 3q_a−q_b independently of n_a,n_b. Attaching a compensating field factor with opposite charge makes the interaction gauge-neutral, but does not distinguish the boundary source n_b=1 from interior sources n_b≥2. For the illustrative *auxiliary* common-number U(1), the operator c O+ + c† O+† commutes with G=N_a+N_b+2N_c (because O+ changes two-mode total by +2 and c removes one c quantum). Its action on |N−2,2;k> for N≥3 and k≥1 produces a nonzero interior transition to |N+1,1;k−1> with the same additive charge balance. The c oscillator in this toy U(1) is charged; do not interpret it as a neutral electromagnetic photon or assert a physical electromagnetic gauge completion.

With harmonic Hosc=ħ(ω_a N_a+ω_b N_b+Ω N_c), the exchange O+ c has frequency gap ħ(3ω_a−ω_b−Ω), state-independent. At resonance Ω=3ω_a−ω_b it couples both boundary and interior states. Neither additive charge conservation nor harmonic resonance produces the null-target postselection.

Amplitude remains a separate obstacle: raw boundary norm squared N(N+1)(N+2), requested AM–GM escape norm squared (N+1)/4. The required factor 1/[2sqrt(N(N+2))] depends on N. Gauge neutrality and primitive-null-edge geometry do not derive it.

## Verification, exceptions, and scope

Independent exact rational/integer loop N=1…15 tested determinant square, midpoint norm, raw and target amplitude ratios, and an explicit interior process for N≥3. The N=1 null-source exception and N=2 shared-source exception are noted. Reproducer `cone_gates_62_63/reproduce.py`, output and report in the conversation's `cone_gates_62_63.zip` archive.

**Conclusion:** No supplied native primitive-unimodular rule or ordinary additive U(1) conservation law selects **both** the boundary-only channel and its precise strength in this auxiliary oscillator embedding. This is a scoped negative, not a theorem against nonlinear constraints, other gauge content, or an independently fixed microscopic interaction. No photons, chirality, G or gravity observable inferred.

**Next gate:** test whether an independently specified cone charge/constraint (not chosen post hoc) yields a kernel consisting exactly of the two boundary legs with the requisite `T†T=2E`, or prove absence for a well-defined candidate class. Examine native Paper C occupation dictionary rather than treating doubled-number encoding as physically determined.

**HANDOFF** target external-audit; status open; type primitive null spinor / U(1) charge selector audit; verify determinant²=N+2, caveats on integrality and N=1, toy interaction's conserved G, nonzero interior transition and state-independent detuning, and missing normalization. No frozen or production changes.