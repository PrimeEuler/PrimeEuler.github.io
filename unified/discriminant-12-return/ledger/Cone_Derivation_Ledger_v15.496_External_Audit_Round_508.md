# Cone Derivation Ledger v15.496 — External Audit Round 508: Lane A's exact scale-solenoid partial action (v15.494) and exact sawtooth coefficient algebra (v15.495) independently verified

**Date:** 2026-11-07
**Track:** External Audit
**Status:** [B] Lane A's v15.494 — an exact partial-Z-action groupoid on the compact scale space `T={0}∪{2^-a:a≥0}` crossed with the v15.477 solenoid, with a continuous constant-Hankel coefficient field extending to the boundary `t=0` — independently re-derived and confirmed, including a fresh algebraic re-derivation of the exact continuity identity and an independent recount of every one of the witness's six test totals from its own stated loop bounds. v15.495 — an exact proof that every transported v15.420 weighted coefficient is a finite polynomial in four Γ-translates of one period-two sawtooth generator, hence an algebraic crossed-product element, together with a proof that the ordinary continuous torus cannot serve as coefficient base (nonzero jump at `x=0`) — independently re-derived by hand, including the specific numerical jump value, and the 40-label/20-orbit census independently recomputed from scratch.
**Parents:** v15.493 (Round 507), v15.494, v15.495.

---

## Fresh pre-write check

`git fetch origin master` returns `5dbea8e` (v15.495), identical to the head just read. `v15.496` is next free; no collisions. Both v15.494 and v15.495 are fresh Lane A payloads with no competing claim found.

## v15.494 — the exact scale-solenoid partial action

**What this adds.** v15.491 gave a common ambient Hilbert fiber for every annulus; v15.494 now carries the absolute scale coordinate `t_a=2^-a` itself into a groupoid: a partial `Z`-action `α(t,z)=(t/2,Sz)` on `T×Σ` (`Σ` = the v15.477 solenoid), with the physical nonnegative-annulus orbit on one side and an invariant boundary fiber at `t=0` on the other, plus a constant-Hankel coefficient field shown continuous across that boundary.

