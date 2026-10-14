# Cone Derivation Ledger v14.415 — External Audit Round 265: v14.414 Literature-Scan Deposit Reviewed

**Date:** 2026-10-14
**Track:** External Audit
**Status:** [V] v14.414 is read in full. It is a Jeremy-directed literature-scan deposit on the exploratory unit-circle/rapidity dictionary (v14.366/v14.367), explicitly scoped as "deposit and record only," affecting no Lane A/B item or evaluator code. Verified the deposited file's exact byte size and SHA-256, and independently re-derived the two load-bearing mathematical claims in the "sharpest discrimination" section by hand/direct computation — both confirmed exactly. The literature-search "not found" verdicts themselves are not independently re-searched (a different kind of task than this audit's recomputation-based method), and the entry's own "moderate, not conclusive" caveat on that negative evidence is noted as accurate framing, not something this auditor can strengthen or weaken.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–413, v14.366, v14.367, v14.369, v14.414.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `d879876...` (v14.414), matching local HEAD; live ledger max was v14.414. v14.415 is next-free. No collision.

---

## 1. Deposit integrity

`research-notes/Unit_Circle_Parabolic_Dictionary_Literature_Scan.md` is exactly 24,583 bytes with SHA-256 `e067a6c694b31a10eaa8697b12c78fd73859fe5cf4d837edcd7cb4f6f0191787` — both match v14.414's declared values exactly, confirmed by direct `sha256sum` on the committed file.

## 2. Scalar identity independently verified

The entry's one verbatim-web-hit claim rests on the identity `tanh(½ ln n) = (n−1)/(n+1)`. Checked both algebraically (substituting `e^x = √n` into `tanh x = (e^x − e^−x)/(e^x + e^−x)` gives `(√n − 1/√n)/(√n + 1/√n) = (n−1)/(n+1)` after multiplying through by `√n`) and numerically for `n ∈ {2,3,5,10,100}` — exact match in every case to floating-point precision. The identity is correct.

## 3. The "sharpest discrimination" angle claim independently re-derived

The entry's central argument is that the construction's point `tanh ψ + i sech ψ` is the classical Gudermannian point `sech ψ + i tanh ψ` with coordinates swapped, giving angle `π/2 − gd(ψ)` instead of `gd(ψ)`, and that this is why `n=3` gives a 60° station while `gd(ψ₃) = 30°`. Computed directly (not taken on the entry's word): with `ψ₃ = ½ ln 3`, `gd(ψ₃) = 2 arctan(tanh(ψ₃/2))` evaluates to exactly 30.000°, and `atan2(sech ψ₃, tanh ψ₃)` (the construction's own point, angle from the positive real axis) evaluates to exactly 60.000° — matching `90° − gd(ψ₃)` to float precision. This is a genuine, independently-reproduced confirmation of the entry's sharpest and most checkable mathematical claim, not a restatement of it.

## 4. What this round does not verify

The negative literature-search verdicts (components 1–5 and (d)/(e) "not found" or "near-miss only") are findings from a web/arXiv/reference-work search process, not a mathematical derivation this auditor can independently re-run by hand algebra or recomputation — that would require conducting an equivalent search, a different kind of task than this audit's established method. The entry's own "moderate, not conclusive" caveat (MathSciNet/zbMath/Scopus/Google Books/non-English literature not searched) is accurate scope-honesty and is not something this auditor can either confirm or dispute without conducting that search itself. The 32/81 vs. 128√2/243 "does not factor through" remark is arithmetically consistent (128/243 = (32/81)·(4√2/3), not a clean rational multiple) but rests on an external tabulated value (the hydrogen-dipole kernel) this auditor has not independently sourced.

## 5. Scope and standing unaffected

Consistent with v14.414's own framing, this remains Jeremy's exploratory track, separate from the ledger's Lane A/B certification program; no Lane A/B item, evaluator code, threshold, or `C_S_32000` is touched by this entry or by this review.

## 6. Verdict

```
v14.414: literature-scan deposit, byte/hash-verified exactly.
The two load-bearing mathematical claims checked independently:
  - tanh(1/2 ln n) = (n-1)/(n+1): confirmed algebraically and
    numerically.
  - Gudermannian-swap discrimination (60 deg vs 30 deg at n=3,
    general pi/2 - gd(psi) relation): independently re-derived by
    direct computation, exact match.
Literature "not found" verdicts themselves not independently
  re-searched (different task class); the entry's own moderate-
  confidence caveat is accurate framing.
No defect found. Exploratory/candidate-only scope unaffected; no
  Lane A/B item touched.
```

---

HANDOFF
target: sandbox
type: audit-confirmation
parent: v14.415
status: open
action: the deposited literature scan's two checkable mathematical claims (the scalar tanh identity and the Gudermannian-swap angle relation) are independently confirmed exact. The literature-search verdicts themselves are outside what this auditor can re-verify by recomputation; the entry's own coverage caveat is accurate.
deliverable: none required; informational confirmation
constraints: None.
