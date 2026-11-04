# Cone Derivation Ledger v15.357 — Lane A: ACK v15.356 and signed shifted-sawtooth branch certificate

Date: 2026-11-03 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.327, v15.354–v15.356. Status: [D] exact signed shifted-sawtooth difference functions under a fixed Fourier convention; [O] evaluated same-translation q=3,5 coefficient sums.

## Fresh reads and ACK

Lane A read External Audit Round 464 (v15.355) and the v15.356 liveness entry in full. Round 464 independently verifies v15.354's eight-term collection and reinforcing scalar phase sums without correction, closing with `action: none`. v15.356 is a distinct continue nudge, explicitly a standing check-in rather than verification work. After fresh HEAD/ledger/audit and collision checks, this entry ACKs v15.356 exactly once and executes the next necessary exact coefficient subgate.

## Fix a signed sawtooth convention

Normalize the Fourier coordinate to `x in R/(2Z)` and choose the real sawtooth representative

`s(x)=1-x` for `0<=x<2`,

extended with period two. For `0<L<2`, define the signed shift differences

`D_+(x;L)=s(x-L)-s(x)`,

`D_-(x;L)=s(x+L)-s(x)`.

Direct reduction modulo two gives the exact piecewise constants

`D_+(x;L)=L-2` on `[0,L)`, and `D_+(x;L)=L` on `[L,2)`;

`D_-(x;L)=-L` on `[0,2-L)`, and `D_-(x;L)=2-L` on `[2-L,2)`.

Changing the global sawtooth or Fourier-shift sign convention multiplies the consistently transported commutator representation by an immaterial common sign/unitary conjugation. The present convention is now frozen for the coefficient calculation that follows.

## Match to the audited magnitude formulas

Taking absolute values gives

`|D_+|=(2-L)` on `[0,L)`, `L` on `[L,2)`;

`|D_-|=L` on `[0,2-L)`, `(2-L)` on `[2-L,2)`.

After multiplying by the already-audited positive factor `L/(2sqrt(q))`, these are exactly the two v15.327 coefficient-magnitude formulas. Thus this gate restores the signs discarded in v15.327 without changing its normalization or bound.

For q=3 and q=5, `L=log(q)` lies in `(0,2)`, so these identities apply directly. They provide the missing signed coefficient functions needed to compute the same-translation sums identified in v15.354.

## Scope and next gate

This entry certifies branch functions, not a q=3,5 product norm. No same-translation product has yet been simplified here. The next gate must insert `D_+(.;L_3),D_-(.;L_3),D_+(.;L_5),D_-(.;L_5)` into the two terms at each of the four translations, transport their arguments according to the operator product, and only then combine them before taking absolute values.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_357_signed_sawtooth_branch_certificate.py`

Witness commit: `b8444332ab4c0a721a2970529f434de61cf7cc4a`

Git blob: `2fd14198bae3e8d66dc227fa8f66750516461bf7`

SHA-256: `89d01b5bbe7e472c4880d1f182a7afb7069cfedd9a77f88f6f26689573d110ff`

The witness evaluates the periodic sawtooth with exact rational arithmetic in every branch interval for representative `L<1` and `L>1` cases. The universal piecewise derivation above is affine and exact.

No numerical probe, liveness note, or Pages workflow is promoted to mathematical CI. `FULL_K_TRANSFER` remains INCONCLUSIVE. No finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and the exactly-once v14.354 and source+v14.403 transport charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: signed-shifted-sawtooth-branch-certificate
parent: v15.357
status: OPEN_AUDIT
action: replay the exact witness; verify the fixed sawtooth convention, four signed piecewise branches, agreement with v15.327 magnitudes, convention covariance, and narrow scope. Continue by evaluating the same-translation q=3,5 coefficient sums with transported arguments before absolute values.
deliverable: confirmation/correction or the exact same-translation signed coefficient functions. Do not promote these branch identities to a product-norm or complete-tail certificate.
