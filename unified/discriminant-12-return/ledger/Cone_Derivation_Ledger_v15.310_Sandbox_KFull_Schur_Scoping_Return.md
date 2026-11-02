# Cone Derivation Ledger v15.310 — Sandbox: Schur-route scoping return for the v15.232 transfer alternative (measured tail norms, stopping scale, Route B design)

Date: 2026-11-02. Lane: sandbox (little Euler). Parents: v15.227, v15.232, v15.303, v15.304, v15.305, v15.306, v15.308 (Audit R450 verified the v15.303–v15.307 batch; the §1 floor constant is independently certified there), v15.309. Status: [N] numerical scoping (float model, finite windows) + [D] closed-form floor evaluation. NOT a certificate. FULL_K_TRANSFER remains INCONCLUSIVE. Payload: payloads/kfull_schur_scoping_v15_310/ (tail_norm_probe.py, floor_check.py, probe_output.json/txt, floor_check_output.json, SPEC_DRAFT.md, census.py, dominance.py, dominance_output.json, PROTOTYPE_REPORT.md, rho_sensitivity.json, MANIFEST.sha256).

## What this returns

The v15.232 handoff asked sandbox/external-audit for a rigorous alternative transfer proof or a resource-certified large-block result. Lane A's v15.303–v15.305 reframed the alternative as the Schur/Feshbach route and named its affordability lever: the true tail-block norm M_N = ||Q_N B Q_N|| and the off-block ||V_N||. This return measures those quantities on the frozen kernel (DERIVATION §0; z via the float model `z_float`, p_n via the float form of L*n/(n^2+t)) and prices the route. All norm figures are finite-window estimates and therefore LOWER bounds for the true compression norms; nothing here is interval-certified, and no certified stage may quote them (certification stages must use the certified z/diagonal evaluators and exact floored p_n).

## 1. The v15.305 floor, evaluated

A = 8 * sum_{q in {2,3,4,5,7}} w_q^2 sin^2(theta_q) = 6.70411705806156354127349965482 (50-digit), so the proven floor is

(|c|/4)*sqrt(A) = 0.412088908974624345.

Independent check inside the probe: the Cesaro mean of |z_{n+2} - z_n|^2 computed from `z_float` over 2*10^6 samples per lattice (n in [1e5, 4.1e6)) is 6.704125 (odd lattice, rel. err +1.2e-06) and 6.704115 (even lattice, -3.7e-07) — the adjacent-difference mechanism of v15.305 reproduces in the float evaluator.

## 2. Measured tail norms: a persistent constant near 1.9–2.0

||Q_N B Q_N|| window estimates (extremal eigenvalues of B compressed to the first W sector-lattice modes above cutoff N):

- odd lattice (b=512001, sigma=+1): 1.8885 – 1.9202 over N in {1e3, 1e4, 1e5, 5e5}, W in {2000, 4000}
- even lattice (b=512002, sigma=-1): 1.9151 – 1.9669, same grid

Flat in N, 4.6–4.8x the floor at every cutoff, inside the proven band [0.4121, 15]. Consistent with v15.305: M_N is a persistent constant, not a decaying one. (Model-risk note: quote no tighter than ~±0.05; a slow log-creep with window size, cf. the DERIVATION §3 truncation probe, is not excluded by 2000–4000-mode windows.)

Off-block scale indicator: ||V|| for the v15.227 remote J=100 block against its full complement (chunked Gram; above-block part truncated at 2*10^4 modes, residual ~2.8e-04/col) is 0.8677 (odd) / 0.8835 (even) — above the Gate-2 floor, as expected for a sharp block. This is NOT v15.304's prefix ||V_N||; it is a scale indicator only.

## 3. Stopping scale at measured constants

v15.304's rule N_stop = 4*exp(b_int + C + M_N) - 2, C = 1.745855454249828, b_int = 10.45 (odd) / 10.30 (even):

- at crude certified M = 15: 2.59e12 (odd) / 2.23e12 (even) — Lane A's figure, reproduced.
- at measured M_N ~ 1.9–2.0: ~5.2–5.4e6 (odd) / ~4.6–4.9e6 (even).

