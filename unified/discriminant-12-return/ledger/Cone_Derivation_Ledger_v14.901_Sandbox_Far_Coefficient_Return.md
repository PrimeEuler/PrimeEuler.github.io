# Cone Derivation Ledger v14.901 - Sandbox return to v14.819 and v14.882: the seed coefficient does not exist; drift is (W_0/2) ln ln(n/4)

**Date:** 2026-10-26. **Lane:** Sandbox (little Euler), on Jeremy's
ledgering direction. **Parents:** v14.819 (Lane A far-coefficient
handoff, tasks 1-5), v14.882 (Lane A seed-diagonal reframing and
sharpened sandbox handoff, items i-iv), v14.816 (reduction),
v14.812-S (finite far gate NOT PASSED), v14.583 (DM scoped PASS).
**Status:** [D] the drift coefficient and the non-existence of
s_inf / B_seed, from the channel decomposition plus a three-band
uniform treatment, numerically verified on 257-row block means at
six centers 6.2e6..2e8 in both sectors. [D] task 3 coefficient
(c_inf) already independently verified by External Audit R346
(v14.883). **Collision check:** immediately before writing, live
master HEAD `d0b2af043d81a393e28fa54b9c95865da226b95f` (v14.900);
v14.901 next free. No frozen source, trial, or threshold modified.
Payload (producer, certificates, evaluator):
`payloads/far_coefficient_attribution_v14_901/` (manifest with
sha256 in PACKAGE_MANIFEST.md).

## Verdict

For the frozen pair, the far coefficient s_inf does not exist,
and neither does Lane A's B_seed. The seed action obeys, on block
means, in both sectors,

  N*S(N) = W_0 - (W_0/2) ln ln(n/4) + (K - W_0) + gamma/ln n
           + o(1/ln n),

so the combined far coefficient of v14.816 grows without bound:

  N*R(N) = 1 - c_inf - N*S(N)
         = -1.36844 + 0.56638 ln ln(n/4) + 0.35474/ln n + o(1/ln n)  (even)
         = -1.36923 + 0.56585 ln ln(n/4) + 0.38076/ln n + o(1/ln n)  (odd)

rho_inf does not exist for this pair. The v14.812-S finite NOT
PASSED verdict is unaffected and strengthened (sec.4). No
finite-support compact correction and no input-side seed
rescaling can cancel the drift (sec.5); the smallest admissible
correction shape is an action-level counter-term (sec.5).

## 1. Task 1 - the seed's full physical action (SEED_FORMULA.md)

S(n) = (c/2)(z_n V(n) - U(n)) + d_n y_n + sigma*2*p_n*P_tot over
ALL inputs m >= b (b = 512000 + start), with V, U the (h-g),
(h+g) channel sums, h = 1/(n-m), g = 1/(n+m); y_m = yhat_m/l_m,
l_m = ln(m/4); yhat_m = w(m) - v(m) z_m + shift_m from the 11
frozen affine channels (exact rationals, hash-pinned payload);
d_n = l_n + D_osc(n) the certified diagonal; z_n the certified
remote-z (five trig modes + nonprime mean pi/2). The affine
defect is quantified: W_0 != 1 (sec.3).

## 2. Task 3 - c_inf from the exact five-component moments

c_inf = -c*M_z + alpha*L*P, all quantities exact or certified:

  even: M_z = 9.5212952699e10, P = 2.1109161113e10, alpha = +2,
        c_inf = -0.18426887511732248
  odd:  M_z = -1.2861453739e8, P = 6.1703941833e7, alpha = -2,
        c_inf = -0.18300198492192950

Signed-moment remainder (replaces the absolute A_1/A_2 form):
|N*C(N) - c_inf| <= c*Zbar(|M_1|/N + A_3/(N(N^2-M^2))) +
c(|M_z2| + A_z4/(N^2-M^2))/N^2 + |alpha| L P t/(N^2+t), with
signed M_1 = 40188.803 even / 40125.187 odd (vs A_1 = 9.6e10),
Zbar = 7.4232946911: the bound is 0.0248 at N = 2M, 0.00190 at
1e8. Validated on the F2 top octave against the buffers
(per-block residual <= 4.63e-5). Required seed limits:
s_inf = 1 + c*M_z - alpha*L*P = 1.1842688751173225 even /
1.1830019849219295 odd. Audit R346 (v14.883) independently
verified this compact asymptotic.

## 3. v14.882 items (i)-(ii) - exact W_0, Phi remainder, E_diag

(i) W_0 is the j = 0 W-channel coefficient of the pinned source
(exact rationals in payload w0_exact.json; common denominator
2^256):
  even W_0 = 1.1327596301371365,  odd W_0 = 1.1317098782051290.
(ii) Phi(m) = W_0/m + R_Phi(m), |R_Phi(m)| <= kappa_Phi/m^2 with
kappa_Phi = 6.62e4 even / 6.61e4 odd assembled termwise from the
exact channels (|R_Phi(b)| <= 2.53e-7); hence the D_log diagonal
coefficient is exactly W_0 with N|R_Phi(N)| <= 1.3e-4 on the far
blocks - Lane A's Gate 1 confirmed in the evaluator realization.
E_diag(N) = D_osc(N), |D_osc| <= 1.76: N*E_diag y =
D_osc(N)(W_0/l_N)(1+O(1/N)) = O(1/ln N), block mean <= 2e-4 on
all twelve blocks. It carries neither coefficient nor drift.

