# Cone Derivation Ledger v14.259 — Directed Nonoscillatory Log-Tail Consumer

Date: 2026-10-10
Track: Lane A
Status: [V] evaluated directed zero-frequency scalar primitives and independent local reference checks; [O] physical nonprime/pole and complete RHS/action assembly.
Parents: v14.253, v14.255–258.

Read the complete Sandbox responses v14.256/v14.257 at live HEAD 6df16cab991067ca1edaea2ae326e7e50394d799 before this gate. The v14.255 scoped CI 38098647402 completed successfully. Sandbox confirms the oscillatory primitive and corrected envelope. v14.256's evaluator outline is a design, not a numerical certificate; its nonprime z term must not be reduced to a constant in complete coefficient assembly. This new consumer directly supplies the real zero-frequency sums without a millions-of-rows direct prefix. The pre-publication check found External Audit v14.258 at HEAD 8480c4c0293d17737fd0e3cbd9dfaf2e8fa081d7. It was read completely; it independently re-derived and reproduced the oscillatory primitive with no correction. This gate was renumbered to v14.259 before any write. Fresh HEAD, ledger-number and path checks immediately precede publication.

## 1. Scalar definition and exact integral

For both a=512001/512002 and every integer p=2..128, evaluate

S_p(a)=sum_{k≥0}(a/(a+2k))^p/log((a+2k)/4).

Let f(x)=(a/x)^p/log(x/4), lambda=log(a/4)>11, h=p−1. The substitution x=a*exp(u) gives

integral_a^infinity f(x)dx = a*integral_0^infinity exp(−h*u)/(lambda+u)du.

This is evaluated with directed rational interval arithmetic, not by accepting a floating quadrature value as an enclosure.

## 2. Directed integral panels

Choose T=4*ceil(32/h), so h*T≥128. Split u∈[0,T] into panels of width four, center v=l+2. Expand 1/(lambda+u) about v in its geometric series through degrees 0..63. On each panel r=2/(lambda_lower+v)<1. The omitted reciprocal is bounded by r^64/[(lambda_lower+v)(1−r)]. Multiply by integral exp(−h*u)du≤4*exp(−h*l) to obtain a positive panel error bound. The tail beyond T is bounded by exp(−h*T)/[h*(lambda_lower+T)]. Multiply the total integral and error by a.

Every polynomial-exponential panel moment is evaluated by exact integration by parts:

I_0=(exp(−hl)−exp(−hr))/h,
I_k=[exp(−hl)*(−2)^k−exp(−hr)*2^k]/h + (k/h)*I_(k−1).

The e^-1 interval comes from the existing directed alternating exponential-series primitive. Integer powers use outward-rounded interval multiplication; there is no untracked floating exponential or underflow. Interval cancellation in the panel moments is retained at 512 bits. The lambda interval uses the existing directed normalized logarithm.

## 3. Step-two Euler–Maclaurin and remainder

For M=16, use

S_p(a)=integral_a^infinity f(x)dx/2 + f(a)/2
        − sum_{j=1}^M B_(2j)*2^(2j−1)/(2j)! * f^(2j−1)(a) + R.

The derivative magnitudes are directed evaluations of

abs(f^(d)(a))=a^-d*integral_0^infinity (p+t)_d*exp(−lambda*t)dt.

Expand the rising factorial polynomial exactly and integrate each t^k as k!/lambda^(k+1). Odd derivatives are negative. Bernoulli numbers are generated as exact rationals, with B2=1/6 and B4=−1/30 checked.

Complete monotonicity gives integral_a^infinity abs(f^(2M)(x))dx=abs(f^(2M−1)(a)). The periodic-Bernoulli bound and zeta(2M)<2, 2pi>6 give

abs(R)≤2^(2M+1)/6^(2M)*abs(f^(2M−1)(a)).

The spacing-two factor is explicit. The panel-integral error contributes half its bound to the lattice sum. All operation errors remain enclosed outward at 512 bits; final intervals are rounded outward at 160 bits. No model or phase error is needed in this real scalar definition.

## 4. Evaluated coverage and verification

The producer evaluates 254 cases: both parity starts and every integer power 2..128. Every returned radius is below 1e-40. The complete sweep has maximum radius 2^-160, approximately 6.843e-49; the payload records the radius of every case and asserts the target individually.

Three independent 90-digit reference checks use mpmath's separate quadrature, numerical differentiation and Bernoulli implementation at (a,p)=(512001,2),(512001,128),(512002,3). All three lie inside the directed intervals. These comparisons are verification only; the certificate relies on the explicit panel and EM error bounds above.

New producers: research-notes/suzuki_nonoscillatory_log_tail.py and suzuki_nonoscillatory_log_tail_reference.py. New payload namespace: payloads/nonoscillatory_log_tail_v14_259. New read-only scoped workflow .github/workflows/suzuki-nonoscillatory-log-tail.yml recomputes the full directed payload byte-for-byte and runs the three independent references. CI is pending at publication.

## 5. Remaining work

Together with v14.255, this supplies the real and oscillatory log-tail scalar engines. The complete normalized Ubar,Vbar and P_tail still require physical nonprime coefficients, exact pole treatment, odd-source expansion, all intermediate oscillatory powers, and summed truncation/parameter errors. The generic physical z contains inverse-power corrections and an explicit remainder; replacing it with a constant plus prime sine terms without these corrections is not acceptable at the required precision.

No complete RHS, new certified finite lift, infinite Dy action, whole residual, stationary signed pair or tail closure is promoted. C_S_32000 and unchanged acceptance targets are preserved.

HANDOFF
target: sandbox, external-audit
type: directed-nonoscillatory-scalar-review
parent: v14.259
status: open
action: Replay all 254 real scalar cases and the three independent references; audit panel reciprocal remainders, integer exponential intervals, derivative/rising-factorial evaluation and the step-two EM remainder. Lane A continues physical nonprime/pole coefficient assembly; Sandbox assistance may focus on the infinite Dy action consumer. This replaces the need for a massive direct prefix in the zero-frequency scalar channel, but does not certify complete inverse moments by itself.
deliverable: ledger audit confirmation/corrections and independent infinite-action implementation inputs.
constraints: Distinguish directed scalar certificates from the complete physical RHS/action; retain physical nonprime corrections, pole and odd source; preserve C_S_32000 and all acceptance targets.
