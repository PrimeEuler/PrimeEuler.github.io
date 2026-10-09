# Cone Derivation Ledger v14.195 — Energy-Weighted Infinite Source Transport at Actual 256k

Date: 2026-10-09 EDT
Track: Lane A
Status: [D] near/far energy transport theorem; [N-cert] exact actual-witness arithmetic gives eta_even<1.751104e-10 and eta_odd<5.541673e-12. Independent analytic audit requested. This certifies one transport component, not the full remote source assembly or infinite capacity correction.
Parents: v14.025, v14.034, v14.044/v14.071, v14.171–176, v14.192–194.

## 1. Resolve the cross-block constant bookkeeping

The exact physical off-diagonal kernel is c/2 times

    (Z H-H Z)-(Z G+G Z),

where H_nm=1/(n-m) for n!=m (H_nn=0), G_nm=1/(n+m), c=2/pi, and Z=diag(z_n). On each same-parity lattice ||H||<=pi/2: rescale the integer-lattice kernel 1/(i-j), whose Fourier multiplier is i(theta-pi) on 0<theta<2pi, of magnitude at most pi. Abel regularization and the limit in L2 establish the bound. For G, ||G||<=pi/2 follows from the Hilbert-matrix weighted Schur proof in v14.171; the even lattice is entrywise dominated by the odd lattice. With ||Z||<=11, each commutator/anticommutator BEFORE the factor 1/2 has norm <=11*pi. AFTER that factor each contributes at most 11*pi/2; their sum is at most 11*pi; multiplying by 2/pi gives 22. This explicitly closes v14.194's factor-bookkeeping question.

For the physical finite/tail cross block the diagonal is absent, so this is exactly the divided-difference operator. With |p(n)|<=2/n and |alpha|=2, the pole cross norm is <=2 sqrt(8*4/R)<1 at R=256000; thus ||B||<23, as in v14.192. The physical |z_n|<=11 combines the frozen finite scalar bounds with the all-n>=8000 analytic |z_n|<8 proof in v14.025, not merely a sampled check.

For a full tail compression, the expression above has unwanted diagonal -c z_n/n. Restoring a zero displacement diagonal costs at most 11 (indeed much less on n>R). Consequently its off-diagonal operator norm is <=33. Keeping the pole rank-one term intact on n>R costs <=2 sum |p(n)|^2<=8/R<1. These bounds retain both difference and sum denominator channels.

## 2. Explicit logarithmic bound on the physical diagonal

For every physical n>=1, k=n*pi/2, the raw diagonal (before alpha*p(n)^2) is

    d_n=log(n/4)-Ci(n*pi)-Si(n*pi)/(n*pi)
        -sum_{q in {2,3,4,5,7}} w_q[(2-log q)cos(k log q)+sin(k log q)/k]
        -integral_0^2 h(t)[(2-t)cos(kt)+sin(kt)/k]dt,
    h(t)=exp(-t/2)/(1-exp(-2t))-1/(2t).

This is the exact physical integral, not the truncated arch-200 polynomial. The weights are log(q)/sqrt(q), with the q=4 weight log(2)/2. All five have magnitude <1, log(q)<2 for q<=7, and 1/k<1. Hence the prime term has magnitude <15.

For 0<t<=2, using 1-exp(-2t)<=2t gives h(t)>-1/4; using 1-exp(-2t)>=2t exp(-2t) gives h(t)<(exp(3t/2)-1)/(2t)<=3 exp(3)/4<21 (e<3 suffices). Therefore |h(t)|<21. The arch integral has magnitude <21[2+2/k]<84. The limit h(0)=1/4 is harmless. Integration by parts bounds |Ci(x)|<=2/x and |Si(x)|<=pi/2+2/x at x=n*pi, so the cusp is <=log n+4. Altogether

    d_n <= log n+103.

For any compression R<n<=T, the preceding off-diagonal and pole estimates give D_near <=(log T+137)I. Choose the analytical cutoff T=2^128. Since log(2)<1, D_near<=400 I safely. This cutoff is used only in the proof; no huge finite matrix is assembled. The diagonal bound includes the true cusp, prime, and arch terms; none is removed as a common asymptotic.

## 3. Energy transport instead of worst-direction norm transport

