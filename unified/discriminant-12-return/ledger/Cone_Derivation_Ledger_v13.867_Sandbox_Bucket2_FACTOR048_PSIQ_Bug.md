# Cone Derivation Ledger v13.867 — Sandbox Bucket 2: FACTOR-048 — PSI_Q Transcription Bug; c_1 Manufactured; Numerical Program Compromised, Re-run Chartered

Date: 2026-09-29

Lane: B (sandbox exploratory track, chartered by the project owner). **Lane disambiguation:** this is NOT the ledger's Lane B (the norm-quotient/idele-class representation track, dormant since v13.736 per v13.760). The sandbox track consumes Lane A's certified results and reports exploratory diagnostics back; nothing here is certified and nothing here alters a certified result.

Status: **[D]** for the bug itself (a checkable constant against v13.258's formula) and the independent re-verification; **[N]** for the numerical findings; **[I]/[O]** for interpretation. No RH/positivity/Hilbert–Pólya claim.

Author: the project owner's sandbox track (autonomous thread under the owner's assistant), by request and with the authorization of the project owner. Full analysis (for-review, not part of this repo): `~/workspace/d12/lane_b/sandbox/runs/20260929-factor048/`.

Parents: v13.866 (External Audit Round 122), v13.862 (PAIR-H), v13.855 (bulk lemma), v13.854 (W3), v13.853 (W2), v13.852 (W1), v13.258 (D12 screw, the source of truth for the constants).

Synchronization: live ledger head checked immediately before this write is v13.866 (External Audit Round 122). No collision on the present version number. **This entry does not audit v13.866 or earlier.**

## 0. Verdict

**[N] refuted-in-part.** The claimed factorization \(0.48 = (-c_1)\int V_\infty^+\) with \(c_1 \approx -0.154\) "set by \(-L'/L(1/2,\chi_{12})\)" does not hold as stated. The entire \(c_1\) is manufactured by a transcription-error bug in the sandbox screw code: a hardcoded `PSI_Q` contradicting v13.258. Every Bucket 2 numeric depending on the linear growth of \(g(t)\) was computed with the wrong screw function and must be recomputed. The project owner has authorized the corrected re-run (chartered in §5).

## 1. What was checked and what survived [D/N]

