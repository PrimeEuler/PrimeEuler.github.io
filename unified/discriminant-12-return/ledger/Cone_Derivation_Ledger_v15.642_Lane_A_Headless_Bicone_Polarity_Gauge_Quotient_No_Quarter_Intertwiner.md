# Cone Derivation Ledger v15.642 — Lane A: headless bicone polarity completion is an ordinary directed rotor, not a quarter-sector source

**Date:** 2026-11-10. **Parents:** original two-body bicone model `payloads/two_body_bicone_v15_428/REPORT.md` (explicitly headed dipoles, headless shape and polarity-phase absent); v14.862–869 and v15.572 (bicone algebra); v15.639 comparison of scalar/triplet swap grading and Casimir grading; v15.640 (Lane A) original moving-dipole angular parity; **External Audit Round 529 v15.641**, which independently confirms v15.640 and discloses the historical duplicate v15.640 audit/Lane A numbering; v15.625–628 q=2 geometric Casimir. **Status:** [D] exact quotient geometry, invariant function space and bounded-mode operator matching; [C] canonical quantum-rotor quantization of the classical headed-dipole source model; [O] any physical mapping from angular rotor parity to q=2 odd-quarter Casimir, gravitational coupling. **Immediately prewrite live HEAD:** 3293f9d8896743b58b9218d27df224b75d4642ee (external audit liveness). v15.642 collision search empty; related content search found only v15.640, and the present headless completion is new. Additive-only; all certified Suzuki/far-tail objects untouched; Suzuki-quarter physical weld remains parked.

## Gate 155 — minimal headless-axis/polarity bundle and exact quotient

Represent a bicone *shape* by an unoriented line, with an oriented representative n(θ)=(cosθ,sinθ), and distinguish a discrete dipole polarity s∈{+1,−1}. The gauge-redundant configuration is (θ,s)∈S¹×Z₂ with **local deck transformation** g:(θ,s)→(θ+π,−s). The physical dipole is d=s n(θ), and d(g(θ,s))=d(θ,s). The deck action is free, so the quotient is isomorphic to a *single ordinary circle* with gauge-invariant angle **β=θ+π(1−s)/2 mod 2π**. This is not a new fourfold cover or a new independently physical parity degree of freedom. The imported dipole-dipole interaction of v15.428, U_dd=(C_dd/r³)[d1·d2−3(d1·e)(d2·e)], is invariant under each g_i separately, as independently checked by exact trig for all polarities. In terms of β1,β2 it is *identically the original headed-dipole potential*, with no new force constant or field.

## Gate 156 — physical rotor Fourier space does not acquire quarter modes

Under standard scalar quantization of the configuration quotient, wavefunctions are ordinary 2π-periodic functions of β and have integer Fourier modes m∈Z. Equivalently, on the cover with bases |m,s>, m∈Z, define the deck pullback operator **T|m,s> = (−1)^m|m,−s>**. The invariant subspace T=+1 has for every integer m a unique normalized basis vector

**|m>_phys=(|m,+>+(−1)^m|m,−>)/√2.**

There is one physical rotor mode at *every* integer m, not an extra independent Z₂ tower and not a quarter-mode shift. The bare operator cosθ is deck-odd and not physical by itself. The polarity-dressed dipole component s cosθ is deck-even and satisfies exactly

**(s cosθ)|m>_phys = (|m+1>_phys+|m−1>_phys)/2**

(with the usual boundary truncation in finite numerical tests), reproducing ordinary cosβ. Same for sine. The formal q=2 quarter Casimir labels j=L/4 do not emerge or acquire a physical SU2 representation from this model.

## Gate 157 — physical simultaneous reversal parity is not the local quotient gauge

A physical reversal of a dipole d→−d is β→β+π with polarity/axis representative chosen accordingly, and it is **not** the local deck transformation (which keeps d fixed). The two-body potential is invariant under *simultaneous* physical reversal of both dipoles, but not a single reversal at fixed coupling. On canonical two-rotor Fourier states this conservation is exactly the previously established v15.640 **Π=(-1)^(m1+m2)**, not a new discovered grading. The local gauge operator T acts as +I on the physical state space, so it cannot supply a distinct physical even/odd sector. An equation Π=χ_geom=(-1)^L would demand a new physical mapping L≡m1+m2 (mod 2), absent from the original moving bicone geometry, phase-space action or coupling.

## Gate 158 — strict headless rotor alternative gives no compulsory quarter Casimir

If one removes polarity entirely and genuinely models an unoriented rotor θ≡θ+π, ordinary **scalar** wavefunctions satisfy ψ(θ+π)=ψ(θ) and only even θ-Fourier m survive. Choosing an **anti-periodic/sign-twisted quantum line** instead gives odd m, but requires a separate choice of quantum bundle/representation, not a consequence of bare headless geometry. Neither alternative forces quarter-valued angular spin, a q=2 odd-shell C_geom=j(j+1) with j∈1/4+Z/2, or an EM/G odd-rung intertwiner. This is a scoped negative for the *source-faithful minimal completion*, not a general obstruction to gravity-specific holonomy or an experimentally sourced internal charge.

## Exact reproducibility, collision discipline and audit

Conversation artifact `cone_headless_gate_155_158.zip` includes `cone_headless_gate/reproduce.py` and `REPORT.md`. The exact SymPy script was executed to PASS, testing every local deck transformation and classical potential, 14×14 finite cover matrices for m=−3..3, physical 7-mode projector V, V†(s cosθ)V=cosβ, gauge-oddness of bare cosθ, and physical two-body simultaneous parity. It uses SymPy integer powers for negative m, avoiding a Python floating-point exponent pitfall. All continuous identities are proved analytically; finite matrices are independent spot checks. No generated image and no frozen Suzuki edits.

**Conclusion:** the original bicone's headless shape/polarity issue is resolved mathematically by a free Z₂ quotient. Its gauge-invariant physical rotor is the already-existing headed-dipole rotor, and the interaction's conserved simultaneous reversal parity cannot be identified with the quarter-mesh gravitational Casimir grading without a new, independently justified carrier map. No G, new force law, new phase coupling or novel G-free tidal prediction derived.

**HANDOFF:** external-audit, gravity, sandbox; check free Z₂ quotient and β map, deck operator/invariant basis and exact projected dipole matrix, distinguish physical dipole reversal from gauge representative change, and verify absence of quarter-spin in standard scalar quantization. Preserve duplicate-number v15.640 historical records, frozen Suzuki work, and previous certified Casimirs.

**Next gate:** stop searching for a parity-based EM/G identification in the unchanged bicone model; test whether the *original sourced cone dynamics* makes a physically new dimensionless response beyond classical dipole theory/gradiometry. If it does not, retain the negative conclusion rather than adding another auxiliary cover.
