# Cone Derivation Ledger v14.327 — Sandbox tail-only Regions 2–3 evaluated action delivered

Sandbox track (our Lane B). Completion of the Regions 2–3 directed
infinite-seed action evaluation opened by v14.290/v14.291 and machined in
v14.292. This entry delivers the evaluated tail witnesses requested by the
sandbox handoffs of v14.306, v14.309, v14.310, v14.312, v14.315, v14.318,
v14.321 and v14.324: actual evaluated rows with directed error charges,
hash-bound, on the exact v14.309 Middle lattice. The evaluated tail is
D·y_tail for the infinite diagonal seed y = Φ/log(n/4), which the v14.298
Near refinement left unchanged — so these witnesses compose directly with
the refined trial's v14.309 compact Middle rows.

## Method (recap; machinery certified in v14.292)

Inputs split at 2a (a = 1024003 even / 1024004 odd; b = 512001 / 512002;
R = 256000). Bank modes [b, 2a): four exact GMP convolutions per output
(the generalized Toeplitz-minus-Hankel channels, kernel audited), with the
diagonal from the certified v14.235 d_n evaluator; the bank was validated
exactly against the v14.291 Region-1 close certificate over the full
256,001-mode close bank (l1, pole moment, max seed/z errors all string-
equal). Tail modes m ≥ 2a: 42 inverse moments per sector obtained by
subtraction from the v14.263 b-start master bank (geometric ratio
(n/2a)² ≤ 0.258 on evaluated rows), with exact remainder bounds from
|y_m| ≤ C_Φ/(m·log(m/4)). Assembly uses
(Dy)_n = (c/2)[z_n·V_n − U_n] + d_n·y_n + σ·2·p_n·P_total, σ = +1 even /
−1 odd, P_total the whole-seed pole moment. Three complete direct-row
checks per stage per sector recompute the bank channels by brute-force
direct summation and match exactly (asserted in code, all true).

## Evaluated results [N-cert]

Region 2 — all 256,000 same-parity rows b ≤ n ≤ 4R per sector, point
buffer in Lane A's v14.309 format (256,000 signed 30-byte integers at 256
fractional bits, 7,680,000 bytes), ready for one-time composition:

| Sector | ℓ² error upper | Action point ℓ² norm | Max row charge | Buffer SHA256 |
|---|---:|---:|---:|---|
| even-v | 6.690496712075973e-15 | 7.601760895379098e-4 | 1.3223255180017402e-17 | 01049b9491c91ff49a640964cb878da6fdcacd08542eddc5d345944cb8edf390 |
| odd-v | 6.64847658308963e-15 | 7.594412811841635e-4 | 1.3140205608035586e-17 | e0dfb52f4255d8f13a1f312b6ae772d6e57d077810d620e4e4bd44eab21621a9 |

Region 3 window — 8,192 same-parity rows from 4R per sector (245,760-byte
buffers, same format):

| Sector | ℓ² error upper | Action point ℓ² norm | Max row charge | Buffer SHA256 |
|---|---:|---:|---:|---|
| even-v | 1.3877527063693985e-16 | 9.468972907411883e-5 | 1.5332646082559147e-18 | 4705c6a0cf10b35d3050ba21c4a347ebe0c7ba393734225112da7eeafec992d2 |
| odd-v | 1.3872495730166127e-16 | 9.46137635771606e-5 | 1.532708719184671e-18 | 29f39fd719d45690fb5240d0dc31e4c3241a482591a715501e04dbfbd1c1bfc7 |

Whole-seed pole moment used in both assemblies (consistent across
stages): P_total = 1.23994e-7 ± 1.41e-43 (even), 5.72467e-8 ± 6.46e-44
(odd), displayed rounded; exact rationals in the certificates.
Subtraction tail-moment files SHA256: even
57751bb72cac7d61ee10f8e67209baf431b38f9e6ffaadf20c90cf49d4777e5d, odd
ce8a5e182029490648a3acac5773fb19c70ccdd1686b51ceb2f84183bc6476f0.
Evaluator: sandbox `sandbox_region23_evaluator.py`, SHA256
2492b1b8dade5ee290153c9c59db80b6d58f3cf4fa3911994bfd22c89eb03727,
built on Lane A's unmodified module stack; pinned inputs: v14.223
whole-source affine payload (SHA256
6c2b8d1d76eca772c625042566d9af62d487808795d1479ee7de7e2735bad3d6),
v14.263 infinite-RHS moments, v14.276 later-start moments, v14.291
close-action certificates.

Region 3 beyond the window: the v14.292 certified envelope stands —
|(Dy)_n| ≤ (A + B·log(n/b))/n for all n > 4R with A = 41.03346435029798,
B = 0.9246976885779616 (even); A = 40.995010915797, B = 0.9238311387052199
(odd); action ℓ² tail beyond the window end (n > 1040384 / 1040386) ≤
0.0314715844867336 / 0.031442090487128475.

## Scope — read before composing

These are evaluated ACTION values of the tail component only, with
directed charges; they are not a residual and not an acceptance bound.
The remaining-residual composition (v14.309 compact Middle + this tail
action − bare g, tested against the v14.310 permissible budgets
B ≈ 2.5715637086692463e-5 even / 2.5732543884387367e-5 odd with global
transport T reserved once) is the joint next step and has not been
performed here. Specifically: the Region-3 envelope above bounds the
ACTION pointwise; it is not a cancellation-aware ℓ² bound on the
beyond-window RESIDUAL (g − action), and if the composition requires
that stronger statement it remains the one named open piece on the
sandbox side. The action point norms (≈7.6e-4 Region 2, ≈9.5e-5 Region 3
window) must not be compared directly against the residual budget —
cancellation with the compact action and g is the composition's content.
whole_infinite_action_evaluated remains componentwise (Region 1 Lane A,
Regions 2–3 here); stationary_acceptance_met = False;
infinite_capacity_tail_closed = False. The v14.297 rejection of the
original unrefined trial stands untouched.

## HANDOFF-ACK

To v14.306 / v14.309 / v14.310 / v14.312 / v14.315 / v14.318 / v14.321 /
v14.324 (sandbox): the tail-only Region-2 buffers on the exact v14.309
lattice and the Region-3 evaluation/remainder certificates are delivered
above with hashes, lengths, schemas and directed charges. The
tail-witness blocker is answered; the composition gate can proceed on
Lane A's side.

## Publication restriction (recorded explicitly)

Buffers and certificates are held in the sandbox workspace
(`~/workspace/d12/region23_work/`), hash-bound by this entry; they are
NOT committed to `research-notes/`. Sandbox code/output publication to
the repository remains restricted pending Jeremy's explicit approval, as
recorded in v14.308. If Lane A requires the buffer bytes inside the
repository, that transfer needs Jeremy's line; the hashes above fix the
bytes unambiguously in the meantime.
