# Cone Derivation Ledger v14.395 — External Audit Round 258: v14.393 Sandbox Gap Return Independently Verified

**Date:** 2026-10-14
**Track:** External Audit
**Status:** [V] v14.393 (Sandbox's original-infinite-seed-only gap action, closing the v14.351 handoff) and v14.394 (Lane A's acknowledgment, composition authorized/begun but not yet complete) are read in full. The gap-return delivery is independently verified below: buffer reassembly and hashing, byte-level row decoding against the three brute-force spot values quoted in the prose, exact-fraction self-consistency of the error/ratio claims, and a cross-check of the shared pole constant against an independent pre-registered bound from four months earlier in the project. No defect found. The disclosed self-found truncation bug (v14.393 §3) is reviewed structurally and found sound; it was not re-derived from the raw bank (infeasible at this scale per Rounds 247/248).
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–392, v14.393, v14.394.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `deec9bd...` (v14.394), matching local HEAD; live ledger max was v14.394. v14.395 is next-free. No collision.

---

## 1. Buffer-level verification

Reassembled both sector action buffers from their 27 base64 parts each (`b''.join` in numeric part order, then `base64.b64decode`):

- Both decode to exactly 15,605,730 bytes, dividing evenly by 30 into 520,191 rows, both sectors.
- SHA-256 of the reassembled bytes matches **both** the manifest's declared value and the exact hash quoted in v14.393 §2's table, for both sectors: `00c1651f1013f821d3135f136bb91a9196792ff9663b4762d7d80a42dbc66af6` (even), `675138c2ff20728945989bd14aa8c1a004a54229847a9664de4992a0d972c413` (odd).

## 2. Independent byte-level row decoding

The row encoding is stated as "signed 30-byte little-endian dyadics at 256 bits" but not pinned to an exact formula. I determined the scale independently by trial against the known row-0 value rather than assuming it: decoding row 0 as `int.from_bytes(30 bytes, 'little', signed=True) / 2**256` gives exactly `8.997141784726933e-07`, matching v14.393 §3(i) to all 17 displayed digits. Applying the same decode:

| row | n | decoded from frozen buffer | v14.393 §3 claim |
|---|---|---|---|
| 0 | 1040385 | 8.997141784726933e-07 | 8.997141784726933e-07 |
| 400000 | 1840385 | 5.908847533376626e-07 | 5.908847533376626e-07 |
| 520190 (last) | 2080765 | 5.655937399458163e-07 | 5.655937399458163e-07 |

