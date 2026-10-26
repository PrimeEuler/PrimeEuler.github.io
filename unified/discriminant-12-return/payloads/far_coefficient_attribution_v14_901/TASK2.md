# v14.819 task 2 — the seed coefficient: NO LIMIT; combined expansion

Status: BOTH sectors COMPLETE (analytic + block numerics; odd block
run finished 2026-10-25 02:22 local, constants folded in 2026-10-25
from ODD_CONFIRMATION_DRAFT.md; W_0^odd = 1.1317098782051290). All
statements about S(N) concern the
TRUE seed action of SEED_FORMULA.md (model inputs over all m >= b),
not the composed F2 buffer — see the coverage finding in sec.4.

## 1. The obstruction [D]

s_inf = lim N*S(N) does not exist. The U channel
U(n) = sum_{m != n} 2n/(n^2 - m^2) * (z y)_m has nonprime-mean input
mean((z y)_m) = (pi/2) * yhat_m / l_m ~ (pi/2) * W_0 / (m l_m),
l_m = ln(m/4). For b <= m <= n/2 the kernel is 2/n (1 + O(1/4)), so

  U(n) >= (2/n)(pi/2) W_0 * sum_{b<=m<=n/2, step 2} 1/(m l_m) (1+o(1))
       = (pi W_0 / (2n)) * ln ln(n/4) + O(1/n),

and the remaining regions (n/2 < m, m != n; m > n) contribute O(1/n)
with NO ln ln term: near-diagonal Hilbert pairing cancels the
1/(n-m) singularity against the amplitude's slow variation; the
m > n mean tail is O(1/(n ln n)). The trig parts of z_m contribute
O(1) via Dirichlet-bounded partial sums; the -v z^2 part of (zy)_m
and the higher affine channels are summable (constants); the V
channel is O(1/(n ln n)) pointwise in n*V (measured nV ~ 0.0086,
flat); the diagonal tends to W_0; the pole term is < 5e-7. Hence

  N*S(N) = K - (W_0/2) * ln ln(n/4) + gamma/ln n + o(1/ln n),

with beta = (c/2)(pi/2) W_0 * 2 * (1/2) = W_0/2 EXACTLY
(c = 2/pi; the factors are: action prefactor c/2, nonprime mean
pi/2, kernel 2/n, step-2 density 1/2). beta_even = 0.5663798151,
beta_odd = 0.5658549391. In particular N*S(N) -> -infinity
logarithmically: no finite s_inf, and rho_inf of v14.816 does not
exist for this pair either. Per v14.816 step 2 / v14.819 task 2,
the deliverable is the combined expansion (sec.3).

## 2. Numerical confirmation (even; true action, block means)

257-row block means of the direct evaluator (eval_seed_blocks.py;
m-grid shared per block, m != n excluded, smooth tail integrals
beyond 5 n_max; z_n/d_n closed forms spot-checked against the
certified module to <= 1.6e-7 / 8e-8):

  center n     N*S(N)    nU       n*diag   nV
  6,161,535    1.02433   0.34060  1.13067  --
  12,000,001   1.00067   0.42343  1.13178  --
  25,000,001   0.97504   0.50799  1.13240  0.00867
  50,000,001   0.95150   0.58314  1.13264  0.00887
  100,000,001  0.92758   0.65763  1.13255  0.00863
  200,000,001  0.90463   0.72914  1.13263  0.00819

Channel checks: nU free fit vs Lambda = ln ln(n/4): slope 1.77320
(gamma_U = 0.014, rms 0.0008) vs analytic pi*W_0/2 = 1.77933
(0.35%); diagonal -> W_0 = 1.13276 (1.13263 at 2e8); nV flat.
NS fit with beta pinned at W_0/2: K = 2.55271, gamma = -0.35474,
rms 0.00085, max resid 0.0011. (Free 3-parameter fits remain
degenerate -- beta = 0.99, gamma = -8.3 fits the same six points
nearly as well; the channel decomposition above, not the joint
fit, is the evidence for beta. K's dominant assembly: W_0
[diagonal] + (W_0/2) ln ln(b/4) = 1.39628 [drift-sum lower
boundary] + 0.024 residual of un-itemized constants [Hilbert
pairing, z^2 v channel, kernel corrections].)

