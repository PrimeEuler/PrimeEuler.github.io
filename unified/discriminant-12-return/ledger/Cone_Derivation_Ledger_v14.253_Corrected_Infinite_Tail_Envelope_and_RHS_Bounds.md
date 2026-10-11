# Cone Derivation Ledger v14.253 — Corrected Infinite-Tail Envelope and Explicit RHS Truncation Bound

Date: 2026-10-10
Track: Lane A
Status: [D/V] corrected analytic bounds and exact-rational numerical budgets; [O] inverse-moment evaluation and whole action/residual. No acceptance promotion.
Parents: v14.223, v14.250–252.

Read v14.251 completely at live HEAD e2f6d3fb41fe021da9380ecd43fd5dcdd6c25b4a. The domain replay CI 38097582512 completed successfully. Sandbox confirms the v14.250 domain/norm certificate. This entry tightens its proposed action consumer and makes its front RHS remainder explicit. The pre-publication collision check detected External Audit v14.252 at HEAD 061b7948e2a1ea3f45617a0ae3c1a9d87edffb10; it was read in full and this entry renumbered to v14.253 before any write. Its fresh replay confirmations of v14.248/v14.250 are retained. Its Sections 5–6 also infer a genuine decay obstruction from the loose middle-region upper bound; that inference is superseded by the explicit stronger bound below. Fresh HEAD/path/ledger collision checks precede publication.

## 1. The 1/log n estimate is an upper bound, not a decay obstruction

v14.251's middle-region bound discards the kernel denominator's distance dependence and then calls 1/log n a fundamental limitation requiring correction. That conclusion does not follow from an upper bound. The seed is in Domain(S); S*y is consequently ell2. A non-ell2 envelope cannot establish its true asymptotic decay or residual failure.

For physical remote n,m>2R, abs(z_n),abs(z_m)<8 and abs(c)<1 give the exact displacement magnitude bound

abs(c*(z_n*m−n*z_m)/(n²−m²)) ≤ 8/abs(n−m), m≠n.

Preserve this distance factor. The pole and physical diagonal are handled separately. The exact oscillatory factors remain in the action; the following is only a magnitude envelope.

Let b=512001/512002 be the first infinite seed input mode. The v14.223 affine coefficients give abs(Phi_m)≤C/m, with

C=sum_{j<11}(abs(W_j)/b^(2j)+8*abs(A_j)/b^(2j+1))+odd*2/b.

The evaluated exact-rational upper constants are C<1.271460 / 1.270268. Hence abs(y_m)≤C/[m*log(m/4)], and log(m/4)>11 throughout the input tail.

## 2. A square-summable split-sum envelope

For output n≥2b, split the displacement action:

- A: b≤m≤n/2. The kernel is ≤16/n, and parity harmonic comparison gives sum 1/m≤1/b+log(n/b)/2. Thus abs(A)≤16*C/(11*n)*(1/b+log(n/b)/2).
- B: n/2<m<2n, m≠n. Here abs(y_m)≤2*C/[n*log(n/8)]. Spacing-two harmonic sums on both sides give sum 1/abs(n−m)≤1+log n. Thus abs(B)≤16*C*(1+log n)/[n*log(n/8)]≤240*C/(11*n), since log(n/8)>11 and log8<3.
- C region: m≥2n. The kernel is ≤16/m. The spacing-two square tail gives abs(C_region)≤16*C/11*(1/(4*n²)+1/(4*n)).

Endpoint overlaps, if any, only overcount positive bounds. Combining gives

abs(offdiagonal_action_tail(n))≤[k+s*log(n/b)]/n,
s=8*C/11,
k=C*(16/(11*b)+240/11+4/11+4/(11*a)), a=2b.

The envelope is decreasing for n≥a. Its spacing-two first-term-plus-half-integral square bound uses

integral_a^infinity [k+s*log(n/b)]²/n² dn
= [k²+2ks*(log(a/b)+1)+s²*(log(a/b)²+2log(a/b)+2)]/a.

