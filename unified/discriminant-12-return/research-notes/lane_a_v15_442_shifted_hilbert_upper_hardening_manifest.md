# Lane A v15.442 SHA-256 manifest

Witness path: unified/discriminant-12-return/research-notes/lane_a_v15_442_shifted_hilbert_upper_hardening.py

- commit: 6b8cdaa111f667efbf19ee360ca646882b041c15
- git blob: 81a906158deb9edc343b45f709c904f4faf053cb
- SHA-256: 2b5378fb648eaa3e525c4eece91df176e75e5cddffdbd89f2ab549adc2554363

Reproduction:

    python3 -I unified/discriminant-12-return/research-notes/lane_a_v15_442_shifted_hilbert_upper_hardening.py
    sha256sum unified/discriminant-12-return/research-notes/lane_a_v15_442_shifted_hilbert_upper_hardening.py

Analytic certificate: moment-Gram positivity plus quadratic-form domination by the classical Hilbert matrix gives ||G_N||<=pi. Combined with Round 491's audited essential-norm lower bound, ||G_N||=pi and the same-parity constant-Hankel tail norm is exactly pi/2.

Scope: chosen counting-measure ell2 only; not source-native Suzuki Phi and not FULL_K_TRANSFER.