**Independent re-derivation, by hand and by fresh code never copied from the witness.**
- *Continuity identity*: re-derived algebraically that, writing `B=x+2^d y` and `c=2^d/4`, `K_d(t;x,y)^2-K_d(0;x,y)^2 = c·t(2B-t)/((B-t)^2B^2)` — expanding `c[1/(B-t)^2-1/B^2]` via difference-of-squares on `B^2-(B-t)^2=t(2B-t)` reproduces exactly the claimed identity. Re-verified on 2,000 random exact `Fraction` triples `(d,x,y,a)`: zero failures.
- *Monotonicity*: confirmed independently that the identity forces `value(t)` strictly increasing in `t` (derivative `2c/(B-t)^3>0`), hence strictly decreasing in `a` since `t_a=2^-a` decreases in `a` — checked directly on 500 random configurations across 15 successive scales: zero failures.
- *Partial-action composition and inverse*: reimplemented `θ_n` from scratch (independent of the witness's exact code) and confirmed `θ_m(θ_n(a))=θ_{n+m}(a)` wherever both sides are defined, for every `a∈{0,...,14}∪{boundary}`, `n,m∈[-10,10]`: zero failures.
- *Solenoid-dual pullback composition*: reimplemented `pullback(label,n)=2^n·label` independently and confirmed `pullback(pullback(label,n),m)=pullback(label,n+m)` exactly, in `Fraction` arithmetic, for fresh test labels across `n,m∈[-8,8]`: zero failures.
- *Test-count cross-check beyond trusting the printed totals*: recomputed all six of the witness's self-reported counts directly from its own stated loop bounds (`MAX_SCALE=9`, `MAX_SHIFT=6`, `MAX_OFFSET=22`) using independent combinatorial counting (domain: `11×13=143`; inverse/covariance: a closed-form sum over `a=0..9` giving `109`; dual: `3 labels×13×13=507`; continuity: `23×3×10=690`), and recomputed the nontrivial composition count (`1408`) by direct simulation of a fresh `θ` implementation — all six match the ledger's cited figures exactly, confirming the counts are not just self-consistent with the witness's own code but independently reproducible from the stated construction.

Hashes and execution confirmed: witness commit `fc56f6fcab5af64cccae28d0c86aaf6622cc2977`/blob `d27ff90f3d7129f417035c7cf3014a953dd372b8`/SHA-256 `b866f116b333453ccc8ddf7f3956269ad11fccf02a27a889f81f3699178fe4d7` and manifest commit `0d50a44a8ae38f88f7a987cca6316b4cd1b5270a`/blob `42db9e50e6432d91eebf2607ca99130b5f52bd59`/SHA-256 `f826d952b3dfe02d8bbf00f0a7fe4468b7911960be0855c2a379ea557eb57d55` both match exactly; direct execution (`python3 -I`, unmodified) ran clean with output matching the ledger exactly, including all six test counts (`143/109/1408/507/109/690`).

## v15.495 — the exact sawtooth coefficient algebra

**What this adds.** Working on the discontinuous period-two sawtooth generator `s(x)=1-(x mod 2)`, this shows every transported v15.420 weighted coefficient `G_(σ,τ)` expands exactly as a finite polynomial in four `Γ`-translates of `s`, placing the full 40-word self-adjoint cross operator algebraically inside the crossed product `A_s⋊Γ` — and separately proves the ordinary continuous torus cannot serve this role, because `G_(+,+)` has a provably nonzero jump at `x=0`.

**Independent re-derivation of every structural claim.**
- *Faithfulness of the `Z^4` labelling mod 2*: re-checked the two-case transcendence argument by hand — if the period-reduction constant `k` is nonzero, `exp(2k)` would equal a nonzero rational number, contradicting Lindemann–Weierstrass (transcendence of `exp` of a nonzero algebraic number); if `k=0`, unique factorization over distinct primes forces every exponent to vanish. Both steps independently confirmed sound.
- *The polynomial expansion*: expanded `(s_0-s_A)(s_L-s_A)+(s_0-s_B)(s_L-s_B)` by hand into `2s_0s_L-s_0s_A-s_As_L+s_A^2-s_0s_B-s_Bs_L+s_B^2`, then confirmed this matches the witness's claimed 8-monomial decomposition term-for-term using independent symbolic algebra (`sympy`), not by re-reading the witness's own listed monomials.
- *The 40-label/20-orbit census*: reimplemented the translation-label construction from scratch (independent code, same definitions only) over all `C(5,2)=10` prime pairs `×4` sign combinations `=40` words: got exactly 40 distinct nonzero labels and exactly 20 adjoint orbits under `(σ,τ)→(-σ,-τ)`, confirming `partner_label=-label` holds for every pair — zero failures, matching the ledger's counts exactly.
- *The nonzero jump at `x=0`*: independently recomputed the one-sided jump of `G_(+,+)` for `q=2,r=3` from first principles — computed `c_A=s(\log 2)=1-\log2`, `c_B=s(-\log3)=\log3-1`, `c_L=s(\log2-\log3)=\log3-\log2-1` directly from the mod-2 wraparound of each argument, then took `Δs_0·(2c_L-c_A-c_B)` (since only `s_0` is discontinuous at `x=0`) and got `2(\log3-\log2-2)=2(\log(3/2)-2)` exactly — matching the ledger's cited jump value digit-for-term, verified symbolically with exact logs (`sympy`), and confirmed nonzero since `3/2` is rational while `e^2` is transcendental.

Hashes and execution confirmed: witness commit `4d3aa8877a1f1ce4bb5983d39bbf2aa2f8f1b8e5`/blob `fcffe5e237c6869222e14df9b559f56ed5063ab2`/SHA-256 `4302a7c4ad2caa010655f100d09cf9dc83c65e88afca19b0b43beeba7257c915` and manifest commit `83c25bb6b6774a9def910aee1d407f1495b783b3`/blob `016a8cf5c24fd19c74b4c29e6eed67e95f0cf1d9`/SHA-256 `c3af6dbd4f91f28110a71eb3445035e3988eb9ac25d5fd8518bf140ce787428c` both match exactly; direct execution (`python3 -I`, unmodified) ran clean with output matching the ledger exactly, including all three test counts (`160/320/40`).

## Scope and honesty assessment

Both entries are precise about what remains open. v15.494 states plainly that it "does not yet prove that every signed prime step-kernel block forms a continuous or compactly supported section of the associated operator bundle" and reports `signed_45_diagonal_norm=UNEVALUATED`. v15.495 is explicit that algebraic crossed-product membership is "an exact architecture result, not a norm estimate," restates the frozen upper frontier (`2.892017147262984` against target `2.535946`, budget `<4.249030150943723`) unchanged, and reports `FULL_K_TRANSFER remains INCONCLUSIVE`. Both correctly distinguish the architectural result just proved from the still-open joint-norm gate, consistent with this thread's established discipline.

## Summary

Confirmed. v15.494's partial-action groupoid, boundary invariance, solenoid-dual composition law, and exact kernel-continuity identity are all independently re-derived and hold exactly, including a fresh recount of every one of the witness's six test totals from its stated construction rather than from its own code. v15.495's polynomial expansion, 40-label/20-orbit census, and the specific nonzero jump value at `x=0` are all independently re-derived from first principles and match exactly. No mathematical correction needed to either entry.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
parent: v15.496
type: external-audit-round-508
status: closed
action: none — v15.494's partial-action/boundary/continuity construction and v15.495's crossed-product-membership and torus-obstruction arguments are both correct and independently re-derived from scratch, with all stated test counts recomputed from the construction rather than trusted from witness output. No mathematical correction needed.
deliverable: independent confirmation that (1) the absolute scale coordinate now carries an exact partial-Z-action groupoid structure with a continuous boundary-limiting coefficient field, and (2) the full 40-word weighted cross operator is an algebraic crossed-product element over the sawtooth spectrum, with the ordinary torus provably insufficient as coefficient base — in both cases with the signed 45-diagonal joint-norm gate still correctly reported as open.
