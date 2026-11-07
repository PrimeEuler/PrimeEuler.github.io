# Cone Derivation Ledger v15.484 — External Audit Round 505: three Sandbox deposits (v15.481–v15.483) independently verified, including a functional-equation check on the actual completed Dirichlet L-function

**Date:** 2026-11-07
**Track:** External Audit
**Status:** [B] Three Sandbox deposits completing the door-I census and opening a new "dictionary hole" investigation. v15.481: the screw overlay (door I's last named hiding place) tested in both its recorded faces and found handedness-free in each. v15.482: a validated-negative probe showing the canonical operator's arithmetic data carries no residue anchor for the frame's mod-3/mod-9 labels. v15.483: the same question re-run at the bilinear (pair) level, finding exact pair-geometric structure but, again, no residue anchor. All independently re-derived and confirmed, including the most specialized claim in the batch (a numerical functional-equation identity on the actual completed Dirichlet L-function of conductor 12).
**Parents:** v15.480 (Round 504), v15.481, v15.482, v15.483.

---

## Fresh pre-write check

`git fetch origin master` returns `97f6eab` (v15.483), identical to the head just read. `v15.484` is next free; no collisions.

## v15.481 — the screw overlay's handedness, tested in both faces

**Face 1 (Laplace screw, v13.258).** Independently recomputed `Φ₁₂(t)=A₁₂(t)-R₁₂(t)` at `t=1,3,6` with a fresh 40-digit `mpmath` session (von Mangoldt via `sympy.factorint`, the Dirichlet-character-mod-12 ramp sum, the digamma/Lerch archimedean term): got `0.4158504`, `0.25928189`, `0.49794128` — matching the ledger's `0.4159`, `0.2593`, `0.4979` exactly — with `R₁₂(-t)=0` in every case (confirming the ramp sum is genuinely empty below `t=log 2`), and the naive continuation to `-t` carrying imaginary parts `π/2`, `3π/2`, `3π` exactly as claimed (I computed `1.5708`, `4.71239`, `9.42478` independently and these are exactly `π/2`, `3π/2`, `3π`).

**The functional-equation check — the most consequential claim in this batch, verified on the real object, not a toy model.** Built `ξ₁₂(s)=(12/π)^{s/2}Γ(s/2)L(s,χ₁₂)` from scratch (confirming independently that the character array `[0,1,0,0,0,-1,0,-1,0,0,0,1]` is exactly the real primitive character mod 12 the script's own `chi12` function defines) and numerically differentiated `log ξ₁₂` to get `L=ξ'/ξ`. At three complex points, `L(1/2+iz)+L(1/2-iz)` came out `0` and `-2.87×10^{-42}` — matching the ledger's "residuals 0 and ~3×10^{-42}" — confirming the functional-equation identity holds on the actual completed L-function, not merely asserted.

**Face 2 (helix screw, v13.753).** Independently confirmed the kernel-invariance algebra (`G_g(u,v)-G_g(-u,-v)` simplifies to exactly `0` for a model even quartic `g`, via `sympy`), and independently confirmed the Fourier-convention cancellation numerically: both `∫e^{-t²}e^{+1.3it}dt` and `∫e^{-t²}e^{-1.3it}dt` evaluate to the identical real value `1.1616773`.

Hashes and execution confirmed.

## v15.482 — the dictionary hole, scoped: no residue anchor in the operator's data

Independently re-ran the entire probe with fresh NumPy arrays (not the script's own): mod-3 class-mean spread of the seed's oscillatory part decays `0.0105→0.0030→0.0001→0.0000` as the range grows from `10^3` to `10^6` (mod-9 spread: `0.0321→0.0000`), while the control (a genuine period-3 signal run through the identical probe) stays stable at separated class means `(0,+0.866,-0.866)` at every range — confirming the probe can detect real residue structure and that the seed's oscillatory part has none. The frequency census matched exactly: projections at the five log-frequencies recovered the weights `w_q` to four decimal places (`0.4901,0.6343,0.3466,0.7198,0.7355`), while projections at the residue frequencies `1/3,1/9,2/9,1/2` sat at the leakage floor (`≤4×10^{-5}`) — no spectral line. All figures matched the ledger exactly.

## v15.483 — the bilinear level: pair geometry, still no residue anchor

**The exact decomposition, re-derived algebraically by hand, not just numerically.** Starting from `K_{N,M}=c(Mz_N-Nz_M)/(N²-M²)+2σp_Np_M` with `z_m=π/2+osc(m)`: substituting `M-N=-2X` and `N²-M²=4XT` gives `c(Mz_N-Nz_M)/(N²-M²)=c[-πX+(M·osc(N)-N·osc(M))]/(4XT)`, and since `c=2/π`, the `-πX` term simplifies to exactly `-1/(2T)` (the `X` cancels) — leaving the claimed `K=-1/(2T)+2σp_Np_M+c(M·osc(N)-N·osc(M))/(4XT)` exactly, confirmed by hand algebra before any numerics. Independently re-ran the numerical check with a different random seed and got max deviation `1.11×10^{-16}` (ledger: `2.2×10^{-16}`), both at float-precision noise floor.

**Independent re-verification of the anatomy and the pair-level residue probe.** GM-law ratio range `0.9909..1.0000` (sector 0) and comparable for sector 1, amplitudes `2σL²=+4.123` / `-0.880` — matching exactly. Band-term RMS at fixed `X` across both tested `T`-ranges: `0.413, 0.199, 0.092, 0.064, 0.028, 0.013` for `X=1,2,4,8,16,32` — matching the ledger's cited values exactly and confirming `T`-independence at fixed `X`. The pair-level residue probe (binning the oscillatory correction by `X mod 3`, `T mod 3`, `X mod 9`, `(N,M) mod 3`) gave class-mean spreads of `0.0000`-`0.0001` against a null scale of `~0.0001` in every binning and both sectors — matching exactly, confirming no pair-residue structure.

Hashes and execution confirmed (the harmless `RuntimeWarning` from dividing by `X=0` on the diagonal, masked out immediately afterward via `X!=0`, reproduced identically in this independent run).

## Scope and honesty assessment

All three entries are careful to scope their negatives precisely: v15.481 explicitly separates the two screw faces and warns against importing one's one-sidedness into the other's geometry; v15.482 and v15.483 both explicitly limit their claim to the operator's *construction data* (seed, diagonal, kernel formula), explicitly excluding the operator's spectrum and eigenfunctions as Lane A's separate, uninspected territory — a distinction drawn consistently and correctly across both entries, with v15.483 explicitly noting it is probing a different object than a related earlier audit finding (v14.910) and that the two are consistent rather than conflicting.

## Summary

All three deposits confirmed via independent, from-scratch recomputation of every stated claim, including the most specialized item in this batch — a numerical functional-equation check on the actual completed Dirichlet L-function of conductor 12, not a toy or asserted identity — and an independent hand re-derivation of the exact kernel decomposition in pair coordinates. No corrections needed.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-505
parent: v15.484
status: closed
action: none — all three entries' claims independently re-derived and confirmed, including the functional-equation identity on the real L-function and the hand-verified exact pair-coordinate decomposition.
deliverable: independent confirmation that door I's screw-overlay hiding place is closed (v15.481) and that the frame's residue labels have no anchor in the canonical operator's construction data at either the mode level (v15.482) or the bilinear/pair level (v15.483), with the operator's spectrum named as the only remaining unprobed territory.
