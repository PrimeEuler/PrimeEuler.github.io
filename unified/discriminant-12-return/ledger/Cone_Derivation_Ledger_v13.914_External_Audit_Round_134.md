# Cone Derivation Ledger v13.914 — External Audit Round 134

Date: 2026-10-01

Auditor: External audit thread (Claude, independent instance).

Scope: the `r_gate.py`/`fem_screw.py`/`diag_r.py`/`sweep_r.py` reproduction code posted to `research-notes/` for v13.912 (the de Branges odd-sector invertibility question), superseding Round 133's "inconclusive, not independently verified" assessment of that entry's §4 numerical claim.

Verdict: **Upgraded from Round 133's "inconclusive" to a confirmed PASS, via three independent angles: (1) running the posted code as-is exactly reproduces the ledger's claimed numbers, (2) swapping in a completely independently-built `g(t)` implementation (from this session's own earlier work, validated separately against the Suzuki PDF) reproduces the same divergent, non-converging trend, and (3) independently checking the near-null-mode mechanism confirms the same qualitative structure claimed in v13.912 §4. This is a real result, not an artifact of one specific `g(t)` implementation.**

## 1. Code review — kernel assembly checked by hand against the README's formulas, confirmed correct

Before running anything, I read `r_gate.py` and `fem_screw.py` in full. The boundary functional `k_x(0,y)` is the clearest hand-checkable piece: given `N(x,y)=(x^2+y^2)/(4A)-|x-y|/2+A/6`, `∂_xN(x,y)=x/(2A)-\mathrm{sign}(x-y)/2`, so `∂_xN(0,y)=\mathrm{sign}(y)/2` (using `\mathrm{sign}(-y)=-\mathrm{sign}(y)`); combined with `∂_x g(x-y)|_{x=0}=g'(-y)=-g'(y)` (since `g` is even), this gives `k_x(0,y)=-g'(y)-λ\cdot\mathrm{sign}(y)/2` — which I derived independently by hand and it matches the code's `kxval = -gp(xg) - lam * sgn / 2.0` exactly. The `KN` matrix assembly (the `(x^2+y^2)/(4A)`, `-|x-y|/2`, and `A/6` pieces assembled separately as `outer(mx2,m)+outer(m,mx2)`, `-0.5*Ka_abs`, and `(A/6)*outer(m,m)`) is a correct, standard Galerkin decomposition of the stated kernel. `fem_screw.py`'s `g(t)` construction (pole term, archimedean terms, `Λ`-weighted prime sum) matches, term for term, the independently-built and PDF-verified `g(t)` I constructed in Round 129 (v13.897) and have reused since.

## 2. Running the posted code as-is — exact reproduction

```
N=400:  M1x=+2.846747e+01   (ledger claims 28.5)
N=800:  M1x=+4.563432e+01   (ledger claims 45.6)
```

Matches to the precision the ledger quoted. The posted code does what `v13.912` says it does.

## 3. The decisive check: an independently-built `g(t)`, swapped in, reproduces the same divergence

Wrote a second, from-scratch implementation of `make_g('lambda', tmax)` — different code, different grid (1201 points vs. the sandbox's finer grid), direct `mpmath.lerchphi` evaluation rather than the sandbox's power-series/direct-series hybrid. First confirmed the two implementations agree on `g(t)` itself to `~10^{-6}` at several points (`t=0,0.5,1,2,3,3.5`), then monkey-patched it into `fem_screw.make_g` and reran `r_gate.solve_moments` unchanged:

| N | sandbox's `g` (`M1x`) | my independent `g` (`M1x`) |
|---|---|---|
| 400 | 28.47 | 27.97 |
| 800 | 45.63 | 42.71 |
| 1600 | 74.3 (claimed) | 66.39 |

The absolute values differ slightly (expected — different grid resolution for `g(t)` feeds slightly different high-frequency content into the kernel), but **the qualitative claim — divergence, not convergence to the analytically-required value of 1 — is reproduced exactly**, with the same growth pattern across three refinement levels. This is the key result: it rules out "artifact of one specific `g(t)` implementation" as an explanation. Two independently-built versions of the same mathematical object, under the same Galerkin discretization, both fail to converge to the predicted value.

## 4. The near-null-mode mechanism — independently checked, confirms the claimed structure

With the independent `g(t)` swapped in, I computed the bottom 6 eigenvalues/eigenvectors of the assembled `K` at `A=2, N=800` directly (not reusing their diagnostic numbers):

| eig | value | parity | overlap with x-source |
|---|---|---|---|
| 0 | `-9.12e-4` | even | `4e-16` |
| 1 | `+1.888e-8` | even | `4e-14` |
| 2 | `+1.892e-8` | **odd** | `5.50e-4` |
| 3 | `+1.928e-8` | even | `8e-15` |
| 4 | `+1.929e-8` | **odd** | `1.30e-4` |
| 5 | `+1.938e-8` | even | `4e-14` |

This independently confirms the exact structure v13.912 §4 describes: a cluster of near-null modes (`~1.9×10^{-8}`, consistent with their claimed `~1.6×10^{-8}`) alternating even/odd parity, with the **even** modes showing essentially zero overlap with the odd x-source (`~10^{-14}`, exactly as symmetry requires) while the **odd** near-null modes show small but distinctly nonzero overlap (`5.5\times10^{-4}`, `1.3\times10^{-4}`, matching their claimed `~10^{-3}` order of magnitude). That nonzero overlap divided by the near-zero eigenvalue is exactly the amplification mechanism (`~5\times10^4`) that explains why solving `Kc=b_x` for the odd sector blows up under refinement rather than converging — independently verified, not just read and accepted.

## Revision to Round 133's verdict

Round 133 reported this specific claim as "could not independently verify... reported honestly as inconclusive." That caution was correct given what was available at the time (no posted code, would have required reconstructing unfamiliar older machinery from the ledger's equations alone). With the code now posted and independently cross-checked against a separately-built `g(t)`, the verdict upgrades to a genuine, multi-angle **PASS**: the odd-sector divergence is real, reproducible, and not an artifact of the specific prime-sum/archimedean numerics used to build `g(t)`.

## What remains open

This confirms the *numerical symptom* (divergence under refinement, the near-null-mode mechanism) is real and robust. It does not resolve the underlying question — whether `0\in\sigma(L_A^{(-)})` as an operator-theoretic fact (which would make the divergence a genuine feature of the continuum operator) versus a discretization pathology that a better-conditioned basis would avoid. v13.912 §7 already correctly identifies this as the open next step, and nothing in this round's numerics distinguishes between those two explanations — only confirms the symptom is not a mirage.

## Self-audit note

Hit two minor API mismatches running the diagnostic code under the installed scipy version (`eigvalsh` no longer accepts the `eigvals=` keyword, and doesn't return eigenvectors at all — needed `eigh` with `subset_by_index` instead). Noting this since it's a reminder that "the code runs as posted" can be environment-dependent; worth the sandbox knowing in case they hit the same thing.

## Result

\[
\boxed{\textbf{Upgraded from Round 133's "inconclusive" to a confirmed PASS on v13.912 §4's numerical claim.} \textbf{Three independent checks: exact reproduction of the posted code, the same divergent trend under a completely independently-built }g(t)\textbf{, and independent confirmation of the near-null-mode/odd-source-overlap mechanism.} \textbf{The odd-sector divergence is a real, robust numerical phenomenon, not an artifact of one specific implementation.} \textbf{The deeper question (genuine }0\in\sigma(L_A^{(-)})\textbf{ versus a discretization pathology) remains open, as v13.912 itself already states.}}
\]
