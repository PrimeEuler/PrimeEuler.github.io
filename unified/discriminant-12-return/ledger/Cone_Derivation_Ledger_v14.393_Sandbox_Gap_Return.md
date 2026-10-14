# Cone Derivation Ledger v14.393 — Sandbox Track (Little Euler)

## Sandbox HANDOFF-ACK v14.351: Original-Seed-Only Gap Action Delivered — 520,191 Rows per Sector, Complete ℓ² Error ≤ 1.05e-15

**Track:** Sandbox (our Lane B). **Closes:** the v14.351 HANDOFF (original-infinite-seed-only gap action), re-issued in v14.371, v14.377, v14.380, v14.383, v14.387, v14.391. **Status:** [D] for every number below (interval/Fraction arithmetic throughout; the two displayed floats are display-only renderings of exact rationals carried in the certificates). **Scope:** this entry delivers the gap witness only. No whole-residual composition is performed or claimed by the sandbox; no signed-stationary or infinite-capacity claim is made (the certificates carry `whole_infinite_action_evaluated: false`, `stationary_acceptance_met: false`, `infinite_capacity_tail_closed: false`).

---

## 1. What was asked (v14.351)

Evaluate the **unchanged original infinite-seed-only** operator action $D\cdot y$ on every gap output row

- even-$v$: $n = 1040385, 1040387, \dots, 2080765$ (520,191 rows),
- odd-$v$: $n = 1040386, 1040388, \dots, 2080766$ (520,191 rows),

with the original v14.250 seed $\Phi/\log$ and the whole-affine normalization **unchanged**; no source/front/lift/refined-Near/finite-patch content of any kind; both physical denominators, the $q=4$ weight and the full pole carried; input bank $[b, T)$ with $T = 4161531$ (even) / $4161532$ (odd); self rows inside the finite input bank excluded from the offdiagonal channels using the same represented reciprocal before the raw diagonal is added; bank/tail split with actual endpoint ratio $\le 1/4$ at the final output row; errors propagated once, target total gap $\ell^2$ error $\le 10^{-12}$ preferred.

## 2. Result

| quantity | even-$v$ | odd-$v$ |
|---|---|---|
| output rows | 520,191 (1040385..2080765) | 520,191 (1040386..2080766) |
| bank modes | 1,824,765 (512001..4161529) | 1,824,765 (512002..4161530) |
| tail start $T$ | 4161531 | 4161532 |
| point $\ell^2$ norm | $5.257719274011153\times10^{-4}$ | $5.252822387758140\times10^{-4}$ |
| **complete $\ell^2$ error upper** | $\mathbf{1.0411227284039428\times10^{-15}}$ | $\mathbf{1.0355019296444129\times10^{-15}}$ |
| $P_{\mathrm{total}}$ point | $1.2399406586564998\times10^{-7}$ | $5.724665194922397\times10^{-8}$ |
| max row charge | $1.4435123720908809\times10^{-18}$ | $1.4357191577761255\times10^{-18}$ |
| endpoint ratio at final output | $4329582985225/17318340263961 \approx 0.2499998798519247$ | exactly $1/4$ |
| buffer | 15,605,730 B = 520,191 × 30 B, dyadic $\lfloor\cdot\,2^{256}\rfloor$ signed LE | same |
| buffer SHA-256 | `00c1651f1013f821d3135f136bb91a9196792ff9663b4762d7d80a42dbc66af6` | `675138c2ff20728945989bd14aa8c1a004a54229847a9664de4992a0d972c413` |
| from-definition direct checks | 3/3 pass (rows 0, 260095, 520190; all bank input terms match, $m\ne n$) | 3/3 pass |
| self rows excluded | yes, all 520,191 rows, represented reciprocal | yes |

The error uppers beat the handoff's $10^{-12}$ preference by three orders of magnitude. Max absolute row value is $\approx 1.27\times10^{-6}$ in both sectors (no outlier rows).

## 3. Self-found defect, disclosed in full (first assembly invalid; nothing defective was delivered)

The first even-sector assembly (2026-10-14, local only) produced a certificate whose own headline numbers failed sanity: point $\ell^2 \approx 192{,}990.7$ and error upper $\approx 6.9\times10^{8}$. Decoding the buffer localized the failure: early rows were correct ($\approx 10^{-6}$) but values grew with $n$, reaching $-1435.3$ at the last row. **No defective artifact was delivered, frozen, or ledgered**; the outputs were quarantined locally and the pipeline halted before the odd assembly finished.

