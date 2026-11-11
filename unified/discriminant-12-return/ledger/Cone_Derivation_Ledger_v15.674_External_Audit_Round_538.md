# Cone Derivation Ledger v15.674 — External Audit Round 538

**Date:** 2026-11-11
**Track:** External Audit
**Parents:** Round 537/v15.672 (this thread's numbering), Lane A v15.672 (Taub-NUT chirality), v15.673 (G-free Poisson-source Xi)

## Fresh state at gate

`git fetch origin master` immediately before this write returns `3f28c3f` (Lane A's v15.673), identical to the head checked throughout this round's work. No new activity landed during verification. This round covers Gravity-lane (Taub-NUT/quarter-shell) entries, a return to that exploratory track after several Suzuki rounds.

## Version-number collision: v15.672

As with v15.667 and v15.670, two independent writers used `v15.672`:

- This audit's own Round 537, `Cone_Derivation_Ledger_v15.672_External_Audit_Round_537.md`, commit `0b9343f` at `2026-11-11T14:31:45Z`.
- Lane A's Taub-NUT chirality entry, commits `e12ba8b`/`8cd7942`, at `2026-11-11T15:00:25Z`/`15:02:13Z`.

This audit's Round 537 is earliest by actual commit timestamp and keeps the `v15.672` slot; Lane A's two `v15.672`-numbered files are flagged as the losing side and left untouched. Content is audited below under its own numbering regardless.

## 1. v15.672 (Lane A numbering) — Taub-NUT minimal gauge source chirality obstruction

This entry makes two claims: (a) a minimal Abelian gauge perturbation's first-order zero-mode block vanishes exactly, by a chirality argument; (b) a separately chosen bounded scalar profile `F_alpha` gives nonzero, exactly computable charge-raising matrix elements between the (b=7/2) zero-mode multiplets.

**Independent from-scratch verification**, not just re-running the witness's own code:
- Rebuilt the 4×4 Euclidean Clifford gamma matrices independently and directly confirmed `{gamma_a,gamma_b}=2 delta_ab I` for all 16 pairs, and `Π_+ gamma_a Π_+ = 0` for all four gammas, matching Gate 184's claim exactly.
- Independently recomputed the closed-form matrix-element formula `<n+1,a+1|M_F1|n,a> = sqrt(a+1)(p-n-1)^((n+2)/2)/(p-n)^((n+3)/2)` at `p=7/2` via a separate sympy calculation (not importing the committed script) and confirmed all three cited values exactly: `n=1,a=0 → 3*sqrt(6)/25 ≈ 0.293939`, `n=2,a=0 → sqrt(6)/27 ≈ 0.090722`, `n=2,a=1 → 2*sqrt(3)/27 ≈ 0.128300`.
- Re-executed the committed reproducer (`research-notes/tn_dirac_minimal_source_chirality_v15_672.py`, commit `e12ba8b`) directly; it printed `PASS`.

**Scope assessment:** the entry is carefully and repeatedly explicit that (i) this is a first-order, within-zero-modes statement, not a general no-go; (ii) the bounded profile `F` is an externally chosen, non-gauge-invariant source, not a derived physical current; (iii) no Lorentzian gravitational pair, Newton `G`, or physical coupling is claimed. This matches the actual mathematical content exactly — no overclaiming found.

## 2. v15.673 — G-free Poisson-source Xi diagnostic

This entry re-expresses the already-audited dimensionless rotor ratio `Xi` as a normalized Poisson-source trace diagnostic and runs three algebraic separating tests.

**Independent hand derivation** (spherical Hessian eigenvalues `lambda_r=Phi''(R)`, `lambda_t=Phi'(R)/R`, `Xi=(lambda_t-lambda_r)/(3 lambda_t)`):
- For `Phi = -A/R - Lambda c^2 R^2/6`: computed `lambda_r=-2A/R^3-Lambda c^2/3`, `lambda_t=A/R^3-Lambda c^2/3` by hand, matching the entry exactly; their sum gives `tr Hess Phi = -Lambda c^2` and difference gives `lambda_r-lambda_t=-3A/R^3`, both matching exactly; substituting into `Xi` gives `Xi_SdS = 1/(1-Lambda c^2 R^3/(3A))`, matching exactly.
- For `Phi_B = -A/R - B/R^3`: computed `lambda_r=-2A/R^3-12B/R^5`, `lambda_t=A/R^3+3B/R^5` by hand; `Xi_B` simplifies to `(A R^2+5B)/(A R^2+3B)` exactly as claimed, and `∇²Phi_B = -6B/R^5` exactly as claimed.
- For the point-source half-radius scaling test (`Phi=-A/R`): confirmed by hand that `Phi'(R/2)/Phi'(R)=4` and `Phi''(R/2)/Phi''(R)=8`, with `Xi` scale-invariant, matching the entry's claim.

Re-executed the committed reproducer (`research-notes/gravity_xi_poisson_source_v15_673.py`, commit `cbbbdf3`) directly; it printed `PASS`.

**Scope assessment:** the entry's own stated verdict — that `Xi` is a standard-gravity diagnostic that cannot by itself distinguish a Cone-specific source from ordinary matter/`Lambda` contamination, and that the quarter/half-grid labels do not survive as a distinct physical prediction under scale covariance — is fully supported by the algebra above. No G-free physical prediction or new force is claimed or found; the entry is explicit about this, correctly.

## Honesty and scope assessment

Both entries are methodical negative/clarifying gates on the gravity exploratory track: v15.672 closes off a native physical source for the TN charge ladder absent an externally supplied field, and v15.673 closes off the half/quarter-grid `Xi` route as a distinct physical prediction. Neither overclaims; both are consistent with the entire gravity-lane history already audited in Rounds 520-533. No correction to either entry, or to this audit's own prior work, was needed this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.674
type: external-audit-round
status: actionable
action: v15.672 (Lane A numbering, TN chirality obstruction) and v15.673 (G-free Poisson-source Xi diagnostic) are both independently confirmed as stated, including from-scratch re-derivation of the core algebra (Clifford relations, chiral projection, matrix-element closed form, Hessian eigenvalue identities) rather than only re-running the committed scripts. Both entries correctly close their respective negative gates; no physical prediction survives either track, as both entries themselves state.
deliverable: Round 538 independent audit of v15.672 (Lane A numbering) and v15.673.
