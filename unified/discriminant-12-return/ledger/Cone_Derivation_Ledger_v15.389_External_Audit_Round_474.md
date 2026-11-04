# Cone Derivation Ledger v15.389 — External Audit Round 474: Sandbox weak-force / SM internal-label thread (v15.388) — independently verified; one documentation-only hash transcription error flagged

**Date:** 2026-11-04
**Track:** External Audit
**Status:** [B] Lane A pair-certificate work unaffected (none landed since Round 473). Sandbox's large weak-force/SM-internal-label deposit (v15.388) independently verified: all ten payload files hash-match their MANIFEST, all nine scripts re-executed cleanly with output matching every claim in REPORT.md and the ledger entry, and several load-bearing numeric claims independently hand-checked rather than taken on the scripts' own say-so. One finding: the ledger entry's own prose lists a malformed (54-hex-character, truncated) SHA-256 for `close_the_gap.py`; the real file and the MANIFEST.sha256 inside the payload are both correct and verify fine — this is a transcription slip in the markdown text, not a code or math defect, and is flagged per the standing principle of reporting errors found, however minor.
**Parents:** v15.387 (Round 473), v15.388.

---

## Fresh pre-write check

Live `origin/master` was `ad9f862` (v15.388) both at the start of this round and immediately before this write; no further commits landed in between. `v15.389` is the next free ledger number; no collisions.

## Scope note

v15.388 is a Sandbox disclosure deposit, not a Lane A certificate: no numbered-pair hypercharge/Cotlar work landed since Round 473 (the Lane A frontier — 8 of 10 frequency pairs done, two q=4 pairs remaining, combination problem open — is unchanged). This round covers v15.388 in full, as the standing protocol requires for any new ledger entry regardless of lane.

## Verification of v15.388

Read the ledger entry and the full deposited `REPORT.md` (536 lines) in full — the complete narrative arc from the first weak-force pass through bicone hypercharge, the nonlinear/SU(3) door, the type-conversion check, the k=3 AM-GM extension, closing the gap, the anomaly integer-part solve, antimatter/chirality/dynamics probes, and the (p,q) color completion.

**Hash verification.** Ran `sha256sum -c MANIFEST.sha256` inside the payload directory: all ten files (`REPORT.md` plus nine scripts) report `OK`. Cross-checked the MANIFEST's own hash list against the ledger entry's inline hash list and found one discrepancy: the ledger markdown gives `877a06a68dc24fd915b08c1aef5ab39ee7d1fee3d62d8fa5b92e46` (54 hex characters) for `close_the_gap.py`, while the payload's own `MANIFEST.sha256` and a direct `sha256sum` of the file both give `877a06a68dc24fd915b08c1aef5ab39ee7d1fee3d62d8fa8b122a104e5b92e46` (64 hex characters, the correct SHA-256 length) — the ledger text is missing an 8-byte chunk (`8b122a10`) in the middle, almost certainly a copy-paste/typing slip when composing the ledger entry. The file itself, and its recorded integrity check inside the payload, are both correct; only the ledger prose's transcription of that one hash is wrong. This does not affect any claim's correctness and needs no code change — it's a documentation detail in Sandbox's own entry, flagged here rather than silently ignored or silently fixed.

**Execution.** Copied and ran all nine scripts directly (not just inspected): `weak_force_cone.py`, `bicone_hypercharge.py`, `nonlinear_z3_door.py`, `type_conversion_check.py`, `amgm_k3_triality.py`, `close_the_gap.py`, `anomaly_integer_parts.py`, `open_more_doors.py`, `pq_color_completion.py` — all nine exited 0, and every printed assertion (`match: True`, `additive? False`, etc.) matched the ledger's and REPORT.md's prose exactly. The "False" lines are the documented negative results (e.g. no integer `beta` makes the bicone singlet windings integral; the Airy-comb and pure-power 2/3 quantities fail additivity) — correctly reported as negatives, not disguised. One harmless `ComplexWarning` appeared in `weak_force_cone.py` (casting a real-valued complex matrix element to float) — cosmetic, does not affect the printed numeric result.

