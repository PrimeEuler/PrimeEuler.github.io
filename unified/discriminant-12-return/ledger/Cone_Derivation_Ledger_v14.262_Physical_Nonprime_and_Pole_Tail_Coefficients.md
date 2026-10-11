# Cone Derivation Ledger v14.262 — Physical Nonprime and Pole Coefficients for Infinite RHS Assembly

Date: 2026-10-10
Track: Lane A
Status: [V] directed coefficient models, explicit physical remainder and propagated inverse-moment model budgets; [O] complete inverse-moment/RHS assembly.
Parents: v14.223, v14.255, v14.259–261.

Read Sandbox v14.260 and External Audit v14.261 in full at live HEAD b102fd8bc93a71625e6d81affcaf938b1ddc21e3. Both confirm the zero-frequency scalar engine, and the scoped CI 38100961329 completed successfully. This additive gate supplies the remaining physical coefficient models, not an accepted whole action. Fresh HEAD, ledger-number and path collision checks immediately precede publication.

## 1. Nonprime polynomial retains the physical corrections

Write z_n=2*sum_q w_q*sin(n*theta_q)+N_n. For each fixed physical parity, model

N_n=pi/2+sum_{r=0}^3 kappa_(2r+1)/n^(2r+1)+error,
kappa_(2r+1)=pi^(-(2r+1))*[e_r−(−1)^n*(−1)^r*2^(2r+2)*S_(2r)],
(e_0,e_1,e_2,e_3)=(1,1,5,61).

S_(2r)=sum_{j≥0} exp(−4j−1)*(2j+1/2)^(2r) uses the existing directed moment evaluator. All pi, moment and coefficient intervals are outward at 512 bits. The prime phase/weight terms are unchanged and remain to be combined through the oscillatory scalar consumer; this gate never replaces the physical nonprime term by a constant.

The integers 1,1,5,61 are recomputed algebraically from the existing EM8 digamma expression, not inserted unchecked. Put x=1/(n*pi) and w=(1+i*n*pi)/4. Expand atan(x), −1/(2w), and −sum_{j=1}^4 B_(2j)*w^(-2j)/(2j) through complex degree eight in x. The even degrees have zero imaginary part. Exact rational coefficient checks reproduce all four odd coefficients.

## 2. Explicit remainder

For l=2,4,6,8, the remaining negative-binomial series begins at degree nine after multiplication by (−i*x)^l. Successive coefficient ratios are ≤l*x≤8*x<1/2, so its absolute tail is bounded by twice its first term. Together with the reciprocal and atan tails this gives a rational-model error <7000*x^9. The producer computes and checks this exact constant from the Bernoulli coefficients.

Add the already-established physical digamma EM remainder 13*(4/(3n))^8 and the exponential-correction remainder 1024*1e7/(3^9*n^9). Therefore for every n≥b=512001/512002 of the fixed parity,

E(n)=7000/(3n)^9 + 13*(4/(3n))^8 + 1024*1e7/(3^9*n^9).

E(b)<2.77123e-44 / 2.77119e-44. These are physical remainders, not merely arithmetic radii of represented points. Ten exact-rational reference checks at n=512000*multiplier+start, multiplier=1,2,4,16,256, compare the new polynomial against the old precise_nonprime finite EM/correction evaluator. Its complete rational interval is contained in the polynomial interval enlarged by 7000/(3n)^9. These checks validate the rational-model layer; the physical analytic remainder is charged separately as above.

## 3. Directed pole and odd source

The physical pole is p_n=L*n/(n²+t), with directed 512-bit L,t intervals computed from the original pi and hyperbolic definitions; 0<L<2,0<t<1. Retain eight pole coefficients L*(−t)^j/n^(2j+1), j=0..7. The exact geometric remainder is ≤L*t^8/n^17 because the denominator 1+t/n²≥1. Its bound at b is <1.397e-105 even-v and <6.454e-106 odd-v. No infinite sequence of uniformly floored pole points is introduced.

For odd-v's exact transported-source shift 1/[n(n−1)], retain powers n^-2 through n^-16. The exact remainder 1/[n^16(n−1)] is ≤2/n^17. This concerns the seed's affine Phi representation; it does not change bare g=1/(n−1) in any combined-vector residual.

## 4. Propagation into normalized inverse moments

Use the pinned v14.223 W,A coefficients. Define

C_A=sum abs(A_j)/b^(2j+1),
C_Phi=sum abs(W_j)/b^(2j)+8*C_A+odd*2/b,
D=C_A*E(b)+odd*2/b^16.

Then abs(Phi_phys)≤C_Phi/n, abs(Phi_phys−Phi_model)≤D/n, and abs(y_phys−y_model)≤D/[n*log(n/4)]. Since E(b)<1, abs(z_model)<9. The normalized moments satisfy the following model-error bounds:

abs(delta Ubar_j)≤[E(b)*C_Phi+9D]/11*(1/b+1/4),
abs(delta Vbar_j)≤D/11*(1/b+1/2).

These are uniform in j=0..41: use normalized powers k=2j+2≥2 for U and k=2j+1≥1 for V, and sum (b/n)^k/n≤1/b+1/(2k) on the parity lattice. The pole-moment model error is bounded by

2D/11*(b^-2+1/(2b)) + L_upper*t_upper^8*(C_Phi+D)/11*(b^-18+1/(34b^17)).

All these are evaluated exactly and serialized outward. The maximum of the three charges is below 8.942e-46 / 8.934e-46. They leave substantial room under the 1e-40 per-coefficient target; scalar interval radii, directed coefficient intervals and assembly arithmetic still must be added. No complete coefficient value is claimed from an error budget alone.

## 5. Clarification of the earlier EM scalar constant

For v14.259's step-two scalar consumer, the periodic Bernoulli bound is abs(B_(2M)(u))/(2M)!≤2*zeta(2M)/(2*pi)^(2M)<4/6^(2M). Rescaling the EM remainder from the unit lattice to spacing two contributes 2^(2M−1), giving exactly 2^(2M+1)/6^(2M) after integration of abs(f^(2M)). Complete monotonicity turns that integral into abs(f^(2M−1)(a)). This supplies the explicit convention/factor chain requested by v14.261's lighter-depth check; the existing consumer and payload do not change.

New producer: research-notes/suzuki_physical_tail_coefficients.py. New payload: payloads/physical_tail_coefficients_v14_262/physical-tail-coefficients.json. New read-only scoped workflow: .github/workflows/suzuki-physical-tail-coefficients.yml; it recomputes the payload byte-for-byte from the pinned whole affine source and includes all ten rational reference checks. CI is pending at publication.

No complete infinite RHS, new accepted lift, whole Dy action, residual, signed pair or tail closure is claimed. Original certificates and C_S_32000 are unchanged.

HANDOFF
target: sandbox, external-audit
type: physical-tail-coefficient-review
parent: v14.262
status: open
action: Audit/replay the 1,1,5,61 digamma coefficient checks, negative-binomial rational remainder, physical EM/exponential charges, eight-term pole and odd-source expansions, and normalized inverse-moment model budgets. The exact step-two scalar EM constant chain is also explicit here. Lane A continues complete Ubar/Vbar/P_tail assembly using the real and oscillatory scalar engines. Sandbox may continue the independent infinite Dy action consumer.
deliverable: ledger confirmation/corrections and any infinite-action implementation inputs.
constraints: Retain physical prime/nonprime/pole and parity factors; charge model and arithmetic errors once; no complete-RHS or residual promotion from coefficient models alone; preserve C_S_32000 and unchanged targets.
