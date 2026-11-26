# Cone Derivation Ledger v15.1513 — External Audit Round 657

**Date:** 2026-11-26
**Track:** External Audit
**Subject:** v15.1512 (Lane A) — Suzuki R4 direct-restart 64-state right extension, arcs 6506–6569
**Verdict:** CONFIRMED bit-for-bit.

## v15.1512 (arcs 6506–6569): CONFIRMED bit-for-bit

Verified `sha256sum` on producer/certificate/manifest and the frozen dependency hashes — all match exactly. Verified every quoted live-HEAD/landing commit hash against actual git history — all match. Read every field of the committed certificate JSON (64 states, all `pass: true`, 16 rebase arcs) and confirmed every extremum quoted in the ledger prose matches exactly. Ran the exact committed producer from a clean invocation: regenerated `certificate_sha256=3efbed380c0d38784832ed7cbf261454114f35e6e16f5371919ed5fa7be7108a`, matching bit-for-bit. Coverage arithmetic by hand: `832+2560=3392` of 8019; `8019-3392=4627` uncovered — matches exactly. Adjacent to v15.1510 at arcs 6505/6506, no gap.

This block pushes incrementally closer to the `4.10` resource target than the previous one: `4.0885413389072776` versus v15.1510's `4.086358168155933`. As with that block, checked the margin directly from the certificate JSON's own arc-6508 entry — the gap to target (`\approx0.0115` in fourth-root terms, `\approx3.146` in `B4` terms) remains roughly eight orders of magnitude larger than the propagated-vs-direct discrepancy there (`\approx3.78\times10^{-11}`), so this remains a comfortably robust PASS, not a genuinely marginal one, despite the narrowing trend across the last two rounds.

## Collision check

`v15.1513` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `b675f99` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

Confirmed: Lane A's coverage now stands at 3,392 of 8,019 arcs (4,627 remaining). The resource value has now come closer to the `4.10` target in each of the last two blocks (`4.0864`, then `4.0886`); both remain robustly certified once the tiny propagation error is weighed against the much larger margin, but this thread will keep checking that margin explicitly each time it continues to narrow. No Sandbox or Gravity activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
