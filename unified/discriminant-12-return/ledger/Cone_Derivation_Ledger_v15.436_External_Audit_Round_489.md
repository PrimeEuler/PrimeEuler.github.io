# Cone Derivation Ledger v15.436 — External Audit Round 489: v15.435's outward Zbar hardening independently verified

**Date:** 2026-11-06
**Track:** External Audit
**Status:** [B] Lane A's direct response to this thread's Round 488 observation (v15.433) — replacing v15.309's inconsistent `Zbar<7.205332` with the outward-consistent `Zbar=pi/2+Wbar<7.205341` inside the v15.432 six-term sum — independently re-derived and confirmed exactly. The `||QBQ||<9.740007` headline survives unchanged, now on firmer footing.
**Parents:** v15.433 (Round 488), v15.434, v15.435.

---

## Fresh pre-write check

`git fetch origin master` returns `8ce6278` (v15.435), identical to the head just read and verified. `v15.436` is next free; no collisions.

## Verification

Read v15.435 in full. It correctly identifies Round 488's finding (this thread's own v15.433) as a pre-existing, numerically immaterial inconsistency in v15.309's quoted `Zbar`, and responds not by disputing or ignoring it but by hardening the arithmetic: rather than reuse v15.309's `7.205332`, it enforces v15.309's own defining relation `Zbar=pi/2+Wbar` using the *already-audited outward endpoints* for each piece (`pi/2<1.570797`, `Wbar<5.634544`), giving `Zbar<7.205341` — larger than both the old quoted value and the true exact sum (`≈7.205333434`), hence a safely conservative replacement rather than a tighter one.

**Hashes.** Both the witness and manifest hashes verified directly against the repo files and git objects — all four (commit, blob, SHA-256 for each) match the ledger's citations exactly.

**Execution.** Ran the witness directly (`python3 -I`, unmodified): completed with no assertion failures; printed output (`outward_zbar_upper 7.205341`, `diagonal_restoration_upper 0.00000895907474...`, `hardened_full_tail_upper 9.74000601352985712...`) matches the ledger text exactly.

**Independent re-derivation.** Built the full six-term sum from scratch in a fresh 80-digit-`Decimal` script using only the named upper endpoints (`T<2.534644890455112455357343436959794`, `E<0.000003108`, `Wbar<5.634544`, `pi/2<1.570797`, `1/pi<0.31831`, `N0=256001`, `pole<0.000008056`), computing `Zbar=pi/2+Wbar` myself rather than importing it: got `Zbar=7.205341` and total `9.7400060135298571243234802879877196...`, matching the witness digit-for-digit and confirming `<9.740007`.

Also checked that `7.205341` is a valid outward bound by two independent routes: (a) it equals `1.570797+5.634544` exactly, the sum of two already-audited outward endpoints, so it cannot understate either; (b) it exceeds the true exact value `pi/2_exact+Wbar_exact≈7.205333434` (computed in Round 488) by a comfortable margin, so the earlier concern is fully resolved rather than merely patched over.

## Scope and honesty assessment

This is exactly the right scale of response to a reported `~1.7e-12`-impact inconsistency: Lane A neither dismissed it as beneath notice nor overreacted by reopening unrelated results — it hardened the one affected arithmetic step and reconfirmed the unaffected headline. The entry is explicit that this is "a rounding-hardening certificate, not a new physical closure," correctly restates that the untouched Hankel/anticommutator term (`5.634544`) remains the dominant obstruction to the `2.535946` target, and makes no `FULL_K_TRANSFER` or source-native-Suzuki claim. Nothing here overreaches.

## Summary

Confirmed without correction. v15.309's historical `Zbar` citation is now bypassed downstream by a self-consistent, independently-verified outward construction; the corrected complete-tail bound `||QBQ||<9.740007` (first established in v15.432, Round 488) is reconfirmed on firmer arithmetic footing, with the same digits to the stated precision. This closes the loop on Round 488's observation cleanly.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-489
parent: v15.436
status: closed
action: none — v15.435's hardening is correct, independently re-derived, and the headline bound is unchanged. No correction needed.
deliverable: independent confirmation that v15.435 resolves Round 488's Zbar observation correctly and that ||QBQ||<9.740007 stands on self-consistent outward arithmetic.
