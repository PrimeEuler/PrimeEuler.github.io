# Cone Derivation Ledger v15.1214 — External Audit Round 613

**Date:** 2026-11-19
**Track:** External Audit
**Scope:** Independent verification of v15.1212 and v15.1213 (Lane A Suzuki R4 direct-restart right extensions)

## Method

`git fetch origin master` + `git merge --ff-only` confirmed `f02fe68` as the head, two new entries since Round 612/liveness v15.1210/v15.1211. Read both `Cone_Derivation_Ledger_v15.1212_Lane_A_Suzuki_R4_Direct_Restart_Right_Extension.md` and the v15.1213 companion in full.

These introduce a new "direct-restart" methodology: instead of walking the full path from the anchor (arc 4009) at every run, the boundary matrix at the extension's start arc is assembled directly via `base.assemble(RADIUS, base.midpoint(cuts, start_arc))`. This is a genuine change in mechanism, not just framing, so it was scrutinized at the code level before trusting the rest of the verification pipeline:

1. **Methodology check.** Diffed `lane_a_v15_1212_...py` against the prior right-extension script (`lane_a_v15_1205_...py`). Confirmed the only structural difference is that `build_extension` directly assembles the matrix at the start arc, versus the prior `build_sequence` walking from the anchor and slicing the tail. Read `assemble(radius, x)` and `midpoint(cuts, index)` in the frozen dependency `lane_a_v15_800_suzuki_r3_norm_transport_obstruction.py` (lines 113–185): `assemble` is a pure, closed-form function of `radius` and a scalar midpoint value `x` alone (builds the matrix from `field = x + h @ L4`), with no dependency on path history or any prior computed state. `midpoint` is likewise a pure function of the cuts list and an index. **Conclusion: directly assembling the boundary matrix at the target arc is mathematically identical to walking there incrementally from the anchor — this is a legitimate performance optimization (it was exhausting a 600-second bound via the full walk), not a weakened or unverified shortcut.**

2. **Hash check (both entries).** `sha256sum -c` against each committed manifest confirmed producer, certificate, and both frozen dependencies match exactly:
   - v15.1212: producer `aff9580eb0...`, certificate `3a66d69404...`, manifest `3ec0b3e3dc...`
   - v15.1213: producer `6f01d06f6c...`, certificate `25c47ffb46...`, manifest `5552312a13...`
   (weight-bytes line reproduced in-memory in both, as in every prior entry.)

3. **Provenance re-check (both).** `grep -n "ledger_version"` against both scripts and `grep -c` against both certificates return no match in all four files.

4. **Certificate structure (parsed independently, both).**
   - v15.1212: 32 records, arcs `{4778,...,4809}`, direction +1 only, steps 769–800, 8 rebase flags, max support 160, all pass.
   - v15.1213: 32 records, arcs `{4810,...,4841}`, direction +1 only, steps 801–832, 8 rebase flags, max support 160, all pass.
   Both match their respective ledger entries exactly.

5. **Independent script re-execution (both).** Ran both committed producers end-to-end from a clean environment:
   - v15.1212 emitted `certificate_sha256 = 3a66d69404138ef5079e1b6128d545c2e0146c7a657925bfe6c5ccb350fa1586` — **bit-for-bit identical** to committed.
   - v15.1213 emitted `certificate_sha256 = 25c47ffb4686c15f87310402f601ad4853fe71f67274381e7ac9aabe7e3a8317` — **bit-for-bit identical** to committed.
   All extrema from both regenerated runs matched their ledger entries exactly (max direct/propagated fourth-roots, propagated B4, cumulative/rebase arithmetic bounds, entry discrepancies, weight condition and SHA-256). Both report `STATUS=R4_BLOCK_COVERAGE_PASS`, exit 0.

6. **Union arithmetic.** Independently recomputed in Python:
   - After v15.1212: `{3177,...,4008} ∪ {4010,...,4809}` = 832 + 800 = **1,632 arcs**, 6,387 uncovered — matches.
   - After v15.1213: `{3177,...,4008} ∪ {4010,...,4841}` = 832 + 832 = **1,664 arcs**, 6,355 uncovered — matches. Confirmed 4809/4810 adjacency, so v15.1212 and v15.1213 form one seamless extension.

7. **Collision check.** `v15.1214` and "Round 613" both confirmed unused before this write.

## Verdict

**PASS (both entries).** v15.1212 and v15.1213's mathematics, certificates, and manifests are all independently confirmed bit-exact. The new direct-restart methodology was checked at the code level and found mathematically sound — a pure re-assembly of the boundary matrix, not a shortcut that weakens the certificate. No recurrence of the v15.1199 provenance issue. Filed R4 coverage is now `{3177,...,4008} ∪ {4010,...,4841}`, 1,664 of 8,019 R4 arcs, 6,355 uncovered. No global C4/C16 claim is made or implied; this covers the R4 resource/coverage certificate only.

No other new commits landed during this check. `__pycache__` cleaned before this commit; final freshness check performed immediately before push confirmed no intervening changes.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
