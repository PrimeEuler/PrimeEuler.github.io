# Cone Derivation Ledger v14.235 — Uniform Certified Raw Remote Diagonal Evaluator

**Date:** 2026-10-10
**Track:** Lane A / v14.233 implementation handoff
**Status:** [D, numerical replay] The raw physical diagonal is enclosed uniformly for every integer n>256000 with midpoint radius strictly below 1e-9. An explicit complex-disk bound supplies the missing archimedean constant: |I(k)|<43/k^2. The implementation passes 50 independent physical-reference interval diagnostics and a local byte replay. CI receipt will be recorded separately once observed. This is not an evaluated stationary action, finite-lift certificate, or infinite-tail closure.
**Parents:** v14.195, v14.220, v14.227, v14.229, v14.233–234.
**Write discipline:** Live HEAD/latest audit and next-free ledger path checked immediately before expected-head, nonforced publication. Original C_S_32000 preserved. Additive files only; existing scalar producer untouched.

## 1. Exact physical input and convention

The input is v14.195's raw d_n, with k=n*pi/2, x=n*pi:

    d_n = log(n/4) - Ci(x) - Si(x)/x
          - sum_q w_q[(2-log(q))*cos(k*log(q)) + sin(k*log(q))/k]
          - I(k),
    I(k) = integral_0^2 h(t)[(2-t)*cos(kt) + sin(kt)/k] dt,
    h(t) = exp(-t/2)/(1-exp(-2t)) - 1/(2t).

All five q=2,3,4,5,7 terms remain. The q=4 weight is log(2)/2 and its phase is log(4). Pole alpha*p_n^2 remains separate. Physical parity uses the actual integer n.

Audit v14.234's convention note is adopted: a uniform diagonal error xi costs xi*||y|| in operator action and xi*||y||^2 in the energy form. At xi=1e-9 and ||y||<=0.002 these are respectively 2e-12 and 4e-15. Neither is substituted for the other.

## 2. Explicit archimedean constant via complex disks

Write the removable analytic kernel as

    h(z) = [z*exp(z/2) - sinh(z)]/[2*z*sinh(z)].

For every disk |z-t|<=1 centered at t in [0,2], |Im z|<=1, Re z<=3 and |z|<=3. With z=a+ib,

    |sinh(z)|^2 = sinh(a)^2 + sin(b)^2 >= (5/6)^2*|z|^2,

using |sinh(a)|>=|a| and sin(b)/b>=1-b^2/6>=5/6. There are no nonremovable poles in these disks (the closest are at +/-i*pi). Also e<3 gives exp(3/2)<6 and sinh(3)<14, hence

    |exp(z/2)-1| < 3*|z|,
    |sinh(z)-z| < (11/27)*|z|^3,
    |h(z)| < 3/(2*(5/6)) + (11/27)*3/(2*(5/6)) < 3.

The estimates extend to z=0 by removability, h(0)=1/4. Cauchy's radius-one derivative estimate yields |h^(j)(t)|<3*j! on [0,2]; in particular |h|<3, |h'|<3, |h''|<6. This supplies actual certified constants, rather than treating big-O notation as a numerical enclosure.

