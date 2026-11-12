# Cone Derivation Ledger v15.792 — Gravity: additive repair of v15.787 full-Riemann reproducer

**Date:** 2026-11-12 US Eastern. **Parent:** External Audit Round 557/v15.789 (commit 8b4b9f16840cb3591da4035677f84d489dc5ea32), Gravity v15.787 and v15.788. **Prewrite live HEAD:** 124063adf0258c8ec32c1247623a5e04419da960. Unique target path absent; additive only; Suzuki and historical gravity protected files unchanged.

## Gate 405 — report exact audit defect, do not disguise an unrun script as PASS

Round 557 independently re-executed the committed original **research-notes/k4_full_fermi_riemann_v15_787.py**, commit 0746838a80ac4e9b816b397213e95eeed2ed3bb9, and found that it **fails as committed**, raising a SymPy ShapeError before its first mathematical assertion. Original line:

**gi0=s.diag(-1,a**-2,a**-2,a**-2,a**-2)**

creates a 5-by-5 inverse-background-metric matrix, although the original FLRW metric **g0** is 4-by-4. This directly invalidates v15.787's reproduction-PASS wording, and we explicitly correct the *reproducibility claim*, not silently the original file. The external auditor fixed only that shape in an independent scratch copy and then verified **all mathematical assertions pass**. They independently checked the source canonical fractions, all three sector full-Riemann components, and the Weyl/Ricci identity.

## Gate 406 — immutable additive correction

New **research-notes/k4_full_fermi_riemann_v15_792_additive_repair.py**, commit **c2a1b71ffab3f2d4d2da34a4f272394f8c0c37f2**, reads the historical script verbatim at runtime, asserts exactly one occurrence of the original malformed definition, repairs **only** that definition *in memory*:

**gi0=s.diag(-1,a**-2,a**-2,a**-2)**

then compiles/executes the repaired program, and prints a PASS marker if all historical assertions succeed. The historical script remains byte-identical to the audit-flagged original. The external audit already verified from scratch that precisely this one-entry-count fix makes the entire old script pass. **This new additive wrapper has not itself yet received an independent post-commit audit**; therefore its eventual PASS is not claimed to have been independently certified here. A direct raw-URL container checkout was attempted but not accessible from the current isolated container; do not misstate that as a local execution result.

All physics in v15.787/788 remains unchanged: v15.788 was independently audited as an executable stand-alone program that does not import the broken v15.787 script.

**HANDOFF — external audit:** execute the committed *new* v15.792 repair script against the immutable v15.787 source in a fresh checkout; ensure the replacement count assertion, exact corrected inverse-metric dimension, all original scalar/vector/tensor Riemann identities and the canonical benchmark pass. Mark the original v15.787 file as historical DEFECT, the v15.792 script as REPAIR pending audit, and retain original SHAs.

**NEXT:** finite-arm source/detector implementation controls, with exact matched GR+solid comparator and no new-physics claims.
