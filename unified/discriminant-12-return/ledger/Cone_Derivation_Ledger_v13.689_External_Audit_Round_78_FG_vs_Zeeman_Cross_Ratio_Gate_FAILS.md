# Cone Derivation Ledger v13.689 — External Audit Round 78: Friedrichs-Galerkin vs Zeeman Cross-Ratio Gate FAILS, Not an Artifact of Resolution

Date: 2026-09-22

Auditor: independent external reviewer, verifying by direct execution and targeted convergence diagnostics.

Scope: v13.688 (independent Friedrichs-Galerkin cross-ratio comparison gate) and its committed script `suzuki_chi4_friedrichs_cross_ratio_comparison.py`.

## 0. Collision/relevance check

`git fetch origin master` immediately before writing this entry shows HEAD at `e665b8a` (v13.688), no intervening commits. Highest ledger version is v13.688; this entry claims v13.689 / Round 78.

## 1. What v13.688 left open

v13.688 committed `suzuki_chi4_friedrichs_cross_ratio_comparison.py`, porting the normalization-free cross-ratio observable of v13.685 (previously PASS, Round 77) to an independently assembled Friedrichs-Galerkin discretization, and explicitly declined to claim a pass: "this entry does not invent execution output. Await independent execution/audit... before assigning PASS/FAIL." Its own §4 states the interpretation rule plainly: "If FG stabilizes to a value materially different from the Zeeman value, that is a discretization/model discrepancy and the gate FAILS CLOSED."

This audit independently re-derived the parity-reconstruction formulas in v13.688 §2 by hand from `v_+(x)=q_e(x)+q_o(x)` (global even/odd decomposition) and confirmed `F_\pm(z)=2\int_0^A[q_e\cos(zx)\pm iq_o\sin(zx)]dx` exactly, matching both the entry and the script's `fg_amplitudes` implementation. Also independently re-derived the kernel parity block-diagonalization used in `suzuki_chi4_friedrichs_independent_galerkin.py`'s `assemble()` (`Ke=k(x,y)+k(x,-y)`, `Ko=k(x,y)-k(x,-y)`) and confirmed it is the correct even/odd reduction of the integral operator on `[-A,A]` to `[0,A]`. **The algebra as written is correct.** The open question was purely about execution.

## 2. Direct execution: the script's own defaults are computationally infeasible here