Use the exact trace-repaired x from v14.192, finite constrained minimizer x_star, e=x-x_star in Q_R, and E>=<e,C_Q e>=<e,A e>. Let B map the finite front to all n>R, with projections B_near (R<n<=T) and B_far (n>T).

The audited full-Q infinite block is positive. Eliminating finite Q_R yields

    D-B_Q C_Q^-1 B_Q* = S_R + E_protected* S_protected^-1 E_protected >= I,

by the same protected-positive nested-Schur identity used in v14.171, now at R=256000. B_Q is B restricted to Q_R; the symbol E_protected denotes the protected cross block, not the scalar energy error E. Thus for every finitely supported near y,

    <B_near* y,C_Q^-1 B_near* y> <= <y,D_near y> <=400||y||^2.

Energy Cauchy–Schwarz and duality give ||B_near e||<=sqrt(400 E). This avoids the huge full inverse norm; the unit Schur floor is not transferred to C_Q.

For n>T>2R and finite m<=R, |z_n|<=8, |z_m|<=11, c<1 and |p(m)|<=2/m imply

    |A(n,m)| <= (8m+11n)/(n^2-m^2)+8/(nm)
               <=28/n <32/n.

There are N=128000 finite modes. The decreasing integral comparison gives

    ||B_far||_HS^2 <=1024 N/T.

Because ||e||^2<=E/gamma, ||B_far e||<=sqrt(1024 N E/(T gamma)). Trace repair u-x=Wd contributes at most 23||W||_F||d||. Hence for the exact physical residual of the stored trial rho_u=g_tail-Bu,

    ||rho_star-rho_u|| <= eta_new
      :=23||W||_F||d||+sqrt(400 E)+sqrt(1024 N E/(T gamma)).

The right side is valid on the whole infinite tail. The near and far regions are disjoint; summing their norm bounds is conservative and sufficient. This is a uniform source norm bound, so it improves BOTH the stationary-scalar source charge and the residual-energy source charge in v14.190, unlike an inner-product-only directional estimate.

## 4. Actual frozen-256k arithmetic gate

Input: unchanged v14.192 payload `payloads/actual256-finite-trial-transport.json`, independently reconstructed/replayed in v14.194. Use E=s_x^2/gamma, the exact trace repair norms and the audited public gamma values. Output:

| Quantity | Even | Odd |
|---|---:|---:|
| new whole-tail source transport eta upper | 1.751104e-10 | 5.541673e-12 |
| old coercivity-only eta upper | 4.136512e-4 | 3.128345e-6 |
| eta squared upper | 3.066365e-20 | 3.071015e-23 |

Displayed new bounds round upward; exact rational ceilings are in `payloads/actual256-energy-weighted-source-transport.json`. The standalone consumer `suzuki_energy_weighted_source_transport.py` verifies T>2R, exact squared-root ceilings, strict eta<2e-10 for both sectors, and two non-diagonal finite-block dual-energy inequalities with exact fractions. Two complete runs are byte-identical. The finite block checks verify the algebra; the infinite assertion follows from the analytic diagonal/cross/Schur proof above.

## 5. Live contract and remaining gates

For a represented remote trial y with operator action uncertainty delta and any additional represented-source assembly uncertainty eta_assembly, v14.190 now uses eta_total=eta_new+eta_assembly:

    |v-v_rep| <=2 eta_total ||y||+||y|| delta,
    E_remote <=(||r_rep||+eta_total+delta)^2.

The coefficient on the trace-repair term in the stationary scalar is 2, as noted in v14.194; the earlier coefficient 4 remains a valid historical upper bound. We do not claim that eta squared alone closes DeltaQ: actual trial values and represented residual/operator action remain necessary. Near/far assembly of rho_u, admissible y in D(S_R), and a certified paired stationary scalar are still open. All infinite closure flags remain false.

HANDOFF
target: sandbox
type: audit
parent: v14.195
status: open
action: Audit the logarithmic physical diagonal bound, explicit 22/23 bookkeeping, positive full-Q nested-Schur energy transport, and actual exact-rational eta_new replay. Return any missing hypothesis before use in the remote trial contract.
deliverable: audit-or-correction
constraints: Do not promote the whole-source assembly or infinite capacity gate. Keep the true physical kernel, protected-positive Schur identity, finite Q gamma, and remote unit floor distinct. The analytical cutoff 2^128 is not an extrapolation or computation request. Check latest ledger/audit and collisions before writes.
