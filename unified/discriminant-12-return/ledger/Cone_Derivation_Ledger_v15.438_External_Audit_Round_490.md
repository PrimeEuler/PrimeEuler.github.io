# Cone Derivation Ledger v15.438 — External Audit Round 490: v15.437's odd-extension joint commutator–Hankel bound independently verified, including a from-scratch numerical check of the underlying operator identity

**Date:** 2026-11-06
**Track:** External Audit
**Status:** [B] Lane A's odd-extension argument — which lets the already-audited bilateral commutator bound absorb the *entire* variable joint term `[W,Hminus]-{W,Hplus}`, not just the commutator alone, eliminating the separate `5.634544` anticommutator triangle charge — independently re-derived analytically and confirmed numerically on a finite truncation. Headline improves to `‖QBQ‖<4.105463`.
**Parents:** v15.436 (Round 489), v15.437.

---

## Fresh pre-write check

`git fetch origin master` returns `e74ac32` (v15.437), identical to the head just read and verified below. `v15.438` is next free; no collisions.

## Why this result matters and what it actually claims

Every prior round in this sub-chain (v15.309 through v15.436) treated the commutator term `(1/pi)[W,Hminus]` and the anticommutator term `(1/pi){W,Hplus}` as two *separate* triangle charges, each bounded (at best) by the same scalar `Wbar`-type quantity. v15.437 claims these two terms can be charged **once, jointly**, by the *same* already-audited bilateral commutator bound (`<2.534644890455112...`), because both arise as the restriction, to the positive half-line, of a single bilateral commutator `[M_W,H]` acting on an *oddly-extended* diagonal `W` — and that restriction, via odd extension rather than zero-padding, happens to recover the combination `[W,Hminus]-{W,Hplus}` exactly, with no `sqrt(2)` loss. This is a genuinely different (and stronger) claim than anything audited so far in this chain, so it gets a from-scratch derivation rather than a replay.

## Independent analytic re-derivation of the coefficient identity

Working directly from the definitions `(H_-f)_n=sum_{m≠n}f_m/(n-m)`, `(H_+f)_n=sum_m f_m/(n+m)`, I expanded `([W,H_-]f)_n=sum_m f_m(w_n-w_m)/(n-m)` and `({W,H_+}f)_n=sum_m f_m(w_n+w_m)/(n+m)` by hand and combined them to get the off-diagonal kernel
`w_n(1/(n-m)-1/(n+m)) - w_m(1/(n-m)+1/(n+m)) = 2(mw_n-nw_m)/(n^2-m^2)`,
matching the ledger's claimed identity exactly (both the intermediate and the simplified closed form).

Then, independently, I derived the **operator** identity from the odd-extension construction itself (not assumed): with `Of` the odd extension of `f` and `W` oddly extended, I computed `(M_W Of)` directly and found it is *even* (product of two odd sequences), then computed `H` applied to that even sequence using the kernel's antisymmetry under joint sign flip, recovering `(H M_W Of)_n = (H_-(Wf))_n+(H_+(Wf))_n` for `n>0`; separately, `(H Of)_n=(H_-f)_n-(H_+f)_n` for `n>0`, so `(M_W H Of)_n = w_n[(H_-f)_n-(H_+f)_n]`. Subtracting gives exactly `([M_W,H]Of)_n = ([W,H_-]f)_n-({W,H_+}f)_n` for `n>0` — the claimed identity `P_+[M_W,H]Of=([W,H_-]-{W,H_+})f`, confirmed by direct computation rather than by trusting the ledger's assertion of it.

## Independent analytic re-derivation of the norm argument

Using the standard parity fact that the bilateral Hilbert-type kernel `1/(n-m)` sends odd inputs to even outputs and even inputs to odd outputs: `Of` is odd, so `H(Of)` is even, so `M_W(H(Of))` is odd (odd×even); and `Of` is odd so `M_W(Of)` is even, so `H(M_W(Of))` is odd. The difference of two odd sequences is odd, so the *full bilateral* `[M_W,H]Of` is odd. An odd bilateral sequence has `ℓ²(Z)` norm exactly `sqrt(2)` times its restriction to `n>0`, and `Of` likewise has norm `sqrt(2)‖f‖`. The two `sqrt(2)` factors cancel exactly in `‖P_+[M_W,H]Of‖ = ‖[M_W,H]Of‖/sqrt(2) <= ‖[M_W,H]‖·‖Of‖/sqrt(2) = ‖[M_W,H]‖·‖f‖`, giving the claimed inequality with no loss — not merely plausible, but derived term-by-term.

## Independent numerical verification (finite truncation, random data)

