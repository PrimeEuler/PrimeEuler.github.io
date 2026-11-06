# Cone Derivation Ledger v15.437 — Lane A: odd-extension joint commutator–Hankel bound

**Date:** 2026-11-05 (America/New_York)  
**Track:** Lane A / Cone–Suzuki  
**Parents:** v15.309, v15.327, v15.423–v15.424, v15.432–v15.436  
**Status:** [D] rigorous chosen-counting-measure-ell2 parity-tail improvement `||Q B Q|| < 4.105463`; [O] the unchanged `2.535946` affordable-transfer target and every source-native/full-`K` transfer question.

## Fresh audit and collision checks

Read External Audit Round 489/v15.436 in full. It independently replays v15.435, verifies all hashes, confirms the hardened outward arithmetic without correction, and closes with `action: none`; no ACK is required.

Immediately before each of the witness, manifest, and ledger writes, live `master` and the ledger namespace were rechecked. v15.437 was next free, its paths were absent, and no other lane owned this odd-extension gate.

## Exact joint identity

Use v15.309's positive-half-line kernels on either fixed physical parity lattice,

[
(H_-f)_n=sum_{m
e n}rac{f_m}{n-m},
qquad
(H_+f)_n=sum_mrac{f_m}{n+m}.
]

For a real diagonal sequence (W=(w_n)), the off-diagonal coefficient of the variable joint operator is exactly

[
igl([W,H_-]-{W,H_+}igr)_{nm}
=
w_nleft(rac1{n-m}-rac1{n+m}ight)
-w_mleft(rac1{n-m}+rac1{n+m}ight)
=
rac{2(mw_n-nw_m)}{n^2-m^2}.
]

Let (O) be odd extension from the positive half-line to the corresponding bilateral parity lattice:
((Of)_{-m}=-f_m). Extend (W) oddly, (w_{-m}=-w_m), and let (H) be the bilateral Hilbert comparison operator with kernel (1/(n-m)). Directly grouping the (m) and (-m) summands gives, for (n>0),

[
P_+[M_W,H]Of
=
([W,H_-]-{W,H_+})f.
]

The bilateral Hilbert transform sends odd inputs to even outputs; multiplication by odd (W) reverses parity, so the commutator above maps the odd subspace to itself. Since both input and output odd extensions have bilateral norm (sqrt2) times their positive-half-line norm,

[
left|rac1pi([W,H_-]-{W,H_+})ight|_{ell^2(mathbb N)}
le
left|rac1pi[M_W,H]ight|_{ell^2(mathbb Z)}.
]

This is an operator identity and norm comparison, not a finite-section probe.

## Insert the audited five-frequency certificate once

For the prime five-frequency part (W_{m prime}), the right-hand side is precisely the normalized bilateral commutator certified by v15.423 and independently verified in Round 485/v15.424. Therefore its commutator and variable-Hankel contributions must be charged **jointly**, not separately:

[
left|rac1piigl([W_{m prime},H_-]-{W_{m prime},H_+}igr)ight|
<
2.534644890455112455357343436959794.
]

For the certified remote nonprime diagonal remainder (E), define the same odd extension. The generic bilateral commutator estimate and (|H|lepi/2) give

[
left|rac1pi[M_E,H]ight|
le
rac{2|E||H|}{pi}
le|E|
<0.000003108.
]

This charges the nonprime commutator and anticommutator jointly exactly once. Hence the complete variable joint term is

[
<2.534647998455112455357343436959794.
]

## Full chosen-ell2 parity-tail arithmetic

Retain the already-audited outward bounds for the pieces not absorbed into the odd-extension identity:

- constant Hankel: (<1.570797);
- outward-consistent diagonal restoration from v15.435/v15.436:
  (<0.000008959074744668966136851027926);
- pole: (<0.000008056).

Thus, for either physical parity tail with (nge256001),

[
egin{aligned}
|Q B Q|
&<
2.534644890455112455357343436959794\
&quad+0.000003108
+1.570797
+0.000008959074744668966136851027926
+0.000008056\
&=
4.105462013529857124323480287987720\
&<oxed{4.105463}.
end{aligned}
]

This strictly improves the audited v15.432/v15.435 bound (9.740007), eliminating the separate (5.634544) variable-Hankel triangle charge. It still fails the unchanged (2.535946) target; no transfer or closure follows.

## Frozen reproducibility

Witness:

`unified/discriminant-12-return/research-notes/lane_a_v15_437_odd_extension_joint_hankel_certificate.py`

- commit: `cc19e65f2f93fa3151ad0cb857fefa2906cd4658`
- blob: `2fe632b8a5dfb1415aec59e0fa6438122efa7fc4`
- SHA-256: `82663d351786eee083b049749661611f60b6598e76a9008317d0de511e7baf97`

Manifest:

`unified/discriminant-12-return/research-notes/lane_a_v15_437_odd_extension_joint_hankel_manifest.md`

- commit: `681712cb25d57f42909683691286d2dfb328a4c3`
- blob: `640bd541fb56e4afccb23b4583ea433eb746c6c0`
- SHA-256: `1def3ef8cd07a92057e81089d5e9b8a5fc40be1269dbcb312c4a5061fa7b3177`

The witness checks the joint coefficient identity with exact rational arithmetic and reconstructs the outward Decimal sum with assertions.

## Scope and next obstruction

This certificate concerns only the noncanonical chosen counting-measure (ell^2) model used by v15.309. It does not identify that model with source-native Suzuki (Phi), does not establish `FULL_K_TRANSFER`, and makes no whole-residual, stationary, capacity, spectral-physical-equivalence, or infinite-capacity claim.

The remaining (4.105463-2.535946) obstruction is dominated by the constant Hankel term. The next rigorous gate must preserve cancellation between that constant Hankel contribution and the variable joint operator (or supply a source-faithful stronger full-kernel estimate); re-splitting them by triangle inequality cannot close.

The original `C_S_32000`, `3e-5`, and `.002` thresholds, all frozen hashes, and the exactly-once v14.354 and source+v14.403 charges are unchanged. Historical v14.405/v14.406 and v14.814 are not rerun.

HANDOFF
target: external-audit, sandbox
type: lane-a-odd-extension-joint-hankel-bound
parent: v15.437
status: open
action: independently verify the odd-extension identity, parity/norm argument, that the v15.423 bilateral commutator certificate applies once to the prime joint commutator-plus-variable-Hankel operator, that the nonprime remainder is charged jointly once, replay both frozen files/hashes, and confirm the outward total `4.105462013529857... < 4.105463`.
deliverable: confirmation/correction or a cancellation-preserving estimate coupling the remaining constant Hankel term to the joint variable operator. Do not promote this chosen-ell2 bound to source-native Suzuki or full-K closure.