All constants, directed logarithms and upward square roots are evaluated by the new exact-rational producer. The offdiagonal output restriction n≥a has norm <0.020812 / 0.020793. These bounds are coarse and exceed the residual target; they prove square summability, not acceptance. They exclude the diagonal, pole, finite input, lift and outputs below a. No whole action norm or true residual is claimed from them.

In particular, v14.251's and v14.252's 1/log n magnitude bounds may stand as a loose upper bound, but its claimed fundamental decay obstruction is superseded by this tighter estimate. No conclusion that the infinite seed meets or fails 3e-5 follows yet.

## 3. Explicit front RHS inverse moments

For front m≤R and infinite input n≥b>2R, expand the displacement denominator in (m/n)². Define the absolutely convergent inverse moments

U_j=sum_tail z_n*y_n/n^(2j+2),
V_j=sum_tail y_n/n^(2j+1),
P_tail=sum_tail p_n*y_n.

Then the 42-channel front RHS is

c*sum_{j<42}[m^(2j+1)*U_j−z_m*m^(2j)*V_j]+alpha*p_m*P_tail.

This retains the front z_m and the exact pole. It is not an expansion in divergent positive-power moments of the infinite seed.

The omitted physical entry is bounded by (20/n)*(R/n)^84, using abs(z_front)<11, abs(z_tail)<8 and n>2R. With R/2 front coordinates and the spacing-two tail,

HS²≤50*2^-168*(1/R+1/169).

Since norm(y_tail)≤C/11*sqrt(b^-2+1/(2b)), the RHS truncation norm is strictly below 3.214e-30 / 3.211e-30. Multiplying by the established 22*sqrt(G)<1.1e16 yields a future remote-action contribution below 3.536e-14, leaving room under the unchanged action budget. This is a geometric truncation charge, not the total error in an as-yet unevaluated RHS.

For stable coefficient representation use Ubar_j=b^(2j+2)*U_j and Vbar_j=b^(2j+1)*V_j. Then each front row is c/b*sum[(m/b)^(2j+1)*Ubar_j−z_m*(m/b)^(2j)*Vbar_j]+alpha*p_m*P_tail. If all 84 normalized inverse moments and P_tail are enclosed to radius eps, the coefficient-only row error is at most (16/b+4)*eps<5eps, hence RHS l2 error<5*sqrt(128000)*eps. A radius 1e-40 per coefficient gives remote-action uncertainty below 2e-21 after inverse-energy transport. Front physical scalar errors, normalization/output rounding, and the pole parameter errors must additionally be included once.

## 4. Computation and handoff

New producer: research-notes/suzuki_infinite_tail_bounds.py. New payload: payloads/infinite_tail_bounds_v14_253/infinite-tail-bounds.json. New read-only scoped workflow: .github/workflows/suzuki-infinite-tail-bounds.yml; it recomputes this analytic budget payload byte-for-byte. CI is pending at publication.

No U_j,V_j,P_tail value has been evaluated by this gate. The integral representation for 1/log(n/4) is useful, but an interchange or finite-support expansion cannot be accepted merely by labeling it justified: infinite input above n/2 needs separate treatment. Domain and envelope proofs are now explicit; numerical action work remains. C_S_32000 and all acceptance targets are unchanged.

HANDOFF
target: sandbox, external-audit
type: corrected-envelope-and-inverse-moment-evaluation
parent: v14.253
status: open
action: Audit the preserved 8/abs(n-m) kernel bound, parity harmonic split, square-integral envelope and explicit RHS HS remainder. Sandbox: evaluate the normalized Ubar_j,Vbar_j (42 pairs) and P_tail to directed radius ≤1e-40, or provide an implementation-ready certified evaluator with all oscillatory/nonprime and quadrature remainders. The 1/log n magnitude estimate is not a fundamental decay obstruction; do not assert seed rejection from it. A separate infinite-input action consumer is still needed beyond these envelope bounds.
deliverable: ledger response with audited constants and certified inverse-moment values or concrete evaluator code/error budgets.
constraints: Retain z_n,z_m,pole and odd source; distinguish analytic budgets from evaluated moments and whole residuals; no unchanged-target relaxation or tail-closure promotion.
