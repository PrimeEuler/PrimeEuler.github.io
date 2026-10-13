# Cone Derivation Ledger v14.331 — Sandbox correction: the "≤ 0.258" prose bound was false; the evaluator used exact rowwise ratios, so no charges or buffers change

Sandbox track (our Lane B). Response to the v14.330 correction request
(Lane A), which is ACCEPTED and verified. HANDOFF-ACK to v14.330's
correction-and-frozen-byte-transfer handoff, correction half.

## The error, conceded plainly

v14.292 §2 and v14.327 stated that the geometric ratio satisfies
(n/2a)² ≤ 0.258 on evaluated rows. That inequality is FALSE at the top
of the Region-3 window. Exact values (recomputed by the sandbox and
agreeing with v14.330):

- Last evaluated Region-3 row: even n = 1040383,
  (n/2048006)² = 1082396786689/4194328576036 = 0.2580619918222901...;
  odd n = 1040384, (n/2048008)² = 0.2580619838868132....
- Window-end endpoints used by v14.330's required check: even
  n = 1040384, ratio = 0.25806248791289493...; odd n = 1040386,
  ratio = 0.25806297606751544....

All exceed 0.258. Region-2 rows are unaffected by the error (there
(n/2a)² ≤ 0.2499980468845367 even / 0.24999804688644403 odd). v14.329
§2(c)'s "match" verdict inherited the false prose bound; the sandbox
prose in v14.292/v14.327 is the origin of the error and is corrected by
this entry. A safe simple bound covering every evaluated row and both
endpoints is (n/2a)² < 0.258063 (v14.330's bound).

## What the evaluator actually used [N-cert]

The constant 0.258 was never used in any computation. It appeared only
in the evaluator's module docstring and in the two ledger entries'
prose. The 42-moment tail remainder in the assembly
(`sandbox_region23_evaluator.py`, as-run SHA256
2492b1b8dade5ee290153c9c59db80b6d58f3cf4fa3911994bfd22c89eb03727)
computes, for every evaluated row n, the EXACT rational ratio and the
exact geometric tail:

    r   = F(n*n, A2*A2)              # exact Fraction, per row
    r42 = r**42 / (1 - r)            # exact tail sum_{j>=42} r^j
    RemV = 2 * S1 * r42
    RemU = 16 * n * S2 * r42

with A2 = 2a and S1, S2 the certified spacing-2 tail sums of
|y_m|/m and |y_m|/m² under |y_m| ≤ C_Φ/(m·log(m/4)). No rounded ratio
enters anywhere: the subtraction tail moments carry their radii from
the v14.263 master intervals plus bank error terms, and the Region-3
envelope stage uses no geometric ratio at all. Because the per-row r
is exact, it automatically covers Lane A's required endpoint maxima
(0.25806248791289493... even / 0.25806297606751544... odd) — each row's
remainder was charged with that row's own true ratio, which is at most
the evaluated-row maxima stated above.

Consequence: NO directed charge, certificate, or buffer byte changes.
All v14.327 hashes, lengths, norms and charges stand exactly as frozen;
nothing is superseded. The as-run evaluator file is preserved unedited
(including its docstring) so its recorded SHA256 continues to identify
the exact code that produced the frozen buffers; this entry supersedes
the docstring's inequality as prose. The action certificates carry the
resulting charges (max_row_charge, complete_l2_error_upper); they carry
no separate ratio field, so this entry is the exact ratio record Lane A
requested.

## Remaining open half of the v14.330 handoff

The frozen-byte transfer (v14.328 handoff) is unchanged by this
correction: the four v14.327 buffers and certificates still sit only in
the sandbox workspace, and placing them in a repository payload
namespace remains pending Jeremy's explicit approval (sandbox
code/output publication restriction, recorded in v14.308/v14.327). On
his approval the transfer will preserve the exact v14.327 hashes —
no regeneration — and will be fetch-back verified before being
ledgered.
