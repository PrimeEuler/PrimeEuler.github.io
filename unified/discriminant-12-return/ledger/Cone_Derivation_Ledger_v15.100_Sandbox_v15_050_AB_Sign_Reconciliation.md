# Cone Derivation Ledger v15.100 — Sandbox: v15.050 A_B sign reconciliation (R389 handoff)

**Entry ID:** v15.100 (sandbox reconciliation; lane-request mode)
**Date:** 2026-10-29
**Author:** Sandbox (little Euler)
**Parents:** v15.050 (triplet-charge build, three-route κC closure), v15.051 (External Audit Round 389 — sign discrepancy flagged, explicitly unresolved by the audit).
**Payload:** `payloads/triplet_charge_sign_reconciliation_v15_100/` — `triplet_charge_fixed.py`, `fixed_output.txt`.
**Status:** [D] internal-consistency adjudication from v15.050's own constraints, sympy-verified. Additive only: v15.050 is untouched; no claim, charge, or verdict in v15.050 changes. κC = 1 remains a matching; G_derived = false.

## The discrepancy (per R389)

- Deposited prose (v15.050 NOTE.md and entry, reading R2): A_B = 1/a² − ω²((z1)² + (z2)²)/3, described in both places as the *matched (static) normalization*.
- Deposited script (triplet_charge.py): B2tr = Σ φ̇ᵢ² − tr(FFᵀ)/a² = ω²((z1)² + (z2)²) − 3/a² (full contraction, signature (+,−,−,−)), and its print line reports A_B as B2tr/3 = ω²((z1)² + (z2)²)/3 − 1/a² — the exact negative of the prose.

## Adjudication: the prose is right; the script's print line mislabels the quantity

Three independent internal checks, all verified symbolically:

1. **Static matching (the entry's own stated normalization).** At ω = 0, reading R2 must reduce to reading R1's A_B = 1/a² (time derivatives vanish; the two readings coincide). Prose at ω = 0: 1/a² ✓. Script's B2tr/3 at ω = 0: −1/a² ✗ — and it would make the static source W = C·A_B negative, contradicting every deposited static background.
2. **Algebra.** −B2tr/3 = 1/a² − ω²((z1)² + (z2)²)/3, identically the prose formula (sympy: difference exactly 0). So A_B = −tr B₂/3, not tr B₂/3: with signature (+,−,−,−) the full-contraction trace carries the opposite overall sign to the spatial-strain trace used in R1 (where A_B = tr B₁/3 is correct).
3. **The script's own canonical momentum.** The same script computes the Noether charge from π_I = (2C/3) φ̇_I, annotated "from L = −C A_B". That coefficient follows from L = −C·A_B only if A_B = −tr B₂/3 (the φ̇² term then enters L as +C φ̇²/3, giving π = (2C/3) φ̇). If the script's printed A_B = tr B₂/3 were the intended one, π_I and q₃ would both flip sign — contradicting Audit R389's independent canonical-momentum derivation, which confirmed q₃ = +(2C/3) ω ((z1)² + (z2)²) exactly. The charge, the verdict, and the prose all stand on the same sign; the print line is the lone outlier.

## The fix

`triplet_charge_fixed.py` (payload) changes exactly the one print line: A_B is now reported as −B2tr/3, with a comment recording checks 1 and 3. Re-run verification (2026-10-28): clean exit; output diff against the deposited script's output is exactly that one line — R1, q₃, and the Derrick lines are byte-identical.

Scope: R2 itself remains a never-previously-established reading, as the audit noted — this reconciliation settles internal consistency only (prose ↔ script ↔ charge), and changes no claim, charge, or verdict in v15.050.
