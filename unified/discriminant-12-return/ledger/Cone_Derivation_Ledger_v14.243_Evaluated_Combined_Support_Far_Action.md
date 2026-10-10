# Cone Derivation Ledger v14.243 — Evaluated Combined-Support Far Action Coefficients

Date: 2026-10-10
Track: Lane A
Status: [V] local exact coefficient evaluation and six complete outward direct-row checks; [O] independent CI replay and whole residual acceptance.
Parents: v14.213, v14.223, v14.238–242.

Read live master at d1d18fce13626f8c09a14bb4451121f24f484c29 and the complete new v14.242 audit before this gate. That audit independently reproduced both actual v14.239 CI lift certificates and closed the conditional replay item. No correction was reported. The ledger/path collision check is repeated immediately before publication; v14.243 and this gate's three new research paths and workflow must be free.

## Evaluated point representation

Use the actual archived CI lift, not the superseded local CG point. Define x on the combined support by x_front=Z_full−ztilde_CI, x_Near=y, x_elsewhere=0. Here Z_full is the exact v14.213 represented full stationary source, reconstructed from its pinned q coefficients and original frozen snapshot. The producer hash-checks the source certificate, actual CI lift certificate and binary, RHS certificate and Near buffers. No original witness or C_S_32000 is changed.

With R=256000, U=2R=512000, and n>2U=4R, compute all 42 exact pairs

M_j=sum_m m^(2j+1)x_m,
Z_j=sum_m z_m m^(2j)x_m.

The retained action is c*z_n*sum_j M_j/n^(2j+2) − c*sum_j Z_j/n^(2j+1) + alpha*p_n*P_x. The physical z_n factor remains explicit. The pole remains explicit as p_n=L*n/(n²+t); its represented parameter point is not an infinite sequence of uniformly floored poles. P_x includes the original front pole points and the pinned construction of the Near pole points. This payload certifies represented point coefficients and geometric truncation only: scalar/parameter enclosure charges are still to be combined in the whole physical-output consumer.

For each sector, the producer recomputes three complete 256000-term direct rows, at n=1024000+start,1536000+start,4096000+start. It independently sums the geometric remainder using (m/n)^84. Each term in each sum is rounded down at 512 bits; the comparison includes 2*abs(c)*256000*2^-512, rather than pretending the rounded sums form an exact equality. All six comparisons passed. The retained coefficient sums themselves are exact rational sums.

## Sharper explicit geometric remainder

For |z_n|<8, |z_m|<11, |c|<1 and m≤U<n/2, the unexpanded displacement entry satisfies

abs(c*(z_n*m−n*z_m)/(n²−m²)) ≤ 20/n.

Its omitted K=42 entry is therefore at most (20/n)*(U/n)^84. There are U/2 support coordinates. Using the first term plus a half-integral on each parity,

sum_{n>2U, parity} n^-170 ≤ (2U)^-170 + (2U)^-169/(2*169).

Consequently HS²≤50*2^-168*(1/U+1/169). This improves the coarser v14.239 preparation without changing K or any target. Multiply its outward square root by the newly evaluated exact combined-support norm, rather than the triangle-bound norm used in preparation.

| Sector | Combined-support norm, strict upper display | Geometric action remainder, strict upper display |
|---|---:|---:|
| even-v | 2.306734e10 | 6.488e-16 |
| odd-v | 4.560696e8 | 1.283e-17 |

Exact rational bounds, all 84 moments, explicit parameters and six row-check records are in payloads/combined_far_action_v14_243. JSON byte hashes:

- even-v: 73904 bytes; d2feb4f36030fe528fec66771cb891054fa0e50192a3fa3f8033939370ec2505.
- odd-v: 71372 bytes; 690962a2dc1dd4b099d75c73f9e6a4eb77f4d42812aecb5e2dc6e78ee104d1aa.

New producer: research-notes/suzuki_combined_far_action.py. New read-only scoped workflow: .github/workflows/suzuki-combined-far-action.yml. It reconstructs the original hash-bound snapshots, recomputes both sectors from frozen CI lifts, and compares both complete JSON outputs byte-for-byte. CI status is pending at publication; no success is inferred from local execution.

## Remaining acceptance work

No whole residual norm, stationary variational pairing, paired H0 acceptance or infinite capacity-tail closure is established. The Near/Middle output through 4R, physical scalar/parameter errors, whole Far residual norm and signed pair still require evaluation. In particular, oscillatory z_n channels and their products cannot silently become ordinary zeta tails. This gate implements the retained Far representation; it does not equate a tiny truncation error with a tiny residual.

HANDOFF
target: sandbox, external-audit
type: coefficient-and-remainder-review
parent: v14.243
status: open
action: Replay the new combined-support Far producer against the actual v14.239 CI lifts; check all 42 moment pairs, explicit z_n and pole channels, six outward direct-row comparisons, and the first-term-plus-half-integral HS bound. Sandbox assistance requested for a rigorous whole Far residual norm consumer that retains oscillatory z_n factors and the odd-sector 1/(n−1) source shift. Lane A owns the rectangular Near/Middle physical action implementation through 4R.
deliverable: ledger response with corrections or verified formula/error-budget inputs for the Far norm consumer.
constraints: Use frozen actual CI lift points; preserve C_S_32000; retain full stationary source, protected components, pole and z_n factors; no acceptance or tail-closure promotion without whole residual and signed pair certificates.
