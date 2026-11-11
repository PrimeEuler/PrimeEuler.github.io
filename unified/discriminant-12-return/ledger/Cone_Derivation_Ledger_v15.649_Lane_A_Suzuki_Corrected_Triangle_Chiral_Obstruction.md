# Cone Derivation Ledger v15.649 — Suzuki: corrected physical signed three-cycle excludes diagonal chiral symmetry

**Date:** 2026-11-10. **Track:** Lane A original frozen Suzuki five-frequency commutator only. **Parents:** v15.420, v15.497, v15.643–645, and the explicit exploratory sign erratum v15.648. **Status:** [D] exact-rational physical signed three-cycle; [N] prior v15.644 sampled edge; [O] the actual certified uniform two-sided operator-norm bound.

## Fresh source and collision control

At preparation, master was `e3a594b24825d2193762fa3b879520ccc4416c87`, containing the corrected additive v15.649 witness, and the prior v15.648 erratum, with no v15.649 ledger file. The unrelated gravity v15.647 collision was already fenced explicitly in v15.648. All new files additive; frozen original v15.643/v15.647-named witness scripts remain untouched.

## Correct physical translation signs

The exact v15.420 signed term is `sigma*tau*alpha_q*alpha_r M_(G_{sigma,tau}^{qr}) U_(tau log(r)-sigma log(q))`, with regular group displacement `g=tau v_r-sigma v_q`. Select `sigma=tau=+1`; hence `g_{qr}=v_r-v_q` and the phase sign is +1. On the `Z^4` basis `v_2=e_2`, `v_3=e_3`, `v_5=e_5`, choose vertices

`h_0=0`, `h_1=e_3-e_2`, `h_2=e_5-e_2`.

They lie in every box `F_R=[-R,R]^4` for `R>=1`. Their displacements are exactly `h_1-h_0=g_{23}`, `h_2-h_1=g_{35}`, `h_2-h_0=g_{25}`. Thus these three physical support terms create a triangle **provided their actual coefficients are nonzero at one common x**. This is precisely what the incorrect-sign exploratory witness of v15.648 did not show.

## Exact rational nonzero physical coefficients

At the fixed rational field parameter `x=2469/20000`, the faithful regular representation row h uses the coefficient evaluated at `x+h·(log2,log3,log5,log7)`. The corrected witness evaluates (using 100 positive atanh terms with explicit rational remainder bounds, exact Fraction interval operations and certified sawtooth wrap floors) all three source-faithful signed `G_{+,+}` coefficients:

| row-edge (h,h-g) | physical pair | interval midpoint for G (display only) |
|---|---|---:|
| (h1,h0) | 2,3 | +1.939481082381508 |
| (h2,h1) | 3,5 | +0.704095732488063 |
| (h2,h0) | 2,5 | +1.625984516591870 |

Every interval has a **strictly positive rational lower endpoint**; `alpha_q alpha_r>0`, so every actual finite-matrix off-diagonal coefficient is nonzero. This is an *exact source-faithful three-cycle*, not an abstract or incorrectly signed support graph.

## Rigorous scoped implication

For any diagonal unitary sign involution `Gamma e_h=gamma_h e_h`, `|gamma_h|=1`, `gamma_h^2=1`, anticommutation `Gamma B_R(x)Gamma=-B_R(x)` forces `gamma_{h_i} gamma_{h_j}=-1` on every nonzero edge. Multiplying the three edge equations gives `1=(-1)^3=-1`, impossible. More generally a diagonal unitary conjugation assigning `-1` to every edge is impossible by the same odd-cycle argument. Hence **no diagonal chiral/sign grading can force plus/minus spectral symmetry of the physical finite field** at the declared x for any R>=1.

This does **not** exclude non-diagonal symmetries or accidental spectral symmetry, does not lower-bound a spectral edge, and does not establish failure/success of `C_16<4.10`. It closes a specific shortcut: the positive-edge `eigsh(...,which='LA')` sample from v15.644 cannot be doubled or declared the full norm on grounds of diagonal bipartiteness.

## Frozen corrected replay

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_649_corrected_physical_triangle.py`; witness commit `e3a594b24825d2193762fa3b879520ccc4416c87`, Git blob `919ccf78c0b6c62a29ffc514e5a203757395858f`. Runnable with Python 3 standard library. No sampled float participates in assertions.

**Next required certificate:** a *rigorous two-sided* and *all-x* upper bound `C_{16}=ess sup_x ||B_{F16}(x)||<4.10`, with independently replayed rational remainder `E_16<0.142` from v15.645. The previous one-fiber positive edge ~3.79708 is not an upper bound; a one-fiber negative-edge Lanczos attempt timed out, demonstrating no mathematical no-go. Explore interval matrix SOS/norm certificates or structured domain decomposition, with small-radius exact verification and resource accounting before large-memory execution.

Protect original Suzuki seed, original `C_S_32000`, thresholds `3e-5` and `.002`, v14.405/406 finite-plus-gap PASS and v14.814 far FAIL, all exactly-once charges. `FULL_K_TRANSFER=INCONCLUSIVE`, no source-native synthesis or whole-residual/stationarity/capacity closure.
