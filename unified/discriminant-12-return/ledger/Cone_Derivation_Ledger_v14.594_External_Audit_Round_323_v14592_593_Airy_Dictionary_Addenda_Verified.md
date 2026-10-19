# Cone Derivation Ledger v14.594 — External Audit Round 323: v14.592/v14.593 Airy-Comb and Dictionary-Closure Addenda Verified

**Date:** 2026-10-19
**Track:** External Audit
**Status:** [V] v14.592 (Airy comb and two powers addendum) and v14.593 (dictionary-candidate closure) are tangential exploratory deposits under Jeremy's direction — both correctly flag `answers_lane_a_handoff=false`, `papers_modified=false`, `certified_objects_modified=false`, `G_derived=false` — not direct-middle/far-residual certification work. All file hashes verified exact; both producer scripts re-executed unmodified and reproduce every cited number exactly; the two most consequential mathematical identities were independently re-derived from scratch by entirely different methods (fresh numerical quadrature, fresh symbolic calculus), not merely by re-running the given scripts. No defect found.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–500, v14.500–591, v14.550/v14.551 (prior Sandbox exploratory deposit, Round 310).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `60df36e...` (v14.593), matching local HEAD; live ledger max was v14.593. v14.594 is next-free. No collision.

---

## 1. File-hash verification

| file | stated SHA-256 | re-hashed |
|---|---|---|
| `Airy_Comb_and_the_Two_Powers_Addendum.md` | `fdce569a15ce2d956bbe31190d9b9781d8a83fcb49dc26de08e0df7af6194fa9` | match |
| `airy_powers_probe.py` | `3e920d24387b6cf758a40ff2786557e38513d52edd42d096237918e133cd0b1f` | match |
| `dictionary_closure_probe.py` | `05de2225518bebbe82018615a4d4d8efa98a1edae51b257f743f59abc32aa1e2` | match |

## 2. Producer re-execution (unmodified, clean)

Both scripts were run directly from the repository checkout with no modification:

- `airy_powers_probe.py` exits 0 / `DONE`. Reproduces exactly: ε₀=0.6016 peV; ν₁₃=463.0 Hz, ν₁→₇=1120.5 Hz, ν₂→₉=1141.7 Hz; the quarter-law relative errors 0.764%→0.003% (Airy zeros) and 2.487%→0.056% (J₁ zeros); the "clean negative" chance-level rational matches (0.03–0.15%); the GM-wrap/Cayley worst discrepancy 1.67e-16; power-law slopes −0.4997/+0.6668; the composed constant 7.0816 vs (36π²)^(1/3)=7.0827; the evolute `27X²=8(Y−1)³`; the segment/parallelogram ratio 2/3; cone:sphere:cylinder = 1/3:2/3:1.
- `dictionary_closure_probe.py` exits 0 / `DONE`. Reproduces exactly: Test 1a relative differences `0`/`0`/`0`/`9.31e-30` (ω=0.7,2.3,5.0,9.4); Test 1b misses of 14.4%/26.0% under D_tanh; `S(∞)=1.84111691664`; the ratio and log-rate table at t=0.25…5.0, including the stated trend toward 2.

All numbers in both ledger entries match the fresh run character-for-character; neither entry overstates or rounds favorably relative to its own producer's output.

## 3. Independent re-derivation of the two load-bearing identities (not re-running the given code)

**Semicircle Fourier transform = J₁ (the crux of v14.593's closure claim).** Using `mpmath` at 30 decimal digits, this auditor numerically integrated $\int_{-L}^{L} 6\sqrt{1-(x/L)^2}\cos(\omega x)\,dx$ directly (fresh quadrature, not the cited script) for $\omega \in \{0.7, 2.3, 5.0, 9.4\}$, $L=12/11$, and compared against $(6\pi/\omega)J_1(L\omega)$: relative difference `0.0` at the first three and `9.30715198...e-30` at $\omega=9.4$ — matching the ledger's `9.3×10⁻³⁰` to all given digits, by an independent method.

**Evolute of $y=x^2/2$.** Using fresh `sympy` symbolic differentiation (standard evolute formulas $X=x-y'(x'^2+y'^2)/(x'y''-y'x'')$, etc., applied from scratch, not read from the deposited producer), this auditor derived $X_c(t)=-t^3$, $Y_c(t)=\tfrac32t^2+1$ and verified $27X_c^2-8(Y_c-1)^3\equiv 0$ identically (symbolic simplification to exactly `0`) — confirming the cusp at $(0,1)$ and the implicit form exactly as cited.

**Parabolic-segment ratio 2/3.** Re-derived by hand with an independent parametrization (segment cut by a chord from a parabola $x=fy^2$): segment area $=\tfrac43 hY$, bounding rectangle $=2hY$ where $Y=\sqrt{h/f}$ — ratio $2/3$ exactly, matching the classical Archimedes result cited. Cone:sphere:cylinder $=\tfrac13:\tfrac23:1$ is the textbook Archimedes inventory and needs no further re-derivation.

## 4. Scope and honesty check

Both entries' scope flags are consistent with their own content: v14.592 explicitly reports a "clean negative" (chance-level rational matches) rather than suppressing it, and explicitly tags its dictionary candidate `[O]` (open/unbuilt) rather than claiming closure prematurely. v14.593 then closes that exact candidate by dissolution (computed negative: the deficit-area dictionary is a legitimate dictionary but is not D_exp, and its warp has no foothold in the archimedean channel) and separately closes the independently-staged 2026-09-28 J₁-signature item by an exact equivalence — while explicitly leaving the helix-representation obstruction open and untouched. No certified object, paper, or threshold in the discriminant-12-return chain is touched by either entry, consistent with both sets of flags.

## 5. Verdict

```
Confirmed: v14.592 and v14.593 are honestly-scoped exploratory deposits.
  Every file hash is exact; both producers re-run clean and reproduce
  every cited number exactly; the two most consequential identities
  were independently re-derived from scratch by different methods and
  match exactly. No G is derived, no certified object or threshold in
  the discriminant-12-return chain is touched, and the scope flags
  accurately describe the content.
No defect found.
```

---

HANDOFF
target: sandbox
type: audit-confirmation
parent: v14.594
status: open
action: this auditor independently verified v14.592/v14.593 exactly, by fresh re-derivation of the two load-bearing identities as well as clean re-execution of both producers. No correction needed. The live open item in the main discriminant-12-return chain remains Sandbox's far-residual construction and certification (v14.585 actions 3-4).
deliverable: none required from this auditor at this checkpoint.
constraints: no duplicate v14.354 or source/v14.403 transport charges; no threshold or C_S_32000 changes; no whole-residual, stationary, or infinite-capacity claim before the all-support far certificate passes.
