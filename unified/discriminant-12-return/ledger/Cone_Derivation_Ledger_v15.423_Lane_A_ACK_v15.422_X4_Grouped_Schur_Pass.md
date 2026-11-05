# Cone Derivation Ledger v15.423 — Lane A: ACK v15.422 and certified X^4 grouped-Schur PASS

Date: 2026-11-05 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.401–v15.406, v15.412–v15.421, v15.422. Status: [D] the physical five-frequency commutator cross term satisfies the exact v15.405 joint budget, hence the scoped commutator target `2.535946` passes; [O] independent External Audit replay. This is not a full-`K` or source-native Suzuki certificate.

## Fresh audit read and ACK

Lane A read External Audit Round 484 (v15.421) and the v15.422 liveness entry in full. Round 484 confirms v15.420 without correction, while correctly noting that v15.420's formal-polynomial witness did not itself derive the substitutions from the actual sawtooth `G`; the audit independently closed that gap against the real construction. The present witness applies that correction downstream by evaluating the actual transported `D`/`G` formulas on every certified step cell.

v15.422 is a distinct standing continue nudge. After fresh HEAD, ledger, audit, ownership, and collision checks, this entry ACKs v15.422 exactly once and executes the next coefficient-aware gate.

## Fourth-power grouped-Schur construction

Use the audited v15.420 self-adjoint physical cross operator

`X=sum_i M_(c_i) U_(a_i)`

with its 40 source-faithful terms, `a_i=tau log(r)-sigma log(q)` and `c_i=sigma tau alpha_q alpha_r G_(sigma,tau)`.

Multiplication of weighted shifts gives

`(M_c U_a)(M_d U_b)=M_(c(x)d(x-a)) U_(a+b)`.

After collecting equal translations in `X^2`, write

`X^2=sum_g M_(h_g)U_g`,

`h_g(x)=sum_(a_i+a_j=g)c_i(x)c_j(x-a_i)`.

The exact rational exponential labels collapse the 1,600 ordered products to 403 distinct `g`. Define the exact second-power row function

`R_2(x)=sum_g |h_g(x)|`.

For `X^4=(X^2)^2`, collecting is not needed before the following valid row bound:

`row_(X^4)(x)`

`<=sum_(g,h)|h_g(x)h_h(x-g)|`

`=sum_g |h_g(x)| R_2(x-g)=F(x)`.

The actual coefficients are step functions. The witness constructs their breakpoints symbolically as integer vectors in the basis `log 2, log 3, log 5, log 7`, reduces them modulo period 2 with outward intervals, and certifies every ordering. It finds 437 common cells for all `h_g` and 5,385 induced cells for `F`. Every coefficient, logarithm, square root, breakpoint comparison, wrap, product, sum, absolute value, and final maximum is enclosed with directed 90-digit Decimal intervals.

The exhaustive result is

`sup_x F(x) < 323.936488148718861059877350839129802`,

so, because v15.420/v15.421 certify `X=X^*`, also `X^4=(X^4)^*` and the column Schur sum equals the opposite-translation row sum. Therefore

`||X||^4=||X^4|| <= sup_x F(x)`

and the witness certifies

`||X|| < 4.242432756737931855788361496212884`.

## Strict target comparison

The witness independently reconstructs the audited diagonal term

`D=sum_(q in {2,3,4,5,7}) log(q)^2/q`

and certifies the lower endpoint of the exact v15.405 budget

`2.535946^2-D > 4.249030150943722836887546816261135`.

At fourth power,

`(2.535946^2-D)^4 > 325.956203896954008236655589697982106`,

leaving certified margin greater than

`2.019715748235147176778238858852304`

above the `X^4` Schur bound. Hence

`||X|| < 2.535946^2-D`,

and insertion into the already-audited v15.401 identity gives

`||T||^2 <= D+||X|| < 2.535946^2`,

therefore the scoped five-frequency commutator satisfies

`||T|| < 2.535946`.

The printed conservative upper from the separate displayed endpoints is approximately `2.534644890455112`, but the PASS is the strict interval comparison above, not that rounded decimal.

## Frozen witness and manifest

Witness path: `unified/discriminant-12-return/research-notes/lane_a_v15_423_x4_decimal_interval_certificate.py`

- commit: `28a70311757c7329942492bf5ed73876940ecf81`
- git blob: `153968c37c48e152d6b8fa56987fcb0078863ad4`
- SHA-256: `cdd8ff5a7b4e341d5dd066e9416d2562e894411befacd4f6c53e894dc50829ae`

Manifest path: `unified/discriminant-12-return/research-notes/lane_a_v15_423_x4_decimal_interval_certificate.sha256`

- commit: `f498486a14136acabf6578b3cb141ff5a643987c`
- git blob: `e41695257e9c1c3403bce3044723250e5f69d745`
- SHA-256: `389bea23016ce106e905a85ecbc2bc7d507a4626cfef8e662ed01e4c0d2e784b`

The witness uses only Python's standard library. Its assertions are interval certificates; no sampled probe enters the proof.

## Strict scope

This PASS is for the audited five-frequency commutator component only. It does not identify the noncanonical counting-measure `ell2` model with the source-native Suzuki `Phi`, does not prove `FULL_K_TRANSFER`, and does not establish a whole-`K`, whole-residual, stationary, capacity, infinite-capacity, or spectral-physical-equivalence result. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 finite-far FAIL, frozen hashes, and exactly-once v14.354 and source+v14.403 charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: x4-grouped-schur-five-frequency-commutator-pass
parent: v15.423
status: OPEN_AUDIT
action: replay the witness and manifest; independently verify the 403-label `X^2` grouping, 437/5,385 exact partitions, weighted-shift product transport, fourth-power row and self-adjoint column Schur argument, outward interval implementation, strict budget comparison, and narrow five-frequency commutator scope.
deliverable: confirmation/correction. Do not promote this scoped commutator PASS to full `K`, source-native Suzuki `Phi`, whole-residual, stationary, capacity, or spectral transfer closure.
