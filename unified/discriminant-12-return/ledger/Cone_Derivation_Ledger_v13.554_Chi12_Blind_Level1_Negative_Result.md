# Cone Derivation Ledger v13.554 — χ12-Blind Suzuki Level-1 Negative Result

**Status:** reproducible finite binary64 midpoint diagnostic; the first genuinely χ12-blind test of the q=5,7 versus q=11,13 phase-bridge proposal. Negative result for the predeclared Level-1 clustering gate. No theorem promotion.

## 1. Motivation and provenance

v13.553 identified the structural defect in the original Level-0 phase test: among the canonical unramified source channels only q=5,7 were present, and both have χ12=-1. It recommended extending the source-faithful Suzuki construction to q=11,13, the two smallest unramified primes with χ12=+1, so that the proposed bridge could finally face a nondegenerate sign contrast.

The original Level-0 script is an algebraic/source identity: χ12 and epsilon are inserted directly into the comparison formula. Passing Level 0 therefore remains an implementation/provenance gate, not independent evidence that the Suzuki operator produces a χ12 phase partition.

This entry records the next gate, constructed so that χ12 is absent from the observable itself.

Reproducer:

`research-notes/suzuki_chi12_phase_bridge_level1_blind.py`

## 2. Exact/frozen inputs

Use the existing Suzuki source construction and unit-core classes

`R={1,5,7,11}`.

For each prime q in `{5,7,11,13}` construct the source matrix `C_q` with

`w_q=log(q)/sqrt(q)`, `ell_q=log(q)`,

`Z_q(n)=2 w_q sin(n pi ell_q/2)`,

and the same diagonal/source `make(Z,d)` formula used by `suzuki_unit_core_delta57_checkpoint.py`.

Crucially, the whitening metric is frozen from the canonical pre-extension baseline

`B0=C_arch+C_2+C_3+C_4+C_5+C_7`.

Thus q=11 and q=13 do not alter the measuring metric used to evaluate themselves.

No χ12 value, epsilon, or character-sign lookup enters `C_q`, `B0`, the Cholesky factors, the SVD, or the response fingerprints.

Only after the fingerprints are frozen is the exact arithmetic partition revealed:

`χ12(5)=χ12(7)=-1`, `χ12(11)=χ12(13)=+1`.

## 3. Level-1 observable

For each center stratum r and destination stratum s, form the fixed-whitened block

`W_q^(r,s)=L_r^{-1} C_q[I_r,I_s] L_s^{-T}`,

where `L_r L_r^T=B0[I_r,I_r]`.

For each r concatenate its three off-diagonal blocks and compute the leading singular triplet. The amplitude-normalized response magnitude is

`R_q(r)=sigma_max(W_q^(r))/(log(q)/sqrt(q))`.

Fix the otherwise arbitrary SVD sign by requiring the largest-magnitude component of the left singular vector to be positive. Resolve the leading response over the three destination blocks and normalize by the leading singular value. The resulting twelve signed block contributions form the χ12-blind directional fingerprint `F_q`.

For two source channels define

`D(q,q')=||F_q-F_q'||_2/sqrt(12)`.

The predeclared pairwise clustering gate is

`min_{q in {5,7}, q' in {11,13}} D(q,q') > max(D(5,7),D(11,13))`.

A positive gap would mean every opposite-sign pair is farther apart than either same-sign pair. A negative gap is a direct failure of this Level-1 χ12 clustering criterion.

## 4. Binary64 cutoff results

The diagnostic was run independently at M=499, 999, and 1999 with the full baseline whitening metric rebuilt at each cutoff.

| M | D(5,7) | D(11,13) | D(5,11) | D(5,13) | D(7,11) | D(7,13) |
|---:|---:|---:|---:|---:|---:|---:|
| 499 | 0.24969865190206586 | 0.18262999130777416 | 0.15487947712713240 | 0.07666661077664701 | 0.26039208565187827 | 0.28821257235631254 |
| 999 | 0.25023163466831722 | 0.18275356241820276 | 0.15487650957487037 | 0.07680790414765121 | 0.26075877132338710 | 0.28875306365465969 |
| 1999 | 0.25044969506637760 | 0.18281543181931478 | 0.15487650604882205 | 0.07687756223288036 | 0.26089969510775923 | 0.28897948195250678 |

The decisive pairwise gap is therefore

| M | max within-sign distance | min cross-sign distance | gap = min cross - max within |
|---:|---:|---:|---:|
| 499 | 0.24969865190206586 | 0.07666661077664701 | -0.17303204112541887 |
| 999 | 0.25023163466831722 | 0.07680790414765121 | -0.17342373052066600 |
| 1999 | 0.25044969506637760 | 0.07687756223288036 | -0.17357213283349723 |

The sign and scale of the failure are stable across the three tested cutoffs. In particular, q=5 and q=13 — which carry opposite χ12 signs — are by far the closest pair in this metric, while the same-sign q=5 and q=7 pair is much farther apart.

## 5. Result

**[OBS] Level-1 blind clustering gate: FAIL.**

The Suzuki source-response fingerprints do not form the proposed `{5,7}` versus `{11,13}` 2+2 partition. The failure is not marginal: at M=1999 the required pairwise gap is approximately `-0.17357213`, and essentially the same negative gap is already visible at M=499 and M=999.

This is the first clean negative result for the χ12 phase-bridge proposal because, unlike Level 0, the tested observable is constructed without χ12 and only compared with the character partition afterward.

## 6. Evidence-status legend and guardrails

**Legend:** `[EXACT]` exact recomputation/algebra; `[B64]` finite binary64 checkpoint output; `[OBS]` empirical pattern from the run; `[UNSUPPORTED]` conclusion not established by present evidence.

- **[EXACT]** `χ12(5)=χ12(7)=-1` and `χ12(11)=χ12(13)=+1`.
- **[B64]** The tabled distances and gaps are finite binary64 midpoint outputs with independently rebuilt whitening at each listed cutoff.
- **[OBS]** The predeclared χ12-blind Level-1 clustering criterion fails stably at M=499,999,1999.
- **[UNSUPPORTED]** This does not prove that no other Suzuki observable can correlate with χ12.
- **[UNSUPPORTED]** It does not establish a universal negative theorem for all q or all cutoffs.
- **[UNSUPPORTED]** It does not establish or refute an exact V4/Pell-Suzuki intertwiner by itself.
- **[UNSUPPORTED]** It does not alter any positivity, index, RH, or GRH statement.

The certified Suzuki index status remains unchanged.

## 7. Next gate

Do not tune or relabel the Level-1 metric to rescue the failed partition. The informative next step is diagnostic rather than promotional: inspect why the χ12-blind fingerprints place q=5 and q=13 unusually close, and test whether the geometry is instead organized by a different already-defined source variable (for example log-frequency proximity or another independently specified arithmetic character). Any such test must be predeclared before consulting its labels, exactly as in Level 1, to avoid post-hoc pattern fitting.
