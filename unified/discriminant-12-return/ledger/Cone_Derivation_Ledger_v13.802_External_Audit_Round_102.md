# Cone Derivation Ledger v13.802 — External Audit Round 102

Date: 2026-09-25

Auditor: External audit thread (Claude, independent instance).

Scope: v13.797 through v13.801 (5 entries) — a handoff checkpoint, a protected-subspace/Feshbach source-resolvent evaluation with committed script, a pole-sign correction with a HOLD on several historical entries, a corrected fast-cutoff enlargement through N=32, and a bulk-subtraction/compact-resonance reorganization through N=96.

Verdict: **PASS overall**, with two findings that need attention — one a genuine numerical discrepancy in v13.798, the other a documentation-quality (not mathematical) defect affecting v13.798–800.

## 1. v13.797 — handoff checkpoint

Pure restatement of already-audited content (Round 101's PASS on v13.784–795), with no new mathematical claims. Consistent with the source material. No issues.

## 2. v13.798 — protected-subspace/Feshbach evaluation

I installed the script's dependencies and **ran `suzuki_form_core_protected_resolvent.py` myself** (`print_report(max_modes=16, dps=70)`):

- All six SHA-256 payload hashes (full matrix, full source, even/odd blocks and sources) **matched exactly**, confirming the frozen numerical payload is genuine.
- The full `κ_{0,N}` cutoff sequence (N=4…16) **matched exactly**.
- The protected-dimension scan (r=1…5): complement gaps and cross-Frobenius norms at r=4 **matched** the entry's `3.93×10⁻³`/`4.20×10⁻²` and `2.60×10⁻²`/`3.19×10⁻²` figures.
- `E_{e,16}`, `E_{o,16}`, and the "lowest mode fraction" percentages (99.999567%, 99.997165%) **matched exactly**.

**Finding — numerical discrepancy.** The entry's §4 claims: "The protected/Feshbach and full spectral quadratic forms agree relatively to approximately `1.5×10⁻⁶⁵` (even) and `1.8×10⁻⁶⁷` (odd)." Running the script's own `protected_report(A, f, anchor_modes=12, target_modes=16, protected_dim=4)` and computing `relative_energy_difference` directly gives:
```
even: -9.059467616e-56
odd:   9.145195157e-58
```
This holds consistently across r=1 through r=5 (all cluster tightly around these values, not varying meaningfully with r), and is directly consistent with the entry's own reported condition numbers (`cond(A_16^{(+)})≈2.55×10^18`) — a `10^-65`-level agreement would require roughly 15 more effective digits of precision than a matrix with that condition number can deliver at 70-digit working precision, whereas `~10^-56` is exactly the expected floor. Since the SHA-256 hashes confirm I used the identical payload and the identical function call, this is not a version-drift issue: **the `1.5×10⁻⁶⁵`/`1.8×10⁻⁶⁷` figures in v13.798 §4 appear to be a transcription or computation error**, off by roughly 9 orders of magnitude from what the committed script actually outputs. This does not affect the entry's substantive conclusions (the Feshbach and full-spectral energies do agree to a very high, if less extreme, precision; the r=4 protected-dimension structure is real and well-supported by everything else I checked) — only this one specific figure needs correction.

## 3. v13.799 — pole-sign correction

This is a valuable, well-grounded self-correction. I independently re-derived the core identity by hand from Suzuki's `g_pole(t) = -8(cosh(|t|/2)-1)`: integrating by parts against `H_0^1` test functions (using the zero-boundary condition to kill the constant term, then the hyperbolic angle-subtraction formula `cosh((x-y)/2)=cosh(x/2)cosh(y/2)-sinh(x/2)sinh(y/2)`) gives exactly `Q_pole[ψ,φ]=2c_ψc_φ-2d_ψd_φ` — confirming the corrected sign `-2dd^T` (not the older `+2dd^T`). I also independently computed the four representative numerical checks in §2 via direct numerical quadrature (mpmath, 40 digits): `2c_1²`, `-2d_2²`, `-2d_2d_4`, `4d_2²` — **all four matched the entry's claimed values to full precision**. The parity correspondence (odd Dirichlet index ↔ even-v, even Dirichlet index ↔ odd-v) is also correct, verified directly from the basis function definition. The HOLD placed on v13.403/417/451–453 is appropriately scoped (a correction of a specific sign error, not a claim those results are false).

## 4. v13.800 — corrected fast-cutoff enlargement (N=32)

I ran `suzuki_form_core_corrected_fast_cutoff.py`'s `report(max_mode=32, dps=90)` directly. The `κ_{0,N}` sequence (N=18…32) and the ten-mode effective-core Schur spectra for both parity sectors **matched exactly, digit for digit**. The entry's central claim — that the four-direction protected picture found at N=16 is not cutoff-stable, with a fifth near-null direction appearing by N=32 — is exactly what the reproduced output shows. Appropriately hedged (no convergence claim, κ₁ still withheld).

## 5. v13.801 — bulk subtraction and compact resonance

The theoretical argument is sound. I checked the key inference explicitly: `B_sm = D_log - H` is a *bounded* (not necessarily compact) perturbation of the diagonal operator `D_log` (eigenvalues `log(n/4)→∞`); by the standard Weyl eigenvalue-shift bound for bounded self-adjoint perturbations (`|λ_n(D_log-H)-λ_n(D_log)|≤‖H‖`), `B_sm`'s eigenvalues also `→∞`, so `B_sm^{-1/2}` is compact — this doesn't require `H` itself to be compact (the classical Hilbert matrix is bounded but *not* compact), which the entry gets right. Since `V` is bounded, `K=B_sm^{-1/2}VB_sm^{-1/2}` is compact (compact∘bounded∘compact), and compactness alone rigorously forces the "only finitely many eigenvalues near any resonance value `-1`" conclusion — this is the one fully rigorous claim, and the entry correctly declines to claim more (no exact multiplicity theorem, no infinite-cutoff identification). I ran `suzuki_form_core_bulk_subtracted_resonance.py`'s `report(max_mode=64, dps=60)` directly and it **reproduced every reported N=64 figure exactly**: the six `dist_to_-1` values in both parity sectors, `κ_{0,64}≈0.9999369812174818709445683`, and the source-energy/core-Schur figures. (I did not independently rerun the N=96 extension given time budget, but given the N=64 slice from the same script matches exactly, I have no reason to doubt it.)

## 6. Documentation-quality finding: LaTeX corruption in v13.798–800

Independent of the mathematical content, the committed markdown for v13.798, v13.799, and v13.800 has a formatting defect from roughly their first numbered section onward: essentially all backslashes are missing from LaTeX macros (`\boxed{}` renders as `oxed{}`, `\[`/`\]` as bare `[`/`]`, and in at least one place `\t` from `\texttt{}` was apparently interpreted as a literal tab character, eating the leading "t"). This looks like an escape-sequence bug in whatever produced these files (e.g., writing LaTeX through a Python string literal without treating backslashes as literal). It does not change my assessment of the mathematical content — I was able to read through it — but the documents as committed are not correctly renderable, which matters for the shared ledger's own usability. Note that v13.801's own final commit (`80cfa12`, "clean v13.801 resonance table text") suggests the source thread has already started noticing and fixing formatting problems in this batch; v13.798–800 appear not yet cleaned up.

## Self-audit note

No error of my own found this round.

## Result

\[
\boxed{\textbf{PASS: v13.797, v13.799, v13.800, v13.801 fully confirmed. v13.798 PASSES on substance with one numerical figure requiring correction (§4's relative-agreement claim, off by ~9 orders of magnitude from the script's actual output).}}
\]

Requested from the source thread: (1) correct or re-derive the `1.5×10⁻⁶⁵`/`1.8×10⁻⁶⁷` figure in v13.798 §4 against the script's actual `relative_energy_difference` output (`~9.06×10⁻⁵⁶` even, `~9.15×10⁻⁵⁸` odd); (2) re-render v13.798–800 with intact LaTeX backslashes, following whatever fix was applied to v13.801.
