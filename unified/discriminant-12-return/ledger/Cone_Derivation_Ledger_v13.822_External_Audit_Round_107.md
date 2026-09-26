# Cone Derivation Ledger v13.822 — External Audit Round 107

Date: 2026-09-26

Auditor: External audit thread (Claude, independent instance).

Scope: v13.820 (adversarial ρ=0.02 cap audit) and v13.821 (ρ=0.02 parity-tail inertia theorem) — the promotion of a fully rigorous, sector-wise, four-resonance certificate at the tighter radius.

Verdict: **PASS. This is a genuine theorem, independently reproduced by direct execution, exactly as scoped.**

## 1. v13.820 — adversarial cap audit: fully verified

I ran `suzuki_endpoint_M3999_rho002_adversarial_audit.py` directly. It completes with `PASS: adversarial rho=0.02 cap audit` and reproduces every one of its ~60 reported figures exactly: all four hash/rank checks, all four buffer floors, the full coupling/residual/reference-defect cap table (headrooms now uniformly in the 4.6%–24% range — no sub-percent brittleness anywhere, exactly as the entry claims), both interval tail floors, the far-generator bound (`7.4547 < 8`), the remote-cross re-derivation (`16.114`, `10.781`, both `< 20`), all four explicit remote-Gram ceilings, and all four final terminal margins. This is a thorough, honest adversarial pass — it treats the frozen v13.818 payload as untrusted, recomputes everything independently, and widens every cap that had thin headroom before anything depends on it. Exactly the discipline asked for in Round 106.

## 2. v13.821 — the theorem: fully verified

I ran `suzuki_endpoint_M3999_rho002_inertia_certificate.py` directly. It completes with `PASS: rho=0.02 parity-tail inertia theorem`, and every terminal figure — both negative-space margins, both minus-positive terminal margins, both plus terminal margins, all four normalized lower bounds, both `N_tail_0p02 = 4` outputs — **matched exactly**, digit for digit, against the ledger's stated public certificate margins in §8.

This is a real theorem, not a diagnostic: it combines a strict 4-dimensional negative subspace (proven via exact rational rank + outward-rounded resolvent-perturbation bounds) with a codimension-4 positive complement (proven via finite Schur reduction + outward interval remote-tail floors + explicit-through-two-million residual Gram + analytic far-tail envelope), on both sides of the endpoint pencil, in both parity sectors, entirely in fail-closed outward arithmetic. Nothing here is a midpoint estimate.

## 3. What it actually says — and what it doesn't

Worth stating plainly, since the entry itself is careful about this and it's easy to overread from the outside:

**What's proven**: for the bulk-subtracted parity-tail operator (excluding a separately-handled 2-mode low core, in each parity sector separately), the compact relative operator `K` has *exactly* four eigenvalues in `(-1.02, -0.98)` — and, combined with the earlier ρ=0.10 result, no fifth eigenvalue anywhere in the wider `(-1.10, -0.90)` either. The four resonances found at the coarser radius are confirmed to be the same four at the finer radius, rigorously, with zero kernel at every one of the four endpoint pencils checked.

**What's not proven** (the entry's own §9 guardrails, which I've now double-checked are respected rather than just stated): this doesn't combine the even-v and odd-v counts into a single multiplicity claim, doesn't touch the separately-scoped low-core problem, and makes no RH/GRH or exact-zero statement. It's a real, load-bearing piece of the Lane A resonance-cluster program — not (yet) a statement about the Riemann Hypothesis or about Suzuki's original infinite-dimensional operator as a whole.

## Self-audit note

No error of my own found this round.

## Result

\[
\boxed{\textbf{PASS: v13.820 and v13.821 fully confirmed by direct execution. The } \rho=0.02 \textbf{ parity-tail inertia theorem is a genuine, rigorously outward-certified result: } N_{\rm tail}^{(e)}(0.02)=N_{\rm tail}^{(o)}(0.02)=4 \textbf{, with zero kernel at all four checked endpoints.}}
\]
