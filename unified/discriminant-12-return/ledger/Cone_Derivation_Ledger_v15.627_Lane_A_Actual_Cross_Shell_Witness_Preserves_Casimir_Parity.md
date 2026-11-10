# Cone Derivation Ledger v15.627 — Lane A: the existing cross-shell Casimir witness preserves, rather than exchanges, EM/odd-quarter parity

**Date:** 2026-11-10. **Parents:** v15.135 §5 Casimir sector grading, v15.602 §3 cross-shell witness, v15.625 recovered all-q C spectrum, v15.626 newly derived Casimir-phase projector and chosen minimal quarter-rung shift. **Status:** [D] exact all-q index and parity identity; [C] cross-shell witness is chosen, not a physical process; [O] EM/G dynamical cross-sector coupling. **Prewrite checked live HEAD:** 3b9f502dc28efb7d359098025b389cef8d04a315; v15.627 collision search negative. Additive only; frozen Suzuki production untouched.

## Gate 118 — critical distinction between the actual v15.602 cross-shell witness and a minimal quarter-rung shift

The generalized cross-shell witness of v15.602 has target j'=j+(q−1)/q, with original shell index j=L/(2q). Therefore the target integer shell index is

**L'=2qj'=L+2(q−1).**

This increment is even for *every* positive integer q. From v15.626, the original geometric all-mesh Casimir spectral grading is

**χ_q=exp(4π i q² C_{q,L})=(−1)^L, C_{q,L}=L(L+2q)/(4q²).**

Consequently, for every individual nonzero source-to-target matrix element of v15.602's T_{q,L},

**χ_target T_{q,L}=T_{q,L} χ_source, so [χ_q,T]=0** on the direct-sum shell tower.

In particular q=2 gives Δj=1/2 and ΔL=2; both EM (L even) and proposed gravity-only (L odd) classes are preserved by T. Its exact relation T†T=2E is consistent with this grading, and it provides no EM↔G transition. This is not a negative about a generic odd-rung interaction; it is a precise selection rule for the **actual previously constructed cross-shell witness**.

By contrast the separately chosen minimal geometric shift U:|L,i⟩→|L+1,i⟩ has ΔL=1, {χ,U}=0 and P_± U P_±=0 (v15.626). That U was not derived as a physical gravitational interaction, does not carry the same strengths as T_{q,L}, and must not be substituted for T. Within-shell EM/Schwinger ladder steps have ΔL=0 and preserve grading. A generic two-rung shell shift preserves χ but changes the scalar C value, so [χ,T]=0 does **not** imply [C,T]=0.

## Direct exact verification and significance

Fraction-arithmetic check for q=2..12, L=1..26 confirms target integrality L'=L+2(q−1), exact even parity of 4q²(C_target−C_source), and equality of χ eigenvalues. Algebraic parity proof establishes all q without relying on the finite test. Script in conversation reproducibility archive `cone_casimir_sectors_115_118.zip` under `cross_shell_check.py`; the archive also contains the v15.626 matrices and report.

**Conclusions:** the Casimir grading is already established and is exactly recoverable as a phase of its geometric spectrum; however the specific available boundary/cross-shell witness **does not couple EM to G**. The quarter mesh remains a mathematically distinguishable proposed gravitational carrier, not a derived gravitational transition. A physically allowed operator with odd ΔL, consistent with gauge/energy symmetries and independently fixed matrix elements, remains the next missing object. No value of G, force law or energy splitting follows.

**HANDOFF** target external-audit, gravity, sandbox; status open. Independently check all-q L' parity and that operator T_{q,L} is *not* the same as the minimal quarter-rung U. Ensure v15.626's abstract shift example is never described as the actual v15.602 cross-shell witness. Suzuki quarter physical integration remains parked; frozen production untouched.
