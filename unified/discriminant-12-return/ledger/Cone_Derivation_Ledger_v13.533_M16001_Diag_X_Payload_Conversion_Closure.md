# Cone Derivation Ledger v13.533 — M16001 diag0/X payload-conversion closure

**Status:** `[N-cert]` arithmetic payload-conversion closure; **no theorem promotion**.

## Purpose
Close the two remaining payload-conversion items left after v13.532: `diag_payload_conversion` and `X_payload_conversion` in the M16001 finite-solve residual replay.

## Executable certificate
Added and CI-executed:

`research-notes/suzuki_M16001_diag_X_payload_conversion_transcript.py`

Merged through commit `964d852a0feae18861fb9fa572618994339e1d61`.

The replay platform reports a 64-bit `longdouble` significand and a 53-bit binary64 significand. Every finite binary64 value is therefore exactly representable after conversion to this longdouble format. The script verifies finiteness and exact round trips for every frozen nominal payload.

CI checked:
- `diag0`: 8001 entries;
- `X`: 79910 entries, shape `(7991,10)`.

Frozen binary64 payload identities:
- `diag0` SHA-256: `858a99124ef69345aa6593c5c64599edf68905a8ee07384913c5e492c020a7bd`;
- `X` SHA-256: `800eb3791cbf1cf803243c60954215d6ce7c2082f726c11598df6960dcb6866f`.

The certified conversion radii are

\[
\rho_{\rm diag0}=0,\qquad \rho_X=0,
\]

hence the residual perturbation caused solely by these two payload conversions is exactly

\[
\boxed{\|\Delta R_{\rm diag0/X\ conversion}\|_2\le
\|\Delta R_{\rm diag0/X\ conversion}\|_F=0.}
\]

Together with v13.532 this closes the conversion gate for `Z`, `c`, `PI`, `diag0`, and `X`.

## Why no forward solve certificate for X is required here
The residual/backward-error argument does not assume that the computed `X` is a forward-accurate representation of the exact solve. Once the binary64 `X` payload is frozen, it is an arbitrary candidate matrix. The proof obligation is to enclose

\[
R_F=A_{FF}^{\rm nom}X-A_{FC}^{\rm nom}
\]

for that candidate and combine the residual with the independently certified coercivity/inverse bound. Thus arithmetic used to *produce* X is not a separate payload-conversion uncertainty. The conversion of the frozen candidate into the longdouble residual replay is exact.

## Separation of uncertainties
The exact-source versus nominal-source uncertainty remains the independently certified operator-level bound

\[
\|A_{\rm exact}-A_{\rm nom}\|<2\times10^{-13},
\]

handled by the shifted-nominal argument. It is not double-counted as a payload-conversion radius.

## Audit consequence
The payload-conversion branch of the v13.520 primitive residual gate is now closed. This does **not** by itself certify the full M16001 seven-plane argument: the remaining global proof obligations are the outward formation/propagation chain outside this payload-conversion subgate, including the Q/N and remote/far-tail arithmetic gates identified in v13.505/v13.510 and subsequent audits.

Therefore theorem status remains

\[
\boxed{\operatorname{ind}_{\le0}(A_{\rm even}(1))\le4},\qquad
\boxed{\operatorname{ind}_{\le0}(A_{a=1})\le6}.
\]

No exact-zero, RH, or GRH claim is promoted.
