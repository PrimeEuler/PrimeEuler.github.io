"""
Weak force on the cone -- first algebraic pass (2026-11-03, sandbox).

Starting point (Jeremy's correction): the cone natively carries SU(2)
(Schwinger two-mode structure) and U(1) (the common phase / Hopf fiber).
Electroweak theory is SU(2)_L x U(1)_Y. Question: does the cone's native
U(2) = SU(2) x U(1) reproduce any of the weak force's actual structure,
or only the group names?

Tests:
 1. Schwinger shell algebra: on a fixed total-number shell N, the SU(2)
    generators obey [Ji,Jj] = i eps_ijk Jk, the number operator commutes
    with all of them, and J^2 = j(j+1) with j = N/2. (U(2) container.)
 2. Locked hypercharge: the cone's U(1) charge on a shell is not a free
    label -- it is the shell number itself, Y = +/-N = +/-2j (sign =
    phase orientation). With Q = T3 + Y/2, compute the charge spectrum
    of every shell and compare EXACTLY against the Standard Model
    multiplet table. Which multiplets does the locked tower hit?
 3. Chirality slot: two spinor copies (direct sum L + R). The weak
    generator diag(J,0) acts as a doublet on L and a singlet (zero) on
    R -- the exact weak representation pattern. Parity (copy swap)
    conjugates it to diag(0,J). Vector/axial split: diag(J,0) is
    (V + A)/2 with V = diag(J,J), A = diag(J,-J). The slot exists;
    nothing here selects L over R.
 4. Charged current shape: J+ on the fundamental doublet has amplitude
    exactly 1 (the W transition shape); on higher shells the amplitudes
    are sqrt(n k) -- symmetric excitations, not generations.
 5. Breaking slot: for the Y = +1 fundamental (Higgs charge pattern),
    Q = T3 + Y/2 annihilates the lower component while T1, T2 do not:
    a residual U(1)_Q sits inside the cone's U(2) as the diagonal.
    No Weinberg angle, vev, or mass is computed -- those need g, g'.
"""
from fractions import Fraction
import numpy as np

np.set_printoptions(suppress=True, linewidth=120)

def spin_ops(j2):
    """Spin operators for j = j2/2. Basis m = j, j-1, ..., -j."""
    j = j2 / 2.0
    d = j2 + 1
    ms = np.array([j - i for i in range(d)])
    Jz = np.diag(ms)
    Jp = np.zeros((d, d), dtype=complex)
    for i, m in enumerate(ms):
        # J+ |j,m> = sqrt(j(j+1)-m(m+1)) |j,m+1>; m+1 is the previous row
        if m < j:
            Jp[i - 1, i] = np.sqrt(j * (j + 1) - m * (m + 1))
    Jm = Jp.conj().T
    Jx = (Jp + Jm) / 2.0
    Jy = (Jp - Jm) / 2.0j
    return Jx, Jy, Jz, Jp, Jm, ms

print("=" * 78)
print("TEST 1 -- Schwinger shell algebra: U(2) = SU(2) x U(1)_number")
print("=" * 78)
for j2 in range(0, 7):
    Jx, Jy, Jz, Jp, Jm, ms = spin_ops(j2)
    j = j2 / 2.0
    comm = np.max(np.abs(Jx @ Jy - Jy @ Jx - 1j * Jz))
    J2 = Jx @ Jx + Jy @ Jy + Jz @ Jz
    cas = np.max(np.abs(J2 - j * (j + 1) * np.eye(j2 + 1)))
    N = j2  # total number on the shell; [N*I, Ji] = 0 trivially (scalar)
    print(f"  j={j:>4}: dim={j2+1}, max|[Jx,Jy]-iJz|={comm:.2e}, "
          f"Casimir err={cas:.2e}, shell number N={N} (commutes with all Ji)")

