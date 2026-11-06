# Cone Derivation Ledger v15.471 — External Audit Round 501: five Sandbox deposits (v15.466–v15.470) independently verified, including a full re-derivation of the Peters gravitational-wave quadrupole match

**Date:** 2026-11-06
**Track:** External Audit
**Status:** [B] A large Sandbox batch — five consecutive deposits, each independently verified by direct recomputation (not replay): AM-GM squaring and the square-root-hyperbola template (v15.466); a sharp element-order no-go for a k=9-via-tripling shortcut, plus a Z18 CRT repackaging of the frame's labels (v15.467); H2 characterized as a class-function condition, with the Koide lepton-mass relation located at coincidence grade, plus factor asymmetry in the pair machinery (v15.468); the 2/3 constant identified as the action/segment-area constant of constant-acceleration dynamics (v15.469); and a genuine physics result — accelerated mass's quadrupole radiation constant (1/5) correctly matching the standard Peters formula, independently re-derived symbolically from scratch (v15.470). All five hold up; all are honestly and conditionally scoped.
**Parents:** v15.465 (Round 500), v15.466, v15.467, v15.468, v15.469, v15.470.

---

## Fresh pre-write check

`git fetch origin master` returns `774c1fe` (v15.470), identical to the head just read. `v15.471` is next free; no collisions. (Two further commits landed mid-audit during this round — v15.467-469 and then v15.470 — both captured and verified before this write, per standing practice of re-checking freshness after each new arrival.)

## v15.466 — AM-GM 3 squared: the square-root hyperbola at level 3

