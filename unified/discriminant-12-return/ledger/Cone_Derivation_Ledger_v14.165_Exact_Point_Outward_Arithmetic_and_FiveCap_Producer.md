# Cone Derivation Ledger v14.165 — Exact Point Arithmetic and the Five Remaining Cap Producer

**Date:** 2026-10-08
**Track:** Lane A / five-cap numerical implementation and audit handoff
**Status:** [D] source-to-point operator and assembly/residual enclosure bridge; [V-synthetic] exact convolution, dense source-action and nonorthogonal projector checks; [N-smoke] all five ceilings and trace ceiling met at 4k/8k in both parities, independently replayed byte-identically. Actual 64k/128k closure remains pending the new CI run and independent review.
**Parents:** v14.059, v14.115, v14.120, v14.123, v14.133, v14.155–v14.164.
**Collision check:** Live HEAD and latest Sandbox/External Audit checked before this gate and immediately before publication; the parent HEAD was `e5882f10cca8aa42bb61d3ab3dc9a0612ed55848`, ledger max v14.164, and the v14.165 ledger/script/payload namespaces were free. No prior lane result or frozen namespace is replaced. Branch publication uses an expected-HEAD lease without force.

## 1. The audit updates are incorporated

v14.163 and External Audit Round 198 (v14.164) independently reproduced the four actual trace witnesses from v14.162 byte-identically. Only the trace ceiling was closed by that freeze. The new implementation addresses the five remaining assembly and exact projected residual ceilings with complete vector snapshots. The source frontier in the actual jobs remains 32000; the smoke frontier is explicitly 1000.

The optional `--kernel exact` path uses the same audited arch-200/correction-50, mp-dps-180 scalar producer and the same frozen represented six-plane P. Its seven represented trial vectors are refined using an independently computed integer point action rounded back into high/low components. The final certificate uses exact integers/Fractions, including every vector row. No measured floating residual is imported as a cap.

The new path exports a **new** serialized matrix: exact point affine assembly rounded downward on an absolute decimal grid of 1e-100. Its former LDDD assembly is retained as `M_lddd_assembly_diagnostic`. The v14.153 and v14.162 frozen runs are untouched. The v14.157 perturbation lemma is reused with the new serialized matrix and a newly recomputed paired scalar; its old numerical baseline is not silently transferred.

## 2. Exact signed convolution and a symmetric point source

For signed integer coefficient families a,b, let C_a=2^max_bit_length(|a_i|), and likewise C_b. Pack a_i+C_a and b_j+C_b into base B coefficient blocks. Choose B=2^(8w), with 8w at least

    bit_length(max|a|)+bit_length(max|b|)+2+bit_length(min(len(a),len(b)))+1.

Every nonnegative convolution coefficient is strictly below B, so multiplying the packed integers creates no inter-block carry. Decode coefficient k and subtract

    C_b sum(a_i) + C_a sum(b_j) + C_a C_b number_of_terms

on the valid k-th diagonal. This recovers the signed convolution exactly. GMP only multiplies two integers; Python performs the scales, carry bound, packing, decoding, and sign corrections. The guarded 64-bit GMP 6.x import/export ABI follows the primary documentation at https://gmplib.org/manual/Integer-Import-and-Export and https://gmplib.org/manual/Integer-Internals. Unsupported ABIs fail closed.

Write n_i=2i+a, where a=1 for even-v and a=2 for odd-v. With k=256, use signed floor dyadic approximations of T_ij=1/[2(i-j)] off the diagonal, T_ii=0, and H_ij=1/[2(i+j+a)]. Retain the represented dyadic scalar families z,d,p,c exactly. Define the point source A0 by

    A0_ij=(c0/2)[(z0_i-z0_j)T0_ij-(z0_i+z0_j)H0_ij]+alpha p0_i p0_j   (i!=j),
    A0_ii=d0_i+alpha p0_i^2,
    alpha=+2 even-v, -2 odd-v.

This matrix is symmetric exactly. Four exact polynomial convolutions compute each action column; the Hankel diagonal is explicitly removed. No rounded FFT computes the certified point action. Twelve signed-convolution cases agree with independent schoolbook multiplication; both parity actions agree with independent dense Fraction multiplication, and their kernel entries satisfy the rational-kernel error bound. A separate dense nonorthogonal P check verifies the exact projector norm identity below. The existing producer's full-system Fraction reference, four native-component checks, and exact trace tests also pass.

## 3. Physical-source uncertainty, including decimal reconstruction slack

The audited scalar caps apply to the decimal reconstruction performed by `ld_string` (scientific precision 40, hence 41 significant digits), whereas the point operator uses the exact binary high+low sum. The full snapshot retains both original high/low scalar components. Replay verifies their component ranges and exact sum. For |high|,|low|<100 (z,d), conversion slack per component is at most 5e-40; for pole components <2 it is at most 5e-41; for c components <1 it is at most 5e-42. Conservatively widened common-parity caps therefore are:

| Family | Audited decimal cap, at most | Additional reconstruction slack | Point-source cap |
|---|---:|---:|---:|
| z | 5.88e-39 | 1e-39 | 1e-38 |
| d | 4.318e-37 | 1e-39 | 4.4e-37 |
| pole | 7.365230177656668e-40 | 1e-40 | 1e-39 |
| c | 6.740593794183538e-42 | 1e-41 | 2e-41 |

The source/cutoff applicability is the uniform arch-200 scalar transport audited through 128k in v14.115/v14.120 and through 256k in v14.123/v14.133. The wider even diagonal and pole caps safely contain the odd ones. This bridge is a new audit target, rather than an assertion that earlier audits already reviewed this implementation. The script refuses cutoffs beyond 256k.

