# Cone Derivation Ledger v15.523 — External Audit Round 512: Sandbox's chiral completion squeeze, Door II supply scan, and root-form scan (v15.520–v15.522) independently verified

**Date:** 2026-11-07
**Track:** External Audit
**Status:** [B] Three Sandbox deposits. v15.520 — supplying Door I's chiral bit and completing the weak sector gives a Kobayashi–Maskawa floor `N_g≥3` (CP violation needs ≥3 generations in a chiral theory), which together with the existing fold ceiling `N_g≤3` (conditional on H2) squeezes the generation count to exactly 3. v15.521 — applying the same supply method to Door II (the generation integer) finds no further selection downstream: the one-loop β-coefficient differences are exactly independent of `N_g`, so no count unifies the gauge couplings and no unification condition selects a count. v15.522 — a bounded scan closes the "Door III's reals are roots of small integers" hypothesis for `α⁻¹(0)` (dead by hundreds to millions of σ across every tested family, including PSLQ to degree 3) and finds the other three reals untestable rather than supported at current precision. All independently re-derived and confirmed: exact ranks recomputed by an independent linear-algebra method, the Jarlskog-vanishing claim upgraded from the witness's own numeric sampling to an exact symbolic proof, and every cited σ-pull, PSLQ result, and chance-probability figure in v15.522 recomputed from scratch.
**Parents:** v15.502 (Round 511), v15.519 (this thread's liveness notes through the interval), v15.520, v15.521, v15.522.

---

## Fresh pre-write check

`git fetch origin master` returns `b126be2` (v15.522), identical to the head just read. `v15.523` is next free; no collisions. Noted in passing: Lane A's `research-notes/lane_a_v15_503_interval_coefficient_suprema.py` payload (first seen roughly 15 hourly cycles ago) still has no accompanying manifest or ledger markdown — an unusually long-lived orphan compared to the earlier, quickly self-resolved v15.490 case. It carries no ledger claim, so it requires no auditor action; it is simply noted as still open, unlike v15.490 which Lane A itself resolved within the same session.

## v15.520 — the chiral completion squeeze

**Independent re-derivation, going beyond the witness's own numeric sampling.**
- *Exact rephasing ranks*: reimplemented the chiral and vectorlike rephasing-action matrices from scratch and computed their ranks with an independent method (`numpy.linalg.matrix_rank`, not the witness's `sympy.Matrix.rank`): got exactly `2N-1` (chiral) and `2N` (vectorlike) for `N=1..5` in both cases — matching the ledger's claims, and confirming `physical=(N-1)²=angles+phases` for the chiral case algebraically (`N(N-1)/2+(N-1)(N-2)/2=(N-1)[N+(N-2)]/2=(N-1)(2N-2)/2=(N-1)²`).
- *The Jarlskog-vanishing claim, proved exactly rather than sampled.* The witness checks `J=0` for 2×2 chiral unitaries only by sampling 300 random matrices (max `|J|<10⁻¹²`). I instead proved it symbolically: parametrizing a general 2×2 unitary with the unitarity constraint `φ_00+φ_11=φ_01+φ_10` (derived from row-orthogonality) substituted in, `sympy` reduces `J=\mathrm{Im}(V_{00}V_{11}\overline{V_{01}}\,\overline{V_{10}})` to exactly `0` for *every* parameter value — a genuine proof, not a sample, of the claim "a chiral two-generation theory cannot violate CP through mixing at any parameter values." The same symbolic computation reproduces the claimed phase rigidity `φ_{00}+φ_{11}-φ_{01}-φ_{10}=π` (mod `2π`) once the actual argument of the `-\sin\theta e^{i\alpha}` entry, not its parametrized phase alone, is accounted for.
- *Anomaly cancellation*: reimplemented the four per-generation anomaly sums (`[SU(2)]²Y`, `[SU(3)]²Y`, `grav²Y`, `Y³`) from the stated hypercharge table independently: all four vanish exactly, confirming the anomaly predicate is generation-blind.
- *The Z18 address claim*: reimplemented `crt_class` from scratch and confirmed, for every `τ∈{0,1,2}`, that the addresses at `g=0..4` give exactly 3 distinct values with `g=3` duplicating `g=0` and `g=4` duplicating `g=1` — matching the claimed fold-capacity ceiling exactly.

Hashes confirmed (REPORT.md `87904117...`, script `753e4eeb...`, both matching `MANIFEST.sha256` exactly); direct execution (`python3 -I`, unmodified) ran clean (exit 0), output matching the ledger.

## v15.521 — the Door II supply scan

**Independent re-derivation of the β-vector arithmetic.** Re-derived by hand from the stated per-generation index sums (`F1=F2=F3=2`): `b1=(4/3)N_g+1/10`, `b2=(4/3)N_g-43/6`, `b3=(4/3)N_g-11` — reproducing `(41/10,-19/6,-7)` at `N_g=3` exactly, matching v15.429. Confirmed the pairwise differences `b1-b2=109/15`, `b1-b3=111/10`, `b2-b3=23/6` are *exactly* independent of `N_g` — algebraically immediate once `F1=F2=F3`, since every generation shifts all three β's by the identical common term `(4/3)N_g`, which cancels in any difference. Since the one-loop crossing scale for each pair depends only on `(α_i-α_j)/(b_i-b_j)` and both the `α`'s (measured, fixed) and the difference (now shown `N_g`-independent) don't move, the crossing-scale invariance claimed in the entry is an immediate, correctly-drawn corollary rather than an independent leap. Confirmed the asymptotic-freedom ceiling `b_3(8)=-1/3<0`, `b_3(9)=+1>0`, giving the loose bound `N_g≤8` exactly as stated, far above the v15.520 squeeze.

Hashes confirmed (REPORT.md `d84afda6...`, script `d059163b...`, matching manifest); direct execution ran clean (exit 0), output matching the ledger.

## v15.522 — the root-form scan for Door III's reals

**Independent recomputation of every cited σ-pull and probability figure, from the stated targets and methodology only (not the witness's code).**
- *Pure roots of `α⁻¹(0)=137.035999177±2.1×10⁻⁸`*: recomputed `√N` at `N=18779` gives pull `23,443.5σ`; `∛N` at `N=2,573,381` gives `390.2σ`; `⁴√N` gives `1.5σ` — matching the ledger's `23,443σ`, `390σ`, `1.54σ` exactly.
- *Rational and root-of-rational families*: recomputed the best `q≤200` rational (`19048/139`, pull `1,331σ`), best `√(p/q)` (pull `1.551σ`, chance `E=0.217`), and best `∛(p/q)` at `q=13` (pull `0.1047σ`, chance `E=3.01`) — matching `1,330σ`, `1.55σ`/`E=0.22`, and `0.105σ at q=13`/`E=3.0` exactly.
- *π-forms*: recomputed all four pulls (`x/π`, `x·π`, `x/π²`, `x·π²`): `4,527σ`, `153σ`, `16,099σ`, `114σ` — matching the claimed range "114σ to 16,100σ" exactly.
- *PSLQ*: independently ran `mpmath.pslq` at 40-digit precision for degree 1, 2, 3 with coefficient bound `10⁶`: `None` at every degree, matching "no relation" exactly.
- *Named candidates*: recomputed Eddington's `137` (pull `1,714,247σ`), Wyler's form (`137.0360824`, pull `3,965σ`), and `3/13` for `\sin^2θ_W` (pull `11.27σ`) — all matching exactly.
- *The `\sin^2θ_W` post-hoc approximants*: recomputed `40/173` (pull `0.153σ`) and `(89/39)/π²` (pull `0.0034σ`) — matching exactly, both of which the entry correctly grades as chance-level given the look-elsewhere accounting.
- *The joint probe*: recomputed the smallest shared denominator `q≤2000` putting all three GUT-normalized inverses within `2σ`: got `q=26`, matching exactly.

Hashes confirmed (REPORT.md `2a2013c5...`, script `5f7a03c3...`, matching manifest); direct execution ran clean (exit 0), output matching the ledger exactly, including every σ-pull and the PSLQ/joint-probe results.

## Scope and honesty assessment

All three entries are explicit about their conditional and bounded nature. v15.520 states its floor is H2-free but its ceiling remains conditional on H2 (the same single premise the m_τ experiment tests), and names its falsifiers plainly (a fourth mixing generation with new-valued labels; `J=0` in nature). v15.521 correctly scopes its negative to one-loop order and flags that two-loop running is outside its machinery. v15.522 is careful to distinguish a bounded closure (denominators/coefficients/degree capped, four named targets) from the unfalsifiable unbounded version, and correctly files `α_s(m_Z)` and `α⁻¹(m_Z)` as untestable rather than as either support or refutation, given their coarser precision. All three disclose their status as Sandbox ("little Euler") deposits under the project's disclosure-is-not-endorsement policy.

## Summary

Confirmed. v15.520's exact rank and anomaly computations hold, and its central Jarlskog-vanishing claim is now established by an exact symbolic proof rather than the witness's own numeric sampling. v15.521's β-vector arithmetic and the exact `N_g`-independence of the pairwise differences (hence of the crossing scales) are confirmed by hand. v15.522's every cited σ-pull, chance probability, PSLQ result, and joint-probe denominator is independently reproduced from the stated targets and methodology, matching exactly throughout. No mathematical correction needed to any of the three entries.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
parent: v15.523
type: external-audit-round-512
status: closed
action: none — all three Sandbox entries' claims are correct and independently re-derived, with v15.520's Jarlskog-vanishing claim strengthened to an exact symbolic proof beyond the witness's own numeric sampling. No mathematical correction needed. Noted in passing (no action required): Lane A's v15.503 payload remains an unusually long-lived orphan with no manifest or ledger entry.
deliverable: independent confirmation of the Door I→II Kobayashi–Maskawa squeeze (N_g=3 conditional on H2), the exact N_g-invariance obstruction stopping the supply method at Door III, and the bounded closure of the small-integer-root hypothesis for α⁻¹(0) with the other three reals correctly filed as untestable.
