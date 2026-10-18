# Cone Derivation Ledger v14.583 — Sandbox: Direct-Middle Residual Composition Return — v14.448 GATE PASSES with the Changed Compact Action

Track: sandbox (Lane B exploratory/execution sandbox under little Euler).
Responds to: v14.554 HANDOFF (Lane A, target sandbox + external audit,
type exact-direct-middle-residual-composition, status OPEN at issue).
Status of that HANDOFF after this entry: CLOSED — the composition is
returned below with a certified PASS in both sectors.

## Verdict

**The v14.448 direct-middle execution gate PASSES in both sectors**
under the changed compact action. Composing, per row at S = 2^256 with
the audited v14.488 conventions,

    residual_i = S // (first + 2i − shift) − changed_compact_i − seed_i

(bare source 1/n even, 1/(n−1) odd; first = 2080767 even / 2080768 odd;
shift = 0 even / 1 odd; 1,040,383 rows per sector), the exact directed
physical residual uppers are:

| sector | point norm upper | complete physical upper | frozen v14.444 allowance a | ratio |
|---|---|---|---|---|
| even-v | 4.814585391685285e-06 | 4.814585591228017e-06 | 2.2251541105255456e-05 | 0.2164 |
| odd-v | 4.805785414647985e-06 | 4.805785613119684e-06 | 2.228757296675468e-05 | 0.2156 |

Both physical uppers sit at ≈21.6% of the frozen allowances implied by
the unchanged 3e-5 finite-plus-gap threshold (≈4.6× inside). The far
headroom squared q − physical_hi² is positive in both sectors
(headroom ≈ 2.172442973114859e-05 even / 2.176327947229337e-05 odd), so
unlike v14.488 the far block is NOT moot: the handoff's pass_next —
Lane A derives fresh far moments/splits and the beyond-middle summable
certification — is the live next step. No far quantity is evaluated or
claimed here.

For scale: the v14.488 composition with the old compact action failed
at 5.0578e-05 even / 5.0485e-05 odd (≈2.27× OVER allowance). The δ_DM
repair chain (v14.500 candidate → v14.539 complete RHS → v14.543 fresh
lifts → v14.552 changed compact action) reduced the direct-middle
residual by ≈10.5×.

## Error budget (exact rationals; floats shown)

Per the v14.554 contract the budget contains ONLY the new
compact-action error, the frozen v14.486 seed error, and the
bare-source floor error:

| sector | compact (v14.552) | seed (v14.486) | bare floor upper(COUNT)/S | complete physical error upper |
|---|---|---|---|---|
| even-v | 9.252926241952067e-18 | 1.995334793914987e-13 | 8.808819957831051e-75 | 1.9954273231774067e-13 |
| odd-v | 9.231899594035513e-18 | 1.9846246697473864e-13 | 8.808819957831051e-75 | 1.9847169887433268e-13 |

The three terms sum exactly to the complete physical error upper in
each sector (verified). The budget is dominated by the frozen seed
term, ~8 orders below the allowances; the verdict turns on the point
norm, as forecast.

## Inputs (all four hash-asserted in the producer before composing)

- Changed compact action (v14.552, repository payload
  payloads/direct_middle_changed_compact_action_v14_552/):
  even SHA-256 807a4c6e89ab0ff89ce7687a617c01a6c37e83f7ee75b94b189d1a9128c4faec,
  odd SHA-256 1788550cb29227a74a0ba9a0561d73b932886e21ff5c1070f368df3db7e8e7a1.
- Original v14.486 seed action (frozen lineage; buffers sandbox-resident
  at the hashes frozen in v14.486):
  even SHA-256 c29411b698b69dbec9a8d7827c8baddc751db6e01d6df46433d744d9064d3cd1,
  odd SHA-256 f4f8a6e576bbc3351d9681073dc06e7012e377294a06a4f9fe37c018a7f5ea2c.
- Budget: the frozen v14.442 certificates (global source +
  v14.403-transport charge t and finite-plus-gap physical upper p_hi),
  q = (3/100000 − t)² − p_hi², allowance a with a² ≤ q read from the
  same certificates (v14.444 values).

## Outputs (retained sandbox-side; hashes frozen here)

Residual buffers (width 30 signed LE, 1,040,383 rows, 31,211,490 B):

- even-v SHA-256 8c6d880c40fc9a3fd4fb0d8da76e737b86457e1ff71e3bd092552e73eb4e0c36
- odd-v SHA-256 5606cc01d675aec1920c2cb887bcf5d3d2b1df20bd1a655cbee0fa51dd245316

Certificates (schema cone.direct-middle-residual-composition.v1,
exact rational fields for every quantity above):

- even-v file SHA-256 96bc942e1119a4dc24d5a8c03ae25138e14bae34c0a62d5f3f8acbaf5a3661dc
- odd-v file SHA-256 0648b71e80a73f49c0b8234d216cfe11fe1a0c4aaefe0a10addbf49fe8dce2b8

Post-run independent verification (sandbox): each residual buffer was
re-hashed against its certificate, and the ℓ² norm was re-derived from
the raw buffer bytes independently of the producer; the exact sum of
squares lies inside the certified directed bracket
[point_lo², point_hi²] in both sectors.

## Charge accounting and scope fences

- No second v14.354 charge; no repeated global source +
  v14.403-transport charge (global_transport_charged_again = false in
  both certificates). C_S_32000 and every threshold preserved.
- The old 912,383-row v14.406 consumer was not used.
- beyond_middle_far_evaluated = false; whole_residual_acceptance_certified
  = false. This PASS is scoped to the direct-middle block against the
  frozen v14.444 budget. It certifies nothing about the far block, the
  whole represented residual, a signed stationary pair, or
  infinite-capacity closure.
- Producer: the audited v14.488 composition script with exactly three
  changes (v14.552 compact buffer + pins; compact error taken as the
  single v14.552 sector-certificate rational; outputs to a fresh
  directory, v14.488 evidence untouched). Norm/upper directed-sqrt,
  bare-source formula, and budget derivation are byte-identical to the
  v14.488 producer. Run 2026-10-18 on Jeremy's explicit go.

## For the audit

Inputs, signs, directed errors, and charge-once accounting are all
frozen above for independent checking. The residual buffers and
certificates are retained sandbox-side at the stated hashes; the
v14.486 seed buffers are being transferred to the repository under a
separate record so the seed side of this composition becomes
byte-replayable from the repo as well.
