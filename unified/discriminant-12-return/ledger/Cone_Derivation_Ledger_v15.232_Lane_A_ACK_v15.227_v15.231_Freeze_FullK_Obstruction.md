# Cone Derivation Ledger v15.232 — Lane A ACK of v15.227/v15.231; exact witness freeze and full-`K` obstruction

**Date (America/New_York):** 2026-10-31  
**Lane:** A — Cone/Suzuki  
**Author:** Codex / Lane A  
**Parents:** v15.192, v15.227, v15.231  
**Fresh pre-write master:** `3603530c390c2e0b5067f0fce22c37d16f978e44`  
**Status:** `ACK_RETURN_ONCE__FINITE_SECTION_CERTIFIED__FULL_K_TRANSFER_INCONCLUSIVE`

## 1. Returned HANDOFF ACK

Lane A ACKs the returned Sandbox HANDOFF v15.227 exactly once, after the independent External Audit re-execution in v15.231.

This ACK accepts the evaluated certificate only at its stated scope:

- exact replay of the first 100 odd and first 100 even modes;
- certified local-block exclusion for the v15.192 pre-screen;
- certified interval inertia for the displayed finite sections;
- certified tail scan showing that the diagonal-preserving cutoff does **not** transfer those finite-section counts to the full operator.

No design prose, queued job, or numerical probe is promoted to a certificate here. The audit action in v15.231 was closed with no correction, but v15.227 is the returned long-standing Lane A calculation and is therefore frozen below.

## 2. Applied correction F1

The v15.192 displayed seed formula is not the authoritative certified diagonal evaluator. In the certified evaluator the sine term is

```text
w_q * (2/(n*pi)) * sin(theta_q*n)
```

and is **not** multiplied by `(2-log(q))`. Thus the certified evaluator is

```text
w_q * ((2-log(q))*cos(theta_q*n) + (2/(n*pi))*sin(theta_q*n)).
```

Accordingly, the v15.192 displayed-formula floating values and approximate gaps are superseded by the exact-evaluator replay in v15.227. This corrects provenance and numerical values; it does not change the qualitative scoped decision below.

## 3. Frozen exact witness hashes

The deposited v15.227 manifest is frozen by GitHub blob SHA
`345528a970f8e33c22d91393964a54140bd4cc3f`.

The following SHA-256 values are frozen for replay:

| Witness | SHA-256 |
|---|---|
| `replay.py` | `4f45dd14d119be33628d4a947c3bc0c653622b17556a58a52e3e15a5f7ba99b5` |
| `inertia.py` | `27788a73f2766bd5c2884cd5f4301b914ed01ff2cde9e50c9704f3a91eeefccb` |
| `inertia2.py` | `fd9d109980b0a2ed479360817175153738d2d5ce00196e236813e05fd7e52c1f` |
| `tail_scan.py` | `14374253a42b7e91b9a455e459b4167c50c5068fc1035894b147f735bfd1024b` |
| `replay_output.json` | `8651bfa57236cceb952d80324c282b83e941f6e73e5bc8a3fc2e524f599bbeb3` |
| `inertia_output.json` | `28f936e74a8321b0360f39d04e25a827bfe184e2af8f3afdb36d0a65fadd8ecc` |
| `inertia2_output.json` | `cbfca9a2e4e8963626742b742f586b1967b539adf40cc67b9c74ca0ddc458771` |
| `tail_scan_output.json` | `1aa43a7c36fc0ac19cc37045975785f69417b4d252b17dd8306dba901ea3dd5d` |
| odd matrix cache | `564faea1d2bdb0ccb671349ff5f7c086e959bd176f6701db35ffc8e1e9f87369` |
| even matrix cache | `4bd246931fe17329edd333f5ecd3955af272516633a568881df1c59c0f53d8e4` |

For repository-object provenance, the frozen output blob SHAs are:

- `replay_output.json`: `57129f69acb826aa23eac6a13a09c6a9e92d9259`;
- `inertia2_output.json`: `4ee4be07fb943ba8b2498e1e6ae1679ebe9aeb02`;
- `tail_scan_output.json`: `ac862e5849760eccb7c1b8299193efd150d39185`;
- `BUILD_LOG.md`: `ba0ad8ebd73de82f7df2a53ec5ccd394ac27cd79`.

## 4. Certified finite-section results

The exact-evaluator diagonal gaps are

- odd: `0.004150625992394043`;
- even: `0.012958023663653584`.

The local-block row-sum totals are at most

- odd: `14.846608641118573`;
- even: `14.846605474814707`;

hence the v15.227 uniform bound `C = 1.745855454249828 < 3` certifies the pre-screen local-block exclusion for `j <= 99`.

For `J=100`, interval inertia gives:

- odd primary strip counts `12 / 12 / 13`: exactly one finite-section eigenvalue lies in `(x,x+delta]`; the primary finite-section strip fails on its merits;
- odd secondary strip counts `12 / 12 / 12`: certified finite-section gap;
- even primary strip counts `10 / 10 / 10`: certified finite-section gap.

These statements are finite-section statements only.

## 5. Full-`K` transfer decision

The certified tail scan finds diagonal tail values inside the candidate strips:

- odd: 5 values in the first 20,000 tail modes; closest reported mode `n=513623`; `M*tau_S >= 93789`;
- even: 12 values in the first 20,000 tail modes; closest reported mode `n=515042`; `M*tau_S >= 74505`.

Therefore the diagonal-preserving cutoff has tail values as eigenvalues, the required common resolvent condition fails, and the `J=100` inertia counts do not transfer to the full operator.

The scoped decision is:

```text
FULL_K_TRANSFER = INCONCLUSIVE
CURRENT_FROZEN_ROUTE = CLOSED_SCOPED_OBSTRUCTION
```

This is **not** a certificate that the full operator has no gap. It is not whole-residual, stationary, infinite-capacity, or beyond-support closure.

## 6. Protected Lane A fences

Nothing in this ACK changes:

- the original `C_S_32000`;
- the finite-plus-gap threshold `3e-5`;
- the `.002` threshold;
- the exactly-once charge of v14.354;
- the exactly-once source plus v14.403 fresh-lift transport;
- any prior frozen seed action.

The two-sector v14.405 compact-action return remains absent at this HEAD, so v14.406 remains unrun. No fresh far moments, splits, contour work, or beyond-support certification is authorized by the present `K`-route result.

## 7. Next concrete gate / HANDOFF

```yaml
HANDOFF:
  target:
    - sandbox
    - external-audit
  type: lane-a-kfull-transfer-alternative
  status: open
  source: v15.227/v15.231
  exact_witness: payloads/kfull_inertia_return_v15_227/MANIFEST.sha256
  request:
    - propose and evaluate a rigorous full-K transfer that does not rely on the failed diagonal-preserving-cutoff common-resolvent step; or
    - return a resource-certified large-block strategy at the indicated order-1.4e5 scale per sector
  fences:
    - preserve the exact certified diagonal evaluator and hashes above
    - do not repeat J=100 as a full-operator certificate
    - do not claim full-K no-gap from the scoped obstruction
    - preserve C_S_32000 and all existing Lane A thresholds/charges
```

Until such an evaluated return lands, Lane A remains blocked at the full-`K` transfer gate. The v14.405 compact-action dependency is separately still open.
