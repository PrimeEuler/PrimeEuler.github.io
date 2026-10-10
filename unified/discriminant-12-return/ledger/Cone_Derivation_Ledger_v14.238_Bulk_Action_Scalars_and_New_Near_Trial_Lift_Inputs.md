# Cone Derivation Ledger v14.238 — Bulk Action Scalars and New Certified Near-Trial Finite-Lift Inputs

**Date:** 2026-10-10
**Track:** Lane A / evaluated trial-dependent finite-lift INPUT gate
**Status:** [N-cert/D] A new compact represented Near seed is constructed in both parities; every one of its 128000 physical finite-front RHS rows is evaluated by exact integer convolution. Physical RHS error <2.53e-36 per sector. All 256000 Near scalar rows use action precision <1e-39, through an additive bulk evaluator that reproduces the entire original v14.229 physical diagnostic payload byte-for-byte. No new finite solve, whole remote action or stationary acceptance is claimed. Scoped CI replay and additive binary freeze pending observation at publication.
**Parents:** v14.210, v14.213, v14.223, v14.227–229, v14.235–237.
**Collision discipline:** Latest Sandbox v14.236 and External Audit v14.237 read in full; both verify the diagonal evaluator with no correction. Immediately before writing, refresh live HEAD, verify next-free v14.238 and all additive paths, and use a nonforced expected-head update. Preserve original C_S_32000 and every original producer/payload.

## 1. Why this is the next input gate

The audited model action requires a NEW RHS g=B_K^*y and a newly certified solve A ztilde approximately g. Old stationary-source solves do not certify this RHS. The former action-z evaluator costs about 0.165 seconds/row locally (about twelve hours for 256000 rows), because exact Fraction denominators grow through the complex EM calculation. A new bulk path keeps the same physical formula and analytic remainder, using explicitly bounded fixed-integer point arithmetic. Its local 1000-row timing was about 1.35 seconds. Timings are informative, not certificate fields.

This entry constructs a concrete finite-support Near seed and its complete new g. Its support is R<n<=2R, with R=256000, so B_K^*y=B_Near^*y exactly. It does not substitute this seed for the previously constructed exact degree-2400 infinite trial. The seed may be refined or extended after evaluating the whole action. Far output of S*y remains nonzero even though y is zero on Far; it MUST be computed and charged before any residual decision.

## 2. Additive bulk action-z evaluator and uniform arithmetic budget

New script suzuki_bulk_action_z.py reuses the original certified Machin pi, phases, weights and 56-term integer sine. The original suzuki_certified_remote_z.py is untouched. It uses the same B=max(512,64*ceil((bit_length(n)+256)/64)), EM through B8 and exponential moments S0,S2,S4,S6 as v14.229. The analytic remainder remains

    13*(4/(3R))^8 + 1024*10^7/(3^9*R^9) <1e-39.

For the nonprime point, b=floor_B(n*pi_mid/4), a=1/4; reciprocal real/imaginary parts are computed by integer division of a/(a^2+b^2), -b/(a^2+b^2). Complex powers and all subsequent operations are fixed-integer products/floors. The five-term atan expansion retains its explicit next-term radius (1/(n*pi_lower))^11/11. The complete point arithmetic radius is 10^12*2^-B, not zero. The final scalar intervals also include all prime errors and the original analytic EM/exponential remainder.

The exponential moments are computed once per B by outward dyadic interval arithmetic. Their midpoint radii are bounded by 10^10*2^-B, checked at runtime. Here is a uniform bound for the finite arithmetic recipe (B>=512): the alternating exponential enclosure has width <3 units, where one unit is 2^-B; q=e^-4<1/32 and (1-q)^-1<16/15, both asserted. Rounded fourth-power width bookkeeping gives q width <20 units, reciprocal width <25 units. For powers through seven, q-power widths <200 units, reciprocal-power widths <500 units, product widths <1000 units. For p<=6, sum_k Stirling(p,k)*k!<=4683. The outer binomial weights sum to (5/2)^(2r)<=245, r<=3. Thus the final moment width is <2e9 units, comfortably below the midpoint radius budget 1e10 units. All moment magnitudes are <3e9 (also checked); one may use S8<1e7 and a_j>=1/2 to get S_(2r)<=256*S8<2.56e9.

The primitive reciprocal-w component error is <3 units: b's physical error is at most (n/4+1) units, while |d(1/w)/db|<=2/n^2; integer quotient floors add at most one unit per component. The inverse pi point error is <2 units, and the x=1/(n*pi) point error is <2 units. With |w^-1|<1e-4, the four complex-power/EM operations and five atan terms together cost <1000 units. An inverse-pi power through degree seven costs <21 units. Each moment-product discrepancy is bounded by its 1e10-unit midpoint radius plus 21*3e9 units and one multiplication floor. The sum of coefficients 2^(2r+2)/n^(2r+1), r=0..3, is <1 for n>R. The four final division floors and pi/2 term are included. Their total is below 1e12 units. Thus the explicit arithmetic radius is valid uniformly, rather than inferred from 50 samples. At B=512 it is already <1e-140.

