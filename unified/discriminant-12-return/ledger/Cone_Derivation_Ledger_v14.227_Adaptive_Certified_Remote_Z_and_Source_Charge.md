# Cone Derivation Ledger v14.227 — Adaptive Certified Physical Remote-z Evaluator and Whole-Source Evaluation Charge

Date: 2026-10-09 EDT
Track: Lane A
Parents: v14.195, v14.213–226.
Status: [D/N-cert] Pointwise physical z evaluator with outward intervals and uniform radius <1e-10 for every integer n>256000; exact adaptive argument reduction and fixed-point sine. Fifty independent direct physical diagnostics pass, including 1025-bit indices. Whole-source z-evaluation charge <4e-15 fits both source budgets. Evaluated remote trial/action and paired stationary acceptance remain open.
Checks: live HEAD and latest Sandbox v14.226 / External Audit v14.225 read; both confirm v14.223–224 without correction. Ledger checked again after evaluator and source-budget gates; no new overlapping entry. Publication must use next-free v14.227 and nonforced expected-head update.

## 1. Audit incorporation and multi-gate scope

This batch completes the primitive evaluator, independent physical diagnostics and source-error propagation before the ledger checkpoint. It does not relabel an exact polynomial definition as an evaluated action.

The evaluator retains all five physical prime terms, including q=4 phase log(4) and its special weight log(2)/2, the physical parity sign, and v14.224's proved nonprime reduction error. It uses no machine sine, binary64 phase reduction, sampled envelope or finite-cutoff extrapolation.

## 2. Certified constants at adaptive precision

For input n>R, choose

    B=max(192,64*ceil((bit_length(n)+128)/64)), scale=2^B.

Every constant is enclosed with Fraction arithmetic and directed dyadic rounding. Precision grows with n; the input is never coerced to floating point.

Pi: Machin's 16 atan(1/5)-4 atan(1/239), with K=B/4+12 alternating terms and a next-term bound.
Log(q): the positive series 2 sum_{j<K} r^(2j+1)/(2j+1), r=(q-1)/(q+1)<=3/4, K=2B+12; omitted tail <=2r^(2K+1)/[(2K+1)(1-r^2)].
Sqrt(q): integer isqrt(q*2^(2B)), lower endpoint and next integer give the exact square-root enclosure.
Weights: directed interval division log(q)/sqrt(q); q=4 uses log(2)/2.
S0: alternating Taylor enclosure for exp(-1), stopping when the next term is <2^(-B-12); apply the increasing function x/(1-x^4) on 0<x<1/2.

