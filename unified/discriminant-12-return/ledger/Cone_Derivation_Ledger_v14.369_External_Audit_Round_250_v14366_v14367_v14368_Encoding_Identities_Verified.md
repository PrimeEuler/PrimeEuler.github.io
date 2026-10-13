# Cone Derivation Ledger v14.369 — External Audit Round 250: Unit-Circle/Hyperbolic Encoding Note (v14.366–368) — All [D] Identities Independently Verified

**Date:** 2026-10-13
**Track:** External Audit
**Status:** [V] v14.366, v14.367, v14.368 and the full research note `Unit_Circle_Encoding_and_Hyperbolic_Cone_Form.md` are read in full. This is a different kind of content from the computational certificates audited in Rounds 241–249: a symbolic/combinatorial mathematical note, carefully tagged `[D]` (derived/verified), `[I]` (interpretation), `[O]` (open/probe-pending), explicitly making **no seed, residual, or capacity claim**. Every `[D]`-tagged identity is independently re-verified below by symbolic algebra (sympy) and, where applicable, direct computation — all confirmed correct. The `[I]`-tagged citation to the separate "Totient note" is verified accurate down to its exact proposition numbers.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–365, v14.366, v14.367, v14.368.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `8d4f201...` (v14.368), matching local HEAD; live ledger max was v14.368. v14.369 is next-free. No collision.

---

## 1. Core encoding identities (§§1–3 of the note) — independently verified

Using sympy, verified symbolically for general `n` (not just numeric spot checks):

- `z_n = ((n-1)+2i√n)/(n+1)` lies exactly on the unit circle: `Re(z_n)² + Im(z_n)² = 1` — confirmed.
- `φ_n = 2·arctan(1/√n)` satisfies `cos φ_n = Re(z_n)` and `sin φ_n = Im(z_n)` — confirmed.
- Rim defect `1 − Re(z_n) = 2/(n+1)` and chord `|1−z_n| = 2/√(n+1)` — confirmed (the chord identity requires `(1−Re)² + Im² = 4/(n+1)`, verified algebraically).
- Hyperbolic form: with `ψ_n = ½ln n`, `cosh ψ_n = (n+1)/(2√n)` and `sinh ψ_n = (n−1)/(2√n)` — confirmed directly. `tanh ψ_n = (n−1)/(n+1)` and `sech ψ_n = 2√n/(n+1)` — confirmed (sympy's default `.simplify()` on the raw `tanh`/`sech`-of-`log` expression did not fully reduce to zero; rewriting through `exp` before simplifying gives exactly `0`, and numeric spot checks at `n=2,3,7,100` agree to machine precision — noting this only because a naive first pass looked like a failure and had to be chased down, not because anything was actually wrong).
- `log(m/4) = 2(ψ_m − ln 2)` — confirmed exactly.

## 2. Euclid-point examples — confirmed by direct computation

Computed `(Re, Im) = ((n−1)/(n+1), 2√n/(n+1))` directly for `n = 4, 9, 16`: `(3/5, 4/5)`, `(4/5, 3/5)`, `(15/17, 8/17)` respectively — all three match the note's stated values exactly.

## 3. Pair encoding (§6 / v14.367) — independently verified

`z_{n,k} = ((n−k)+2i√(nk))/(n+k)` on the unit circle, `ψ_{n,k} = ½ln(n/k)` with `tanh ψ_{n,k} = (n−k)/(n+k)` and `cosh ψ_{n,k} = (n+k)/(2√(nk))`, rapidity additivity `ψ_{n,k} + ψ_{k,j} = ψ_{n,j}`, and the sharpened seed-contact identity `log(m/4) = 2ψ_{m,4}` — all confirmed symbolically, the same way as §1 (again via `exp`-rewrite for the `tanh` case).

## 4. Hyperbola/divisor content (§7 / v14.368) — classical components confirmed, citation verified accurate

- `A(n) = T(n) − D(n)` with `T(n) = n(n+1)/2`, `D(n) = Σ_{k≤n} d(k)`, and the recursion `A(n+1) = A(n) + (n+1) − d(n+1)`: this is an immediate telescoping consequence of the definitions of `T` and `D` (`T(n+1)−T(n) = n+1`; `D(n+1)−D(n) = d(n+1)`), correctly marked `[D, classical]`.
- `d(n) mod 2` is the square indicator: **independently verified by direct computation for every `n` from 1 to 2000 — zero exceptions**, matching the note's stated verification range exactly.
- The V4-overlay citation to `arxiv/note-totient-v4qr12/Note_TotientHyperbolas_V4QR12_v1.0.tex`: located the source file and confirmed the complementarity identity `φ_+(r)+φ_-(r) ≡ 1 (mod 12)` is literally present (line 153 of the `.tex` source) for `U(12) = {1,5,7,11}`, and the genus-split claim (`{1,11}` split / `{5,7}` inert in `ℚ(√3)`) is likewise present (line 190). **The specific proposition numbers cited — "Props. 4.2/4.3" — were checked against the source's own section/theorem structure and are exactly correct**: `\section{The double V_4↔QR(12) bijection}` is the note's 4th section, containing (in order) `prop:bijection` (4.1), `prop:complement` (4.2), `prop:genus` (4.3) — matching the citation precisely, not just approximately.

## 5. What this round does not evaluate

Per the note's own explicit scoping, §4's three candidate seed modifications (sech-damped, tanh-modulated, rim-defect) are named only as a "dictionary," not asserted as machinery — the actual finite probe testing them against the frozen v14.353 residual buffers is stated to be running separately in the sandbox, with its result "reported separately." There is accordingly no seed, residual, or capacity number in v14.366–368 for this round to verify; this auditor will review that probe's result when it lands, with the same rigor applied to every other numerical claim in this thread.

## 6. Verdict

```
v14.366/367/368 and the underlying research note: every [D]-tagged
  identity independently verified -- symbolically for the general-n
  statements (sympy, confirmed via exp-rewrite where a naive simplify
  call initially looked inconclusive), and by direct computation for
  the specific numeric claims (Euclid points; d(n) mod 2 up to n=2000,
  zero exceptions).
[I]-tagged citation to the separate Totient note verified accurate,
  including exact proposition numbers (4.1/4.2/4.3).
No seed, residual, or capacity claim is made or evaluated in this round,
  consistent with the note's own explicit scoping. Nothing miscomputed
  found.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.369
status: closed
action: all [D]-tagged identities in v14.366-368 independently reproduced and confirmed correct; the Totient-note citation checked accurate to the exact proposition numbers. No corrections needed. This auditor will review the §4 finite-probe result (sech/tanh/rim-defect seed candidates vs. the frozen v14.353 residual) with full rigor once it is reported.
deliverable: none required; independent confirmation only
constraints: None.
