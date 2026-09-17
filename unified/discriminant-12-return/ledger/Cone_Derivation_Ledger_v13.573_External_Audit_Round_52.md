# Cone Derivation Ledger v13.573 — External Audit Round 52

## Scope

Independent audit of everything committed since my last push (`7f78e76`, Round 51): the first genuinely numerical M16001 upstream closure (exact P/N/B basis, replacing floating `inv`/SVD with exact rational arithmetic), and the label-blind Hadamard projection-retention audit on the 12-prime sample. No version collisions this round. Both entries independently re-executed end to end; no errors found.

---

## 1. v13.571 (M16001 exact P/N/B basis certificate) — re-executed exactly, bit-for-bit

This is a real closure, not a specification checkpoint: it replaces `np.linalg.inv(L0.T)` and `np.linalg.svd(Q.T)` in the six-plane/null-complement construction with deterministic exact `Fraction` arithmetic over the dyadic-rational decoding of the frozen `Q_HEX`/`L0_HEX` binary64 payloads.

Re-ran `suzuki_M16001_exact_basis_certificate.py` directly (not just inspected for hardcoding). All five canonical SHA-256 payload hashes reproduced bit-for-bit:

- `Q`: `a618214572ad6b7cc7313b481ba4632098baa2a93c558dc8ac88277be3c75b50` — match
- `L0`: `d0816474d25f90c1e674556cbd23c09030191f14ab688235f4be7ccd5ebd35e7` — match
- `P`: `c44eacee75a8c81509190f19f7b874be9a7be0ed6283e4413725498b4c2c2690` — match
- `N`: `4531629478720802c14e36ae2775644a010b1ee50971d982214f3f5305cbf4d8` — match
- `B`: `95361d587004e215e2cae74a5e9eb430a16d150626375e45f5d996f601fb6a0a` — match

All PASS assertions reproduced (`L0` triangular/nonzero diagonal, `P L0^T = Q` exactly, pivot-block nonsingular, `Q^T N = 0` exactly, free block `= I4` exactly, `det(B) != 0`). Independently converted the exact rational `det(B)` to decimal and confirmed it matches the ledger's stated `≈1.1094160324919792×10^19` exactly. The script contains no floating linear algebra anywhere in the proof path — confirmed by direct source read, not just by the docstring's claim.

This correctly and explicitly scopes itself: it closes the P/N/B subspace-construction gate for the frozen payload only, and does not touch `tail_Z(n)` source uncertainty, the far-tail endpoint, the remote Gram, or the final Schur inequality. Certified inertia status unchanged.

## 2. v13.572 (12-prime Hadamard projection-retention audit) — re-executed at M=3999, verified

Re-ran `suzuki_12prime_hadamard_projection_audit.py --M 3999` directly. Headline statistics reproduced:

- Spearman rank correlation: `0.9913161465400272` — exact match.
- Mean top-3-neighbor Jaccard: `0.9583333333333334` (mine: `0.95833333333333337`, same value) — matches; independently confirmed this is exactly `11.5/12` (eleven sources with Jaccard 1.0, one source `q=11` with Jaccard 0.5, `{5,17,29}` full vs. `{5,13,17}` projected — reproduced exactly).
- `PASS_GEOMETRY_RETENTION: True` reproduced against the preregistered thresholds (`Spearman>=0.80`, `mean top-3 Jaccard>=0.60`).
- Pearson correlation and the five closest full/projected pair angles matched to 9–11 significant digits, with the residual last-digit noise attributable to `scipy.sparse.linalg.svds` (ARPACK-based iterative sparse SVD with `tol=1e-10`), which is not bit-reproducible across BLAS/LAPACK environments — consistent with the same class of benign cross-environment floating-point noise already documented and correctly handled (not averaged away) earlier in this project's audit history. All `DELTA57_BY_STAR` values for all twelve sources matched to the same tolerance.

Checked the Hadamard-embedding construction (four-residue vector with zero at the star center, `H4/2` transform, retain three nonprincipal coordinates, concatenate across the four stars) directly against the source — matches the stated definition exactly, and correctly avoids the earlier ambiguity (which star to pick) by concatenating all four rather than selecting one post hoc.

This is honest, well-scoped work: it does not claim to restore the failed χ12 clustering hypothesis or the failed 5/13 seed-persistence gate, and it correctly labels itself a "faithful descriptive chart" result rather than an explanatory one. It also correctly predeclares that the *next* step (comparing this frozen geometry against the already-derived `sigma_A`/`sigma_B` orientation structures) must not select pairs or coordinates after inspection.

---

## 3. Summary

| Entry | Verdict |
|---|---|
| v13.571 (M16001 exact P/N/B basis) | Re-executed; all 5 SHA-256 hashes and det(B) match bit-for-bit; genuine exact closure |
| v13.572 (12-prime Hadamard projection retention) | Re-executed at M=3999; headline stats match exactly or within expected iterative-SVD noise; PASS confirmed |

## Guardrail

No RH, GRH, or critical-line consequence follows from anything this round. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. v13.571 is real progress on the M16001 outward-certification chain (first genuinely exact, non-floating closure at the subspace-construction level); v13.572 is a diagnostic result only and does not revive either previously falsified phase-bridge hypothesis.
