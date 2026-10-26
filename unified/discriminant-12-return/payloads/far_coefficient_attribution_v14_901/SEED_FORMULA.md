# v14.819 task 1 — the seed's full physical action formula

Status: IDENTIFIED from the generation source. All objects below are
the operative ones — the far seed buffers composed in v14.812-S were
assembled by `far585/far_assemble.py` in exactly these conventions
(the DM assemblies used the same evaluator lineage).

## Input sequence (seed generation)

Source: `sandbox_region23_evaluator.seed_row`, stated identical to
Lane A's v14.290 close producer; channel data from the hash-pinned
`payloads/whole-source-affine.json` (sha asserted in the evaluator).

For each sector (start = 1 even, 2 odd), b = 512000 + start, and each
input mode m ≡ start (mod 2), m ≥ b:

- z_m: midpoint of the certified remote-z enclosure
  (`suzuki_certified_remote_z.evaluate`, 2^160 grid, radius < 1e-39).
  z_m = Σ_{q∈{2,3,4,5,7}} 2 w_q sin(θ_q m) + nonprime(m),
  w_q = log q / √q (w_4 = log 2 / 2), θ_q = π log q / 2,
  nonprime(m) = π/2 + O(1/m).
- Affine model (11 channels, j = 0..10, exact rationals):
  w(m) = Σ_j W_j m^{-(2j+1)},  v(m) = Σ_j A_j m^{-(2j+2)}.
  W_0 = 1.1327596301371365 (even) / 1.1317098782051290 (odd);
  A_0 = 7608.869974367743 / 7600.753431988682 (the A family is large:
  A_1 ≈ 1.83e14 — an inverse-moment fit, not a perturbation series).
- ŷ_m = w(m) − v(m)·z_m + shift_m,  shift_m = 1/(m(m−1)) if odd
  else 0.
- y_m = ŷ_m / l_m,  l_m = log_normalized(m) = ln(m/4) (certified).
- p_m = ⌊L·m/(m²+t)⌋ at 2^256, with (L, t) the sector points
  (L = 1.4357379705709206 even / 0.6634791495304894 odd;
  t = 0.10132118364233778 both).

## Diagonal

d_n = `suzuki_certified_remote_diagonal.evaluate(n)`:
d_n = l_n + cusp_n − Σ_q w_q (2 − log q)·[cos(θ_q n)
+ (2/(nπ))·sin(θ_q n)] + O(1/n²),
cusp_n = −1/(2n) + 2(−1)^n/(nπ)². So d_n = l_n + D_osc(n) with
D_osc bounded oscillatory (amplitude < 2), and
d_n·y_n = ŷ_n·(1 + D_osc(n)/l_n), n·ŷ_n → W_0.

## Action at an output row n

S(n) = c·(z_n·V(n) − U(n))/2 + d_n·y_n + σ·2·p_n·P_tot,

- c = 2/π (point, radius < 2^-255), σ = +1 even / −1 odd;
- V(n) = Σ_{m≠n} (h−g)_nm y_m, U(n) = Σ_{m≠n} (h+g)_nm (z y)_m,
  h = 1/(n−m), g = 1/(n+m), over ALL seed inputs m ≥ b;
  evaluated as exact bank channel sums (m ≠ n) on [b, split) plus
  the certified tail series at the assembly split,
  −2·Σ_j n^{2j}·mid V_j(split), −2·Σ_j n^{2j+1}·mid U_j(split),
  with envelope remainder bounds (far_assemble RemV/RemU);
- P_tot = P_bank + P_tail(split) = Σ_{all m} p_m y_m = P_∞,
  |P_∞| ≈ 1.4e-7: the pole term contributes < 4e-7 to N·S(N) —
  negligible for the coefficient question.

## Empirical asymptotics (bridge to task 2)

Block means (2^16 rows) of N·S(N) over the composed F1+F2 buffers,
least squares in (1, −ln ln n, 1/ln n), 94 blocks per sector:

N·S(N) ≈ A − β·ln ln N + γ/ln N,  A = 2.567, **β = 0.5192**
(identical in both sectors), γ = −2.307, rms residual 0.0015.

So N·S(N) has NO finite limit: it drifts down like −β·ln ln N
(the drift is visible directly: +1.0207 → +1.0006 across F2 even).
The naive nonprime-mean prediction for the drift coefficient is
β = W_0/2 = 0.5664 (from −(c/2)·2·(π/2)·W_0·(1/2)·ln ln N with
c = 2/π); the fit gives 0.5192 — pinning the exact β, and the
constant A − β·ln ln(l_b) assembly, is task 2. Regressor
collinearity over the composed window's short ln ln lever
(2.630 → 2.723) is a live caveat; the fit extends to n ∈ (S, 2S)
with the existing producer moments at split 2S.
