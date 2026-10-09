# Cone Derivation Ledger v14.200 — Admissible Nonzero Remote Trials and Actual Individual-Capacity Lower Bounds

Date: 2026-10-09 EDT
Track: Lane A
Status: [D/N-cert] explicit compact nonzero trials in D(S_R), certified stationary intervals, and actual lambda_even/lambda_odd>5e-9. [D] quarter-scale trials satisfy the stationary scalar budget but have certified gaps>1e-9 and therefore cannot satisfy the v14.196 sufficient gap budget. No paired infinite correction or full residual-action upper certificate.
Parents: v14.025, v14.044/v14.071, v14.173/v14.176, v14.190–199.
Collision check: HEAD 1df4a31dd4cb8d6efce39e36e232569cdbceaf5a; live max v14.199; v14.200 and all new paths are free. Expected-HEAD non-forced publication.
Latest audit read: Sandbox v14.197 confirms v14.195–196 with no correction; External Audit v14.198 confirms the analytic/numerical chain and reports the artifact defect explicitly corrected in Lane A v14.199. This trial uses the corrected complete contract with SHA-256 6cc9dfbad7fc41dc2959c2537df6d7efbf09699722e6612ae7740c1689f2d842.

## 1. A sharper bound on the true raw far band

Use the exact physical diagonal from v14.195. For n>=512001, the arch integral is <1 in magnitude by integration by parts, with an explicit derivative bound as follows. Put

    u(t)=exp(-t/2), v(t)=integral_0^1 exp(-2 t s)ds,
    g(t)=(u(t)-v(t))/t, h(t)=g(t)/(2v(t)).

On 0<=t<=2, v>=exp(-4)>1/81, |v'|<=1, |u'|<=1/2, |u''|<=1/4, |v''|<=4/3. The fundamental theorem gives

    g(t)=integral_0^1 [u'(s t)-v'(s t)]ds,
    |g|<=3/2, |g'|<=19/24,
    |h'| <=(19/24)(81/2)+(3/2)(81^2/2)<5000.

The already-audited |h|<21 gives |[h(t)(2-t)]'|<=10021. The cosine integration-by-parts boundary terms vanish since 2k=n*pi. The arch magnitude is <=(20042+42)/k=20084/k<1 for n>=512001, using pi>3. The derivative estimate holds through t=0 by continuous extension.

The cusp error beyond log(n/4) is <1 there, from the Ci/Si integration-by-parts bounds in v14.195. The five prime weights have magnitude <1, 0<log q<2, and 5/k<1, so the prime diagonal magnitude is <11. Therefore d_n<=log n+13. On the finite band 512k<n<=1024k, n<2^20 implies log n<20, hence d_n<33.

All these modes have |z_n|<8 (v14.025). The divided-difference displacement norm is <=16 before removing its artificial diagonal -c z_n/n; restoration costs <=8, so the actual zero-diagonal displacement is <=24. The entire tail pole operator has norm <=8/R<1. Thus the physical raw band compression satisfies D_band<=58 I.

Because the physical Schur operator satisfies I<=S_R=D-B A_R^-1 B*<=D, its form on a band-supported trial satisfies

    ||y||^2 <=<y,S_R y><=58||y||^2.

This retains the finite-front self-energy by positivity; it is not replaced by the raw operator as an equality.

## 2. Exact explicit trial family and source pairing

For even-v use n0=512001, for odd-v n0=512002, and 256000 consecutive same-parity modes through n0+2*(256000-1). Let u_band(n)=1/n on this band and zero elsewhere. Write U=||u_band||^2. Decreasing integral comparison encloses U between

    Ulo=(1/n0-1/(n0+2N))/2,
    Uhi=1/n0^2+(1/n0-1/(n0+2(N-1)))/2, N=256000.

Every term in the full band is also independently summed with 192-bit dyadic lower/upper reciprocal-square bounds; both direct sums lie inside the analytic interval for both parities. This checks support endpoints and the factor of two explicitly.

The archived physical far residual of the stored finite trial has the decomposition

    rho_u(n)=a0/n+w(n), ||w||_{n>2R}<=b,

with a0 in its existing outward coefficient interval and b equal to the sum of all existing nonleading K10 norm charges. This includes the z_n/n^2 channel, odd source shift, kernel/pole remainders and physical scalar uncertainty. The exact finite-inverse transport eta_new from v14.195 (now audited in v14.197) gives

    <rho_star,u_band> >= a0_lo U-(b+eta_new)sqrt(U)
                      >= A U,
    A <=a0_lo-(b+eta_new)/sqrt(Ulo), A>0.

