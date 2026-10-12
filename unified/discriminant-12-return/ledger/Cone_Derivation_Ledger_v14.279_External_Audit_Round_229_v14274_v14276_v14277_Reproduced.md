# Cone Derivation Ledger v14.279 — External Audit Round 229: v14.274's Weighted Remainder, v14.276's Direct Later-Start Moments, and v14.277's Compact Far Action All Independently Reproduced Byte-for-Byte

**Date:** 2026-10-12
**Track:** External Audit
**Status:** [V] All three new frozen-payload gates this round reproduce byte-for-byte from fresh, independent execution: v14.274's coded Region-1 weighted-remainder bounds (both sectors), v14.276's direct later-start inverse-moment banks at the doubled start $a=2b+(b\bmod2)$ (both sectors, the heaviest check — 1736 fresh oscillatory plus 127 fresh nonoscillatory real-scalar evaluations per sector, $\approx$135s each), and v14.277's compact-support Far action coefficients built from the actual archived CI finite lift (both sectors, including all three direct 256000-term row identity checks per sector). Independently hand-verified the two analytic lemmas behind v14.274's bound (the spacing-two tail sum $\le1/a^2+1/(2a)$ and the harmonic bound $\sum_{k\le K}1/(2k)\le(1+\log K)/2$) and the parity-preservation arithmetic of $a=2b+(b\bmod2)$. v14.275/v14.278 (Sandbox) are code-in-progress in a private workspace with no committed artifact to byte-check; their one concrete numeric claim is order-of-magnitude plausible given the now-reproduced v14.276 moments. No correction found.
**Parents:** v14.223, v14.250, v14.253, v14.263–278.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `b54837b...` (v14.278), matching local HEAD; live ledger max was v14.278. v14.279 is next-free. No collision.

---

## 1. v14.274 — coded Region-1 weighted remainder, reproduced and hand-checked

Ran `suzuki_close_far_weighted_remainder.py` fresh against the v14.223 whole-affine-source input. Output matched v14.274's table exactly (far remainder $l^2$ upper `2.2966109888139326e-29`/`2.2944565550627643e-29`; close envelope `1.2148315536564526e-05`/`1.2136907439373943e-05`) and the produced JSON is **byte-for-byte identical** to the committed `corrected-weighted-remainder.json` (SHA `e8d00dc1...`, matching on both sides).

Independently re-checked the two analytic steps behind the bound:
- **Far weighted-sum bound.** For the same-parity spacing-two sum $\sum_{m=a,a+2,\dots}1/m^2$, the claimed bound $1/a^2+1/(2a)$ (first term plus a half-weight integral tail) was checked against a direct 200000-term partial sum at $a=1000$: partial sum $\approx4.9925\times10^{-4}$, claimed bound $5.01\times10^{-4}$ — the bound exceeds the (necessarily incomplete, smaller) partial sum by a small positive margin, consistent with a valid, non-vacuous upper bound.
- **Close harmonic bound.** $\sum_{k=1}^K1/(2k)\le(1+\log K)/2$ is the standard harmonic-number bound $H_K\le1+\ln K$ (valid since $H_K-\ln K\to\gamma\approx0.577<1$), applied at half-weight for the spacing-two close range. Correct.
- Confirmed the close-bound algebra is internally consistent: $8C(1+\log K)/(22b)=4C(1+\log K)/(11b)$, matching the expected $(8/|n-m|\text{ kernel})\times(C/(11b)\text{ pointwise }y\text{ bound})\times(\text{harmonic sum})$ composition, using the same $|y(m)|\le C/(11m)\le C/(11b)$ bound (for $m\ge b$) that underlies the far row's own $C/(11m)$ factor.

## 2. v14.276 — direct later-start inverse moments, reproduced for both sectors

Ran `suzuki_later_start_inverse_moments.py` fresh for both sectors — the heaviest check this round, since (per the entry's own description) the real scalar bank is evaluated **fresh at the new start $a$**, not read from the old $b$-start bank (that bank's hash is checked only as a provenance pin, exactly as v14.276 states). Each run freshly evaluated 127 nonoscillatory real-scalar powers and 1736 oscillatory scalar primitives, taking $\approx$135s/sector.

- even-v: max radius `8.946278037620597e-46`, matching exactly; output **byte-for-byte identical** to the committed JSON (SHA `d141dcda...`).
- odd-v: max radius `8.939435759962761e-46`, matching exactly; output **byte-for-byte identical** (SHA `c9ece888...`).

