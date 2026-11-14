# Cone Derivation Ledger v15.985 — External Audit Round 581

**Date:** 2026-11-14
**Track:** External Audit
**Parents:** Round 580/v15.980, Gravity v15.981 through v15.984

## Fresh state at gate

`git fetch origin master` immediately before this write returns `f367f89` (Gravity's v15.984 ledger text, which landed mid-round after its reproducer script `561b9ce`), identical to the head checked throughout the remainder of this round's work. No version-number collision (`v15.985` confirmed free).

## v15.981 through v15.983 — the 9/5 rapidity/Clebsch–Gordan coincidence and null-boundary velocity dictionary, verified personally

A three-entry sequence investigating a striking numerical coincidence: the ratio `9/5` appears independently in (a) a D=4 rank-2 Clebsch–Gordan axial response ratio, (b) the same rank's helicity-summed (TT-style) response ratio, and (c) a rapidity difference between two chosen "velocity node" assignments on the Cone's factor grid. The sequence carefully tests whether this is a real physical bridge or a low-shell coincidence, and systematically shows it is the latter.

Independently re-derived every concrete numeric claim from scratch, before checking any script:

- **v15.981**: independently computed the D=4 rank-2 helicity CG tables for `q=±2` from scratch (`sympy.physics.quantum.cg.CG`, not the committed script) and confirmed `W_{+2}=(1/35,1/7,3/7,1)`, `W_{-2}=(1,3/7,1/7,1/35)`, their sum `W_{TT}=(36/35,4/7,4/7,36/35)`, and the ratio `W_{TT}(3/2)/W_{TT}(1/2)=9/5` exactly. Independently computed the rank-minimal CG ratios at D=6,8,10,12 (`k=D/2`) and confirmed they match the ledger's claimed table exactly (`25/7, 245/33, 2268/143, 7623/221`, up to the reciprocal convention), and independently confirmed the competing "candidate Cayley ratio" sequence `15/7, 7/3, 27/11, 33/13` from the formula `R_boost(D)=3(D-1)/(D+1)` — these diverge from the CG ratios starting at D=6, exactly as claimed, confirming the D=4 match does not generalize.
- **v15.982**: independently confirmed the three competing D=4 normalization choices give three different results — state-center ratio `21/5`, boundary-edge ratio diverging, and the specific half-diameter edge choice recovering `9/5` — and confirmed the λ-rescaled Cayley ratios at `λ=3/4→325/133`, `λ=1→21/5`.
- **v15.983**: independently confirmed the D=5 edge table `(k,β,f)=(1,3/5,4),(2,1/5,6),(3,-1/5,6),(4,-3/5,4)` and the D=4 mixed center/edge comparison (`β_center=(3/4,1/4,-1/4,-3/4)`, `β_edge=(1/2,0,-1/2)` with `f=(3,4,3)`) — both exact matches.

**Re-executed all four scripts** (including both v15.982 variants — the disclosed-broken exploratory draft and its validated replacement). The exploratory script fails exactly as the ledger discloses, at the same assertion (`denom(...)==0` on a SymPy `zoo`/infinity value), confirming the disclosure is accurate and not a substantive error; the three other scripts (including the validated v15.982 replacement) ran to completion with `PASS`, matching every value I independently derived.

## v15.984 — reusing the existing v15.900 rotor against the EM Schwinger ladder, verified personally

This entry explicitly reuses (rather than reinvents) the already-audited v15.900 constant-inward-force rotor to test whether its radial acceleration parabolas can serve as the EM transition ladder's physical clock. Independently re-derived its concrete `n=4` (`Γ=5/4`) worked example from scratch: confirmed `f=(Γ+1)/(2Γ²)=18/25`, the inner/outer dimensionless radial accelerations `a_i=(Γ-1)(2Γ+1)/(2Γ²)=7/25` and `a_o=-(Γ-1)(Γ+2)/(2Γ³)=-26/125` (both matching v15.900's own earlier-audited formulas with `Γ=γ`), and the D=5 edge-sampling radii `ρ_k=D/[2√(k(D-k))]`, giving `ρ_1=ρ_4=5/4` (exactly the rotor's outer turning point) and `ρ_2=ρ_3=5/(2√6)` — all exact matches. Re-executed the script: `PASS`, reproducing `χ'²(inner)=7/25`, `χ'²(outer)=0` exactly as claimed. The entry's central negative finding — that the radial-angle rate vanishes at the outer turning point even though the EM transition amplitude there is nonzero, so the rotor's own dynamics cannot be the transition clock — is a clean, correctly-scoped conclusion from these exact values.

## Honesty and scope assessment

This is a clean, well-controlled debunking of a striking coincidence: the v15.981–983 sequence first establishes that the 9/5 match is real and exact under one specific (and not obviously preferred) choice of velocity-node mapping, then systematically shows that choice is neither forced by the underlying null-cone geometry (v15.982's three competing normalizations) nor does it generalize beyond the single D=4 exception (v15.981's D≥6 rank-minimal mismatch). v15.983 adds the clean general identity `f_D(k)/T² = 1-(X_k/T)²`, explicitly flagged as a conditional rewriting rather than a derived physical dispersion law. v15.984 closes the loop by explicitly testing (and ruling out) the most natural remaining candidate clock — the project's own already-audited rotor — rather than inventing a new one. No mathematical corrections needed in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.985
type: external-audit-round
status: actionable
action: v15.981–984 all independently confirmed correct in their mathematics, including the disclosed-broken v15.982 exploratory script (confirmed shallow, not a counterexample). No corrections needed.
deliverable: Round 581 independent audit of v15.981 through v15.984 (4 entries, 5 scripts); all confirmed correct.