Odd sector (same evaluator, blocks_odd-v.json, 6 blocks of 257 rows,
centers 6,161,536 to 200,000,002):

  center n     N*S(N)    nU       n*diag   nV
  6,161,536    1.02340   0.34115  1.12994  0.00412
  12,000,002   1.00062   0.42046  1.13078  0.00735
  25,000,002   0.97456   0.50578  1.13123  0.00866
  50,000,002   0.95011   0.58380  1.13155  0.00886
  100,000,002  0.92710   0.65616  1.13169  0.00862
  200,000,002  0.90478   0.72603  1.13177  0.00819

Channel checks: nU free-fit slope 1.7457 vs analytic pi*W_0/2 =
1.77769 (1.8% low — looser than even's 0.35%; stated as such, the
direction and magnitude still confirm the U-channel drift source);
diagonal -> W_0^odd = 1.13171 (1.13177 at 2e8); nV flat ~0.0086.
NS fit with beta pinned at W_0/2 = 0.5658549391: K = 2.55224,
gamma = -0.38076, rms 0.00078, max resid 0.00124. Free 3-parameter
fits degenerate in odd too (beta = 0.907, gamma = -6.78) — same
collinearity caveat as even.

## 3. Combined leading expansion of the residual [D]

With c_inf from TASK3.md (even -0.18426887511732248) and
N*C(N) = c_inf + O(1/N) (sharp bound, TASK3.md):

  N*R(N) = 1 - c_inf - N*S(N) + O(1/N)
         = -1.36844 + 0.56638 * ln ln(n/4) + 0.35474 / ln n
           + o(1/ln n)        (even)
         = -1.36923 + 0.56585 * ln ln(n/4) + 0.38076 / ln n
           + o(1/ln n)        (odd; c_inf^odd = -0.18300198)

-> +infinity like (W_0/2) ln ln n. Sanity at the F2 block center
n = 12,000,001: formula 0.1812 (after the O(1/N) compact gap
+0.0026..0.0030) vs direct 1 - N*C - N*S_true = 0.1806..0.1810.
The v14.812-S buffer-based numbers (rho_emp 0.1771 F2 / 0.1596 F1
block means) are NOT this expansion's values: F1 agrees (seed
buffer exact there), F2 buffer values are biased by sec.4.

## 4. Coverage finding (supersedes the SEED_FORMULA bridge fit)

The F2 seed buffer of the v14.812-S composition is NOT the full
seed action: the assembly summed bank inputs [b, S) plus the
producer tail series at split 2S, omitting the input band
[S, 2S) entirely (the F1 assembly, bank + tail at S, is complete).
Block measurement (same 257 rows, even): eval - buffer =
-0.00039 (F1 center 6,161,535; evaluator noise level) vs
-0.00891 (F2 center 12,000,001); single-row anchors -0.01084 at
n = 10,323,065 and -0.05641 at n = 14,646,125: the buffer
overstates N*S(N) increasingly across F2. Consequences:
(i) the buffer-fit beta = 0.5192 (SEED_FORMULA.md) is superseded —
    band bias + short-window collinearity, not a property of S(N);
(ii) the v14.812-S NOT-PASSED verdict is unaffected and in fact
    strengthened: F1 alone exceeds the headroom (3.6x in squares),
    and since the band enters R with a minus sign, the true F2
    residual exceeds the composed one pointwise in aggregate;
(iii) Audit R345's confirmation is unaffected (it verified the
    certificates' arithmetic for what was composed).
(The earlier check_f2_coverage.py run returned NaN: it failed to
exclude the self term m = n from its bank sums. Do not cite it;
the block comparison above is the coverage measurement.)
Odd sector, same measurement: eval - buffer = -0.00038 (F1 center)
vs -0.00893 (F2 center) — numerically identical to even; the
[S, 2S) omission is sector-independent, as expected for an
assembly bug.

## 5. What this closes / leaves open

Closes v14.819 tasks 1-2 for BOTH sectors: seed formula
(SEED_FORMULA.md), nonexistence of s_inf with the exact drift
coefficient and remainder shape, combined expansion. The seed-side
asymptotic is a property of the affine model's leading channel:
beta = W_0/2 with W_0 = lim m*yhat_m — the SAME constant that sets
the diagonal limit. That identification is the input to task 4.
