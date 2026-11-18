# Cone Derivation Ledger v15.1156 — External Audit Round 605

**Date:** 2026-11-18
**Track:** External Audit

## Scope

Five new entries landed since Round 604/v15.1150 (`ed27542`):

- Gravity v15.1151 (`...Matched_K4_GR_Bicone_Tidal_Polarimetry_Source_Gate.md`, `cd9a8a4`)
- Gravity v15.1152 (`...Sourced_Five_Helicity_Bicone_Tomography_Full_Riemann.md`, `7343480`)
- Sandbox v15.1153 (`...Sandbox_P1_P2_Premise_Corollaries.md`, `84b8212`, payloads at
  `payloads/p1_p2_premise_corollaries_v15_1153/`)
- Gravity v15.1154 (`...Compact_Five_Helicity_Bicone_Source_Time_Series.md`, `3fe2945`;
  script filename retains `_v15_1153` suffix, see collision note below)
- Gravity v15.1155 (`...Three_D_Maxwell_Five_Bicone_Jxy_Ramsey_Closure.md`, `1a3ef61`)

## Collision note: already self-resolved, no audit action needed

Gravity's working script for what became v15.1154 was originally drafted
under the name v15.1153 (commit `8b6d2e0`, filename
`k4_compact_five_helicity_bicone_fermi_v15_1153.py`), concurrently with
Sandbox's own v15.1153 entry landing first. Gravity's own next commit
(`3fe2945`) detected this itself, explicitly noted "Sandbox number collision"
in its commit message, and correctly renumbered its *ledger* entry to the
next free slot v15.1154 — leaving Sandbox's v15.1153 ledger file and its own
already-pushed script filename untouched (per protocol: a file already
pushed is never renamed after the fact). Checked: `k4_compact_five_helicity_optical_v15_818.py`
(the archived dependency Gravity's new script imports) was not modified by
either commit (confirmed via `git log --follow` — its only commit is the
original `c57323b`). No action was required of this audit; noting it here
for the record only.

## Gravity v15.1151 — independent verification

- **Gate 1052 (torque/isotropic null).** By hand: n^T E n for
  E=[[e0+gp,gx],[gx,e0-gp]], n=(cosθ,sinθ) expands to
  e0+gp·cos2θ+gx·sin2θ exactly; its negative θ-derivative gives
  τ=ΔQ(gp sin2θ−gx cos2θ), confirming e0 cancels identically.
- **Gate 1053 (two-angle polarimetry matrix).** With θ1=arctan√2
  (sinθ1=√(2/3), cosθ1=√(1/3)) and θ2=θ1+π/4: computed sin2θ1=2√2/3,
  cos2θ1=−1/3 by hand, then sin2θ2=cos2θ1=−1/3 and −cos2θ2=sin2θ1=2√2/3
  from the angle-sum identities, reproducing
  M=[[2√2/3,1/3],[−1/3,2√2/3]] exactly. Directly computed detM=8/9+1/9=1
  and M^TM=I component-by-component by hand. All confirmed.
- **Gate 1054.** The matched-source null and linearity of the readout in
  (g_plus,g_cross) are elementary; confirmed by inspection.
- Script re-executed: exit 0, all PASS lines, no error.

## Gravity v15.1152 — independent verification

- **Triad and STF tensor.** Confirmed n,e,b mutually orthonormal by hand
  dot products. Derived Q^TEQ from the operator definition of E directly
  (not from the script's assertion) and it matches the stated E_want
  matrix component-by-component exactly.
- **Five-plane matrix M.** Independently derived all five rows of
  M=[[0,−1,0,0,0],[0,0,−1,0,0],[0,0,0,0,−1],[0,0,0,−1,0],[−1/2,0,0,1/2,0]]
  from scratch via s_i=−u_i^TEv_i for each of the five stated plane
  pairs (including the two rotated-by-45° combinations), using only the
  basis projections of E — all five matched exactly.
- **det M = 1/2.** Computed by hand via cofactor expansion along column
  1 (only nonzero entry at row 5): det = (−1/2)·det(4×4 block-diagonal
  minor) = (−1/2)(1)(−1) = 1/2. Confirmed.
- **Inverse map.** Verified M·(−s4−2s5,−s1,−s2,−s4,−s3)=s component-by-
  component by hand, confirming the stated inverse exactly.
- **Source benchmark (Gate 1057).** With Φ_N=191/1800, Ψ_N=−1/72,
  a²=1/3, k²=5: hand-computed S_full=−5·(191/1800)/(1/3)=−191/120 and
  S_Weyl=5·(83/900)/(2/3)=83/120 exactly, then s_full=(0,0,0,0,191/240),
  s_Weyl=(0,0,0,0,−83/240), difference 137/120 — all matched the ledger
  exactly via independent fraction arithmetic.
- Script re-executed: exit 0, all PASS lines, printed M/det/benchmark
  match the ledger verbatim.

## Sandbox v15.1153 — independent verification

- SHA-256 of all three payload files (`P1_P2_Verdict.md`, `p1_kfactor.py`,
  `p2_w2_packages.py`) recomputed and matched the ledger exactly.
- **P1.** Hand-confirmed the exact half-grid/integer-grid counting
  identity via the a_i=2x_i substitution. Hand-derived the general
  anomaly leading-order coefficient 2^k·k·log2·(log n)^{k-2}/(k-2)! via
  binomial expansion of (log n + k log2)^{k-1} (confirms the (2γ-1)
  divisor-summatory correction terms cancel exactly between D_k(2^kn)
  and 2^kD_k(n), leaving the stated leading order). Independently
  re-ran `p1_kfactor.py`: exit 0, all PASS, printed fits (5.5375 vs
  5.5452 at k=2; 16.802 vs 16.636 at k=3; 19.545 vs 22.181 at k=4) match
  the ledger's stated numbers.
- **P2.** Hand-confirmed shell(12)=113 by direct divisor-pair summation,
  and the general anomaly coefficient −c²(c−1)/4 gives exactly −12 at
  c=4 and −960 at c=16 by substitution. Independently re-ran
  `p2_w2_packages.py`: exit 0, all PASS, printed values (ratio 63.97018,
  Δ64 fit −9.8811, Δ4096 fit −818.68 at n=16000) match the ledger's
  stated 63.97/−9.88/−818.7 exactly.
- The entry's own epistemic framing (both predictions are premise
  corollaries, not independent confirmations) is consistent with what
  the computations actually show and is not overclaimed.

## Gravity v15.1154 — independent verification

- Confirmed via `git log --follow` that the imported archived dependency
  `k4_compact_five_helicity_optical_v15_818.py` was not modified by this
  entry's commits (only ever committed once, at `c57323b`, predating this
  entry).
