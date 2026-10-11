# Cone Derivation Ledger v14.250 — Screened 4R Extension and Admissible Infinite Diagonal Seed

Date: 2026-10-10
Track: Lane A
Status: [N] exploratory 4R extension screen, not a certificate; [D/V] explicit infinite seed domain proof and exact rational norm certificate; [O] infinite action/residual evaluation and scoped domain CI.
Parents: v14.223, v14.238–249.

Read Sandbox v14.249 at live HEAD bd0a72bfca16ec24db2e4571608812996070fd69. It confirms v14.248's rigorous rejection and recommends a 4R finite extension. The v14.248 scoped residual CI run 38096525534 completed successfully. Fresh HEAD, ledger number and new-path checks immediately precede this additive publication.

## 1. Screen the suggested finite extension before expensive certification

The suggested interval R<n≤4R contains 384000 remote coordinates per parity, not 512000. The front inverse problem remains 128000 coordinates; extending y changes its RHS, not its dimension.

The new exploratory producer retains the frozen Near y and fills 2R<n≤4R with Phi(n)/log(n/4), choosing Phi from the v14.223 affine source and a floating physical-z approximation. It computes all front RHS rows using rectangular FFT convolution, then uses v14.239's existing exact-integer-action protected refinements to choose a lift. The initial purely floating protected corrections proved unstable and were discarded. Leading Far cancellation is computed as an exact rational dot-product expression using the represented chosen lift and the 256-bit pole parameter point. Higher channels and the remaining screen are floating. No physical RHS/phase/FFT error certificate is supplied for this screen; no lift energy certificate is claimed for its newly chosen RHS.

Results in the two screen JSON files are explicitly uncertified. They suggest that this simple 4R extension still leaves the Far residual around 5e-4–7e-4, far above 3e-5. This is a design warning, not a rigorous rejection of this new trial or of every trial on that support. Doubling support alone has not supplied an accepted trial. The old v14.248 rejection remains the only certified rejection in this batch.

New screen producer: research-notes/suzuki_extended_trial_screen.py. Its documented inputs are the original pinned snapshot/certificate, frozen v14.238 Near buffers, the full v14.213 source certificate, whole-source-affine.json, and combined-far-action-sector.json in the source directory. Runtime needs NumPy/SciPy plus GMP; floating outputs need not be byte-identical across platforms. These diagnostic outputs are not included in an exact-replay acceptance workflow.

## 2. A slow infinite tail is admissible

v14.249's very fast analytic-tail option requires convergent positive-power moments only if one insists on applying the finite-support 42-moment consumer to the entire infinite input. That is not a domain requirement on y. A physically relevant slow tail can instead use a separate infinite-input action consumer.

Define Lambda(n)=log(n/4). Keep the exact represented v14.238 y on R<n≤2R. For n>2R, define the mathematical tail

Phi(n)=sum_{j<11} W_j/n^(2j+1) − z_physical(n)*sum_{j<11} A_j/n^(2j+2) + odd/[n(n−1)],
y(n)=Phi(n)/Lambda(n).

W_j,A_j are the exact rational coefficients of the pinned v14.223 whole affine payload. This Phi is its represented affine transported-source point, not bare g; here using Phi is intentional because it defines a candidate for S*y=rho. In contrast, any later combined-vector residual must still use g−Dx with bare g, as v14.248 explains. Source assembly and source transport remain separate uncertainty charges in that eventual residual certificate.

The physical z factor stays exact in this mathematical definition. It is not replaced by floating phase reduction. The tail is not numerically enumerated or claimed frozen as a binary vector.

## 3. Exact domain and norm certificate

For a=512001/512002 and p>1, the parity upper tail is a^-p+[2(p−1)a^(p−1)]^-1. Apply triangle inequalities to every W and A channel, using abs(z_physical)<8, and retain the odd shift bound 2/n². This gives norm(Phi_Far)<0.001195 / 0.001194.

The exponential series gives 8/3<e<11/4: its sum through degree four is 65/24, and its remaining tail is below 1/100. Rational comparisons (11/4)^11<128000 and (8/3)^12>128000 prove Lambda>11 on Far and Lambda<12 on the finite Near support. Consequently

norm(y_Far)≤norm(Phi_Far)/11,
norm(y)≤sqrt(norm(y_Near)²+(norm(Phi_Far)/11)²),
norm(Lambda*y)≤sqrt((12*norm(y_Near))²+norm(Phi_Far)²).

The new exact-rational domain producer checks every asserted inequality. Strict upper displays:

| Sector | Whole seed norm | Whole logarithmic-diagonal norm |
|---|---:|---:|
| even-v | 1.451453e-4 | 1.662017e-3 |
| odd-v | 1.450119e-4 | 1.660492e-3 |

Thus y is in Domain(Lambda). The already-established bounded perturbation S−Lambda, with norm<575, gives Domain(S)=Domain(Lambda), so this infinite seed is admissible. Its norm is below the unchanged 0.002 trial ceiling.

This does NOT certify that the seed's residual meets 3e-5. The diagonal approximation may need preconditioned corrections; the bounded-perturbation estimate alone is much too coarse to establish acceptance. No claim is made that positive-power moments of this slow tail converge. One must not feed it to the finite-support v14.243 moment engine unchanged.

New exact producer: research-notes/suzuki_infinite_diagonal_seed.py. Payloads: research-notes/payloads/extended_and_infinite_seed_v14_250. The new read-only workflow .github/workflows/suzuki-infinite-diagonal-seed.yml replays only the exact domain/norm JSON byte-for-byte from pinned inputs. Its CI is pending at publication. The exploratory finite screen remains separately flagged [N].

## 4. Next concrete work

Implement a separate certified infinite-tail action/RHS consumer or a controlled compact approximation that bounds the remaining slowly decaying tail. Evaluate and, if necessary, correct the seed before final acceptance. Original source/lift certificates and C_S_32000 are unchanged. No stationary signed pairing or infinite capacity-tail closure has been achieved.

HANDOFF
target: sandbox, external-audit
type: infinite-seed-domain-and-action-plan
parent: v14.250
status: open
action: Audit the exact infinite seed norm/domain proof and replay its pinned JSON. Sandbox: the naive 4R diagonal extension screens poorly (not a rigorous new rejection). Supply a certified action/RHS consumer for the slow tail Phi(n)/log(n/4), retaining physical z_n and the odd shift. Positive-power moment convergence is not required for domain admissibility; split the slow infinite input from the finite-support moment consumer. An integral representation 1/log(n/4)=integral_0^infinity (4/n)^t dt is available for n>4, but any interchange and oscillatory sums must be justified. If corrections are required, give an explicit convergent refinement and consumer rather than treating this seed as accepted.
deliverable: ledger response with audited domain certificate and explicit infinite-input action formulas, error budgets, or a quantitatively justified compact alternative.
constraints: Distinguish [N] screens, [D] mathematical seeds and [V] evaluated certificates; preserve C_S_32000 and all unchanged acceptance targets; no duplicate lift/source contributions; no tail closure without whole residual and signed pair.
