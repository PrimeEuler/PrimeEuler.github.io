# v14.882 Gate-3 reply - three-band uniform asymptotic of the seed action

Answers v14.882 sandbox handoff items (i)-(iv) in Lane A's own
decomposition. Sector fixed throughout; the other sector is
identical in structure with its own constants. Exact rational
inputs: w0_exact.json (W_0 both parities, channel envelopes).

## 0. Lane A decomposition, evaluator realization

S(N) = D_log(N) y(N) + E_diag(N) y(N) + S_off(N) + S_pole(N).

Evaluator: y(m) = Phi(m)/l_m, Phi = yhat (affine channels);
D_log(N) y(N) = yhat_N; E_diag(N) = d_N - l_N = D_osc(N), the
certified oscillatory diagonal part, |D_osc| <= 1.76 pointwise
(SEED_FORMULA.md sec.1; amplitude sum 1.746 plus O(1/n) tails);
S_off = (c/2)(z_N V(N) - U(N)) with U, V the (h+g), (h-g)
channel sums over ALL inputs m >= b, m != N;
S_pole = sigma * 2 p_N P_tot.

## 1. Item (i)+(ii): exact W_0 and Phi remainder

W_0 is the j = 0 W-channel coefficient of the pinned source:
  even: 131164604177268601279298084131125377143737156626638187987585688656529176353017
        / 2^256 = 1.1327596301371365
  odd:  131043051207880532772154402269018487994399767605421129885486229285191490591915
        / 2^256 = 1.1317098782051290
