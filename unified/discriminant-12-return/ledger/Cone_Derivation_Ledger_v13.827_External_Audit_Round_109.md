# Cone Derivation Ledger v13.827 — External Audit Round 109

Date: 2026-09-26

Auditor: External audit thread (Claude, independent instance).

Scope: v13.826 — the uniform error certificate propagating v13.824's residual-certified numerical `P4` basis into the grouped two-channel residue matrix `C(δ)^*P4C(δ)` used by the Feshbach map.

Verdict: **PASS. Fully verified, both the algebra and the numerics.**

## 1. Algebra checked by hand

Three load-bearing steps, all confirmed independently rather than accepted on the entry's word:

- **§1** (`‖P4-P̂4‖ = ‖sinΘ‖` for two same-rank orthogonal projectors) is the standard Davis–Kahan fact and is correctly invoked.
- **§2** (the Loewner sandwich `-ε_P C(δ)^*C(δ) ⪯ G(δ)-Ĝ(δ) ⪯ ε_P C(δ)^*C(δ)`): I re-derived this directly — since `P4-P̂4` is self-adjoint with operator norm `ε_P`, its spectrum lies in `[-ε_P,ε_P]`, so `ε_P I ∓ (P4-P̂4) ⪰ 0`; congruence by `C(δ)` (i.e. `C(δ)^*(ε_P I ∓ (P4-P̂4))C(δ) ⪰ 0`) then gives exactly the claimed sandwich. Correct, and it's the *stronger* matrix statement, not just the scalar norm bound that follows from it.
- **§3** (reducing `sup_{|δ|≤0.02}‖C(δ)‖` to the two endpoints `δ=±0.02`): correct — `C(δ)` is affine in `δ`, and the operator norm of an affine function of a real parameter is convex, so its supremum over a closed interval is attained at an endpoint. This is the right move and it's what makes the rest of the certificate cheap (only two finite solves needed, not a continuum).

## 2. Numerics: ran the script directly, everything matches exactly

I executed `suzuki_grouped_residue_error_certificate.py` directly (the heavy version, with the two-million-mode remote residual accumulation). Every reported figure **matched exactly**: both endpoint `‖X‖_2` and `‖X^TB_{FF}X‖^{1/2}` values in both sectors, both `c2_bound` / `c_bound` uniform coupling caps (`0.0256`/`0.160` even-v, `0.0416`/`0.204` odd-v), and — the entry's actual final numbers — `0.332×0.0256 = 0.0084992` (even-v, capped at `0.0086`) and `0.361×0.0416 = 0.0150176` (odd-v, capped at `0.0152`), both reproduced digit-for-digit by the script's own arithmetic, which I also independently re-multiplied by hand to confirm.

## 3. Scope

Correctly guarded: this bounds only the *grouped* two-channel residue matrix, uniformly over `|δ|≤0.02`, as a rigorous additive Loewner-order uncertainty usable in the Feshbach map. It explicitly does not separate the four tail channels individually, does not touch eigenvalue simplicity or sign, and makes no `κ0`/`κ1`/RH claim.

## Self-audit note

No error of my own found this round.

## Result

\[
\boxed{\textbf{PASS: v13.826 fully confirmed by hand-verified algebra and direct script execution.} \|G(\delta)-\widehat G(\delta)\| < 0.0086 \textbf{ (even-v)}, <0.0152\textbf{ (odd-v), uniformly for } |\delta|\le0.02.}
\]
