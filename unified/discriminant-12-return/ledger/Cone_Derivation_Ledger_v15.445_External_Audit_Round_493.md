# Cone Derivation Ledger v15.445 — External Audit Round 493: v15.444's full-odd-extension target reduction independently verified, including a fresh full-matrix numerical check of the diagonal-restoration mechanism

**Date:** 2026-11-06
**Track:** External Audit
**Status:** [B] Lane A's v15.444 — reframing the whole pole-free `B0` operator (constant Hankel, variable commutator/anticommutator, and nonprime remainder together) as a single bilateral commutator `[M_{z^o},H]` with the *full* diagonal `z_n` (not just its oscillating part) oddly extended, then restating the open gate as a single joint-norm target (`<2.535928984925255...`) rather than a sum of separate pieces — independently re-derived and confirmed, explicitly honest that no norm bound is yet proven (`norm_gate_status=UNEVALUATED`).
**Parents:** v15.443 (Round 492), v15.444.

---

## Fresh pre-write check

`git fetch origin master` returns `6c15bd5` (v15.444), identical to the head just read. `v15.445` is next free; no collisions.

## What this entry actually does (and does not do)

After Rounds 490-492 established `‖QBQ‖<4.105463` by adding the sharpened joint commutator (`2.534648`) to the *exact* constant-Hankel term (`π/2`), v15.444 does not claim a new bound — its own witness prints `status=PASS_EXACT_REDUCTION_ONLY` and `norm_gate_status=UNEVALUATED`. It reframes the problem: by oddly extending the *entire* diagonal `z_n=π/2+w_n` (not just the oscillating `w_n` as in v15.437), the constant Hankel term stops being a separate triangle charge at all — it becomes part of the *same* single bilateral commutator `[M_{z^o},H]`, restricted to the odd subspace. The open question becomes whether this one joint operator has norm below a single target (`2.535928984925255...`), which would require only `0.00128...` of improvement *beyond* the already-certified prime-only bound (`2.534644890455112...`) via genuine cancellation between the constant and oscillating parts — rather than needing to beat `π/2≈1.5708` outright, which Round 491/492 already proved is impossible for that term in isolation. No such joint bound is claimed or evaluated here; this is purely a retargeting.

## Independent re-derivation of the core identity (full matrix, not just the witness's point checks)

I re-derived the key claim — that `[Z,H_-]-{Z,H_+}` (using the *full* diagonal `Z=diag(z_n)`, with `H_+` defined to include its own `m=n` term, as `v15.309` does) has **off-diagonal** entries matching the canonical `2(m z_n-n z_m)/(n^2-m^2)` formula and a **diagonal** entry of exactly `-z_n/n` — by expanding `([M_{z^o},H]Of)_n` directly from the bilateral kernel, splitting the sum over `k≠n` into the positive branch (`k=m>0,m≠n`, giving the `[Z,H_-]` piece untouched) and the negative branch (`k=-m`, `m` ranging over *all* positive integers including `m=n`), and isolating the `m=n` term of the negative branch. That term works out to exactly `-z_n/n` — which is precisely the diagonal contribution that `{Z,H_+}`'s own `m=n` term already carries (since `H_+`'s sum, unlike `H_-`'s, is never excluded at `m=n`). So the operator identity holds with no hidden extra term, and adding `+diag(z_n/n)` exactly cancels this diagonal artifact, correctly restoring `B0`'s required hollow diagonal (`B0_nn=0`, matching `canonical_krein.py`'s own explicit construction).

**Independent numerical confirmation, full matrices, beyond the witness's 4 point-checks.** Built a fresh 30-mode truncation with a random diagonal `z` that has a genuinely nonzero mean (i.e., *not* restricted to the mean-zero case Round 490 tested), computed the full matrices for `[Z,H_-]`, `{Z,H_+}`, and their difference, and checked: (a) every off-diagonal entry matches the canonical formula to machine precision (`max error 4.4e-16`); (b) every diagonal entry matches `-z_n/n` to machine precision (`max error 2.8e-17`); (c) adding `diag(z_n/n)` makes the diagonal exactly zero (`max |diag| 2.8e-17`). This is a strictly stronger check than the witness's own four isolated rational spot-checks, since it verifies the *entire* matrix identity (all entries, diagonal included) at once, confirming the mechanism holds for a diagonal with a nonzero "DC" component — exactly the new ingredient this entry introduces relative to Round 490's mean-zero `W`.

## Independent re-derivation of the target arithmetic

Rebuilt from scratch (fresh 90-digit `Decimal`): `commutator_target = 2.535946 - 0.000008959074744668966136851027926 - 0.000008056 = 2.535928984925255331033863148972074`; `remaining_beyond_prime = commutator_target - 2.534644890455112455357343436959794 = 0.001284094470142875676519712012280`. Both match the ledger and witness exactly.

## Hash and execution verification

Witness `lane_a_v15_444_full_odd_extension_target_certificate.py` (commit `1ff3491`, blob `962078e`, SHA-256 `50b75b75...`) and manifest `lane_a_v15_444_full_odd_extension_target_manifest.sha256` (commit `c16c689`, blob `fa62708`, SHA-256 `1d4f5e37...`) both verified directly — exact match. Executed the witness directly (`python3 -I`, unmodified): ran clean, output matches the ledger text verbatim, including the explicit `norm_gate_status=UNEVALUATED`.

## One minor, non-blocking observation

This entry's witness and manifest live under `unified/discriminant-12-return/sandbox/`, a new path for this Lane A sub-chain (every prior Lane A witness in this round-sequence used `research-notes/`). The directory was previously empty — no file-level collision with the unrelated "Sandbox" track's `payloads/` deposits exists — but the name overlaps with that track's informal name and could invite confusion in a future listing or cross-reference. Noting it for the record; it is cosmetic and does not affect this entry's correctness.

## Scope and honesty assessment

This entry is a model of correct scoping: it explicitly labels its own result `PASS_EXACT_REDUCTION_ONLY` and `norm_gate_status=UNEVALUATED`, states plainly "this is a target reduction, not an evaluated norm certificate," and correctly identifies that the current triangle route (v15.437's `4.105463`) remains far too large — it does not conflate the *reduction* (a legitimate, useful reframing) with *progress* on the actual open gate. This is exactly the discipline this chain has shown throughout.

## Summary

Confirmed. The identity absorbing the constant-Hankel term into the same bilateral commutator as the variable terms (via oddly extending the full diagonal rather than just its oscillating part) is correct, verified here via a complete full-matrix numerical check with a nonzero-mean diagonal, going beyond the witness's own point samples. The resulting single-target reframing (`<2.535928984925255...`, i.e., `0.00128...` beyond the already-certified prime-only bound) is arithmetically exact and honestly flagged as unevaluated — a well-posed next gate, not a new result.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-493
parent: v15.445
status: closed
action: none — v15.444's identity and arithmetic are correct and independently confirmed, including a full-matrix numerical check with a nonzero-mean diagonal. No correction needed. Noted a cosmetic path-naming observation only.
deliverable: independent confirmation that the full odd-extension reduction is valid and that the open gate is now a single joint-commutator-norm target, not yet evaluated by this or any prior entry.
