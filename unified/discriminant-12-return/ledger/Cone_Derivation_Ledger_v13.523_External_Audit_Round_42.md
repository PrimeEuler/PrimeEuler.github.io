# Cone Derivation Ledger v13.523 — External Audit Round 42

## Scope

Independent audit of v13.520, v13.521, v13.522, committed since my last push (`3c0a7e5`, v13.519). All three independently verified; v13.521's script was fully re-executed at scale (63.8M+ entries, ~6.3 minutes) rather than spot-checked. Everything confirmed exact.

---

## 1. v13.520 (M16001 primitive residual audit gate) — confirmed genuinely fail-closed

This entry tightens the standard further: it identifies that even the v13.514 residual transcript (already confirmed real, re-executable arithmetic in Round 40) still rests on nine unaudited primitive-formation steps (displacement-entry formation, payload conversion radii, Frobenius accumulation, etc.) before it can count as a theorem-level radius, and correctly declines to treat it as one in the meantime.

Re-executed `research-notes/suzuki_M16001_primitive_residual_audit_gate.py` directly: `gamma_7991` matches the previously-verified value exactly, `gamma_79910` and the entry count `79910=10×7991` are correct, and the script genuinely raises `RuntimeError` listing all nine missing transcripts — confirmed by reading the source that none of the nine `REQUIRED` fields have a hardcoded fallback. This is the same honest discipline as v13.510/512/514, applied one level deeper.

## 2. v13.521 (M16001 primitive displacement entry bounds) — fully re-executed at scale, confirmed exact

This entry closes two of the nine gaps from v13.520 (off-diagonal `A0_FF` and `A0_FC` entry-formation radii) with genuine propagated-roundoff code, not literals. Given the O(7991²) scope (63,848,090 ordered off-diagonal `A0_FF` entries plus 79,910 `A0_FC` entries), timed a small sample first (≈168,000 calls/sec, giving a ≈6.3-minute estimate), then ran the full script to completion in the background rather than spot-checking or trusting the estimate.

**Every reported quantity matches the ledger's claimed values to full displayed precision**, including the entry count itself (`63848090 = 7991×7990`, confirmed):

| quantity | re-executed | claimed |
|---|---|---|
| FF max entry radius | `9.022982959826540786e-16` | `9.022982959826541e-16` |
| FF max numerator | `160923.02110693137675` | `1.6092302110693138e5` |
| FF max denominator | `256031560.0` | `2.56031560e8` |
| FF max quotient radius | `1.4171314499758582351e-15` | `1.4171314499758582e-15` |
| FC max entry radius | `4.8480471029224167118e-19` | `4.848047102922417e-19` |
| FC max numerator | `96053.91621703398471` | `9.6053916217033985e4` |
| FC max quotient radius | `7.096315233660020792e-19` | `7.096315233660021e-19` |

(full transcript has 18 reported values; all checked, all match). Read the full script source: no hardcoded radius or empirical-discrepancy shortcut anywhere — every value is propagated from the stated first-order roundoff formulas through products, subtraction, division, and the `2/π` scaling, exactly as documented. This is genuinely reproducible arithmetic at real scale, the strongest form of verification available and a clean contrast with the v13.508 episode from Round 38.

## 3. v13.522 (cone sign vs. QR-kernel fiber decomposition) — exhaustively verified

This entry catches and corrects a subtle conflation from looser prior discussion: cone sign `S` moves *between* QR fibers, while the QR-kernel involution `K` moves *within* a fiber; they differ by the positive V4 element `h=11`. Independently rebuilt the full 8-state action table in code:

- Fiber decomposition `P⁻¹(q)={(q,0),(q+h,1)}`: confirmed for all four fibers, matching the claimed pairs `{1,-11},{5,-7},{7,-5},{11,-1}` exactly.
- `P∘K=P` (K acts within fibers): confirmed for all 8 states.
- `P∘S=T_h∘P` (S maps fiber to fiber): confirmed for all 8 states.
- The full 8-row action table (`P`, `S(v,c)`, `P(S(v,c))`, `K(v,c)`, `P(K(v,c))` for every state): confirmed row-by-row against direct computation — exact match.
- Character-level consequence (`S*P*χ` is even iff `χ(11)=+1`): confirmed for all four characters — `1` and `χ12` are S-even, `χ-4` and `χ-3` are S-odd, matching `χ12(11)=+1` and the other two `=-1`.

No error found. This is a correct, well-caught self-correction, not a new independent claim, and it strengthens rather than revises the mechanism established in v13.518.

---

## 4. Summary

| Entry | Verdict |
|---|---|
| v13.520 | Confirmed genuinely fail-closed, same honest pattern as v13.510/512/514 |
| v13.521 | Fully re-executed at scale (64M+ entries); every value matches exactly |
| v13.522 | Exhaustively verified; correct and useful self-correction |

## Guardrail

No RH, GRH, Suzuki-spectral, or critical-line consequence follows from any of these three entries, consistent with their own guardrails. Certified status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`.
