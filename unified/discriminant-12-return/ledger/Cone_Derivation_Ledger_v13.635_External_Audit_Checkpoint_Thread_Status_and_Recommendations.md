# Cone Derivation Ledger v13.635 — External Audit Checkpoint: Thread Status and Recommendations

Date: 2026-09-21

Status: advisory checkpoint from the external audit thread, not a new mathematical result. This entry consolidates a status assessment and concrete recommendations across the four currently active threads, at the project owner's request, so each thread can read it directly rather than have the assessment relayed secondhand.

## 0. Live collision/relevance check

The live ledger was fetched immediately before this write. Tip is v13.634 (four-term magnetic endpoint residual-order audit), which independently reinforces one of the points below (Section 2). v13.635 is free.

## 1. Purpose of this entry

This is a coordination note, not a derivation. Nothing here should be treated as a new theorem, certificate, or numerical result — it summarizes what External Audit Rounds 50-67 (v13.55x-v13.632) found across the four active lines of work, and recommends what each thread should consider doing next. Treat every "recommendation" below as exactly that: a recommendation, open to disagreement.

## 2. chi_-4 / L-function thread — recommend a closed-avenues consolidation, not further blind repair attempts

Status: two independent carrier constructions have now failed A-robustness in direct succession — the naive bare-Jz carrier (v13.620) and, after a genuine and independently-certified operator-level repair (v13.623, v13.625, both independently re-audited), the domain-faithful Friedrichs-Galerkin carrier as well (v13.627), with a clean `r_1(A)~pi/A` box-mode law. v13.629 then showed this box branch is already present with the arithmetic kernel turned off entirely (free/endpoint origin, not created by g_-4), and v13.633's homotopy continuation confirmed those are genuine continuously-tracked branch displacements, not a root-relabeling artifact.

This is real, hard-won negative information, presently scattered across five-plus entries. Recommendation: write a single consolidation entry that states plainly (a) which constructions are now closed (naive carrier, repaired Galerkin carrier, both as direct ordered-zero-vs-beta-zero comparisons), (b) the one open question that both v13.629 and v13.633 already converge on independently — what renormalized or A-to-infinity-limit-aware object should replace direct ordered-root comparison — and (c) that the chi_-4 screw-kernel source-normalization caveat is still unresolved and should probably be addressed before further A-robustness attempts, since an unverified normalization could itself be contributing to the box-branch dominance. This is not a request to abandon the thread; it is a request to stop re-attempting variations on direct ordered-zero comparison until the renormalization question is actually engaged.

## 3. LQG/tetrahedron thread — recommend a synthesis note; this sub-result is done

Status: v13.624 (three paths — magnetic/SU(2), Racah, tetrahedral-volume — are spectrally inequivalent as raw operators from j=3/2 up) and v13.631 (explicit constructive orthogonal D8 intertwiner between any two flattened carriers, plus the integer-j zero-line extension) together form a complete, closed statement. Both were independently re-derived from scratch in External Audit Round 66/67 — v13.624 via independent sympy reconstruction of all three operators from raw formulas, v13.631 via independent construction on freshly generated random test operators satisfying its stated hypotheses, not on anything the ledger itself produced. Every boxed claim in both entries checked out exactly.

Recommendation: this deserves its own synthesis note before it gets buried under unrelated rounds, the same way the divisor/ladder/magnetic parabola pattern was pulled into v13.598. Two things the synthesis note should be explicit about, precisely because it will be an attractive result to over-read: (1) this is a representation-theoretic unification — three physically distinct operators sharing one flattened D8 skeleton — not a claim of physical equivalence between spin drive, Racah recoupling, and LQG volume dynamics; the spectral-inequivalence half of v13.624 is exactly what rules that stronger claim out. (2) There is currently no established link between this result and the chi_-4/L-function thread (Section 2) or the magnetic-driver thread (Section 4); any such link is presently only the project owner's own outside observation (the physical resonance with Coldea et al.'s E8 golden-ratio spin-chain result), not something derived in this ledger.

## 4. Magnetic-driver thread — no synthesis yet; keep going, the guardrails are doing their job

Status: healthy, still-growing perturbative expansion, now through 8th order (v13.630), with every coefficient independently reproduced (Round 67: adaptive 50-digit ODE + Richardson extrapolation for the raw Floquet coefficients, independent sympy reconstruction for the derived endpoint series) and, as of v13.634, an independent high-precision check that the actual remainder after all four known phase/inversion terms is genuinely `O(eps^9)`/`O(eps^10)` rather than an artifact of the expansion method. This is exactly the discipline this kind of perturbative program needs.

Recommendation: no consolidation note yet — a synthesis now would just freeze a snapshot of an expansion that is still being actively and correctly extended. The standing guardrail (no uniform large-j remainder bound, no all-orders closed form) remains the right caveat and should stay attached to every future order.

## 5. M16001 certificate thread — blocked, not close; fix the bug before anything else

Status: `research-notes/suzuki_M16001_orthonormal_sixplane_certificate.py` does not run. It crashes with `IndexError` because it reuses `chol_upper`/`inv_upper` from `suzuki_M16001_orthonormal_nullspace_certificate.py`, both of which hardcode `n=4` (sized for the earlier 4x4 nullspace problem) on what is now a 6x6 Gram matrix. This was independently diagnosed and reported in External Audit Round 66 (v13.628) and remains unresolved as of this checkpoint.

Recommendation: this is not "almost done" — no six-plane certificate has actually been produced, passing or otherwise, by the code as committed. Before any further claim is built on top of the six-plane result, generalize the two helper functions to read `n` from the input matrix shape, rerun, and report the actual outcome (pass or fail) rather than the outcome that was assumed. This is a small, mechanical fix; it is flagged here mainly so it does not get silently skipped while other threads move on.

## 6. Summary

| Thread | Recommendation | Reasoning |
|---|---|---|
| chi_-4 / L-function | Write a closed-avenues consolidation note; do not re-attempt direct ordered-zero comparison without engaging the renormalization/limit question | Two independent constructions have failed the same gate; the open question is already visible in v13.629/v13.633 |
| LQG/tetrahedron | Write a synthesis note now | v13.624 + v13.631 form a complete, independently-verified closed result |
| Magnetic driver | Continue as-is, no note yet | Healthy ongoing perturbative program with strong internal remainder-order checks |
| M16001 certificate | Fix the `n=4` hardcoding bug before claiming anything about the six-plane certificate | The certificate script has never actually executed to completion |

This checkpoint will be treated by the external audit thread as a standing reference; the next "External Audit Round" entry will note whether any of the four recommendations above have been acted on.
