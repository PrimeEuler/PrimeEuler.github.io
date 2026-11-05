# Cone Derivation Ledger v15.414 — Lane A: all 40 signed pair translations are distinct

**Date:** 2026-11-05. **Lane:** A / Suzuki five-frequency commutator. **Parents:** v15.354, v15.364–400, v15.401, v15.405, v15.412–413. **Status:** [D] exact algebraic translation-label noncollision; [O] full operator-level cross-pair interference estimate.

**Pre-write collision check:** master HEAD `8762a434f890751a2205288a381d8c80772228ec`, which adds the independent v15.414 witness; v15.413 ledger already present. This is additive, no existing code altered.

For Q={2,3,4,5,7} there are ten unordered pairs q<r and four signs (sigma,tau) each. The transported q,r cross block has shift label

`lambda(q,r,sigma,tau)=sigma log q + tau log r = log(q^sigma r^tau)`,

which is a real translation on x in R/(2Z). In particular log4=2log2 is retained exactly, not treated as independent.

The replay witness enumerates the 40 exact rational numbers q^sigma r^tau using `fractions.Fraction`, and proves all **40 distinct**. Thus no two cross-pair signed groups have exactly the same real shift.

Modulo the period 2, if two shifts coincided one would have `log(u/v)=2k` for an integer k, hence rational `u/v=e^(2k)`. For k not zero this is impossible by the transcendence of exp(nonzero algebraic) (Hermite–Lindemann); for k=0 the rational labels would be equal, also excluded. Thus **all 40 shift labels remain distinct modulo 2**, not merely as real numbers.

Consequence: the v15.413 shared-row absolute-Schur sum cannot be reduced by aggregating coefficients from different cross pairs at an identical translation before taking magnitudes. The common row method has a certified value >5.5 at x=3/1250, already above the required v15.405 cross budget 4.249030150943723. This is a scoped obstruction to that particular absolute-row proof strategy; distinct shifts can still interfere at the operator-norm level through the same input vector, and **no lower bound on the joint cross operator norm** is asserted.

**Witness:** `research-notes/lane_a_v15_414_translation_collision_exact.py`, commit `8762a434f890751a2205288a381d8c80772228ec`. Run with plain Python 3; exact Fraction equality assertions and integer enumeration, no floating approximation.

**Next Lane A gate:** replace absolute row estimates with a genuinely operator-level construction (e.g. finite-word weighted-shift matrix and a certified C*-algebra norm enclosure, or an operator-valued Cotlar/Gram estimate) retaining interference among distinct shifts. Any such gate must certify the exact *physical* cross sum below 4.249030150943723 and must not substitute an artificial commutative model.

Production fences unchanged: chosen ell2 source provenance unresolved, full-K transfer inconclusive, v14.405/v14.406 finite-plus-gap PASS, v14.814 finite-far FAIL, C_S_32000, 3e-5 and .002, exactly-once transport charges preserved. No Sandbox job submitted.