For N modes, H_(N-1)<=1+ceil(log2 N). The off-diagonal scalar source formula gives entry error at most (epsilon_z+11 epsilon_c)/|n_i-n_j|, using |z|<=10 and |c0|<1. Symmetric row sums thus give that coefficient times H_(N-1). The pole charge uses the existing global ||p||<2 bound and ||p-p0||<=sqrt(N) epsilon_p. Hence

    delta_scalar = epsilon_d+(epsilon_z+11 epsilon_c)[1+ceil(log2 N)]
                   +8 sqrt_up(N) epsilon_p+2N epsilon_p^2.

Each rational Toeplitz/Hankel kernel error is <2^-256. Since |z0|<11 and |c0|<1, each point-kernel off-diagonal error is at most 22*2^-256. Thus

    ||A-A0|| <= delta_A = delta_scalar+22N*2^-256.

All square-root upper bounds use integer isqrt ceilings and verify their squared inequality exactly. Let g0 be the 256-bit dyadic floor of the exact source (zero through the fixed frontier, then 1/n or 1/(n-1)). The source charge is delta_g=N*2^-256, a conservative l2 bound.

## 4. Exact projection and the five outward caps

For frozen represented P and V=[W,u], form G=P*P and G^-1 with Fractions. Each point raw residual is y_j=A0 V_j, subtracting g0 only in column seven. Its exact projected squared norm is

    ||Q y_j||^2 = ||y_j||^2-(P*y_j)*G^-1(P*y_j).

The large dots use scaled integers; only the small inverse uses Fractions. This computes the exact Euclidean projector, including the represented P Gram, rather than a floating projector approximation. Let W2=||W||_F^2 and U2=||u||^2; let w,u be certified square-root uppers; let f0 and s0 bound the exact point projected graph/source residuals. With r=1e-100 for serialization, the five certified quantities are

    alpha_J    = delta_A W2+6r,
    alpha_beta = delta_A w u+delta_g w+6r,
    alpha_eta  = delta_A U2+2 delta_g u+r,
    f          = f0+delta_A w,
    s          = s0+delta_A u+delta_g.

These respectively bound graph operator norm, mixed Euclidean norm, scalar absolute error, graph projected Frobenius residual, and source projected l2 residual. Every threshold comparison is rational. Trace coefficients are independently recomputed from the full vectors and required to agree exactly with the standalone trace witness. The frozen P byte hash is required to match v14.155's audited plane.

## 5. Completed final-code smoke and reproducibility

| Parity / cutoff | alpha_J | alpha_beta | alpha_eta | f | s |
|---|---:|---:|---:|---:|---:|
| even / 4000 | 1.625e-7 | 4.747e-12 | 1.387e-16 | 3.827e-15 | 1.106e-19 |
| even / 8000 | 1.905e-7 | 5.564e-12 | 1.626e-16 | 7.106e-15 | 2.063e-19 |
| odd / 4000 | 6.454e-11 | 1.872e-15 | 5.430e-20 | 4.668e-16 | 1.353e-20 |
| odd / 8000 | 7.564e-11 | 2.194e-15 | 6.364e-20 | 6.785e-16 | 1.966e-20 |

These table entries are upward-rounded displays. All five exact caps and rho<=1e-20 pass at each smoke row. The even source's last mode is R-1; its certificate correctly names nominal cutoff R=2N. Actual 64k/128k success is not inferred from this smoke.

Frozen smoke namespace: `research-notes/payloads/exact_outward_smoke_v14_165/`. Every full ZIP retains all source high/low components and vector rows, dyadic scales, represented P, normalizer, mode list, and content hashes. Base64 parts are contiguous pieces with no inserted whitespace. The replay wrapper validates file hashes, reconstructs ZIPs, reruns integer actions and Fraction certificates from scratch, compares certificate bytes, and checks their binding to the original small payload. All four final-code certificates replay byte-identically.

    python suzuki_frozen_outward_witness_replay.py --payload-root payloads/exact_outward_smoke_v14_165 --output /tmp/outward_replay.json --compare-reference

The updated workflow runs both smoke parities, four actual 64k/128k jobs, separate trace and full-vector replays, and paired composition. Any failed numerical ceiling fails CI. The exact finite-pair consumer uses v14.156's trace charge and residual transport, the independently audited full-Q floors from v14.155/v14.158/v14.161, and v14.157's blockwise perturbation lemma. It recomputes exact endpoint capacities and the entire paired interval. It requires the 9e-10 budget in the actual paired job. Remote-Schur gamma=1 is never substituted.

`overall_certificate_ready` remains false pending independent audit of this new arithmetic bridge and actual-cutoff evidence. No infinite-tail conclusion or final Cone theorem is promoted.

HANDOFF-ACK
from: v14.164
target: lane-a
status: closed
result: Read the independent actual trace confirmation and retained its scope; the five remaining ceilings now have an exact-point/full-snapshot producer with four complete, byte-identically replayed smoke witnesses and an actual-cutoff CI gate.

HANDOFF
target: sandbox
type: audit
parent: v14.165
status: open
action: Independently verify the widened arch-200 scalar applicability and decimal-to-dyadic slack, carry-free convolution, symmetric point-source kernel charge, exact projector/assembly cap formulas, and frozen smoke replay; report any omitted charge before the actual endpoint caps are promoted.
deliverable: theorem-or-obstruction
constraints: The 4k/8k smoke has frontier 1000 and does not close the actual 64k/128k targets; new point-assembled matrices have a freshly computed paired baseline; preserve both prior frozen namespaces; full-Q floors are the audited small floors; no infinite-tail claim; check live HEAD and audits before each gate or write.

External Audit is invited to review this implementation and the forthcoming actual-cutoff freeze under the standing update-watch scope.
