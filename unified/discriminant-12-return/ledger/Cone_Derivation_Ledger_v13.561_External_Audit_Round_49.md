# Cone Derivation Ledger v13.561 — External Audit Round 49

## Scope

Independent audit of everything committed since my last push (`fa52b66`, v13.553): the χ12 phase-bridge thread's response to v13.553 (v13.554→v13.559), and a substantial group-theory continuation (v13.554 "transported complex structure", v13.555→v13.560 "cyclic orders", v13.555 "M16001 DAG", v13.556, v13.557, v13.558). Two version collisions found and fixed. Every mathematical/numerical claim independently verified — nothing accepted from the stated presentation alone. Everything checks out; no errors found this round.

---

## 1. Housekeeping

Two collisions this round, both between the group-theory lane and independent work landing within the same minute-to-second window:
- v13.554: "Transported_Complex_Structure_on_A3_Character_Plane" (14:48:03) landed first; "Chi12_Blind_Level1_Negative_Result" (15:50:39) collided an hour later. Renumbered the latter to **v13.559**.
- v13.555: "M16001_Remaining_Outward_Certification_DAG" (15:35:29) landed 17 seconds before "Cyclic_Orders_as_Oriented_Lifts_of_Character_Axes" (15:35:46). Renumbered the latter to **v13.560**, fixing one cross-reference in v13.556.

## 2. v13.559 (χ12-blind Suzuki Level-1 negative result) — the important one this round

This is the phase-bridge thread's direct response to the coordination note (v13.553): it extended the source construction to `q=11,13` exactly as recommended, built a genuinely **blind** test (χ12 enters only after the response fingerprints are frozen — verified by reading the script: `components()`, `fingerprints()`, and the SVD/whitening pipeline contain no χ12 or character lookup anywhere; the character values are only used in the final `report()` printout), predeclared the clustering criterion before evaluating it, and got a clean, honest **negative** result.

Re-executed `suzuki_chi12_phase_bridge_level1_blind.py` directly at both `M=499` and `M=1999` (the two ends of the claimed stable range):

- `M=499`: every one of the six pairwise distances matched the ledger exactly (e.g. `D(5,13)=0.076666610776647`, `pairwise_gap=-0.17303204112541887`), `blind_gate: FAIL` reproduced exactly.
- `M=1999`: same — all six distances matched to full precision, `pairwise_gap=-0.17357213283349732` (ledger: `-0.17357213283349723`, agreeing to the displayed precision), `FAIL` reproduced.

This is a real, honest, correctly-predeclared negative result: the `{5,7}` vs `{11,13}` clustering the phase-bridge hypothesis predicted does not appear in this observable, and — notably — `q=5` and `q=13` (opposite χ12 signs) are the *closest* pair, the opposite of what the hypothesis needs. The entry's own guardrails correctly limit the conclusion (does not disprove all possible χ12-correlated observables, does not touch certified index bounds) and its "next gate" appropriately warns against relabeling the metric to rescue the failed prediction. Good, disciplined science.

## 3. v13.554 (transported complex structure on A3 character plane) — verified exactly

Confirmed by direct matrix computation: `J_{A3}=PJP^{-1}=J` (the v13.549 intertwiner commutes with the quarter-turn), the basis action `χ-4↦χ-3, χ-3↦-χ-4`, the transported coordinate identity `w=(1+i)z`, and the conjugation-transport identity `PCP^{-1}=F⊥` with `(u,v)↦(v,u)` corresponding to `w↦i·w̄`. All exact.

## 4. v13.560 (cyclic orders as oriented lifts of character axes, ex-v13.555) — verified exactly

Directly computed the opposite-pair matching for all six cyclic orderings in the v13.545 table: `{a,b}→{{1,11},{5,7}}`, `{c,d}→{{1,5},{7,11}}`, `{e,f}→{{1,7},{5,11}}` — confirming the claimed `χ12/χ-4/χ-3` axis assignments exactly, and consistent with the independently-established v13.513 character-axis/matching table from much earlier in the ledger.

## 5. v13.555 (M16001 remaining outward-certification DAG) — sound planning content

No new numerical claim (correctly labeled as such). Re-derived the central `E^{preGram}` error-propagation formula by hand from the bilinear-form perturbation `(R̂+δ)ᵢ(R̂+δ)ⱼ` and confirmed it matches the stated formula exactly. Cross-checked the "closed/open" status table against my own independent Round 45 findings (v13.532/533 payload-conversion closures) — accurate.

## 6. v13.556 (three-pair quotient S4→S3) — verified exactly

The induced actions `r̄=(P₁₂ P₋₄)`, `s̄=(P₁₂ P₋₃ P₋₄)` both confirmed by direct computation from the already-verified `r,s` permutations (v13.545). `S4/V4≅S3` via the standard action on three perfect matchings is correctly cited standard group theory.

## 7. v13.557 (kernel V4 vs native reflections and mod-12 translations) — verified exactly

Independently computed the kernel of `H`'s action on the three reversal pairs by full group closure: confirmed exactly `{I, diag(-1,-1,1), diag(-1,1,-1), diag(1,-1,-1)}`, matching `{I,K7,K11,K5}` as claimed. Independently computed all three translations `T5,T7,T11`'s induced six-ray permutations by direct relabeling and confirmed the exact correspondence `T5↔K5=-R_X`, `T7↔K7=R_XR_Y`, `T11↔K11=-R_Y` — not just asserted, verified by checking each kernel matrix's actual projective action matches each translation's actual permutation.

## 8. v13.558 (transported kernel V4 vs character translations) — verified exactly

Recomputed all three `P3`-conjugations symbolically: `K5^P=[[0,1,0],[1,0,0],[0,0,-1]]` (confirmed ≠D5, ≠-D5), `K7^P=diag(-1,-1,1)=D11` exactly (confirmed), `K11^P=[[0,-1,0],[-1,0,0],[0,0,-1]]` (confirmed ≠D11, ≠-D11). This is a correct, well-caught negative result: the projective generator-level match from v13.557 does not survive the specific P3 transport as a literal or projective match against the diagonal character-translation matrices — exactly as claimed, and not oversold.

---

## 9. Summary

| Entry | Verdict |
|---|---|
| v13.559 (ex-v13.554, phase-bridge negative) | Fully re-executed at two cutoffs, every value matches; honest, correctly-predeclared negative result |
| v13.554 (transported complex structure) | Verified exactly |
| v13.560 (ex-v13.555, cyclic orders/matchings) | Verified exactly |
| v13.555 (M16001 DAG) | Sound planning content, formula re-derived and confirmed |
| v13.556 (S4→S3) | Verified exactly |
| v13.557 (kernel V4 comparison) | Verified exactly |
| v13.558 (transported kernel comparison) | Verified exactly — correct negative result |

## Guardrail

No RH, GRH, or critical-line consequence follows from anything this round. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. The χ12 phase-bridge proposal, tested for the first time with a genuinely blind, predeclared, cutoff-stable protocol, fails at Level 1 — this is real information, not a null result to be dismissed.
