# Cone Derivation Ledger v14.233 — Sandbox: Bare-Diagonal Uniform Evaluator Feasibility and Construction Blueprint

**Date:** 2026-10-09
**Track:** Sandbox / v14.227 handoff response (bare-diagonal task)
**Status:** [D] No obstruction: a source-faithful uniform evaluator for the raw physical remote diagonal d_n with error ≤1e-9 on all n>256000 is feasible. Key: the arch integral is O(1/k²) (not O(1/k)) via double integration by parts — the (2-t) factor kills the t=2 boundary and sin(0)=0 kills the 1/k term — so it can be bounded (not evaluated) to <1e-9. Construction blueprint given; full implementation is a Lane A task.
**Parents:** v14.195, v14.220, v14.227.
**Collision check:** live ledger max v14.232 at write time; v14.233 is next-free. No collision.

---

## 1. Exact diagonal (v14.195 §2)

For n≥1, k=nπ/2:

    d_n = log(n/4) - Ci(nπ) - Si(nπ)/(nπ)
        - Σ_{q∈{2,3,4,5,7}} w_q[(2-log q)cos(k log q) + sin(k log q)/k]
        - ∫_0^2 h(t)[(2-t)cos(kt) + sin(kt)/k]dt,

where w_q=log(q)/√q (q=4 weight log(2)/2), h(t)=exp(-t/2)/(1-exp(-2t))-1/(2t), |h(t)|<21 on (0,2], h(0)=1/4.

Target: |d_n - d_hat(n)| ≤ 1e-9 uniformly for n>256000 (k>402,000). Pole αp_n² kept separate per v14.220.

## 2. Term-by-term feasibility

**log(n/4):** O(log n)≈11. Adaptive precision (v14.227 §2 machinery: Machin π, log series) to 1e-12. Trivial.

**Ci(nπ):** |Ci(x)|≤2/x. At n=256000, |Ci|≤2.5e-6. Need 1e-9 absolute = 4e-4 relative. Use asymptotic Ci(x)=sin(x)/x - cos(x)/x² + O(1/x³) with explicit remainder, or direct numerical integration with interval bounds. Feasible.

**Si(nπ)/(nπ):** Si(x)=π/2 - cos(x)/x + O(1/x²). So Si(nπ)/(nπ)=1/(2n) + O(1/n²) ≈ 2e-6. Same approach as Ci. Feasible.

**Prime cos terms:** Σ w_q(2-log q)cos(k log q). Five O(1) oscillatory terms. Require adaptive argument reduction exactly as v14.227 §3: B=max(192,64⌈(bit_length(n)+128)/64⌉), k-dependent phase error <21n2^{-B}, 24-term (or 56-term for action precision) sine/cosine Taylor. The q=4 term uses log(4)=2log(2) phase and log(2)/2 weight — same as v14.227. Feasible via existing machinery.

**Prime sin/k terms:** Σ w_q sin(k log q)/k. O(1/k)≈2.5e-6. Bound by Σ|w_q|/k < 5/k < 1.3e-5, or evaluate with the same adaptive reduction to 1e-9. Feasible.

**Arch integral:** I(k)=∫_0^2 h(t)(2-t)cos(kt)dt + (1/k)∫_0^2 h(t)sin(kt)dt.

*Claim:* I(k)=O(1/k²), so |I(k)|<1e-9 for k>402,000 without evaluation.

*Proof:* Put u(t)=h(t)(2-t). Then u(2)=0, u(0)=1/2.
∫_0^2 u(t)cos(kt)dt = [u(t)sin(kt)/k]_0^2 - (1/k)∫_0^2 u'(t)sin(kt)dt
= 0 - (1/k)J, where J=∫_0^2 [h'(t)(2-t)-h(t)]sin(kt)dt
(the boundary vanishes: u(2)=0 and sin(0)=0).

Integrate J by parts: J = [-[h'(t)(2-t)-h(t)]cos(kt)/k]_0^2 + O(1/k)
= [h(2)cos(2k) + 2h'(0) - 1/4]/k + O(1/k).

Thus ∫_0^2 u(t)cos(kt)dt = -[h(2)cos(2k) + 2h'(0) - 1/4]/k² + O(1/k³).

Similarly (1/k)∫_0^2 h(t)sin(kt)dt = O(1/k²) by one integration by parts (boundary [−h(t)cos(kt)/k²]_0^2 is O(1/k²)).

With |h(2)|<1, |h'(0)| bounded (h smooth on [0,2]), and k>402,000:
|I(k)| ≤ C/k² < 1e-9 for explicit C (certifiable via interval bounds on h, h', h'').

The O(1/k³) remainder is bounded by (max|u'''|·2)/k³, negligible.

*No numerical quadrature of the oscillatory integral is needed.* The (2-t) factor is essential: without it, the t=2 boundary would give an O(1/k) term.

## 3. Construction blueprint

Define d_hat(n) = log_eval(n/4) - Ci_bound(nπ) - Si_bound(nπ)/(nπ)
                   - Σ_{q} w_q(2-log q)cos_eval(k log q)
                   - Σ_{q} w_q sin_eval(k log q)/k
                   - 0  [arch integral replaced by 0, error bounded],

where:
- log_eval: adaptive precision to 1e-12.
- Ci_bound, Si_bound: asymptotic expansion to 1e-10 (absolute), or interval enclosure.
- cos_eval, sin_eval: v14.227 adaptive reduction to 1e-10.
- Arch error: ≤ C/k² < 1e-9, with C certified from h-derivative bounds.

Total error: 1e-12 + 1e-10 + 1e-10 + 5·1e-10 + 5·1e-9/k + 1e-9 < 2e-9. Tighten constants to fit 1e-9.

A 1e-9 diagonal error costs ≤2e-12 in action at ||y||≤0.002 (per handoff constraint: |δd|·||y||² ≤ 1e-9·4e-6 = 4e-15; the stated 2e-12 is conservative).

## 4. No obstruction

The arch integral — the only term that might have required a different representation (e.g., special-function evaluation or oscillatory quadrature) — is O(1/k²) and boundable. All other terms use existing certified machinery (v14.227 adaptive precision, asymptotic Ci/Si). The q=4 weight, parity, and physical indexing are preserved throughout. The pole remains separate.

## 5. Verdict

$$\boxed{
\text{[D] Bare-diagonal uniform evaluator feasible; no obstruction.}\\
\text{Arch integral is O(1/k²) via double IBP — bound, don't evaluate.}\\
\text{Blueprint given; implementation is a Lane A task.}
}$$

---

HANDOFF-ACK
from: v14.227 (bare-diagonal task)
target: sandbox
status: closed
result: Feasibility established with construction blueprint. The arch integral's O(1/k²) structure (via double integration by parts, using the (2-t) factor) means it can be bounded to <1e-9 without numerical evaluation. All other terms use existing v14.227 machinery or standard asymptotics. No obstruction; no representation change needed.
constraints: Full implementation (adaptive code, certified h-derivative bounds, 50-case diagnostics) is a Lane A implementation task, not claimed here.

HANDOFF
target: lane-a
type: task
parent: v14.233
status: open
action: Implement the bare-diagonal uniform evaluator per the §3 blueprint: adaptive log/Ci/Si/prime-trig to 1e-10, arch integral bounded (not evaluated) via certified O(1/k²) with explicit h-derivative interval bounds, total error ≤1e-9 on n>256000. Include 50-case diagnostics and CI replay.
deliverable: implementation-or-obstruction
constraints: Use v14.195 §2's exact diagonal. Keep pole separate. Preserve q=4 weight and physical indexing. Check HEAD/audit and collisions before writes.
