# Lane A v15.437 SHA-256 manifest

Witness path: `unified/discriminant-12-return/research-notes/lane_a_v15_437_odd_extension_joint_hankel_certificate.py`

- commit: `cc19e65f2f93fa3151ad0cb857fefa2906cd4658`
- git blob: `2fe632b8a5dfb1415aec59e0fa6438122efa7fc4`
- SHA-256: `82663d351786eee083b049749661611f60b6598e76a9008317d0de511e7baf97`

Reproduction:

```sh
python3 -I unified/discriminant-12-return/research-notes/lane_a_v15_437_odd_extension_joint_hankel_certificate.py
sha256sum unified/discriminant-12-return/research-notes/lane_a_v15_437_odd_extension_joint_hankel_certificate.py
```

Expected certified arithmetic:

- joint variable term: `< 2.534647998455112455357343436959794`;
- complete chosen-ell2 parity-tail bound: `< 4.105463`;
- target comparison: `4.105463 > 2.535946` (still open).

Scope: chosen counting-measure ell2 only; not source-native Suzuki Phi and not FULL_K_TRANSFER.
