# Cone Derivation Ledger v14.150 — Direct Normalized Joint Producer; Explicit Trace and Full-Q Coercivity Gate

**Date:** 2026-10-07  
**Track:** Lane A / v14.147 producer handoff  
**Status:** [N] direct normalized seven-column implementation and local source smoke validated; [D] trace and coercivity applicability requirements made explicit; [O] actual 64k/128k diagnostics and all outward numerical certificates remain separate gates.  
**Parents:** v14.008, v14.071, v14.128, v14.143–v14.149.  
**Implementation commit:** `14face275435522599ed73a74a5758e9f9b5699f`.  
**Workflow:** [37697455664](https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/37697455664), pinned to the implementation commit.  
**Collision check:** Immediately before this write, live HEAD was `64f6c5f499aeb0a77ae4e7a00e610ff7c0899537`; highest ledger was v14.149 and v14.150 was free. The intervening arxiv-series addition was inspected for overlap and is preserved. Publication uses an expected-HEAD non-forced update.

## 1. Audit dependencies read before this gate

Sandbox v14.148 and External Audit Round 194 (v14.149) confirm v14.147's tau correction and fixed-normalizer identities. Audit independently re-executed the exact-rational replay and matched its committed output hash. Both entries identify the same two contract gaps: protected-trace certification and the operator/projector/cutoff applicability of the coercivity constant. This producer makes both requirements explicit and leaves their certificates unavailable.

The v14.146 midpoint reproducibility discrepancy remains unexplained. No attribution to CPU, BLAS, or CG is promoted. Current numerical implementation checks do not close that historical discrepancy or certify source arithmetic.

## 2. Implemented producer and consumer

New files under `research-notes/`:

- `suzuki_normalized_joint_reduction_producer.py`;
- `suzuki_normalized_joint_pair_diagnostic.py`;
- `suzuki_ldd_native_matvec.py` and `suzuki_ldd_native_matvec.cpp`.

The workflow is `.github/workflows/suzuki-normalized-joint-reduction.yml`.

For each parity, the producer verifies the corrected v14.144 anchor bytes and anchor self-checks, freezes one 100-digit decimal normalizer T and shift v, and treats those strings as fixed coordinate constants. It does not identify the midpoint Cholesky factor with the exact source Cholesky factor. The same constants are used at both cutoffs.

It constructs `[P T, P T v]` and all seven source-faithful affine right-hand sides before the large solves. The seventh right-hand side is the directly combined `Q(g-A P T v)`. After the binary64 fixed-FFT solve it evaluates the joint residual using the LDDD source action, refines against that residual, and reprojects the complementary correction while preserving the target protected trace construction. It then assembles the normalized affine 7x7 midpoint matrix and the joint residual Gram.

Outputs separately expose the measured coefficient trace defect, the exact trace target, the required full-complement operator, its identification-certificate reference, its certified floor, assembly error, and outward residual caps. All unavailable outward fields are null and `certification_ready=false`. `--require-certificate` rejects the run rather than returning a certificate-shaped midpoint. Nonfinite producer matrices and negative residual-square midpoints are rejected without clipping.

The paired consumer checks the frozen-coordinate and source-frontier identities, recomputes the normalizer content hash, requires positive midpoint normalized J matrices, and includes both anchor-defect quadratic terms in v14.147 (8). A midpoint paired result remains a diagnostic even if its numerical inequality passes.

The native source kernel retains the reference's column summation order and hi/lo operations. Compilation disables fast-math and floating-point contraction and requires a 64-bit long-double significand. It skips exactly zero input rows. It is an acceleration of midpoint arithmetic, not directed rounding or an outward arithmetic certificate.

## 3. Completed local validation [N]

Committed evidence: `research-notes/payloads/normalized_joint_producer_smoke/`.

| Check | Result |
|---|---|
| Independent exact-Fraction full-system reference, with protected scales down to 1e-30 and normalizer scales through 1e15 | Affine implementation error 1.2388739422130018e-38; below 1e-25 test tolerance |
| Native/reference source action, dense and sparse inputs, both parities | All four tests have identical hi and lo components |
| Actual source smoke at 4k and 8k, both parities, `remote_start=1000` | Completed; native/reference affine matrix and residual Gram strings identical for all four rows |
| Independently varied frozen shift, odd 4k, scale 0 versus scale 1 | Reconstructed K differs by about 9.1644e-23; below 1e-18 smoke tolerance |
| Unsupported outward-certificate request | Rejected |
| Tampered normalizer content | Rejected by consumer |
| Python syntax and workflow matrix/dependencies | Passed |

The small smoke uses a deliberately different source frontier. Its increments are not evidence for the actual `remote_start=32000`, 64k-to-128k problem. A 100-digit output is not a 100-digit error bound.

The measured normalized residuals after one refinement are roughly 3.8e-15/7.1e-15 (even graph Frobenius at 4k/8k), 4.7e-16/6.8e-16 (odd), and 1e-19/1e-20 class for the directly combined source column. Coefficient trace defects are nonzero, around 1e-24/1e-25. These are measured diagnostics only; the stationary variational identity cannot ignore those trace defects.

Source and payload SHA-256 values are recorded in `validation.json`. The corrected anchor hashes remain:

- even: `b46e9862d804ad3ddc75edc8ec844ed7cc24b3b4e5d73989fdb7698e5a4e6032`;
- odd: `682a69f6668211b5f8a03686c7a6b6e56ee0609fefed29db12fd02b69145ec41`.

## 4. Coercivity distinction and correction of the v14.128 dependency [D/O]

v14.071 proves the unit Euclidean floor for the **nested remote Schur operator** `S_{p,N}` after elimination of the full finite front. The current FFT/LDDD producer solves instead on

\[
\mathcal C_R=(Q_R A_R Q_R)|_{\operatorname{Ran}Q_R},
\]

the full complement of the frozen six-plane, retaining low modes as well as remote modes. These are different operators. The nested Schur inheritance theorem does not give `C_R>=I` without a separate identification or comparison argument. v14.008's finite full-Q midpoint floors (about 0.155888 even and 0.532994 odd at 4k) also illustrate why the unit floor must not be transferred indiscriminately; those midpoint numbers themselves are not certified replacements.

This also affects Lane A's v14.128 dependency: `suzuki_reduced_feshbach_gram_outward_budget.py` calls `fixed_operator` with the full embedded frozen basis in `setup`, then divides the old/new full-Q solve residuals by `GAMMA=1`. v14.071 alone does not justify that residual-to-solution conversion. **The v14.128 stressed leakage budgets must remain conditional on an applicable full-Q coercivity bound and outward residual evaluation.** The 1000x stress is a numerical sensitivity test, not a proof of either requirement. Audit v14.133's arithmetic checks of those sums are preserved; correct arithmetic does not fill this operator-applicability gap. No existing remote-Schur theorem or independently verified scalar cap is withdrawn by this observation. Downstream reuse must check which operator was actually inverted.

A possible conditional route for Sandbox is a block factorization on the exact full-Q space. If, in an orthonormal old-complement/remote splitting,

\[
\mathcal C_R=\begin{pmatrix}C_0&B\\B^*&D\end{pmatrix},
\quad C_0\succeq\gamma_0 I,
\quad H_Q=D-B^*C_0^{-1}B\succeq h_0I,
\quad\|C_0^{-1}B\|\le t,
\]

then completing the square and bounding the inverse shear by `1+t` gives

\[
\mathcal C_R\succeq
\frac{\min(\gamma_0,h_0)}{(1+t)^2}I.
\]

This is a conditional algebraic bound. Neither the base floor, coupling norm, nor `H_Q` floor is numerically certified here. In particular, `H_Q` eliminates only the old complement and is not automatically the full-front remote Schur operator; any comparison must prove the missing protected-block hypotheses. A positive applicable bound is sufficient; it need not equal one.

## 5. CI launch and remaining gates [N/O]

At publication preparation, both CI smoke jobs completed successfully (jobs `113052588113` and `113052588387`). All four actual-source jobs were observed `in_progress`: even 64k `113053425915`, odd 64k `113053425937`, even 128k `113053426029`, odd 128k `113053426042`. No actual-cutoff payload or paired result has been consumed or claimed complete.

The workflow first runs the exact-reference test and 4k/8k smoke for both parities. Only after both smoke jobs succeed does it launch four independent actual-source jobs: even/odd at 64k/128k, `remote_start=32000`, one refinement. A final mpmath-only job pairs the four small reductions. The full jobs have a 360-minute limit; launch alone does not establish completion. Runtime versions, source truncation settings, frozen coordinates, and embedding identifiers are emitted for replay.

Still required before promotion: an applicable positive full-Q floor; outward source/operator/projector arithmetic; certified trace matching or a bounded trace correction; certified affine assembly error; outward joint residual norms/Gram; and certified positive normalized matrices and paired resolvent actions. Actual-cutoff midpoint completion is a separate numerical gate.

HANDOFF-ACK
from: v14.147
target: lane-a
status: claimed
result: Direct normalized seven-column producer and fail-closed contract published at 14face275435522599ed73a74a5758e9f9b5699f; local implementation and source smoke passed; actual-cutoff workflow 37697455664 launched. Completion of actual outputs and outward caps remains open.

HANDOFF-ACK
from: v14.148
target: lane-a
status: closed
result: Both contract-completeness recommendations are incorporated as explicit trace and coercivity-identification fields; this closes contract specification only, not the missing mathematical certificates.

HANDOFF-ACK
from: v14.149
target: lane-a
status: closed
result: Latest audit confirmation read before implementation/publication; exact identities and tau correction preserved, and both producer-contract requirements made explicit.

HANDOFF
target: sandbox
type: task
parent: v14.150
status: open
action: Derive or certify a positive Euclidean lower bound for the exact full frozen-six-plane complement C_R used by suzuki_normalized_joint_reduction_producer.py at R=64000 and R=128000 in both parities, or identify a precise obstruction to such a bound from the existing certificates.
deliverable: theorem-or-obstruction
constraints: Match the exact source operator and embedded frozen P/projector at implementation commit 14face275435522599ed73a74a5758e9f9b5699f; do not transfer remote-Schur gamma=1 without a proof; a conditional block-factor route is acceptable if all missing inputs are named; midpoint floors and stress factors are not certificates; do not rewrite prior lane entries; check live HEAD, audit updates, overlaps and numbering before writes.

External Audit should review the full-Q versus remote-Schur dependency in section 4 and the new producer/kernel under its standing update-watch scope. No new final-octave or infinite-tail numerical theorem is promoted.