## 4. Task 2 + v14.882 items (iii)-(iv) - the drift, three bands

Block means of N*S(N) (257-row blocks, exact action, inputs to
5x center, m != N excluded):
  centers   6161535   12000001  25000001  50000001  1e8       2e8
  even      1.02433   1.00067   0.97504   0.95150   0.92758   0.90463
  odd       1.02340   1.00062   0.97456   0.95011   0.92710   0.90478

Channel decomposition (TASK2.md, TASK2B_THREEBAND.md): the only
non-summable, non-cancelling accumulation in the action is the
U channel's below-band smooth mean: kernel 2N/(N^2-m^2) ~ 2/N
against the nonprime mean (pi/2) yhat_m/l_m ~
(pi/2)(W_0)/(m l_m), giving sum_{step 2, m<N} 1/(m l_m) =
(1/2) ln ln(n/4) + boundary; the factors (c/2)(pi/2)(2)(1/2)
with c = 2/pi reduce the drift coefficient to exactly
beta = W_0/2 = 0.5663798151 even / 0.5658549391 odd. Three-band
uniform treatment: near band - the singular kernel pairs
exactly on the step-2 lattice (the log N growth cancels);
trig channels are Hilbert eigenfunctions with bounded
phase-shifted limits; above band absolutely summable;
V channel has no log-log term (its below band is li-type
W_0/(N l_N)); pole contributes sigma*2*L*P_inf = +/-3.6e-7.
Channel check: nU slope vs ln ln(n/4) is 1.77320 even (analytic
pi*W_0/2 = 1.77933). Pinned-beta fits: K = 2.55271 even /
2.55224 odd, rms <= 8.5e-4. The assembled constant
K - W_0 = 1.41995 even / 1.42053 odd is 98% the drift sum's
lower boundary (W_0/2) ln ln(b/4) = 1.39628 / 1.39499; the
discretization constant C_Sigma of sum 1/(m l_m) is 0 to six
decimals (direct summation to 2e8).

(iv) B_seed does not exist: B_seed(N) = -(W_0/2) ln ln(n/4) +
(K - W_0) + O(1/ln N) -> -infinity. Required (v14.882):
+0.05151 even / +0.05129 odd. Measured at the F2 centers:
-0.13209 / -0.13109 - 0.184 / 0.182 below required and falling.
This is the precise limit obstruction of the handoff's
alternative branch; no interval for a limit can be reported.

Coverage finding (erratum-grade, disclosed): the F1 seed buffer
is the true action (block diff -0.00039 / -0.00038, evaluator
noise). The F2 seed buffer is NOT the full action: assembly
summed bank inputs [b, S) plus the producer tail series at
split 2S, omitting the input band [S, 2S) entirely (block diff
at the F2 centers -0.00891 / -0.00893; single-row anchor
-0.05641 at n = 14,646,125 even). Consequences: the v14.812-S
NOT PASSED verdict is unaffected and strengthened (F1 alone is
3.6x headroom^2; the band enters R with a minus sign, so the
true F2 residual is larger than composed); Audit R345 is
unaffected (it verified the composed certificates' arithmetic);
the earlier sandbox buffer fit beta = 0.5192 is superseded.

## 5. Task 4 - admissible corrections

[D] No finite-support compact correction can work: its scaled
action tends to a constant (sec.2 bound shape) while the seed
drift is unbounded. [D] No input-side seed rescaling can work:
the drift coefficient and the diagonal limit are the same
constant w* = lim m*yhat_m; zeroing the drift forces w* = 0,
which kills the diagonal too (check: K - W_0 = 1.41995 !=
1 - c_inf = 1.18427 even). Smallest admissible shape: an
action-level counter-term CT with N*CT(N) = -[combined
expansion of sec.0] exactly, satisfying (a) far support / DM
silence |N*CT| <~ 1e-5 on region-1 and DM rows - then v14.583
stands without recertification (an input-side change fails (a)
automatically); (b) its own approximant provenance in Lane A's
framework (phantom input family with no diagonal footprint is
the natural shape; constructing it is Lane A's geometry);
(c) l2-admissible on the far half-line; a fresh finite F1/F2
composition is still required for any concrete candidate.
(d) SEPARATELY, the F2 band omission (sec.4) is an assembly
bug: any future far composition must include the [S, 2S) band;
fixing it changes no definitions or certificates.

## Scope / guardrails

Thresholds C_S_32000, 3e-5, 0.002 untouched; no v14.354/global
transport charge repeated; no far F1/F2 rerun performed (v14.882
bars one until an admissible correction is identified and
audited). v14.583 DM scoped PASS and v14.812-S NOT PASSED stand.
External Audit handoff: replay eval_seed_blocks.py and
task3_validate.py from the payload against the frozen hashes;
the three-band bounds of TASK2B_THREEBAND.md are stated with
their (loose) absolute constants; block-mean residuals are in
blocks_{even,odd}-v.json.