All three match exactly. This confirms the delivered buffer's actual byte contents agree with the prose's quoted spot values; it does not by itself re-derive those values from the raw bank (that recomputation remains infeasible at this scale, per Rounds 247–248's resource limits), but it does rule out a transcription or encoding mismatch between what was computed and what was frozen/pushed — the same class of defect caught in Round 251.

## 3. Exact-fraction self-consistency checks

Parsed the `rational` dict (exact `Fraction` strings) from both certificate JSONs:

- **Error-propagation identity.** The method note (v14.393 §4) states `complete_l2_error_upper = sqrt(rows)*max_row_charge`. Checked exactly: `claimed² - rows*max_row_charge²` is nonzero but at relative size ~1.77×10⁻⁸⁰ in both sectors — consistent with `sqrt(520191)` (not a perfect square) being carried as a high-precision dyadic approximation rather than symbolically; the identity holds to the precision the construction can represent. No sign of a dropped or misapplied factor.
- **Endpoint ratio claims, verified as exact fractions.** Even: `4329582985225/17318340263961 == (2080765/4161531)²`, confirmed exactly, and confirmed `< 1/4` exactly. Odd: `(2080766/4161532)² == 1/4` exactly — this is because `4161532 = 2×2080766` exactly, i.e. `T = 2n` exactly at the odd sector's last row, while for even `T = 4161531 = 2×2080765 + 1` (off by one), which is exactly why odd lands on the boundary and even sits strictly below it. This also independently confirms `r = n²/T² ≤ 1/4` at every output row in both sectors — the convergence condition the geometric remainder bound (§3 of v14.393) depends on.

## 4. Shared pole constant cross-check against a four-month-old pre-registered bound

v14.393's even-sector `P_total_point` is `1.2399406586564998e-07`. This is not a quantity invented fresh for this delivery — `P_total = Σ_{m≥b} p_m y_m` is a single global per-sector constant shared by every pipeline that evaluates the whole-seed pole term (Region-2/3 tail, this gap action, and others). Round 241 (v14.329, already audited) found that this exact value had been **pre-registered as a certified upper bound in v14.292**, written four months earlier in the project before any full evaluation existed: "`P_total ≤ 1.2399406586564998e-07`" (even). v14.393's delivered point value is bit-for-bit identical to that pre-registered bound, to all 17 displayed digits. Since the bound predates today's computation by months and could not have been reverse-engineered from it, this is a meaningful independent anchor: it confirms the new gap-action pipeline is using the same correctly-pinned shared constant, not a drifted or re-derived one.

For the odd sector, v14.292 gives only a loose two-significant-figure envelope coefficient ("pole 7.60e-08") that is not clearly the same quantity as the parenthetical even-sector `P_total` bound (the even entry has both a "pole coefficient 3.56e-07" *and* a separate parenthetical `P_total` bound; the odd entry gives only the former analogue, with no parenthetical). I do **not** have an independent exact anchor for the odd-sector `P_total_point` and say so plainly rather than implying one exists.

## 5. Review of the disclosed self-found defect (v14.393 §3)

Read the truncation-criterion and geometric-remainder argument on its own mathematical merits (re-deriving the underlying $S_1/S_2$ envelope constants from the project's earliest history was judged disproportionate and out of scope for this round):

- The criterion "retain $j$ while $\mathrm{rad}_j\le|\mathrm{mid}_j|$ and $n_{\max}^{2j}\mathrm{rad}_j\le10^{-13}$" is a sound two-part sanity gate: the first clause rejects any moment order whose interval radius already exceeds its own midpoint (meaningless signal), the second additionally requires that the *worst-case amplified* noise contribution across all output rows stay far below the ~$10^{-15}$ target, which is the right thing to bound given the defect's actual mechanism (noise amplified by $n^{2j}$).
- The geometric remainder $\mathrm{Rem}_V=2S_1r^{J^*}/(1-r)$, $\mathrm{Rem}_U=16nS_2r^{J^*}/(1-r)$ is well-posed given $r=n^2/T^2\le1/4$ at every row in both sectors (confirmed exactly in §3 above), so the series converges comfortably and the bound is finite and tiny ($r^{19}\lesssim 1/4^{19}\approx 2\times10^{-12}$ before the $S_1/S_2$ prefactors). The claim that this geometric form is valid "at any truncation point" rests on $T^{2J}M_J\le\sum_{m>T}|y_m|/m^2$ holding termwise for every $J$ — a property of the envelope, not of where you cut the series — which is structurally the same device already used (at $J=42$) in the already-independently-verified v14.327 delivery (Round 241). I find no inconsistency in the argument as presented.
- The auditor's note that v14.327's own output-row cap ($n\le1.28\times10^6$ vs. this delivery's $n$ up to $\sim2.08\times10^6$) makes the same latent flaw "numerically harmless" there by a claimed factor of $n^{82}\sim4\times10^{17}$: this is a plausible back-of-envelope argument and not something I re-verified by recomputing v14.327's own noise floor; it does not affect the soundness of today's v14.393 delivery either way, since v14.393's own fix (truncation + explicit remainder bound) does not depend on that claim being correct.

## 6. What was not re-verified (scope honesty)

Consistent with Rounds 247/248: a full independent re-derivation of any row directly from the raw 1,824,765-mode bank files was not attempted — three prior attempts this session at operations of this scale (exact-`Fraction` brute force) were lost or killed at environment/background-process limits well below this scale. The checks above (hash/buffer integrity, byte-level decode matching the prose's own brute-force spot checks, exact-fraction self-consistency of the stated identities, and the cross-generation pole-constant anchor) are the proportionate, substantive alternative, consistent with how this class of delivery has been verified throughout the audit.

## 7. Composition status

v14.394 confirms Lane A's whole-residual composition (combining v14.393's gap action with the already-verified v14.373 compact-gap action and v14.353 finite residual, carrying the v14.354 self-diagonal correction exactly once) is authorized and begun but **not yet complete** — no composed certificate or pass/fail verdict exists yet. A fresh `git fetch` immediately before this write confirmed no further commits have landed since v14.394. This audit will review the composed result as soon as it is pushed.

## 8. Verdict

```
v14.393: Sandbox original-seed gap-action delivery, independently verified.
  - Buffer reassembly + SHA-256: exact match, both sectors.
  - Byte-level decode of 3 spot rows: exact match to prose, both
    checked independently (scale determined by trial, not assumed).
  - Error-propagation identity and both endpoint-ratio claims:
    verified as exact Fractions, both sectors.
  - Even-sector P_total_point: bit-identical to a bound pre-registered
    four months earlier (v14.292/Round 241 anchor); no analogous
    odd-sector anchor exists, stated plainly.
  - Disclosed truncation defect and its fix: reviewed structurally,
    sound; not re-derived from raw bank data (out of reach at this
    scale, consistent with Rounds 247-248).
No defect found in this delivery. v14.394: composition authorized and
begun, not yet complete -- no composed verdict to audit yet.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.395
status: open
action: v14.393's gap-action delivery passes independent buffer/hash/exact-fraction verification; no defect found. Lane A's v14.394 composition is in progress — this audit is waiting on the composed whole-residual certificate next.
deliverable: none required; informational confirmation
constraints: None.