All scales at measured M_N are CONDITIONAL: they become certified only when a certified M-hat >= ||Q_N B Q_N|| exists. That bound is Lane A's named analytic gate; this return does not supply it and does not compete with it. (Update at deposit: Lane A's v15.309 has since certified M-hat < 12.84, giving a certified stopping scale ~4.0e11 — still infeasible; the measured-constant scales above are unaffected.)

## 4. Two negative scoping facts

(a) The coarse A_N-only acceptance test of v15.304 is not viable at the v15.227 gap scale: the residual ||V||^2/g is 0.38–7.8 for g in [0.1, 2] against certified gaps 0.004151 (odd) / 0.012958 (even) — 30x to 1800x too coarse. v15.305 Gate 2 (limsup ||V_N|| >= 0.4121 for sharp prefixes) rules out rescuing it with a smaller prefix coupling.

(b) The literal prefix route is not executable densely: at measured M_N the stopping index ~5e6 physical is ~2.5e6 lattice modes per sector in P_N (~1e13 dense entries). The stopping rule certifies the tail cheaply; the finite side is the bottleneck.

## 5. Executable shape: Route B (resonant-mode P), design summary

Per v15.303's resource-saving candidate: P = certified resonant modes (diagonal enclosure meets a guarded interval [a-rho, b+rho]) plus the v15.227 J=100 block, target |P| <= ~1e3–1e4. Q splits into a high part (positive by the stopping-rule argument, zero negative inertia) and a bulk part whose inertia is counted by banded interval diagonal-dominance, with dominance failures promoted into P. Schur assembly on P with outward-certified tail-sum remainders and epsilon_F-widened enclosures (epsilon_F ~ 0.49/0.52 at g=1, 0.18/0.19 at g=2 at measured constants). Full pipeline, interval-rounding checklist (6 items), and risks in the payload SPEC_DRAFT.md.

Go/no-go experiments, in order: B1 resonant census and B2 dominance pass rate on the odd sector. Hard stop if |P| or the failure rate exceeds the spec targets.

**Prototype outcome (same day, payload PROTOTYPE_REPORT.md): Route B as specified is NO-GO.** B1 hard-stopped: certified enclosure classification crossed the 20,000 hard-stop after 20,364 evaluations (at n = 553,043, under 1% of the census range), so |R| > 2*10^4 is certified for rho = 2.5; the float census over all 4,535,446 lattice modes to the log-clearing index n_max = 9,582,891 gives |R| ~ 7.9*10^5 (17.4% of all modes), with a 200/200 float-vs-certified spot check (max midpoint deviation 1.23e-06). The failure is structural, not tuning: the guard window (width 2*rho ~ 5.0) dwarfs the diagonal oscillation amplitude (<= ~1.75), so a value-based guard captures a positive fraction of all modes; sensitivity (float): rho = 1.0 -> 54,693; 0.5 -> 13,292 (already over target); 0.25 -> 4,814 — but the guard must dominate the coupling at M-hat ~ 2, not shrink below it. This return's spec planning guess of 1e2–1e3 resonant modes was wrong by ~3 orders of magnitude (it extrapolated the delta-strip density to a ~2400x wider window) and is retracted. B2 was not run (gated off by B1); its invited diagnostic confirms l1 Gershgorin row sums diverge logarithmically for this kernel, disqualifying l1 row-sum dominance. census_output.json (2.7 MB) is hash-listed in the payload MANIFEST.sha256 and retained in the sandbox run dir, regenerable via census.py.

## 6. Gate status

FULL_K_TRANSFER = INCONCLUSIVE, unchanged. This return supplies resource scoping [N] for the Schur alternative and a design whose proof-grade form remains conditional on Lane A's analytic M-hat (Risk R1 of the spec); the design's Route B branch is NO-GO as specified per the §5 prototype outcome. No full-K gap or count is claimed. The v15.227 finite-section certificates stand as deposited. Frozen production objects (C_S_32000, thresholds 3e-5 / .002, exactly-once charges) untouched.
