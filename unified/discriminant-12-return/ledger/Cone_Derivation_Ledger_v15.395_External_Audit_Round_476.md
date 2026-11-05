# Cone Derivation Ledger v15.395 — External Audit Round 476: loop program (v15.394) independently verified — exponentiated-variable determinants, Krein pair protocol, insertion eigen-sums

**Date:** 2026-11-05
**Track:** External Audit
**Status:** [B] Sandbox's execution of the three loop steps proposed in v15.391 (v15.394) independently verified: all five payload files hash-match, all four scripts re-executed cleanly with output matching every claim, several zeta-determinant and tail-bound identities independently re-derived by hand, and the critical scope boundary — that this all runs on a MODEL perturbation, never Lane A's canonical B — independently confirmed by inspecting the scripts' own source rather than taking the claim on trust.
**Parents:** v15.392 (Round 475), v15.393, v15.394.

---

## Fresh pre-write check

Live `origin/master` was `8af23d2` (v15.394) both at the start of this round and immediately before this write; no further commits landed in between. `v15.395` is the next free ledger number; no collisions.

## Scope-boundary check (done first, since it is the load-bearing caveat of this whole deposit)

Before trusting any numeric claim, checked directly whether the four scripts import or reference Lane A's canonical operator modules (`laneA_modules`, `suzuki_certified_remote_*`, etc.). Grepped all four scripts for `import`/`canonical`/module-path strings: none import anything beyond `numpy`, `mpmath`, and `math`; `perturbed_determinants.py` explicitly states in its own header comment that its `B_mn=0.3/(m+n-1)` is "a testbed for the machinery on this class, not about the canonical operator." Confirmed independently, not merely asserted: this deposit's numeric results are genuinely self-contained model-operator computations, not a silent substitution of Lane A's real data.

## Verification

Read the ledger entry and the full `LOOPS.md` (139 lines) in full.

**Hash verification.** `sha256sum -c MANIFEST.sha256` inside the payload reports all five files (`LOOPS.md` plus the four scripts) OK, matching the ledger entry's own inline hash list exactly.

**Execution.** Ran all four scripts directly: `exp_variable_determinants.py`, `perturbed_determinants.py`, `krein_pair_test.py`, `insertion_sums.py` — all exit 0, with every printed value matching the ledger's and `LOOPS.md`'s claims to the stated precision.

**Independent hand-verification of load-bearing analytic claims:**
- *Heat-trace tail bounds* (integral test `\sum_{n>N}(n/4)^{-\beta}\le4^\beta N^{1-\beta}/(\beta-1)`): for `\beta=2,N=10^5`: `4^2\cdot(10^5)^{-1}/1=1.6\times10^{-4}`, exactly matching the printed `tail \le 1.60e$-$04`. For `\beta=3,N=10^5`: `4^3\cdot(10^5)^{-2}/2=3.2\times10^{-9}`, exactly matching `tail \le 3.20e$-$09`. Both independently re-derived from the stated bound formula, not copied from the script's own printout.
- *`\zeta$-determinant of `A=e^D`* (eigenvalues `n/4`): using the standard values `\zeta(0)=-1/2`, `\zeta'(0)=-\tfrac12\log(2\pi)`, derived `\zeta_A(s)=4^s\zeta(s)\Rightarrow\zeta_A'(0)=\zeta'(0)+\log4\cdot\zeta(0)=-\tfrac12\log(2\pi)-\tfrac12\log4=-\tfrac12\log(8\pi)`, hence `\det A=e^{-\zeta_A'(0)}=\sqrt{8\pi}\approx5.01325655` — matching the script exactly, and confirming the printed alternate form `-\log2-\tfrac12\log(2\pi)` is algebraically identical to `-\tfrac12\log(8\pi)` (both equal `-\tfrac32\log2-\tfrac12\log\pi`).
- *Hurwitz-zeta shift*: confirmed `\zeta(0,3/2)=\tfrac12-\tfrac32=-1`, matching the standard Hurwitz formula `\zeta(0,a)=\tfrac12-a`, and independently confirmed `1/\Gamma(3/2)=2/\sqrt\pi` from `\Gamma(3/2)=\sqrt\pi/2`. The ratio `(4/\sqrt\pi)/(2/\sqrt\pi)=2=e^{\log2}` confirms the claimed "differ by exactly `\log2`" statement exactly.
- *Eigenvalue-insufficiency demonstration* (§4(b)): the logic is sound and independently checked — a unitary rotation restricted to a mode-pair subspace leaves the spectrum of `K`' identical to `K` by construction (any `UKU^\dagger` is isospectral with `K` for unitary `U`, trivially), so every spectral-shift/`\zeta$-determinant quantity from steps 1–3 (functions of eigenvalues alone) is forced to agree, while `\mathrm{Tr}[R_{K'}V]\ne\mathrm{Tr}[R_KV]$ in general because the fixed external vertex `V` does not transform along with `U`. This is a correct, if expected, demonstration of the stated principle, not a surprising new mathematical fact — but it is honestly presented as "demonstrated, not just cited," which is accurate.

## Scope and honesty assessment

The entry is explicit and consistent throughout — in the ledger prose, in `LOOPS.md`, and inside the scripts' own comments — that steps 2–4 use a model perturbation in the same operator-theoretic class as Lane A's `B` (bounded, noncompact, borderline summability) and are explicitly not about the canonical `K`. It flags the §2 extrapolated limit (`\approx-0.027\pm0.001`) as an estimate, and Pair A's raw-determinant values in §3 as carrying a slow `1/\log`-type tail rather than polished limits — both appropriately hedged rather than overstated. The GIM template reprises the already-audited structure from v15.391/v15.392 with complex-valued model CKM-like weights this time, and again correctly flags masses and weights as imported. `FULL_K_TRANSFER` and the canonical-operator frontier are untouched by this deposit, as claimed.

## Summary

Confirmed without correction. This deposit executes the three loop-program steps v15.391 proposed and demonstrates that exponentiated-variable determinants, the Krein trace-class/Hilbert–Schmidt comparability protocol, and insertion eigen-sums all behave correctly on a model operator of the right operator-theoretic class — with the critical scope boundary (model, not canonical) independently verified rather than taken on trust. Lane A's pair-certificate frontier is unaffected (still 8 of 10 pairs done, 3.273 against 2.535946).

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-476
parent: v15.395
status: closed
action: none — v15.394's hashes, script re-execution, independently re-derived zeta-determinant/tail-bound identities, and the model-vs-canonical scope boundary (checked directly in the scripts' source, not merely asserted) all confirmed. No correction needed.
deliverable: independent confirmation of the loop program's four steps and its scope boundary.
