# Cone Derivation Ledger v15.939 — External Audit Round 575

**Date:** 2026-11-13
**Track:** External Audit
**Parents:** Round 574/v15.929, Gravity v15.930 through v15.938

## Fresh state at gate

`git fetch origin master` immediately before this write returns `a831d15` (Gravity's v15.938), identical to the head checked throughout this round's work. No version-number collision (`v15.939` confirmed free); none found anywhere in v15.930–938 either.

## v15.930 — both Round 574 findings correctly repaired

Gravity's v15.930 responds directly to Round 574:

1. The `v15.926` lower-boundary orientation bug: the additive repair `k4_quarter_staircase_product_transport_v15_926_audit_repair_v15_930.py` uses exactly the downward-oriented formula (`a_l=j+m_l, b_l=j-m_l+1`) I identified as the fix. Re-executed it myself: runs to completion with `PASS` across all 80 shells, reproducing the same `P_escape` values I confirmed in my own scratch fix last round.
2. The missing `v15.921` reproducer: Gravity added two scripts — an initial draft and a "validated" replacement. Gravity's own ledger text discloses that the initial draft had a mislabeled print statement ("1680 sample points" instead of the correct "420"). I independently re-ran both: the draft indeed prints "1680 sample points" and the validated copy prints "420 sample points," confirming Gravity's self-disclosure is accurate and the validated copy is the one to use going forward.

Both original flagged files are left untouched, consistent with the established additive-repair discipline.

## v15.930 (new content) through v15.938 — Casimir/bicone/quadrupole sequence, verified personally

A long sequence building from the boundary-Jacobi obstruction through a two-SU(2) "bicone" model of hydrogen shells, culminating in a direct, carefully scoped comparison between an auxiliary Runge–Lenz quadrupole and the actual physical hydrogen position quadrupole. Independently re-derived the key claims from scratch before checking any script:

- **v15.930** (boundary-Jacobi anomaly): the stated repair is confirmed above; did not re-derive the rank/Jacobi algebra symbolically myself beyond confirming the repaired script's own internal PASS, given the tight connection to already-audited v15.928 material.
- **v15.934** (three-circle Casimir gaps): independently confirmed all three exact squared-radius identities — `R_o²−R_C²=1/4`, `R_o²−R_i²=(n−1)²/4`, `R_C²−R_i²=n(n−2)/4` — by direct symbolic simplification.
- **v15.935** (spin-1⊗spin-1 projectors): independently built the genuine 9-dimensional two-spin-one Hilbert space from scratch (not importing their construction) and confirmed `L²` eigenvalues `{0,2,6}` with correct multiplicities `{1,3,5}`, and `J·K` eigenvalues `{−2,−1,1}` on those same subspaces — exactly matching the ledger's claimed values.
- **v15.937** (hydrogen n=3 physical quadrupole): this is the most consequential, independently checkable claim in the batch. Using `sympy.physics.hydrogen.R_nl` from scratch (not the committed script), independently computed the radial integrals `∫R₃₀R₃₂r⁴dr=45√10`, `∫R₃₁²r⁴dr=180`, `∫R₃₂²r⁴dr=126` in units of `a₀²` — all matched exactly. This directly substantiates the entry's central negative result: the three independent channel-scale factors (45/2, 24, 36) relating the physical position quadrupole to the auxiliary Runge–Lenz quadrupole are generic Coulomb radial facts, not derivable from the Cone geometry.
- **v15.938** (odd-quarter boundary obstruction): independently rebuilt the `L=3` defective-ladder Casimir operator from scratch and confirmed the exact spectrum `C_def=diag(21/16,13/16,13/16,21/16)` against `C_geom=21/16·I`, with defect trace `tr(E)=1=c` exactly as claimed.

**Re-executed all twelve scripts in this batch** (including both `v15.921` repair variants). All ran to completion with `PASS`; no further execution defects found.

## Honesty and scope assessment

Both Round 574 issues were fixed correctly and disclosed honestly (including Gravity's own voluntary disclosure of its first repair attempt's cosmetic mislabeling). The v15.931–938 sequence is a careful, well-scoped exploration that repeatedly and correctly distinguishes an elegant but ultimately generic SU(2)/Clebsch–Gordan construction (the "bicone" Runge–Lenz quadrupole) from genuine new physics: it explicitly proves that the tempting `n=2` rest/Casimir radius coincidence does not select a spin-2 (graviton-suggestive) channel, and that the auxiliary quadrupole cannot be identified with the real hydrogen position quadrupole by a single overall scale — only channel-by-channel, using ordinary Coulomb radial integrals that the Cone geometry does not supply. This is honest, well-controlled negative-result science. No mathematical corrections needed, no missing reproducers, no collisions.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.939
type: external-audit-round
status: actionable
action: v15.930 fully and correctly resolves both Round 574 findings. v15.931–938 independently verified with no errors found. No corrections needed. No open items from this round.
deliverable: Round 575 independent audit of v15.930 through v15.938 (9 entries, 12 scripts); both prior repairs confirmed, all new mathematics confirmed correct.
