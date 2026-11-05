"""
Loop program, step 2 (2026-11-04 evening, sandbox): the perturbed
operator. K = D + B with D diagonal, d_n = log(n/4), and B a MODEL
perturbation of the same operator-theoretic class as the ledger's B
(bounded, noncompact, borderline summability): the Hilbert-like
matrix B_mn = c/(m+n-1), c = 0.3 (norm <= 0.3 pi). This is NOT Lane
A's canonical B -- provenance discipline: it is a testbed for the
determinant machinery, and every conclusion below is about the
machinery on this class, not about the canonical operator.

Questions:
 (a) Does the raw perturbation determinant
     log D_N(z) = log det[(K_N - z)(D_N - z)^{-1}] converge as the
     section grows? (Expect: no -- it drifts like the trace
     Tr(B R_D) ~ sum 1/(n log n) ~ log log N.)
 (b) Does the renormalized (det_2) version,
     log D_N(z) - Tr(B_N R_{D,N}(z)), converge? (Expect: yes --
     B R_D is Hilbert-Schmidt because sum 1/(n log^2 n) converges.)
 (c) Birman-Krein on a finite section: with xi(lambda) the
     eigenvalue counting difference N_D(lambda) - N_K(lambda),
     verify Tr[f(K) - f(D)] = int f'(lambda) xi(lambda) dlambda
     for f(lambda) = (lambda - z)^{-1}, and
     d/dz log D(z) = Tr[(D-z)^{-1} - (K-z)^{-1}].
"""
import numpy as np

C = 0.3
Z = -3.5  # below both spectra: d_1 = -1.386, Weyl bound mu_min >= d_1 - 0.3*pi = -2.33

def build(N):
    n = np.arange(1, N + 1)
    d = np.log(n / 4.0)
    m = n[:, None]; k = n[None, :]
    B = C / (m + k - 1)
    return d, B

print("=" * 76)
print("(a)/(b) raw vs renormalized perturbation determinant, z =", Z)
print("=" * 76)
prev_raw, prev_ren = None, None
for N in [50, 100, 200, 400, 800]:
    d, B = build(N)
    K = np.diag(d) + B
    RD = 1.0 / (d - Z)
    # log det[(K-z)(D-z)^{-1}] via slogdet of the ratio matrix
    M = (K - Z * np.eye(N)) * RD[None, :]  # columns scaled: (K-z)(D-z)^{-1}
    sign, logdet = np.linalg.slogdet(M)
    trBR = np.sum(np.diag(B) * RD)
    ren = logdet - trBR
    print(f"  N={N:>4}: raw log D = {logdet:+.6f} (sign {sign:+.0f}), "
          f"Tr(B R_D) = {trBR:+.6f}, renormalized = {ren:+.6f}")
    if prev_ren is not None:
        print(f"         increments: raw {logdet - prev_raw:+.4f}, renormalized {ren - prev_ren:+.6f}")
    prev_raw, prev_ren = logdet, ren
print("  -> raw drifts (log log N-shaped, from the trace); the det_2-")
print("     renormalized determinant settles: B R_D is Hilbert-Schmidt")
print("     though not trace class -- the Krein gate, quantitatively.")

print()
print("=" * 76)
print("(c) Birman-Krein identities on one finite section (N = 120)")
print("=" * 76)
N = 120
d, B = build(N)
K = np.diag(d) + B
evD = np.sort(d)
evK = np.linalg.eigvalsh(K)
# Independent evaluation of int f'(lambda) xi(lambda) dlambda:
# xi(lambda) = #{d_j <= lambda} - #{mu_j <= lambda} is a step function,
# constant between consecutive eigenvalues (and 0 outside the joint
# range, since both sections have N eigenvalues). Integrate exactly
# interval by interval using only counting and values of f.
f = lambda lam: 1.0 / (lam - Z)
pts = np.sort(np.concatenate([evD, evK]))
total = 0.0
for a, b in zip(pts[:-1], pts[1:]):
    mid = 0.5 * (a + b)
    xi = np.sum(evD <= mid) - np.sum(evK <= mid)
    total += xi * (f(b) - f(a))
lhs = np.sum(1.0 / (evK - Z)) - np.sum(1.0 / (evD - Z))   # Tr[R_K - R_D]
print(f"  Tr[R_K - R_D]             = {lhs:+.10f}")
print(f"  int f'(lambda) xi dlambda = {total:+.10f}   (interval-integrated, independent)")
print(f"  agreement: {abs(lhs - total) < 1e-8}")
# d/dz log D(z) identity
h = 1e-5
def logD(zz):
    M = (K - zz * np.eye(N)) / (d - zz)[None, :]
    s, ld = np.linalg.slogdet(M)
    return ld
deriv = (logD(Z + h) - logD(Z - h)) / (2 * h)
trdiff = np.sum(1.0 / (d - Z)) - np.sum(1.0 / (evK - Z))
print(f"  d/dz log D(z) numeric    = {deriv:+.10f}")
print(f"  Tr[(D-z)^-1 - (K-z)^-1]  = {trdiff:+.10f}   agreement: {abs(deriv - trdiff) < 1e-6}")
print()
print("SCOPE: model B (Hilbert-like, same class), finite sections.")
print("Conclusions are about the determinant machinery on the log")
print("spectrum's perturbation class, not about the canonical K.")