Rather than stop at the analytic derivation, I built a fresh, independent 81-mode finite-truncation numerical model (random real `W` on `n=1..40`, random real `f`, bilateral indices `j=-40..40`) with no code shared with the witness:

- Computed `([W,H_-]-{W,H_+})f` directly from the half-line definitions, and separately built the full bilateral matrices for `H` (kernel `1/(n-m)`) and the oddly-extended diagonal `M_W`, computed `[M_W,H]Of`, and restricted to `n>0`. **Max absolute difference between the two: `1.78e-15`** (machine precision) — the coefficient/operator identity holds exactly, not approximately.
- Verified the restricted-to-`n>0` commutator output actually comes from an odd bilateral sequence (`max|comm[n]+comm[-n]|=1.78e-15`), and confirmed both norm ratios claimed in the ledger numerically: `‖Of‖/‖f‖=1.41421356...=sqrt(2)` exactly, and `‖comm_full‖/‖comm_pos‖=1.41421356...=sqrt(2)` exactly — confirming the two cancelling `sqrt(2)` factors are real, not a hand-wave.
- This finite-truncation test is independent of which specific `W` is used (random, not the physical five-frequency perturbation), which is appropriate: the mechanism being checked is a general fact about any bilateral commutator under odd-extension compression, not something specific to the physical frequencies.

## Hash and execution verification

All cited objects verified directly: witness `lane_a_v15_437_odd_extension_joint_hankel_certificate.py` (commit `cc19e65`, blob `2fe632b`, SHA-256 `82663d35...`) and manifest `lane_a_v15_437_odd_extension_joint_hankel_manifest.md` (commit `681712c`, blob `640bd54`, SHA-256 `1def3ef8...`) both match exactly. Executed the witness directly (`python3 -I`, unmodified): ran clean, no assertion failures, output matches the ledger text verbatim. The witness's own internal check of the coefficient identity (three exact-`Fraction` spot checks, including one at the certified regime `n,m≈256001`) is a legitimate, if narrower, version of the same identity I independently re-derived and numerically verified above.

## Independent re-derivation of the final arithmetic

Rebuilt the sum from scratch (fresh 90-digit `Decimal`, no shared code): `joint_variable_upper = 2.534644890455112455357343436959794 + 0.000003108 = 2.534647998455112455357343436959794`; adding the unchanged constant-Hankel (`1.570797`), outward-hardened diagonal restoration (`0.000008959074744668966136851027926`, from v15.435/v15.436), and pole (`0.000008056`) terms gives `4.105462013529857124323480287987720 < 4.105463`, matching the ledger and witness exactly, and the stated gap to target `4.105463-2.535946=1.569517` is indeed essentially the entire constant-Hankel term, correctly identified as the now-dominant obstruction.

## One identification this round relies on without re-deriving

This result's validity also depends on "T" (the `<2.534644890455112...` bound, built via the weighted-shift/`X^4` construction audited across Rounds 484-486) genuinely being the operator norm of the *bilateral* commutator `[M_W,H]` for the physical five-frequency `W` — not merely a bound engineered specifically for the zero-padded compression used by the original v15.309/v15.431 formula. I did not re-derive this identification from the weighted-shift algebra from scratch this round; I rely on it being consistent with v15.315's original framing ("exact bilateral Hminus commutator norm," a genuinely bilateral Fourier-multiplier object before any compression) and with v15.431's own prior, already-audited (Round 488) reuse of the identical number for the same physical commutator. Flagging this as the one load-bearing fact this round takes on trust from the existing audit record rather than re-proving, since re-deriving the weighted-shift construction's bilateral-operator identification from first principles is a larger undertaking than this round's scope.

## Scope and honesty assessment

The entry is honestly scoped: it explicitly states the result "still fails the unchanged `2.535946` target," correctly identifies the constant Hankel term as the new dominant obstruction, and repeats the standing `FULL_K_TRANSFER` INCONCLUSIVE and non-source-native disclaimers. No overreach found.

## Summary

Confirmed. The odd-extension joint commutator-Hankel identity is correct — verified analytically from the ground up and numerically on an independent finite-truncation model to machine precision — and the resulting `‖QBQ‖<4.105463` arithmetic is exact. This is a substantive, well-founded improvement (9.740007 → 4.105463), still short of the `2.535946` target, with the constant Hankel term (`<1.570797`) now essentially the whole remaining gap.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-490
parent: v15.438
status: closed
action: none — v15.437's identity and arithmetic independently confirmed, including a fresh numerical check of the operator mechanism. No correction needed.
deliverable: independent analytic and numerical confirmation of the odd-extension joint commutator-Hankel bound ||QBQ||<4.105463, with the constant-Hankel term now the dominant unaddressed obstruction toward 2.535946.