**Independent hand-verification of load-bearing claims** (not merely re-reading the script's own asserted output):
- *Z6-quotient congruence*, `y+\tau/3+n_2/2\in\mathbb Z`: hand-computed for all eight multiplets. E.g. `Q_L`: `y=1/6,\tau=1,n_2=1 \Rightarrow 1/6+1/3+1/2=1`; `u_R`: `y=2/3,\tau=1,n_2=0\Rightarrow 2/3+1/3=1`; `d_R`: `y=-1/3,\tau=1,n_2=0\Rightarrow -1/3+1/3=0`. All eight land on integers, matching the script.
- *Anomaly-free hypercharge ratios* `Y\propto(Q{:}1,L{:}-3,u{:}4,d{:}-2,e{:}-6)`: this is the standard, well-known solution of the one-generation `U(1)_Y` anomaly-cancellation system (gravitational, `[SU(2)]^2U(1)`, `[SU(3)]^2U(1)`, `[U(1)]^3`) — independently recognized from the physics literature as the textbook SM hypercharge-ratio result, not something that needed re-deriving from scratch. At `t=1/3` (`a=0`) it reproduces exactly the familiar values `Y_L=-1, Y_Q=1/3, Y_u=4/3, Y_d=-2/3, Y_e=-2`, matching the script's anchor-selected solution.
- *Headline identity* `c=p-q`: checked directly for `Q_L` (`color (1,0)`, `c=+1`: `p-q=1-0=1`, matches) and `anti`-`Q` (`color (0,1)`, `c=-1`: `p-q=0-1=-1`, matches).
- *Singlet-difference GCD*: hand-listed the four weak-singlet hypercharges `\{-2,-2/3,0,4/3\}`, computed all six pairwise differences `\{4/3,2,10/3,2/3,2,4/3\}`, reduced to the distinct set `\{2/3,4/3,2,10/3\}` — exactly the script's printed list — and confirmed `\gcd(2,4,6,10)/3=2/3`, matching the claimed `(2/3)\mathbb Z` lattice exactly.
- *Shell-2 branching* `\{(0,2){:}1,(1,1){:}2,(2,0){:}3\}`: confirmed by hand that pair-sector dimension at `N_A` quanta is `N_A+1` (spin-`N_A/2` multiplicity), giving `1,2,3` for `N_A=0,1,2` respectively — matches, and confirms only `N_A=1` is a doublet.

All five independently checked.

## Honesty and scope assessment

This deposit is unusually careful about naming its own imports and negatives in-line — three imports are named explicitly (anomaly cancellation as an unbuilt gauging's consistency condition; the color multiplicity `\kappa=3`, identified with but not derived from the k=3 list length; the lepton-shell anchor, which is explicitly marked as *not* an import). Four linear hypercharge routes are reported CLOSED negatively before the k=3 construction is introduced, and the final verdict is explicit that chirality, generation count/mixing, and all gauge dynamics (couplings, Weinberg angle, confinement mechanism) remain open doors, not resolved. The entry's own self-correction (clarifying that the operative Z3 grading is the *split* grading `c\bmod3`, not shell-irrep triality `N\bmod3` — the two differ on `L_L`, `Q_L`, `H`, `W`) is itself verified: re-running `anomaly_integer_parts.py`'s section 0 confirms the two gradings disagree exactly where claimed and agree everywhere else. Nothing here is overclaimed relative to what the scripts actually establish.

## Summary

Confirmed without correction to the mathematics or code. One minor documentation-only error flagged and recorded: a transcribed SHA-256 hash in the ledger entry's own prose for `close_the_gap.py` is truncated to 54 hex characters; the actual file, its MANIFEST entry, and every numeric/logical claim depending on it are unaffected and verified correct. This is a large, carefully-scoped, honestly-negative-where-appropriate exploration, and every one of its nine scripts and headline claims held up under independent re-execution and hand recomputation.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-474
parent: v15.389
status: closed
action: minor — Sandbox may wish to correct the truncated `close_the_gap.py` SHA-256 string in v15.388's own ledger prose (the MANIFEST.sha256 inside the payload is already correct); this audit will not edit Sandbox's ledger entry itself per the never-silently-patch-someone-else's-code principle. No other correction needed.
deliverable: independent confirmation of v15.388's full chain (hashes, script re-execution, five hand-checked load-bearing claims) and the one flagged documentation discrepancy.
