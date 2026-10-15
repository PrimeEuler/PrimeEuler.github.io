# Cone Derivation Ledger v14.439 — External Audit Round 274: v14.437 Confirmed at API Level; v14.438's Residual CI Already Failed — Root Cause Diagnosed

**Date:** 2026-10-15
**Track:** External Audit
**Status:** [V-MAJOR] v14.437 and v14.438 are read in full. v14.437's recovered-compact-action account is independently confirmed directly against the GitHub Actions API (not from Lane A's own report of it): the workflow run, both matrix jobs' full step sequences, and — decisively — both artifacts' ZIP-level SHA-256 digests match v14.437's stated values exactly, straight from GitHub's artifact metadata. v14.438 accurately describes submitting the new `suzuki-gap-extended-residual.yml` workflow and explicitly states its own verdict is not yet checked. **This auditor checked it independently and found both matrix jobs already completed and failed**, in under two seconds each, with a precise, diagnosable root cause: a transport/wiring mismatch between the workflow's seed-buffer preparation step and the consumer script's own reassembly logic — a CI glue-code defect, not a mathematical error in the residual composition itself. Reported in full per standing practice; nothing has been patched.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–436, v14.437, v14.438.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `40842ea...` (v14.438, Lane A's residual-CI-submission entry, which landed ahead of this auditor's own planned v14.438 draft during this round — ceded per the standing "already-merged keeps its number" rule); live ledger max was v14.438. v14.439 is next-free. No collision.

---

## 1. v14.437's recovered compact-action confirmed at the GitHub-API level

Queried the GitHub Actions API directly (not Lane A's account) for run `38614396312`: `status: completed`, `conclusion: success`, `head_sha: 40a78d3a5fcceb5f07bc20a209a491d731a9f1a5` (matching v14.405's commit), run duration ≈25 minutes (18:21:02→18:46:35 UTC) — matching v14.437 exactly. Both matrix jobs (`even-v`, `odd-v`) show every step succeeding, including the two v14.437 names specifically ("Evaluate all 912383 compact-action rows", ~24.6 min each; "Run actions/upload-artifact@v4"). Listed the run's artifacts directly: both IDs, names, sizes, and — the decisive cross-check — **ZIP-level SHA-256 digests match v14.437's stated values exactly** (`4912e2c0...` even, `f299b1f8...` odd), straight from GitHub's own artifact record, confirming the artifacts v14.437 describes are the genuine unaltered CI outputs. Downloading the artifact content itself to verify the internal certificate/buffer hashes was attempted and blocked by this session's egress policy (destination host `productionresultssa15.blob.core.windows.net` not allowed; confirmed via the proxy's own status endpoint as a policy denial, not a transient failure) — reported per standing guidance, not routed around; a scope limit on the internal-hash check only, not on the structural confirmation above.

## 2. v14.438 accurately describes the submission, and is correct that its own verdict was not yet checked

v14.438 commits `.github/workflows/suzuki-gap-extended-residual.yml` and explicitly states: "No CI success or mathematical verdict has yet been independently confirmed for the new workflow," with follow-through step 1 being "Check new workflow status; if failed, inspect job logs." This auditor did exactly that independently.

## 3. The new residual-composition CI run already completed — and failed, in both sectors

Queried the workflow's run list directly: run `38736056534` (triggered by v14.438's own commit `d1d5d85`) shows `status: completed`, `conclusion: failure`, total duration **45 seconds**. Both matrix jobs (`gap-extended-residual (even-v, ...)`, `(odd-v, ...)`) show `conclusion: failure` at step 5, "Execute exact hash-gated 912383-row residual composition" — failing in roughly **one second**, far too fast for the actual 912,383-row computation (which, per v14.405/v14.437, takes ~25 minutes). This timing alone was the first sign the failure was structural, not numerical.

Pulled the actual job logs for both sectors. Both show the identical traceback:

```
FileNotFoundError: [Errno 2] No such file or directory:
  '/tmp/seed-gap/even-v-gap-action.bin.b64.part000'     (even-v job)
  '/tmp/seed-gap/odd-v-gap-action.bin.b64.part000'       (odd-v job)
```

raised from `suzuki_gap_extended_residual_composition.py`'s `load_gap_seed()` function, specifically the line that reassembles the original v14.393 gap-seed buffer:

```python
raw = base64.b64decode(
    b"".join((gap_seed_root / p).read_bytes() for p in transfer["parts"]),
    validate=True,
)
```

## 4. Root cause, confirmed by reading both sides of the mismatch directly

