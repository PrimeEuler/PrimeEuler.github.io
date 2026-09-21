# Cone Derivation Ledger v13.642 — M16001 Six-Plane Orthonormalization Executed Certificate Freeze

Date: 2026-09-21

Status: executed CI certificate freeze; this closes the v13.619/v13.628/v13.635 six-plane normalization gate only. No downstream M16001 theorem is promoted here.

## 0. Live collision/relevance check

The live ledger was checked immediately before this write. v13.641 is the latest numbered entry and belongs to the chi_-4/Friedrichs thread, so v13.642 is free. The controlling audit checkpoint is v13.635, whose M16001 instruction was to repair the hard-coded n=4 Cholesky/inverse path, rerun, and report the actual outcome before building anything on the six-plane result.

External Audit Round 66 (v13.628) correctly found that the original six-plane checker could not execute on its 6x6 Gram matrix. The repair was carried onto a fresh branch from current master, and the CI pipe was also made fail-closed with `set -o pipefail` so a Python exception cannot be hidden by `tee`.

## 1. Executed CI identity

Current-master PR head:

```
0517fb84e297ec33b0d7a1cfeefe36c824ebb114
```

GitHub Actions:

```
workflow: M16001 Frobenius audit
run:      35665154337
job:      106549126938
run no.:  22
platform: ubuntu-latest / Python 3.12
result:   success
```

The six-plane step itself completed successfully and its nonempty transcript ends with

```
ORTHONORMAL SIX-PLANE CERTIFICATE: PASS
```

Artifact `m16001-frobenius-output` has GitHub artifact digest

```
sha256:0735b477e90d038e043066253c6f80c61425a183e43e4f13780266a7661e2304
```

## 2. Executed gates

All six required gates printed PASS:

```
exact G_P=P^T P SPD             PASS
R_P^T R_P contains exact G_P    PASS
R_P R_P^{-1} contains I6        PASS
P_perp^T P_perp contains I6     PASS
P_perp^T N_perp contains 0       PASS
B_perp^T B_perp contains I10     PASS
```

Thus the repaired interval construction has actually executed to completion; this is no longer a specification-only checkpoint.

## 3. Exact Gram identity and LDL pivots

```
G_P exact SHA-256 =
e22c303a0f0bea6856153777188e5b5de93e54c3eb5d22d1c77107e5f570ae8a
```

The six exact positive LDL pivots printed by the executed checker are:

1. `9452287970026066457700190046240362496 / 364636135865909913300630815841`
2. `156857871517967279245189690564291132995861183383742402213991276375891 / 33913392257617473734815943789130841433489840477237258543970699375`
3. `573374653997517864982764062482465824220779328709810644486397868867580469315062994308895692791568774417537 / 442216977379499397192066695842303678844915608008811306412862191900476872328542632270374928498147904000000`
4. `9526820527087387127942429281895807699960862697534048215851920826649442012712332973863636592240091659207005983124604986172819363270693336333 / 16214399585684940232629516832303846381407528231807891383416120838274806733674469016012016605419448156656047922675910319959580003083821056000`
5. `63316582777114829142776095708629989111084189645478213603931701714956934484326635775624119488672031118531806254085014636563384966117423436100909334399930366201480789503628632573 / 127602723756734959666981601354697191189738472987249877856372727077447886662923642198352861010727185709593981723313503537823193027384253324414916249863242405687602793846529064960`
6. `438344658462365455467882733730792214867228908649074406200197494705772871697124187310265951133284465711883698221302007512146374900144560045331134395144724326699524126358028125190344093655624718263750217901205587 / 1029024480246460554539386949617240517267979057697668385226070920557029477346764885466605580853445810600301481654308557237597836726123243212922769527064719491190036102710641115114600113243782935504114477772774400`

## 4. Frozen interval payload identities

```
M16001_P_Gram_exact_interval.interval
sha256 ef130c3c2def0e1c5e58d8dda460de0d17ef6245acb189fef5290c059d0011fe

M16001_P_Cholesky_R.interval
sha256 c735dc82861d3fbd265540e4057aa98f38a348925331679947863407051112e0

M16001_P_Cholesky_Rinv.interval
sha256 fb180a12b89d2438796ed403d6aa840c1a4999f733181633bd8d8321b8f039ac

M16001_P_perp.interval
sha256 47d8e410807d2f051fd2d6d9a903c4aed2430ab06223ca0ff6f8550c1ffb3286

M16001_B_perp.interval
sha256 630ed6bd2095a0cdf570e12e3092b710fdd337ba31bd6b0ffa813edbfd363b01
```

Certificate JSON byte identity:

```
M16001_orthonormal_sixplane_certificate.json
sha256 f2ba93e800a0bab5cd9d50eb75875cd23e8e44c4068caafad839a2915d2005fe
```

## 5. Maximum interval widths

```
R_P      3e-116
R_P_inv  2.4e-119
P_perp   2.0e-119
B_perp   2.29921673843335e-101
```

The wider B_perp width is inherited from the independently reconstructed four-dimensional N_perp interval block; it is not evidence of failure of the six-plane normalization.

## 6. Consequence and next gate

The v13.635 M16001 recommendation has now been acted on and the actual outcome is PASS. The orthonormal basis

[
B_\perp=[P_\perp,N_\perp]
]

is therefore the frozen basis for the next replay.

The next gate is deliberately narrower than the old integrated raw-P replay: reconstruct and freeze, from the certified B_perp intervals and the frozen X payload,

[
B_\perp \longrightarrow X B_\perp \longrightarrow
W_\perp=\begin{bmatrix}B_\perp\\-XB_\perp\end{bmatrix}.
]

That replay must hash-match the B_perp payload above and the frozen X binary64 payload, propagate midpoint/radius arithmetic outward, and freeze its own payloads/transcript before any finite QQ/QN/NN projections, p/a_q/b_q values, remote-row reductions, or final Schur penalty are recomputed.

No value from the earlier raw-P/SVD downstream calculation is promoted or silently reused by this entry. No index<=3, exact-zero, RH, or GRH claim is made.
