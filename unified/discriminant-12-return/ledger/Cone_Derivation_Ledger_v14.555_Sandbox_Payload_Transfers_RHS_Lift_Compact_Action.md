# Cone Derivation Ledger v14.555 — Sandbox record: repository transfer of the v14.539 complete-RHS, v14.543 fresh-lift, and v14.552 changed-compact-action payloads

**Timestamp:** 2026-10-17 (EDT)
**Lane:** Sandbox (little Euler)
**Parents:** v14.539 (complete-RHS return), v14.543 (fresh-lift return), v14.552 (changed compact-action return), v14.554 (Lane A ACK + exact compact payload replay + residual HANDOFF).
**Status:** transfer record only, written under Jeremy's explicit instruction of 2026-10-17 ("put them in the repo"). No new numerical claim is made; every byte below was already frozen by hash in its parent return.

## What was transferred

All three payloads were staged sandbox-side, split into 700,000-byte chunks (suffix `.partNNN`; each manifest lists its chunk filenames explicitly), pushed file-by-file with per-file fetch-back SHA-256 verification (215 pushes, zero failures), and then verified a second time from the repository: every listed file re-fetched and re-hashed, and every buffer reassembled from its repository chunks and matched against the frozen whole-buffer SHA-256 of its parent return.

### 1. Complete RHS (v14.539)

Destination: `unified/discriminant-12-return/payloads/direct_middle_complete_rhs_v14_539/` — 79 files (2 certificates, 76 chunks, manifest.json).
Manifest SHA-256: `65301ff63c46868d3976d0901a33dfb73e96d1b832c9242725a5ac8bb65c09c9`.
Reassembly from repository chunks: lift-RHS even `2fb4363ff1ad6a12fb6428eb80dd4aab90365662e79ff90f4ac0c826d7b5d658` (6 chunks), lift-RHS odd `e8d1e795c2df50c66bb9c972797c50af1581f31288c4550a3a1e307ef06d13a2` (6), input-z even `0e9e889c915a55267bcf81f9c39d9aed0d768dc857e5bcbf0731f503e6a3ed7f` (32), input-z odd `4ba2d312191080a3d302704ef14e9479a7fab913401c508fb22cfe0dbab87c21` (32) — all MATCH. Certificates: even `d56eaf3ade699c5c85ad3ae954c5817c3e58045c6894268b3e49e6a7b2ad55ad`, odd `19c67577d032366253625a0f12ed08c217d10c0245fdd03e4bb6ce953cfb2884`.

### 2. Fresh finite lifts (v14.543)

Destination: `unified/discriminant-12-return/payloads/direct_middle_fresh_lift_v14_543/` — 35 files (2 certificates, 32 chunks, manifest.json).
Manifest SHA-256: `7e21c97f78bec2540e4e6904c5f62cae96e9e502248d3f0090862f112aebcfdf`.
Reassembly from repository chunks: lift buffer even `d3fd00e05bd19709811086ec246764feb36379dc52ec410798d2a01d8e1bf237` (16 chunks), odd `a852b54e22ef62d029528c9856f24a5ea6fb9618c99725ccdb052b5a562a739c` (16) — both MATCH. Certificate files: even `d3ea64364f8ca69b569ed9f981828048bd80448d3dc6055934b50e6a278fa263`, odd `6c52c4fd7eaa615582375e455588164316254ced57cfb9b4a90d5b82bd5fa95f`. The byte-level replay fences noted in Audit Rounds 306/307/308 on the RHS and lift certificates are discharged by this transfer.

### 3. Changed direct-middle compact action (v14.552)

Destination: `unified/discriminant-12-return/payloads/direct_middle_changed_compact_action_v14_552/` — 101 files (2 sector certificates, 8 shard certificates, 90 chunks, manifest.json).
Manifest SHA-256: `ea361dc1a6b0f2bacb2dd542389ff6d6bfbc8755afe29df08204977b2d2170cb` — identical to the manifest Lane A independently replayed in v14.554 (38,822 bytes), whose per-sector chunk and concatenation checks all PASS.
Reassembly from repository chunks: stitched buffer even `807a4c6e89ab0ff89ce7687a617c01a6c37e83f7ee75b94b189d1a9128c4faec` (45 chunks), odd `1788550cb29227a74a0ba9a0561d73b932886e21ff5c1070f368df3db7e8e7a1` (45) — both MATCH. Certificate files: even `2013799b36b5810ec90e9f815822634c7da518e8e18dda401b9f1c72dc0d7a6a`, odd `ebe5cc360f1daceb90de47c12ae98ec90836941213b595f2b234340ae92fe4c1`. The 8 shard buffers were not transferred: each stitched buffer is the exact concatenation of its four shard buffers in shard order (all 8 shard-buffer SHA-256s are recorded in the manifest and in the v14.552 shard table; the concatenation identity was verified before staging).

## Scope and disposition

Nothing else was transferred; in particular the v14.486 original-seed payload remains sandbox-resident and untouched. This record closes the transfer items for the three parent returns. The active gate is now the v14.554 residual-composition HANDOFF; the seed buffers it requires are retained in the sandbox workspace at their frozen v14.486 hashes.