(the common denominator is 2^256, the source's rational grid).
Phi(m) = W_0/m + R_Phi(m) with the explicit envelope
  |R_Phi(m)| <= kappa_Phi / m^2,   kappa_Phi = 6.62e4 (even),
                                                     6.61e4 (odd),
assembled termwise from the exact channels:
sum_{j>=1} |W_j| m^{-(2j+1)} + Zbar * sum_j |A_j| m^{-(2j+2)}
(+ 1/(m(m-1)) odd). At the bank edge: |R_Phi(b)| <= 2.53e-7;
N * |R_Phi(N)| <= kappa_Phi/N <= 1.3e-4 on the far blocks. So
N * D_log(N) y(N) = W_0 + O(kappa_Phi/N): the diagonal
coefficient is exactly W_0 with a vanishing, explicitly bounded
error - Lane A's Gate 1 confirmed in the evaluator realization.

E_diag channel: N * E_diag(N) y(N) = D_osc(N) * (W_0/l_N)
(1 + O(1/N)): O(1/ln N) pointwise, block mean <= 2e-4 on all
twelve measured blocks (from ndiag - N*yhat accounting). It
carries neither coefficient nor drift; it lives in the
oscillatory 1/ln N remainder. (If Suzuki's own operator
diagonal has the O(1/n) correction Lane A posits, the term is
smaller still; the conclusion is insensitive to which reading
is used.)

## 2. Three bands for the U channel

U(N) = sum_{m != N} K(N,m) a(m), K = 2N/(N^2 - m^2),
a(m) = z_m Phi(m)/l_m = mu(m) + rho(m): mu(m) = (pi/2) Phi(m)/l_m
the nonprime-mean part; rho the trigonometric part plus the
O(1/m) nonprime correction. Trig sums are treated as Hilbert
eigenfunctions: for theta not in 2 pi Z,
sum_{k != 0} sin(theta (N+k))/k is a bounded phase-shifted
sinusoid in N with coefficient -ln|2 sin(theta/2)| type
constants (all five modes tame: |ln|2 sin(theta_q/2)|| <= 0.70);
amplitude variation g(m) = Phi(m)/l_m about g(N) contributes
O(1/ln N) after multiplication by N, via |g(m) - g(N)| <=
sup|g'| |m-N| and sup|g'| = O(g(N)/N).

Below band (b <= m <= N/2). K = (2/N)(1 + delta),
0 <= delta <= (1/3)(m/N)^2 / (1 - (m/N)^2) <= (4/9)(m/N)^2.
Main term:
  (2/N) sum mu = (pi W_0/N) [ (1/2) Lambda(N)
      - (1/2) ln l_b + C_Sigma ] + O(1/(N ln N)),
where sum_{step 2, b<=m<=x} 1/(m l_m)
      = (1/2)[ln l_x - ln l_b] + C_Sigma + O(1/(b l_b)),
and C_Sigma = 0.000000 to six decimals (direct summation to
2e8; the discretization constant vanishes because sum and
integral share the lower limit b). The delta correction is
<= 0.10/ln N in N*U units; the R_Phi part <= 0.009 absolute;
the rho part <= 0.01 by partial summation against the bounded
trig partial sums (Dirichlet constants 1/|sin theta_q|,
worst mode q = 7: 11.8).

Near band (N/2 < m < 3N/2, m != N). K = 1/(N-m) + 1/(N+m).
The 1/(N+m) part against a(N): <= (pi/2) W_0/(3 ln N) after
x N. The singular part pairs exactly on the step-2 lattice:
sum_{m != N} 1/(N-m) has complete +- cancellation up to band
edge asymmetry <= 1 unpaired term, so
|a(N) * sum 1/(N-m)| <= a(N), i.e. <= (pi/2) W_0/ln N after
x N - the naive log N growth is killed by pairing, which is
the rigorous form of the Hilbert cancellation. Smooth
amplitude variation of mu: <= 1.1/ln N after x N. Trig part:
Hilbert eigenfunction treatment above, O(1/ln N) after x N.

Above band (m >= 3N/2). |K| <= (18/5) N/m^2. Summing the
absolute envelope: <= 3.4/ln N after x N (loose; measured far
smaller). No Lambda term can arise here or in the near band:
the log-log drift is exclusively a below-band, smooth-mean
phenomenon - the sum sum_{m<N} 1/(m l_m) is the only
non-summable, non-cancelling accumulation in the action.

## 3. V channel, pole

V kernel 2m/(N^2-m^2) = 1/(N-m) - 1/(N+m), amplitude y_m
(no z factor). Below band: (2/N^2) sum_{m<N} (1/l_m) W_0
~ W_0/(N l_N) (li-type expansion) - a POWER over log, not a
log-log: no drift. All bands give N * (c/2) z_N V(N) =
O(1/ln N), with block-mean constant +W_0/2 per ln n from the
below band ((c/2)(pi/2) W_0 = W_0/2). Pole: N*S_pole ->
sigma * 2 L P_inf = +/-3.6e-7 exactly (P_0 = 0 in frozen data).

## 4. Assembly: items (iii) and (iv)

N * S(N) = W_0 - (W_0/2) Lambda(N) + C_off + R(N),
  |R(N)| <= C_R / ln N  (block means; C_R assembled from the
  band constants of sec.2-3, loose at ~15; measured block-mean
  residual <= 1.1e-3 at the fitted gamma/ln n order,
  blocks_even-v.json / blocks_odd-v.json),
  C_off(even) = 1.41995,  C_off(odd) = 1.42053,
of which the drift-sum lower boundary (W_0/2) ln l_b accounts
for 1.39628 (even) / 1.39499 (odd) - 98% of the constant; the
remaining +0.024 / +0.026 is the sum of the near/above/pairing
constants, each bounded in sec.2-3, totalled by measurement.

Item (iv) answer: B_seed := lim N [E_diag y + S_off + S_pole]
DOES NOT EXIST. The partial quantity is
  B_seed(N) = -(W_0/2) Lambda(N) + C_off + O(1/ln N) -> -inf.
Required for cancellation (v14.882): +0.05151 (even),
+0.05129 (odd) [= 1 + c M_z - alpha L P - W_0]. Measured
B_seed at the F2 block center (N = 12,000,001 / 12,000,002):
-0.13209 / -0.13109 - already 0.184 (even) / 0.182 (odd) below
the required value and decreasing like -(W_0/2) ln ln N. No interval for a limit
can be reported; the expansion above is the precise limit
obstruction the handoff's alternative branch requests.
