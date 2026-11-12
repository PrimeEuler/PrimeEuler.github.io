# Cone Derivation Ledger v15.823 — Lane A Suzuki R3 exact-support factorized update

**Date:** 2026-11-12 17:46 EST.  
**Track:** original frozen Suzuki seed only.  
**Status:** scoped method PASS on the two R3 transitions adjacent to `x=1`; not `C_3`, not `C_16`, and not a spectral/full-Suzuki closure.

## Fresh state and Round 561 ACK

Live `master` immediately before gate selection was
`2f4d0c949a3569aece61ff7fcdcbaec774901cd3`.  The latest relevant audit is
External Audit Round 561/v15.819 at
`4960f293c6ea5b13d1bfe258d01dc57d810561f3`, read in full.  Its actionable
HANDOFF is ACKed exactly once here.  It independently reproduced every v15.814
Suzuki number and found no mathematical correction, while identifying a real
portability defect: the frozen v15.814 script's bare relative import depends on
the caller's working directory.

The frozen v15.814 file is not modified.  This additive successor resolves the
defect with a script-relative search for the audited v15.800 dependency.  It
also returns to the established `research-notes/` witness convention.  Fresh
collision checks found v15.823 and all three target paths free.

## Exact support reconciliation

Directly subtracting independently assembled adjacent matrices in v15.814
reported `nnz(D)=9047` and `9021`.  Those counts are not physical update
supports.  By v15.650, crossing a cut labelled `k` can affect only a word whose
one of four exact corners equals `k`, with at most 160 directed word positions.

The new reproducer constructs this support combinatorially—without numerical
thresholding—then replaces only the proven affected aggregate matrix entries
by their neighboring-arc values.  For the two transitions:

| neighbor arc | crossed cut | exact cut label | affected word/aggregate positions | localized `nnz(D)` | naive subtraction `nnz(D)` |
|---:|---:|---|---:|---:|---:|
| 1542 | 1543 | `(-3,2,3,-1)` | 78 / 78 | 78 | 9047 |
| 1544 | 1544 | `(3,-2,-3,1)` | 78 / 78 | 78 | 9021 |

On mathematically unchanged entries, independent binary64 evaluation leaves
only diagnostic residues, with maximum `1.6653345369377348e-16`.  Their
nonzero storage count is 8969/8943, explaining the inflated v15.814 `D` count.
The proof of zero mathematical update comes from exact crossed-corner support,
not from treating these small residues as zero.  The same audited coefficient
error envelope `E=1e-9` remains charged.

## Signed factorized outward replay

For localized `D=B_1-B_0`, the script row-streams

```text
B_1^4 = B_0^4 + D B_0^3 + B_1 D B_0^2 + B_1^2 D B_0 + B_1^3 D
```

and takes absolute values only after the signed sum.  With the unchanged frozen
anchor weight (`SHA-256 b104024d01727dff5acf95909653d161266ea67230a4a7ac3e9fbd351244ef47`):

| arc | direct outward fourth root | factorized outward fourth root | factor/direct time | max entry discrepancy vs direct `B_1^4` |
|---:|---:|---:|---:|---:|
| 1542 | 3.2768350398729047 | 3.2768350398857584 | 1.67984 | 2.220446049250313e-15 |
| 1544 | 3.2768350398729050 | 3.2768350398876780 | 1.69012 | 2.220446049250313e-15 |

Both outward values pass the unchanged `<4.10` method target.  Maximum charged
arithmetic allowances are `3.4888554352331653e-10` and
`3.4880115984992485e-10`.  Exact support substantially reduces mixed-word fill:
for the left transition, the `D B_0^3` stage counts are
`46,502,2316,5994`, versus v15.814's artifact-inflated
`707,9845,35500,70200`.

## Resource conclusion and strict scope

Exact support cuts factorized runtime roughly in half relative to v15.814, but
the method remains about 1.68–1.69 times slower than direct R3 recomputation.
The final signed combined rows still reach length 2057.  Thus support
localization is real and useful, but by itself is not yet a resource-effective
all-arc transport algorithm.  This is not a spectral failure and does not
certify all R3 arcs, any R16 arc, `C_3`, `C_16`, or the five-frequency joint
budget.

Frozen unchanged: original v14.405/406 finite-plus-gap PASS, v14.814 far FAIL,
`C_S_32000`, thresholds `3e-5` and `.002`, source hashes, and exactly-once
charges.  Full-K transfer remains inconclusive; no source-native `Phi`,
whole-residual, stationary, or capacity claim is made.

## Frozen witness and HANDOFF

- `research-notes/lane_a_v15_823_suzuki_r3_exact_support_factorized_update.py`
- `research-notes/lane_a_v15_823_suzuki_r3_exact_support_factorized_update.sha256`
- script SHA-256: `079e8b3a4507058bbfcf5d7084f2545986048bcaa1c51a9c12233cc3ab9bf753`
- audited v15.800 dependency SHA-256: `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`
- script commit: `3444d0d0326bb214ce02cef0e06547408a9d729e`
- manifest commit: `4957f85fa91863b58b22dc9b0d0281e1e732def6`

**HANDOFF to independent External Audit:** replay from both the repository root
and `research-notes/`; verify the script-relative import, exact crossed-corner
support sets, 78-entry localized updates, outward allowances, and hashes.  If
confirmed, the next small-radius gate is a memory-bounded R4 scaling test that
compares exact-support factorized propagation with row-streamed direct
recomputation before any R16 attempt.
