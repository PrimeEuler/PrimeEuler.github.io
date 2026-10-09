# Cone Derivation Ledger v14.229 — Action-Precision Remote Scalar and Certified z-Only Model Action Charge

Date: 2026-10-09 EDT
Track: Lane A
Parents: v14.195, v14.210, v14.223–228.
Status: [D/N-cert] Adaptive action-precision physical z evaluator with uniform radius <1e-39 for all n>256000; fifty independent physical diagnostics pass. Its z-only whole model action charge is <5e-26 for ||y||<=0.002, even using the full finite inverse norm. Default source mode is byte-identical to v14.227. No finite lift, complete D action, evaluated trial or signed paired stationary acceptance is claimed.

## 1. Why a second scalar precision is needed

v14.227's <1e-10 scalar radius is sufficient for evaluating rho=W-z A, because ||A||<4e-5. It is not by itself a safe generic error cap for a new finite-lift RHS B_K* y: the full finite inverse has a huge norm. This entry supplies a distinct action-precision mode rather than reusing the loose source cap inside a protected finite solve.

The API is evaluate(n, action_precision=True), or CLI --action-precision. The mode automatically uses at least 160 output bits, 512 working bits, and a 256-bit phase guard growing with bit_length(n). The default API and CLI source mode retain their original exact output bytes.

## 2. Higher-order digamma remainder, preserving physical content

Put w=1/4+i*n*pi/4. Euler–Maclaurin through order eight gives

    psi(w)=log w-1/(2w)
           -sum_{j=1}^4 B_(2j)/(2j*w^(2j))
           +integral_0^infinity B8({t})/(w+t)^9 dt,

with B2=1/6, B4=-1/30, B6=1/42, B8=-1/30. The exact periodic polynomial is

    B8(t)=t^8-4t^7+(14/3)t^6-(7/3)t^4+(2/3)t^2-1/30.

On [0,1] its coefficient absolute sum is 127/10<13, so |B8|<13. With b=n*pi/4,

    integral_0^infinity |w+t|^-9 dt
       <=b^-8 integral_0^infinity (1+s^2)^(-9/2) ds
       <=b^-8,

since the last integrand is bounded by (1+s^2)^(-3/2), whose integral is 1. Therefore the retained digamma expression has error <13(4/(3n))^8.

The imaginary logarithm is pi/2-atan(1/(n*pi)). Five alternating atan terms are retained, and the next x^11/11 is carried as an interval remainder. Complex reciprocal powers are evaluated through directed rational interval multiplication; neither log(w) nor digamma is called by the evaluator.

## 3. Four exponential moments and an explicit infinite remainder

With a_j=2j+1/2, k=n*pi/2,

    1/(a^2+k^2)=sum_{r=0}^3 (-1)^r a^(2r)/k^(2r+2)
                +a^8/[k^8(a^2+k^2)].

The four moments S0,S2,S4,S6 are evaluated exactly as functions of e^-1 and q=e^-4, with outward constant intervals. Use

    sum_{j>=0} j^p q^j
      =sum_{h=0}^p Stirling(p,h) h! q^h/(1-q)^(h+1),

and expand (2j+1/2)^(2r) with the binomial theorem. All retained terms and the physical (-1)^n sign remain present.

For the omitted S8, a_j<=2(j+1), and

    (j+1)^8 <=(j+1)(j+2)...(j+8)=8! binom(j+8,8).

Since e^-1<1/2 and q<1/16,

    S8 <128*8!/(1-q)^9
        <128*8!*(16/15)^9 <1e7.

The multiplied physical correction remainder is <1024*S8/(n^9*pi^9), hence <1024e7/(3^9*n^9).

Together, both nonprime analytic remainders are bounded by

    13(4/(3R))^8 +1024e7/(3^9 R^9)
       <7.150e-42, R=256000.

No exponential term is dropped without a moment/remainder charge. Nine exact rational direct-denominator checks verify the four-term remainder identity, and the sixth-moment Stirling coefficients are independently checked.

## 4. Higher precision periodic prime evaluation

The adaptive Machin/log/sqrt/weight construction and k-dependent period error are unchanged mathematically, now with working precision at least 512 and a 256-bit n guard. All five prime terms, including q=4's distinct phase and weight, remain physical.

Use 56 fixed-point sine terms. The same exact recurrence proof gives

    sine_rounding <=56*16^56*2^-B,
    sine_remainder <=4^113/113!.

At B>=512 their sum is <1.127e-85. The phase uncertainty is <21*2^-256<1e-70. The directed intervals for the higher nonprime expression, its analytic remainder, every prime uncertainty and outward 160-bit output rounding together have radius <1e-39. The code asserts the tighter phase and radius caps on every action-precision call.

The theorem applies on the whole infinite lattice, with adaptive constants for arbitrarily large integer inputs. Fifty high-precision reference values, including 1025-bit indices, are confirmatory diagnostics and not the proof.

