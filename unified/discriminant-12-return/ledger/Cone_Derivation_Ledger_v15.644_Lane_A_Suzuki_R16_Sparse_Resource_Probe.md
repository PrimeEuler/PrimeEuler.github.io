# Cone Derivation Ledger v15.644 — Lane A Suzuki: radius-16 sparse field executes, spectral norm certification still open

**Date:** 2026-11-10 (America/New_York). **Lane:** A, frozen original Suzuki five-frequency commutator. **Parents:** v15.420, v15.497–502, v15.643. **Status:** [N] reproducible binary64 finite sparse matrix probes and resource feasibility; explicitly **NOT** an outward spectral norm upper certificate. No Sandbox handoff.

## Fresh state

At the preceding gate, v15.643 deposited a rational interval improvement in the tensor-tent localization penalty: `E_16^word < 0.142` (more precise orientation 0.14117490094584). A certified finite field supremum `C_16 < 4.10` would, by the audited v15.499 localization theorem, imply the desired joint cross-operator budget `||X||<4.249030150943723`. The new sparse experiment tests practicality of the finite representation, not the remaining inequality.

Live HEAD and next-free path checked before writing the witness, now committed at `665ee993a4b6a68928ab8592aae9dd5a3025b6e4`; no other lane's data modified.

## Physical 40-word sparse assembly

Use the already-certified v15.420 `X=sum_(q<r,s,t) s*t*alpha_q*alpha_r*M_G U_(t log r-s log q)`, with integer four-vector shift `g=t v_r-s v_q`, `v_4=2v_2`. The regular-representation finite matrix at period coordinate x has row h, column h-g and coefficient

`B_R(x)[h,h-g] = s*t*alpha_q*alpha_r*G_{s,t}^{qr}(x+h·L)`,

if both h and h-g lie in `[-R,R]^4`, and zero otherwise; `L=(log2,log3,log5,log7)`. Here `alpha_q=log q/(2sqrt q)`. This is exactly the v15.497 regular representation's `alpha_{-h}` convention. No missing factor 2, no wrong `s log q+t log r` shift, and **no intermediate absolute values** were introduced.

Independent entry-by-entry float-adjoint checks on radii 2, 4, 6, 8, 10 found max defects around `1e-15` or smaller, consistent with v15.420's exact adjoint transport. Binary64 may misresolve intervals extremely near a sawtooth discontinuity: this experiment has NO rigorous branch certification.

## Evaluated resource and norm-orientation results

On a single local CPU process with `OPENBLAS_NUM_THREADS=1` (SciPy CSR, `eigsh` sparse Lanczos for the **largest algebraic eigenvalue** at the single coordinate `x=0.12345`):

| R | sites | nonzeros | sampled largest eigenvalue |
|---:|---:|---:|---:|
| 2 | 625 | 14,700 | 2.50480581 |
| 4 | 6,561 | 199,260 | 3.28170551 |
| 6 | 28,561 | 948,428 | 3.54541114 |
| 8 | 83,521 | 2,902,716 | 3.66167082 |
| 10 | 194,481 | 6,948,396 | 3.72279581 |
| 12 | 390,625 | 14,217,500 | 3.75874141 |
| 16 | **1,185,921** | **44,182,908** | **3.79708131** |

Radius 16 assembled in approximately **7.1 s**, compressed CSR memory around **535 MB** and the sampled largest eigenvalue completed in approximately **21.4 s** total. Runtime figures are machine-dependent, not complexity theorems. A scan of 20 period-coordinate samples at R=8 yielded positive extreme eigenvalue values approximately `3.66177`–`3.66196`; not an exhaustive x-envelope. An attempted radius-16 smallest algebraic eigenvalue run did not complete before execution timeout; no statement about that negative spectral edge is made.

**Interpretation:** the sparse field at R=16 is practical for *some* one-coordinate numerical operations. The observed `3.79708` is at most a **noncertifying orientation value** for the positive edge, and cannot replace the necessary `C_16 = ess sup_{x}||B_R(x)||` (which requires **both** signed spectral ends and **all** x). A sampled largest eigenvalue is NOT a norm upper bound. This gate does not improve the rigorously audited `2.892017147...` global five-frequency commutator upper frontier.

## Exact remaining computational gate

1. Establish fully rigorous, outward Hermitian coefficient intervals for finite field matrices using certified log/sqrt and sawtooth cut enclosures; resolve jumps, not merely round samples.
2. Establish an interval-certified upper bound on the **full absolute eigenvalue norm**, with a posteriori residual/eigenvalue enclosure or proven positive-polynomial/SOS majorant, not bare `eigsh`.
3. Uniformize across the period-two x-variable. The field is piecewise constant but its breakpoints are translated by every h in the 33^4 box, so 20-point sampling is inadequate. Exploit translation covariance, symbolic breakpoints, or a certified multiscale bound.
4. If the rigorous outcome `C_16<4.10` is achieved, then combine with v15.643's rigorous `E_16<0.142` and the v15.499 upper enclosure. Otherwise report nonclosure without weakening the target.

**Reproducer:** `unified/discriminant-12-return/research-notes/lane_a_v15_644_sparse_matrix_field_probe.py`, witness commit `665ee993a4b6a68928ab8592aae9dd5a3025b6e4`. Dependencies: numpy and scipy; run with `OPENBLAS_NUM_THREADS=1 python3 ...`. Values are floating reconnaissance, explicitly not interval certificates. Independent External Audit should verify signed matrix indices, adjoint transport, the sampled matrices, and the scope boundary.

**Protected state:** original seed unmodified; v14.405 recovered/v14.406 finite-plus-gap PASS and v14.814 finite-far FAIL unchanged; original `C_S_32000`, `3e-5`, `.002` and charge-once constraints untouched. `FULL_K_TRANSFER=INCONCLUSIVE`, noncanonical chosen ell2 not physical Suzuki Phi; no whole-residual, stationarity, or infinite-capacity claim.