**Survives [D]:** \(-L'/L(1/2,\chi_{12}) = -1.4436383847188329\ldots\) — computed by 40-digit numerical differentiation, agreeing to 15 digits with the functional-equation value \(-1.4436383847188326\), and with the ledger's archimedean slope \((\psi(1/4)+\log(12/\pi))/2 = -1.4436\). The character was verified primitive mod 12 (\(\chi_{12}(1)=1,\ \chi_{12}(5)=\chi_{12}(7)=-1,\ \chi_{12}(11)=1\), conductor 12), matching `screw.py`'s table; \(L(1/2,\chi_{12}) = 0.498557\ldots \neq 0\). **But this number is the \(R_{12}\) slope, not \(c_1\):** with the correct screw constants it cancels exactly against the archimedean \(A_{12}\) slope, as v13.258's formula dictates. It does not survive as \(c_1\).

## 2. The bug [D]

The ledger/sandbox claim was \(c_1 = \mathrm{slope}(R_{12}) - \mathrm{slope}(A_{12}) = (-1.4436) - (-1.2883) = -0.1554 \approx -0.154\), with \(g(t) = R_{12}(t) - A_{12}(t)\) growing linearly. The \(-1.2883\) \(A_{12}\) slope traces to a single hardcoded line:

`lane_b/sandbox/runs/20260928-155806-bucket2-distributional-ta/scripts/screw.py:29`:
`PSI_Q = -3.9170715877437315`

v13.258's formula requires \(\psi(1/4) = -4.2274535333762654\ldots\) (independently re-verified in this session via mpmath at 30 digits). Bug archaeology:

- `20260928-120000…/screw_d12.py:22`: `PSI_Q = mp.digamma(1/4)` — **correct**.
- `20260928-150847…/screw_fast.py:16`: `PSI_Q = -4.22745353337626540…` — **correct**, hardcoded.
- `20260928-155806…/screw.py:29`: `PSI_Q = -3.9170715877437315` — **wrong, changed without explanation**; inherited by `20260928-165927` — the run behind W1, PAIR-H, W2, W3 and all downstream numerics.

**Smoking gun [N]:** \((PSI_Q^{\mathrm{wrong}} - \psi(1/4))/2 = 0.15519\), matching the measured \(|c_1| = 0.154\) to four digits — the entire \(c_1\) is the transcription error, halved. Decisive test (`psiq_test.py`): reconstructing \(A_{12}\) with the correct \(\psi(1/4)\), \(g(t)/t \to 0\) (\(t=6\): \(-0.052\); \(t=10\): \(-0.003\); \(t=12\): \(-0.012\)) — **no linear growth**. The \(-1.4436\) slopes of \(R_{12}\) and \(A_{12}\) cancel exactly.

**Secondary flags [D]:** `LOG_12_PI = 1.34053524` vs \(\log(12/\pi) = 1.34017676\), and `ZETA_2_Q = 16.45371108` vs \(\zeta(2,1/4) = 17.19732915\) — also inconsistent with v13.258. These affect only the constant term, not the slope; secondary to the PSI_Q bug but included in the re-run audit.

## 3. Blast radius [I]

**Compromised (numerical evidence must be recomputed):** the \(Ae^A\) scaling law; \(L_0 = 0.48\); \(\alpha_\infty = 0.48\); the PAIR-H bulk/edge split magnitudes; the W1–W3 numerical programs (v13.852–v13.854); the bulk-lemma numerics (v13.855); the PAIR-H report (v13.862). The fresh \((8.5)\)-LS solves in FACTOR-048 measured an edge-profile integral \(K_6(\mathrm{full}) = 3.00\) with \(0.154 \times 3.0 = 0.46 \approx 0.48\) — consistent-looking, **but \(v_A\) was solved with the buggy \(g\)**, so this consistency validates nothing.

**Unaffected (analytic statements, independent of the numerics):** the PAIR-H\(_0 \iff E = L_0\) equivalence (mod COMB-H); W3's remnant-inclusive boundary theorem (β cancels, α-even survives as distortion — the *structure*, not the measured 0.48); the T-side closures (D̄, Route T, G1–G3, H1); the IDENT dissolution. These are analytic claims whose proofs do not use the screw numerics.

**Not established either way [O]:** whether 0.48 survives on the corrected kernel. This finding does **not** prove 0.48 wrong — only that the current numerics do not establish it via the claimed \(c_1\) mechanism. Re-solved with bounded, non-growing \(g\), the \((8.5)\) system may reproduce 0.48 through a different mechanism or not at all. That is now the question.

## 4. How this happened, and the guardrail

A correct constant was hand-transcribed into a hardcoded literal in a later run's script, with no assertion against the source formula and no comment marking the change. Every downstream run inherited it silently. **Guardrail going forward:** sandbox screw-construction scripts must assert `PSI_Q == mp.digamma(1/4)`, `LOG_12_PI == log(12/pi)`, `ZETA_2_Q == zeta(2,1/4)` at import time (or compute them from mpmath rather than hardcoding). Hand-transcribed literals with no provenance comment are banned from the numerical program.

## 5. Re-run chartered (project-owner authorized, this entry's date)

RERUN-048: (i) fix `PSI_Q = ψ(1/4)` and audit `LOG_12_PI`, `ZETA_2_Q` against v13.258 in the screw construction, with the §4 guardrail installed; (ii) re-solve the \((8.5)\) system (natural BCs) on the corrected kernel; (iii) re-measure \(L_0, L_1, \alpha_\infty\) and the edge criteria \(R_A \to 1,\ \Delta_A \to 0\); (iv) re-derive the PAIR-H bulk/edge accounting on the corrected kernel; (v) report whether 0.48 survives, and if so by what mechanism — the merged 0.48-value problem restated on clean numerics. Scratch under `~/workspace/d12/lane_b/sandbox/runs/`; nothing enters the repo/ledger/research-notes without per-item authorization.
