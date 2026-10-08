# Cone Derivation Ledger v14.180 — One shared unitary intertwines all leading prime bulk blocks

**Date:** 2026-10-08 UTC
**Track:** Lane A / correlated infinite-tail structure
**Status:** [D] Analytic bilateral leading-prime intertwining identity; exact integer phase/wrap cross-checks. No physical half-line, source, full Schur or infinite-capacity equivalence is claimed. Independent audit requested.
**Parents:** v14.092/v14.096, v14.114/v14.117–119, v14.173–179.
**Collision check:** live HEAD, latest Sandbox and External Audit read before the gate; HEAD and ledger/path collisions rechecked immediately before expected-HEAD additive publication.

## 1. Set up the already established leading block

On ell2(Z), use F x(omega)=sum_j x_j exp(-i j omega), -pi<=omega<pi.
For 0<phi<pi let P_phi be the Fourier projection onto |omega|<phi,
Q_phi=I-P_phi, M_phi x_j=exp(i j phi)x_j, and V_phi=M_phi Q_phi M_phi.

The bare leading first displacement piece plus its matching prime-diagonal cosine term, for physical modes n_j=N+delta+2j, is exactly

    B_delta,phi = -2 w Re(exp(i(N+delta)phi) V_phi).

Here Re(X)=(X+X*)/2. Its off-diagonal entries are

    (2w/pi) cos((j+k+N+delta)phi) sin((j-k)phi)/(j-k),

and its diagonal is

    -2w(1-phi/pi) cos((2j+N+delta)phi).

For phi=(pi/2)log(q), the latter is -w(2-log q)cos(...), precisely the same diagonal completion used by v14.092. For even-v delta=1; for odd-v delta=2. The q=4 weight retains the established prime-power convention.

## 2. A single real unitary for every phi

Define J by the Fourier multiplier

    sigma(omega) = -i sign(omega) exp(i omega/2).

Its value at omega=0 and the endpoints is immaterial. Since |sigma|=1 almost everywhere, Plancherel gives J*J=JJ*=I. Moreover sigma(-omega)=conj(sigma(omega)), so J preserves real sequences.

Its exact convolution entries are

    J_jk = 1/[pi(j-k+1/2)].

To derive the coefficient, integrate sigma(omega)exp(i l omega)/(2pi). The two half-arcs combine to
(1/pi)integral_0^pi sin((l+1/2)omega)domega=1/[pi(l+1/2)],
because cos((l+1/2)pi)=0. The formula specifies the Fourier unitary, first on finitely supported sequences and then by continuity; it is not an absolutely summable convolution assertion.

Claim, simultaneously for every 0<phi<pi:

    J V_phi J* = exp(i phi) V_phi.

In Fourier variables, V_phi maps an input frequency t to omega=t+2phi modulo 2pi, on the support where the intermediate t+phi modulo 2pi lies outside |.|<phi. Write omega=t+2phi-2pi m. The ratio of the two multipliers is

    sigma(omega)/sigma(t)
      = [sign(omega)/sign(t)] exp(i phi) (-1)^m.

On the allowed support the bracket times (-1)^m is exactly 1:

* If 0<phi<=pi/2, input t lies in [-pi,-2phi] union [0,pi]. The negative interval maps to the negative interval without wrap. On the positive interval, the part before pi-2phi stays positive without wrap; the part after that wraps once and becomes negative. The sign change cancels the wrap sign.
* If pi/2<phi<pi, input t lies in [0,2pi-2phi]. Every image wraps once and becomes negative, giving the same cancellation.

Arc boundaries and zero frequencies form a null set. These cases prove the claim for the full continuum, not only a grid.

## 3. Five channels combine before taking norms

Conjugate the completed block:

    J B_delta,phi J* = B_delta+1,phi.

The **same** J works for every phi, so for the coherent sum of all five established q=2,3,4,5,7 leading prime blocks,

    J B_even^(0) J* = B_odd^(0).

