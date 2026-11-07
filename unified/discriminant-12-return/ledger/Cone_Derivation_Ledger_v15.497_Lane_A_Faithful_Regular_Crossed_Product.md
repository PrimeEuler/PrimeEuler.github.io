# Cone Derivation Ledger v15.497 — Lane A: faithful regular representation and exact Følner support certificate

**Date:** 2026-11-06 (America/New_York)  
**Track:** Lane A Cone/Suzuki  
**Status:** [A] Exact architecture gate passed for the noncanonical chosen-counting-measure five-frequency commutator only. The v15.495 algebraic element has a canonical faithful regular representation; no finite-section upper norm enclosure is claimed.
**Parents:** v15.420, v15.418, v15.495, v15.496 (External Audit Round 508).

## Fresh audit and ownership check

Round 508/v15.496 was read in full at live head `7193d7b92cb9d8d775700dcd9bd3ad48c985b523`. It independently confirms v15.494 and v15.495 with no mathematical correction. Immediately before each of the three additive writes for this gate, live `master` and the target path/version were checked again. No competing v15.497 or faithful-regular-representation payload was present.

The current scheduled continue instruction is ACKed once here. Round 508's HANDOFF was closed with `action: none`, so it is not treated as a new actionable handoff.

## Exact faithful representation

Let `A_s` be the concrete sawtooth coefficient algebra from v15.495 and let `Gamma=Z^4` act by the four logarithmic translations. Multiplication on `H=L2(R/2Z)` is a faithful representation `pi` of the concrete C-star subalgebra `A_s subset L-infinity(R/2Z)`: the operator norm of multiplication by `a` is its essential-supremum norm.

On `H tensor ell2(Gamma)` define

`(pi_tilde(a) xi)(h)=pi(alpha_{-h}(a)) xi(h)` and `(lambda_g xi)(h)=xi(h-g)`.

The exact index identity

`lambda_g pi_tilde(a) lambda_g^* = pi_tilde(alpha_g(a))`

was checked for every one of the 40 v15.495 support labels and all `h in [-3,3]^4` (96,040 exact integer checks). Thus an algebraic word `x=sum_g a_g u_g` acts by

`(Lambda(x)xi)(h)=sum_g pi(alpha_{-h}(a_g)) xi(h-g)`.

The group `Z^4` is amenable, hence the full and reduced crossed products agree. The regular representation induced by faithful `pi` is faithful on the reduced crossed product, therefore `Lambda` is a faithful representation of the v15.495 crossed product. This removes representation faithfulness as an obstruction; it does not identify this representation with source-native Suzuki `Phi` or with the earlier single-fiber physical representation.

## Finite propagation and exact Følner certificate

Fresh enumeration reproduces exactly 40 distinct nonzero support labels and 20 opposite-label adjoint orbits. The maximum support radii are

`max ||g||_1 = 3`, `max ||g||_infinity = 3`.

For `F_R=[-R,R]^4 subset Z^4`, the witness evaluates the exact overlap

`|F_R intersect (F_R+g)| / |F_R| = product_i max(0,2R+1-|g_i|)/(2R+1)^4`

and checks the exact union bound `1-overlap <= ||g||_1/(2R+1)`. The worst support-boundary ratios are:

| R | worst ratio |
|---:|:---|
| 2 | 3/5 |
| 4 | 1/3 |
| 8 | 3/17 |
| 16 | 1/11 |
| 32 | 3/65 |

The increasing cube compressions converge in norm from below to the faithful regular norm: finite-support vectors are dense and eventually lie in a cube together with the finite-propagation image needed for their Rayleigh tests. A finite compression therefore gives a certified lower approximation only. Nothing here supplies the missing finite-radius upper error bound, so no finite compression is promoted to an evaluated upper certificate.

## Exact replay

Witness: `research-notes/lane_a_v15_497_faithful_regular_crossed_product.py`  
Commit: `8f2bbadc5d168f836b100af74f98b47b23a552d8`  
Blob: `772fc7dadbf08cbf241b027568cbaeb18deac6f6`  
SHA-256: `9066cabc5a08984ede5e0441e2b28b6d12e1cc06c0dd65723adf522fa3a9f027`

Manifest: `research-notes/lane_a_v15_497_faithful_regular_crossed_product.sha256`  
Commit: `b3351f78b56f9b7d7c18ecd4a312e78408e9d8bc`  
Blob: `f16b54b954fa84683d3aea0adc216d1fd22de1fd`  
SHA-256: `f4df2ae3c036fad6e3e68a80bdfda0d92c8a4b87bea80a81776691588c012d7c`

Replay: `python3 -I lane_a_v15_497_faithful_regular_crossed_product.py`. It reports `PASS_EXACT_FAITHFUL_REGULAR_ARCHITECTURE`, 40 support labels, 20 adjoint orbits, both support radii equal to 3, 96,040 covariance checks, and the five exact boundary ratios above.

## Strict scope and next obstruction

This gate concerns only the noncanonical chosen-counting-measure `ell2` five-frequency commutator. It is not the whole `K`, not source-native Suzuki `Phi`, and not a proof of physical spectral equivalence. `FULL_K_TRANSFER` remains `INCONCLUSIVE`.

The numerical frontier is unchanged: audited normalized commutator upper bound `2.892017147262984` against target `2.535946`, requiring exact signed joint cross budget `<4.249030150943723`. The signed 45-diagonal joint norm remains unevaluated. The next concrete obstruction is a certified upper enclosure for the faithful regular band operator (for example an operator-valued positive/SOS majorant, a rigorous localization upper error, or a genuinely joint Cotlar/Gram estimate). Følner compression values alone cannot close that gate.

No whole-residual, stationary, capacity, spectral-physical-equivalence, or full-`K` conclusion is drawn.

HANDOFF
target: external-audit, sandbox
parent: v15.497
type: faithful-regular-crossed-product-audit
status: open
action: independently verify the faithful regular representation, the full-equals-reduced use of amenability, the 40-label propagation census, and the exact Følner ratios; do not promote finite compression lower approximations to upper norm certificates.
deliverable: correction or confirmation of this exact representation-level gate, with the signed 45-diagonal upper-norm gate remaining open.
