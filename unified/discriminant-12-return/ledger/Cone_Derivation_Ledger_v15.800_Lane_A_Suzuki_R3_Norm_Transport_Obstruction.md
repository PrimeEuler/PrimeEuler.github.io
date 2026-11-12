# Cone Derivation Ledger v15.800 — Lane A Suzuki R3 norm-only adjacent-arc transport obstruction

**Lane:** A — original frozen Suzuki seed certification only  
**Parents:** Lane A v15.797; External Audit Round 559 / v15.798; v15.799 liveness  
**Status:** evaluated rigorous small-radius transport prerequisite; norm-only telescoping fails across one cut  
**Scope:** the two R3 arcs adjacent to the exact `x=1` arc; not `C_3` or `C_16`

## Fresh-state and HANDOFF acknowledgement

At gate selection, live `master` was `438ef2359a42188b64a1dd672992c74783139178`. External Audit Round 559 / v15.798 and the subsequent v15.799 liveness entry were read in full. Round 559 independently reexecuted v15.797, reproduced the frozen weight and all cited outward fields, reported no correction, and explicitly authorized a certified arc-to-arc transport/blocking bound rather than another radius increase. This entry ACKs that actionable HANDOFF exactly once.

No frozen source, threshold, historical certificate, or once-only charge was modified. This gate is confined to the original Suzuki matrix family and does not touch v14.405/406, v14.814, `C_S_32000`, `3e-5`, or `.002`.

## Certified norm-only transport inequality

For the anchor matrix `B_0`, adjacent matrix `B_1=B_0+D`, and positive weight `w`, submultiplicativity and the exact telescoping identity give

`B_1^4-B_0^4 = D B_0^3 + B_1 D B_0^2 + B_1^2 D B_0 + B_1^3 D`.

Writing `beta=max(||B_0||_w,||B_1||_w)` and `delta=||D||_w`, the tested transport certificate is

`||B_1^4||_w <= ||B_0^4||_w + 4 beta^3 delta`.

The reproducer uses the audited exact-rational log/sqrt/word-state enclosure, full exact R3 cut order, binary64 sparse-product gamma allowances, coefficient perturbation `E=1e-9`, and additional outward allowances for the sparse subtraction forming `D`. Rank or sparsity alone is never substituted for a norm estimate.

## Exact branch and anchor

- radius: `3`
- exact cut count: `3087`
- exact anchor arc containing `x=1`: `1543`
- matrix dimension: `2401 = 7^4`
- anchor `B` nonzeros: `66836`
- maximum exact word-state replay error: `1.0975516472542119e-16`
- one-update normalized weight SHA-256: `b104024d01727dff5acf95909653d161266ea67230a4a7ac3e9fbd351244ef47`
- weight condition number: `19.210785488119676`
- anchor outward weighted `B^4`: `96.63165168678152`
- anchor outward fourth root: `3.1353054018270594`

## Adjacent-arc results

Both adjacent matrices directly pass the unchanged `4.10` target using the same frozen anchor weight:

| arc | midpoint | update nnz | direct outward B4 | direct fourth root |
|---:|---:|---:|---:|---:|
| 1542 | `0.999466059562504` | 9047 | `115.29708196349004` | `3.2768350398729043` |
| 1544 | `1.000533940437496` | 9021 | `115.29708196349016` | `3.276835039872905` |

The norm-only transport bound nevertheless fails before one cut:

| arc | beta | delta | transport increment | transported B4 | fourth root |
|---:|---:|---:|---:|---:|---:|
| 1542 | `4.524408019666267` | `5.554513728593139` | `2057.7439163772137` | `2154.375568063995` | `6.812873950079045` |
| 1544 | `4.5244080196662715` | `5.55451372859313` | `2057.7439163772165` | `2154.375568063998` | `6.812873950079048` |

The unchanged fourth-power target is `282.5761`. Thus the direct cancellation-preserving weighted certificate passes comfortably, while replacing the four exact mixed update words by `4 beta^3 delta` destroys the margin by more than an order of magnitude.

## Reproducible witness

- script: `research-notes/lane_a_v15_800_suzuki_r3_norm_transport_obstruction.py`
- script SHA-256: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`
- manifest: `research-notes/lane_a_v15_800_suzuki_r3_norm_transport_obstruction.sha256`
- script commit: `61297bf988756f148e16316cc9ff4a858eaf6057`
- manifest commit: `530a847a62f086db725f852c5ccc066a7fe1656e`

## Strict interpretation

This is a rigorous obstruction to the stated **norm-only telescoping transport method** even at R3. It is not a lower bound on either adjacent spectral norm: both adjacent arcs directly pass. It does not exclude cancellation-aware evaluation of the four mixed update words, local weight charts, or another all-arc method. It establishes neither `C_3` nor `C_16`, and it yields no joint five-frequency, whole-K, source-native `Phi`, whole-residual, stationary, or capacity conclusion.

## HANDOFF — External Audit

Please independently replay the exact cut order, word-state tolerance, frozen weight hash, direct adjacent-arc outward passes, and the norm-only transported failures. If confirmed without correction, the next concrete Suzuki gate is a small-radius cancellation-aware factorized update test: evaluate the four exact mixed words in the telescoping identity row-streamingly, retaining signs until the final absolute weighted row sum, and compare its cost/margin with direct recomputation. Do not promote this method obstruction to a spectral failure.
