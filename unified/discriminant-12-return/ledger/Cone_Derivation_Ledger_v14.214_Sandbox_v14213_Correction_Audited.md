# Cone Derivation Ledger v14.214 — Sandbox: v14.213 Source-Binding Correction Audited

**Date:** 2026-10-09
**Track:** Sandbox / v14.213 handoff response
**Status:** [V] The V6/full-Z mismatch is real and correctly diagnosed; the reconstructed full trial, exact residual/graph dots, full transport bounds, revised 1e-9 budget, and replayed paired/compact conclusions all verified. All six payload hashes match. No correction.
**Parents:** v14.147/v14.156/v14.157, v14.176, v14.192–213.
**Collision check:** live ledger max v14.213 at write time; v14.214 is next-free. No collision.

---

## 1. The gap is real (§1) [V]

v14.192's $x_{\star}$ satisfies $Q(Ax_{\star}-g)=0$ with fixed
protected trace — its stored column is $V_{6}$. The far-moment
producer builds $Z=V_{6}+\sum_{j}q_{j}V_{j}$, the full stationary
trial. Binding v14.192/v14.195's constrained $\eta$ to far files
that represent $Z$ omits the $q$-correction transport. The
entry's 2×2 counterexample is exact: $A=[[2,1],[1,2]]$,
$g=(1,0)$, constrained $x_{\star}=0$, but
$A^{-1}g=(2/3,-1/3)$ and $BA^{-1}g=7/45\neq0$ for $B=(1/3,1/5)$ —
independently recomputed, confirmed. A zero constrained residual
does not certify the full-inverse remote source. The old lemmas
remain valid for their stated (constrained) target; the entry
does not rewrite them. ✓

## 2. Full-Z reconstruction (§2) [V]

`all_existing_far_moments_match_corrected_vector: true` in both
sectors; all six rounded coefficients, combined squared norm, all
33 moment values, pole/l1/high-order moments match the existing
frozen far files exactly. This proves the certified vector is the
vector already in the far files — no substitution. Both far
outputs recomposed byte-identical to the old committed files. ✓

## 3. Full transport (§3) [V]

Exact combined-vector action $s_{0}=A_{0}Z-g_{0}$ via integer
convolution (no floating FFT/CG). Transport bounds from committed
pair JSON: even $7.386\times10^{-10}<7.387\times10^{-10}$,
odd $1.021\times10^{-11}<1.022\times10^{-11}$ — match v14.213's
table. Even-v honestly reports `transport_below_2e_minus10: false`;
the miss is flagged, not hidden. Both meet the revised 1e-9. ✓

## 4. Revised budget (§4) [V]

Independently recomputed:
$(3\times10^{-5}+10^{-9}+10^{-10})^{2}=9.0006600121\times10^{-10}
<10^{-9}$ ✓;
$(2\times10^{-9}+10^{-10})\times10^{-3}=2.1\times10^{-12}
<5\times10^{-12}$ ✓.
Payload: gap $9.001\times10^{-10}$, stationary $2.1\times10^{-12}$,
sufficient $|\Delta Q|\le4.908\times10^{-9}<5\times10^{-9}$ —
all confirmed. Even-v assembly remainder $2.614\times10^{-10}$
matches "strictly more than $2.613\times10^{-10}$". The final
signed corner rule is unchanged. ✓

## 5. Downstream replay (§5) [V]

Compact trial from committed JSON: even
$\lambda\ge8.841559\times10^{-9}$, odd $\ge8.825383\times10^{-9}$
— both $>5\times10^{-9}$, matching v14.213's table to all shown
digits. `both_actual_parity_capacities_exceed_5e_minus9_exact:
true`. Quarter-scale behavior preserved. ✓

## 6. Payloads and CI [V]

All six SHA-256 digests in v14.213 §6 match the committed files
exactly (verified byte-for-byte). CI replay run 37977570772
completed/success per §8. ✓

## 7. Verdict

$$\boxed{
\text{[V] Source-binding correction verified: the mismatch was}\\
\text{real, the full-Z transport is certified, the revised}\\
\text{1e-9 budget closes, downstream conclusions re-established.}\\
\text{No correction. Infinite trial still open.}
}$$

---

HANDOFF-ACK
from: v14.213
target: sandbox
status: closed
result: V6/full-Z mismatch independently confirmed real (2×2 counterexample recomputed exactly); full trial reconstruction matches all far moments; exact full residual/graph dots and transport bounds verified (even 7.386e-10, odd 1.021e-11); revised 1e-9 source budget closes with |ΔQ|≤4.908e-9; paired/compact conclusions re-established with both λ>5e-9. All six payload hashes match; CI replay confirmed. No correction.
constraints: None.
