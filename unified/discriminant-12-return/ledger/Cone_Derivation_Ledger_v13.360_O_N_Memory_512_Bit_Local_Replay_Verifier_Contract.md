# Cone Derivation Ledger v13.360
## O(N)-Memory 512-Bit Local Replay Verifier Contract

### Purpose
This checkpoint converts the v13.359 local-defect identity into a practical streaming proof implementation for the shifted pole-free high block

\[
B=A_{0,[21,16001]}-0.22I,
\]

of dimension 7991.

The desired theorem remains

\[
B\succ0.
\]

The established a-posteriori sufficient residual allowance is approximately

\[
\|B-LDL^T\|_2<3.15\times10^{-6}.
\]

### No dense factor storage is required
At each generator-LDL step only the current multiplier column \(\ell_k\) is produced.

Maintain a persistent row accumulator

\[
r_i\leftarrow r_i+|\ell_{ik}|.
\]

The current absolute column sum is

\[
c_k=1+\sum_i|\ell_{ik}|.
\]

At the end,

\[
\boxed{
\||L|\|_\infty=\max_i(1+r_i)
}
\]

and

\[
\boxed{
\||L|\|_1=\max_k c_k.
}
\]

Therefore the factor-growth part of the residual certificate costs only \(O(N)\) memory.

### Two-precision replay
Recommended implementation:

- factorization state: 512-bit MPFR point arithmetic, round to nearest;
- checker state: 768–1024 bits with outward rounding or ball arithmetic;
- every stored 512-bit point number is interpreted by the checker as an exact dyadic input.

At each step the checker reconstructs the exact Schur quantities associated with the current stored point state,

\[
b_*,\ \ell_*,\ d_*',\ u_*',\ v_*',
\]

compares them with the next stored point state, and evaluates the v13.359 local Frobenius defect enclosure

\[
\delta_k\ge\|\Delta_k\|_F.
\]

The verifier accumulates only

\[
S_\Delta=\sum_k\delta_k.
\]

### Final residual inequality
By the exact global residual composition from v13.359,

\[
\|E_{\rm arith}\|_2
\le
\||L|\|_1\||L|\|_\infty S_\Delta.
\]

Thus define

\[
\boxed{
E_{\rm arith}^{\rm bd}
=
\||L|\|_1\||L|\|_\infty S_\Delta.
}
\]

A successful run should verify

\[
\boxed{\min_j d_j>0.25}
\]

and

\[
\boxed{E_{\rm arith}^{\rm bd}<10^{-8}}.
\]

The exact-vs-nominal matrix uncertainty is targeted at

\[
\boxed{E_{\rm matrix}^{\rm bd}<2\times10^{-13}}.
\]

The final check is

\[
\boxed{
E_{\rm arith}^{\rm bd}+E_{\rm matrix}^{\rm bd}
<3.15\times10^{-6}.
}
\]

If all inequalities are validated, then the v13.356 a-posteriori theorem yields

\[
B\succ0.
\]

### Compact proof transcript
The proof object need contain only:

1. dimension;
2. factor precision;
3. checker precision;
4. minimum pivot and its mode;
5. \(\||L|\|_1\);
6. \(\||L|\|_\infty\);
7. \(S_\Delta\);
8. arithmetic residual bound;
9. matrix uncertainty bound;
10. total residual bound;
11. pass/fail.

No dense \(7991\times7991\) factor and no dense residual matrix need be stored.

### Complexity
The structured factorization and local replay remain

\[
O(N^2)\text{ arithmetic},\qquad O(N)\text{ storage}.
\]

This is practical for \(N=7991\) and avoids the interval dependency explosion seen in direct interval Schur propagation.

### Guardrail
This checkpoint specifies the final streaming verifier contract. The full directed-rounded 7991-step replay has **not yet** been run, so finite high-block positivity, full high-complement positivity, exact zero modes, RH, or GRH are not claimed here.

### Next target
Execute the full two-precision replay and record the compact certificate transcript. If it passes, the finite high-block part of the global high-complement proof closes; the remaining global step is then the independently targeted cross-norm/tail Schur certificate at the \(N=16003\) split.
