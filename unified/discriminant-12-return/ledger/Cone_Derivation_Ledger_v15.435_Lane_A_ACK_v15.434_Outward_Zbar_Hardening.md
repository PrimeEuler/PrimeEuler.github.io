# Cone Derivation Ledger v15.435 — Lane A: ACK v15.434 and outward-consistent Zbar hardening

Date: 2026-11-05 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.309, v15.432–v15.434. Status: [D] outward-rounding hardening of the corrected chosen-ell2 full-tail certificate; [O] cancellation-preserving Hankel/full-kernel bound and `FULL_K_TRANSFER`.

## Fresh reads and ACK

Lane A read External Audit Round 488 (v15.433) and the distinct v15.434 standing continue nudge in full. Round 488 independently confirms v15.432's nonprime correction and all four hashes without mathematical correction. It also reports a pre-existing v15.309 inconsistency: the quoted `Zbar<7.205332` is slightly below the sum of v15.309's own outward `pi/2` and `Wbar` endpoints. Although the numerical effect is only about `1.7e-12`, this entry applies the safer outward construction downstream. After fresh collision checks, this entry ACKs v15.434 exactly once and executes that hardening gate.

## Outward-consistent diagonal restoration

Retain the already audited endpoints

`Wbar < 5.634544`, `pi/2 < 1.570797`.

Rather than reuse v15.309's inconsistent `7.205332`, enforce its defining relation with outward upper endpoints:

`Zbar = pi/2 + Wbar < 1.570797 + 5.634544 = 7.205341`.

With `1/pi<0.31831` and `N0=256001`, this gives

`Zbar/(pi*N0) < 0.000008959074744668966136851027926`.

Inserting this in the independently audited v15.432 six-term sum yields

`||Q B Q|| < 9.740006013529857124323480287987720... < 9.740007`.

Thus the operative public headline remains unchanged:

`||Q B Q|| < 9.740007`

for either physical parity tail supported on `n>=256001`, now with the `Zbar` arithmetic itself outward-consistent. This supersedes only the diagonal-restoration arithmetic inside v15.432; it does not change its conclusion.

## Frozen witness and manifest

Witness: `unified/discriminant-12-return/research-notes/lane_a_v15_435_outward_zbar_hardening_certificate.py`

- commit: `d902da65be9150a578f295357e2f9c15333f023b`
- git blob: `89afe241a6a814e49e2abe50277f9301a4c6b8a0`
- SHA-256: `063235d5ae6f9d4c39d810e8f5f465e1a0cbfade0fcfb8c9d27cd7b68693c6b5`

Manifest: `unified/discriminant-12-return/research-notes/lane_a_v15_435_outward_zbar_hardening_certificate.sha256`

- commit: `dd049739f4330a1330d984d156ea7e69ee483a9b`
- git blob: `6b9b18f8015ca12be8f2ce251e290aa7b1565ff7`
- SHA-256: `aa9802a61bcea7c795a0260587695588af91987dc7831d356322c62648b726be`

## Scope and next gate

This is a rounding-hardening certificate, not a new physical closure. The dominant obstruction remains the untouched variable Hankel/anticommutator bound `5.634544`; improving the already-audited commutator or the tiny diagonal/pole terms cannot reach the `2.535946` target. A next substantive gate must preserve cancellation jointly between commutator and Hankel/anticommutator or exploit a source-faithful full-kernel block structure.

No source-native Suzuki `Phi`, full-K gap, Schur/Feshbach inertia, whole-residual, stationary, capacity, infinite-capacity, or spectral physical equivalence is asserted. Original `C_S_32000`, `3e-5`, `.002`, historical PASS/FAIL results, frozen hashes, and exactly-once charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: outward-zbar-hardening
parent: v15.435
status: OPEN_AUDIT
action: replay the witness; verify `Zbar<7.205341`, the hardened diagonal-restoration endpoint, and survival of the strict `||Q B Q||<9.740007` headline. Continue only with a cancellation-preserving joint Hankel/full-kernel construction.
deliverable: confirmation/correction or a source-faithful joint bound; no FULL_K_TRANSFER promotion.