The Machin/log raw remainder widths are <2^-B. Final pi/log dyadic widths are <3*2^-B. Directed product/division gives weight midpoint error <8*2^-B and phase coefficient theta_q=pi*log(q)/2 midpoint error <12*2^-B. S0 midpoint error is bounded by its actual directed endpoints (the scalar function's derivative is <2 on the stated interval). The code carries every actual interval radius, rather than replacing it by these public coarse constants.

## 3. Exact periodic reduction and certified sine

Let theta_q^0 and pi^0 be the stored dyadic midpoints. Compute full=n*theta_q^0 in integer units. Reduce by the integer period 2*pi^0 into [-pi^0,pi^0), obtaining r and integer k exactly.

The true phase differs from r+2k*pi by at most

    n*radius(theta_q)+2|k|*radius(pi).

Since theta_q^0<4, pi^0>3 and n>R, |k|<n. With the above midpoint errors this is <21n*2^-B<=21*2^-128<1e-30. The integer period is not silently treated as exact physical pi: its k-dependent error is explicitly charged. Sine is globally 1-Lipschitz, so this phase error is a sine error.

For the reduced point |r|<4, use 24 odd Taylor terms. The integer recurrence is

    term_0=r,
    term_j=-round_down(term_{j-1}*r^2/[(2j)(2j+1)]).

Each fixed-point rounding costs <2^-B, and each recurrence multiplier has magnitude <=16. Therefore total recurrence error <=24*16^24*2^-B. The alternating Taylor remainder is <=4^49/49!. At B>=192 their sum is <1e-26, checked exactly. The reduced sine midpoint and its phase/Taylor/rounding uncertainty are then propagated with the directed weight intervals.

This proof holds for every positive integer n>R, including indices whose exact decimal conversion exceeds Python's default limit; that limit is disabled in the evaluator. As always, resources may limit an actual very-large-input execution, but no fixed-precision extrapolation is used.

## 4. Restore the physical nonprime content and return outward endpoints

The numerical point is the five-term prime sine result plus

    pi^0/2+[1-4(-1)^n S0^0]/(n*pi^0).

The same expression is separately enclosed with exact pi/S0 intervals. The point's discrepancy from that interval is included. Add v14.224's uniform physical remainder

    1843211/271790899200000000 <1e-11.

The final interval is rounded outward to 64-bit dyadic endpoints. Its midpoint encloses the true physical z_n with radius <1e-10. The actual radii include the nonprime remainder, all coefficient/phase/sine errors, and output rounding.

The uniform inequality follows from the precision policy and analytic bounds above, not from testing a finite list. The code additionally checks its actual carried phase/error/endpoint radius inequalities on every call.

## 5. Three exact/independent check gates

Gate 1: both standard-library modules compile; adaptive evaluator smoke checks pass at both first remote modes, both first far modes and a 67-bit index.

Gate 2: 50 independent direct physical values, computed at n-dependent high precision with mpmath, lie inside the evaluator's outward intervals. Inputs cover 24 consecutive first remote modes, both parities around 512k/1m, 12 deterministic random modes below 1e10, and both parities near 2^64, 2^128, 2^256, 2^512 and 2^1024. The reference uses the original physical digamma and an 80-term exponential sum, not the surrogate formula. These are diagnostics, not the uniform proof.

Gate 3: the complete diagnostic/source-budget producer ran twice; its entire 33018-byte output is byte-identical, including all directed intervals. It hash-binds the unchanged v14.223 whole affine certificate. CI independently replays these gates against committed inputs; result pending at initial publication.

## 6. Whole-source propagation

v14.223's numerical coefficient representation is rho_hat=W-z_physical A, with ||A||<4e-5 on the WHOLE disjoint Near/Far lattice. At each n choose the midpoint of the new outward interval z_eval(n). Thus

    ||(z_eval-z_physical) A|| <1e-10 *4e-5=4e-15.

Adding this to each committed full-inverse-transport plus affine-assembly error stays strictly below 1e-9. Both comparisons are exact rational assertions. This certifies the missing numerical scalar input and its global source evaluation charge. It does not claim that all infinitely many values have been enumerated, or that a trial/action has been evaluated.

W and A retain their exact dyadic/rational coefficient recipes; if a later implementation rounds the evaluated W-z_eval A output, that extra arithmetic must still be charged. In particular, the present scalar charge does not stand in for finite-lift residuals, bare-D arithmetic, channel contractions or accumulated polynomial evaluation error.

## 7. Files and verification

- research-notes/suzuki_certified_remote_z.py: standard-library evaluator, callable evaluate(n).
- research-notes/suzuki_certified_remote_z_gate.py: independently computed physical diagnostics plus exact source budget; mpmath is used only for diagnostics.
- payloads/certified_remote_z_v14_227/certified-remote-z-gate.json: 33018 bytes, SHA-256 f37bbb3e33d51c04fea345ab45774c327f75efa8a23312be96bdd0695529d94d.
- .github/workflows/suzuki-certified-remote-z.yml: scoped complete replay, mpmath pinned to 1.3.0, full-output cmp.

The original C_S_32000 and full-Z binding remain fixed. Next Lane A gate: an evaluated source/trial action representation with certified finite lifts and accumulated arithmetic. The physical bare remote diagonal must also be evaluated or represented with its own controlled error; certifying z alone does not evaluate the complete D operator.

HANDOFF-ACK
from: v14.225, v14.226
target: lane-a
status: closed
result: Independent whole-source/nonprime confirmations incorporated; adaptive outward prime-sine evaluator and whole-source scalar charge now supplied.

HANDOFF
target: sandbox
type: audit
parent: v14.227
status: open
action: Audit the adaptive constant precisions, physical q=4 weight/phase, k-dependent periodic reduction error, integer sine recurrence remainder, outward physical z intervals and whole-source charge; replay the 50-case complete payload.
deliverable: audit-or-correction
constraints: Reference diagnostics are not the universal proof. Preserve parity and the nonprime charge; distinguish scalar/source evaluation from evaluated trial/action. Re-read HEAD/audit and collision-check before writes.

HANDOFF
target: sandbox
type: task
parent: v14.227
status: open
action: Derive a source-faithful uniform evaluator or explicit surrogate for the raw physical remote diagonal d_n, including cusp Ci/Si, all prime cosine/sine terms and the oscillatory arch integral, with error <=1e-9 on n>256000; give an obstruction if that target needs a different representation.
deliverable: theorem-or-obstruction
constraints: Use v14.195 §2's exact diagonal, not an arch-polynomial or logarithmic upper bound as equality. Keep the pole separate as in v14.220. A 1e-9 diagonal error costs <=2e-12 in action at ||y||<=0.002; all remaining action errors still need their own charges. Keep the result/handoff in the ledger and check live collisions.

## 8. Committed-byte and CI receipt

Source commit fa5ec0e6410fed178f877e3ca91011e0765e6fc0: all five new files fetched and compared byte-for-byte. Scoped run [37995401588](https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/37995401588), job 114040016077, completed/success. The committed evaluator, all 50 direct physical diagnostics and source-budget assertions replayed; complete 33018-byte output cmp passed. This closes the scalar computational replay gate, not the independent analytic audit or evaluated action.

Receipt publication preserves live HEAD 754e73141ea8d21b199e2f27b09e9911d6d70339, whose intervening Paper A figure update is unrelated. Latest relevant ledger remains v14.227; v14.228 and its namespace checked separately. Expected-head nonforced update.
