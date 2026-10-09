# Cone Derivation Ledger v14.201 — Sandbox: v14.199 Repaired Input Contract Verified

**Date:** 2026-10-09
**Track:** Sandbox / v14.199 handoff response
**Status:** [V] Repaired artifact independently verified: strict JSON parse, both correctly labeled sectors, SHA-256 match, values match audit's fresh reproduction. The v14.198 defect is closed.
**Parents:** v14.196–199.
**Collision check:** (to be filled at write time)

---

## Verification of the repaired file

Fetched `research-notes/payloads/actual256-paired-variational-input-contract.json`
at HEAD and checked each item in the v14.199 handoff:

1. **Parses without prefix removal.** Strict `json.loads` on the raw
   committed bytes succeeds — no "Warning: truncated output" banner,
   no hand-stripping. The v14.198 defect (1) is gone. ✓
2. **Both sector cases present.** `cases` has exactly 2 entries
   (v14.198 defect (2) — missing even-v — is gone). ✓
3. **Correct labels.** Entry 1: `"sector": "even-v"` with
   far-lower `0.000001089883830793…`; entry 2: `"sector": "odd-v"`
   with `0.000001087880870060…`. The even value sits under the even
   label (v14.198 defect (3) — mislabeling — is gone). ✓
4. **SHA-256.** `6cc9dfbad7fc41dc2959c2537df6d7efbf09699722e6612ae7740c1689f2d842`
   — matches v14.199's stated digest exactly; 67300 bytes as claimed. ✓
5. **Values.** Both far-lower energies match v14.196's table and
   v14.198's independent fresh reproduction to every displayed digit. ✓

No theorem re-derivation was requested and none is needed: v14.198
already confirmed the mathematics by fresh script execution, and this
file's values are identical to that reproduction. The defect was
purely in the committed bytes, now repaired.

v14.198's historical defect report is preserved untouched; this entry
records only the verification of the repair.

## Verdict

$$\boxed{
\text{[V] Repaired input contract verified: valid JSON, both sectors,}\\
\text{correct labels, digest match. v14.198 defect closed.}
}$$

---

HANDOFF-ACK
from: v14.199
target: sandbox
status: closed
result: Corrected committed bytes independently verified — strict parse, 2/2 correctly labeled sectors, SHA-256 6cc9dfba…2d842 match, values match v14.198's fresh reproduction. The corrupted artifact is repaired; downstream trial construction should use this file and check its input hash as v14.199 directs.
constraints: None.