New gate suzuki_bulk_action_z_gate.py runs the original v14.229 diagnostic builder with the bulk evaluator substituted, then compares the COMPLETE generated 44537-byte output with the untouched original. All 50 independent original physical reference checks run again. Every original exact-Fraction nonprime interval is also enclosed inside the new nonprime point-budget interval. Two bulk-gate runs are byte-identical. Gate payload: 750 bytes, SHA-256 9bf149989cb12ab4e7b8984af142aefc72dc501c14a9dc7022b419cea8e05865.

## 3. Exact represented Near seed

Use the unchanged v14.228 numerical Near source point buffer and pinned certificate. For each physical Near n, let ell_n be the exact midpoint of log_normalized(n,128) (v14.235's directed recipe); all ell_n>11. Define

    y_n=floor_160(rho_near_point(n)/ell_n), R<n<=2R;
    y_n=0 elsewhere.

This is an exact dyadic trial recipe. No uncertainty in its choice is charged as if it were an approximation to a mandatory trial: any represented finite-support vector is admissible. The underlying physical source transport remains separately governed by v14.223/v14.228 when a future residual/stationary scalar is evaluated. Source error is NOT removed by choosing its midpoint as a seed.

All 128000 seed coordinates per parity and all action-z midpoints at those same modes were evaluated. The z point is floored at 160 bits and its actual interval-plus-floor radius is checked <1e-39 on every row.

| Quantity | even-v | odd-v |
| --- | --- | --- |
| Actual certified trial norm upper | 9.627298817e-5 | 9.618637224e-5 |
| Physical new RHS l2 error upper | 2.525e-36 | 2.523e-36 |
| Future B_K lift-action RHS charge upper | 2.778e-20 | 2.775e-20 |

Displayed ceilings are checked against exact rational certificate fields; they are not decision values.

## 4. Complete physical RHS and transpose convolution

Let n=2(N+k)+s on Near, m=2j+s on the front, N=128000, s=1 or 2. Set H_nm=1/[2(N+k-j)], G_nm=1/[2(N+k+j+s)]. Then

    g_m=c/2*[(H-G)^T(z_near*y)_m - z_m*(H+G)^T y_m]
          +alpha*p_m*sum_near p_n*y_n.

The complete physical pole is retained. Four exact signed GMP integer convolutions with 256-bit reciprocal kernels evaluate every front row. The Toeplitz transpose extraction is convolution(y_reversed,h,N,N) reversed again; the Hankel extraction is convolution(y_reversed,g,2N-1,N). Twenty-four small exact direct-sum row identities validate both parity offsets and three sizes. First/middle/last front rows in each full parity run are independently summed over ALL 128000 Near terms and agree exactly with both convolutions and the final stored RHS coordinate.

Front z,c,p use the original hash-pinned source snapshot and primary certificate, retaining audited physical errors <=1e-38. The source snapshot is original/full and the primary certificate's flags are checked; a constrained source vector is not substituted. The near pole uses directed pi/hyperbolic L,t intervals, midpoints rounded to 256 bits, then floor_256(L*n/(n^2+t)); its physical error is <4*2^-256. The front point pole magnitude <2, front point z magnitude <11, Near point z magnitude <8 and |c_point|<1 are checked.

With eps=2^-256, l1=sum|y_n| and P_point=sum p_near_point*y, the complete per-front-row RHS error is bounded by

    (21e-38+19eps)*l1 + 2e-38*|P_point|
      +4*(4eps)*l1 +eps.

The terms cover Near z, front z, c, both reciprocal kernel errors, front pole error, Near pole/moment error and final RHS floor respectively. Multiply by upward sqrt(N) for the l2 radius. All convolutions themselves are exact integer products; no floating FFT residual is used.

From v14.210 sqrt(G)<5e14 and ||B_K A^-1/2||<22. Thus RHS uncertainty alone has inverse-energy norm <=5e14*rhs_error and future remote-action contribution <=22*5e14*rhs_error, as recorded above. This is only the INPUT uncertainty. A future solve still needs its full physical residual, projected and protected components; no solve error is certified here.

## 5. Frozen outputs and replay

New producer: research-notes/suzuki_near_trial_lift_rhs.py.
Payload namespace: payloads/new_near_trial_rhs_v14_238/.
Certificates: new-near-trial-rhs-even-v.json, 3958 bytes, SHA-256 7183ea82d33db24ece4cbb4c73e7ff84a001fe1783c565dc90dcd7fac498af45; odd-v, 3949 bytes, SHA-256 3865461f0f672a0b04a9511cc49527f28316fc5c5ed551fb10b813cd9c3f2480. Each includes complete binary hashes, packing widths/scales, actual rational norm/error fields and the full-row checks.

Six binary witnesses are generated (160-bit trial and action-z points; 256-bit RHS). Per sector their sizes are 2304000, 2688000 and 3840000 bytes. Full hashes are in the certificates. The scoped workflow reconstructs the ORIGINAL snapshot archives from committed manifest-hashed parts, verifies the immutable v14.228 numerical Near archive, replays the full bulk gate and both 128000-row new RHS producers, and compares all three complete JSON payloads. It then freezes all six binaries, all three certificates and a manifest into the unique payloads/near_trial_rhs_witness_v14_238 namespace. The freezer refreshes HEAD, reads latest ledger, checks any existing namespace for exact equality, stages only that namespace, and uses a normal nonforced push. CI/archive receipt remains pending until observed.

Local input-pin protection caught a truncated copy of odd archive part019. That part was re-fetched from the committed archive, checked against its manifest length/hash, and all 42 parts revalidated before decoding. The decoded original odd snapshot matched SHA-256 6ba7a15aafacebdf0eb4e8b035370f4a7588d63133031e99a8a882779f20a453. No mismatched input was used in the completed odd producer. The committed archive was never changed.

## 6. Next action gate and explicit remaining scope

The actual trial-dependent RHS INPUT gate is closed locally; CI and durable witnesses are pending observation. Next Lane A work: solve the newly evaluated g in both sectors, certify the full residual using the trace-aware finite-inverse energy contract, then evaluate the entire remote action including Far output. The true whole-source error and represented residual norm must be charged before stationary acceptance. A finite Near seed alone does not establish that acceptance; no final sign, paired cancellation or infinite-capacity closure is asserted.

HANDOFF-ACK
from: v14.236, v14.237
target: lane-a
status: closed
result: Sandbox and independent External Audit diagonal verifications read; both include full diagnostics/byte replay, no correction. Linear operator-action and quadratic energy budgets remain separate.

HANDOFF
target: sandbox, external-audit
type: audit
parent: v14.238
status: open
action: Audit the bulk fixed-integer nonprime 1e12*2^-B budget and cached moment error proof; reproduce the entire unchanged v14.229 50-case payload through the new path. Check all new trial/RHS input hashes, transpose offsets, pole error, six complete direct rows and inverse-energy RHS uncertainty propagation. Independently replay both complete new RHS producers from the immutable source/near archives.
deliverable: verified-or-correction
constraints: The new RHS is for the explicitly stated compact Near seed, not an old source solve and not the exact Chebyshev trial. No finite lift or whole remote action is achieved yet.

HANDOFF
target: sandbox
type: task
parent: v14.238
status: open
action: Supply the complete Far-output representation and norm/pairing error contract for S_K*y with y supported on Near and a future residual-certified finite lift ztilde. Combine physical D*y-B_K*ztilde without dropping either denominator or the pole. On R<n<=4R use exact signed H/G convolutions; on n>4R the combined support vector (-ztilde on Front,y on Near) permits geometric expansion with support<=2R. Derive explicit retained moments and remainder norms, and explain how to evaluate the whole represented source-minus-action residual and stationary pairings without enumerating an infinite tail. Identify any required new scalar/moment inputs. The source still has the true full-inverse transport error from v14.213/v14.223; do not identify it with a fixed-trace source.
deliverable: implementation-ready-formula-and-error-budget-or-specific-obstruction
constraints: Keep physical parity/index shift, exact pole and q=4 weight. Do not assume a zero Far action because y_Far=0. Total output arithmetic target 3e-11 is shared by all remaining output errors, not per term. Put the response in the ledger after checking live HEAD/audit and collisions.

## Observed full CI and immutable witness receipt — 2026-10-10

Source commit 1bd7ec50432d34f3304e46a3f6563c0d102b2402. Scoped workflow [38087004649](https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/38087004649), job 114315499295, completed SUCCESS: source archive reconstruction, immutable near witness checks, complete original 50-case action-z replay, both complete 128000-row new RHS producers, all six complete direct sums and all three certificate cmp checks passed. Artifact 11681674787 uploaded successfully. The guarded normal push froze the nine generated witness/certificate files plus manifest in archive commit 10ff11180575cf2ff205dbc3c1a3c9e7abc21c44. Each of the six binaries and three JSON files was checked against its direct local SHA-256/length AND the live Git blob SHA-1/length; all nine match exactly. The manifest was fetched at the archive commit, pins the original source commit, and lists 17672657 payload bytes. All eight originally published producer/workflow/ledger/certificate files were separately byte-verified at the source commit. This closes the input CI/durable archive gate. Finite-lift solve and whole action remain outside this entry's scope; a newly prepared solve gate follows separately. Before this append, live HEAD was the archive commit and latest ledger/audit entry remained v14.238.
