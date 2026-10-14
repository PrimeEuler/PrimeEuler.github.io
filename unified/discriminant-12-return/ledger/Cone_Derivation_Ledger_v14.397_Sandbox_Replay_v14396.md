# Cone Derivation Ledger v14.397 — Sandbox Track (Little Euler)

## Sandbox HANDOFF-ACK v14.396: Independent Replay of the Finite-Plus-Gap Composition — Fail Verdict Confirmed Exactly (Byte-Identical Residual Buffers, Zero Rational Mismatches)

**Track:** Sandbox (our Lane B). **Answers:** the v14.396 HANDOFF (target: external-audit, sandbox — independently replay the frozen finite-plus-gap residual composition, verify the fail verdict against the unchanged $3\times10^{-5}$ threshold, check the source-minus-compact-minus-seed convention and the zero beyond-gap allowance, report any correction before further Lane A computation). **Status:** [D] for the replay equalities and verdict (exact integer/Fraction arithmetic); the localization paragraph in §4 is float64 diagnostics, marked [N], and is not certificate content. **Scope:** this entry confirms the scoped v14.396 gate verdict only. It evaluates nothing beyond the same 912,383 rows/sector and infers nothing about the whole infinite residual, stationarity, or the infinite-capacity tail.

---

## 1. Method

The composition was re-implemented independently from the convention stated in v14.396 — on each gap row, `residual = floor(bare source) − compact action − original-seed action` (bare source $1/n$ even-$v$, $1/(n-1)$ odd-$v$, floors at $2^{256}$) — without importing Lane A's producer (`compose_finite_gap_residual.py`, manifest SHA-256 `0657cccffa429feb45e297291194e8000a88529d28f327c10cd77eac8f34237a`). Every parent witness was hash-verified against its own certificate or manifest before use: all 46 chunk SHA-256 values of the v14.373 compact buffers and both reassembled whole-buffer hashes; both v14.353 finite-residual buffer sets against their certificate specs; the v14.393 seed buffers and certificates against the sandbox's own frozen copies. 36 witness/spec checks per sector, all pass.

## 2. Replay result — exact agreement

The independently computed gap-residual buffers are **byte-identical** to Lane A's derived buffers:

| derived buffer | sandbox replay SHA-256 | v14.396 manifest SHA-256 |
|---|---|---|
| even-$v$ gap residual (15,605,730 B, width 30) | `52211d2328ed390dc9874b1534784c709fe9412244f552194f4dd558b9e830fe` | `52211d2328ed390dc9874b1534784c709fe9412244f552194f4dd558b9e830fe` |
| odd-$v$ gap residual (15,605,730 B, width 30) | `350e020a7bc9f30aa66dae7b1b7966e112b81c56141c7bd73ae64eaeefdcb5fd` | `350e020a7bc9f30aa66dae7b1b7966e112b81c56141c7bd73ae64eaeefdcb5fd` |

All 20 compared output rationals per sector (gap point-norm bracket, the three gap error components and their sum, finite-plus-gap point bracket, the v14.354 envelope term, the corrected finite error, the quadrature-combined error, the physical brackets, the transport, the Schur bracket, and the beyond-gap allowance) match the v14.396 certificates **exactly, as Fractions — zero mismatches in either sector**. Headline values:

| quantity | even-$v$ | odd-$v$ |
|---|---|---|
| gap point norm | $6.190680111783266\times10^{-5}$ | $6.179331126462022\times10^{-5}$ |
| complete gap physical error upper | $1.7321072552110701\times10^{-15}$ | $1.0491625387211167\times10^{-15}$ |
| finite-plus-gap Schur lower | $6.455881206451175\times10^{-5}$ | $6.444121568319198\times10^{-5}$ |
| finite-plus-gap Schur upper | $6.456064557532373\times10^{-5}$ | $6.444139753725056\times10^{-5}$ |
| certified beyond-gap allowance | $0$ | $0$ |

**Verdict: the v14.396 FAIL is confirmed.** Both certified Schur lower bounds exceed the unchanged $3\times10^{-5}$ threshold; the failure is decisive and is not an artifact of the composition arithmetic, the buffer transport, or the error accounting. **No correction to v14.396 is required.**

## 3. Accounting checks specifically requested

- **v14.354 charged exactly once.** The replay charges the Region-2 + Region-3 self-term envelope ($8.072873472141806\times10^{-11}$ even, $8.065080648332971\times10^{-11}$ odd, summed from the v14.354 summands) once, to the finite physical error only. As a cross-check, the replay's finite point-norm bracket over the 392,192 finite rows reproduces the v14.353 certificate's declared bracket exactly in both sectors.
- **Convention.** The source floors use the same dyadic convention as the accepted finite evaluator ($S\,/\!/\,n$ resp. $S\,/\!/\,(n-1)$ with $S = 2^{256}$); compact and seed buffers are decoded at the certificate-declared 256-bit/30-byte format; row ranges of the compact and seed certificates agree ($1040385..2080765$ / $1040386..2080766$). The seed buffer's self-exclusion flag and the compact buffer's no-diagonal-beyond-support flag were both checked before composing.
- **Zero beyond-gap allowance.** With the combined physical upper ($\approx 6.456\times10^{-5}$ / $6.444\times10^{-5}$) already above $3\times10^{-5} - \text{transport}$, the allowance radicand is negative and the allowance is exactly 0, as certified.

## 4. Localization diagnostics [N] (float64; not certificate content)

Offered to Lane A's localization step; computed from the verified buffers:

- The gap residual mass is **broad and smooth**, not concentrated: decile shares of the gap $\ell^2$ mass decline monotonically from 16.6% (first decile of rows) to 6.0% (last) in both sectors, and the largest single row is only $\approx 3.3\times10^{-7}$ (at $n = 1047183$ even / $1064230$ odd). There is no defect row, spike, or boundary artifact to repair.
- The three gap-row vectors are nearly collinear: correlations $\langle\text{source},\text{seed}\rangle/(\lVert\text{source}\rVert\lVert\text{seed}\rVert) \approx +0.997$, $\langle\text{source},\text{compact}\rangle \approx -0.987$, $\langle\text{compact},\text{seed}\rangle \approx -0.987$ (both sectors). Component norms (even): source $4.9020\times10^{-4}$, seed action $5.2577\times10^{-4}$, compact action $8.09\times10^{-5}$.
- Along the near-common direction the seed action overshoots the source ($\langle\text{source},\text{seed}\rangle/\lVert\text{source}\rVert^2 \approx 1.069$), so the residual's along-direction component alone is $\approx 4.6\times10^{-5}$; the transverse (non-collinear) remainder is $\approx 4.2\times10^{-5}$. Both components exceed what the gate could absorb; the failure is a global coefficient-level mismatch of the current candidate on the gap rows, not a localized error.

## 5. Handoff status

The sandbox arm of the v14.396 HANDOFF is **CLOSED**: independent replay performed, fail verdict confirmed exactly, no correction reported. The scoped candidate stands rejected at the finite-plus-gap gate; what candidate change follows is Lane A's design question, and the sandbox asserts nothing about the whole infinite problem from this scoped result.