Checked the parity-preservation arithmetic directly from the reproduced output: even-v has $b=512001$ (odd) and $a=2\cdot512001+1=1024003$ (odd) — same parity preserved; odd-v has $b=512002$ (even) and $a=2\cdot512002+0=1024004$ (even) — same parity preserved. In general $a=2b+(b\bmod2)$ always has the same parity as $b$ ($2b$ is always even; adding $b\bmod2$ flips it to match $b$'s parity exactly when $b$ is odd, and leaves it even when $b$ is even), confirming this is the correct "first same-parity mode at or above $2b$" as claimed.

The monotonicity claim ("every nonprime remainder and pole remainder decreases with the lower limit, so retaining the original $b$-start model-error budgets at the later start $a$ is conservative") is immediate from the shape of the v14.262 budget formulas themselves (e.g. $7000/(3n)^9$, $13(4/(3n))^8$ — manifestly decreasing in $n$), so reusing the $b$-start budget as a looser-but-valid bound at $a>b$ needs no further re-derivation.

## 3. v14.277 — compact Far action from the actual CI lift, reproduced for both sectors

Ran `suzuki_infinite_seed_compact_far_action.py` fresh for both sectors, binding the actual archived CI lift witness binaries (the same ones independently replay-certified in Round 227) rather than any local numerical proposal. Output matched exactly: even-v combined-support norm upper `24464309065.055855`, geometric remainder upper `6.88060509181381e-16`; odd-v norm upper `483661816.5248495`, remainder upper `1.3603024506628133e-17`. Both JSON outputs are **byte-for-byte identical** to the committed payloads, and both sectors' three direct Far-row checks (each comparing the retained 42-moment expansion against a full direct sum over all 256000 compact-support terms, via the exact geometric-tail identity used since Round 221) reproduced and passed identically — the strongest available check, since it validates the retained/omitted split against the complete direct sum rather than trusting the moment machinery alone.

Noted that this "Far" (output $n>4R$, finite compact support) is the mirror-image case from Round 221/v14.240/v14.243 — a different object from Region 1's "far input $m$" terminology in v14.264–278 — and is explicitly scoped as excluding the infinite-tail D·y action (`infinite_seed_tail_action_included: False`), consistent with the entry's own stated scope.

## 4. v14.275/v14.278 (Sandbox) — no committed artifact; one plausibility check

These two entries describe evaluator code living in Sandbox's private `~/workspace/d12/` namespace, never committed to the repository, so there is no frozen JSON to byte-check. Their one concrete numeric claim — $S_{\rm far}(n{=}b{-}2)\approx-2.077\times10^{-7}$ (even-v) using the now-reproduced v14.276 moments — is order-of-magnitude plausible: with $n/a\approx0.5$, $\overline U_j,\overline V_j=O(1)$, and $1/a\approx10^{-6}$, the leading term of $(c/a)\sum_j(n/a)^{2j+1}\overline U_j$ is $O(10^{-6})$, consistent with the claimed $2\times10^{-7}$. This is not a certification, only a sanity check that the claim is not wildly inconsistent with the data it is built from.

Also noted, purely as informational context and not something this auditor is positioned to evaluate: v14.278 §4 states that Sandbox's standing authorization covers autonomous ledgering of handoff responses only, and that committing code/payloads to `research-notes/` requires separate per-item approval from the project's human principal — which is why v14.276's request to commit the evaluator code into the repository was declined. This is an internal permission boundary between Sandbox and its principal, not a claim this audit thread verifies or acts on.

## 5. Verdict

```
v14.274: coded Region-1 weighted-remainder bounds INDEPENDENTLY
  REPRODUCED byte-for-byte (both sectors). The spacing-two tail-sum
  bound and the close-range harmonic bound are both independently
  hand-verified as standard, correctly-applied inequalities.
v14.276: direct later-start inverse-moment banks at a=2b+(b mod 2)
  INDEPENDENTLY REPRODUCED byte-for-byte for both sectors, including
  fresh (not cached) real-scalar evaluation at the new start. Parity
  preservation of a=2b+(b mod 2) confirmed by direct arithmetic on
  the actual b,a values in both sectors.
v14.277: compact Far action coefficients from the actual archived CI
  lift INDEPENDENTLY REPRODUCED byte-for-byte for both sectors,
  including all six (three per sector) full 256000-term direct-row
  identity checks.
v14.275/v14.278: no committed artifact to byte-check (private
  Sandbox workspace); one concrete numeric claim is order-of-
  magnitude plausible against the reproduced v14.276 data.
No correction found in any claim this round. No ledger content is
  altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.279
status: open
action: v14.274's weighted-remainder gate, v14.276's direct later-start moment banks, and v14.277's compact Far action coefficients are all independently reproduced byte-for-byte for both sectors, with the underlying analytic lemmas (tail-sum and harmonic bounds, parity preservation) independently hand-verified. No corrections to report this round. Sandbox's Region-1 evaluator work (v14.275/v14.278) is noted as in-progress and not yet certifiable since it has no committed payload.
deliverable: none required; informational confirmation
constraints: None.
