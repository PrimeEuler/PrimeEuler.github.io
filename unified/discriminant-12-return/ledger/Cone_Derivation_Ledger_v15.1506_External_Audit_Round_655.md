# Cone Derivation Ledger v15.1506 — External Audit Round 655

**Date:** 2026-11-26
**Track:** External Audit
**Subject:** v15.1504 (Lane A) — Suzuki R4 direct-restart 64-state right extension, arcs 6314–6377; v15.1505 (Gravity) — 32³ GH Einstein-H² evolution independently confirmed on a 64³ off-grid monitor and checkpointed half-timestep refinement through T=.04
**Verdict:** Both entries CONFIRMED.

## v15.1504 (Lane A, arcs 6314–6377): CONFIRMED bit-for-bit

Verified `sha256sum` on producer/certificate/manifest and the frozen dependency hashes — all match exactly. Verified every quoted live-HEAD/landing commit hash against actual git history — all match. Read every field of the committed certificate JSON (64 states, all `pass: true`, 16 rebase arcs) and confirmed every extremum quoted in the ledger prose matches exactly. Ran the exact committed producer from a clean invocation: regenerated `certificate_sha256=3e097a606a95f5236296bb21393e8259d49e55e1b3d337ebf671a92e413ada74`, matching bit-for-bit. Coverage arithmetic by hand: `832+2368=3200` of 8019; `8019-3200=4819` uncovered — matches exactly. Adjacent to v15.1501 at arcs 6313/6314, no gap.

## v15.1505 (Gravity, 32³ GH off-grid + checkpointed half-dt): CONFIRMED

Before running anything, independently re-derived the entry's claimed "fast" harmonic-gauge formula by hand. Expanding the standard contracted Christoffel `\Gamma^\mu=g^{\nu\rho}\Gamma^\mu_{\nu\rho}=g^{\nu\rho}\cdot\tfrac12g^{\mu\sigma}(\partial_\nu g_{\sigma\rho}+\partial_\rho g_{\sigma\nu}-\partial_\sigma g_{\nu\rho})$, the first two terms coincide under the `\nu\leftrightarrow\rho$ relabeling (since `g^{\nu\rho}` and `g_{\sigma\rho},g_{\sigma\nu}` are symmetric), giving exactly `\Gamma^\mu=g^{\mu\alpha}g^{\nu\beta}\partial_\nu g_{\alpha\beta}-\tfrac12g^{\mu\nu}g^{\alpha\beta}\partial_\nu g_{\alpha\beta}` — precisely the entry's claimed divergence-of-inverse-metric shortcut, confirmed as an exact algebraic identity with the standard definition, not an approximation. Verified the committed `fast_harmonic_constraint` function implements exactly this formula (inspected line-by-line; `inv` raises both free indices, `d` concatenates the time derivative `p` with `grid.grad(g)`, and the trace/subtraction structure matches term-for-term).

Ran `k4_gh3d_offgrid_timestep_v15_1505.py` exactly as committed, all three documented invocations (`offgrid`, `first --checkpoint`, `second --checkpoint`) with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1` as specified:
- **Gate 1422 (off-grid):** native N32³ and the same evolved state reconstructed on 64³ both matched the ledger table closely — the native `max_inverse_gtt=-0.9987381424513845` matched **exactly**, and GH/H/M matched to within the same last-few-digit roundoff tolerance already documented in prior rounds (Rounds 648, 650–653); the off-grid Hamiltonian ratio I computed (`\approx0.884$ of the native value) matches the ledger's claimed "~0.884" exactly.
- **Gate 1423 (checkpointed half-timestep):** checkpoint 1 (T=.02) matched within the same tolerance; checkpoint 2 (T=.04, resumed) matched closely, with `H=1.2635389387343973\times10^{-10}` and `max\_inverse\_gtt=-0.9987381424513847` matching **exactly**, and the reported dt=.002-vs-dt=.004 absolute differences (`\approx4.72\times10^{-15}$, `1.38\times10^{-13}`, `1.95\times10^{-14}`) matching the ledger's quoted values closely.

This entry resolves, for its own numbers, the `inverse g^tt` discrepancy flagged in Round 653 against v15.1495/1496 — here the value matches exactly rather than differing by `\sim10^{-7}`, suggesting that earlier discrepancy was specific to those two entries (or their execution environment) rather than a persistent issue with the underlying solver.

## Collision check

`v15.1506` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `06cc004` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

Confirmed: Lane A's coverage now stands at 3,200 of 8,019 arcs (4,819 remaining). Gravity has now closed both outstanding items from v15.1496 (off-grid certification and timestep refinement at N32, T=.04) using a genuinely independent and mathematically verified divergence-of-inverse-metric shortcut for the harmonic-gauge monitor — a legitimate performance optimization, not an approximation, as confirmed by an exact hand re-derivation from the standard Christoffel formula. The off-grid Hamiltonian residual at N32 is now close to its native value (unlike N24's earlier ~3.9× increase), consistent with the resolution-dependent aliasing picture built over the last several rounds. The previously flagged `inverse g^tt` discrepancy did not recur here.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