**Root cause.** The tail beyond $T$ is evaluated as a 42-term moment series whose moments are obtained by subtracting the finite-bank sums from the v14.263 $b$-start master bank. That subtraction carries an absolute noise floor ($\sim 10^{-514}$ in $V$-units): from $j = 20$ onward the stored midpoint is dominated by construction noise (the interval radius meets or exceeds the midpoint from $j = 20$; the moment is informative only for $j \le 19$). The old assembly evaluated all 42 midpoints as point values; the $j$-th noise term is amplified by $n^{2j}$, so at the largest rows the $j = 41$ noise completely swamps the true $\sim 10^{-6}$ action. The certificate's error accounting was honest throughout — the $6.9\times10^{8}$ upper is exactly the radius sum reporting that the high-$j$ moments carried no information.

**Fix.** The point series is truncated at the last informative term, chosen per sector by the recorded criterion (retain $j$ while $\mathrm{rad}_j \le |\mathrm{mid}_j|$ and $n_{\max}^{2j}\,\mathrm{rad}_j \le 10^{-13}$): $J^\* = 19$ in both sectors (the criterion counts $V$ informative for 20 terms and $U$ for 19, so the series uses $j = 0..18$ for both channels; certificates record `tail_series_terms_used: 19`, `tail_series_moments_computed: 42`). The omitted series remainder is bounded geometrically, $\mathrm{Rem}_V = 2 S_1 r^{J^\*}/(1-r)$, $\mathrm{Rem}_U = 16 n S_2 r^{J^\*}/(1-r)$ with $r = n^2/T^2$, using the same $S_1/S_2$ envelopes as the previous $r^{42}$ form (valid at any truncation point, since $T^{2J} M_J \le \sum_{m>T}|y_m|/m^2$ for every $J$). The retained terms alone pin the tail to $\sim 10^{-22}$ at the largest row; the bounded remainder is $\sim 10^{-18}$.

**Validation of the fix.** (i) The truncated evaluation reproduces the first assembly's *valid* rows exactly — row 0 is unchanged, $8.997141784726933\times10^{-7}$. (ii) Independent brute-force spot checks (float bank sums from the bank files + the truncated tail in exact Fractions) agree with the delivered buffer at $n = 1840385$ ($5.908847533376626\times10^{-7}$) and at the last row $n = 2080765$ ($5.655937399458163\times10^{-7}$). (iii) The bank, the chunked channel convolutions, the self-row exclusion, and the direct checks were verified independently of the tail and were never implicated.

**Note for the auditor.** The Region 2–3 tail evaluator (v14.327) uses the same master-subtraction moment construction and the same all-42-terms evaluation. The flaw is latent there and numerically invisible: its output rows satisfy $n \le 1.28\times10^{6}$, so the amplifying factor $n^{82}$ is $\sim 4\times10^{17}$ times smaller and the noise contribution sits at $\sim 10^{-14}$, far below that certificate's scale. The v14.327 results and verdicts are unaffected; the sandbox states this so the parallel does not have to be re-derived.

## 4. Method notes

- Bank/tail split at $T = 4161531/4161532$ with merged-bank contiguity asserted (first mode $b$, last mode $T-2$, step 2, 1,824,765 modes). Tail moments at $T$: 42 moments per channel by master-minus-bank subtraction (see §3 for the informativeness limit).
- Channels computed by exact integer convolution over bank segments of 400,000 modes (integer-identical to the single full-bank call; the segmentation exists because the full-bank workspace was OOM-killed twice on this host). Self-exclusion per row: subtract $g_k\, z_n y_n$ from the $U$ channel integer and add $g_k\, y_n$ to the $V$ channel integer, $g_k = \lfloor 1/(2n) \rfloor_{256}$, the same represented reciprocal the channels use.
- Errors are propagated once into a single per-row charge; the complete $\ell^2$ error upper is $\sqrt{\text{rows}}\times$ max row charge, as in the certificates.

## 5. Payload

Frozen at `research-notes/payloads/sandbox_seed_gap_action_v14_351/` (58 files): both action buffers as base64 parts (27 parts per sector, 800,000 B parts; reassembly: concatenate `.b64.partNNN` in numeric order and base64-decode), both certificates (`gap-action-even-v.json`, `gap-action-odd-v.json`), the as-run producer (`sandbox_gap_evaluator.py`, including the §3 truncation), and `manifest.json` binding every buffer hash. Post-push, the payload was re-downloaded from the repository and reassembled fresh: both buffers reproduce the certificate SHA-256 values in §2 exactly.

## 6. Handoff status

The v14.351 HANDOFF is **CLOSED** by this return. The sandbox's gap witness for the whole-residual composition — the original-seed gap action Lane A has been blocked on since v14.356/v14.371 — now exists in the repository with hash-bound buffers and directed remainder certificates. Composition itself is Lane A's next step; the sandbox claims nothing about its outcome.
