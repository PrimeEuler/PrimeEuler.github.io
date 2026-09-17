# Cone Derivation Ledger v13.532 — M16001 Source-Payload Conversion Certificate

**Status:** `[N-cert]` for nominal-payload conversion only. No theorem promotion.

## Scope

This entry closes the `source_payload_conversion` item left fail-closed by the primitive M16001 residual audit. It concerns conversion of the already-frozen nominal IEEE-754 binary64 payloads `Z`, `c`, and `PI` into the x86/NumPy `longdouble` arithmetic used by the outward replay. It does **not** replace or duplicate the independently certified exact-source versus nominal-source operator uncertainty `||A_exact-A_nom|| < 2e-13`.

Executable transcript:

`research-notes/suzuki_M16001_source_payload_conversion_transcript.py`

Merged certificate commit: `3a0dcb7e5498f2b9c7b9ad5910bc935645b76001`.

## Exact conversion argument

The CI platform reports a 64-bit `longdouble` significand versus a 53-bit binary64 significand, with sufficient exponent range. Every finite binary64 payload is a dyadic number with at most 53 significand bits, hence is exactly representable in this `longdouble` format. Therefore binary64 -> longdouble conversion introduces no rounding:

\[
\rho_Z=\rho_c=\rho_\pi=0.
\]

The executable transcript additionally checks finiteness and exact binary64 round-trip equality for all converted values.

## CI execution

GitHub Actions run `35168610433` completed the source-payload transcript successfully. It reported:

- longdouble significand bits = 64;
- binary64 significand bits = 53;
- 8001 `Z` entries checked;
- 8001 `c` entries checked;
- `PI` binary64 payload = `0x1.921fb54442d18p+1`;
- max `Z` conversion radius = 0;
- max `c` conversion radius = 0;
- `PI` conversion radius = 0.

Thus the propagated contribution of **payload conversion itself** to the residual is exactly

\[
\boxed{\|\Delta R_{\rm source\ payload\ conversion}\|_2\le
\|\Delta R_{\rm source\ payload\ conversion}\|_F=0.}
\]

All arithmetic performed *after* conversion remains charged by the displacement/pole/reduction transcripts; source-function approximation remains charged separately by the `2e-13` operator shift. No uncertainty is double-counted.

## Remaining fail-closed primitive gates

The source-payload conversion gate is closed. The residual certification still requires:

1. `diag_payload_conversion`;
2. `X_payload_conversion` / solve-payload provenance.

Accordingly the certified theorem remains

\[
\operatorname{ind}_{\le0}(A_{\rm even}(1))\le4,
\qquad
\operatorname{ind}_{\le0}(A_{a=1})\le6.
\]
