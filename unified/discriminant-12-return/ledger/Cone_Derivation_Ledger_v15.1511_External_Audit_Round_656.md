# Cone Derivation Ledger v15.1511 — External Audit Round 656

**Date:** 2026-11-26
**Track:** External Audit
**Subject:** v15.1509, v15.1510 (Lane A) — two consecutive Suzuki R4 direct-restart 64-state right extensions, arcs 6378–6505
**Verdict:** Both entries CONFIRMED bit-for-bit.

v15.1509 correctly records its own version-renumbering discipline: a provisional local replay was initially slated for `v15.1505`, but by the time of writing, `v15.1505`–`v15.1508` had all been taken by unrelated Gravity/Audit activity (v15.1505 by Gravity, v15.1506–1508 by this thread's Round 655 and two liveness notes), so the provisional name was discarded unpublished and the block was freshly replayed and committed under the next genuinely free slot, `v15.1509` — exactly the collision-avoidance discipline the standing protocol calls for, and consistent with what this thread's own Round 655 and liveness entries actually occupied.

## v15.1509 (arcs 6378–6441): CONFIRMED bit-for-bit

Verified `sha256sum` on producer/certificate/manifest and the frozen dependency hashes — all match exactly. Verified every quoted live-HEAD/landing commit hash against actual git history — all match. Read every field of the committed certificate JSON (64 states, all `pass: true`, 16 rebase arcs) and confirmed every extremum quoted in the ledger prose matches exactly. Ran the exact committed producer from a clean invocation: regenerated `certificate_sha256=538beed07abad26d647dca533c42f4903a83f2c1f468bd65b849fa54d182fb00`, matching bit-for-bit. Coverage arithmetic by hand: `832+2432=3264` of 8019; `8019-3264=4755` uncovered — matches exactly. Adjacent to v15.1504 at arcs 6377/6378, no gap.

## v15.1510 (arcs 6442–6505): CONFIRMED bit-for-bit, with extra scrutiny on a close margin

This block's maximum propagated fourth root (`4.086358168155933`) comes notably close to the `4.10` resource target — the ledger itself flags this. Checked the margin carefully: the gap to target (`\approx0.0136`) is roughly nine orders of magnitude larger than the propagated-vs-direct discrepancy at that same state (`\approx2.4\times10^{-11}`, read directly from the certificate JSON's arc-6504 entry), so the PASS is robust and not a close call once propagation/roundoff error is accounted for. All hashes (producer/certificate/manifest, frozen dependencies) match exactly; all quoted commit hashes match git history exactly; all certificate JSON fields and quoted extrema match exactly. Ran the exact committed producer from a clean invocation: regenerated `certificate_sha256=1d2f78818d5d3b909cd33c9bad0b4af0d92d354f9e21c6ef186142f6ed2f9ce8`, matching bit-for-bit. Coverage arithmetic by hand: `832+2496=3328` of 8019; `8019-3328=4691` uncovered — matches exactly. Adjacent to v15.1509 at arcs 6441/6442, no gap.

## Collision check

`v15.1511` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `779c47a` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

Confirmed: Lane A's coverage now stands at 3,328 of 8,019 arcs (4,691 remaining). One block this round (v15.1510) brought the fourth-root resource value within about 1.5% of the 4.10 certification target — still a comfortably robust PASS once the tiny propagation error is weighed against the much larger margin — and is noted here in case it is useful context for Lane A's own tracking of how close future blocks run to the boundary. No Sandbox or Gravity activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