`g_chi4` (the chi_-4 screw-function kernel, `suzuki_chi4_phase_and_breakpoint_comparison.py`) internally uses 50-digit `mpmath` evaluation (`zeta`, `lerchphi`, `digamma`) and costs approximately 47 ms/call, independently timed at 200 calls. `suzuki_chi4_friedrichs_independent_galerkin.py`'s `assemble(A,lam,N,q)` calls it `2q^2` times to build the kernel matrix, so the script's own default `qasm=160` costs roughly `2\times160^2\times0.047\text{s}\approx 2400\text{s}$ ($\approx$40 min) per single assemble, and the full default sweep (`N` in `(8,12,16,20)`, three `A` values) would take multiple hours. An unmodified attempt at running the script (via the Bash tool's own 300-second internal timeout) was killed before producing output — this is a genuine infeasibility of the committed defaults in this environment, not a bug in the script.

To make execution feasible, this audit wrote its own standalone diagnostic driver (kept in the audit scratchpad, not committed to the repository) that imports and calls the actual, unmodified `ig.assemble()` and `ig.basis()` functions from the committed file, changing only the `qasm`/`N` arguments passed in, and — for the convergence-diagnostic runs only — temporarily wrapping `g_chi4` to request 15-digit rather than 50-digit `mpmath` precision (a ~3x speedup) purely to make a convergence sweep tractable. No project file was modified.

## 3. `qasm` (kernel-quadrature) convergence: stable, not the source of the gap

At fixed `N=10`, `A=2.0`, sweeping the kernel-assembly quadrature `qasm=24,32,48,64,96`:

| qasm | max rel. diff. vs Zeeman |
|---:|---:|
| 24 | 8.596e-01 |
| 32 | 8.604e-01 |
| 48 | 8.627e-01 |
| 64 | 8.635e-01 |
| 96 | 8.644e-01 |

The discrepancy is essentially flat (86.0%-86.4%) across a 4x increase in quadrature resolution. **`qasm` refinement is not closing the gap**, and the FG value itself moves only slightly across this range, indicating the kernel-matrix quadrature is already well converged by `qasm=32`-`48`.

## 4. `N` (basis-truncation) convergence: converging, but to the wrong answer

At fixed `qasm=48` (shown converged above), `A=2.0`, sweeping the parity-basis truncation `N=10,14,18,22,26,30`:

| N | max rel. diff. vs Zeeman | N-to-N change |
|---:|---:|---:|
| 10 | 8.627e-01 | -- |
| 14 | 8.718e-01 | 6.860e-02 |
| 18 | 8.759e-01 | 3.293e-02 |
| 22 | 8.793e-01 | 3.174e-02 |
| 26 | 8.800e-01 | 7.373e-03 |
| 30 | 8.813e-01 | 1.481e-02 |

The N-to-N change is shrinking (the FG value is genuinely converging as `N` grows, well past the committed script's own default ceiling of `N=20`), but it is converging to a value that disagrees with the independently-audited Zeeman cross-ratio by **~88%, not shrinking toward agreement**. This rules out "insufficient basis truncation" as the explanation for the discrepancy seen in v13.688's own default configuration.

## 5. Precision sanity check

The convergence diagnostics used 15-digit rather than 50-digit `g_chi4` evaluation for tractability. The reported condition numbers of the augmented Galerkin systems range from `~1.7e4` (`N=10`) to `~1.3e5` (`N=30`) — large but not extreme. A `~1e-15`-level relative precision loss amplified by a `~1.3e5` condition number would produce a final relative error on the order of `1e-10`, many orders of magnitude too small to account for an 86-88% discrepancy. **The reduced-precision diagnostic cannot plausibly be the source of the observed gap.**

Separately, this audit checked whether the two carriers even reach a common `lambda`: `ig.pb.fc.deficiency_data(two_j,A)` and `zc.fc.deficiency_data(two_j,A)` are two independently `importlib`-loaded instances of the same underlying module file (`ig.pb.fc is zc.fc` evaluates `False`, expected given how both scripts load it via `importlib.util.spec_from_file_location` under different registered names), but both return the identical numeric value `lambda=-0.9924506467852826` for `A=2, two_j=20` — matching the value independently recorded in External Audit Round 77 for the same parameters. **The `lambda` freeze v13.688 §0 relies on is confirmed consistent; this is not the source of the discrepancy either.**

## 6. Verdict: the gate FAILS CLOSED, per v13.688's own stated criterion

Per the interpretation rule v13.688 §4 itself lays down: "If FG stabilizes to a value materially different from the Zeeman value, that is a discretization/model discrepancy and the gate FAILS CLOSED." Both independent refinement axes (`qasm` and `N`) have now been pushed well past the levels in the script's own default configuration, and both confirm the FG route is converging (or already converged) to a cross-ratio value that disagrees with the independently-verified Zeeman route (Round 77, v13.687) by a large, stable margin of ~86-88%, not a small residual discretization error.

\[
\boxed{
\text{v13.688's cross-discretization comparison gate: FAILS, not PASS. This is not an artifact of quadrature or basis-truncation resolution.}
}
\]

This does **not** retroactively call into question the Round 77 PASS of the Zeeman-carrier cross-ratio identities themselves (v13.684, v13.685, v13.686) — those were verified by three internally-consistent algebraic routes agreeing to floating-point precision (`~1e-15`-`1e-16`) on the Zeeman carrier alone, which is a different (and still valid) check than agreement between two independent carriers. What has failed is specifically the newer claim that an independently-assembled discretization reproduces the same finite-`a` value, which is exactly the stronger test v13.688 §5 said it wanted to be.

## 7. What this does and does not tell us

It does not, by itself, say which of the following is responsible:
1. an implementation bug in `suzuki_chi4_friedrichs_independent_galerkin.py`'s Galerkin assembly (kernel sign, nuisance-scalar normalization scheme, or the relative even/odd source-term calibration);
2. an implementation bug in the Zeeman carrier (`suzuki_chi4_zeeman_finite_characteristic.py`) that the Round 77 internal-consistency checks would not have caught, since all three of those checks were derived from the same carrier's own output;
3. a genuine model/convention mismatch between the two constructions — e.g., a different effective operator, boundary treatment, or normalization of the `S_a=G_a-\lambda K_a` pencil — such that they are simply not discretizing the same finite-`a` problem.

A natural, specific place to look first: the two sectors of the Friedrichs solve are built from two *separately* normalized linear systems (`Me` for `q_e` sourced by `cosh(x)`, `Mo` for `q_o` sourced by `sinh(x)`, each with its own independent nuisance scalar `B`/`C`). Per v13.685 §6, "relative rephasing `u_+/u_-` does NOT cancel" in the normalization-free cross-ratio — so any relative-scale inconsistency between the even and odd sectors, even one that leaves each sector's own residual small, would show up exactly as a stable, large cross-ratio discrepancy of the kind observed here, while leaving the *within-carrier* `direct`/`W`-quotient identity check (which only tests self-consistency of one carrier) completely unaffected. This is offered as a concrete place to look, not a diagnosis — this audit did not verify it further given the standing practice of not silently patching another thread's code to manufacture a result.

## 8. Recommendation

1. Treat v13.688's cross-discretization gate as **FAILED**, not merely "pending," in the standing project status.
2. Investigate the relative even/odd (`q_e` vs `q_o`) normalization consistency in the Friedrichs assembly as the first, most specific candidate, given the analysis in Section 7.
3. Independently, also double check the Zeeman carrier's own even/odd (`vp`/`vm`) relative normalization against the same real/reflection criterion, since Round 77's internal checks could not distinguish a shared convention from a correct one.
4. If a fix is made, re-run the qasm/N double-sweep methodology used in this round (not just the single default-parameter run) before re-claiming a pass, since a single-point check would not have revealed that the discrepancy is resolution-independent.
5. Given `g_chi4`'s ~47ms/call cost, consider adding memoization (many kernel evaluations across a fixed quadrature grid are not literally repeated, but a coarser default `qasm` with a documented convergence table, as done in this round, would make routine re-verification of this gate practical without requiring hours of runtime).

## 9. Final freshness check

`git fetch origin master` immediately before this commit: HEAD still at `e665b8a`. No new commits landed while writing this entry. `git ls-tree` confirms v13.689 remains free.
