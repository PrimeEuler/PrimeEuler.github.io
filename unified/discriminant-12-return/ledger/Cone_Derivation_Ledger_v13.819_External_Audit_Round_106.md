# Cone Derivation Ledger v13.819 — External Audit Round 106

Date: 2026-09-26

Auditor: External audit thread (Claude, independent instance).

Scope: v13.816 (ρ=0.10 plus-tail certificate, completing the fifth-resonance exclusion), v13.817 (independent cross-check plus ρ=0.02 midpoint reconnaissance), v13.818 (ρ=0.02 exact-dyadic freezes, no theorem yet).

Verdict: **PASS on all three entries.** Every research script I ran (the plus-tail terminal certificate, the ρ=0.02 midpoint anatomy, both ρ=0.02 freeze modules) completed and reproduced its ledger figures exactly, including every SHA-256 hash. `N_tail^(e)(0.10) = N_tail^(o)(0.10) = 4` — the fifth-resonance exclusion at radius 0.10 — is now a genuinely closed, reproducible result in both parity sectors.

## 1. v13.816 — ρ=0.10 plus-tail: fully verified

I ran `suzuki_endpoint_M3999_plus_terminal_certificate.py` directly. It completes with `PASS: rho=0.10 plus tail endpoint is strictly positive`, and every figure matched exactly: the corrected far-generator bound (`7.580345...< 8`, confirming the self-caught proof-hygiene fix in §3 — the earlier v13.812 proof had omitted the `ρπ/2` shift term, caught and fixed here), both point-Gram maxima, both terminal margins (`3.783895551287793...`, `3.801400795309342...`), and both normalized lower bounds (`0.990419919968...`, `0.994958890918...`). Combined with the externally-confirmed minus-tail result from Round 105, this closes `ind_-(F^+_{0.10,tail}) = 0` and `ind_-(F^-_{0.10,tail}) = 4` in both sectors — a genuine, sector-wise fifth-resonance exclusion at radius 0.10, correctly scoped (excludes the separate two-mode low core, and is explicitly not a claim about the direct-sum total multiplicity).

## 2. v13.817 — independent cross-check and ρ=0.02 reconnaissance: fully verified

I ran `suzuki_endpoint_M3999_rho002_midpoint.py` directly; it reproduced every eigenvalue and every `(4,0,6)`/`(0,0,10)` inertia claim for both the ρ=0.02 minus and plus midpoint cores, in both parity sectors, exactly. This entry is appropriately disciplined: it explicitly does **not** promote any ρ=0.02 theorem, and it independently re-derives (via a separate reconstruction path, not by reusing v13.816's frozen Cholesky payload) the ρ=0.10 plus-tail numbers before moving on — the same good habit flagged approvingly in Round 105.

## 3. v13.818 — ρ=0.02 freezes: fully verified

I ran both `suzuki_endpoint_M3999_rho002_minus_frozen_inputs.py` and `suzuki_endpoint_M3999_rho002_plus_frozen_L0.py`. Both reproduced every SHA-256 hash, every exact-rational minor, and every reference scale exactly. No theorem is claimed here, correctly. The entry itself flags the tighter margins at this radius (`~2.4×10⁻³` vs. `~1.1×10⁻²` at ρ=0.10) as something the next gate's cap audit must account for — a self-directed caution, already anticipating what I would otherwise have flagged.

## 4. Caution for the Lane A thread, per the user's request

The user asked that a specific caution be passed along explicitly, so the source thread has it in view rather than only inferring it from audit rounds. Recording it here:

**Context**: earlier this session, before this certificate program existed, we discussed whether Lane A's growing Feshbach/protected-subspace machinery risked repeating the pattern of this project's old `M16001` numerical-certificate lineage — a large, sprawling pile of "outward/certificate/replay" scripts that (per v13.799) turned out to rest on an undetected sign error for a long time. Round 103 found a concrete, unrelated instance of the same *failure mode* (4 of 6 freshly committed scripts didn't run as committed) in this very program. Rounds 104–106 then showed a real, sustained correction: reference-defect caps reconciled honestly, a source-thread-initiated adversarial self-audit (v13.814) that found and fixed brittle margins before any theorem depended on them, and now three consecutive batches (v13.812–818) where every script I've independently executed has completed and passed on the first try.

**The caution, forward-looking**: this is working *because* of specific habits — independent reconstruction before trusting a certificate routine, checking cap headroom rather than just checking pass/fail, freezing payloads with runtime hash/rank verification, and scoping every result explicitly (tail vs. low core, this radius vs. that one, minus vs. plus). As the radius tightens (ρ=0.02's smallest scales are already `~2×10⁻³` against `~1×10⁻²` at ρ=0.10 — roughly 5× less headroom) and if the architecture is ever pushed past `M=3999/4000` toward the `M=16001` scale this project has used before, that is exactly the regime where the old lineage went wrong. The concrete ask: keep applying the v13.814-style discipline at every new radius and every scale increase, not just when an external audit flags something — which is exactly what v13.817–818 already did unprompted. Don't let success at ρ=0.10 create pressure to move faster at ρ=0.02.

## Self-audit note

No error of my own found this round.

## Result

\[
\boxed{\textbf{PASS: v13.816, v13.817, v13.818 all independently confirmed by direct execution.} N_{\rm tail}^{(e)}(0.10)=N_{\rm tail}^{(o)}(0.10)=4 \textbf{ is a fully closed, reproducible result. } \rho=0.02 \textbf{ midpoint anatomy is correctly reconnoitered and frozen with no theorem yet claimed.}}
\]
