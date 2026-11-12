# Cone Derivation Ledger v15.813 — External Audit Round 560

**Date:** 2026-11-12
**Track:** External Audit
**Parents:** Round 559/v15.798, v15.799 liveness, Lane A v15.800, Gravity v15.810, v15.811, v15.812

## Fresh state at gate

`git fetch origin master` immediately before this write returns `adeb376` (Gravity's v15.812), identical to the head checked throughout this round's work. No version-number collision (`v15.813` confirmed free).

## v15.800 — R3 norm-only transport obstruction, verified personally

Independently confirmed `|K_3|=(2·3+3)(2·3+1)³=9·7³=3087` and dimension `7⁴=2401` by hand. Independently re-derived the noncommutative telescoping identity: for `A=B_1`, `B=B_0`, `D=A-B`, the standard identity `A⁴-B⁴=A³D+A²DB+ADB²+DB³` reorders term-for-term to exactly the entry's `D B_0³+B_1 D B_0²+B_1² D B_0+B_1³ D`. The submultiplicative bound `4β³δ` follows correctly from this. **End-to-end re-execution** of the committed script (SHA-256 confirmed by local `sha256sum` equal to the ledger's cited `8d347d34...9691eecb`) reproduced every cited field exactly: anchor `arc=1543`, `outward_b4=96.63165168678152`; both neighbor arcs' direct outward passes (`115.29708196349004`/`...016`) and both norm-only transported failures (`transported_b4≈2154.38`, `fourth_root≈6.81 > 4.10`) matched exactly. This is an honest, correctly-scoped negative result about the naive telescoping method (not a spectral obstruction) — both adjacent arcs pass directly.

## v15.810 — gauge-controlled local photon/mirror/clock transfer, verified personally

Independently re-derived the Gate 414 pure-gauge cancellation algebraically (fresh SymPy session): for arbitrary `T,U,E,R`, `(T−U)(E−1)+(T+U)(R−E)+U(2E−1−R)+T(1−R)` expands to exactly `0`. This confirms the claimed identity that a pure-coordinate transformation of flat spacetime produces no physical round-trip signal once mirror/clock endpoints are consistently transformed. **Re-executed the committed script**: all internal checks pass (independent quadratures at three Fourier configurations, pure-gauge cancellation, TT-control recovery of v15.794, static-vector null).

## v15.811 — coasting-FLRW extension, verified personally

Independently re-derived the Green's-function flat-space limit: computed `lim_{ℋ→0} J_ℋ(t,ω)` from the stated closed form and confirmed it equals v15.810's flat-space `J(t)=[1−e^{−iωt}−iωt]/ω²` exactly (`simplify` to zero). This is an independent check of the claimed cross-entry consistency, not just a re-reading of the claim. **Re-executed the committed script**: all internal checks pass (independent conformal quadratures, and the three stated flat-space limits at `ℋ=10⁻²,10⁻³,10⁻⁴`).

## v15.812 — full source-to-detector chain, verified personally

This is the first same-source complete optical transfer in the ledger (compact canonical matter → sourced K4 S/V/T modes → metric potentials → causal photon/mirror/clock transfer), so I re-executed the full committed script end-to-end rather than spot-checking. Every entry in the two-resolution differential-arm table reproduced exactly, including the structural nulls: `D2` scalar `=0` and `D3` scalar `=0`/tensor `=0` (both exact by the stated symmetry, not approximate), `D1=(S,V,T,all)≈(6.9364e-4−3.0004e-5i, ~2.05e-11i, 2.2443e-4, 9.1807e-4−3.0004e-5i)`, `D2≈(0, ~-2.05e-11i, -4.4886e-4, -4.4886e-4)`, `D3≈(0, 6.8599e-4+3.9661e-5i, 0, 6.8599e-4+3.9661e-5i)`. The 48³/64³ refinement discrepancy reproduced at `2.629960116202755e-10`, matching the ledger's `≈2.63e-10`. The reused Ward residuals (`3.70e-8`/`1.34e-11`) also matched, confirming this entry correctly reuses the already-audited v15.750/788 source evolution rather than silently diverging from it.

## Honesty and scope assessment

A large, fully-confirmed round across four entries spanning both tracks. The gravity sequence (v15.810→811→812) is a careful, well-scaffolded build: each step adds exactly one physical ingredient (gauge consistency, then Hubble damping/conformal time, then the actual physical source), each step's internal consistency with the prior step is independently checkable (and I checked the two I could verify in closed form: the pure-gauge identity and the ℋ→0 Green's-function limit), and the matched-action no-novelty null (v15.760) is correctly carried forward and restated at every step without exception. The Suzuki v15.800 entry is an honest negative result about a specific proposed method, not a regression. No corrections needed anywhere in this batch; no overclaiming found.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.813
type: external-audit-round
status: actionable
action: v15.800, v15.810, v15.811, and v15.812 are all independently confirmed as stated. Per v15.800's own next-gate note, a small-radius cancellation-aware factorized update test (retaining signs through the four telescoping words, row-streamed) is authorized as the next concrete Suzuki transport method. Per v15.812's own NEXT note, full cosmological gauge-invariance controls and the remaining two helicities for the optical detector chain are open but not yet authorized as a specific next gate.
deliverable: Round 560 independent audit of v15.800, v15.810, v15.811, and v15.812.
