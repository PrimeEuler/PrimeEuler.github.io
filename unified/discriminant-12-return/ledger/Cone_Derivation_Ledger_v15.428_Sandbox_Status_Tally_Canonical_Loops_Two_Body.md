# Cone Derivation Ledger v15.428 — Sandbox status return: side-thread program tally — canonical loop classification (steps 5–6) and the two-body bicone arc deposited; standing doors restated

Date: 2026-11-05 (America/New_York). Lane: sandbox (our Lane B), depositing the current state of the Cone-dynamics side thread at Jeremy's direction ("lets ledger where we are at with everything and continue working on these doors"). Parents: v15.388 (SM frame), v15.391 (evening sections + direction), v15.394 (loop program steps 1–4); live HEAD v15.427 at deposit. Status: mixed — the tally sections are by reference to audited deposits; §§2–3 are new deposits, [D] script-verified where marked, probe-grade [N] where marked. Disclosure deposit under the ledger-everything policy: listing is disclosure, not endorsement by the other lanes.

## 1. The tally, by reference

- **SM internal labels (v15.388; Audit R474 at v15.389 verified in full; erratum v15.390).** The SM's internal label system — color (p,q)/triality, weak slots, hypercharge fractions AND integers, antimatter, composite singlet rules — is reproduced in one frame from the cone's k=2 U(2) container plus the AM-GM family's k=3 member (2+1 split grading c mod 3, not shell triality), headline identity c = p − q exact on all fifteen fields (a consistency of completed assignments, not a derivation). Exactly three imports: anomaly cancellation (promissory note against a gauging that does not exist yet), κ=3 (candidate native source: the same k=3 list length), and the anchor Y_L = −1, which is the cone's own shell, not an import. Named negatives deposited with it: linear bicone hypercharge routes closed (gcd 2/3), the nonlinear door closed (charge lattices are representation theory), the parabola 2/3 (v14.592) the wrong type for a charge (fails additivity).
- **Evening sections (v15.391; confirmed by Audit R475 at v15.392).** Doubled SU(3) gluing = chiral flavor SU(3)_L×SU(3)_R → SU(3)_V, species-fenced (not color, not weak chirality, not generations); coupling anatomy (imported number × geometric matrix element) compressing the dynamics door to g₁, g₂, g₃ + Higgs/Yukawa with C_F=4/3, C_A=3, T_F=½, C_A/C_F=9/4 as pure (p,q) arithmetic; loop extent (architecture cone-native, weights imported, GIM completeness exact); the literature direction (DIRECTION.md).
- **Loop program steps 1–4 (v15.394).** Exponentiated-variable determinants with certified tails (det e^D = √(8π); the ζ(0)-mismatch ratio lesson, finite parts differing by exactly log 2); perturbed determinants and the Krein pair protocol on a MODEL perturbation class (raw drifts log log N, det₂ settles; protocol quotes only licensed determinants, per parity channel); insertion eigen-sums with the eigenvalue-insufficiency of amplitudes demonstrated by an isospectral twist; the GIM template over the generation direction.

## 2. New deposit: loop steps 5–6 — the canonical pair classified (probe-grade)

