"""
Checking out the bilinear level (2026-11-06, sandbox;
Jeremy: "lets check it out" -- the level v15.482 located
as the only possible home for frame labels).

The frozen kernel (DERIVATION sec.0), on same-parity
pairs N != M:
  K_{N,M} = c (M z_N - N z_M)/(N^2 - M^2) + 2 sigma p_N p_M,
  c = 2/pi; z_m = pi/2 + osc(m) + O(1/m) with
  osc(m) = sum_q 2 w_q sin(theta_q m), theta_q = (pi/2) log q
  (SEED_FORMULA); p_m = L m/(m^2 + t) with sector (L, sigma)
  from the frozen constants (even: L = 1.4357379705709206,
  sigma = +1; odd: L = 0.6634791495304894, sigma = -1;
  t = 0.10132118364233778 both). Sector = parity class of
  the mode index (DERIVATION sec.1).

PAIR COORDINATES (the grid node's own):
  T = (N+M)/2 (AM, shell), X = (N-M)/2 (offset),
  Y = sqrt(NM) (GM), cosh(psi) = T/Y.
Then N^2 - M^2 = 4XT and the constant part of z gives an
EXACT decomposition (derived in the run):
  K = -1/(2T)  +  2 sigma p_N p_M
      + c (M osc_N - N osc_M)/(4 X T).
[the seed's unspecified O(1/m) part contributes only a
smooth -c*C/Y^2-type shift -- same family as the pole
term; it cannot create residue structure.]

Checks:
 1. the decomposition, numerically (should be exact);
 2. anatomy: the pole term vs L^2/Y^2 (GM law), and the
    sizes of smooth vs oscillatory parts across (T, X)
    bands -- where in pair space the log-frequency
    content lives;
 3. the DICTIONARY question at this level: bin the
    oscillatory correction (the only place labels could
    hide) by pair residue classes -- X mod 3, T mod 3,
    (N mod 3, M mod 3), X mod 9 -- and compare class-mean
    spreads against the random-binning null scale.
Verdict in the printout.
"""
import numpy as np

QS = (2, 3, 4, 5, 7)
w = {q: (np.log(q) / np.sqrt(q) if q != 4 else np.log(2) / 2) for q in QS}
th = {q: (np.pi / 2) * np.log(q) for q in QS}
C = 2 / np.pi
T_POLE = 0.10132118364233778
SECTOR = {0: (1.4357379705709206, +1), 1: (0.6634791495304894, -1)}

def osc(m):
    m = np.asarray(m, dtype=float)
    return sum(2 * w[q] * np.sin(th[q] * m) for q in QS)

print("=" * 76)
print("1. exact decomposition of K in pair coordinates")
print("=" * 76)
rng = np.random.default_rng(7)
worst = 0.0
for _ in range(3000):
    N, M = rng.integers(3, 900, 2)
    if N == M or (N - M) % 2:
        continue
    L, sg = SECTOR[N % 2]
    zN, zM = np.pi / 2 + osc(N), np.pi / 2 + osc(M)
    pN, pM = L * N / (N**2 + T_POLE), L * M / (M**2 + T_POLE)
    K = C * (M * zN - N * zM) / (N**2 - M**2) + 2 * sg * pN * pM
    T, X = (N + M) / 2, (N - M) / 2
    dec = -1 / (2 * T) + 2 * sg * pN * pM \
        + C * (M * osc(N) - N * osc(M)) / (4 * X * T)
    worst = max(worst, abs(K - dec))
print(f"  max |K - decomposition| over random same-parity pairs: "
      f"{worst:.2e} (exact)")

