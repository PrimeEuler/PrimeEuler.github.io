# Cone Derivation Ledger v13.831 — External Audit Round 111

Date: 2026-09-28

Auditor: External audit thread (Claude, independent instance).

Scope: v13.830 — the exact full smooth-bulk Pontryagin index two (both parity sectors), the N=96 six-root Krein-signature diagnostic, and the theorem-scale M3999/4000 finite low-core endpoint Schur sign pattern at rho=0.02 and 0.10.

Verdict: **PASS. Fully verified, algebra and both scripts.**

## 1. Algebra checked by hand

- **Exact core block entries (§1)**: recomputed `B_CC^(e)` and `B_CC^(o)` directly from the stated closed forms (`-log4-1/2`, `log(3/4)-1/6`, `-1/4` for even-v; `-log2-1/4`, `-1/8`, `-1/6` for odd-v). Both matrices and both eigenvalue pairs reproduced to the reported precision by hand (even-v: `-1.92868628, -0.41195682`; odd-v: `-0.97579633, -0.09235085`), confirming `tr<0` and `det>0` in both sectors and hence `B_CC≺0`.
- **Schur/congruence argument (§2)**: re-derived independently. `B_T>0 ⟹ B_CT B_T^{-1}B_TC ⪰0` (it's `X^TB_T^{-1}X` with `B_T^{-1}≻0`), so `S_B=B_CC-B_CT B_T^{-1}B_TC ⪯ B_CC`. Since `B_CC≺0` is negative *definite*, `S_B⪯B_CC` gives `v^TS_Bv≤v^TB_CCv<0` for all `v≠0`, i.e. `S_B≺0` too — not just "more negative" in the Loewner sense, but strictly negative definite. Block congruence (Schur-complement decomposition into `diag(S_B,B_T)`) then gives `ind_-(B_sm)=ind_-(S_B)+ind_-(B_T)=2+0=2` by Sylvester's law of inertia. Correct and exact — this is the strongest of the three new claims and it holds unconditionally, not just numerically.
- **§3 guardrail (signed Krein/Pontryagin spectral flow)**: the stated fact — that once negative-metric directions are present, endpoint inertia differences are *signed* crossing counts (weighted by `-⟨q,Bq⟩` at each simple real crossing) rather than raw multiplicities — is the standard indefinite-inner-product spectral-flow fact and is correctly invoked as a guardrail, not overclaimed.

## 2. Numerics: ran both new scripts directly

**`suzuki_full_bulk_pontryagin_index_signature.py`** — ran to completion, PASS. The exact-interval core-block values matched hand computation to all printed digits in both sectors. The N=96 diagnostic reproduced the invariant claims exactly: `full N96 B negative index = 2` in both sectors, cluster Krein inertia `(2,4)` in both sectors, and `endpoint inertias (F-,F+,difference) = {0.02: (4,2,2), 0.10: (4,2,2)}` in both sectors — all matching v13.830 §§4–5 exactly.

One thing worth flagging (not an error): I reran the N=96 cluster-eigenvalue diagnostic three times and got a **deterministic but different** set of individual `cluster_B_eigenvalues` than the ledger's printed decimals — e.g. even-v: mine is `[-1.696365, -0.24113, 0.13136, 0.21739, 0.24267, 0.32617]` vs the ledger's `-1.5390, -0.2152, 0.1502, 0.2183, 0.2427, 0.3262`. This is expected, not a bug: four of the six generalized roots sit at floating-point zero (`~1e-16` to `~1e-19`), so the basis LAPACK returns for that near-null invariant subspace is essentially arbitrary (it isn't B-orthonormalized before forming `W^TBW`), and congruent bases give congruent — same inertia, different eigenvalues — matrices by Sylvester's law. The entry's own text already carries the correct caveat for this ("invariant under rotations among the nearly degenerate Ritz vectors; does not assign signatures to individual machine-zero eigenvectors"), so the only actual invariant claim, the `(2,4)` split, reproduces exactly. Worth a one-line note in a future entry that the raw decimal eigenvalues shown for this diagnostic are platform/BLAS-dependent and shouldn't be treated as reproducible figures, only their signs/count.

**`suzuki_low_core_endpoint_schur_M3999.py`** — ran to completion, PASS. **Every single reported number matched exactly**: all four `S_C` matrices and eigenvalue pairs at `rho=0.02` (even-v minus `[0.00918488, 0.04426462]`, even-v plus `[-0.046136, -0.00959144]`, odd-v minus `[0.00348164, 0.02660098]`, odd-v plus `[-0.02138735, -0.00202571]`) and at `rho=0.10` (even-v minus `[0.01891717, 0.15834345]`, even-v plus `[-0.24321735, -0.05036823]`, odd-v minus `[0.01204398, 0.11203389]`, odd-v plus `[-0.1125374, -0.012072]`), digit-for-digit. Confirmed by hand that the smallest absolute eigenvalue across all eight `rho=0.02` cases is `0.00202571` (odd-v plus), matching the claimed sign margin `≈2.03×10⁻³`. Tail-solve residuals (min `3.599×10⁻¹⁶`, max `1.489×10⁻¹⁴`) and solution norms (max `2.2833`) both fall inside the entry's stated ranges (`residual<2×10⁻¹⁴`, `norm<2.5`), matching §9's summary of "between 3.2e-16 and 1.5e-14" / "below 2.3" to within the stated "approximately."

## 3. Scope

Correctly guarded throughout. The entry is explicit that: the exact theorem is only `ind_-(B_sm)=2`; the six-root/signature split and the M3999 Schur sign pattern are finite-section diagnostics, not infinite-tail theorems; no claim is made that the two low-core roots are real/simple, that the finite signs survive the infinite remote correction, that the endpoint inertia difference counts ordinary multiplicity, or that `κ0`/`κ1`/RH/GRH are touched. This matches the actual strength of what was computed.

## Self-audit note

No error of my own found this round.

## Result

\[
\boxed{\textbf{PASS: v13.830 fully confirmed.} \operatorname{ind}_-(B_{\rm sm})=2 \textbf{ exactly in both parity sectors (hand-verified unconditional algebra); the N=96 Krein-signature split } 2^-{+}4^+ \textbf{ and the theorem-scale M3999 low-core endpoint Schur sign pattern } S_C^{(M)}(+\rho)\succ0,\ S_C^{(M)}(-\rho)\prec0 \textbf{ at } \rho=0.02,0.10 \textbf{ both independently reproduced exactly by direct script execution.}}
\]
