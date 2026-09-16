# Cone Derivation Ledger v13.520 — M16001 Primitive Residual Audit Gate

Date: 2026-09-16

Status: **[Audit]** fail-closed. No theorem promotion.

## 0. Synchronization

Live head checked at start and immediately before this numbered write. v13.519 (External Audit Round 41) is the latest numbered entry; helper commit `3af897c1...` is newer but unnumbered. Therefore v13.520 is free.

## 1. Line-by-line audit result

The v13.514 residual helper correctly charges the principal reductions *conditional on its nominal long-double payloads*:

- ten reductions `c_F^T X[:,r]`, each length 7991, with radius `gamma_7991 sum |c_j X_jr|`;
- 79910 reductions `(A0_FF X)_{ir}`, each length 7991, with radius `gamma_7991 sum_j |A0_ij X_jr|`;
- propagated pole-dot uncertainty `2 |c_i| radius(c_F^T X_r)`;
- a `gamma_3` allowance for pole scaling/combination;
- a `gamma_1` allowance for the final subtraction of the stored nominal `A_FC`.

The helper reports the maximum absolute-product sum and maximum dot charge, and accumulates entrywise envelopes into a Frobenius upper bound. External Audit Round 40 independently reran the calculation and obtained a slightly smaller residual, so the stated `9.55035036608530e-15` envelope remains a useful conservative arithmetic diagnostic.

## 2. Primitive gaps

That envelope is **not yet accepted as a theorem-level primitive outward radius**. The audit identifies nine explicit remaining transcripts:

1. formation of every off-diagonal `A0_FF` displacement entry, including the two products/subtraction in the numerator, the two squares/subtraction in the denominator, division, and `2/pi` scaling;
2. identical primitive formation for `A0_FC`;
3. formation of the rank-one `2*cF*cC` contribution and its addition to `A0_FC`;
4. nominal diagonal payload conversion to long double;
5. nominal `Z`, `c`, and `pi` payload conversion radii;
6. provenance/conversion radius for the computed `X` payload consumed by the residual checker;
7. rounding of each `(|R|+E)^2` term;
8. the 79910-term nonnegative Frobenius accumulation, whose standard factor is `gamma_79910`;
9. an outward square-root endpoint (or a rigorously larger algebraic surrogate).

Source-function uncertainty remains separate and is already intended to be absorbed by the shifted-nominal `2e-13 I` construction; it must not be double-counted here. The present issue is arithmetic formation of the nominal payload.

## 3. Executable gate

Added

`research-notes/suzuki_M16001_primitive_residual_audit_gate.py`

commit `3af897c1dd32f17861fad072d78d6713df7600c3`.

It records the nine primitive obligations explicitly and fails closed while any is absent. It also prints `gamma_7991` and `gamma_79910` from `u=2^-64`; no empirical discrepancy or chosen safety multiplier is accepted.

## 4. Certified status

Unchanged:

\[
\boxed{\operatorname{ind}_{\le0}(A_{\rm even}(1))\le4},\qquad
\boxed{\operatorname{ind}_{\le0}(A_{a=1})\le6}.
\]

Next obligation: implement primitive interval/roundoff formation for the displacement and `A_FC` entries, then close the Frobenius sum/sqrt transcript. Only afterward may the residual radius enter the final seven-plane replay.