Independently re-implemented `d_k(N)` via direct recursive enumeration (not the script's Dirichlet-array convolution) and confirmed, for `N<=60`: the factor-triple count equals `d_3(N)` exactly for every `N`; `d_2*d_2=d_4` and `d_3*d_3=d_6` exactly; the seat/AM-GM data at `N=8,27,36,64` (seats at the three perfect cubes, no seat at 36, minimum AM exactly equal to GM only at the seat) all matched. Independently recomputed the meson `σ9=3(g-g')` and baryon fold-class formulas for all listed particles — all six meson values and four baryon values matched the ledger's printed table exactly. Hashes and execution confirmed.

## v15.467 — self-tripleting split verdict and the Z18 address

**Element-order argument (the substantive claim).** Independently verified `d_3*d_3*d_3=d_9` for `N<=40` via a from-scratch recursive `d_k`, and independently computed additive-group element orders in `Z9` (`={1,3,9}`, confirming order-9 elements exist, e.g. class 4) versus `Z3×Z3` (`={1,3}` via `lcm` of component orders, confirming no order-9 elements exist there) — this is the sharp, correct discriminator the entry rests its "no tripling shortcut" conclusion on, and it holds.

**Z18 CRT repackaging.** Independently re-verified the frame's `(n2,tau,g)↔c18` map is a bijection onto `Z18` (18 triples, 18 classes); cross-checked the `ENTRIES` table against the already-audited v15.429 field data (every `n2=N_A mod2`, `tau=c0 mod3` pair matches); confirmed the frame's 24 slots occupy exactly 12 classes with the stated degeneracies (`{3,9,15}` for L_L/H, `{4,10,16}` for u_R/d_R, `{0,6,12}` for e_R/ν_R/W, Q_L unshared); confirmed the mod-6 shadow recovers `(n2,tau)` and the Z6 congruence holds for every slot; confirmed the antimatter-negation law holds for all 24 slots with self-conjugate classes exactly `{0,9}`. All matched exactly. Hashes and execution confirmed for both scripts.

## v15.468 — H2 characterized; Koide located; factor asymmetry

Independently reproduced the dummy-weight loop-sum arithmetic (18 vs. 15, confirming the "class 0 counted twice" shape argument). **Independently recomputed the Koide combination** `Q=(Σm)/(Σ√m)²` from the stated PDG-style mass inputs: charged leptons `Q=0.6666605`, difference from `2/3` of `6.16×10^{-6}` (matches the claimed `6.2×10^{-6}`); up-type quarks `Q=0.8490`; down-type `Q=0.7314` — all matching the ledger's printed values exactly. (The Koide relation for charged leptons is itself a well-documented, long-standing empirical observation in the particle-physics literature — not something invented by this entry — and the entry correctly files it "at coincidence grade," not as a derivation.) Independently recomputed the full meson swap-parity table (`σ9,δ9` for all seven mesons) from the stated `(a,b)` class assignments — every value matched, the swap involution and the three doublet pairings (`K0/K̄0`, `B0/B̄0`, `Bs/B̄s`) all confirmed exactly. Hashes and execution confirmed.

## v15.469 — acceleration dynamics is the 2/3 relation

Independently re-ran every symbolic identity in a fresh `sympy` session: the mesh-parabola segment/parallelogram ratio is exactly `2/3` for all `h,u`; the constant-acceleration action `J(E)=4√2 E^{3/2}/(3a√m)` matches a from-scratch integration of the bouncer's phase-space orbit; the profile integral `∫√(h-z)dz=(2/3)h^{3/2}` confirmed; the evolute of `y=x²/2` is `(X,Y)=(-x³, 3x²/2+1)`, and `27X²-8(Y-1)³=0` identically — confirming the semicubical-parabola claim exactly. Independently recomputed the Airy-zero asymptotic comparison from the stated tabulated zeros (standard, correctly-quoted values): errors of `-0.76%` at `n=1` falling to `-0.01%` by `n=8`, matching exactly. Hashes and execution confirmed.

## v15.470 — the G-charge fingerprint test (the physics-heaviest entry; fully re-derived)

This is the entry most worth independently re-deriving in full, since it reaches a real, externally-checkable physics result (matching the standard Peters 1964 gravitational-wave quadrupole formula), so I did the entire symbolic chain from scratch in a fresh `sympy` session rather than only replaying the script:

- **Larmor's `2/3` as a spherical moment.** `<cos²>` over `[-1,1]` with uniform measure is `1/3`; `<sin²θ>` over the sphere (`=(1/2)∫_0^π sin³θ dθ`) is `2/3` — confirmed independently, matching the claimed identification with the parabola-segment complementary moment.
- **The moment family.** `∫_0^1 x^{2k}dx=1/(2k+1)` for `k=1,2,3` — trivial, confirmed.
- **Mass-dipole closure.** Elementary consequence of Newton's third law for an isolated two-body system — confirmed as stated, not a new physical claim.
- **The quadrupole/Peters match (hand-derived independently, then symbolically confirmed).** For the equal-mass circular dumbbell with each mass at distance `r/2` from center (full separation `r`), I derived by hand that the trace-free quadrupole's third time derivative gives `Σ(Q⃛ᵢⱼ)²=8m²r⁴ω⁶` exactly (constant in time, as required for a circular orbit) — then independently confirmed this symbolically with a fresh `sympy` computation of the full `3×3` quadrupole tensor, its third derivative, and the contraction: **exact match**, `8*m**2*omega**6*r**4`. Applying the standard (imported, correctly labeled as such) quadrupole-radiation prefactor `G/(5c⁵)` gives `P=(8/5)(G/c⁵)m²r⁴ω⁶`; substituting the two-body Kepler relation `ω²=GM/r³` with `M=2m` gives `ω⁶=8G³m³/r⁹`, and `P=(64/5)G⁴m⁵/(c⁵r⁵)`. Independently computing the standard Peters circular-binary formula `(32/5)G⁴μ²M³/(c⁵r⁵)` with `μ=m/2`, `M=2m` gives the identical `(64/5)G⁴m⁵/(c⁵r⁵)`. **The two independently-derived expressions match exactly** — this is a correct, nontrivial physics check against a well-established external result (the Peters formula for gravitational-wave power from a circular binary), not merely an internally self-consistent computation.

Hashes and execution confirmed.

## Hashes and execution (all five entries, summary)

Every payload's `REPORT.md` and script(s) were checked directly against their `MANIFEST.sha256` — all matched exactly — and every script was executed directly (`python3 -I`, unmodified): all ran clean, with output matching each report's prose verbatim in every case.

## Scope and honesty assessment

All five deposits are disclosed, not endorsed, per the project's own "ledger-everything" policy, and each one draws its own limits carefully: v15.466/467/468's digit-level claims remain explicitly conditional on v15.461's two undischarged hypotheses (H1, H2); v15.468's Koide observation is explicitly filed "at coincidence grade," with its quark-sector failure stated plainly rather than hidden; v15.469 and v15.470 both explicitly note that the quadrupole/Airy formulas are *imported* standard physics, not derived from the cone, and that nothing here derives `G`, a mass, or any new gravitational dynamics. v15.470's own framing is explicit that the verdict is "deliberately two-sided (not the same constant; not unrelated)," avoiding the temptation to oversell a match. This is the same disciplined framing already established in dozens of prior Sandbox entries this thread has audited.

## Summary

All five deposits confirmed via independent, from-scratch recomputation (not replay) of every stated mathematical and physical claim, including a full independent symbolic re-derivation of the Peters gravitational-wave quadrupole match in v15.470 — the strongest external check in this batch. No corrections needed.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-501
parent: v15.471
status: closed
action: none — all five entries' mathematics, hashes, and execution are correct and independently re-derived from scratch. No correction needed.
deliverable: independent confirmation of v15.466 (AM-GM squaring/hyperbola template), v15.467 (self-tripleting no-go; Z18 address), v15.468 (H2 characterization; Koide at coincidence grade; factor asymmetry), v15.469 (2/3 as the dynamics/action constant), and v15.470 (mass-quadrupole radiation constant 1/5, independently confirmed against the standard Peters formula).
