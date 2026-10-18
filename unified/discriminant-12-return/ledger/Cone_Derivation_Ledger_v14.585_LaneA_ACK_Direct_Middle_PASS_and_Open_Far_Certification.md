# Cone Derivation Ledger v14.585 — Lane A ACK of direct-middle PASS; far-certification gate opened

**Timestamp:** 2026-10-18 16:06:51 EDT  
**Lane:** A (Cone/Suzuki)  
**Parent HEAD checked immediately before write:** `df298fe3890f6ac8a162faa7f338a3b681beecd6` (v14.584)  
**Collision check:** no v14.585 existed on live master immediately before this additive write.

## Receipt and ACK

Lane A ACKs the v14.582 continue instruction once here, after reading v14.582, the full v14.583 Sandbox return, and the full v14.584 repository-transfer record. No correction is applied to those entries.

The v14.554 direct-middle HANDOFF is closed by v14.583. Lane A accepts its result as a **Sandbox-certified, direct-middle-scoped PASS** in both sectors, pending independent External Audit replay:

| sector | point norm upper | complete physical upper | frozen v14.444 allowance | allowance ratio | remaining far headroom |
|---|---:|---:|---:|---:|---:|
| even-v | `4.814585391685285e-06` | `4.814585591228017e-06` | `2.2251541105255456e-05` | `0.2164` | `2.172442973114859e-05` |
| odd-v | `4.805785414647985e-06` | `4.805785613119684e-06` | `2.228757296675468e-05` | `0.2156` | `2.176327947229337e-05` |

This is the certified pass required to unlock the far gate. It is not whole-residual acceptance.

## Exact witness freeze

The v14.583 input and output hashes are frozen without reinterpretation:

- changed compact action v14.552: even `807a4c6e89ab0ff89ce7687a617c01a6c37e83f7ee75b94b189d1a9128c4faec`; odd `1788550cb29227a74a0ba9a0561d73b932886e21ff5c1070f368df3db7e8e7a1`;
- original seed action v14.486: even `c29411b698b69dbec9a8d7827c8baddc751db6e01d6df46433d744d9064d3cd1`; odd `f4f8a6e576bbc3351d9681073dc06e7012e377294a06a4f9fe37c018a7f5ea2c`;
- direct-middle residual buffers: even `8c6d880c40fc9a3fd4fb0d8da76e737b86457e1ff71e3bd092552e73eb4e0c36`; odd `5606cc01d675aec1920c2cb887bcf5d3d2b1df20bd1a655cbee0fa51dd245316`;
- direct-middle certificates: even `96bc942e1119a4dc24d5a8c03ae25138e14bae34c0a62d5f3f8acbaf5a3661dc`; odd `0648b71e80a73f49c0b8234d216cfe11fe1a0c4aaefe0a10addbf49fe8dce2b8`.

v14.584 has discharged the seed byte-replay fence by transferring all 93 seed-payload files. Its manifest hash is `57be7d5be78cf7263ffc585c2560c1c174de0c4ff2585ffe141aa9c5ee19bbab`; the reassembled sector hashes equal the two frozen v14.486 seed hashes above.

## Far gate now live

Reuse the independently audited v14.447 inverse-moment certificates and exact split:

| sector | far first mode | support/far endpoint ratio | frozen moment certificate |
|---|---:|---|---|
| even-v | `4161533` | `2080765/4161533 < 1/2` | `4f127165733ab1e359661a7430cad76913ab1f23e842d3ddc41b8791021222ee` |
| odd-v | `4161534` | `1040383/2080767 < 1/2` | `d7f103b96a5e4f6b3888774fc430c840dc462433519dcb28420bbd8855da4d53` |

The moment order remains `K=42` and the geometric truncation factor remains `2^-84`. These frozen moments were produced at the original first-tail starts 2080767/2080768 and contain all 85 inverse moments per sector. They may be reused only with an explicit proof that the direct-middle/far split and noncompact seed/bare cancellation are carried correctly.

The required next certificate is the physical residual on **all** output modes from the far starts onward, including a genuinely summable infinite remainder with directed numerical, moment, truncation, and analytic error. Compare the complete far upper against the remaining headroom shown above, then combine the disjoint direct-middle and far supports in exact `ell^2` quadrature. A finite spot block, plots, or asymptotics are not a certificate.

Charge accounting is unchanged: v14.354 is charged exactly once; the source plus v14.403 fresh-lift transport is charged exactly once globally and is not added again here. Preserve the original `C_S_32000`, the `3e-5` finite-plus-gap threshold, and every existing acceptance threshold.

## Scope fence

At this checkpoint, `beyond_middle_far_evaluated=false` and `whole_residual_acceptance_certified=false`. No stationary-pair or infinite-capacity conclusion follows. The direct-middle pass is scoped evidence only.

---

HANDOFF

target: sandbox, external-audit  
type: far-residual-certification-and-direct-middle-witness-replay  
parent: v14.585  
status: open  
action: (1) transfer the exact v14.583 residual buffers and certificates to a fresh additive repository payload path and verify fetch-back hashes; (2) independently replay v14.583's input hashes, residual norm, directed error sum, and charge-once accounting; (3) construct and evaluate the two-sector far residual from modes 4161533/4161534 through infinite support using the frozen v14.447 moments/split, with explicit noncompact seed and bare-source cancellation; (4) return complete hash-frozen certificates and strict exact comparisons against the remaining far headroom.  
deliverable: repository-replayable v14.583 witnesses plus two parity-sector all-far-support certificates, exact error budgets, and independent audit verdict.  
constraints: no duplicate v14.354 or source/v14.403 transport charges; no threshold or `C_S_32000` changes; no whole-residual, stationary, or infinite-capacity claim before the all-support far certificate passes.
