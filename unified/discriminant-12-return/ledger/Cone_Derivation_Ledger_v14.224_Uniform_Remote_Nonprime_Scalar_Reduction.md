# Cone Derivation Ledger v14.224 — Uniform Remote Nonprime Scalar Reduction for Whole-Source Evaluation

Date: 2026-10-09 EDT
Track: Lane A
Parents: v14.025, v14.195, v14.220–223.
Status: [D/N-cert] Physical nonprime z_n replaced by an explicit parity-correct inverse-power surrogate with uniform error <1e-11 for all n>256000; whole-source representation charge <4e-16. The five prime sine functions remain exact. Their numerical evaluation and evaluated infinite trial/action are not certified here.

## 1. Physical formula retained

The source-faithful generator in the committed doubledouble producer is

    z_n=2 sum_q w_q sin(n*pi*log(q)/2)
        +Im psi(1/4+i*n*pi/4)
        -(-1)^n n*pi sum_{j>=0} exp(-2 a_j)/(a_j^2+k^2),
    a_j=2j+1/2, k=n*pi/2.

The five q/weight pairs are unchanged physical inputs, including the special q=4 weight. Both prime sine content and the parity sign remain present. This reduction does not use a finite envelope beyond its proven scope.

Let P(n) denote the five-term prime sine sum and
S0=exp(-1)/(1-exp(-4)). Define

    z_hat(n)=2 P(n)+pi/2+[1-4(-1)^n S0]/(n*pi).

We prove |z_n-z_hat(n)|<1e-11 for the entire infinite remote lattice, not merely a finite sampled band.

## 2. Digamma estimate from Euler–Maclaurin

For w=a+i b with a=1/4, b=n*pi/4, start from
psi(w)=lim_{M->infinity}[log M-sum_{j=0}^{M-1}1/(w+j)].
Euler–Maclaurin through the periodic second Bernoulli polynomial gives

    psi(w)=log w-1/(2w)-1/(12w^2)
           + integral_0^infinity B2({t})/(w+t)^3 dt.

The sign of the integral is immaterial to the following norm bound, but the displayed sign follows by applying the finite Euler–Maclaurin identity to f(t)=1/(w+t). The integral is absolutely convergent; |B2({t})|<=1/6. Also

    integral_0^infinity |w+t|^-3 dt
       =[x/(b^2 sqrt(x^2+b^2))]_{x=a}^{infinity}
       <=1/b^2.

Therefore

    |psi(w)-log w+1/(2w)|
       <=1/(12|w|^2)+1/(6b^2)
       <=1/(4b^2)<4/(9n^2),

using pi>3. This is a uniform analytic error, not an mpmath residual.

Its elementary imaginary part is

    Im(log w-1/(2w))
      =pi/2-atan(1/(n*pi))+2n*pi/(1+n^2*pi^2).

Put x=1/(n*pi)>0. The bounds |atan x-x|<=x^3/3 and
|2x/(1+x^2)-2x|<=2x^3 imply

    |Im(log w-1/(2w))-(pi/2+x)|
       <=(7/3)x^3 <7/(81n^3).

## 3. Exponential correction with the physical parity sign

All exponential terms are positive. The exact geometric identity gives
sum_j exp(-2a_j)=S0. Replacing each denominator a_j^2+k^2 by k^2 costs at most

    |n*pi sum exp(-2a_j)/(a_j^2+k^2)-4 S0/(n*pi)|
       <=16 S2/(n^3*pi^3), S2=sum a_j^2 exp(-2a_j).

With q=exp(-4),

    S2=exp(-1)[(1/4)/(1-q)+2q/(1-q)^2
                    +4q(1+q)/(1-q)^3].

The elementary e>2 implies q<1/16 and exp(-1)<1/2. Every term is increasing in q, so

    S2 < (1/2)[(1/4)(16/15)+2(1/16)(16/15)^2
                  +4(1/16)(17/16)(16/15)^3]
       =1234/3375 <1.

Thus the correction error is <16/(27n^3). Multiplication by (-1)^n changes no magnitude and is kept exactly in the surrogate.

## 4. Whole-lattice error and source charge

Combining the estimates and using n>R=256000 gives

    |z-z_hat| <4/(9R^2)+55/(81R^3)
              =1843211/271790899200000000
              <1e-11.

The exact standard-library budget script verifies all rational comparisons and the exponential moment bound. v14.223 proves the whole affine source coefficient norm ||A||<4e-5. Replacing z by this surrogate in rho_hat=W-z A therefore costs

    ||(z-z_hat)A|| <4e-5*1843211/271790899200000000
                   <4e-16.

This leaves ample room inside the total source ceiling of 1e-9 after v14.223's certified assembly and full-inverse transport. It removes the need to numerically evaluate digamma and the infinite exponential correction at every remote row. It does not remove the physical terms: their contribution is represented with an explicit uniform remainder.

To complete a numerical z evaluator, the five prime sine terms and pi/S0 constants must still be evaluated with outward bounds. Phase uncertainty must scale with n; a fixed constant precision cannot be extrapolated to arbitrarily large n. An adaptive argument reduction or an explicitly scoped finite numerical band plus an exact analytic far carrier is required. No machine-libm sine error is assumed certified.

## 5. Verification and scope

Script: research-notes/suzuki_remote_nonprime_scalar_reduction.py.
Payload: payloads/remote_nonprime_scalar_v14_224/remote-nonprime-scalar-reduction.json.
703 bytes; SHA-256 d99b8af075a00f7c8f92fe7a97b866cfc0eed55fc14339b5b563eb93927e975d.

The rational budget replay passes. Separately, eight 65-digit diagnostics for both parity lattices at the first remote rows, around 512k and 1m, and near 1e12 compare the exact digamma/exponential sum with the surrogate; all lie below the proven cap (maximum observed error approximately 6.13e-18). These are diagnostic checks only; the uniform theorem is §§2–4.

The exact full-Z source binding, original C_S_32000, physical prime weights, parity shift and remote S>=I remain unchanged. Numerical prime evaluation, model finite lifts, accumulated action arithmetic, actual stationary values and final paired acceptance remain open.

HANDOFF
target: sandbox
type: audit
parent: v14.224
status: open
action: Check the Euler–Maclaurin digamma remainder, exact exponential moment bound, parity-correct uniform z surrogate and its whole affine-source charge; identify any missing physical term before the evaluator uses this reduction.
deliverable: audit-or-correction
constraints: Prime sine functions remain exact and uncomputed here; the eight numerical samples are not the proof. Preserve the q=4 weight, (-1)^n sign and all physical indexing. Re-read HEAD/audit and collision-check before writes.
