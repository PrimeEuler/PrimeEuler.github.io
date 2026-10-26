# Certificate — v14.909 counter-term construction gate return

**Verdict: CONSTRUCTION EXISTS** (DERIVATION.md §2–§4), under
one declared non-derived element — the output-support clause
(DERIVATION.md §7, flagged [O] for Lane A / audit). If that
element is rejected, DERIVATION.md §8 is the exact obstruction
and the return converts to the gate's failure branch with no
change to any number below. No production run was performed; no
F1/F2 composition is claimed; nothing is ledgered by this
package (main-chat review first, per plan).

## The construction in one paragraph

Phantom inputs on the seed's own lattice (m ≥ b, sector parity):
ŷ^ph = −ŷ_seed + y_1·1[m = m_1], m_1 = b, y_1 = δ/κ an exact
Fraction (δ = 1 − c_inf − W_0; κ = −c·z_{m_1} + 2σL·p_{m_1} from
the certified z enclosure and the exact 2²⁵⁶ p floor). Action:
the (zV − U) channel sums plus the family's own pole term, no
diagonal term, identically zero on rows N < F0. Coefficients:
drift +W_0/2 = β [exact identity]; constant −(K − W_0) + δ = A
[exact identity]; 1/ln coefficient D = −γ up to the audited
E_diag block-mean slack |γ_E| ≤ 2e-4. Remainder: block-mean
envelope 15/ln N + C_sp/N + 2e-4 (DERIVATION §6).

## Witness numbers

Constants (constants.json; exact Fractions where the framework
has them, pinned fits re-derived from the frozen blocks and
asserted against the recorded v14.901 values to 1e-12):

| quantity | even | odd |
|---|---|---|
| W_0 | 1.1327596301371365 (exact) | 1.131709878205129 (exact) |
| c_inf | −0.18426887511732248 (exact) | −0.18300198492192950 (exact) |
| K (pinned fit) | 2.5527139612295247 | 2.5522359590515484 |
| γ (pinned fit) | −0.35474258710667983 | −0.38075887760049554 |
| A = 1 − c_inf − K | −1.368445086112202 | −1.369233974129619 |
| β = W_0/2 | 0.5663798150685683 | 0.5658549391025645 |
| D = −γ | +0.354742587106680 | +0.380758877600500 |
| δ = 1 − c_inf − W_0 | 0.0515092449801860 | 0.0512921067168005 |
| m_1, z_{m_1} | 512001, 1.006692 | 512002, 1.511710 |
| κ, y_1 | −0.640872, −0.0803736544 | −0.962386, −0.0532967985 |

Block anchors (anchors.json `blocks`; 257-row block means of
N·CT(N) vs the block-averaged template; envelope = §6 block-mean
envelope):

| center | phantom (even) | template | dev | phantom (odd) | template | dev |
|---|---|---|---|---|---|---|
| 6,161,535/6 | 0.151440 | 0.158881 | −0.007441 | 0.153735 | 0.158362 | −0.004627 |
| 12,000,001/2 | 0.179274 | 0.183851 | −0.004577 | 0.179263 | 0.183240 | −0.003977 |
| 25,000,001/2 | 0.207254 | 0.210122 | −0.002868 | 0.206894 | 0.209417 | −0.002522 |
| 50,000,001/2 | 0.231824 | 0.233856 | −0.002033 | 0.232199 | 0.233069 | −0.000870 |
| 1e8 | 0.256064 | 0.256632 | −0.000568 | 0.255608 | 0.255767 | −0.000159 |
| 2e8 | 0.279302 | 0.278524 | +0.000778 | 0.278152 | 0.277587 | +0.000565 |

All twelve inside the envelope (0.79–0.99); deviations decay
faster than 1/ln N, consistent with the o(1/ln N) remainder.
The dominant deviation source at the first centers is the
spike's exactly-evaluated O(1/N) V-term (block mean −0.006768
at the first even center, ∝ 1/N), which is part of the phantom
value, not an error.

DM silence (anchors.json `dm_silence`): support-clause
self-test passes in both sectors — representative region-1/DM
rows (512001/512002, 2080767/2080768, 3000001/3000002,
4161531/4161532) return exact 0 and the channel branch is never
entered. [By declaration + code path; see DERIVATION §5/§7.]