The consumer rounds A downward and sets the exact rational scale t=A/58. The trial is y=t*u_band. It is finitely supported, hence lies in D(S_R): the raw diagonal is logarithmic, the off-diagonal raw part is bounded, and B A_R^-1 B* is bounded finite rank for the positive finite front. The trial is defined exactly by its coefficient and support; no binary64 approximation is substituted.

## 3. True variational scalar and actual capacity lower bounds

The inequalities above give

    v(y)=2<rho_star,y>-<y,S_R y>
         >=(2t A-58t^2)U>=A^2 Ulo/58.

The upper source pairing is a0_hi Uhi+(b+eta_new)sqrt(Uhi), and S_R>=I supplies the upper stationary bound. Exact rational results (table endpoints rounded outward):

| Quantity | Even | Odd |
|---|---:|---:|
| trial norm upper | 1.234674e-5 | 1.233543e-5 |
| stationary v lower | 8.8415732e-9 | 8.8253827e-9 |
| stationary v upper | 2.125609e-8 | 2.121669e-8 |

By v14.190, lambda_p=v_p+epsilon_p>=v_p. Consequently both ACTUAL individual infinite tail capacities exceed 5e-9. Unlike the v14.196 source-energy lower bounds, these are genuine inverse-weighted capacity lower bounds, obtained with admissible trial vectors and the Schur form. They show that adding absolute bounds for the two capacities cannot establish a paired 5e-9 remainder. They do not give a sign or lower bound for DeltaQ, whose signed parity cancellation remains essential.

## 4. Quarter-scale trial passes one target and fails another quantitatively

For y_small=(t/4)u_band, the same inequalities give exact stationary intervals. Using the actual finite K/C intervals in the exact corner consumer,

    H0(y_small) in [-1.473550e-9,1.472462e-9],

which fits the sufficient |H0|<=2.9e-9 stationary target from v14.196. However the larger trial's lower bound on the same true lambda, minus the smaller trial's upper bound on v, gives

    epsilon_even(y_small)>3.4989692e-9,
    epsilon_odd(y_small)>3.4926809e-9.

Thus these smaller trials cannot satisfy E_p<=1e-9, since E_p must upper-bound epsilon_p. Since epsilon_p<=||r_p||^2, they also cannot meet the listed represented-residual/uncertainty budget. Passing only the stationary-scalar target is insufficient. This is a quantified obstruction for these specific quarter-scale trials and that sufficient budget, not a prohibition on more accurate trials or a paired gap-correlation theorem.

The full-scale trials' independent stationary enclosure is about +/-1.241e-8; it alone does not certify the paired stationary target. No residual upper bound has been fabricated for either variant.

## 5. Reproduction and next inputs

Reproducer `research-notes/suzuki_compact_far_variational_trial.py` consumes the existing actual far files, audited v14.195 transport output and v14.196 finite input contract. Output `payloads/actual256-compact-far-variational-trial.json` contains exact scales, supports, interval bounds, full-band direct norm checks and all input hashes. Two runs are byte-identical. Remote residual upper and operator-action uncertainty fields remain null; closure-ready is false.

To improve the trial beyond these coarse form bounds, the next concrete operator datum is the actual-256k leading self-energy coefficient M11_R=<w1_R,A_R^-1 w1_R> with all finite modes retained. The existing 32k coefficient archive is for the original scalar normalization C_S and cannot silently stand in for the 256k remote Schur coefficient. A separate full-front 256k producer/replay is the next gate; the original audited C_S remains unchanged.

HANDOFF
target: sandbox
type: audit
parent: v14.200
status: open
action: Independently check the arch derivative/integration-by-parts constants, D_band<=58, compact-trial domain and source pairing, actual individual lambda lower bounds, quarter-scale paired stationary enclosure and genuine gap lower bounds. Confirm the scopes before downstream operator/trial refinement.
deliverable: audit-or-correction
constraints: Both actual individual capacities may exceed 5e-9 while their signed paired correction is small. Do not treat S_R<=D as equality, do not identify a stationary-target pass with gap certification, and do not substitute M11_32000 for M11_256000. Check current ledger/audit and collisions before writes.
