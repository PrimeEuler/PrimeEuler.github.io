# Cone Derivation Ledger v13.527 — M16001 Entrywise Primitive Residual Propagation

Date: 2026-09-16

Status: **[N-cert arithmetic-stage] / [Audit]**; fail-closed remainder; no theorem promotion.

## 0. Synchronization

Live repository head was checked at start and again immediately before this numbered write. v13.526 is the latest numbered ledger entry; v13.527 is free. The arithmetic helpers were merged at `3e77d036167265eaad5ac92da52790451708a02f` after successful GitHub Actions execution.

## 1. Pole-FC primitive formation

The executable primitive transcript over all 79,910 FC entries gives

\[
\rho_{\rm pole}\le 1.9322245000793252\times10^{-20},
\]

and the subsequent addition into `A0_FC` contributes at most

\[
1.937913948121446246\times10^{-20}.
\]

Combining these with the audited v13.521 FC displacement radius gives the conservative per-entry FC arithmetic radius

\[
\boxed{\rho_{FC}\le5.235060947742494145\times10^{-19}}.
\]

## 2. Why the uniform FF maximum is unusable

A first conservative propagation used the global v13.521 maximum

\[
\rho_{FF}^{\max}=9.022982959826541\times10^{-16}
\]

for every FF entry. With

\[
\max_r\sum_j|X_{jr}|=6.771795643970706864,
\]

this gives a residual-entry increment as large as `6.110703176392302837e-15` and a Frobenius increment

\[
9.137545268291809376\times10^{-13}.
\]

This is valid as a coarse guard but far too pessimistic for the seven-plane margin. It must not be used as evidence that the margin is lost, because the worst primitive displacement radius is highly localized and is not representative of all 63.8M FF entries.

## 3. Entrywise-weighted propagation

New helper

`research-notes/suzuki_M16001_displacement_weighted_residual_radius.py`

recomputes the same primitive v13.521 roundoff formula row-by-row for every FF coefficient and contracts the actual radius with the actual solve payload:

\[
E_{ir}^{FF}=\sum_{j\ne i}\rho_{ij}^{FF}|X_{jr}|.
\]

No observed double/long-double discrepancy, fitted factor, or manual safety multiplier is used. The reduction itself is charged with `gamma_7991`, and the final 79,910-term square/sum/sqrt endpoint is outward charged.

The independent CI replay reproduced the v13.521 maximum exactly:

\[
\max_{i\ne j}\rho_{ij}^{FF}
=9.022982959826540786\times10^{-16}.
\]

But after actual entrywise weighting the largest residual-entry primitive increment is only

\[
1.2017055003645024938\times10^{-18},
\]

and the complete known-primitive Frobenius increment is

\[
\boxed{
\|E_{\rm known\ primitive}\|_F
\le1.5659242855578671182\times10^{-16}.
}
\]

Thus the apparent `9.14e-13` obstruction from the uniform-max guard collapses by roughly four orders of magnitude when the already-certified entrywise radii are propagated according to their actual locations.

## 4. Reproducibility observation

The same CI run re-executed the v13.526 integrated residual stage and obtained an arithmetic-stage endpoint `9.550294946230173122e-15`, versus `9.582335208983397532e-15` in the preceding CI execution. This small run-to-run/environment/payload change is not promoted or averaged away. It reinforces that the `X` payload/provenance gate must be closed explicitly rather than treating a particular computed solve payload as exact.

## 5. Fail-closed remainder

The primitive residual chain is **not yet theorem-consumable**. The remaining explicit gates are:

- `diag_payload_conversion`;
- `source_payload_conversion` for nominal `Z,c,pi` at the arithmetic interface;
- `X_payload_conversion` / reproducible solve-payload provenance.

The Frobenius square/sum/sqrt stage is closed by v13.526, and off-diagonal FF/FC plus pole-FC primitive formation are now propagated entrywise rather than through a global maximum.

Certified inertia therefore remains

\[
\boxed{\operatorname{ind}_{\le0}(A_{\rm even}(1))\le4},\qquad
\boxed{\operatorname{ind}_{\le0}(A_{a=1})\le6}.
\]

No RH/GRH, exact-zero, or kernel-multiplicity conclusion is made.
