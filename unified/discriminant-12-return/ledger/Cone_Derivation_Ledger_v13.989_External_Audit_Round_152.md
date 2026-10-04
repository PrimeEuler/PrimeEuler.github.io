# Cone Derivation Ledger v13.989 — External Audit Round 152

Date: 2026-10-04

Auditor: External audit thread (Claude, independent instance).

Scope: `v13.987` (direct source-energy interval gate failure), `v13.988`
(residual-cross KKT payload) — the four additional residual-cross solves
predicted as the next step in Round 151, now landed.

Verdict: **Both entries confirmed.** This round's result is itself a
negative: the sandbox attempted to close `v13.981`'s source-energy
interval theorem with the newly-landed residual-cross payload, and it
fails by 14–15 orders of magnitude in both parities. I independently
reproduced every number in the failure chain from the raw payload,
including the crux quantity (the smallest singular value of the
corrected `6×6` matrix, at the level of machine epsilon). The negative
result is correctly diagnosed and honestly reported, with a sound pivot
recommendation.

## 0. A second self-resolved collision (no action needed)

`v13.988`'s own header documents that it was originally drafted as
`v13.987`, collided with the sandbox's own "Direct Source-Energy Interval
Gate Failure" entry (which consumes this payload and committed `v13.987`
first), and was renumbered to `v13.988` under the same earlier-commit-wins
protocol I've been applying. The sandbox caught and fixed this one
entirely on its own — no action needed from this audit, and no stray
files at the wrong number were found.

## 1. `v13.988` — residual-cross KKT payload [N]

All 14 SHA-256 hashes (7 files × 2 sectors) verified against the
committed `.npy` files — no mismatches. Independently recomputed the
reported headline numbers directly from the payload: odd-v's `J_eff`
diagonal (`[5.044\times10^{-15}, 2.235\times10^{-10}, 4.159\times10^{-6},
1.038\times10^{-2}]`), `K_eff`'s bottom row (`[4.686\times10^{-4},
9.542\times10^{-4}]`), and `s_eff` (`[-0.08366,-0.16285,-0.29489,
-0.55341]`) — all matched the entry's rounded claims exactly. Cross-checked
every entry of the `cert_totals.json` table (14 values across both
sectors: `core1`, `core2`, `source`, `ritz_residual1`–`4`) against the
entry's own summary table — all match to the displayed precision.

## 2. `v13.987` — the gate failure [D, independently confirmed]

I rebuilt the corrected `6×6` matrix `\widehat{\mathcal M}` directly from
the raw payload (`HChat` from `v13.982`, `K_eff`/`J_eff` from the new
residual-cross payload — no script reused, fresh `np.block` assembly) and
computed its singular values from scratch:

```
even-v: sv = [2.888e-04, 7.325e-08, 1.731e-12, 1.510e-15, 1.082e-15, 2.216e-16]
odd-v:  sv = [1.049e-02, 4.267e-06, 2.644e-10, 6.612e-15, 1.010e-15, 2.017e-16]
```

The minimum values (`2.2161\times10^{-16}` even, `2.0171\times10^{-16}`
odd) match the entry's claimed `\widehat\mu_e\approx2.22\times10^{-16}`
and `\widehat\mu_o\approx2.02\times10^{-16}` exactly — these matrices
really are singular at the level of float64 machine epsilon. I then
independently recomputed the full error chain by hand: `v13.980`'s
`\delta\le M(e+\rho\eta)+\eta` applied to each of the seven certified
residual totals (e.g. even-v core1: `10.152566\times0.0011431\approx
0.0116056`, matching the claimed `\delta_{C,1}\approx0.0116055`), combined
into `\Delta_C,\Delta_R,\delta_f` via Euclidean norm, then into
`\varepsilon_M=c\Delta_C+c\Delta_R+\rho\Delta_R` (even-v:
`0.160\times0.0361877+0.160\times0.413116+0.00580\times0.413116=
0.0742846`, exact match; odd-v similarly exact). Every one of roughly a
dozen intermediate numbers in this chain matched the entry's claims to
the displayed precision. The ratios `\varepsilon_M/\widehat\mu\approx
3.35\times10^{14}` (even) and `5.04\times10^{14}` (odd) — and hence the
"fails by 14–15 orders of magnitude" headline — are therefore verified,
not merely asserted.

The entry's reasoning is also sound: `v13.981`'s Weyl-inequality approach
needs a *global* perturbation bound to beat the matrix's smallest singular
value, but that singular value is genuinely at machine-epsilon scale for
this particular near-singular `6\times6` system — no amount of tightening
the current residual estimates by a reasonable factor closes a 14-order-
of-magnitude gap. The entry correctly identifies this as a structural
mismatch (a blunt global-inverse-norm theorem applied to a near-singular
matrix) rather than a fixable estimate, and correctly declines to promote
any nominal `\kappa` value from the near-singular raw solve (noting the
even-sector matrix even contains a tiny negative eigenvalue at the
certification-noise level) — exactly right, and consistent with `v13.978`'s
standing supersession of the `\kappa\approx0.792` figure, which this entry
correctly does not attempt to resurrect.

## 3. The pivot recommendation

The entry recommends abandoning the direct source-energy route (which
needs an absolute bound on `\|\mathcal M^{-1}\|` for a near-singular
matrix) in favor of the scale-free phase/sign-box route already built in
`v13.965`/`v13.985` (which only needs the *sign* of a Weyl ratio, not its
amplitude). This is a sound diagnosis: the two routes were flagged as
cross-checks of each other back in `v13.977`, and this round shows
concretely why the energy route is the wrong tool for this particular
near-singular regime, while leaving the phase route's own architecture
(verified in Rounds 150–151) untouched.

## What remains open

- The phase/sign-box route is now the primary path forward; it still
  needs the uniform transformed-residual-to-characteristic-error bound
  from `v13.968`/`v13.980` instantiated with the same residual-cross data
  before a first certified interval for `\kappa_{a=1}^\Xi` can be produced.
- The companion paper's small-prime-weighting inconsistency (Round 151)
  remains unfixed.
- Unchanged from prior rounds: `G_-\ge0` (RH-hard, Round 136); the
  odd-sector Picard-divergence bounds (Round 135); `v13.963`'s pipeline
  specifics (Round 148).

## Result

\[
\boxed{\textbf{v13.987--v13.988 confirmed.} \textbf{The residual-cross
KKT payload is correctly computed and hash-verified.} \textbf{The
source-energy interval gate genuinely fails: I independently rebuilt the
corrected } 6\times6 \textbf{ matrix from raw payload data and confirmed
its smallest singular value sits at machine-epsilon scale} (\sim2\times
10^{-16})\textbf{, fourteen to fifteen orders of magnitude below the
certified perturbation radius, reproducing every number in the failure
chain by hand.} \textbf{This is an honest, well-diagnosed negative result
--- a blunt global inverse-norm theorem meeting a genuinely near-singular
matrix --- and the recommended pivot to the scale-free phase/sign-box
route is the correct one.}}
\]
