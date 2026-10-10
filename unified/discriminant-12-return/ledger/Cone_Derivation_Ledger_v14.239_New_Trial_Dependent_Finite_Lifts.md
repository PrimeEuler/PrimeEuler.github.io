# Cone Derivation Ledger v14.239 — New Trial-Dependent Finite Lifts with Full Physical Residual Energy Certificates

**Date:** 2026-10-10
**Track:** Lane A / finite-lift solve gate for v14.238's compact Near trial
**Status:** [N-cert, local] Both NEW finite-lift solves have complete physical residual-energy enclosures. Local lift-action charges <5e-11 even-v and <2e-14 odd-v; both fit the unchanged overall action ceiling 2e-10 when the remaining TOTAL output arithmetic <=3e-11 is achieved. The even solve does not meet the old sufficient protected-dot target, and that fact is explicitly retained. No whole remote action, represented remote residual or stationary paired acceptance is asserted. Scoped producer/point-witness/exact-replay/freeze CI pending observation at publication.
**Parents:** v14.210–213, v14.223, v14.229, v14.235–238.
**Write discipline:** Read latest live Sandbox/External Audit and HEAD, verify next-free ledger number and unique paths immediately before writing; use nonforced expected-head update. Original C_S_32000, original finite snapshots and original producers stay unchanged.

## 1. Actual new RHS, not an old source solve

The input g is v14.238's physical B_Near^*y for its explicitly frozen compact Near trial y. On this support B_K^*y=B_Near^*y, K=42. All 128000 front RHS entries and their physical input error are already certified. Each source snapshot, primary certificate, new RHS certificate and binary RHS is hash-pinned. The old fixed-trace source and the exact degree-2400 infinite trial are not substituted for g or y.

New implementation: research-notes/suzuki_new_finite_lift.py. It supplies two modes:

- produce: construct a new represented finite iterate with a graph seed and two complement/protected refinements;
- replay: read the frozen represented iterate and recompute the COMPLETE physical residual-energy certificate from scratch, independent of the floating solver history.

The producer chooses an iterate; the exact residual consumer supplies the proof. FFT/CG residuals are not acceptance certificates.

## 2. Represented iterate construction

Let V_0,...,V_5 be the unchanged original graph columns and J_point their pinned represented 6x6 matrix. The graph seed has coefficients floor_512(J_point^-1 V^*g). It contains ONLY those six graph columns; the old source column V_6 is replaced by zero when the existing exact dyadic combination helper is used.

For each of two refinements:

1. Evaluate the full point action A_point*ztilde by the existing exact GMP integer convolution engine.
2. Form s_point=A_point*ztilde-g_point. Project it with the exact frozen P Gram inverse, then floor the complete projected combination at 256 bits.
3. Solve the projected correction numerically using a fixed binary64 FFT/CG operator; convert the chosen correction to exact dyadics and add it without discarding the graph column's much larger coordinates.
4. Re-evaluate the full point action exactly, compute all six V^*s contractions, and apply a newly rounded 512-bit graph correction.

The floating operator retains the Toeplitz and Hankel commutator, the matching c*z/(2n) diagonal restoration, raw diagonal and full pole. The acceptance replayer does not trust this operator: it uses the original physical source's exact point action and charges the physical scalar/kernel uncertainty. Different floating environments may choose different acceptable point iterates; CI freezes the one it actually certifies, then independently replays that SAME point witness byte-for-byte.

Local complement iterations were 59,61 (even) and 56,58 (odd). Point projected residuals fell from about 7.14e-5 to about 1.01e-18/8.11e-19 after one refinement, then to 1.35e-32/1.15e-32 after two. These are diagnostic values, not physical residual bounds.

## 3. Physical residual and retained protected component

For every represented iterate, with physical s=A*ztilde-g, compute exact point quantities

    q_point^2 = ||s_point||^2
                -(P^*s_point)^* (P^*P)^-1 (P^*s_point),
    d_point^2 = sum_j |V_j^*s_point|^2,

using all 128000 residual coordinates. The first quantity is nonnegative by an exact Fraction comparison; no negative clipping or floating Gram subtraction occurs. Let delta_A be the unchanged audited physical point-operator radius, rhs_eta the v14.238 physical RHS radius, and

    input_eta=delta_A*||ztilde|| + rhs_eta,
    q_s=sqrt_upper(q_point^2)+input_eta,
    d_s=sqrt_upper(d_point^2)+sqrt_upper(graph_vector_norm2)*input_eta.

The RHS uncertainty enters this complete physical residual exactly once. It is NOT added again as a separate future lift-action term. All source and kernel uncertainty in A enters delta_A. Both primary certificate bytes and the recomputed delta_A are checked against their pinned values.

Local outward physical bounds:

| Quantity | even-v upper | odd-v upper |
| --- | --- | --- |
| ||ztilde|| (display only) | 1.514e9 | 2.990e7 |
| q_s | 5.277e-27 | 1.043e-28 |
| d_s | 2.217e-12 | 8.727e-16 |

The physical upper bounds are larger than the tiny point residual because physical operator uncertainty is charged. In particular, even-v d_s exceeds the older sufficient target 8e-13. No flag promotes that older target as met.

## 4. Actual inverse-energy and remote lift-action certificate