print()
print("=" * 78)
print("TEST 2 -- Locked hypercharge Y = +/-N: charge spectra vs the SM table")
print("         Q = T3 + Y/2,  T3 = m.  Cone lock: Y = +/-2j on shell j.")
print("=" * 78)
SM = {
    "lepton doublet L_L  (j=1/2, Y=-1)":   [Fraction(0), Fraction(-1)],
    "quark doublet Q_L   (j=1/2, Y=+1/3)": [Fraction(2, 3), Fraction(-1, 3)],
    "Higgs doublet H     (j=1/2, Y=+1)":   [Fraction(1), Fraction(0)],
    "right-handed e_R    (j=0,   Y=-2)":   [Fraction(-1)],
    "right-handed u_R    (j=0,   Y=+4/3)": [Fraction(2, 3)],
    "right-handed d_R    (j=0,   Y=-2/3)": [Fraction(-1, 3)],
    "W triplet           (j=1,   Y=0)":    [Fraction(1), Fraction(0), Fraction(-1)],
    "neutral singlet     (j=0,   Y=0)":    [Fraction(0)],
}
for sign, sname in [(+1, "Y=+N"), (-1, "Y=-N")]:
    print(f" -- orientation {sname}:")
    for j2 in range(0, 6):
        j = Fraction(j2, 2)
        Y = sign * j2  # Y = +/-N, N = 2j = j2 (in units of the U(1) quantum)
        charges = sorted(Fraction(j2 - 2 * i, 2) + Fraction(Y, 2) for i in range(j2 + 1))
        hits = [name for name, want in SM.items() if sorted(want) == charges]
        print(f"    j={str(j):>4}, Y={Y:+d}: Q spectrum {[str(c) for c in charges]}"
              + (f"   == SM: {hits}" if hits else ""))
print(" Pattern: Y=-N gives Q = 0,-1,...,-2j on every shell (top state always")
print(" neutral); Y=+N gives Q = 2j,...,1,0. Only j=0 and j=1/2 hit SM entries.")

print()
print("=" * 78)
print("TEST 3 -- Chirality slot on two copies (direct sum L + R, dim 4)")
print("=" * 78)
Jx, Jy, Jz, Jp, Jm, _ = spin_ops(1)
Z2 = np.zeros((2, 2))
def blk(a, b): return np.block([[a, Z2], [Z2, b]])
T_L = [blk(J, Z2) for J in (Jx, Jy, Jz)]     # weak generators: doublet on L
T_R = [blk(Z2, J) for J in (Jx, Jy, Jz)]     # mirror: doublet on R
V = [blk(J, J) for J in (Jx, Jy, Jz)]        # vector: both copies
A = [blk(J, -J) for J in (Jx, Jy, Jz)]       # axial: opposite sign
P = np.block([[Z2, np.eye(2)], [np.eye(2), Z2]])  # parity: swap copies
for a in range(3):
    assert np.allclose(T_L[a], (V[a] + A[a]) / 2), "V-A decomposition failed"
    assert np.allclose(P @ T_L[a] @ P, T_R[a]), "parity swap failed"
    assert np.allclose(P @ V[a] @ P, V[a]) and np.allclose(P @ A[a] @ P, -A[a])
print("  diag(J,0) = (V + A)/2 exactly; parity conjugates L-form to R-form;")
print("  V is parity-even, A is parity-odd. The doublet/singlet split is")
print("  representable exactly -- as a projector choice, not a selection.")

print()
print("=" * 78)
print("TEST 4 -- Charged-current shape: J+ amplitudes by shell")
print("=" * 78)
for j2 in [1, 2, 3, 4]:
    _, _, _, Jp, _, ms = spin_ops(j2)
    amps = [round(float(Jp[i - 1, i]), 4) for i in range(1, j2 + 1)]
    print(f"  j={j2/2}: J+ amplitudes {amps}")
print("  Only the j=1/2 shell has the single unit-amplitude transition of an")
print("  elementary weak doublet. Higher shells are symmetric multi-quantum")
print("  states of the same U(2) tower -- excitations, not generations.")

print()
print("=" * 78)
print("TEST 5 -- Breaking slot: residual U(1)_Q inside U(2) (Higgs pattern)")
print("=" * 78)
Jx, Jy, Jz, Jp, Jm, _ = spin_ops(1)
Y = 1.0  # Y = +N on the j=1/2 shell
Q = Jz + (Y / 2) * np.eye(2)
vev = np.array([0.0, 1.0])  # lower component (the Q=0 one)
print(f"  Q eigenvalues: {np.linalg.eigvalsh(Q)} (spectrum {{1, 0}})")
print(f"  Q @ vev = {Q @ vev}  -> U(1)_Q leaves this component invariant")
print(f"  T1 @ vev = {(Jx @ vev)},  T2 @ vev = {(Jy @ vev)}  -> both move it (broken)")
print(f"  J+ @ vev = {Jp @ vev} (raises to the charged component)")
print("  The diagonal U(1)_Q exists inside the cone's U(2). The Weinberg")
print("  angle (rotation between T3 and Y in the neutral plane) depends on")
print("  the ratio g'/g of two gauge couplings -- no cone quantity fixes it.")
