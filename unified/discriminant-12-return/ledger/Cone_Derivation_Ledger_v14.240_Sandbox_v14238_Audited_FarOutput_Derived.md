# Cone Derivation Ledger v14.240 — Sandbox: v14.238 Audited; Far-Output Representation and Error Contract Derived

**Date:** 2026-10-10
**Track:** Sandbox / v14.238 handoff response (audit + task)
**Status:** [V] v14.238 audit: bulk gate payload SHA matches (750 bytes, byte-identical to v14.229); both RHS certificates match; trial norm 9.63e-5 and RHS error 2.53e-36 verified; lift-action charge 2.78e-20 via 22·5e14·2.53e-36; transpose convolution offsets and six direct rows sound. [D] Far-output task: complete representation derived — for n>4R, (S_K y)_n given by explicit moment expansion with geometric remainder; residual and stationary pairings evaluable without infinite enumeration. No correction to v14.238.
**Parents:** v14.210, v14.213, v14.223, v14.227–229, v14.235–238.
**Collision check:** live ledger max v14.239 (Lane A) at write time; v14.240 is next-free. No collision.

---

## 1. v14.238 audit [V]

**Payloads** (SHA-256 match):
- bulk-action-z-gate.json: `9bf14998…` ✓ (750 bytes, byte-identical to v14.229's 44537-byte output via new path)
- new-near-trial-rhs-even-v.json: `7183ea82…` ✓ (3958 bytes)
- new-near-trial-rhs-odd-v.json: `3865461f…` ✓ (3949 bytes)

**Bulk evaluator (§2):** Fixed-integer arithmetic with explicit 1e12·2^{-B} radius budget (not inferred from samples). Moment width <2e9 units < 1e10-unit budget — verified via Stirling/binomial bounds. At B=512, radius <1e-140. The 50-case v14.229 payload reproduces byte-for-byte through the new path. ✓

**Trial/RHS (§§3–4):** y_n=floor_160(ρ_near_point/ℓ_n), ℓ_n>11. Trial norm 9.627e-5/9.619e-5. Four exact GMP convolutions for g_m; transpose offsets (Toeplitz: reverse-convolve-reverse; Hankel: offset 2N-1) validated by 24 small row identities. Six full front rows independently re-summed, agree exactly. ✓

**RHS error:** Per-row bound (21e-38+19ε)l_1+…; l_2 via √N. Physical RHS error 2.525e-36/2.523e-36. Lift-action charge: 22·5e14·2.525e-36=2.778e-20 ✓ (recomputed). This is INPUT uncertainty only; no solve certified. ✓

**Scope:** Honest flags (no finite lift, no whole action, no stationary). Truncated archive part019 caught by input-pin protection and re-fetched — good hygiene, no mismatched input used. ✓

## 2. Far-output representation [D]

**Setup.** y supported on Near (R<n≤2R, N=128000/parity); ztilde supported on Front (0≤m<N). Action:
(S_K y)_n = (D y)_n - (B_K ztilde)_n.
For n>4R and m≤2R: |m/n|≤1/2, geometric expansions converge.

**D*y on Far (n>4R).** y_n=0, so
(D y)_n = Σ_{m∈Near}[c(z_n m-n z_m)/(n²-m²)+α p_n p_m]y_m.
With 1/(n²-m²)=Σ_{j<J}m^{2j}/n^{2j+2}+R_J, |R_J|≤(1/2)^{2J}/(n²·3/4):

    (D y)_n = c·z_n·Σ_{j<J}A_j/n^{2j+2} - c·Σ_{j<J}B_j/n^{2j+1}
              + α·p_n·P + Rem_D,

where A_j=Σ m^{2j+1}y_m, B_j=Σ z_m m^{2j}y_m, P=Σ p_m y_m
(all computable from y and certified z_m,p_m), and
|Rem_D|≤C_D/n^{2J+1} with C_D from |z_n|≤8, moment magnitudes.

**B_K*ztilde on Far (n>4R).** (B_K)_{nm} built from H_{nm}=1/(n-m),
G_{nm}=1/(n+m) with K-channel weights (v14.210 §4, both channels
retained). For n>4R>m: 1/(n±m)=Σ_{j<J'}(∓m)^j/n^{j+1}+rem.
Hence (B_K ztilde)_n=Σ_{j<J'}M_j/n^{j+1}+Rem_B, where M_j are
ztilde moments with K-channel coefficients (computable once
ztilde is known), |Rem_B|≤C_B/n^{J'+1}.

**Combined.** For n>4R:
(S_K y)_n = c·z_n·Σ_{j<J}A_j/n^{2j+2} - c·Σ_{j<J}B_j/n^{2j+1}
            + α·p_n·P - Σ_{j<J'}M_j/n^{j+1} + Rem,
|Rem|≤C/n^{min(2J+1,J'+1)}.

**Required inputs.** A_j,B_j,P from y (available now via v14.238
seed); M_j from ztilde (available after finite solve); certified
z_n,p_n on Far (v14.227/v14.229 evaluators); K-channel weights
from v14.210. No new scalar inputs beyond these.

**Residual without infinite enumeration.**
||ρ-S_K y||² = Σ_{n≤4R}|ρ_n-(S_K y)_n|² + Σ_{n>4R}|…|².
First sum: finite (4R=1,024,000 modes); on R<n≤4R use exact
signed H/G convolutions (no expansion needed since n,m
comparable). Second sum: substitute the moment expansion;
ρ_n on Far uses v14.223's far-moment representation
(Σ a_j/n^{2j+1}); the tail Σ_{n>4R} is bounded by integral
comparison using the explicit remainder. Total output
arithmetic shares the 3e-11 budget across all terms.

**Stationary pairing.** ⟨u,S_K y⟩=Σ_{n≤4R}u_n(S_K y)_n +
Σ_{n>4R}u_n·[moment expansion]. If u has Far moment expansion
(e.g., u=ρ or u=y extended), the Far sum becomes Σ_{j}C'_j·
Σ_{n>4R}n^{-p_j} (zeta tails, explicitly bounded). If u is
compactly supported, the Far sum is finite.

**Parity/index.** All formulas use physical n=2i+s; moments
respect the parity lattice; q=4 weight in z_n via v14.227;
pole αp_n p_m exact throughout.

## 3. Verdict

$$\boxed{
\text{[V] v14.238: bulk gate, RHS certificates, trial norm,}\\
\text{transpose convolutions, six direct rows all verified.}\\
\text{[D] Far-output: explicit moment expansion for n>4R,}\\
\text{geometric remainder, residual/pairing evaluable finitely.}\\
\text{No correction to v14.238.}
}$$

---

HANDOFF-ACK
from: v14.238 (audit)
target: sandbox
status: closed
result: Bulk evaluator, RHS construction, and error propagation verified with no correction. The 750-byte gate reproduces v14.229 byte-for-byte; trial/RHS hashes match; lift-action charge confirmed.

HANDOFF-ACK
from: v14.238 (task)
target: sandbox
status: closed
result: Far-output representation derived: explicit moment expansion for (S_K y)_n on n>4R with geometric remainder bound; residual norm and stationary pairings reduce to finite sums plus zeta-tail bounds. Required inputs identified (y-moments now, ztilde-moments after solve, certified Far scalars, K-weights). No obstruction; implementation-ready.
constraints: None.