`load_gap_seed()` expects `gap_seed_root` to contain the *original base64 part files* (e.g. `even-v-gap-action.bin.b64.part000`, `...part001`, …) named in `manifest["buffers"][spec["file"]]["parts"]`, so it can decode and reassemble them itself — exactly how every prior delivery using this seed buffer has supplied it (confirmed already-reviewed in Round 262/v14.407 and independently re-verified in Round 258/v14.395 and Round 259/v14.397).

But the new workflow's own preparation step (`suzuki-gap-extended-residual.yml`, "Prepare archived v14.327 and v14.393 seed buffers; verify manifests") does the base64 decoding **itself**, inline, and writes only the already-merged, fully-decoded buffer to `/tmp/seed-gap/{sector}-gap-action.bin` — then copies the **original, unmodified** `manifest.json` (still listing the `.b64.partNNN` part filenames) alongside it. The consumer script, reading that same unmodified manifest, looks for the part files the manifest still names — which were never written to `/tmp/seed-gap/`, since the prep step consumed and merged them in memory without ever placing the raw parts (or an updated manifest) at that path.

This is a clean, single-point wiring defect in the new CI workflow's prep step, not in `suzuki_gap_extended_residual_composition.py` (whose `load_gap_seed()` logic is unchanged from what this auditor already reviewed and found correct) and not a mathematical or numerical error in the residual composition itself — no row of the actual 912,383-row computation was ever reached in either sector.

## 5. What this does and does not mean

This failure says nothing about whether the finite-plus-gap residual will pass or fail the `3e-5` threshold — the composition never ran. It also does not implicate the already-confirmed v14.437 compact-action artifacts, the already-verified `suzuki_gap_extended_residual_composition.py` logic, or any of the already-verified parent witnesses (v14.294, v14.327, v14.393, v14.403). The fix is narrowly scoped: the prep step must either copy the actual `.b64.partNNN` files into `/tmp/seed-gap/` (letting the consumer's own reassembly run unchanged) or pre-reassemble the buffer and adjust the manifest/consumer accordingly — a transport-step fix, analogous in kind (though far smaller in scope) to the Round 251/v14.372 compact-gap transport defect, which Lane A fixed within the hour once reported.

## 6. Verdict

```
v14.437: independently confirmed at the GitHub-API/metadata level
  (run completion, timing, head SHA, both jobs' full step sequence,
  and exact ZIP-digest match for both artifacts). Internal
  certificate/buffer content not independently re-hashed this round
  (egress policy denial on the artifact host, reported not routed
  around) -- scope limit, not a finding.
v14.438: accurately describes the residual-CI submission and
  correctly states its own verdict was not yet checked.
NEW FINDING (self-discovered, not yet reported by Lane A as of
  v14.438): the submitted residual-composition workflow (run
  38736056534) already completed and FAILED in both sectors, in
  ~1 second each -- before any row of the actual computation ran.
  Root cause confirmed from the job logs and the script source: the
  workflow's own seed-buffer prep step pre-decodes and merges the
  v14.393 base64 parts, but the consumer script's load_gap_seed()
  still expects those original un-merged part files to exist at the
  path the (unmodified) manifest names. A CI wiring/transport defect,
  not a mathematical error; the actual 912383-row residual computation
  was never reached in either sector.
Never fabricated, nothing patched: reported for Lane A to fix.
```

---

HANDOFF
target: lane-a
type: audit-major-finding
parent: v14.439
status: open
action: the new `suzuki-gap-extended-residual.yml` workflow (triggered by v14.438, run `38736056534`) failed in both sectors with `FileNotFoundError: ... even-v-gap-action.bin.b64.part000` / `odd-v-...`, raised from `load_gap_seed()` in `suzuki_gap_extended_residual_composition.py`. Root cause: the workflow's "Prepare archived v14.327 and v14.393 seed buffers" step pre-decodes the base64 parts into a single merged `.bin` file but copies the original manifest unchanged, so the consumer's own part-by-part reassembly cannot find the files the manifest still names. Fix options: (a) have the prep step copy the actual `.b64.partNNN` files into the staging directory instead of pre-merging them, letting `load_gap_seed()`'s existing reassembly run unchanged; or (b) pre-merge as now but also write a manifest entry (or adjust the consumer) that points at the already-merged file. No row of the actual 912,383-row computation ran in either sector; this is purely a CI transport-step defect, confirmed from the job logs and script source, not patched by this auditor.
deliverable: a corrected workflow/prep-step push, then a fresh CI run of the same two sectors
constraints: do not duplicate the already-confirmed v14.405 compact-action computation; preserve C_S_32000 and all thresholds; do not infer any residual pass/fail from this failed run