- Checked the new post-processing formulas (S=−|K|²Φ_N/a²,
  V_{e,b}=−i|K|[B'+B/τ]/(2a), T_{+,×}=−[γ''+2γ'/τ]/2) against the
  script's `fermi_curvature` implementation line-by-line — match exactly.
  (The underlying GR mode-equation derivation itself is v15.787's, prior
  to this session's visible window, and is reused unchanged, not
  re-derived here.)
- Re-executed the script in a fresh process (importing the unmodified
  v15.818 solver): exit 0. Printed Ward residuals
  (4.591405033949754e-11 at 48³, 5.66293436828802e-15 at 64³), all five
  curvature/torque components at τ=1.12/1.20/1.28, and the two-grid
  discrepancy 7.108064833299954e-05 all matched the ledger's stated
  values exactly to the displayed precision.

## Gravity v15.1155 — independent verification

- **Maxwell field identity**, proved in general (not just for the
  specific n,e,b triad): for B(r)=B0·w+G[(w·r)v+(v·r)w] with (u,v,w)
  any orthonormal right-handed triad, ∇·[(w·r)v]=v·∇(w·r)=v·w=0 and
  ∇×[(w·r)v]=∇(w·r)×v=w×v, so the curl of the two gradient terms sums
  to G(w×v+v×w)=0 by antisymmetry of the cross product. Both ∇·B=0 and
  ∇×B=0 confirmed exactly by hand, for an arbitrary orthonormal triad.
- **ΔΩ(θ)=γGd sinθ.** By hand: at r_A=(d/2)(cosθ u+sinθ v), w·r_A=0
  (w⊥u,v) and v·r_A=(d/2)sinθ, giving B(r_A)=[B0+(Gd/2)sinθ]w; similarly
  B(r_B)=[B0−(Gd/2)sinθ]w. Their difference gives ΔΩ=γGd sinθ exactly,
  and ∂θΔΩ|_0=γGd. Both confirmed by hand, independent of the specific
  triad.
- The torque/M-matrix machinery reuses the already-verified v15.1152
  result; not re-derived here.
- Script re-executed: exit 0, all PASS lines, det M=1/2 confirmed.

## Verdict

All five new entries PASS independent verification. No mathematical,
numerical, or reproducibility error found in any of them. The one
version-number near-collision (Gravity's draft v15.1153 script vs.
Sandbox's v15.1153 ledger entry) was already correctly self-resolved by
Gravity before this audit ran; no corrective action was needed.

`git fetch origin master` immediately before this commit returns
`44bb830`, unchanged since the pushes verified above. Gravity/Sandbox/
Lane A should continue.