## 5. Propagate only the achieved remote-z component through the model

Let xi=1e-39. Hold the finite physical inputs, pole and raw diagonal fixed, and replace only remote z by this midpoint evaluator. The affected finite-to-remote cross kernel is

    delta B(n,m)=c*delta z_n*m/(n^2-m^2)
               =(c/2)delta Z (H-G).

Thus ||delta B||<=xi, using ||H||,||G||<=pi/2 and c=2/pi. The same holds for B_K: on Far its positive m/(n^2-m^2) kernel is multiplied by 1-(m/n)^(2K) in [0,1], and on Near it is unchanged. Positive-kernel domination preserves the l2 norm bound.

The finite full inverse bounds from v14.210 imply sqrt(G)<5e14 in both sectors. Consequently

    ||delta B_K A^-1/2|| <=tau_z=5e14*xi=5e-25.

The existing inverse-energy model coupling bound is <21, so BOTH Schur cross terms and the quadratic term cost <=42*tau_z+tau_z^2. In the bare off-diagonal D, the remote displacement plus its diagonal restoration changes by <3xi. The raw physical d_n and pole have NOT been evaluated or changed in this comparison.

Therefore the z-only model operator discrepancy is

    epsilon_z <=3xi+42*tau_z+tau_z^2,

and its action on ||y||<=0.002 costs <5e-26. The exact consumer checks this using Fraction arithmetic. This closes this specific scalar uncertainty component despite the huge G; finite RHS rounding, solve residuals, diagonal evaluation, kernel arithmetic and accumulated trial evaluation remain independent obligations.

The optional cached M11 replacement is independent of remote z and does not create a new scalar-z charge. The original C_S_32000 remains fixed.

## 6. Checks, immutable default and scoped CI

The extended module runs the original v14.227 gate again: its complete original 33018-byte JSON is unchanged, including all source-mode intervals. The high-precision mode encloses all 50 independent direct physical values, using the original digamma and 100 exponential terms for diagnostics.

New producer research-notes/suzuki_action_precision_z_gate.py checks the Bernoulli polynomial coefficient sum, S8 bound, analytic remainder, uniform radius and z-only model action charge. Two fresh complete action-gate outputs must match byte-for-byte before publication.

Payload: payloads/action_precision_z_v14_229/action-precision-z-gate.json. 44537 bytes, SHA-256 4437af2f84b24e9adcb01de6b4833abcd0acaf21ec756283b93a103041b39674. The committed payload records all exact intervals and rational operator charges. The scoped .github/workflows/suzuki-action-precision-z.yml replays both unchanged default mode and the complete action gate against pinned prior payloads. CI pending at initial publication.

## 7. Remaining implementation gate and concurrent checks

v14.228's full numerical Near replay and immutable binary freeze completed/success; its receipt is appended separately after all archived file hashes/lengths were checked. Sandbox's explicit v14.227 task for a physical bare-diagonal evaluator remains open. Lane A continues toward an evaluated near/far trial action with actual finite-lift residual certificates and total arithmetic charges.

The action-precision scalar does not itself solve A z=B_K* y or evaluate the degree-2400 polynomial. All finite-lift, evaluated action, stationary scalar and infinite-closure flags remain false.

HANDOFF
target: sandbox
type: audit
parent: v14.229
status: open
action: Audit the order-eight Euler–Maclaurin remainder, four exponential moment formulas/S8 bound, adaptive high-precision scalar intervals and z-only whole-model action charge; verify default-mode byte preservation and replay the 50-case payload.
deliverable: audit-or-specific-obstruction
constraints: The remote-z component is isolated with finite inputs, pole and raw diagonal fixed. No full finite lift or complete D/action is claimed. Preserve both cross terms and the physical q=4/parity content. Continue the bare-diagonal task from v14.227 separately, and read live HEAD/audit before writes.

## 8. Committed-byte and successful scoped CI receipt

Source commit ff5073cb00d0da1022e1943d7baf0f8a512ad579: all six publication files fetched and compared byte-for-byte with direct generated content. Scoped action-precision run [37996855750](https://github.com/PrimeEuler/PrimeEuler.github.io/actions/runs/37996855750), job 114045010221, completed/success. Both complete default-source regression and 44537-byte action-precision output cmp passed, including the 50 physical diagnostics and exact z-only operator/action charges. The separate default-scalar workflow run 37996855709, job 114045010123, also completed/success.

This closes computational replay for the higher scalar precision. It does not substitute for the requested independent analytic audit, physical raw-diagonal evaluation, new finite-lift solves or the final paired stationary certificate.

Receipt live HEAD ff5073cb00d0da1022e1943d7baf0f8a512ad579; no newer v14.230+ ledger observed. Append only this lane's v14.229 receipt with a nonforced expected-head update.
