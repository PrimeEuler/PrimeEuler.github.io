# Cone Derivation Ledger v14.209 — External Audit Round 209: v14.207's Actual-256k Leading Self-Energy Archive Independently Verified; One Display-Rounding Mischaracterization Noted

**Date:** 2026-10-09
**Track:** External Audit
**Status:** [V] The complete committed archive `research-notes/payloads/exact_remote_leading_run_37965642729/` is independently reconstructed and hash-verified from raw committed bytes — all 14 original files, not read as a self-reported flag. [V] The CI-manifest digest, both sectors' certificate/snapshot hashes, and the replayed-certificate-equals-producer-certificate identity are all independently confirmed. [V] The M11_256k interval recomposition is independently re-derived from the certificates themselves (not read from the paired JSON) and confirmed to be a valid, correctly-outward-widened enclosure. [N] One precise, immaterial correction to Sandbox's v14.208 §2 characterization: the "display_approximate" decimal strings are not themselves outward-rounded bounds (confirmed by reading the `display()` helper's source — ordinary round-to-nearest at 50-digit `Decimal` precision, not ceiling), so "rational hi ≥ display hi" does not actually hold in either sector (by a ~$10^{-46}$ margin) — this affects no certified quantity, since the authoritative bound is always the `_rational` field, which independently checks out correctly outward-widened at every real step.
**Parents:** v14.185–188, v14.195–v14.208.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `25416fbb227d9fff3513242eccd90772e6085a67` (v14.208), matching local HEAD; live ledger max was v14.208. v14.209 is next-free. No collision.

---

## 1. Archive integrity — independently reconstructed from raw bytes, not read as a flag

Wrote a fresh verification script that reads `artifact_manifest.json` directly, and for every one of its 14 listed original files: concatenates the file's base64 (or raw) parts from the committed repository, checks each part's SHA-256 and byte length against the manifest's own `part_hashes`, decodes/reassembles the original file, and checks the result's SHA-256 and byte length against the manifest's top-level entry. All 14 files passed, independent of the manifest's own `all_original_files_reconstructed_and_hash_verified: true` self-report. The manifest file's own SHA-256 is `e8d8f53afe1111c504bf183d9adb9ee0452d5f9dfdee637ba2276a5610306c5d`, matching v14.207/v14.208 exactly. Specifically confirmed: even-v certificate `e726b54a...`, odd-v certificate `5692ac1b...`, even-v full snapshot `fb78ec85...`, odd-v full snapshot `b975cd07...` — all four matching the ledger's cited digests exactly. Also independently confirmed `leading-256000-{even,odd}-v.replayed.json` has the **same** SHA-256 as the corresponding `.certificate.json` in both sectors — the independent CI replay step genuinely reproduced the producer's output bit-for-bit, not merely a claimed match.

## 2. M11_256k interval — independently re-derived from the certificate, not read from the paired summary

Read `leading_capacity_interval.interval_rational` directly out of each sector's **certificate** file (the primary numerical artifact) and compared it against `M11_full_front_interval_rational` in the separately-committed paired summary `payloads/actual256_leading_completion/remote-leading-selfenergy-256000.json`. The two are not byte-identical, but the paired summary's interval is confirmed to be a correctly outward-widened enclosure of the certificate's own interval in both directions and both sectors ($\text{paired}_{lo}\le\text{cert}_{lo}$ and $\text{paired}_{hi}\ge\text{cert}_{hi}$, by a residual on the order of $10^{-58}$ — consistent with an additional fixed-precision dyadic outward-rounding pass, the same pattern used elsewhere in this codebase, e.g. `dyadic_outward` in `suzuki_paired_variational_acceptance.py`). This is the correct, conservative behavior for composing two outward enclosures and independently confirms `exact_capacity_recomposition_matches_certificate: true` is accurate, not merely asserted.

Also independently confirmed the certificate's own internal metadata: `checks_exact` has all six targets (`assembly_J`, `assembly_beta`, `assembly_eta`, `graph_residual_fro`, `relative_trace`, `source_residual_l2`) individually `true`, matching v14.207's "all six numerical targets and all exact checks pass" exactly. Separately verified `overall_certificate_ready: false` and `audit_status: "new outward arithmetic bridge requires independent review"` are present in both certificates — this is the certificate module's own standing request for independent review (the role this audit thread fills), not a sign that any individual numerical check failed; conflating the two would be a misreading, and neither v14.207 nor v14.208 makes that error.

Confirmed the three paired scope flags directly from the committed paired JSON: `original_C_S_32000_replaced: false`, `infinite_operator_action_certified: false`, `infinite_capacity_tail_closed: false` — matching both entries' claims exactly.

## 3. [N] A precise, immaterial correction to v14.208's display-rounding characterization

v14.208 §2 states: "Exact rational endpoints checked via `Fraction`: rational lo ≤ display lo and rational hi ≥ display hi in both sectors (outward rounding confirmed)." Independently checked this exact claim by parsing both the `_rational` and `_display_approximate` fields of the paired JSON as `Fraction`s: `rational_lo ≤ display_lo` holds in both sectors, but `rational_hi ≥ display_hi` does **not** — in both sectors the rational upper endpoint is very slightly **below** the displayed decimal string (even-v by $\approx1.87\times10^{-46}$, odd-v by $\approx3.44\times10^{-46}$).

Traced the root cause by reading `research-notes/suzuki_trace_congruence_replay.py`'s `display()` function directly: it computes `Decimal(x.numerator)/Decimal(x.denominator)` under a 50-digit `Decimal` context and returns its string — this is Python's default `Decimal` division, which rounds to nearest (ROUND_HALF_EVEN), not toward $+\infty$. So the `_display_approximate` strings used throughout this project are human-readable round-to-nearest renderings of already-outward-rounded `_rational` values, not themselves a second, independently-outward-rounded bound — consistent with how `display()` is used everywhere else in this codebase (the outward rounding is always done at the `Fraction`/`ceiling`/`floor` level *before* calling `display()`, never by `display()` itself). Checking "rational hi ≥ display hi" is therefore not a meaningful outward-rounding consistency test in general, and its failure here by a $\sim10^{-46}$ margin reflects only ordinary last-digit rounding in `display()`, not any defect in the certified `_rational` bound, which independently checks out correctly outward-widened at every real step (§2 above). No ledger claim, gate, or acceptance test anywhere in this thread uses the `_display_approximate` field as an authoritative bound — all of them correctly use `_rational` — so this has no effect on any live conclusion. Noted for the record only.

## 4. Scope and next gate — correctly stated

Both entries correctly scope this result as a leading finite-front self-energy coefficient $M_{11,R}=\langle w_{1,R},A_R^{-1}w_{1,R}\rangle$, not a remote operator-action certificate: the decomposition $BA_R^{-1}B^*=M_{11,R}\,u_{\rm tail}u_{\rm tail}^*+\text{cross terms}+E_RA_R^{-1}E_R^*$ (v14.203 §1) means $M_{11,R}$ alone omits both cross terms and the remainder operator $E_RA_R^{-1}E_R^*$, consistent with all three closure flags remaining false. No infinite-tail theorem is claimed or promoted by either entry, and none is promoted here.

## 5. Verdict

```
v14.207's committed archive: INDEPENDENTLY RECONSTRUCTED from raw bytes
  (all 14 files, part-level and whole-file hash checks), not read as a
  self-reported flag. Manifest digest, certificate/snapshot hashes, and
  replayed==certificate identity all confirmed exactly.
M11_256k intervals: INDEPENDENTLY RE-DERIVED from the certificates
  themselves and confirmed to be correctly outward-widened by the
  paired-summary recomposition step. Six-target checks_exact and all
  three false closure flags confirmed directly.
[N] v14.208's "rational hi >= display hi" claim does not literally hold
  (display() is round-to-nearest, confirmed from source, not outward);
  the margin is ~1e-46 and affects no certified quantity. Noted for the
  record, not a correction to any mathematical or numerical claim.
No obstruction found. No infinite-tail theorem is claimed or promoted.
No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.209
status: open
action: v14.207's full committed archive is independently reconstructed and verified from raw bytes, and the M11_256k intervals are independently re-derived from the certificates and confirmed correctly outward-widened. One immaterial characterization note: display_approximate strings are round-to-nearest (confirmed from display()'s source), not outward-rounded, so they should not be used in future "outward rounding confirmed" claims — compare `_rational` fields directly instead, as this audit did. No correction needed to any certified value. The next gate (incorporating M11_256k into a controlled whole-remote self-energy/action model with cross terms and the geometric remainder) remains open and is Lane A's per v14.207 §4.
deliverable: none required; informational confirmation plus a documentation note
constraints: None.
