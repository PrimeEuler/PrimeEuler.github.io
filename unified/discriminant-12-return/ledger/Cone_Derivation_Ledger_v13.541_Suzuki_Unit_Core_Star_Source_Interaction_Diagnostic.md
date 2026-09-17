# Cone Derivation Ledger v13.541 — Suzuki Unit-Core Star Source-Interaction Diagnostic

**Renumbering note:** originally filed as v13.537, which collided with the already-pushed `Cone_Derivation_Ledger_v13.537_Split_Matrix_Congruences_and_Combined_C4xS4.md`. Renumbered to v13.541 during External Audit Round 46. Mathematical content is unchanged.

**Status:** `[N-diagnostic]` finite binary64 midpoint computation. No theorem/index promotion.

## Scope

Decompose the source-faithful pole-free finite-high Suzuki matrix at cutoff `M=3999` into the exact linear assembly

\[
B=B_{\rm arch}+B_2+B_3+B_4+B_5+B_7,
\]

using the established unit-core coordinate

\[
n=2^a3^b u,\qquad u\bmod12\in\{1,5,7,11\}.
\]

The four block-diagonal pieces of the **full** matrix are frozen as the whitening metric. For star center `r`, retain only the three off-diagonal blocks incident to `r` and define `sigma_r` as the largest singular value of the concatenated whitened blocks. This entry tests source interactions without refitting the whitening metric source-by-source.

Executable diagnostic:

`research-notes/suzuki_unit_core_star_pairwise_source_interactions.py`

## 1. Baseline reproduction

The computation reproduces the established four-star values:

| center | sigma_r | 1-sigma_r |
|---|---:|---:|
| 1 | 0.642540833295687 | +0.357459166704313 |
| 5 | 1.002863608196589 | -0.002863608196589 |
| 7 | 0.751742333382373 | +0.248257666617627 |
| 11 | 0.774600757641453 | +0.225399242358547 |

Define class-5 selectivity

\[
G_5=\sigma_5-\max(\sigma_1,\sigma_7,\sigma_{11}).
\]

For the full matrix,

\[
\boxed{G_5=0.228262850555136}.
\]

Only the class-5 star is slightly supercritical in this finite diagnostic.

## 2. Single-source stars in the frozen full metric

| source | sigma_1 | sigma_5 | sigma_7 | sigma_11 | G_5 |
|---|---:|---:|---:|---:|---:|
| arch | .199381 | .205117 | .163835 | .177315 | +.005736 |
| q=2 | .369938 | .361855 | .314012 | .386230 | -.024375 |
| q=3 | .357832 | .465605 | .462547 | .308850 | +.003058 |
| q=4 | .245049 | .294005 | .243583 | .237226 | +.048957 |
| q=5 | .318874 | .536331 | .395739 | .402866 | **+.133465** |
| q=7 | .264509 | .275493 | .176280 | .253059 | +.010984 |

Thus the strongest **single-source** class-5 selector is `q=5`, not `q=3`. The `q=3` atom makes stars 5 and 7 nearly tied; `q=2` alone actually favors star 11 over star 5.

This distinction is important: earlier leave-one-out results showed that removing `q=3` from the full background causes the largest loss of class-5 selectivity. Therefore `q=3` is primarily a **background-dependent interaction driver**, whereas `q=5` carries the strongest direct single-source class-5 preference.

## 3. Leave-one-source-out check

With fixed full whitening, the established ablation gaps are reproduced:

| removed | G_5(all minus source) | loss from full G_5 |
|---|---:|---:|
| arch | +.174714 | +.053549 |
| q=2 | +.086466 | +.141797 |
| q=3 | **-.185645** | **+.413907** |
| q=4 | +.217243 | +.011020 |
| q=5 | +.033384 | +.194879 |
| q=7 | +.256637 | -.028374 |

Removing `q=3` reverses the class-5 preference; removing `q=5` nearly erases it. Removing `q=7` strengthens it slightly.

## 4. Pair-only connected selectivity

For a pair of isolated source pieces define

\[
J_{ij}=G_5(i+j)-G_5(i)-G_5(j).
\]

The largest positive pair-only connected term is

\[
\boxed{J_{2,3}=+0.069741612660584}.
\]

Selected controls:

\[
J_{3,5}=-0.065978677113737,
\qquad
J_{2,5}=-0.223026709364774,
\]

\[
J_{3,7}=-0.009199149708384,
\qquad
J_{5,7}=-0.127167289644093.
\]

Hence the isolated `(2,3)` pair has the clearest positive nonlinear enhancement of class-5 selectivity. The `(3,5)` pair is not positively synergistic in isolation.

## 5. Full-background pair interactions

To measure interaction in the complete source background define the inclusion-exclusion quantity

\[
C_{ij}=G_5({\rm all})-G_5({\rm all}\setminus i)-G_5({\rm all}\setminus j)
+G_5({\rm all}\setminus\{i,j\}).
\]

Largest magnitudes:

| pair | C_ij |
|---|---:|
| (2,3) | **+0.361498701067715** |
| (3,5) | **+0.301903816645162** |
| (3,4) | +0.104111507297509 |
| (2,5) | +0.097611784527579 |
| (3,7) | +0.095668890036612 |
| (arch,2) | +0.084571361222417 |
| (arch,5) | +0.066152298073746 |
| (4,7) | -0.060195529649526 |
| (arch,7) | +0.057144946313473 |
| (2,7) | -0.048116613454439 |

The strongest full-background interaction is `(q=2,q=3)`, followed by `(q=3,q=5)`. This reconciles the apparently conflicting direct and ablation diagnostics:

1. `q=5` is the strongest isolated class-5 selector;
2. `q=3` is the strongest leave-one-out dependency;
3. the largest background interaction is `q=2` with `q=3`;
4. `q=3` with `q=5` is the second-largest background interaction.

Thus class-5 selection is not attributable to a single prime-source channel. It is an interference effect in which `q=5` supplies a strong direct vertex preference and ramified `q=3`, especially through its interaction with `q=2` and `q=5`, makes that preference structurally decisive in the assembled operator.

## Guardrails

- Fixed-full-`D` whitening is intentional here; rewhitened source ablations answer a different nonlinear question.
- `C_ij` and `J_ij` are finite singular-value interaction diagnostics, not additive energies or canonical physical couplings.
- No exact Suzuki `V_4`, `D_8`, Clifford, Pell-to-Suzuki, or cone-to-Suzuki intertwiner follows.
- No asymptotic statement follows from `M=3999`.
- No RH/GRH or critical-line consequence is claimed.
- Certified Suzuki index bounds are unchanged.

## Next target

Resolve the dominant `(2,3)` and `(3,5)` interactions simultaneously by the ramified valuations `(v_2,v_3)` and the Hadamard unit-core character coordinates. The key test is whether the class-5 vertex preference survives as a stable connected interaction after separating direct `q=5` selection from the `q=3` background rotation.