Use the full finite inverse decomposition from v14.210, preserving the non-unit graph traces and the six protected components. Recompute from the ORIGINAL primary certificate:

    gamma = 2.37e-13 (even), 4.15e-12 (odd),
    f=graph_residual_fro/(1-rho),
    j=min_i(J_ii-sum_(k!=i)|J_ik|),
    nu=rho/(1-rho),
    assembly=b_J+2*b_beta+b_eta,
    a=b_J+nu*(2+nu)*(||M||_infinity+assembly)+f^2/gamma,
    h=j-a>0.

Then

    E <= q_s^2/gamma + [d_s/(1-rho)+f*q_s/gamma]^2/h,
    ||B_K*(ztilde-A^-1 g)|| <=22*sqrt_upper(E).

Every operation is exact rational or upward dyadic square root. The serialized E is rounded UP to 192 bits after the full rational calculation. The ceiling 22 dominates the already certified chi+tau; it is not a new unproved Euclidean B bound.

Local certificate results:

| Quantity | even-v strict upper | odd-v strict upper |
| --- | --- | --- |
| Physical inverse-energy error E | 4.936e-24 | 7.646e-31 |
| Remote finite-lift action error | 4.888e-11 | 1.924e-14 |

These are actual new residual-energy certificates for this g, not an extrapolation of the old stationary source certificate. The local point witnesses contain all 128000 finite coordinates, each packed into 87 signed little-endian bytes (11136000 bytes per sector).

## 5. Old sufficient targets versus unchanged final contract

v14.210's q_s/d_s targets were sufficient to achieve lift action <3e-11 at the old generic trial ceiling. They were not necessary conditions for any successful certificate. Here the actual compact trial has norm <1e-4. Compute the actual lift error, rather than declaring the old sufficient targets achieved:

    conditional_delta = actual_lift_error
                        + epsilon_model*||y||
                        +3e-11 remaining TOTAL output arithmetic
                        +5e-26 remote-z model charge.

Use epsilon_model<3.454e-8 even, <1.334e-10 odd (the conservative geometric plus optional cached-M11 bound). The source-faithful direct finite-lift path does not replace a mixed block by cached M11; retaining this larger charge is conservative.

| Conditional total action | even-v strict upper | odd-v strict upper |
| --- | --- | --- |
| Including actual lift plus all stated reserves | 8.220e-11 | 3.004e-11 |

Both are below the UNCHANGED v14.223 final action ceiling 2e-10. This does not claim that output arithmetic has been evaluated: the 3e-11 reserve still covers all bare-D/output/channel/remaining arithmetic together. The diagonal scalar's linear action cost must live in that reserve; do not give every remaining term its own 3e-11 allowance. Source transport/assembly remains separate in the final residual and stationary form. No actual represented remote residual norm or stationary scalar is computed here.

## 6. Witness production, exact replay and durable freeze

Local represented lift SHA-256:

- even-v: 737b23f211568d73ebe07a1f2c63561a885dc5a1cd11747f693d8835abb4f9fb
- odd-v: d9195dffdad1d191fdcb2cf41dc33198df43d3381dea06ced25b249f6f683f10

The new scoped CI workflow reconstructs and verifies the original snapshot/primary certificates, verifies the immutable v14.238 new trial/RHS witness archive, constructs its own two represented lifts, and runs a fresh --mode replay on both complete point witnesses. Both complete certificate JSONs must pass cmp before upload/freezing. The accepted point vector is then frozen with its matching certificate and manifest in the unique payloads/new_finite_lift_witness_v14_239 namespace, through an immediately refreshed HEAD, collision check and normal nonforced push. The source producer and workflow are additive. No prior archive is rewritten.

Floating CG output is allowed to vary between environments, so the exact CI certificate is compared to a FRESH REPLAY OF THE SAME FROZEN POINT VECTOR, not to a presumed universal CG byte stream. The CI archive and its recorded certificate become the durable evaluated witnesses. This distinction is explicit; the local display/hash values above describe local witnesses only. CI receipt and actual archived hash/bounds will be appended after observation and live byte/hash checks.

## 7. Remaining action and paired closure

This closes the new finite-lift solve analytically/locally. Durable CI replay/freeze is pending at publication. Next is the entire represented remote action D*y-B_K*ztilde, including every Far output despite y_Far=0, with the shared arithmetic error certificate. The Sandbox Far-output task is already in v14.238. Only after computing the whole represented residual and stationary form may the existing paired acceptance consumer be used. No final tail theorem is claimed.

HANDOFF
target: sandbox, external-audit
type: audit
parent: v14.239
status: open
action: Independently replay the new finite point witnesses and physical residual certificate; verify projected and all six protected components, the inclusion of RHS uncertainty exactly once, original full inverse-energy graph floor, and actual lift-action propagation. Check that even-v's old 8e-13 sufficient d_s target is NOT marked met, while the unchanged overall 2e-10 action contract still fits using the actual small trial norm and shared 3e-11 output reserve. Review the additive producer/point-witness/replayer/CI freeze discipline. Continue the v14.238 Far-output task using these actual lift witnesses once frozen.
deliverable: verified-or-specific-correction
constraints: Finite lift certification is not a whole remote action or stationary residual certificate. Preserve full unrestricted A^-1, physical parity, pole, both denominator channels, source transport, and original C_S_32000. Re-read live HEAD/audit and collision-check before writing.
