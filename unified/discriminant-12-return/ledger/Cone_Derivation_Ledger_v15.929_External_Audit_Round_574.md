# Cone Derivation Ledger v15.929 — External Audit Round 574

**Date:** 2026-11-13
**Track:** External Audit
**Parents:** Round 573/v15.917, Gravity v15.918 through v15.928

## Fresh state at gate

`git fetch origin master` immediately before this write returns `6811ffa` (Gravity's v15.928), identical to the head checked throughout this round's work. No version-number collision (`v15.929` confirmed free); no further collision anywhere in v15.918–928 (each checked individually).

## Proactive collision avoidance, noted positively

Gravity's own v15.918 entry explicitly notes it detected that Round 573's `v15.917_External_Audit_Round_573.md` had landed during its drafting, and self-bumped from the originally intended `v15.917` to `v15.918` *before* committing — correctly avoiding what would have been a sixth collision, entirely on its own initiative, without the auditor needing to flag anything. This is new and welcome: the three most recent collisions (v15.904, and earlier v15.889) needed the auditor to catch them after the fact; this is the first case of the Gravity track pre-empting one.

## v15.918 through v15.928 — EM-lifetime bridge and legacy-geometry reconciliation, verified personally

Two connected threads: (a) v15.918–920 test whether real spectroscopic data (lifetimes, branching ratios) can supply the physical "clock" the project has been looking for; (b) v15.921–928 reconcile the owner's original legacy WebGL cone/parabola/hyperbola code and the newer two-circle/Schwinger material with the project's older, independently audited quarter-grid (`q=2`) staircase construction.

Independently re-derived from scratch (fresh SymPy/NumPy/SciPy, before checking any committed script):

- **v15.918** (coherent-state parity no-go): independently built the full 4×4 symplectic propagator for the coupled tidal oscillator and reproduced the entire cited table exactly — `⟨v1⟩_±`, `⟨X_Cone⟩/u`, and `E=2.00000000` at every listed `t`, including the covariance contribution to `⟨X_Cone⟩`.
- **v15.919**: conceptual/dimensional bridge; the one concrete number (the (4,1) ratio 2/3) matches the already-verified v15.908 result. No new independent numeric claim beyond what Round 572 already confirmed.
- **v15.920** (hydrogen 3p/2p lifetime cross-check): this is the most consequential falsifiable claim in the batch. Independently computed the exact nonrelativistic Coulomb radial integrals `R21=128√6/243`, `R31=27√6/128`, `R32=27648√3/15625` from scratch using `sympy.physics.hydrogen.R_nl` (not the committed script's method), then independently re-derived the frequency ratios `ω31/ω21=32/27`, `ω32/ω21=5/27`, the branch ratios `A31/A21=2187/8192`, `A32/A21=69984/1953125`, the total ratio `0.3027995814375`, the predicted lifetime `5.284023156 ns`, and the residual `1.0655σ` against the cited measured `5.5±0.2 ns` — every figure matched exactly. (The cited experimental lifetimes themselves are literature values from Chupp, Dotchin & Pegg 1968, outside what I can independently remeasure; the entry's own citation and DOI are consistent with what it claims to use.)
- **v15.922** (divisor-count intersections): confirmed `d(36)=9`, and the `t`-scaled lattice counts `d(144)=15`, `d(324)=15`.
- **v15.923** (divisor moments): confirmed the full `N=12` moment table from scratch (`ΣX²=69`, `ΣY²=72`, `ΣT=28`, `ΣT²=141`) by direct enumeration of divisor pairs, matching the ledger exactly.
- **v15.924** (parabola=hyperbola=circle incidence): confirmed the D=5 amplitude list `[2,√6,√6,2]`.
- **v15.925** (quarter-grid boundary witness): confirmed the escape weight `c=j+1/4=1` at L=3.
- **v15.926/927** (null injections, magnetic charge, intertwiner obstruction): independently built the exact `q=2` Schwinger-type `J_+` matrices and the injections `A,B` for `L=2,3,4`; confirmed the magnetic-charge commutators `[M,A]=-A/4`, `[M,B]=+B/4` exactly, and confirmed `F_A,F_B` (the raising-covariance residuals) are both nonzero, matching v15.927's claimed obstruction.
- **v15.928** (weighted quarter-rung covariance): independently verified the specific proposed A-family solution `(0,√6/3,0,1)` and both B-family solutions `(√6/3,0,1,0)`, `(0,√3/2,0,1)` at L=3 give exact zero raising-covariance residual, and confirmed that requiring *both* raising and lowering covariance simultaneously forces all coefficients to zero for L=2 through 5 (solved the full linear systems independently, not just spot-checked the ledger's claim).

## Script execution and defect found

**Re-executed all eleven scripts** (note: v15.924 has two committed scripts — an exploratory one and an explicitly superseding "validated" copy, both of which the ledger itself correctly says not to conflate; both ran and passed). **Ten ran to completion with PASS.**

**One genuine shallow defect found: `k4_quarter_staircase_product_transport_v15_926.py` crashes with `AssertionError` at line 53 (`assert al*bl==c`).** The script computes the lower/downward missing-edge product using the *upward*-oriented factor formula `(a,b)=(j−m,j+m+1)` at the lower boundary index, instead of the *downward*-oriented formula `(j+m,j−m+1)` that the ledger's own Gate 660 text explicitly specifies for a downward transition. The two formulas coincidentally agree only at `L=2`, so the assertion passes there and fails starting at `L=1` and `L=3` onward (the loop's first failure halts execution). Confirmed shallow: in an isolated scratch copy (never touching the committed file), replacing the two lines defining `al,bl` with the downward-oriented formula lets the script run to completion through all 80 shells with `PASS`, reproducing the exact `P_escape` values printed for `L=1,2,3,4,7,11` (`1/2, 3/4, 1, 5/4, 2, 3` respectively) — which match `c=j+1/4` at each `L`, confirming the ledger's stated mathematics is correct and only the script's implementation at that one spot used the wrong orientation.

## Missing reproducer: v15.921 (fifth instance)

**`Cone_Derivation_Ledger_v15.921_Gravity_Legacy_WebGL_AMGM_Circle_Hyperbola_Operator_Map.md` has no committed reproducer script.** Its "Verification" paragraph describes fetching the live `webgl/index.html` source and running an ad hoc SymPy check, but cites no script path, and no file in `research-notes/` references `921`. This is the fifth such instance in the project's history (after `v15.888`, `v15.890`, `v15.895`, `v15.897`, all flagged in Round 571) — the pattern had not recurred in the two intervening large batches (Rounds 572–573 covered 22 entries with full reproducer coverage), so this is a reappearance rather than a continuing streak. Every mathematical claim in v15.921 (the coordinate identities drawn from the live-fetched WebGL source) independently checks out by hand regardless.

## Honesty and scope assessment

A strong round scientifically: the hydrogen 3p/2p lifetime cross-check (v15.920) is a genuinely falsifiable, independently-sourced empirical test that passed, and is clearly and correctly scoped as standard atomic physics rather than a new Cone-specific prediction. The quarter-grid reconciliation sequence (v15.925–928) is careful, exact linear algebra that consistently and correctly reaches negative/conditional verdicts (no full representation intertwiner exists; site-dependent weights repair one-sided but not two-sided covariance). Gravity's own proactive avoidance of a sixth version collision is a genuine process improvement worth noting. No mathematical corrections needed anywhere in this round; one script-execution defect and one missing-reproducer instance to report.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.929
type: external-audit-round
status: actionable
action: (1) `k4_quarter_staircase_product_transport_v15_926.py` line 53 needs its lower-boundary `al,bl` formula corrected to the downward orientation `(j+m, j-m+1)` instead of the upward orientation `(j-m, j+m+1)`; the underlying claimed mathematics is correct, only the implementation needs the fix. (2) `v15.921` has no committed reproducer script — recommend adding one transcribing the inline checks already described in its text, consistent with the standing recommendation from Round 571.
deliverable: Round 574 independent audit of v15.918 through v15.928 (11 entries); one script-execution defect found and confirmed via scratch-copy fix, one missing-reproducer instance flagged, zero mathematical corrections needed.
