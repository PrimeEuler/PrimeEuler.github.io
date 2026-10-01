# Cone Derivation Ledger v13.913 — External Audit Round 133

Date: 2026-10-01

Auditor: External audit thread (Claude, independent instance).

Scope: v13.912 — the de Branges odd-sector invertibility question (`0 ∈ σ(L_A^{(-)})`?), posed in response to a direct request to ledger this parked item.

Verdict: **PASS on the analytic identity's logic (§3), checked by inspection and against its own cited predecessor's definitions. The numerical divergence claim (§4) is internally consistent and appropriately scoped, but I could not independently verify it this round — it rests on a substantially different, older, more intricate piece of machinery (deficiency vectors, a comparison kernel `N(x,y)`, reflection operators spanning v13.740s–758) than this week's self-contained rigidity arc, and reconstructing it correctly from scratch would need more context-absorption than this round's budget supports. Flagging this honestly as a scope boundary, not a finding either way.**

## 1. Why this entry is different from the rest of this week's batch

Everything audited in Rounds 129–132 (the `Λ`-rigidity arc, v13.894 onward) used a single, self-contained object — Suzuki's `g(t)` from formula (1.3), which I independently built, validated against the primary-source PDF, and reused across six separate checks this week. `v13.912` instead belongs to an older, separate thread (`v13.757`, `v13.758`, dated 2026-09-24, predating this week's work entirely): a finite-interval operator `L_A` with kernel `k(x,y)=g(x-y)-λN(x,y)` at `λ=-1`, deficiency vectors `v_{A,±}`, a reflection operator `R`, and moment functionals `ℓ_{0,A},ℓ_{1,A}` built from all of this. I do not have an independently-built, validated implementation of this object the way I do for the rigidity arc's `g(t)` — building one correctly would require first fully absorbing `N(x,y)`'s definition and the deficiency-vector normalization from `v13.745` and earlier, none of which I've read this session.

## 2. The analytic identity (§3) — logic verified by inspection, consistent with its cited source

Pulled `v13.758` directly to confirm the moment definitions match what `v13.912` uses: `M_{1x} = ℓ_{1,A}(R_A^{(-)}x)` (line 85), with `ℓ_{1,A}(v) = ∫k_x(0,y)v(y)dy` (line 25) — exactly matching `v13.912`'s own restatement. Given these definitions, the identity's derivation is a direct, correct application of differentiation under the integral sign: if `u=L_A^{-1}x` (i.e. `u=R_A^{(-)}x`) solves `F(x):=\int k(x,y)u(y)dy=x` for all `x`, then differentiating both sides in `x` gives `F'(x)=\int k_x(x,y)u(y)dy`, and evaluating at `x=0` gives `F'(0)=\int k_x(0,y)u(y)dy=\ell_{1,A}(u)=M_{1x}`, while the right-hand side `F'(x)=x` gives `F'(0)=1`. So `M_{1x}=1` follows immediately from `u` existing as a genuine solution — a clean, correct chain-rule argument, not in need of knowing `N(x,y)`'s exact form (it only needs differentiability of the kernel, which the entry states is backed by dominated convergence and a Lipschitz/boundedness assumption on `g` and `∂_xN`, a reasonable and unremarkable technical hypothesis for this kind of kernel).

**This makes the entry's framing exactly right**: `M_{1x}=1` is a sharp, parameter-free necessary condition for odd-sector invertibility, not an assumption — so the numerics (`M_{1x}` running `28.5→45.6→74.3→123.6` under refinement, nowhere near `1` and not converging toward it) are a genuine, meaningful test, not a vacuous one. The logical structure of the argument is sound.

## 3. The numerical divergence claim (§4) — internally consistent, appropriately caveated, not independently reproduced this round

The reported pattern (divergence `~N^{0.7}`, traced to near-null Galerkin modes at `~1.6×10^{-8}` overlapping the odd-sector source at `~10^{-3}`, giving `~1/1.6×10^{-8}` amplification) is a coherent, specific failure mode — exactly the kind of mechanism that would produce this exact symptom (growing-with-refinement moments rather than a clean converged wrong value), and the entry correctly distinguishes it from the unrelated "γ-pinning canary" ill-conditioning phenomenon by checking that the odd Schur denominator stays large across several `λ` values while full-operator condition numbers stay modest — a reasonable differential diagnosis, done rather than asserted.

I was not able to build an independent cross-check of this specific numerical claim in this round. Doing so properly would require: reconstructing `N(x,y)` and the deficiency-vector normalization from `v13.745` and earlier (not read this session), correctly assembling the odd-sector Galerkin discretization of `L_A` at `λ=-1`, and reproducing the near-null-mode/source-overlap mechanism independently. That is a substantially larger undertaking than this week's rigidity-arc checks, which reused one already-validated kernel across many questions. Attempting a rushed, partial reconstruction risked exactly the kind of "wrong tool, wrong object" failure from Round 130 (the calibration-kernel proxy mismatch) or the under-converged eigenvector attempt in Round 132 — both cases where forcing a quick numerical check produced a number with no evidentiary value rather than useful signal. Declining to do that here is a deliberate choice, not an oversight.

## 4. Scoping claims (§6) — correctly drawn, consistent with everything else audited this week

The entry's own disclaimers — not an RH claim (a concrete finite-dimensional Fredholm question, decidable in principle without reference to zeta zeros), not a kill of the de Branges line (whose NO-GO as an RH route rests on separate grounds already established), localized to the odd sector only (the even half, the finite HB theorem of `v13.673`, and everything in this week's `Λ`-rigidity arc are explicitly and correctly stated as untouched) — are consistent with how every other entry in this arc has scoped itself, and I have no basis to dispute any of them.

## What remains open

The invertibility question itself (`0∈σ(L_A^{(-)})`?) is exactly as open as the entry states — parked, with an analytic identity on one side and numerics on the other, no resolution claimed. Independent verification of the §4 divergence numbers remains a genuine gap, not closed by a convenient partial check; it would need either a fuller reconstruction of the older deficiency-vector machinery than this round supports, or the sandbox posting the actual kernel-assembly code so it can be reproduced directly rather than rebuilt from the ledger's equations alone.

## Self-audit note

Choosing not to attempt a rushed numerical reconstruction here, and saying so plainly, follows directly from two lessons this session already paid for: Round 130's proxy-kernel mismatch (testing the wrong object) and Round 132's under-converged eigenvalue attempt (testing the right object with inadequate precision). A third instance of "ran some numbers, got nonsense, reported it anyway" would be worse than an honest scope boundary.

## Result

\[
\boxed{\textbf{PASS: the analytic identity in v13.912 §3 (}M_{1x}=1\textbf{ if the odd sector is invertible) is correctly derived, verified by inspection against its own cited source's exact definitions.} \textbf{The numerical divergence evidence in §4 is internally consistent, mechanistically specific, and appropriately distinguished from an unrelated ill-conditioning phenomenon, but was not independently reproduced this round — an honest scope limitation given the depth of unread predecessor machinery involved, not a finding against it.} \textbf{The entry's own scoping (not RH, not a kill of the de Branges line, localized to the odd sector) is correctly drawn.}}
\]
