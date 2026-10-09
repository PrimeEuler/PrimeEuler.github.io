# Cone Derivation Ledger v14.208 — Sandbox: v14.207 Actual-256k Leading Self-Energy Archive Audited

**Date:** 2026-10-09
**Track:** Sandbox / v14.207 handoff response (complete-payload-audit-after-freeze)
**Status:** [V] Committed archive independently verified: manifest digest match, certificate/snapshot SHAs match v14.207, M11 intervals recomposed and rationally consistent, part-level hash verification confirmed, replayed==producer certificates. No correction.
**Parents:** v14.185–188, v14.195–207.
**Collision check:** live ledger max v14.207 at write time; v14.208 is next-free. No collision.

---

## 1. Archive integrity [V]

Committed manifest
`payloads/exact_remote_leading_run_37965642729/artifact_manifest.json`
(SHA-256 `e8d8f53afe1111c504bf183d9adb9ee0452d5f9dfdee637ba2276a5610306c5d`)
matches v14.207's stated deterministic digest exactly. ✓

14 original files retained; every hash independently checked:
- even-v certificate `e726b54aa728d598…` ✓ / odd-v `5692ac1b3bf7f4bf…` ✓
- even-v snapshot `fb78ec8572485d04…` ✓ / odd-v `b975cd0769445492…` ✓
- CI manifest `46fbe78e59f96f7e…` ✓
- `all_original_files_reconstructed_and_hash_verified: true` ✓

Reconstructed one encoded snapshot part directly and verified its
SHA-256 against the manifest's part hash — match. The freezer's
lossless preservation holds at the part level, not merely as a
self-reported flag. ✓

Replayed certificates are byte-identical to producer certificates
(same SHA both sectors) — the independent CI replay genuinely
reproduced the producer output. ✓

## 2. M11_256k intervals [V]

From the committed paired JSON
(`actual256_leading_completion/remote-leading-selfenergy-256000.json`):

| Sector | M11_full_front outward interval |
|---|---|
| even-v | [44210.40614400759…, 44210.46426781083…] |
| odd-v | [43399.50234615309…, 43399.50236793977…] |

Both match v14.207's deliberately widened decimal endpoints.
Exact rational endpoints checked via `Fraction`: rational lo ≤
display lo and rational hi ≥ display hi in both sectors
(outward rounding confirmed). `exact_capacity_recomposition_matches_certificate:
true` both. ✓

Note: the even-v interval (width ≈0.058) is ~2600× wider than odd-v
(≈2.2e-5) — a property of the computation, not a defect; both are
exact outward enclosures.

## 3. Scope discipline [V]

All three paired flags remain false:
`original_C_S_32000_replaced: false`,
`infinite_operator_action_certified: false`,
`infinite_capacity_tail_closed: false`.
No 5e-9 acceptance claimed. The entry correctly states these are
leading finite-front coefficients, not remote action certificates. ✓

## 4. Verdict

$$\boxed{
\text{[V] Committed 256k archive verified: hashes, intervals,}\\
\text{freezer lossless, scope flags. No correction.}
}$$

The certified M11_256k intervals are now available for the
controlled whole-remote self-energy/action model (v14.207's stated
next gate).

---

HANDOFF-ACK
from: v14.207
target: sandbox
status: closed
result: Full committed archive independently audited — manifest digest, all 14 file hashes, M11 intervals with rational consistency, part-level reconstruction, replayed==producer identity, and scope flags all verified. No correction. M11_256k certified for downstream use.
constraints: None.
