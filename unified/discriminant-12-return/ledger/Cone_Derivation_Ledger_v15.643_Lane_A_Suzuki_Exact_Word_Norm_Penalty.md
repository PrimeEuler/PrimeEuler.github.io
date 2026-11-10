# Cone Derivation Ledger v15.643 — Lane A Suzuki restart: exact per-word coefficient suprema and improved Følner penalty

**Date:** 2026-11-10 (America/New_York). **Track:** Lane A — original frozen Suzuki five-frequency commutator **only**, NOT the quarter-shell/gravity program. **Parents:** v15.420, v15.495–502. **Status:** [D/N] exact-rational enclosure calculation executed on 40 physical signed transported coefficients, conditional on the audited v15.420/v15.499 representation; [O] the finite matrix-field essential supremum and the original Suzuki far-tail certificate. Independent External Audit pending.

## Restart and collision control

The previous Suzuki-specific calculation v15.501 was independently verified by External Audit Round 511/v15.502. The live ledger subsequently advanced mainly on separate Cone-geometry work. The user explicitly requested resumption at v15.501. Live HEAD was checked before starting and before the witness write; the additive witness was committed at `31f4d6e15730fda371f11cc3ce1bedc05f8f635a`. This ledger entry is additive. No production code, data, thresholds, or frozen source hashes were changed.

## 1. The exact coefficient problem

For each pair `q<r` in `Q={2,3,4,5,7}`, and each `sigma,tau=±1`, use the already-audited v15.420 coefficient and shift
`
G_{sigma,tau}^{qr}(x)
 = D_sigma(x+sigma A;A)D_tau(x+sigma A;B)
 + D_{-tau}(x-tau B;B)D_{-sigma}(x-tau B;A),
`
where `A=log q`, `B=log r`, `D_s(y;L)=s(y-sL)-s(y)`, `s(y)=1-(y mod 2)`, the translation label is `tau v_r-sigma v_q` in the exact `Z^4` lattice (including `v_4=2v_2`), and `alpha_q=log q/(2sqrt q)`. The physical signs `sigma*tau` affect operator interference but *not* the absolute localization remainder.

Rather than use the uniform v15.501 bound `||G||_∞<=2 m_q m_r`, evaluate each of the **40 exact individual** `||G||_∞` via an exhaustive piecewise-constant decomposition. Each word has possible breakpoints on the period-two circle exactly at

`x=0,` `x=-sigma A,` `x=tau B,` `x=tau B-sigma A` (mod 2).

Proof of completeness: the two signed differences in the first product can jump only when `x+sigma A` meets `0`, `sigma A`, or `tau B`; the two in the second product only when `x-tau B` meets `0`, `-tau B`, or `-sigma A`. Union equals the four displayed locations. Between ordered cuts, both products are constant. Therefore one rational interior point per cell suffices to enclose the *essential supremum*, once all branch floors and interval orderings are certified.

## 2. Outward rational computation

The replay witness uses `fractions.Fraction` throughout; it bounds `log q` by the 160-term positive atanh series at `t=(q-1)/(q+1)` with exact upper remainder `2 t^(321)/[321(1-t²)]`, and `sqrt q` by rational grid endpoints computed with integer `isqrt(q*10^70)`, with grid denominator `10^35`. It certifies that every cut interval has a strict ordering and that sawtooth wrap floors agree for each sampled cell. Products and the four-branch maxima are outward interval operations; *floating output is display only*.

Combining the 40 upper/lower word-supremum enclosures with the previously audited exact rational tensor-tent `1-c_R(g)` factors yields, for the absolute localization remainder `E_R^{word}`,

| radius R | v15.501 uniform difference penalty (display) | v15.643 exact-word penalty enclosure (rounded display) | rigorous coarse upper |
|---:|---:|---:|---:|
| 8 | 1.0389048102 | 0.4849756547931857 | <0.485 |
| 16 | 0.3019296618 | 0.1411749009458400 | <0.142 |
| 32 | 0.0814460309 | 0.0381165182040051 | <0.039 |

All strict coarse inequalities are rational comparisons on the reconstructed enclosures, not assertions about rounded decimals. Exact-rational interval widths are respectively less than `5.0e-36`, `1.5e-36`, and `4.0e-37`. Relative to the previous audited coefficient-penalty formula, the improvement is approximately 53% at radius 16. These coefficients are piecewise *constant*; this step did not sample a continuous field and call a sample its supremum.

This is a substantive improvement in a proven **upper-error term**, not a certified bound on the physical 45-diagonal band operator norm.

## 3. Immediate acceptance target

The audited v15.405 budget demands `||X||<4.249030150943723...` for the joint signed five-frequency cross operator `X`. By the v15.499 exact Følner inequality,

`||X|| <= C_{16} + E_{16}^{word},`
`C_{16}=ess sup_x ||B_{F_{16}}(x)||,` with `|F_{16}|=33^4=1,185,921`.

Since `E_{16}^{word}<0.142`, a **verified** outward enclosure `C_{16}<4.10` would suffice to prove `||X||<4.242<4.24903015`. This is only a *sufficient future acceptance gate*. No radius-16 `C_{16}` evaluation has been performed, and the earlier collocation probe ~3.763 is still NONCERTIFYING.

## 4. Frozen replay and next gate

Reproducer: `unified/discriminant-12-return/research-notes/lane_a_v15_643_exact_word_norm_tent_penalty.py`. Witness commit `31f4d6e15730fda371f11cc3ce1bedc05f8f635a`; Git blob `0d692640b98233958e6e12dc9ffc444f15265af2`. Run with plain `python3`; uses only Python standard library. Printed floating values are for orientation; rigorous content consists of rational interval inequalities and asserted branch order / wrap decisions.

**Next direct Suzuki gate:** devise and execute a resource-bounded, mathematically rigorous **upper** enclosure of `C_{16}`, including exhaustive resolution of the x-dependent piecewise-constant coefficient field and outward spectral-norm certification (e.g. interval-certified sparse positive polynomial / enclosure). Start with small-radius validation of exact 40-shift self-adjoint matrix assembly and memory/time measurements; do not confuse Rayleigh/Lanczos lower bounds with a norm upper certificate. If resource-prohibitive, document the exact obstruction and examine multiscale block methods. Independent Audit should replay all 40 word cuts and the three exact rational penalties before any promotion.

**Fences:** the seed and v14.405/v14.406 certified finite-plus-gap PASS are untouched; v14.814 finite-far FAIL unchanged; `C_S_32000`, thresholds `3e-5` and `.002`, and all once-only charges unchanged. Chosen counting-measure `ell2` is not a source-native physical Suzuki synthesis; `FULL_K_TRANSFER=INCONCLUSIVE`. No whole-residual, stationarity or infinite-capacity claim.