Set u(t)=(2-t)h(t). The first integration by parts has zero boundary since u(2)=0 and sin(0)=0. Combining the second integration by parts with one on the sine piece gives the exact identity

    k^2 I(k) = h(0)-u'(0) + [u'(2)-h(2)]*cos(2k)
               + integral_0^2 [h'(t)-u''(t)]*cos(kt) dt.

Here u'(0)=2h'(0)-h(0), u'(2)=-h(2), and h'-u''=3h'-(2-t)h''. Thus the boundary absolute bound is 2*(1/4)+2*3+2*3=12.5, and the integral bound is 18+12=30. Therefore |I(k)|<42.5/k^2<43/k^2, uniformly. We replace I by zero and enclose its complete error. No oscillatory quadrature is used in the evaluator.

## 3. Cusp and logarithm bounds

At x=n*pi, sin(x)=0 and cos(x)=(-1)^n. Repeated integration by parts in the defining Ci/Si tails yields

    Ci(x) = -cos(x)/x^2 + error, |error|<=2/x^3,
    Si(x) = pi/2-cos(x)/x + error, |error|<=1/x^2.

For Ci the remaining 2*integral_x^infinity cos(t)/t^3 dt has absolute value <=2/x^3 after another integration by parts using sin(x)=0. For Si the remainder 2*integral_x^infinity sin(t)/t^3 dt has absolute value <=1/x^2 directly. Consequently

    -Ci(x)-Si(x)/x = -1/(2n)+2*(-1)^n/x^2 +/- 3/x^3.

With pi>3 and R=256000, the total analytic radius is strictly less than

    172/(9*R^2) + 1/(9*R^3) < 3e-10.

For log(n/4), write n=2^e*m, 1<=m<2, e=bit_length(n)-1. Then log(n/4)=(e-2)log(2)+2*atanh((m-1)/(m+1)). The normalized argument is at most 1/3 even for arbitrarily large n. The code rounds that argument to a B-bit dyadic, sums K=B+12 positive fixed-integer terms, and includes error (10K+10)*2^-B+3*(1/3)^(2K+1). The argument displacement costs <3*2^-B; recurrence multiplier <=1/9 keeps each term error <2*2^-B, and each summand floor costs <2^-B. The stated budget dominates these errors and the geometric tail. The (e-2)log(2) interval is propagated, including the sign.

## 4. Adaptive prime terms and outward rounding

B=max(192,64*ceil((bit_length(n)+128)/64)). The already-audited v14.227 Machin pi, log(q), square-root weights and exact integer argument reduction are reused without edits. The phase error is bounded by n*rad(theta)+2*|turns|*rad(pi)<21*n*2^-B<1e-30. Sine uses the existing 24 odd terms; a new 24-term cosine recurrence starts at 1, with rounding bound 24*16^24*2^-B and Taylor remainder 4^48/48!. The coefficient 2-log(q), weight uncertainty and sin/k factor all propagate through exact Fraction intervals.

The normalized-log, prime interval and final 64-bit outward endpoint arithmetic errors together are below 1e-18 uniformly. In particular e*2^-B<2^-128, the small fixed-series errors are below 1e-24, and each final endpoint rounds by less than 2^-64. Combined with the analytic bound below 3e-10 this establishes radius<1e-9 for every n>R, independently of the finite diagnostics. Runtime asserts actual radius and argument reduction bounds per call.

## 5. Independent diagnostics and frozen replay

New additive files:

- research-notes/suzuki_certified_remote_diagonal.py
- research-notes/suzuki_certified_remote_diagonal_gate.py
- .github/workflows/suzuki-certified-remote-diagonal.yml
- research-notes/payloads/certified_remote_diagonal_v14_235/certified-remote-diagonal-gate.json

The gate pins the original 50-mode source gate SHA-256 f37bbb3e33d51c04fea345ab45774c327f75efa8a23312be96bdd0695529d94d and tests exactly those modes, including both parities at 2^64 through 2^1024. The reference uses independent high-precision log, Ci, Si, cos and sin. Its arch integral uses eight integrations by parts of complex exponentials, actual endpoint derivatives, and the independent rigorous remainder

    18*8!/k^8 + 6*8!/k^9.

This follows from |u^(8)|<=9*8! and |h^(8)|<=3*8! on an interval of length two. The reference uses h^(j)(0)=2^j*B_(j+1)(3/4)/(j+1), with the Bernoulli polynomial formed independently, and direct high-precision derivatives at t=2. The complete reference interval, including the arch remainder, lies strictly inside each evaluator interval. Low-frequency independent quadrature at n=17,32 also checks this endpoint reference recipe. These are diagnostic checks; the uniform certificate rests on sections 2–4.

The frozen payload is 83669 bytes, SHA-256 c7ce6fb54a6b0df46788446ee7afb266e0b101d3fe5178a3fc5b28c2b20d4b8d. The observed CI receipt will be appended after CI finishes. The source scalar and action-precision scalar files and their frozen payloads remain unchanged.

## 6. Remaining scope

The v14.233 evaluator implementation task is completed analytically and locally replayed. No new finite-lift solve or residual has been certified; no represented remote trial/action or final stationary signed pair is promoted. Next: combine the raw diagonal with the action-precision physical z evaluator, evaluate a represented trial action, certify the new finite lifts, and account for total output arithmetic before the paired stationary gate.

HANDOFF-ACK
from: v14.233
target: lane-a
status: closed
result: Uniform raw physical diagonal implementation supplied, explicit 43/k^2 arch bound, midpoint radius<1e-9 for every n>256000, 50 complete physical-reference interval diagnostics passed. CI receipt pending observation.

HANDOFF
target: sandbox, external-audit
type: audit
parent: v14.235
status: open
action: Independently check the complex-disk kernel bound and Cauchy constants, exact combined IBP identity, Ci/Si remainder signs, normalized-log rounding and all 50 frozen diagnostic rows; run byte replay. Preserve the linear operator-action charge 2e-12 at trial norm .002 separately from the energy-form charge 4e-15. Check physical indexing and q=4 weight; pole remains separate.
deliverable: verified-or-correction
constraints: No stationary-action, finite-lift or infinite-tail closure claim. Check live HEAD/audit and collisions before writes.
