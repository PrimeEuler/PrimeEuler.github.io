# Cone Derivation Ledger v15.718 — External Audit Round 545

**Date:** 2026-11-11
**Track:** External Audit
**Parents:** Round 544/v15.707, Lane A v15.708-v15.715

## Fresh state at gate

`git fetch origin master` immediately before this write returns `4b17fc2` (Lane A's v15.717, two entries beyond what this round covers). This round covers v15.708 through v15.715, which were fully verified before v15.716/717 landed; those two will be covered in the next round. No version-number collision in the covered range.

## v15.713 — verified personally, in depth

**v15.713** (sourced K4 scalar Ward identity; audit-alert on the original archived `v14.935` `scalar_statespace.py`): this required direct, from-scratch investigation of the *original archived chain* (not just Lane A's new reproduction), since the entry explicitly requested this and the finding concerns previously-certified historical content. Ran the literal unmodified original scripts in `payloads/k4_full_svt_v14_935/` end to end (`tensor_check.py → matter_sector.py → eh_scalar.py → assemble.py → scalar_statespace.py`), regenerating `scalar_reduced.pkl` from scratch.

**Confirmed, exactly, via `sympy.simplify(...)==0` on the fully symbolic (pre-numeric-substitution) expressions — not just at the cited sample point:** the psi Euler-Lagrange equation's coefficients of `psi`, `P`, `psi_dot`, `P_dot`, `psi_ddot`, and `P_ddot` are *all* identically zero, and the full source-free `E_psi` expression simplifies to exactly `0`. Separately confirmed the coefficient of `psi` in the *P*-equation (`C20`) is also identically zero. This fully substantiates Gate 310's claim that the psi-equation carries no psi/P information at all, so `alpha=-C01/C00` is a genuine `0/0`.

**However, a precise correction to the entry's specific wording is warranted.** Running the literal original `scalar_statespace.py` (unmodified, as archived) does **not** raise a Python `ZeroDivisionError` or visibly fail, contrary to the phrase "gives e1=0 and a Python 0/0 division." Floating-point evaluation of the `sqrt(3)`-laden substitutions leaves `C00`/`C01` as tiny (~1e-15–1e-16) nonzero residues rather than exact 0.0, so `alpha=-C01/C00` silently computes a numerically meaningless but finite value (confirmed at the cited `eta=3/4, k/H=10` point: `alpha=-1.55078125`, derived from pure floating-point noise). The script therefore runs to completion and prints a full table with no visible error.

**More importantly, this floating-point accident does not actually corrupt the archived table's numbers.** Because `C20` (the coefficient multiplying `alpha` in `Ceff=C21+C20*alpha`) is *also* tiny floating-point noise (~1e-16) rather than exact zero, the contaminating product `C20*alpha` stays at the ~1e-16 scale — negligible against the true `Ceff≈146.7` at the tested point. Direct computation confirms `Ceff` as the script computes it matches the symbolically-exact `C21` (with `C20` treated as exactly 0) to full double-precision agreement (`relative difference: 0.0`), and this value equals `106/3 · A22` exactly, matching Gate 311's independently-derived closed form `omega_S²=(8η/3)H²+(-1/3+8η/9)k_phys²` (independently re-derived by hand from the stated `A_P`, `B_P/A_P`, `C_P/A_P` formulas, confirmed exactly).

**Net assessment:** Lane A's substantive finding is fully confirmed — the `psi=alpha·P` elimination step in the archived `v14.935` script is mathematically ill-defined, and this is a real reproducibility concern worth flagging and repairing (as the entry itself requests). But the specific claim of an actual runtime `0/0` crash does not hold: the real script runs clean and, at least at the tested grid points, its printed numbers are not actually numerically corrupted, because the floating-point noise in the contaminating term happens to stay negligible relative to the true coefficient. This is a more fragile, "right-answer-by-luck" situation than a clean crash would be — arguably a subtler and more concerning defect, not a milder one, since nothing in the method guarantees the noise will always stay negligible at every grid point. This nuance should be carried into any future repair: the fix should replace `alpha=-C01/C00` with a derivation that does not depend on dividing two quantities that are symbolically zero, not merely suppress the visible symptom.

**v14.935's previously-certified physical conclusions are not overturned by this finding**, consistent with the entry's own careful framing: the scalar dispersion relation itself is independently reproduced via the genuine propagating P-equation (Gate 311), bypassing the flawed elimination step entirely.

## v15.708-v15.712, v15.714 — verified by three background forks

- **v15.708** (common conserved Fourier stress, SVT source projectors): the conservation identity, the `Q_T+Q_V+Q_S=Q` decomposition, mutual orthogonality, and the three projector norms (`N_T+N_V+N_S=2/3`) were independently re-derived by hand; both scripts confirmed byte-identical to their commits and re-execute to their cited `PASS` lines.
- **v15.709** (gauge-invariant SVT tidal response): the full six-component `R_{0i0j}` tidal tensor was independently re-derived from the standard linearized-Riemann formula; the scalar-ratio and vector-cancellation identities confirmed exactly. Script confirmed byte-identical, re-executes cleanly.
- **v15.710** (sourced vector shift, pole residue): the Schur-complement elimination, transfer function, pole residue, and coasting-background reduction `ω_V²=(8η/3)+(2η/3)k_phys²` were independently re-derived by hand; all match exactly. Script confirmed byte-identical, re-executes cleanly.
- **v15.711** (sourced scalar auxiliary Hessian): the coasting Hessian, its determinant, and both sourced lapse/shift response components were independently re-derived via direct 2×2 matrix inversion; all match exactly. Script confirmed byte-identical, re-executes cleanly.
- **v15.712** (full scalar sourced mixed coupling): independently reconstructed from the actual archived pickles (not from the script's own regeneration) and cross-checked the Fourier-substitution convention against the original `assemble.py`; all claimed formulas (Hessian, mixed-coupling vector, kinetic-rank coefficients) matched exactly. Script confirmed byte-identical, re-executes cleanly.
- **v15.714** (sourced scalar retarded Green's kernel): the characteristic roots, Wronskian, retarded Green's function, boundary conditions, marginal-`η` limit, and particular-solution amplitude were all independently re-derived by hand from the stated ODE; all match exactly. Script confirmed byte-identical, re-executes cleanly.

No recurrence of the bare-`==` SymPy equality bug in any of these six scripts. No overclaiming found in any of the six entries — each is explicit about the formal, not-yet-physically-normalized status of its source coefficients (`J_Phi`, `J_B`), and none claims a complete physical gravitational-wave transfer function or new observable.

## v15.715 — Suzuki R6 fully streamed scaling, verified personally

**Hand-checked** the exact cut-count formula `|K_6|=(2·6+3)(2·6+1)^3=15·13^3=32955` and the dimension formula `(2·6+1)^4=13^4=28561`, both matching the ledger exactly. Read the script and confirmed it is the audited v15.704 architecture applied unchanged at `R=6` — no new error-propagation logic requiring re-derivation.

**End-to-end re-execution** of the committed script (SHA-256 confirmed by local `sha256sum` equal to the ledger's cited `1905fe6b...1b227eb` [full: `1905fe6b8d0e936f049379e38cec9eaafe80dbf425a3f9b7d8b32bbf51b227eb`]). Reproduced exactly: unique arc index `16477` containing `x=1` with margins `3.5920545746366354e-05` on both sides; dimension `28561`, `nnz(B)=948428`; all five checkpoint weight hashes; `weight_condition=675.1610284977405`; `certified_argmax=1306`; `outward_weighted_b4=158.26381150127094`; `outward_fourth_root=3.5468710959553458`; `pass=true`; `construction_peak_nnz_by_stage=[4976,48249,194276,480402]`; `max_row_lengths_by_stage=[40,403,1715,4557]`; `formed_global_b2_or_b4=false`. All match exactly (timing/RSS varied with machine load, as expected).

**Scope assessment:** correctly reports this as one measured scaling point (R5→R6: dimension ×1.95, construction time ×2.09, peak RSS ×1.53), explicitly not an R16 extrapolation certificate. No overclaiming found.

## Honesty and scope assessment

This was a demanding round requiring genuine historical-code archaeology (v15.713) rather than only checking new work. The substantive finding there — that the archived `v14.935` auxiliary-elimination method is mathematically ill-defined, though its printed numbers happened not to be corrupted by the resulting floating-point noise — is reported with the precision the standing honesty obligation requires: neither overstating Lane A's description (no crash actually occurs) nor understating the real defect (the method remains unsound and needs a proper fix, not just a reassurance that today's numbers look fine).

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.718
type: external-audit-round
status: actionable
action: v15.708-v15.712, v15.714, and v15.715 are all independently confirmed as stated. v15.713's core finding is confirmed but its description should be corrected: the original v14.935 scalar_statespace.py does not crash with a visible 0/0 when re-run (floating-point noise masks the exact symbolic zero), and its archived table's numbers were not actually corrupted at the tested points — but the method itself is still genuinely unsound and the recommended additive repair should replace alpha=-C01/C00 with a derivation that never divides two quantities that are symbolically zero, rather than one that merely avoids visibly crashing.
deliverable: Round 545 independent audit of v15.708 through v15.715 (eight entries), with an in-depth historical-code investigation of the v15.713 audit alert.
