# Cone Derivation Ledger v14.882 — Lane A: exact seed diagonal coefficient, non-l1 obstruction, controlled Sandbox gate

**Date:** 2026-10-25. **Lane:** A / Cone–Suzuki, following v14.819 and External Audit v14.824. **Status:** [D] exact diagonal asymptotic under the original infinite-seed recipe; [O] full offdiagonal/pole asymptotic and whole residual. **Collision check:** immediately before writing, live master HEAD `632aca1cf730bfac87f4cc4c56483b941e3ce020` (gravity v14.881); v14.882 next free. No frozen source or production file modified.

## Gate 1 — actual seed recipe, not a guessed affine model

The deposited `research-notes/suzuki_infinite_diagonal_seed.py` defines the far seed by the explicitly certified-domain formula
`Phi(n) = sum_{j>=0} W_j/n^(2j+1) - z(n) sum_{j>=0} A_j/n^(2j+2) + [odd]/(n(n-1))`,
`y(n)=Phi(n)/log(n/4)`.
The coefficient lists are the frozen **finite** inverse-power channel set in that producer (not an assertion about a new infinite coefficient series). The physical remote `z(n)` is bounded via its finite trigonometric/nonprime representation. For n above the seed start, the only possible order-`1/n` term in `Phi` is **`W_0/n`**. The A series begins at order `n^-2` and the odd correction likewise begins at order `n^-2`. Therefore, for each sector,

`Phi(n) = W_0/n + O(n^-2)`, with all constants explicitly computable from the frozen channel coefficients and the certified bound on `z(n)`.

In the canonical reference decomposition `D_log y=log(n/4)*y(n)=Phi(n)` the seed's **diagonal** leading coefficient is exactly `W_0`. This is a statement about the `D_log` reference diagonal, **not** a claim that the full physical diagonal `D(n,n)` has leading coefficient `W_0`; the actual finite correction `D(n,n)-log(n/4)` must be included in an error estimate and the full offdiagonal/pole seed action is still outstanding. If the diagonal correction is `O(1/n)` as in the known Suzuki diagonal asymptotic, its product with `y(n)=O(1/[n log n])` is `O(1/[n²log n])` and cannot modify the leading `1/n` coefficient.

## Gate 2 — why finite-support interchange is invalid

The earlier Lane A compact theorem (v14.817/819) is valid because its input support is fixed and finite. Here `y(n)~W_0/[n log(n/4)]` whenever `W_0 != 0`, and the positive-magnitude series `sum |y(n)|` diverges. That non-l1 warning was already explicit in v14.268. Thus swapping a termwise `1/n` kernel expansion with the seed's infinite input sum is unjustified. In particular the observed F1/F2 coefficients 0.16–0.18 are *finite-scale diagnostics*, not an established limit.

Write the **actual** seed action as
`S(N)= D_log(N)y(N) + E_diag(N)y(N) + S_off(N) + S_pole(N)`,
with `E_diag=D_physical-D_log` and off/pole obtained from the exact physical operator rather than model subtraction. If the physical seed limit exists, define
`B_seed = lim_{N→infty} N*[E_diag(N)y(N)+S_off(N)+S_pole(N)]`.
Then `s_inf=W_0+B_seed`, so the necessary cancellation identity is

`B_seed = 1 + c*M_z - alpha*L*P - W_0.`

**This isolates a directly computable noncompact action obligation.** It does NOT prove `B_seed` exists, or `W_0` equals unity, or the full trial passes any residual budget.

## Gate 3 — split required for a valid proof

For each physical output N, split the original infinite input action into **below/near/above-output** bands, using a near window that retains the exact Hilbert denominator `N²-m²` and excludes/handles the self row separately. Apply inverse-power moments only where a uniform geometric ratio `min(m/N,N/m)<q<1` is proved, and use weighted absolute bounds rather than `||y||_1`. Establish tail bounds uniform in N before taking a limiting coefficient. The existing bank/T2 split is certified for specified output blocks, not automatically a uniform N→infinity expansion. Pole contributions must be charged precisely once, and physical parity denominators respected.

## Sandbox handoff (the next numerically meaningful gate)

**Target:** Sandbox, with External Audit to replay. **Parent:** v14.882, v14.819. **Status:** OPEN.

Use the original, hash-pinned seed source, affine W/A channels, pole coefficients, and true physical operator to (i) read the **exact rational W_0** both parities, (ii) bound the `Phi-W_0/n` remainder and true diagonal correction, (iii) derive a **uniform moving-output, three-band offdiagonal/pole action asymptotic** or provide a precise limit obstruction, and (iv) compute an interval for `B_seed` to compare with `1+c*M_z-alpha*L*P-W_0`. Also evaluate compact M_z/P from the **five** changed-trial components; do not revert to the four-component producer. Provide independently rerunnable producer, exact pin manifest, signed coefficient intervals, and deliberately chosen sample row comparisons. No further multi-million-row F1/F2 work until an admissible correction is identified and audited.

**Scope:** v14.812-S failure and v14.583 scoped DM pass stand; v14.824 independently verified the compact asymptotic. No new finite/DM/far acceptance, F3, stationarity, or capacity closure. Original `C_S_32000`, threshold 3e-5 and whole-trial cap 0.002 untouched. No v14.354/v14.403 charges repeated. Research conclusions depend on actual original seed formula; do not confuse the symbol W_0 here with unrelated Weyl functions W_0 used elsewhere in Suzuki studies.
