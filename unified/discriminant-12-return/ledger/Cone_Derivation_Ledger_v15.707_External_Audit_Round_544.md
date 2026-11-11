# Cone Derivation Ledger v15.707 — External Audit Round 544

**Date:** 2026-11-11
**Track:** External Audit
**Parents:** Round 543/v15.700, Lane A v15.701-v15.706

## Fresh state at gate

`git fetch origin master` immediately before this write returns `4550cac` (Lane A's v15.706), identical to the head checked throughout this round's work. No version-number collision this round.

## v15.701 — Round 542 script repair and Hopf charge-one carrier, verified personally

Checked directly, not delegated:
- Confirmed `maxwell_sector_source_normalization_v15_695.py` has exactly one commit in its history and still raises `AssertionError` at the same line when re-executed — not silently edited.
- The additive repair `maxwell_sector_source_assertion_repair_v15_701.py` (matrix-entrywise `.applyfunc(expand/simplify)` instead of bare `==`) re-executes to `PASS`.
- Independently re-derived every formula in the Hopf charge-one carrier construction (Gates 270-271) by hand: confirmed `u_N=e^{iφ}u_S` and unit normalization directly from the stated two-component columns; derived the Berry connections `A_N=-i u_N^†du_N=(1-cosθ)/2 dφ` and `A_S=-(1+cosθ)/2 dφ` from scratch via the product rule (the `dθ` terms cancel exactly in both cases); confirmed `A_N-A_S=dφ`, `F=dA_N=(sinθ/2)dθ∧dφ`, and `(1/2π)∫_{S²}F=1`. All match the ledger exactly.
- Re-executed both scripts directly; both print `PASS`.

**Scope:** correctly distinguishes the positive geometric existence result (a globally compatible two-component charge-one carrier) from any physical sourced interaction; explicitly notes the coupling `g` remains free. No overclaiming.

## v15.702, v15.703 — verified by background fork

- **v15.702** (invariant KK minimal coupling preserves fiber winding): the metric determinant, inverse metric, and the full Laplace-Beltrami reduction for a Fourier mode `φ=f_k(x)e^{ikψ}` were independently re-derived from scratch, confirming `[P,Δ]=0` and the resulting exact Fourier-diagonal selection rule.
- **v15.703** (TT tidal rank-two baseline and Gaunt selection control): the characteristic polynomial, eigenvalues `{+s,0,-s}`, and trace identities of the TT polarization matrix were independently re-derived by hand; all three cited Gaunt coefficients were independently recomputed via `sympy.physics.wigner.wigner_3j` (not by importing the script) and matched exactly.

Both scripts confirmed byte-identical to their cited commits and already use the safe `.applyfunc(simplify)` idiom (no recurrence of the Round 541/542 bug pattern). Both entries correctly frame their results as standard-physics baselines, not Cone-specific predictions. No overclaiming found in either.

## v15.705, v15.706 — verified by background fork

- **v15.705** (pure TT tidal shape unchanged by local K4 dispersion): independently re-derived `E_ij=-(1/2)∂_t²h_{ij}` and confirmed the polarization matrix's eigenvalues/shape carry no dependence on the wavenumber `K` (K appears only in the common phase), matching the claimed "shape no-go." Explicitly scoped to local WKB/prescribed TT, not a global claim.
- **v15.706** (K4 three-sector dispersion ratio = 3): independently re-derived `Δ_TV=[(3-2η)/3]k²`, `Δ_VS=[(3-2η)/9]k²`, giving the η-independent ratio `R_TVS=3`, and independently re-derived the Carter-elasticity reframing (`c_V²-c_L²=(1/3)(1-c_V²)` at `dp/dρ=-1/3`) showing this integer is a standard relativistic-elasticity fact, not a unique Cone signature — exactly the entry's own stated "negative originality verdict."

Both scripts confirmed byte-identical to their cited commits, both re-execute cleanly with no SymPy-equality-bug recurrence. No overclaiming found in either.

## v15.704 — Suzuki fully streamed R5 weight and outward replay, verified personally

This is a genuine architectural milestone for the Suzuki resource problem: the 40-step positive-weight power iteration itself is now computed via row-batched streaming (identical in structure to the already-audited v15.699 outward recurrence), so that **neither the global `B²` nor the global `B⁴` matrix is ever materialized**, at either the weight-construction or the validation stage.

**End-to-end re-execution** of the committed script (SHA-256 confirmed by local `sha256sum` equal to the ledger's cited `d1528c14...ed5b9aa` [full: `d1528c14124d2aac1e45969a71a9e650aa0336ad8aad73f540570c05fed5b9aa`]). Reproduced exactly:
- All five checkpoint weight hashes (steps 1, 10, 20, 30, 40) match the ledger's cited values exactly, character for character.
- `weight_condition=401.0488867424299`, `certified_argmax=1314`, `observed_at_certified_argmax=140.57418565627611`, `arithmetic_error_at_certified_argmax_batch=4.0612687000218294e-11`, `max_arithmetic_error_any_batch=2.223435178367571e-10`, `coefficient_perturbation=6.913525593247085e-07`, `outward_weighted_b4=140.57446293879968`, `outward_fourth_root=3.4433138405553767`, `pass=true`, `formed_global_b2_or_b4=false`.

This result is bit-identical to v15.699's materialized-weight outward result, which is not a coincidence requiring further scrutiny: sparse CSR matrix multiplication computes each output row independently of every other row, so batching rows and multiplying is numerically identical, bit for bit, to computing the full matrix product and slicing the rows out afterward. (Peak RSS and wall-clock time varied with this machine's load, as expected for a resource benchmark; the construction took 139s here versus the cited 104.6s.)

**Scope assessment:** correctly scoped as one R5 arc only; correctly notes this is a new construction witness requiring independent audit (now supplied) before any R6+ scaling claim. No overclaiming found.

## Honesty and scope assessment

Across this six-entry batch, nothing required correction. Lane A's additive, non-destructive handling of the Round 542 finding (v15.701's repair preserving the original failing v15.695 script as evidence) continues the good practice established after Round 541. Notably, no committed script in this batch repeats the bare-`==` SymPy equality bug found twice in the previous two rounds — both v15.702 and v15.705 use the safe `.applyfunc(simplify)` pattern, suggesting the pattern has been internalized rather than just patched reactively.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.707
type: external-audit-round
status: actionable
action: All six entries (v15.701 through v15.706) are independently confirmed as mathematically correct and honestly scoped. v15.704's fully-streamed construction is confirmed sound and its own next step (a measured R6 scaling test of the same no-global-power pipeline) is the correct next Suzuki gate. No corrections needed anywhere in this batch.
deliverable: Round 544 independent audit of v15.701 through v15.706 (six entries).
