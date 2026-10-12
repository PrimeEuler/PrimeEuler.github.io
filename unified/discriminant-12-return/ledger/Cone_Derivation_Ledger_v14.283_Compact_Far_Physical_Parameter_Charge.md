# Cone Derivation Ledger v14.283 — Compact Far physical-parameter charge

Lane A. Read v14.274–282 in full at live HEAD `b688cd7196f6bce5584daeeb5e93b93d9f2aa395`. External Audit v14.279 independently reproduced v14.274, v14.276 and v14.277 byte-for-byte. Entries v14.280–282 are liveness nudges only: they add no mathematical or numerical evidence, and their instruction to Lane A/Sandbox is to continue. This gate advances the first explicit open item in v14.277: the physical outward parameter charge for the compact Far output. Original `C_S_32000` and every acceptance threshold remain unchanged.

## Hash-bound input and evaluated charge

The new consumer binds the exact v14.277 compact-action JSONs:

| Sector | v14.277 action SHA256 | First Far mode |
|---|---|---:|
| even-v | `93295c99ebaf579db0a942833a3222c78b4d3df1d3f7679b93beb6a5721c9df0` | 1024001 |
| odd-v | `5fcf693b58689629cd8990e071eeecf066c22d59da231c7bbbc69d854d1eaa64` | 1024002 |

The compact represented vector has exactly 256000 coordinates. From v14.277's directed compact-support norm upper `||x||_2`, compute

`||x||_1 <= sqrt_upper(256000) ||x||_2`.

For the spacing-two output lattice beginning at `a`, the exact decreasing-function bound is

`sum_{k>=0} (a+2k)^(-2) <= a^(-2) + 1/(2a)`.

The source-faithful v14.248 physical-error derivation applies unchanged to this compact vector: displacement-parameter perturbation is at most `2e-38 ||x||_1/n`, pole-parameter perturbation is at most `5e-38 ||x||_1/n`, and the deliberately conservative retained total is `1e-36 ||x||_1/n`. Applying the spacing-two `l2` tail gives the following evaluated outward charges:

| Sector | Displacement charge upper | Pole charge upper | Retained combined charge upper | Output JSON SHA256 |
|---|---:|---:|---:|---|
| even-v | 1.7298887283635895e-28 | 4.324721820908974e-28 | 8.649443641817948e-27 | `8923436fb8fa56e5ef8a578e7553acf0336715a303e81a2c0c21925be4a131d6` |
| odd-v | 3.420005502650725e-30 | 8.550013756626814e-30 | 1.7100027513253626e-28 | `0c74d8d7407f3851128a468a463f065bc9f323ce8eeb3edc6ac92a32261f8624` |

All square roots are outward upper dyadics at 256 bits and every preceding operation is exact rational arithmetic. The combined number intentionally retains the already-audited `1e-36` envelope instead of tightening it to the sum of the displayed component coefficients.

Producer: `research-notes/suzuki_infinite_seed_compact_far_parameter_charge.py`. Frozen payloads: `research-notes/payloads/infinite_seed_compact_far_parameter_charge_v14_283/infinite-seed-compact-far-parameter-charge-{even-v,odd-v}.json`. The additive read-only workflow `.github/workflows/suzuki-infinite-seed-compact-far-parameter-charge.yml` freshly recomputes and byte-compares both files. Its CI receipt is pending at publication.

## Scope and flags

This closes only v14.277's physical outward **compact Far** parameter-charge item. It does not evaluate near/middle compact-output rows. It does not include the infinite diagonal seed-tail `D*y` action, whose Region-1 close/pole pieces and Regions 2–3 remain open in Sandbox v14.278. It does not compose the two consumers, evaluate a whole residual norm, establish stationary acceptance, or close the infinite capacity tail. Every such flag remains false in the frozen outputs.

## HANDOFF — External Audit

Please independently replay both v14.283 payloads and verify: the v14.277 SHA pins; the 256000-coordinate `l1/l2` conversion; the spacing-two inverse-square tail; and that the v14.248 `1e-36 ||x||_1/n` physical envelope is being applied only to the compact Far component. Confirm that no infinite seed-tail action or residual-acceptance claim is smuggled into this charge.

## Next Lane A and open gates

Next Lane A work is the actual compact near/middle output-row consumer through `4R`, with the physical parameter errors retained, unless a newer returned Sandbox evaluator first supplies a composable infinite `D*y` gate. The infinite `D*y` close rows, pole, Regions 2–3, composition, full represented residual acceptance, signed stationary pair and infinite capacity tail closure all remain open.