`canonical_krein.py`, `detp_density.py`; running notes in the deposited LOOPS.md. The protocol of steps 1–4 applied to finite sections of the frozen canonical kernel (dm490/far585/kfull DERIVATION.md §0: K_{N,m} = c(m z_N − N z_m)/(N²−m²) + 2σ p_N p_m, K_{N,N} = d_N + 2σ p_N²; B = the ledger's hollow off-diagonal part, D = diag(K)), per sector, head and remote regimes. Float stack copied verbatim from this ledger's own v15.310 scoping payload — probe-grade [N] standing (scales, not certified values); finite sections only; NO full-K transfer claim (FULL_K_TRANSFER stands INCONCLUSIVE; the Schur route of v15.310 is the certificate path).

- **Validation [D].** d_float matches the certified diagonal evaluator (`suzuki_certified_remote_diagonal.evaluate`, regime n > 256000) to 1.2e-6 (odd) / 1.4e-6 (even) on 24 sampled remote modes per sector; census max |d_float − log(n/4)| = 1.7431 / 1.7452 against the certified bound 1.74586; section ‖B‖ = 1.71–1.86, the v15.310 window estimates' scale.
- **The canonical pair fails the determinant gate in the strongest form [D, probe].** ‖B R_D(z)‖²_HS grows with section size in both regimes (≈ S/log²S at the head: 2.63 → 4.42 → 7.43; ≈ linear in S remotely: 5.11 → 10.31 → 20.66, S = 200 → 800) — the kernel's O(1) z-oscillations give every column non-decaying HS content. Step 6: per-mode Schatten ratios stabilize at positive constants (‖X‖₂²/S = 0.0258, ‖X‖₃³/S = 0.0064, ‖X‖₄⁴/S = 0.0017 remotely) and the singular-value quantiles are S-independent to three decimals (median s ≈ 0.10, 99th percentile ≈ 0.36): X = B R_D has a limiting singular-value distribution, so Σⱼ sⱼ^p ≈ c_p·S diverges for EVERY finite p — **no det_p exists for the canonical pair at any order.** The determinant level for this pair is a density.
- **The density, renormalized [D, probe].** (1/S) log det_p per mode, remote (z = 7): p=2: −0.01315 (odd) / −0.01309 (even); p=3: −0.00056 / −0.00054; p=4: −0.00044 / −0.00044. The p=2 bulk was almost exactly the trace term (Tr X²/S = +0.0252; −½ of it accounts for −0.0126 of the −0.0131), and Tr X³/S ≈ −0.0003 ≈ 0 (the per-mode eigenvalue distribution of X is nearly odd-symmetric). After the X² subtraction, the residual determinant content is ≈ −4.4×10⁻⁴ per mode, S-stable from S=200 and sector-independent at probe precision.
- **What survives is the ledger's native level [D].** Birman–Krein verifies on every canonical section checked (S=400, both sectors/regimes, by independent interval integration); ξ is a genuine counting difference (max|ξ| = 38 head / 66, 61 remote; small mid-range); Weyl displacement from the sorted diagonal ≤ 0.72 against ‖B‖ ≈ 1.8. Insertions are finite: the kernel's own pole vertex 2σ⟨p, R p⟩ at head S=800 gives +1.1591 (K) vs +1.2362 (D) odd, −0.1167 vs −0.1080 even; remotely it is ~1e-9 (p ∈ ℓ² lives at the lattice head).

## 3. New deposit: the two-body bicone arc (2026-11-02, sandbox exploration)

The interaction probe that followed the v15.270–v15.282 dynamics chain (whose seam #2 was "all single-particle"). Scope, stated in every report: **all force laws are imported classical physics; nothing here is claimed cone-derived.** The cone supplies the arena and the questions (bicone dipoles, drive × reaction split); the dynamics is Liénard–Wiechert/Newtonian as labeled. Stage verdicts [D]:

- **Newtonian bicone dipoles.** Control (dipole off) deviation exactly 0.0000°; dipole on: RMS deviation 10.3°, extremes −30°/+22°, separation breathing 2.00 → 3.49, rosette precession, no tidal locking; conservation ~1e-11.
- **Relativistic.** Dipole bends the force (RMS 12.9°, max 30.3°); relativity alone bends coordinate acceleration away from force (RMS 1.16°, max 1.70°) — the two effects are distinct species. Seams: not covariant, instantaneous potential, no Thomas precession.
- **Retarded EM point charges.** Full Liénard–Wiechert inspirals with no damping inserted (10 → 9.27 → 7.25 → 5.71, plunge stopped at r=3.18, t=166); the velocity-fields-only truncation is inconsistent (gains energy, drifts to r=14.1); Larmor audit ratio 1.24–1.33 quasi-circular.
- **Retarded bicone dipoles.** Finite-size retarded drag: deviation −6.9° at t=0 growing to +21°, tangential brake ~36% of force, plunge at t=58 vs the point baseline 166; the effect collapses at S=0.2 (deviation ≤ 4.5°) — a size effect. Negatives: a delay-pumped spin-up regime (QD=3, I=0.5 ran away); full retarded intra-body interaction ran away in <10 time units; constituent Larmor sums overcount composite radiation.
- **Split-channel intra-body.** The symmetric intra-body channel is exactly silent for a rigid dipole (net force and torque 0.00e+00) — rigid internal dynamics is entirely antisymmetric-channel, matching the drive × reaction split (v15.275). Dirac reaction torque τ_rr = (2/3c³)(p × p⃛)_z; ALD runaway fixed by reduction of order; plunges 56.5 (R1) and 24 (R2).
- **Spring-arm dipoles.** The symmetric channel sets the size: spring vs intra-Coulomb balance at S_EQ = 0.867; the arm is quiet/adiabatic (modulation ≤ 0.003); plunge delayed to t=60.5; no resonance crossing (ω_s ≈ 6.3 stayed ≥ 4.5× the drive frequencies).
- **Drag scaling scan.** At separation 10: deviation RMS ≈ 9.57·S^1.17; plunge time ≈ 56.7·S^{−0.49}; inspiral slope ≈ 0.112·S^0.75 (monotone on 0.2 ≤ S ≤ 2). Caveats deposited with it: the scan log has 10 SCANJSON lines, not 11 (sep=10, S=1 duplicates scan A); circular runs cannot separate the velocity law from the separation/delay law (excess fits sep^{−1.27} ≡ v^{+2.53}; separation would need a non-circular run — undecided); the sep=20, S=0.05 reference had not plunged at stop and its slope ratio is inflated — the excess-RMS column is the robust readout.

## 4. Standing doors, restated as the work queue

Unchanged in kind through all of the above: (1) the **chiral correlation** — identifying the frame's N_A=1 sector with the bicone's (½,0) Spin(4) factor; located exactly (open_more_doors §B at v15.388), not opened; every equation in the frame thread is invariant under the global L↔R flip. (2) **Generation count and mixing** — the frame supplies the c → c+3 direction, unbounded, generation-blind in every output; no count, no CKM/PMNS, no masses; all loop weights imported. (3) **Coupling values** — compressed to g₁, g₂, g₃ + Higgs/Yukawa (v15.391 §2); Ŷ exists as values per field, not as a frame operator. Canonical side: FULL_K_TRANSFER remains INCONCLUSIVE (Schur route is the path); certified versions of §2's steps 5–6 would ride on that machinery and are untouched; confinement as a mechanism untouched (the label level only, v15.388).

## Payloads and snapshot notes

Payload A: `unified/discriminant-12-return/payloads/weak_force_loops_canonical_v15_428/` — LOOPS.md (running notes, steps 1–6 with status), canonical_krein.py, detp_density.py, with `MANIFEST.sha256` (sha256 d2377b2fbc1def62ca285e42f3b8a2344e5b58f19058d5751faa8498b754b8d4). Both scripts re-executed from the staged copies on 2026-11-05 (exit 0). SHA-256 (generated mechanically from the manifest):

- LOOPS.md `4d09fe6804d32a20cf10dff740c881151570c30d9a1aa4a5a834879b1c2c5b6a`
- canonical_krein.py `2b09e128a6b6da1874600853dbf634cfbd2257b14a9edee5a655fe49545cad96`
- detp_density.py `e900eddabc7f0341fe2bd358ffe382368f8e232358c6b24049e02ba5fd7b6929`

Snapshot note: LOOPS.md supersedes the v15.394 snapshot (it contains steps 1–4 as deposited there, plus steps 5–6 and the revised status).

Payload B: `unified/discriminant-12-return/payloads/two_body_bicone_v15_428/` — 8 reports/analyses, 7 scripts, run_scan.sh, scan_log.txt, and the 19 .npz run-data files, with `MANIFEST.sha256` (sha256 fbca3faa9b807921f4837c07020a426d1648cd4bae5800d3ae1e748c73ca3985; the manifest covers all 36 files including the .npz data). SHA-256 for the text files (generated mechanically from the manifest):

- REPORT.md `f09ee278d2d0e8ac4b92364e2fd2679792f8e030ece38b43e6309024f7a3a4ae`
- REPORT_REL.md `1006824dfcfd7169f4ed410b217e89b8619ddd9887349eb635736c4b3b8fb49e`
- REPORT_RET.md `405e448119efb68c844abe9bdf3d60c223bbfc5adb155981e8a8b9db35b0f64d`
- REPORT_RETDIP.md `a634c950b99c1544f680f3193c1f39e5d7788fcb5d9d8bf6e123c615ea38b92b`
- REPORT_RR.md `abbc81bbe8456ff581194c8a2b4a9440c5d1c342fb0ac957f939c9636faefafc`
- REPORT_SCAN.md `92a7cde01ca1f0a1610c4d3d4cd422a72c01759b574e497ab27db6a330a54d60`
- REPORT_SPRING.md `05b60e583c0090331bf56ef9b67d85a323a46ab2e8a7fcce740d9bba8950d611`
- SCAN_ANALYSIS_2026-11-02.md `b6e531af03353279cb84739e5854b8ab40511cd4c2bb026767ee97a535f6f112`
- scan_log.txt `fb6737248f60edddb301a5a80a35e63cb67cdc1e38ca81d856b348e1514c2624`
- two_body_bicone.py `a7345325d2d7d298d7c38ad1b4db69900db8b3861fcc5d5329861585c76c9aeb`
- two_body_bicone_rel.py `a33f68e0672097c5f46ca160e1097bfe08dd888875c126c4cccc0b44a510060a`
- two_body_drag_scan.py `1b72ebe37e0d99939aa019dde0960c78aab1d52f485e504614b02e9a5ba4d9b5`
- two_body_retarded.py `204d6e5b74c1c354b2a5b8ae34894848558ea07a1766cb8d1a9b374568cd383a`
- two_body_retarded_dipole.py `c3a57c789e9ef01e2b8e8fa0e8c26db10f9218acedd341b55b4b287f2aaaa575`
- two_body_retarded_dipole_rr.py `8bc6a71f8d8fba826c87c86385df7cb686de95c7a9bd799bf2031b1a3192d8ed`
- two_body_spring_dipole.py `e5da1f73a0389ed679f1b5ce43bca0305ba1a5d508b5827a81b508373187b1ed`

Exclusion, stated: the arc's 20 PNG figures (~3.9 MB) are NOT deposited; they are regenerable from the deposited scripts, and the .npz run data they plot IS deposited.
