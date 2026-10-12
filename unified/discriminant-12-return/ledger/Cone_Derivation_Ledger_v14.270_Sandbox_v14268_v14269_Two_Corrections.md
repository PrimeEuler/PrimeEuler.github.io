# Cone Derivation Ledger v14.270 — Sandbox: v14.268/v14.269 Received; v14.264's Two Errors Corrected

**Date:** 2026-10-11
**Track:** Sandbox / v14.268+v14.269 handoff response
**Status:** [C] Both corrections in v14.268's handoff are VALID. (1) v14.264's "n≤2R implies n<b/2" is FALSE near 2R since b=2R+start; the geometric expansion ratio (n/m)²→1⁻ as n→b⁻, m=b. The remainder bound is not uniform. (2) v14.264 used an unweighted ||y_tail||_1 remainder, but y_tail(n)~1/[n·log(n/4)] is NOT in l1 (Σ1/(n log n) diverges). The bound is vacuous. [D] Corrected framework: close-index split (m<2b direct via 8/|n-m|, m≥2b expansion with uniform ratio ≤1/4) and weighted remainders throughout (kernel 1/m² decay makes Σ|y_tail|/m² converge). v14.264's t-integral structure stands with these corrections. No correction to v14.268/v14.269's certified gates.
**Parents:** v14.223, v14.250, v14.253, v14.263–269.
**Collision check:** live ledger max v14.269 (Lane A) at write time; v14.270 is next-free. No collision.

---

## 1. v14.268/v14.269 audit notes

**v14.268:** Complete finite RHS for infinite seed. 128000 rows/sector.
RHS l2 ≤3.21e-30, future action charge ≤3.54e-14. Payload JSON
structure verified (infinite-seed-finite-rhs-{even,odd}-v.json).
Adopts v14.266 corrected Region-1. CI receipt was pending at
publication; v14.269 confirms CI 38186832285 succeeded with
byte-compared archives. No correction.

**v14.269:** Fresh finite lift from actual RHS. Even-v action
charge <9.402e-11, odd-v <3.759e-14. Both below 2e-10 individually.
Six protected graph components retained. Projected residual via
exact ||r||²−⟨P*r,G_P⁻¹P*r⟩. No correction. This is a finite-lift
certificate only; whole infinite action and residual acceptance
remain open.

## 2. Correction 1: close-index ratio [C]

v14.264 §3 stated the Region-1 geometric expansion has uniform
ratio (n/m)²≤1/4 because "n≤2R implies n<b/2."

This is wrong. b=2R+start (start=512001−2R>0 but small relative
to R). For output n approaching b from below and input m=b,
(n/m)²→1⁻. The series converges (n<m strictly) but the remainder
bound const·(n/m)^{2J}/(1−(n/m)²) blows up. Not uniform in n.

**Fix:** Split at m=2b.
- S_close(n)=Σ_{b≤m<2b} D_{nm}y_tail(m): bound directly.
  |D_{nm}|≤K₁/(m−n) with K₁=O(1) (m+n>b, |z|≤11, |p|≤2).
  |y_tail(m)|≤C/[b·log(b/4)] on [b,2b).
  Σ_{b≤m<2b}1/(m−n)≤log((2b−n)/(b−n))≤log b.
  Hence |S_close(n)|≤K₁·C·log(b)/[b·log(b/4)]=O(1/b),
  uniform in n<b. No expansion; finite harmonic sum.
- S_far(n)=Σ_{m≥2b} D_{nm}y_tail(m): here m≥2b>2n so
  (n/m)²≤1/4 uniformly. The v14.266 corrected formula applies:
  S_far=−c·z_nΣ_{j<J}n^{2j}V_j^{far}+cΣ_{j<J}n^{2j+1}U_j^{far}
        +α·p_nP_tail^{far}+Rem_J^{far},
  with partial moments V_j^{far}=Σ_{m≥2b}y_tail(m)/m^{2j+1}.
  Relate to v14.263 full moments via V_j=V_j^{[b,2b)}+V_j^{far};
  the [b,2b) piece is finite (≤256k terms), bounded directly.

## 3. Correction 2: weighted remainder [C]

v14.264 bounded remainders via |Rem|≤sup|kernel|·||y_tail||_1.

This is vacuous: y_tail(n)=Φ(n)/log(n/4) with Φ(n)~1/n gives
|y_tail|~1/[n·log(n/4)], and Σ_{n≥b}1/[n·log(n/4)] diverges
(integral test: ∫dx/[x·log x]=log log x→∞). So ||y_tail||_1=∞.

**Fix:** Never factor out ||y_tail||_1. Bound
Σ|kernel_{nm}|·|y_tail(m)| directly, using kernel decay.

For the far geometric remainder (m≥2b):
|Rem_J^{far}|≤Σ_{m≥2b}|c|(|z_n|m+n|z_m|)·(n/m)^{2J}/(m²−n²)·|y_tail(m)|.
With m²−n²≥3m²/4 and (n/m)^{2J}≤4^{−J}:
≤const·4^{−J}·Σ_{m≥2b}|y_tail(m)|/m²
≤const·4^{−J}·Σ_{m≥2b}C/[m³·log(m/4)]
≤const·4^{−J}·C/[b²·log(b/4)]<∞.
The 1/m² from the kernel (not from y_tail) drives convergence.
No l1 norm appears.

## 4. Regions 2–3 and diagonal (corrected)

The v14.264 t-integral framework stands with the same two
corrections applied:

- **t>83 moment expansion:** HS remainder must be weighted
  (Σ|kernel|·|Φ_t(m)| with kernel decay), not via ||Φ_t||_1.
  For t>83, Φ_t(m)=Φ(m)m^{−t} decays as m^{−(1+t)}, and the
  moment-expansion kernel supplies 1/m², so all remainders
  converge absolutely.

- **0≤t≤83 split-sum:** The n/2<m<2n region already uses
  the 8/|n−m| bound directly (v14.253), which is a weighted
  (pointwise) bound, not an l1 bound. Correct as written.
  The m≤n/2 and m≥2n regions gain kernel decay 1/n and 1/m
  respectively; with |Φ_t(m)|≤C·m^{−(1+t)} these converge
  without l1.

- **Diagonal:** d_n·y_tail(n) with |d_n|≤log(n/4)+100 (v14.235)
  and |y_tail|≤C/[n·log(n/4)] gives O(1/n) pointwise. No l1
  norm involved. Correct as written.

## 5. What remains

The corrected design is complete on paper. The next step is
actual code: a directed D*y evaluator implementing
(1) the Region-1 close/far split with v14.263 moments,
(2) Regions 2–3 via t-integral with weighted remainders,
(3) diagonal via certified d_n.
Lane A owns the finite RHS (v14.268) and lift (v14.269); the
sandbox evaluator consumes their certified outputs.

---

HANDOFF-ACK
from: v14.268 (sandbox part)
target: sandbox
status: closed
result: Both corrections conceded as valid. Corrected Region-1 with close-index split (m<2b direct, m≥2b expansion) and weighted remainder (no l1 on y_tail) derived. Regions 2–3 and diagonal corrected similarly. v14.268's gate audited with no correction.
constraints: None.

HANDOFF-ACK
from: v14.269 (sandbox part)
target: sandbox
status: closed
result: Finite lift gate audited with no correction (even-v <9.402e-11, odd-v <3.759e-14). Directed D*y evaluator design corrected per v14.268's two points. Code implementation is the next step.
constraints: None.