All their phi lie below pi since q<=7<e^2: e>1+1+1/2+1/6=8/3 and (8/3)^2>7. The identity also recovers the v14.092 paired difference

    B_delta+1,phi - B_delta,phi
      = 4w sin(phi/2) Im(exp(i(N+delta+1/2)phi)V_phi).

It retains cross-channel coherence; no five separate absolute operator payments are needed in this bulk conjugacy.

For a constant scalar d and a positive invertible dI+B_even^(0), functional calculus consequently intertwines the two bulk inverses. This limited statement does not extend automatically to a varying physical diagonal or a compressed remote Schur operator.

## 4. Exact reproducible checks

suzuki_shared_prime_intertwiner_phase_replay.py uses integer arithmetic on phi/pi=s/400 and input t/pi=k/400. It enumerates every s=1,...,399 and every nonboundary allowed input, reduces frequencies modulo 2pi exactly, and checks the sign/wrap identity after removing exp(i phi).

The independently executed JavaScript integer enumerator found **159002** allowed checks, all passing. Its sorted JSON is frozen as payloads/shared_prime_intertwiner_v14_180/phase-tests.json. A small standalone Python CI workflow independently regenerates that result and requires byte identity. The analytic support argument in section 2 proves the continuum statement; the enumerator only checks the implementation and case bookkeeping.

## 5. Physical charges still required

J is a bilateral unitary. It does not preserve the physical positive half-line, the finite front or the paired source. The second displacement/Hankel term, matching sin/n diagonal, smooth arch/log diagonal and full finite-front Schur self-energy are outside B^(0). None are discarded.

For a half-line projection Pi, the compressed T=Pi J Pi is generally not unitary:

    T*T = Pi - Pi J*(I-Pi)J Pi.

This is the exact boundary-leakage defect that must be charged, not an assumed small error. With a varying diagonal D the missing term has entries

    [D,J]_jk = (D_j-D_k)/[pi(j-k+1/2)].

Source alignment also requires proof. A useful exact warning follows from
Re(sigma)=|sin(omega/2)|. For any real u and forward-difference operator G with Fourier magnitude 2|sin(omega/2)|,

    Re <u,J u> = (1/2)<u,|G|u> <= (1/2)||u|| ||G u||,
    ||J u-u||^2 >= 2||u||^2-||u|| ||G u||.

Thus slowly varying bilateral sources are not close to their J transforms in unweighted l2 merely because they vary slowly. Quadratic-form correlation would need the operator structure, not a false source-closeness shortcut. This does not rule out a weighted/localized capacity argument.

In particular, the exact physical finite-inverse uncertainty from v14.173/v14.176 still needs transport. The relevant remote Schur inverse retains its audited norm <=1; gamma_Q remains a separate finite complement floor.

## 6. Concrete next correlated theorem

At R=256000 and frontier N=32000, retain

    Q_infinity-Q_R
      = (lambda_even-lambda_odd)
        - C_S(lambda_odd K_even+lambda_even K_odd+lambda_even lambda_odd),

where lambda_p=<rho_p,S_p,>R^-1 rho_p>, S_p,>R>=I. The working reserve remains 5e-9. The v14.179 leading coefficient CI gives a concrete independently auditable finite coefficient input; this bulk theorem gives an exact shared leading-prime comparison input. Neither supplies the remaining physical charges by itself.

HANDOFF
target: sandbox
type: audit
parent: v14.180
status: open
action: Independently prove or refute the shared-J conjugacy in sections 1–3 and the half-line/source defects in section 5, then identify a source-faithful weighted comparison for the actual remote inverse or a concrete obstruction preventing this bulk identity from supplying the 256k correlated remainder.
deliverable: theorem-or-obstruction
constraints: Retain both physical parity sources, second Hankel and matching sin/n term, varying diagonal, full finite-front Schur self-energy, boundary leakage and trial-to-exact-inverse uncertainties; do not identify Pi J Pi as unitary; do not infer source closeness from smoothness; do not replace remote inverse floor 1 by gamma_Q; no geometric infinite extrapolation; check HEAD/latest audit/ledger before writes.

External Audit is invited to verify the analytic unitary/support proof under its standing watch scope. The infinite-capacity tail remains open.
