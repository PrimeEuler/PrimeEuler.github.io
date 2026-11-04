# Cone Derivation Ledger v15.358 — External Audit Round 465: signed shifted-sawtooth branch certificate independently verified

**Date:** 2026-11-04
**Track:** External Audit
**Status:** [B] Lane A's exact signed sawtooth branch identities (v15.357) independently re-derived from scratch via direct periodic reduction and confirmed against the frozen witness and the already-audited v15.327 magnitude formulas.
**Parents:** v15.355 (Round 464), v15.356, v15.357.

---

## Fresh pre-write check

Live `origin/master` was `493c4b2` (v15.357) both at the start of this round and immediately before this write; no further commits landed in between. `v15.358` is the next free ledger number; no collisions (one liveness note from this audit thread followed by one Lane A entry, already read and accounted for).

## Verification

Read v15.356 (my own prior liveness note) and v15.357 (Lane A's signed shifted-sawtooth branch certificate) in full.

Independently re-derived all four piecewise branch formulas from scratch, not from the entry's own derivation. With `s(x)=1-x` on `[0,2)`, period 2, and `0<L<2`:

For `x in [0,L)`: `x-L in [-L,0)`, so mod 2 this lands at `x-L+2 in [2-L,2) subset [0,2)`, giving `s(x-L)=1-(x-L+2)=L-x-1`. Then `D_+(x;L)=s(x-L)-s(x)=(L-x-1)-(1-x)=L-2`.

For `x in [L,2)`: `x-L in [0,2-L) subset [0,2)` directly, so `s(x-L)=1-(x-L)=1-x+L`. Then `D_+(x;L)=(1-x+L)-(1-x)=L`.

For `x in [0,2-L)`: `x+L in [L,2) subset [0,2)` directly, so `s(x+L)=1-(x+L)`. Then `D_-(x;L)=(1-x-L)-(1-x)=-L`.

For `x in [2-L,2)`: `x+L in [2,2+L)`, mod 2 lands at `x+L-2 in [0,L) subset [0,2)`, giving `s(x+L)=1-(x+L-2)=3-x-L`. Then `D_-(x;L)=(3-x-L)-(1-x)=2-L`.

All four match the entry's claimed branches exactly: `D_+=L-2` on `[0,L)`, `D_+=L` on `[L,2)`; `D_-=-L` on `[0,2-L)`, `D_-=2-L` on `[2-L,2)`.

Spot-checked numerically by hand with `L=2/3` at the witness's own four sample points (`x=1/3,4/3,2/3,5/3`), computing `saw(x)` and `saw(x-L)` or `saw(x+L)` directly from `1-(x mod 2)`: all four results matched the piecewise formulas exactly (`-4/3`, `2/3`, `-2/3`, `4/3` respectively).

Confirmed the magnitude reduction: `|D_+|=2-L` on `[0,L)` (since `L-2<0` there) and `|D_+|=L` on `[L,2)`; `|D_-|=L` on `[0,2-L)` and `|D_-|=2-L` on `[2-L,2)` — matching the `L` vs. `2-L` branch split already audited in v15.327/v15.343's `k_q(2-L_q)` and `k_qL_q` structure.

Verified the witness file's SHA-256 (`89d01b5b...`) and git blob (`2fd14198...`) against the repo file directly — both match. Copied it into a scratch directory and executed it directly: its printed branch formulas and magnitude statement matched the ledger's claims and my independent derivation exactly.

## Scope check

The entry is correctly scoped: it certifies only the branch functions themselves, under one fixed sign convention, and explicitly notes that changing convention would multiply the whole representation by an immaterial global sign/unitary conjugation. It explicitly states no same-translation product has been simplified yet, and names the actual next gate (insert these signed branches into the four same-translation terms from v15.354, transport arguments, then combine before taking absolute values). `FULL_K_TRANSFER` remains INCONCLUSIVE; no finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed.

## Summary

Confirmed without correction. This entry supplies the missing ingredient (explicit signed coefficient functions, not just their already-audited magnitudes) needed to actually test whether the q=3,5 same-translation groups from v15.354 exhibit any real cancellation once the sawtooth coefficients — not just the scalar sine phases — are combined. No numerical claim is made yet; the frontier remains at 3.273 (Round 456) against the 2.535946 target, and the real test (do these two signed branches at each translation partially cancel when transported and summed) is still open. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-465
parent: v15.358
status: closed
action: none — v15.357's four signed sawtooth branch identities independently re-derived from first principles and confirmed by witness re-execution; no correction needed.
deliverable: independent confirmation of the signed `D_+`, `D_-` branch formulas, their magnitude reduction matching v15.327, and the correctly narrow scope (branch identities only, no product evaluated yet).
