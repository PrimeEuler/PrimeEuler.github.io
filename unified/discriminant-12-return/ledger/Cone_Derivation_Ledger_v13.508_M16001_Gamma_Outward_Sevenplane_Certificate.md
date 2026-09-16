# Cone Derivation Ledger v13.508 — M16001 Gamma-n Outward Seven-Plane Certificate

Date: 2026-09-16

Status: **[N-cert]** outward numerical certificate; **[D]** inertia consequence; **[Audit]** guardrails.

## 0. Synchronization [Audit]

The live ledger was checked at the start and again immediately before this write. v13.507 was the newest numbered entry; the M16001 gamma helper commits `2fff6e10...` and `419f1c8d...` landed afterward. Thus v13.508 was free.

## 1. Shifted nominal setup [D]

As in v13.477, use the certified operator enclosure

\[
A_{\rm exact}\succeq A_{\rm nom}-2\times10^{-13}I.
\]

It is therefore enough to certify a seven-dimensional positive subspace for the shifted nominal operator. The M16001 split is C={1,3,...,19}, F={21,23,...,16001}, T={16003,16005,...}.

The midpoint anisotropic replay is

\[
\lambda_Q=0.6777335772034006,
\quad \|B_{QN}\|=2.6759323085395717\times10^{-7},
\]
\[
a_N=9.221503119690585\times10^{-13},
\quad m_{7,\rm mid}=8.164950226231554\times10^{-13}.
\]

## 2. 7991-dimensional solve and finite Schur [N-cert]

The M3999 residual-plus-gamma_n method was ported directly. With long-double unit roundoff `u=5.421010862427522e-20`,

\[
\gamma_{7991}=4.331929780165835\times10^{-16}.
\]

The explicit shifted finite solve gives residual Frobenius norm

\[
6.953589059005369\times10^{-15},
\]

and the gamma-dot envelope contributes

\[
2.135044237583902\times10^{-15}.
\]

Thus the fail-closed total residual is

\[
\boxed{\|R_F\|_F<9.08863329658927\times10^{-15}}.
\]

After coercivity propagation and Schur-formation rounding, the normalized block radii are rounded upward to

- QQ: `<2.0e-8`,
- QN: `<7.0e-13`,
- NN: `<1.0e-16`.

The large QQ radius is caused by the normalization through the small first diagonal of L0; it is harmless because the Q block has O(1) coercive margin. The NN radius is the relevant scalar charge.

## 3. Remote Gram and far tail [N-cert]

For `16003 <= n <= 2,000,000`, the explicit inverse-power residual rows were accumulated in chunks with long-double `R^T R` products. The direct double/long-double Gram discrepancies were approximately

- QQ: `9.67e-18`,
- QN: `3.84e-23`,
- NN: `1.64e-29`.

The outward envelopes are deliberately enlarged to include gamma_n chunk accumulation, inverse-power moment formation, and propagation of the finite-solve residual into `W=[Basis;-X Basis]`:

- QQ remote Gram radius `<1e-10`,
- QN remote Gram radius `<1e-16`,
- NN remote Gram radius `<1e-20`.

For the analytic tail beyond 2,000,000, the midpoint block bounds are

\[
f_Q=4.706301536488523\times10^{-4},\qquad
f_N=1.2657888576676901\times10^{-15}.
\]

The direct double/long-double difference in `f_N` is below `9e-26`. After gamma_8001 moment accounting and the W-perturbation allowance, the far-tail Gram radii are again conservatively taken as QQ `<1e-10`, QN `<1e-16`, NN `<1e-20`.

The shifted remote coercivity floor is

\[
\delta_{\rm remote,shift}=0.18212727272298945.
\]

## 4. Final outward seven-plane Schur complement [N-cert]

Combining finite, remote, and far-tail arithmetic radii gives total normalized charges

\[
\varepsilon_Q<2.1098133174\times10^{-8},
\]
\[
\varepsilon_{QN}<7.0109813318\times10^{-13},
\]
\[
\varepsilon_N<1.0010981332\times10^{-16}.
\]

Therefore

\[
\lambda_Q^{\rm cert}>0.6777335566488433,
\]

\[
\|B_{QN}\|^{\rm cert}<2.675939309143546\times10^{-7},
\]

and

\[
a_N^{\rm cert}>9.220502021557411\times10^{-13}.
\]

Using the block Schur criterion,

\[
m_7^{\rm cert}
=a_N^{\rm cert}-\frac{\|B_{QN}\|_{\rm cert}^2}{\lambda_Q^{\rm cert}}
>\boxed{8.1639435588\times10^{-13}}>0.
\]

Thus the shifted nominal operator is positive on an exact seven-dimensional subspace. By the certified operator ordering, the exact even Suzuki operator has at most three nonpositive directions:

\[
\boxed{\operatorname{ind}_{\le0}(A_{\rm even}(1))\le3}.
\]

This is a theorem-level promotion from the previous certified bound `<=4`.

## 5. Consequence and guardrails [D/Audit]

Together with the unchanged certified odd-sector bound

\[
\operatorname{ind}_{\le0}(A_{\rm odd}(1))\le2,
\]

the full parity bound improves to

\[
\boxed{\operatorname{ind}_{\le0}(A_{a=1})\le5},
\]

equivalently the sixth eigenvalue is strictly positive.

This does not identify the remaining five directions as exact kernels and gives no exact-zero, RH, or GRH conclusion.

Executable arithmetic transcript: `research-notes/suzuki_M16001_gamma_outward_sevenplane_certificate.py`, latest helper commit `419f1c8d07d397c4e2b7931f4bee5c6ca74a2efc`.