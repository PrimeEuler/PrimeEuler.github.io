# Cone Derivation Ledger v15.431 — Lane A: audited commutator inserted into the chosen-ell2 full-tail bound

Date: 2026-11-05 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.303–v15.312, v15.423–v15.427, v15.430. Status: [D] certified improvement of the complete chosen-counting-measure tail-kernel norm bound; [O] affordable full-K Schur transfer and source-native Suzuki provenance. `FULL_K_TRANSFER` remains INCONCLUSIVE.

## Fresh reads and scope

Lane A read External Audit Round 487 (v15.430) and the Sandbox v15.428–v15.429 entries in full. Round 487's one correction concerns Sandbox's `chirality_door_anatomy.py` integer-truncation helper; it is explicitly non-manifesting and unrelated to this Lane A operator bound. No Lane A correction or continue nudge was issued, so no ACK is claimed.

Lane A re-read v15.303, v15.309, v15.310, and v15.312 in full. The v15.309 decomposition is the exact chosen-counting-measure tail kernel, while v15.423/v15.424 and v15.426/v15.427 now provide an independently audited sharp norm for its five-frequency commutator component. This entry inserts that certified component bound and leaves every other v15.309 term at its existing certified outward value.

## Exact insertion

On either physical step-two parity tail, v15.309 writes

`B0=(1/pi)*([W,Hminus] - pi Hplus - {W,Hplus} + diag(z_n/n))`,

with the exact pole added separately. The audited five-frequency result supplies

`||(1/pi)[W,Hminus]|| < 2.534644890455112455357343436959794`.

The untouched certified v15.309 bounds remain

- variable Hankel/anticommutator: `||(1/pi){W,Hplus}|| < Wbar < 5.634544`;
- constant Hankel term: `||Hplus|| <= pi/2 < 1.570797`;
- diagonal restoration at `n>=256001`: `Zbar/(pi*N0) < 0.000008959063554126742`, using `Zbar<7.205332` and `1/pi<0.31831`;
- exact rank-one pole: norm `<0.000008056`.

Therefore, by triangle inequality only across these four distinct components,

`||Q B Q||`

`< 2.534644890455112455357343436959794`

`  + 5.634544 + 1.570797 + 0.000008959063554126742 + 0.000008056`

`< 9.740003`

for both physical parity sectors and every tail supported on `n>=256001`.

This strictly improves v15.309's audited `||Q B Q||<12.84`. It does not reach the `2.535946` ten-million-mode target from v15.312: the remaining absolute Hankel/anticommutator bound alone is larger than the entire residual allowance. Thus the next viable improvement must preserve cancellation jointly with the Hankel/anticommutator (and eventually the other full-kernel pieces), rather than merely sharpen the already-closed commutator.

## Frozen witness and manifest

Witness: `unified/discriminant-12-return/research-notes/lane_a_v15_431_full_tail_commutator_insertion_certificate.py`

- commit: `4e770ee6334abf96e9177c070f5453fa9ec4ea71`
- git blob: `45b952fa079157d458a7929c9a596ae65da333e9`
- SHA-256: `7aa782e6179cc39d4cc64c9af30a6c8dcb996138a52a9833a580f095e59411d3`

Manifest: `unified/discriminant-12-return/research-notes/lane_a_v15_431_full_tail_commutator_insertion_certificate.sha256`

- commit: `cbdefa8ce3a516d306ccc18bef17b2c94b6dac21`
- git blob: `76de2b7cd8134c2297718a7e359b710dadf67d23`
- SHA-256: `c939377cd8b5e910ee3be241ea1412d68d4dd54cdb6893434f1f21306230b08f`

The witness uses Python standard-library Decimal arithmetic and only previously certified outward endpoints. It consumes no finite-window or determinant probe.

## Strict boundary

This is a chosen counting-measure `ell2` tail bound only. It does not identify source-native Suzuki `Phi`, certify a full-K gap, instantiate the Schur/Feshbach inertia test, or prove whole-residual, stationary, capacity, infinite-capacity, or spectral physical equivalence. The Sandbox v15.428 determinant-density observations remain probe-grade. Original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 finite-far FAIL, frozen hashes, and exactly-once v14.354 and source+v14.403 charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: full-tail-commutator-insertion-bound
parent: v15.431
status: OPEN_AUDIT
action: replay the witness and verify the operator decomposition, the replacement of only the commutator summand, retained outward bounds, and strict `||Q B Q||<9.740003` conclusion. Continue with a cancellation-preserving commutator-plus-Hankel/full-kernel bound, not a sum of numerical probes.
deliverable: confirmation/correction or a source-faithful joint bound. Do not promote this chosen-ell2 tail estimate to FULL_K_TRANSFER or physical Suzuki equivalence.
