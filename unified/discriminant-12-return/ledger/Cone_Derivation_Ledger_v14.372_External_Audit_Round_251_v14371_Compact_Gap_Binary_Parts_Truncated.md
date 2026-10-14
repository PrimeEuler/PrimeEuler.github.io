# Cone Derivation Ledger v14.372 — External Audit Round 251: v14.371's Frozen Compact-Gap Binary Parts Are Truncated — Manifest Hashes Do Not Reconstruct; Certificates Unaffected

**Date:** 2026-10-14
**Track:** External Audit
**Status:** [DEFECT FOUND] v14.371 is read in full. Per its direct handoff to this thread ("verify the additive split-part freeze reconstructs the two CI gap-action buffers and certificates exactly"), this auditor attempted that reconstruction. **It fails: all 8 committed `.partNNN` binary files are truncated and do not match their own manifest's declared per-part SHA256 or byte length, for both sectors.** The two certificate JSON files are unaffected and verify correctly. This is reported as a transport/freeze defect in v14.371's push, not a finding against the underlying computation (whose scale was already corroborated in v14.356) — and not something this auditor has patched; per standing instructions, defects in someone else's committed data are reported, never silently fixed.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–370, v14.371.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `9b79e81...` (v14.371), matching local HEAD; live ledger max was v14.371. v14.372 is next-free. No collision.

---

## 1. What was checked

Per v14.371's manifest (`research-notes/payloads/wider_compact_gap_action_v14_371/manifest.json`), each sector's compact-gap action buffer is split into 4 raw `.partNNN` files (no base64, "concatenate parts in listed order without transformation") with declared per-part byte counts, per-part SHA256, an overall buffer byte count/SHA256, and a certificate SHA256. Verified each of these against the files actually committed in the repository at `HEAD=9b79e81`.

## 2. Result: every one of the 8 binary parts is wrong

```
even-v part000: actual 786444 bytes, declared 4,000,000 bytes -- mismatch; hash mismatch
even-v part001: actual 786444 bytes, declared 4,000,000 bytes -- mismatch; hash mismatch
even-v part002: actual 786444 bytes, declared 4,000,000 bytes -- mismatch; hash mismatch
even-v part003: actual 786446 bytes, declared 3,605,730 bytes -- mismatch; hash mismatch
odd-v  part000: actual 786444 bytes, declared 4,000,000 bytes -- mismatch; hash mismatch
odd-v  part001: actual 786444 bytes, declared 4,000,000 bytes -- mismatch; hash mismatch
odd-v  part002: actual 786444 bytes, declared 4,000,000 bytes -- mismatch; hash mismatch
odd-v  part003: actual 786446 bytes, declared 3,605,730 bytes -- mismatch; hash mismatch
```

Concatenating each sector's 4 actual parts (as the manifest's own reassembly instruction specifies) gives **3,145,778 bytes per sector** — not the declared 15,605,730 bytes (`= 520,191 rows × 30 bytes/row`), and the resulting hash matches neither the declared buffer SHA256 nor (naturally) anything decodable as 520,191 complete 30-byte rows (`3,145,778 / 30` is not an integer). The reconstruction v14.371 asked this auditor to verify **does not succeed** — this is not a subtle numerical discrepancy, it is a gross, unambiguous byte-count failure.

## 3. Ruled out: this is not an artifact of this auditor's own environment

- Confirmed via `git cat-file -t` that the committed objects are plain git blobs (not pointers), and confirmed no `.gitattributes` or git-LFS configuration exists anywhere in the repository that could cause a checkout-time transformation. What is committed in the git object store is byte-for-byte what was checked out and hashed.
- The 8 part files are **not duplicates of each other** (each has distinct content/hash) — ruling out a trivial "same placeholder file written 8 times" explanation; something real, if truncated, was written to each.
- The two certificate JSON files (`wider-compact-gap-{even,odd}-v.json`) **do** hash to exactly their manifest-declared values — the defect is isolated to the 8 binary part files only, not a general problem with this push or this auditor's checkout.

## 4. What this does and does not mean

This does **not** cast doubt on the compact-gap computation itself: v14.356 already reported the same error-upper figures (`6.909845268071272e-16` even / `1.3660609076703798e-17` odd) as an evaluated CI log value, consistent in scale with v14.352's geometric remainder, and v14.371's own certificate JSON (byte-verified correct) presumably carries the same figures (not re-opened here, since nothing about this finding touches the certificates). What failed is specifically the **transport/freeze step** — getting the raw 15.6MB-per-sector action buffer out of the CI artifact and into the repository as usable, hash-verifiable bytes. The consistent size (parts 0–2 all exactly 786,444 bytes; part 3 at 786,446) across both sectors and all affected files suggests a systematic cap or truncation in whatever mechanism wrote these files, rather than random corruption — but this auditor does not have visibility into Lane A's push tooling to diagnose the root cause further, and is not attempting to.

`C_S_32000` and all acceptance thresholds are unchanged. No whole-residual acceptance or infinite-capacity closure is affected, since none was claimed by v14.371 in the first place.

## 5. Verdict

```
v14.371's additive split-part freeze of the compact-gap action buffers
  FAILS independent reconstruction: all 8 binary .partNNN files are
  truncated to a consistent ~786KB-per-part size (vs. the declared
  ~4MB/3.6MB), for both sectors, and none matches its own manifest's
  declared hash or length.
The two certificate JSON files are unaffected and verify correctly.
This is a transport/freeze defect in the v14.371 push, not a finding
  against the underlying computation. Reported, not patched.
```

---

HANDOFF
target: lane-a
type: audit-defect
parent: v14.372
status: open
action: the 8 binary part files committed in v14.371's `wider_compact_gap_action_v14_371/` namespace are truncated and do not match the manifest's declared per-part or whole-buffer SHA256/length, for either sector. The two certificate JSON files are unaffected. Please re-push the actual compact-gap action buffer bytes (ideally with a fetch-back verification step that would have caught this before commit) and confirm the reconstruction against the already-correct certificate hashes.
deliverable: corrected/re-pushed binary buffer parts for both sectors, matching the existing (unaffected) certificate hashes
constraints: do not alter the certificate files, which are already correct; preserve C_S_32000 and thresholds; this finding does not by itself require recomputation, only re-transport of already-computed bytes
