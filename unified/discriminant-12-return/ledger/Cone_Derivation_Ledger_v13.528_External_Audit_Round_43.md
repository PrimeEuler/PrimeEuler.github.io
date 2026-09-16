# Cone Derivation Ledger v13.528 — External Audit Round 43

## Scope

Independent audit of v13.524, v13.525, v13.526, v13.527, committed since my last push (`1599e32`, v13.523), plus the figure/paper rebuild and new CI workflow. Every mathematical claim independently re-derived or re-executed; every arithmetic script re-run directly. One genuine reproducibility finding, already caught and correctly handled by the project itself before I could raise it.

---

## 1. v13.524 (character descent and χ12 eigenspace decomposition) — exhaustively verified

Independently rebuilt the full simultaneous-parity structure in code:

- The `(ε_K,ε_S)` sector table for all eight characters of `G=F2³` (`ε_K=(-1)^{p+q+s}`, `ε_S=(-1)^s`): confirmed exactly against the claimed four-sector table.
- `K^⊥` splits into the `S`-even pair `{1,χ12}` and `S`-odd pair `{σχ-3,σχ-4}`: confirmed.
- Projector commutativity `Π_K^{εK}Π_S^{εS}=Π_S^{εS}Π_K^{εK}`, and that `Π_K^+Π_S^+` is exactly rank 2 with Fourier support `{1,χ12}` (verified via eigendecomposition of the actual 8×8 operator, not just the claimed labels): confirmed exactly.

No error found. This correctly sharpens v13.515/518's χ12-survival mechanism into a clean simultaneous-eigenspace statement.

## 2. v13.525 (figure-source sign audit and carrier separation) — confirmed, including direct source check

This entry catches a real risk: conflating the cone figure's visible `X→-X`/`Y→-Y` reflections with the abstract `U(24)` arithmetic sign bit. Checked the actual (recently extended) figure generator `figures/discriminant12_mod12_v4_cone_triple.py` directly — confirmed it does plot `xs=[c,-c]` and both `±half` (i.e. `±√r`) exactly as described, validating the entry's claim that the two visible reflections are genuinely present in the source. The distinction it draws (`V_geom` acting within a shell vs. `V_arith` indexing the four shells) is a correct and useful clarification, not yet a new theorem, and is appropriately left as an open question (§9) rather than overclaimed.

## 3. v13.526 (M16001 Frobenius outward replay) — re-executed; confirms a real cross-environment discrepancy

Re-executed `suzuki_M16001_integrated_frobenius_replay.py` locally (numpy 2.4.6, scipy 1.17.1, vs. the CI's numpy 2.5.3, scipy 1.18.1):

- My result: point Frobenius residual `7.8022588445607556094e-15`, outward endpoint `9.550294946230173122e-15`.
- Ledger's CI-reported result: point Frobenius residual `7.8288856433727728125e-15`, outward endpoint `9.582335208983397532e-15`.

These differ by ≈2.7e-17 in the point residual (≈0.3% relative) — larger than the sub-ppm floating-point wobble noted in earlier rounds, and reproducible (ran twice locally, identical both times, so not run-to-run noise on my end; must be a genuine numpy/scipy-version-dependent effect in the underlying LDL/Woodbury solve or reduction order). Checked whether this is absorbed by the already-charged entrywise error margin: the margin between the point residual and the charged envelope is ≈1.75e-15, roughly **65× larger** than the observed cross-version discrepancy, so it is comfortably covered *for this specific comparison*. I did not need to raise this as a new finding, because **v13.527 §4 independently caught and reported the identical discrepancy** (their two CI runs differ by the same `9.550294946230173122e-15` vs. `9.582335208983397532e-15` pair I found locally) and correctly declined to average it away, instead naming it as a reason the `X`-payload-provenance gate must be closed explicitly. That is exactly the right response, reached independently.

## 4. v13.527 (M16001 entrywise primitive residual propagation) — re-executed, all key numbers match exactly

Re-executed `suzuki_M16001_pole_FC_primitive_outward_transcript.py` and `suzuki_M16001_displacement_weighted_residual_radius.py` directly:

- Pole-FC entry radius: my run gave `1.9322245000793252e-20`, matching the ledger exactly. AFC addition-rounding charge: my run gave `1.937913948121446246e-20`, matching exactly.
- Full weighted-propagation script (15s runtime, vectorized): entrywise-recomputed max FF radius `9.022982959826540786e-16` (matches v13.521's independently-verified maximum exactly), max weighted residual-entry increment `1.2017055003645024938e-18` (matches exactly), outward Frobenius increment `1.5659242855578671182e-16` (matches exactly).
- A second `RuntimeWarning: invalid value encountered in divide` fires in this script (line 21, from the unmasked `ad*safe` term in the diagonal case before `np.where` selects the correct branch) — same benign pattern already traced and confirmed harmless twice in Rounds 40 and 42 (masked/discarded before affecting any reported value, confirmed here since all reported numbers match the claimed ones exactly).

This entry's central point — that the uniform-maximum FF guard (`9.14e-13` Frobenius impact) collapses by roughly four orders of magnitude once genuine entrywise weighting is applied — is independently confirmed by my re-run, and correctly not oversold as closing the seven-plane margin question.

## 5. Figure/paper rebuild and CI workflow

`figures/discriminant12_mod12_v4_cone_triple.py` was extended (confirmed via source read, §2 above) and the corresponding PNG/PDF artifacts were regenerated; this is consistent, mechanical output, not an independent claim requiring separate verification beyond the source check already performed. The new `.github/workflows/m16001-frobenius-audit.yml` is a small, reasonable CI job (runs the integrated Frobenius replay on `pull_request` touching `research-notes/`, uploads its output as an artifact) — no concerns.

---

## 6. Summary

| Entry | Verdict |
|---|---|
| v13.524 | Exhaustively verified exact |
| v13.525 | Confirmed, including direct check of the actual figure source |
| v13.526 | Re-executed; real cross-environment discrepancy found, safely margined, and independently caught by the project itself in v13.527 |
| v13.527 | Re-executed; every key number matches exactly; correctly avoids overclaiming |

## Guardrail

No RH, GRH, Suzuki-spectral, or critical-line consequence follows from anything in this round. Certified status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. The `X`-payload-provenance gate flagged in v13.527 remains the binding obligation before any of this arithmetic chain can be theorem-consumable.
