# Lane A v15.440 SHA-256 manifest

Witness path: `unified/discriminant-12-return/research-notes/lane_a_v15_440_constant_hankel_tail_barrier.py`

- commit: `e37df271112ed448a1d9e75a737d96a71a520791`
- git blob: `d917632184edb34e83a210959bcd76965b826ab3`
- SHA-256: `2967c8104fb507c92858deb001a4c2aa10e4a9ea7b40d625d677a272f31aba92`

Reproduction:

```sh
python3 -I unified/discriminant-12-return/research-notes/lane_a_v15_440_constant_hankel_tail_barrier.py
sha256sum unified/discriminant-12-return/research-notes/lane_a_v15_440_constant_hankel_tail_barrier.py
```

Certified arithmetic:

- sharp same-parity constant-Hankel tail norm: `pi/2`;
- remaining independent triangle allowance: `0.001280986470142875676519712012280`;
- therefore tail depth alone cannot close the constant-Hankel term.

Scope: chosen counting-measure ell2 only; not source-native Suzuki Phi and not FULL_K_TRANSFER.
