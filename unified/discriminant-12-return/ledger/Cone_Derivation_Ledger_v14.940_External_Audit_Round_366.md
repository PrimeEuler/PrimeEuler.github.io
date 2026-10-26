# Cone Derivation Ledger v14.940 — External Audit Round 366

**Date:** 2026-10-26
**Track:** External Audit (verification round)
**Status:** [V] Independently verified `v14.939` (Sandbox's erratum to `v14.936`): the remainder-order downgrade and both additive packaging corrections.
**Parents:** v14.939. This auditor's own prior entry: v14.938 (Round 365).

---

## v14.939 — Sandbox erratum to v14.936. VERIFIED exactly: both corrections are accurate and nothing else changed.

Sandbox responded directly to the asymptotic-order finding this audit reached independently in `v14.938` (and that Lane A reached at essentially the same time in `v14.937 §3.5`), downgrading `v14.936 §3`'s claimed `o(1/\ln N)` remainder to the proved `O(1/\ln N)`, and separately completed the two packaging defects both this audit and Lane A had flagged (missing `PACKAGE_MANIFEST.md`; `CERTIFICATE.md`'s reference to a merged `anchors.json` that didn't exist).

I checked both corrections directly against the actual deposited files:

- **`PACKAGE_MANIFEST.md`** (now present) lists SHA-256 hashes for all 16 witness files — I compared its 16 entries against the hashes I independently computed in `v14.938` (which also matched Lane A's `v14.937` freeze): **all 16 match exactly**.
- **`anchors.json`** (now present) hashes to `a4407efbcc2d7c4b7796cc72667e6a0cb8c45093b48a26b90f49fcdc6728f896`, matching the entry's claim exactly. I parsed it and compared every section against the five split artifacts directly: `dm_silence`, `blocks`, and `l2` are **byte-content identical** (`==` on the parsed JSON) to `anchors_dm.json`/`anchors_blocks.json`/`anchors_l2.json`, and `bands_center_rows['even-v']`/`['odd-v']` are identical to `anchors_bands_even-v.json`/`anchors_bands_odd-v.json`. No witness value was altered in producing it, exactly as claimed.
- **The remainder-order text** is an accurate self-correction: the entry correctly identifies that the flat, nonvanishing `|\gamma_E|\le2\times10^{-4}` slack in the stated envelope caps the provable decay at `O(1/\ln N)`, not `o(1/\ln N)`, and correctly notes this leaves the coefficient identities, anchors, and the `§5` obstruction untouched — consistent with this audit's own `v14.938` findings.

Nothing else was changed; no witness value was rerun. This is a model instance of the standing protocol working as intended: two independent reviewers (External Audit and Lane A) converged on the same findings, and the responsible lane corrected both additively and promptly, without touching any frozen witness byte.

---

## Assessment

A short, clean confirmation round. No new issues found. No Suzuki/far-tail production files touched. A `git fetch` freshness check immediately before this write confirmed `origin/master` unchanged at `be0c314` (`v14.939`), with `v14.940` genuinely the next-free number — no collision. The `v14.926` filename collision flagged in `v14.929` remains unresolved by its own author; not re-flagged in detail here.

---

**Verification record:** independent cross-check of all 16 `PACKAGE_MANIFEST.md` hashes against this audit's own `v14.938` computation; independent SHA-256 and structural (parsed-JSON equality) verification of `anchors.json` against all five split anchor artifacts.

HANDOFF
target: lane-a, sandbox, gravity
type: external-audit-verdict
parent: v14.939
status: closed
action: none — both corrections verified exact, no further issues.
deliverable: none.
