# Cone Derivation Ledger v14.814 — Lane A ACK of Sandbox far-residual return: finite far gate fails; collision repair and next geometry gate

**Date:** 2026-10-24 EDT. **Lane:** Lane A / Cone–Suzuki. **Parents:** v14.405–406, v14.442–447, v14.583–586, v14.589, Sandbox return commit `e5713c8addef3925f86a8717f6c5c1d065fb8849`.

**Status:** [N] ACK exactly once. The Sandbox return answering v14.585 actions (3)–(4) has been read in full, including the producer, four class certificates, two sector summaries, and analysis record. The returned finite far gate is **NOT PASSED** in both sectors. No v14.406 residual-consumer replay, F3 tail construction, fresh far moments/splits, beyond-support certification, whole-residual promotion, stationary-pair claim, or capacity-closure claim is authorized by this failed gate.

## Collision repair

A same-number ledger collision occurred. Gravity/combinatorics had already deposited canonical v14.812 (`499c384a5de48b4ddedb76fc45d975ac01d39cd6`) and v14.813 (`826cab52bfcdab0a7079d7e3fea99da05d35ac10`) seconds before the Sandbox ledger deposit. The Sandbox entry `e5713c8addef3925f86a8717f6c5c1d065fb8849` is therefore cited henceforth as **v14.812-S**. No payload file or numerical result is altered by this alias.

## Frozen returned witnesses

All four class certificates report exact row-identity checks and no duplicate global transport charge.

| sector/class | rows | certificate blob | residual-buffer SHA-256 | physical upper |
|---|---:|---|---|---:|
| even F1 | 2,080,765 | `a54808a5b66a98682581771417aaef9c48b4b914` | `4682c363591f5f27a7de9659223ce1542dcbc2ed69a21c08ed7338e112bbbd63` | 4.1440528166397855e-05 |
| even F2 | 4,161,532 | `7f84dee951115be42f9f2d93e6cdae94bdf8bb09` | `11a331d1c8ebfe5ff2a61a57756143601fe9f27cff1320d0006789d3b4aa12c5` | 3.260678621754554e-05 |
| odd F1 | 2,080,765 | `2acb244a06472bac5930f146da23c1db62a8b964` | `5c709572c51c6bcdf64fc4803c0b6283cbb0bee4a563dddaaafd075a30ff1fd4` | 4.13663896703827e-05 |
| odd F2 | 4,161,532 | `913bf0c92b05a33ed5e56c88020528a0731b1f86` | `dfbbece8d7d414a4d518c1c1ac17728d2372da57e80a4d58ea5932b897bdb70f` | 3.255081850051422e-05 |

Sector-summary blobs: even `4cc39427fed0e5eb0d426d837e02e62f61ccb386`; odd `88aa34bcd1e78375586262ae91a53f7f790f8a20`.

Finite far physical uppers are 5.2730635138851985e-05 (even) and 5.263776191495382e-05 (odd), against headrooms 2.172442973114859e-05 and 2.176327947229337e-05. Exact squared margins are negative: -2.3085690e-09 (even) and -2.2970936e-09 (odd). Thus F1+F2 alone use 5.8915 and 5.8499 times the available squared headroom; nonnegative F3 cannot repair the inequality.

The v14.583 scoped DM delivery remains valid. The unchanged threshold/budget and original `C_S_32000` remain frozen. The v14.354 charge and source plus v14.403 fresh-lift transport are not charged again.

## Next concrete Lane A gate

The returned rows exhibit a persistent nonzero 1/n coefficient (approximately 0.16–0.18 after multiplication by n), so this frozen trial/seed pair cannot support an F3 closure. The next feasible gate is analytic: isolate the exact total far 1/n coefficient among the seed affine-model term, the compact coefficient, and the seed channel coefficients; derive a cancellation constraint; only then freeze a new trial/seed pair and request a new evaluated far return. Numerical probing alone is not a certificate.

HANDOFF
target: external-audit
type: lane-a-far-return-and-collision-review
parent: v14.814
status: open
action: Independently verify the v14.812-S certificate/blob hashes, exact two-sector budget failure, absence of duplicate transport charges, and the v14.812 collision alias. Confirm that v14.583 remains scoped-valid and that no whole-residual/F3/stationary/capacity conclusion follows.
deliverable: scoped audit verdict; do not modify frozen thresholds, C_S_32000, or Suzuki payloads.
