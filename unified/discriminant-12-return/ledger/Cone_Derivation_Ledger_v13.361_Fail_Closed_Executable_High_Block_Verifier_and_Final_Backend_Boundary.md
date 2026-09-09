# Cone Derivation Ledger v13.361 — Fail-Closed Executable High-Block Verifier and Final Backend Boundary

## Status
Certification architecture / executable integration checkpoint. No global positivity, exact-zero, RH, or GRH claim is made here.

## What changed
The v13.354–v13.360 finite high-block work is now consolidated into one executable, fail-closed verifier entry point:

`research-notes/suzuki_final_high_block_verifier.py`.

The target remains

\[
B=A_{0,[21,16001]}-0.22I,
\]

a 7991-dimensional pole-free high block.

The structured recurrence is

\[
b_i=\frac{2}{\pi}\frac{u_1v_i-v_1u_i}{x_1-x_i},\qquad
\ell_i=b_i/a,
\]
\[
u_i'=u_i-\ell_i u_1,\qquad
v_i'=v_i-\ell_i v_1,\qquad
d_i'=d_i-b_i\ell_i.
\]

The local replay certificate from v13.359 and global composition from v13.360 are wired into a single transcript interface. A successful proof transcript must contain

- minimum pivot and its mode;
- \(\||L|\|_1\);
- \(\||L|\|_\infty\);
- sum of local Frobenius defects;
- arithmetic residual bound;
- exact-vs-nominal matrix uncertainty;
- total residual;
- pass/fail.

The pass conditions are

\[
\min d_j>0.25,
\]
\[
E_{\rm arith}<10^{-8},
\]
\[
E_{\rm matrix}<2\times10^{-13},
\]
\[
E_{\rm arith}+E_{\rm matrix}<3.15\times10^{-6}.
\]

The default archimedean kernel uncertainty is kept separately at

\[
1.22\times10^{-13},
\]

rather than confusing the strict \(2\times10^{-13}\) acceptance limit with a default value. This fixes a fail-condition bug caught during integration.

## Important implementation boundary
The verifier deliberately aborts until two certified backends are connected:

1. a scalar-data provider for the diagonal and unified generator sequence \(Z_n\), with the v13.338–v13.343 rational/transcendental enclosures;
2. a 512-bit point / 1024-bit outward-rounded local replay backend.

This is now the only missing finite-block implementation layer. The spectral target, structured LDL recurrence, local defect theorem, global residual composition, factor-growth streaming statistics, and numerical pivot margins are already separated from it.

## Why fail-closed matters
The program cannot accidentally turn midpoint data into a theorem. Until the certified data and replay backends are present, it raises an explicit runtime error instead of emitting PASS.

## Current proof chain after this checkpoint
A completed run satisfying the transcript inequalities would certify

\[
A_{0,[21,16001]}\succeq0.22I.
\]

Together with the still-to-be-interval-certified cross target

\[
\|A_{0,[21,16001],[16003,\infty)}\|<1
\]

and analytic tail target

\[
A_{0,[16003,\infty)}\succeq4.673\,I,
\]

this would yield the full high-complement lower margin

\[
0.22-\frac1{4.673}>0.006.
\]

Only after the entire high complement is certified positive may the infinite inertia problem be reduced to the ten low modes via the exact Schur complement.

## Guardrail
v13.361 is an executable verifier boundary, not the completed 7991-step validated run. The high complement is not yet certified positive, and no RH/GRH conclusion follows.
