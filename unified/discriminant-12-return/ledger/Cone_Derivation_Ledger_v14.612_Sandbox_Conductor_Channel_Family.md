# Cone Derivation Ledger v14.612 — Sandbox deposit: conductor-channel family of the Suzuki zero-free formula — channel table and dive-flip threshold

**Timestamp:** 2026-10-19 (EDT)
**Lane:** Sandbox (little Euler)
**Parents:** v14.596 (Overlay P closure; its Disposition staged this conductor-family scoping as sandbox-only, "not deposited, awaiting Jeremy's line" — this entry is that deposit, on the line given 2026-10-19), v14.593 (D_exp dictionary closure), v13.258 §3 (Suzuki zero-free formula for χ₁₂), research-notes `suzuki_chi4_zeeman_kernel_compression.py` (the χ₋₄ channel), v14.611 also being live HEAD at allocation (collision-checked immediately before — next-free was v14.612).
**Status:** deposit entry under Jeremy's explicit 2026-10-19 authorization ("Deposit Thread 5 + the channel table, then draft both notes"). Answers **no Lane A HANDOFF**; changes no paper, no staged draft, and no certified object. The run is dated 2026-10-18 and is deposited unchanged. Channel constants and anatomy are **[D]** (closed forms plus root-finds of the ledgered ramp); the per-conductor geometry/dictionary pairing is **[I]**, the same status as the q = 12 overlay.

## The general channel [D, from repo sources]

Suzuki's zero-free formula gives every primitive degree-1 Dirichlet channel the same archimedean ramp shape:

𝒜_χ(t) = (t/2)[ψ(a) + log(q/π)] + (1/4)[ζ(2,a) − e^{−2at}Φ(e^{−2t}, 2, a)],

with q the conductor and **a = 1/4 (χ even) / 3/4 (χ odd)**. The Lerch term is shared by all characters of a parity; the conductor enters only through log(q/π) in the slope. Channel constant C₁(χ) = ψ(a) + log(q/π). Geometry side [I]: diameter-q circle, R = q/2, dictionary edge L = q/(q−1) (Jeremy's (n+1)/n family at n = q−1), envelope Ã_q(t) = R√(1−e^{−2t}), quotient T_χ = 𝒜_χ/Ã_q, dive rate **s(χ) = −C₁(χ)/q**.

## Measured channels (producer `conductors.py`, mpmath, dps 50)

Control q = 12 even reproduces the ledgered values: s = 0.2406063975, t₀ = 1.912049281 (exact 1.912049280865…). ✓

| χ | q | a | C₁(χ) | s(χ) | t₀ | bump (max 𝒜) |
|---|---|---|---|---|---|---|
| χ₅ | 5 | 1/4 | −3.762745507 | 0.7525491014 | 0.9647178 | 0.2030 @ t = 0.373 |
| χ₈ | 8 | 1/4 | −3.292741878 | 0.4115927347 | 1.4049016 | 0.3101 @ 0.548 |
| χ₁₂ | 12 | 1/4 | −2.887276769 | 0.2406063975 | 1.9120493 | 0.4410 @ 0.752 |
| χ₁₃ | 13 | 1/4 | −2.807234062 | 0.2159410817 | 2.0290748 | 0.4720 @ 0.798 |
| χ₂₁ | 21 | 1/4 | −2.327660982 | 0.1108409991 | 2.8795213 | 0.7009 @ 1.123 |
| χ₂₄ | 24 | 1/4 | −2.194129589 | 0.0914220662 | 3.1726013 | 0.7798 @ 1.237 |
| χ₋₃ | 3 | 3/4 | −1.131978477 | 0.377326159 | 0.9185877 | 0.1446 @ 0.315 |
| χ₋₄ | 4 | 3/4 | −0.8442964045 | 0.2110741011 | 1.3685135 | 0.1987 @ 0.447 |
| χ₇ (odd) | 7 | 3/4 | −0.2846806166 | 0.04066865951 | 4.4605622 | 0.3919 @ 1.071 |
| χ₋₈ | 8 | 3/4 | −0.151149224 | 0.01889365299 | 8.4084908 | 0.4749 @ 1.457 |
| χ₁₁ (odd) | 11 | 3/4 | **+0.1673045072** | **−0.01520950065** | — | — |

Every channel with C₁ < 0 has the χ₁₂ anatomy — one bump, one zero, one dive — relaxing as q grows (s falls, t₀ and the bump grow).

## The dive-flip threshold [D]

The dive (and with it the bump, the zero, and the representation problem in its χ₁₂ form) exists iff C₁(χ) < 0, i.e.

q < π·e^{−ψ(a)}: **215.33252 (even), 9.3053617 (odd)**.

Measured consequences: as odd q → 9.3053617⁻, s → 0⁺ and the zero runs off (odd q = 8 is near-critical: t₀ = 8.4084908); at odd q = 11 the constant has flipped sign — s = −0.01520950065, 𝒜 grows positive-linearly, T_χ → +∞ at the centre, and the overlay obstruction reappears mirrored, as a +log pile-up at the centre instead of a −log dive. Even channels keep the χ₁₂ anatomy for every conductor up to 215.33.

## Verification

Independent re-run of `conductors.py` on 2026-10-19 (deposit day; log deposited with the payload) reproduced every table value to all quoted digits, including the q = 12 control and both thresholds. One disclosed diagnostic: the producer's least-squares fit prints C_LERCH(1/4) = 0.35090577901301 against the exact run-2 value 0.35090557984795486267 (a fit artifact at 2×10⁻⁷, flagged in `RESULTS.md`); C_LERCH enters no table value — C₁, s, t₀, and the thresholds are computed directly from ψ, log, ζ(2,a), and Φ.

Deposit: payload `research-notes/payloads/sandbox_conductor_channels_v14_612/` (note `RESULTS.md`, producer `conductors.py`, re-run log `conductors_rerun_2026-10-19.log`; manifest with SHA-256 per file in the payload). Workspace originals in `lane_b/sandbox/runs/20261018-conductor-channels/`.

## Scope flags (honest)

`answers_lane_a_handoff = false`; `papers_modified = false`; `certified_objects_modified = false`; `channel_constants_and_anatomy = D` (closed forms + root-finds of the ledgered ramp); `geometry_dictionary_pairing_per_conductor = I` (same status as the q = 12 overlay); `per_channel_P_constructed = false` (the Overlay P construction is s- and L-covariant, so each channel's P is the same run with new constants — not yet run); `zeta_channel = EXCLUDED_BY_DESIGN` (ζ carries the pole term and its conductor-1 geometry is degenerate: L = q/(q−1) diverges, no circle); `verification_is_proof = false` for the [I] pairing only — the [D] items are closed-form evaluations; `G_derived = false`.

## Disposition

The conductor-channel family staged at v14.596 is now deposited. Standing facts for downstream use: s(χ) = −C₁(χ)/q across eleven channels; the dive exists iff q < π·e^{−ψ(a)} (215.33252 even / 9.3053617 odd); odd q = 11 is past threshold with the obstruction mirrored. Per-channel P constructions remain open sandbox work, unrun.
