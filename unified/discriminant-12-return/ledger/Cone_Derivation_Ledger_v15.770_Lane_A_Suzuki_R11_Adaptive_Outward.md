# Cone Derivation Ledger v15.770 — Lane A Suzuki R11 adaptive outward certificate

**Date:** 2026-11-12  
**Lane:** A / original frozen Suzuki seed only  
**Parents:** Lane A v15.768; External Audit Round 551 / ledger v15.769  
**Status:** one exact R11 arc, one streamed signed-\(B^4\) weight update, outward PASS; not \(C_{11}\), not \(C_{16}\)

## Fresh-state and audit acknowledgement

Before this gate, live `master` was read through commit
`fbba90bf62d2126f66661bd5e2cd8d7974241bfc`. External Audit Round 551 / ledger
v15.769 was read in full. It independently replayed v15.768 with no correction
and explicitly authorized the adaptive R11 step. This is the single ACK of that
actionable HANDOFF.

Round 551 landed as v15.769 while the R11 baseline computation was running.
The unpublished local R11 paths were therefore moved to next-free v15.770
before any repository write. No losing-side v15.769 Suzuki path was published.

## Exact R11 branch

The baseline script reconstructs and sorts all exact logarithmic cuts and
proves that \(x=1\) lies strictly in the unique arc with:

- exact cut count: `304175`;
- arc index: `152087`;
- left and right certified margins: `1.3584268433051784e-06` each;
- matrix dimension: `279841`;
- signed sparse \(B\) nonzeros: `10099668`.

The streamed recurrence uses batches of 128 rows and never forms global
\(B^2\) or \(B^4\). Directed-rounding arithmetic and the audited coefficient
perturbation are charged in the final upper bounds.

## Unweighted prerequisite: method failure only

The all-ones-weight replay returned:

- observed maximum row sum of stored signed \(B^4\): `323.9342504553336`;
- outward \(B^4\) upper bound: `323.93425114731684`;
- outward fourth root: `4.24242543249927 > 4.10`;
- certified argmax row: `139971`;
- arithmetic error at the argmax batch: `2.522527982520533e-10`;
- maximum arithmetic error over all batches: `2.522550534189243e-10`;
- coefficient perturbation: `6.913525593247099e-07`;
- peak streamed fills by stage: `[5040, 50054, 217492, 632948]`;
- maximum row lengths by stage: `[40, 403, 1779, 5261]`.

This is strictly an **unweighted-method failure**, not a spectral lower bound.
Runtime was `177.1385054588318` seconds, including `103.09081077575684`
seconds exact ordering and `72.59589529037476` seconds validation; peak RSS was
`1075236` KiB.

## One streamed weight update: outward pass

Starting from the all-ones vector, the second script computes exactly one
row-streamed signed-\(B^4\) absolute-value weight update, normalizes it, freezes
the binary64 vector hash, and independently replays the directed-rounding
weighted row bound. It returned:

- weight SHA-256: `839d9fe77aef5d86b44c92cbfe841f2588a41a2b9d254ba4b5f9b7248af86103`;
- weight condition number: `34.45533848257555`;
- observed maximum weighted ratio: `221.18386246275563`;
- outward weighted \(B^4\) upper bound: `221.18388629249193`;
- outward fourth root: `3.856455915297061 < 4.10` (**PASS**);
- certified argmax row: `139442`;
- arithmetic error at the argmax batch: `2.522527982520531e-10`;
- maximum arithmetic error over all batches: `2.522550534189243e-10`;
- coefficient perturbation: `6.913525593247099e-07`;
- construction and validation peak fills: `[5040, 50054, 217492, 632948]`;
- maximum row lengths by stage: `[40, 403, 1779, 5261]`.

The weighted run took `245.78131008148193` seconds, with
`65.99945974349976` seconds weight construction and `75.83604168891907`
seconds validation; peak RSS was `1073876` KiB. It also formed no global
\(B^2\) or \(B^4\).

## Frozen reproducible witnesses

- `research-notes/lane_a_v15_770_suzuki_r11_exact_arc_unweighted_outward.py`  
  SHA-256 `85d4e82b590914d8d85be71f5533adf45608449033de02a56f54808daf04da94`  
  Git commit: `8dcf5287431e72e227df66260efce845ee6c79e1`
- `research-notes/lane_a_v15_770_suzuki_r11_one_update_outward.py`  
  SHA-256 `a99e41658e9f13ec8c180321b94eef9c979b7792ef97a671ad565324fd62ed3f`  
  Git commit: `529d1ccd133fa5a992c83d331bc66eeae1a522a4`
- `research-notes/lane_a_v15_770_suzuki_r11_adaptive_outward.sha256`  
  Git commit: `a0f431f82f709cae9419b9b24f7285db40a8e491`

## Scope boundary and next gate

This certificate covers **one exact R11 arc only**. It does not prove an
essential supremum over all R11 arcs, \(C_{11}\), \(C_{16}\), the joint
five-frequency cross budget, full-\(K\) transfer, source-native Suzuki \(\Phi\),
or any whole-residual/stationary/capacity/full Suzuki conclusion. It does not
alter any frozen v14.405/406/814 witness, original \(C_{S,32000}\), threshold,
source hash, or exactly-once charge.

**HANDOFF (External Audit / Sandbox):** replay both frozen R11 scripts and the
manifest. Check exact cut ordering, unique arc and margins, streamed signed
products, weight bytes/hash, directed-rounding charges, resource claims, and
scope. If confirmed, the next resource-scaling gate is the same exact adaptive
test at R12; this remains small-radius feasibility work and is not authorization
to infer an all-arcs or R16 result.