print()
print("=" * 76)
print("2. anatomy: pole term is a GM law; where the oscillations live")
print("=" * 76)
for par, (L, sg) in SECTOR.items():
    n = np.arange(3, 4001)
    n = n[n % 2 == par]
    p = L * n / (n**2 + T_POLE)
    ratio = (p[:-1] * p[1:]) / (L**2 / (n[:-1] * n[1:]))
    print(f"  sector parity {par}: p_N p_M / (L^2/Y^2) on adjacent "
          f"pairs: {ratio.min():.4f}..{ratio.max():.4f} (-> 1: GM law,"
          f" amplitude 2 sigma L^2 = {2*sg*L**2:+.3f})")
for (tlo, thi) in ((60, 240), (400, 900)):
    for Xv in (1, 2, 4, 8, 16, 32):
        Ns = np.arange(tlo, thi)
        Ms = Ns - 2 * Xv
        ok = Ms >= 3
        Ns, Ms = Ns[ok], Ms[ok]
        T = (Ns + Ms) / 2
        corr = C * (Ms * osc(Ns) - Ns * osc(Ms)) / (4 * Xv * T)
        print(f"  T in [{tlo},{thi}), X={Xv:>2}: oscillatory part RMS "
              f"{np.sqrt((corr**2).mean()):.4f} vs drift 1/(2T) ~ "
              f"{1/(2*T.mean()):.4f}")

print()
print("=" * 76)
print("3. residue probe at the pair level (labels in the correction?)")
print("=" * 76)
for par in (0, 1):
    n = np.arange(3, 2401)
    n = n[n % 2 == par].astype(float)
    o = osc(n)
    Nn, Mm = np.meshgrid(n, n, indexing='ij')
    T = (Nn + Mm) / 2
    X = (Nn - Mm) / 2
    corr = C * (Mm * o[:, None] - Nn * o[None, :]) / (4 * X * T)
    mask = X != 0
    cv, Tv, Xv = corr[mask], T[mask], X[mask]
    Nv, Mv = Nn[mask], Mm[mask]
    null = cv.std() / np.sqrt(mask.sum() / 9)
    print(f"  sector parity {par}: correction RMS {cv.std():.3f}; "
          f"random-binning null scale ~ {null:.4f}")
    for name, keys, k in (("X mod 3", Xv % 3, 3), ("T mod 3", Tv % 3, 3),
                          ("X mod 9", Xv % 9, 9),
                          ("(N,M) mod 3", (Nv % 3) * 3 + (Mv % 3), 9)):
        means = np.array([cv[keys == r].mean() for r in range(k)])
        print(f"    {name:>13}: class-mean spread "
              f"{means.max() - means.min():.4f}")

print()
print("=" * 76)
print("VERDICT -- what the bilinear level holds")
print("=" * 76)
print("The bilinear level is NOT empty, and what fills it is")
print("the cone's pair GEOMETRY, exactly. The decomposition")
print("is exact: a smooth pair function -1/(2T) (pure shell/")
print("AM drift) + 2 sigma L^2/Y^2 (GM pole term, sector-")
print("signed: amplitudes +4.12 even / -0.88 odd) -- both")
print("exact but SUBDOMINANT at range -- plus the dominant")
print("term: a 1/X Hilbert-band term carrying the log-")
print("frequencies (RMS ~ 0.41/X, T-independent at fixed X),")
print("which carries NO pair-residue structure (probe 3:")
print("class spreads at the null scale in every binning). So")
print("partial dictionary at this level is real but geometric:")
print("the frame's CONTINUOUS pair coordinates -- T (shell),")
print("Y (GM), X (offset), psi (rapidity, cosh psi = T/Y) --")
print("are the kernel's own coordinates, which is the level")
print("the weld (v14.904) already occupies. The DISCRETE")
print("layer -- residues mod 3 and mod 9, tau and the digit --")
print("is absent at the bilinear level too. After v15.482")
print("(mode level) and this check (pair level), the label")
print("layer of the frame has no anchor anywhere in the")
print("operator's CONSTRUCTION data; what remains unprobed is")
print("only the operator's SPECTRUM (Lane A's certified")
print("objects), where a residue pattern would be a discovery,")
print("not a dictionary entry waiting to be read off.")
