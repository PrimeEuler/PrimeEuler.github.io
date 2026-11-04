# Cone Derivation Ledger v15.390 — Sandbox erratum to v15.388: one truncated SHA-256 string in the entry prose

Date: 2026-11-04 (America/New_York). Lane: sandbox (our Lane B). Parent: v15.388 (sandbox weak-force / SM internal-label deposit); occasion: External Audit Round 474 (v15.389), which verified v15.388 in full and flagged this one documentation-only error. Status: [D] transcription correction; no claim, file, or payload is affected.

## The error

In v15.388's payload hash list, the SHA-256 printed for `close_the_gap.py` is truncated to 54 hex characters — an 8-hex-character chunk (`8b122a10`) was dropped from the middle of the string when the entry prose was composed. The string as printed in v15.388,

`877a06a68dc24fd915b08c1aef5ab39ee7d1fee3d62d8fa5b92e46` (54 hex chars, malformed),

should read

`877a06a68dc24fd915b08c1aef5ab39ee7d1fee3d62d8fa8b122a104e5b92e46` (64 hex chars).

## Scope

The deposited file itself and the payload's `MANIFEST.sha256` were always correct: Round 474 ran `sha256sum -c MANIFEST.sha256` inside `payloads/weak_force_cone_v15_388/` and all ten files report OK, and the sandbox has re-verified the corrected string above against the file directly. Only the ledger entry's prose transcription of that one hash was wrong. No mathematical claim, script, or verdict in v15.388 depends on the prose string, and none changes. The other nine hashes in v15.388's list were cross-checked by Round 474 against the MANIFEST and match.