l2 (anchors.json `l2`): template partial sums Σ_{F0≤N≤2e8, step2}
CT⁰(N)² = 3.8241e-9 (even) / 3.7988e-9 (odd), norms 6.184e-5 /
6.163e-5; phantom partial sums bounded by 3.854e-7 / 3.804e-7
(2× template + 2× envelope-remainder sums). The far half-line
sums converge (Λ(N)/N class).

Band separation (anchors_bands_even-v.json /
anchors_bands_odd-v.json; center-row pointwise N·CT(N)
channel attribution, spike wholly in below):

| center | below (even) | near | above | pole | total | below (odd) | near | above | pole | total |
|---|---|---|---|---|---|---|---|---|---|---|
| 6,161,535/6 | 0.095137 | 0.011812 | 0.034521 | −1.003e-06 | 0.141469 | 0.158981 | 0.041274 | −0.038636 | +1.676e-07 | 0.161620 |
| 12,000,001/2 | 0.125313 | 0.082605 | 0.033134 | −1.003e-06 | 0.241052 | 0.144311 | −0.064518 | 0.011788 | +1.676e-07 | 0.091581 |
| 25,000,001/2 | 0.142860 | 0.035560 | 0.047657 | −1.003e-06 | 0.226076 | 0.146070 | −0.042808 | 0.044741 | +1.676e-07 | 0.148002 |
| 50,000,001/2 | 0.184856 | −0.023437 | 0.028874 | −1.003e-06 | 0.190293 | 0.199384 | 0.036533 | 0.010972 | +1.676e-07 | 0.246889 |
| 100,000,001/2 | 0.188029 | 0.015427 | 0.055874 | −1.003e-06 | 0.259328 | 0.285253 | 0.006593 | −0.065176 | +1.676e-07 | 0.226669 |
| 200,000,001/2 | 0.247372 | 0.078305 | 0.011871 | −1.003e-06 | 0.337547 | 0.229868 | −0.041854 | 0.033367 | +1.676e-07 | 0.221380 |
Pointwise band values carry the z_N/Hilbert oscillation (the
near band is pointwise O(1) at a single row and cancels in
block means by the pairing argument); the coefficient-grade
statements are the block anchors above. The Λ growth across
centers is carried by the below band, as §1 requires.

Pure-affine variant (DERIVATION §9; z3.json, stage S4;
direct lattice summation to m ≤ 4·10^7, Z₃ tail bound
5.7e-20 absolute):

| quantity | even | odd |
|---|---|---|
| Z₃ = Σ z_m/(m³ l_m) | 1.2237461739301652e-13 | 1.2238425112912964e-13 |
| Π₃ = Σ p_m/(m³ l_m) | 1.475328444603237e-19 | 6.817704818152428e-20 |
| c₂ = −c·Z₃ + 2σL·Π₃ | −7.790567743129865e-14 | −7.791232456330331e-14 |
| W′₁ = δ/c₂ | −6.611744699301218e11 | −6.583311049219951e11 |

## Provenance and replay

- constants.py regenerates constants.json from the frozen
  coeff819 artifacts and the hash-pinned source (load_source
  asserts sha256 6c2b8d1d76e… of whole-source-affine.json).
- ctgate_producer.py stages dm/blocks/l2/bands regenerate
  anchors.json (`merge`). The blocks stage reads only the
  frozen blocks_{sector}.json and constants.json; the bands
  stage re-evaluates the model directly over all inputs m ≥ b
  (no composed buffers anywhere → the F2 [S, 2S) assembly
  defect cannot enter, gate condition 5).
- z3_eval.py regenerates z3.json.
- PACKAGE_MANIFEST.md carries SHA-256 of every witness file.

## Scope limits (unchanged from the gate)

No F1/F2 composition; no finite-gate verdict for the corrected
pair; no whole-residual / stationary / capacity claim;
thresholds (C_S_32000, 3e-5, 0.002) untouched; v14.354/v14.403
transport charged exactly once, elsewhere; v14.583 untouched.
Next steps belong to the gate order (Lane A hash freeze and
formula review, audit replay) — not taken here.
