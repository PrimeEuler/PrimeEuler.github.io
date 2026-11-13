# Cone Derivation Ledger v15.861 — External Audit Round 565

**Date:** 2026-11-13
**Track:** External Audit
**Parents:** Round 564/v15.846, v15.847-v15.856 liveness, Sandbox v15.857, v15.858, v15.859, v15.860

## Fresh state at gate

`git fetch origin master` immediately before this write returns `75db6f4` (Sandbox's v15.860 payload manifest), identical to the head checked throughout this round's work. No version-number collision (`v15.861` confirmed free). This is the first Sandbox-track activity audited in this window (prior rounds covered only Lane A Suzuki and Gravity).

## v15.857 — HJ inversion on the cone's phase field, verified personally — confirmed defect found

Independently re-derived the bouncer action formula from scratch via direct integration: for constant force `F=ma`, the full-cycle action `J(E)=2∫₀^{E/(ma)}√(2m(E-max))dx` simplifies exactly to `(4√2/(3a√m))E^{3/2}`, matching the entry's stated formula exactly (confirmed with SymPy, difference simplifies to `0`). Independently re-derived the direct Hamilton–Jacobi check from scratch: with `S(x,E)=∫₀ˣ√(2m(E-Fx'))dx'`, computed `U:=E-(∂ₓS)²/(2m)` and got exactly `F·x`, matching the entry's claim exactly.

**However, re-executing the committed script as-is crashes**: `unified/discriminant-12-return/payloads/hj_inversion_v15_857/hj_inversion.py` calls `np.trapz` at three sites (lines 82, 96, 102), which does not exist in this environment's NumPy (`2.4.6` — `trapz` was removed in NumPy 2.0, renamed to `trapezoid`). The script raises `AttributeError` partway through the Kepler control check, before reaching the numeric round-trip section, directly contradicting the ledger's claim "Producer re-executed at staging, exit 0." This is analogous in kind (though not in author) to the shallow NumPy/SymPy API-compatibility defects found earlier in this audit's history (e.g. v15.787's `gi0` shape typo): a genuine, confirmed defect, but environment-dependent and shallow, not a math error.

To check whether the underlying claims survive, I copied the script to a scratch location (never touching the committed file) and replaced the three `np.trapz` calls with `np.trapezoid`. With that one-line-pattern fix, **every remaining claim reproduces exactly**: Kepler log-log slope `-0.5000`, numeric round-trip closures `1.00e-03` (linear) and `1.70e-08` (harmonic), and the `a=1,2,7` parameter-passthrough checks. The underlying mathematics is correct; the committed script is broken only by a NumPy-version incompatibility in this execution environment. No repair script exists yet for this in the Sandbox track's history; flagged for an additive fix following this project's established remediation pattern, without touching the original.

## v15.858 — the null channel, verified personally

Independently confirmed the shell identity `E²-p²=m²`, the null-surface fact `E=|p|` (giving `F=P/c` absorbing, `2P/c` reflecting from basic photon-momentum bookkeeping), and the rapidity relation `v/c=tanh ψ` as standard results. **Re-executed the committed script**: runs cleanly with no errors, reproducing every stated identity exactly (`F_∥=P/(c·tanh ψ)`, the null limit `F→P/c`, absorb/reflect momentum-rate bookkeeping).

## v15.859 — the leverage split, verified personally

Independently re-derived every claimed identity from the definitions `u=E+p`, `v=E-p`, `uv=m²`: confirmed `du=F(1+β)dt`, `dv=-F(1-β)dt` follow directly from `dp/dt=F` and the automatic relation `dE/dt=v·F` (itself forced by `E²=p²+m²`, not an independent assumption), confirmed the ratio `(1+β)/(1-β)=e^{2ψ}=u/v` exactly, and confirmed the response-share formulas `u/(u+v)=(1+β)/2`, `v/(u+v)=(1-β)/2` exactly. Independently resolved the "record's 1 MeV electron" figure: this means **total energy** `E=1`MeV (not kinetic energy) — with `m=0.511`MeV this gives `γ=1.9569`, `β=0.85958`, `ψ=1.291737`, and `e^{2ψ}=13.2431`, matching the entry's cited `13.24:1` split exactly (kinetic-energy convention would have given a different, non-matching number, so this confirms the correct reading of the entry's own convention). **Re-executed the committed script**: reproduces every spot-check value (`ψ=0,0.5,1.0,1.2917,2.0,3.0`) and the transverse-force null-first-order check exactly.

## v15.860 — the m/s tag addendum, verified personally

Independently re-derived the SI-unit restatement from scratch: with `E=γmc²`, `p=γmv`, confirmed `u=E+pc=γmc(c+v)` and `v=E-pc=γmc(c-v)` exactly, and the resulting ratio `u/v=(c+v)/(c-v)`. **Re-executed the committed script**: reproduces every value exactly, including the restated `13.2421:1` split and shares `0.9298/0.0702` (matching `(1±β)/2` with `β=0.85958` computed above).

## Honesty and scope assessment

This is a different track (Sandbox, exploratory physics directed by the project owner) from the Suzuki/Gravity work audited in prior rounds, but the same verification discipline applies and was applied in full: every claim was independently re-derived from first principles before checking the committed scripts, not just re-read and accepted. One genuine defect was found (v15.857's NumPy-version incompatibility), confirmed shallow via a scratch-only fix, and reported rather than silently patched. The other three entries (v15.858, v15.859, v15.860) are fully confirmed with no corrections needed. The material itself is consistently careful about scope: v15.857 explicitly frames the HJ-inversion result as confirming the action/phase-field machinery is "faithful... and transports laws without selecting them," not as a physical discovery, and v15.859 transparently discloses and corrects its own pre-build sign error in the entry text — exactly the kind of self-disclosure this audit's standing principles ask for.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.861
type: external-audit-round
status: actionable
action: v15.858, v15.859, and v15.860 are independently confirmed as stated with no corrections needed. v15.857's mathematics is confirmed correct, but its committed script (hj_inversion.py) crashes in this environment due to three np.trapz calls incompatible with NumPy 2.0+ (removed/renamed to np.trapezoid) — an additive repair script is needed, following the established remediation pattern (e.g. v15.692/v15.701, v15.792), without modifying the original file.
deliverable: Round 565 independent audit of v15.857 through v15.860 (first Sandbox-track audit in this window).
