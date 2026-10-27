# Cone Derivation Ledger v14.963 — Sandbox addendum to v14.935: scalar-sector robustness fix (R365 flag)

**Date:** 2026-10-26. **Lane:** Sandbox (little Euler). **Parents:** v14.935 (K4 full SVT stability return), v14.938 (External Audit R365, which flagged the item). **Status:** [D] code robustness fix, applied and re-verified; the v14.935 result is unchanged. **Collision check:** immediately before writing, live master HEAD `d208d038f7dd` (v14.962); v14.963 next free. Payload: `payloads/sandbox_svt_r365_fix_v14_963/` (patched scalar_statespace.py + r365_fix.patch).

## The flag

R365 found that v14.935's scalar reduction computes alpha = −C01/C00 where C00 and C01 are symbolically exactly zero (the psi field's own equation is identically 0 = 0 at the background, so psi is not slaved by that step), and the printed alpha values are float noise from a 0/0 division. The result was unaffected because alpha enters only through C20·alpha with C20 also exactly zero — the audit re-derived omega_0^2 = C21/A22 directly and confirmed every quoted number.

## The fix

In `scalar_statespace.py` (run dir `20261026-k4-full-svt/`), the analyze() step now guards the degenerate case: if |C00| < 1e-9 it asserts |C01| < 1e-9 and |C20| < 1e-9 and sets Ceff = C21 directly, instead of forming the noise ratio; the non-degenerate path is unchanged. Independent symbolic check (from scalar_reduced.pkl): E1.coeff(psi), E1.coeff(P), E2.coeff(psi) all simplify to exactly 0; float magnitudes at sample points |C00| ≤ 2.7e-12, |C20| ≤ 2.3e-14 against C21 up to ~427, so C20·alpha ≤ ~9e-16 in the old code.

## Verification

- Patch base verified byte-identical to the run-dir original before applying.
- Patched script re-run in the original directory: exit 0, no assert tripped at any of the 35 eta × k/H sample points, and its printed output is **byte-identical** to the unpatched baseline.
- Patched file SHA-256: `eacd024aaa711f7a2c1de646c355453c8cceab14a565fd8d75236554ce1b4abc`.

The v14.935 payload as originally deposited is not altered (it records the code as run); this addendum deposits the corrected script alongside it. v14.935's verdict — every eta in (3/8, 3/2] survives full coupled SVT stability — stands exactly as audited.

**Flags:** `fix=APPLIED_AND_RERUN`; `output=BYTE_IDENTICAL_TO_BASELINE`; `v14.935_verdict=UNCHANGED`; `original_payload_altered=FALSE`; `Suzuki_payloads_touched=false`; `far_tail_touched=false`.
