# v14.819 task 3 — compact functionals: CLOSED (sandbox, 2026-10-24)

All quantities from the hash-pinned five-component frozen trial
(ca544 `changed.load_components`; prep recomputed in-session and
matched the pinned prep-{sector}.json field-by-field, incl.
pole_pairing_P, compact_l1, Lpoint, tpoint — asserted in mz_eval.py).

## c_inf (exact rationals in mz-{sector}.json)

c_inf = -c*M_z + alpha*L*P,  c = 2/pi point:

- even: c_inf = -0.18426887511732248,  M_z = 9.5212952699e10
  (front-dominated: front 9.5212952699e10; near/patch1/patch2/delta
  together 0.0672), P = 2.1109161113e10, alpha = +2,
  L = 1.4357379705709206, t = 0.10132118364233778.
- odd:  c_inf = -0.18300198492192950,  M_z = -1.2861453739e8,
  P = 6.1703941833e7, alpha = -2, L = 0.6634791495304894.

Cancellation targets (v14.817): s_inf must equal
1 + c*M_z - alpha*L*P = 1.1842688751173225 (even) /
1.1830019849219295 (odd). Z-point perturbation charge on M_z:
4.48e-34 even / 9.41e-36 odd (negligible). A_1, A_2 exact in the
mz JSONs (even 9.5974075793e10 / 8.9874468720e11).

## Remainder: rigorous signed-moment bound (sharpens handoff sec.1)

With M_k = sum x_j m_j^k, M_zk = sum x_j z_j m_j^k (signed, dyadic
points), A_3 = sum |x_j| m_j^3 = 1.1515e17 (even) / 1.1492e17 (odd),
A_z4 = sum |x_j z_j| m_j^4 = 7.0667e23 / 7.0525e23,
M = max input mode = 4161531 / 4161532, Zbar = 7.4232946911
(zbar_moments.py; certified remote-z trig weights + nonprime sup,
spot-checked against enclosures), M_1 = 40188.803 / 40125.187,
M_z2 = 5.6811585291e10 / 6.6334287763e10:

|N*C(N) - c_inf| <= c*Zbar*(|M_1|/N + A_3/(N (N^2-M^2)))
                  + c*(|M_z2| + A_z4/(N^2-M^2))/N^2
                  + |alpha| L P t/(N^2+t)        for all N > M.

Evaluated: 0.0248 at N = 2M (= 8323062, the F2 threshold — F2
outputs start exactly at 2M+1), 0.0135 at N = 1.45e7, 0.00190 at
1e8, 1.9e-4 at 1e9. Dominant term c*Zbar*M_1/N = 1.90e5/N.
This replaces the handoff's absolute A_1/A_2 form (41706 at
1.45e7) — a ~3.1e6 sharpening, from keeping the first moment
signed (M_1 = 4.0e4 vs A_1 = 9.6e10).

## Empirical validation (F2 top octave, mz_eval block set, 31 blocks)

Observed mean gap N*C(N) - c_inf: +0.0026138 even / +0.0026097 odd.
Sharp-identity leading-term prediction (c*z_N*M_1/N - c*M_z2/N^2
- alpha*L*P*t/N^2, block zbar = 1.57059 ~ pi/2): +0.0025820 /
+0.0025781. Per-block residual <= 4.63e-5 both sectors — the gap
is the predicted O(1/N) remainder, not a coefficient error.
Empirical NS (F2 top octave): 1.004456 even / 1.003523 odd;
identity 1 - NC_emp - NS_emp = 0.17720 / 0.17687 reproduces the
v14.812-S composed rho_emp (0.1771 / 0.1768) — the compact side of
the attribution is consistent end-to-end.

Files: mz_eval.py -> mz-{sector}.json; zbar_moments.py ->
remainder-{sector}.json; task3_validate.py -> task3-{sector}.json.
