# Cone Derivation Ledger v15.915 — External Audit Round 572

**Date:** 2026-11-13
**Track:** External Audit
**Parents:** Round 571/v15.904 (mine), Gravity v15.904 (Inner n+1 Frequency Test) through v15.914

## Fresh state at gate

`git fetch origin master` immediately before this write returns `ee15ad8` (Gravity's v15.914), identical to the head checked throughout this round's work. No further new commits landed during this round's writing.

## Version-label collision: v15.904 (fifth collision, NOT self-resolved)

Both `Cone_Derivation_Ledger_v15.904_External_Audit_Round_571.md` (mine) and `Cone_Derivation_Ledger_v15.904_Gravity_Inner_NPlusOne_Frequency_Test.md` (Gravity's) now exist on disk under the same version number. Per the established UTC-timestamp-priority protocol:

- My commit `f58cd1a`: `2026-11-13T19:29:31+00:00`
- Gravity's commit `b78120d`: `2026-11-13T14:33:18-05:00` = `2026-11-13T19:33:18Z`

My commit precedes Gravity's by 3 minutes 47 seconds, so my Round 571 entry correctly holds the `v15.904` slot. **Gravity's file is flagged but not renamed, edited, or touched.** Unlike the three earlier collisions in this project (v15.836, v15.864, v15.877), which Gravity self-resolved before I reached them, this is the second collision (after v15.889) that was **not** self-resolved and required the auditor to flag it. Gravity continued its sequence at v15.905 without renumbering the colliding v15.904 file.

## v15.904 through v15.914 — the Schwinger-ladder/action-circle sequence, verified personally

An eleven-entry sequence (Gravity's v15.904 plus v15.905–914) connecting the earlier two-circle geometry to the project's existing Paper C Schwinger SU(2) dictionary, testing whether any physical frequency, force, or EM/gravity coupling selector falls out of the construction. Every entry in this batch **has a committed reproducer script** — the four-entry missing-reproducer trend flagged in Round 571 (v15.888, v15.890, v15.895, v15.897) did not continue into this batch.

I independently re-derived the key claims from scratch (fresh SymPy/NumPy/SciPy, before checking any committed script):

- **v15.904** (rotor/frequency compatibility): confirmed `ω_i/ω_o − γ_n² = 0` for `γ_n=(n+1)/(2√n)`, and that the two routes to `L_n` (via inner vs. outer assumed rates) agree exactly, giving `L_n = M(ℓ*u)²n(n+1)ω*`.
- **v15.905** (Paper C Schwinger embedding): confirmed `N=n`, `T=(n+1)/2`, `Y=√(xy)=√n`, `T²−X²−Y²=0`, Casimir `j(j+1)=n(n+2)/4` (not `n(n+1)`), and `T²=j(j+1)+1/4` exactly.
- **v15.906** (diameter–secant ladder): confirmed `cos²φ+sin²φ=1`, `coth(ψ)=(n+k)/(n−k)` numerically (n=7,k=2: both give 1.8), and the example table at D=5.
- **v15.907** (chord-squared operator / leakage): confirmed the D=5, (4,1) two-way leakage coefficient `(nk+(n−1)(k+1))/4 = 5/2` exactly.
- **v15.908** (EM/tidal comparator): confirmed the (4,1) squared right/left ratio `nk/[(n−1)(k+1)] = 2/3`.
- **v15.910** (Heisenberg equations): confirmed `[J_x,J_z]=−iJ_y` convention gives `d⟨X⟩/dt=gu⟨J_y⟩` and `d²⟨X⟩/dt²=−g²u⟨J_z⟩=−g²(⟨X⟩−u/2)`.
- **v15.911** (D=5 dark-node distribution): independently built the j=2 SU(2) `J_x` matrix and computed `exp(−iπJ_x/2)` acting on the `|3,1⟩` initial state from scratch: reproduced the exact dark-center distribution `(0.25,0.25,0,0.25,0.25)` at `τ=π/2`.
- **v15.912** (tidal detuning): independently rebuilt the finite-D projection and the detuned evolution; reproduced `P_center` at `A/B=0.2,0.5,1` as `0.00010977201163581694`, `0.004126498548491597`, `0.0560361235824451` — exact matches to the ledger's cited figures.
- **v15.913** (velocity-operator no-go): confirmed symbolically that `[Q,P]=iħI` cannot hold on a finite-dimensional space (trace argument) and that the parity/selection-rule argument for `P_N v_i P_N=0` is sound.
- **v15.914** (full tidal evolution benchmark): independently reconstructed the full two-mode Fock Hamiltonian (Nmax=13, 105 states) and reproduced the entire cited table exactly: `⟨K_diff⟩,⟨C⟩,P(N=4)` at t=0,2,8,16,24 all matched to the printed precision, and the normal-mode frequencies `ω_+=1.0437637276222964`, `ω_−=0.9542312512698421`, splitting `0.08953247635245432` matched exactly.

**Re-executed all eleven scripts.** Ten ran to completion with PASS. **One genuine shallow defect found: `k4_fermi_tidal_full_shell_projection_v15_912.py` crashes with `TypeError: bad operand type for abs(): 'numpy.flatiter'`** at both assertion lines (lines 32–33), from writing `max(abs((...).flat))` instead of `np.max(np.abs(...))` — `.flat` returns a `numpy.flatiter`, which Python's builtin `abs()` cannot operate on. Confirmed shallow: in an isolated scratch copy (never touching the committed file), replacing those two lines with `np.max(np.abs(HA[np.ix_(ids,ids)]-jz))` and `np.max(np.abs(HB[np.ix_(ids,ids)]-jx))` lets the script run to completion and print exactly the detuning values independently re-derived above, plus `PASS`. The mathematics in v15.912 is correct; only the committed script fails to execute.

## Honesty and scope assessment

A long, internally disciplined sequence consistent with this project's established epistemic hygiene: every entry carefully distinguishes operator-level SU(2) structure (exact, standard) from an unselected physical frequency/force/coupling scale (never supplied by geometry alone), explicitly tests and rejects several more tempting identifications (SU(2) Casimir is not the n(n+1) needed for the rotor hypothesis; literal oscillator velocity has an exact parity no-go against the Cone's X coordinate; a geometric osculating parabola cannot generate SU(2) ladder transitions because it is diagonal). The negative/conditional verdicts are correct and well-supported wherever I could independently check them. No mathematical corrections needed beyond the one script-execution defect in v15.912.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.915
type: external-audit-round
status: actionable
action: (1) Gravity's `Cone_Derivation_Ledger_v15.904_Gravity_Inner_NPlusOne_Frequency_Test.md` collides with my own `v15.904_External_Audit_Round_571.md`; by UTC commit-timestamp priority (mine `f58cd1a` at 19:29:31Z precedes Gravity's `b78120d` at 19:33:18Z), my file correctly holds `v15.904` — Gravity should move its content to a new free version number, as was done after the v15.836/864/877/889 collisions. (2) `k4_fermi_tidal_full_shell_projection_v15_912.py` needs a one-line fix on its two assertion lines (replace `max(abs((X).flat))` with `np.max(np.abs(X))`); the underlying mathematics and all cited numeric values are independently confirmed correct.
deliverable: Round 572 independent audit of v15.904 (Gravity) through v15.914 (11 entries); one collision flagged, one shallow script-execution defect found and confirmed via scratch-copy fix.
