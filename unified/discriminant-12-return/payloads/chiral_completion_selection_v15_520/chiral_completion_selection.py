"""
Supplying the chiral bit: does the completed framework select?
(2026-11-07, sandbox; Jeremy: "can we supply the chiral bit and
complete more of the framework to see if there is a selection?")

Door I (v15.429) is exactly one bit: the correlation between the
frame's chirality tags and the bicone's Spin(4) factors. Nature
supplies it empirically (weak parity violation). This build
SUPPLIES it -- either orientation; both passed every internal
constraint at v15.429 -- and completes the framework's weak
sector on top of it: with the bit in place the completed theory
is a CHIRAL gauge theory (one Lorentz chirality of quark/lepton
doublets gauged under SU(2), the opposite chirality singlets),
so quark mixing is a SINGLE unitary matrix V (the CKM matrix),
not a pair. The question: does anything downstream become
SELECTED that was open before?

Test 1 (the floor -- Kobayashi-Maskawa counting, exact).
A unitary V in U(N) carries N^2 real parameters. Quark-field
rephasing V_ij -> exp(i(beta_j - alpha_i)) V_ij removes the
rank of that action; the surviving physical parameters split
into mixing angles and CP phases. The ranks are computed here
exactly (sympy, rational incidence matrices), and the phase
counts are witnessed numerically by the Jarlskog invariant
J = Im(V_00 V_11 V_01* V_10*):
  N=2: phases = 0 and J == 0 identically -- a two-generation
       chiral theory CANNOT violate CP through its mixing
       matrix, for any parameter values;
  N=3: phases = 1 and J != 0 generically.
CONTROL (why the bit is load-bearing): refuse the bit and
complete VECTORLIKE instead (both chiralities gauged, V_L and
V_R independent): the rephasing rank drops relative to the
parameter count and N=2 already carries physical CP phases.
They live in the RELATIVE phases between V_L and V_R (the
shared quark rephasing cannot remove both matrices' phases);
witnessed below by the exactly invariant, CP-odd combination
z = Q_00 Q_11* with Q = V_L . conj(V_R) elementwise, whose
phase is a relative-phase difference and is generically
nonzero at N=2. (The naive quartet cross-ratio of Q is
identically real -- each 2x2 unitary obeys
phi_00 + phi_11 - phi_01 - phi_10 = pi, the same rigidity
that forces J = 0; an early draft of this build probed that
dead invariant and the run caught it.) The floor exists
only in the chiral completion.
MIRROR CHECK: conjugating V (the swap correlation) sends
J -> -J: the bit's VALUE flips CP's sign, not its existence;
the floor depends on chirality, not on which side nature picked.

Premises for the floor (stated, both empirical):
 (P1) the bit is supplied (parity violation; either value);
 (P2) the completed framework's flavor-CP source is its CKM
      sector -- theta_QCD ~ 0 (neutron-EDM bound |theta| <
      1e-10, imported) and no flavor structure beyond the
      frame's Yukawa sector.
Datum: quark-sector CP violation is observed, with the CKM
Jarlskog invariant measured J ~ 3.1e-5 != 0 (imported).
=> under (P1)+(P2): N_g >= 3. This bound does NOT use H2.

Test 2 (the ceiling -- address capacity, rechecked here).
At the selected flat level 9 (v15.474), the frame's Z18 address
(v15.467) depends on the generation digit only through g mod 3:
distinct addresses per tau = 3, and g=3 duplicates g=0's address
for every slot (recomputed below from crt_class). IF a sector
reads the address (H2 -- the mass sector is the candidate; the
m_tau fingerprint is its experiment), distinctly-labeled
generations number at most 3.

Test 3 (other completions on the supplied bit -- negatives).
Witten's SU(2) global anomaly: left doublets per generation =
1 (L_L) + 3 (Q_L, colors) = 4, even for every N_g -> no count
selection. Per-generation gauge anomalies: the four sums vanish
per generation (recomputed, exact Fractions), identically for
each replica -> the anomaly predicate is generation-blind, as
filed at v15.429. Corroboration (bit-independent): two distinct
nonzero neutrino Delta-m^2 scales are observed (v15.472 data),
and n mass eigenstates carry only n-1 independent Delta-m^2,
so n >= 3 neutrino mass states -- a parallel floor on mass
eigenstates, not on mixing generations; recorded as
corroboration only.

VERDICT SHAPE: a squeeze, not a derivation. Floor 3 (chiral
completion + CP datum; H2-free) meets ceiling 3 (fold + H2).
Under all premises, N_g = 3 -- Door II's formerly unbounded
integer acquires a floor from an unexpected sector and keeps
its ceiling on the same single premise (H2) the m_tau
experiment already tests. The bit itself remains supplied,
not selected; nothing here touches Door III.

All premises named in the output; imported data flagged.
"""
from fractions import Fraction as F
import numpy as np
import sympy as sp

rng = np.random.default_rng(20261106)

print("=" * 76)
print("0. premise: the bit supplied -- the completion is CHIRAL")
print("=" * 76)
print("""  Both tag->factor correlations passed every internal constraint
  (v15.429, C1-C5). Supplying either one fixes the Lorentz reps of
  all 15 fields: the frame's doublets are ONE Lorentz chirality,
  gauged; the tagged singlets are the other chirality, ungauged.
  Quark mixing in the completed theory is therefore a single
  unitary V in U(N_g). (The vectorlike alternative -- gauging
  both -- is the control in Test 1b.)""")

# ----------------------------------------------------------------------
print()
print("=" * 76)
print("1a. exact rephasing ranks and CP-phase counts (chiral completion)")
print("=" * 76)

def chiral_rank(N):
    """Rank over Q of the rephasing action (alpha, beta) on V in U(N)."""
    cols = 2 * N
    rows = []
    for i in range(N):
        for j in range(N):
            r = [0] * cols
            r[i] = -1          # -alpha_i
            r[N + j] = 1       # +beta_j
            rows.append(r)
    return sp.Matrix(rows).rank()

def vectorlike_rank(N):
    """Rank over Q of rephasing (alpha, beta, chi_L, chi_R) on (V_L, V_R)."""
    cols = 2 * N + 2
    rows = []
    for block, chi in ((0, 2 * N), (1, 2 * N + 1)):
        for i in range(N):
            for j in range(N):
                r = [0] * cols
                r[i] = -1
                r[N + j] = 1
                r[chi] = 1
                rows.append(r)
    return sp.Matrix(rows).rank()

print(f"  {'N':>3} {'rank':>5} {'phys':>5} {'angles':>7} {'CP phases':>10}")
floor_ok = True
for N in range(1, 6):
    rk = chiral_rank(N)
    phys = N * N - rk
    angles = N * (N - 1) // 2
    phases = (N - 1) * (N - 2) // 2
    assert rk == 2 * N - 1 and angles + phases == phys
    floor_ok &= (phases == 0) if N < 3 else (phases >= 1)
    print(f"  {N:>3} {rk:>5} {phys:>5} {angles:>7} {phases:>10}")
print("""  rank = 2N-1 exactly; physical = (N-1)^2 = angles + phases,
  phases = (N-1)(N-2)/2: ZERO below N=3, first nonzero at N=3.""")

print()
print("1b. CONTROL -- vectorlike completion (bit refused): phases at N=2")
print(f"  {'N':>3} {'rank':>5} {'phys':>5} {'angles':>7} {'CP phases':>10}")
for N in range(1, 5):
    rk = vectorlike_rank(N)
    phys = 2 * N * N - rk
    angles = N * (N - 1)
    phases = N * (N - 1)  # 2 * N(N+1)/2 phase params - rank 2N
    assert rk == 2 * N and angles + phases == phys
    print(f"  {N:>3} {rk:>5} {phys:>5} {angles:>7} {phases:>10}")
print("  vectorlike N=2 carries 2 physical CP phases: no KM floor.")
assert floor_ok

# ----------------------------------------------------------------------
print()
print("=" * 76)
print("1c. Jarlskog witnesses (numeric, seeded; 300 random unitaries each)")
print("=" * 76)

def rand_unitary(N):
    z = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    return q * (d / np.abs(d))

def jarlskog(V):
    return float(np.imag(V[0, 0] * V[1, 1] * np.conj(V[0, 1]) * np.conj(V[1, 0])))

mx2 = max(abs(jarlskog(rand_unitary(2))) for _ in range(300))
js3 = [abs(jarlskog(rand_unitary(3))) for _ in range(300)]
print(f"  chiral N=2: max |J| over 300 samples = {mx2:.2e}  (identically 0)")
print(f"  chiral N=3: max |J| = {max(js3):.4f}; "
      f"fraction with |J| > 0.005 = {np.mean([j > 0.005 for j in js3]):.2f}")
assert mx2 < 1e-12 and max(js3) > 0.05

V = rand_unitary(3)
print(f"  mirror: J(conj V) + J(V) = {jarlskog(np.conj(V)) + jarlskog(V):.2e}"
      "  (bit's value flips CP's sign only)")
assert abs(jarlskog(np.conj(V)) + jarlskog(V)) < 1e-14

def rel_phase(VL, VR):
    """arg z, z = Q_00 * conj(Q_11), Q = V_L . conj(V_R) elementwise.
    Invariant under quark rephasing (acts identically on both
    matrices) and under the W_L/W_R phase conventions (cancel
    between Q_00 and conj(Q_11)); CP-odd (z -> conj(z))."""
    Q = VL * np.conj(VR)
    return float(np.angle(Q[0, 0] * np.conj(Q[1, 1])))

def cross_ratio_phase(VL, VR):
    Q = VL * np.conj(VR)
    return float(np.angle(Q[0, 0] * Q[1, 1] / (Q[0, 1] * Q[1, 0])))

phis, inv_err, cr_max = [], 0.0, 0.0
for _ in range(300):
    VL, VR = rand_unitary(2), rand_unitary(2)
    phis.append(rel_phase(VL, VR))
    cr_max = max(cr_max, abs(np.sin(cross_ratio_phase(VL, VR))))
    a, b = rng.uniform(0, 2 * np.pi, 2), rng.uniform(0, 2 * np.pi, 2)
    cL, cR = rng.uniform(0, 2 * np.pi, 2)
    ph = np.exp(1j * (b[None, :] - a[:, None]))
    VL2, VR2 = VL * ph * np.exp(1j * cL), VR * ph * np.exp(1j * cR)
    d = abs(np.angle(np.exp(1j * (rel_phase(VL2, VR2)
                                  - rel_phase(VL, VR)))))
    inv_err = max(inv_err, d)
frac = np.mean([abs(np.sin(p)) > 0.1 for p in phis])
print(f"  vectorlike N=2: relative-phase invariant rephasing-exact "
      f"(max drift {inv_err:.1e});")
print(f"    fraction of samples with |sin(arg z)| > 0.1 = {frac:.2f}"
      "  (CP-odd witness generically nonzero)")
print(f"    [control on the witness choice: the quartet cross-ratio of Q"
      f" is identically")
print(f"     real -- max |sin| = {cr_max:.1e} -- by the 2x2 phase rigidity; "
      "the surviving")
print("     vectorlike phases are relative L-R phases, seen by z.]")
assert inv_err < 1e-9 and frac > 0.8 and cr_max < 1e-9
print("  => the KM floor is a property of the CHIRAL completion:")
print("     supply the bit and CP violation needs N_g >= 3; refuse")
print("     it (vectorlike) and N_g = 2 already violates CP.")

# ----------------------------------------------------------------------
print()
print("=" * 76)
print("2. the ceiling rechecked: Z18 addresses see only g mod 3")
print("=" * 76)

def crt_class(n2, tau, g):
    c9 = (tau + 3 * g) % 9
    for c in range(18):
        if c % 2 == n2 and c % 9 == c9:
            return c
    raise ValueError

for tau in range(3):
    addrs = [crt_class(1, tau, g) for g in range(5)]
    assert len(set(addrs[:3])) == 3 and addrs[3] == addrs[0] and addrs[4] == addrs[1]
    print(f"  tau={tau}: addresses g=0..4 -> {addrs}"
          "  (3 distinct; g=3 duplicates g=0)")
print("  => IF a sector reads the address (H2), distinctly-labeled")
print("     generations <= 3. (Fold capacity; v15.461/v15.467.)")

# ----------------------------------------------------------------------
print()
print("=" * 76)
print("3. other completions on the supplied bit: no further selection")
print("=" * 76)
Y = {"L_L": F(-1), "Q_L": F(1, 3), "e_R": F(-2), "u_R": F(4, 3), "d_R": F(-2, 3)}
a_su2 = Y["L_L"] + 3 * Y["Q_L"]
a_su3 = 2 * Y["Q_L"] - Y["u_R"] - Y["d_R"]
# gravitational / cubic sums over left-handed Weyl fermions per generation
lh = [(2, Y["L_L"]), (6, Y["Q_L"]), (1, -Y["e_R"]), (3, -Y["u_R"]), (3, -Y["d_R"])]
a_grav = sum(m * y for m, y in lh)
a_cube = sum(m * y ** 3 for m, y in lh)
print(f"  per-generation anomalies: [SU2]^2Y = {a_su2}, [SU3]^2Y = {a_su3}, "
      f"grav^2Y = {a_grav}, Y^3 = {a_cube}")
print("    -- identical for every replica: the anomaly predicate is")
print("       generation-blind (as filed, v15.429). No count selection.")
assert (a_su2, a_su3, a_grav, a_cube) == (0, 0, 0, 0)
print(f"  Witten SU(2) global anomaly: doublets/generation = 1 + 3 = 4, "
      f"even for all N_g (4*N_g even, N_g=1..5: "
      f"{all((4 * n) % 2 == 0 for n in range(1, 6))}). No selection.")
print("  corroboration (no bit needed): observed neutrino Delta-m^2 "
      "scales = 2 distinct")
print("    nonzero values (7.4e-5, 2.51e-3 eV^2, v15.472); n mass states "
      "carry n-1")
print("    independent Delta-m^2, so n >= 3 mass eigenstates. Parallel "
      "floor, filed as")
print("    corroboration only (mass eigenstates, not mixing generations).")

# ----------------------------------------------------------------------
print()
print("=" * 76)
print("VERDICT -- a squeeze, under named premises (not a derivation)")
print("=" * 76)
print("""  FLOOR:  chiral completion (bit supplied, either value) + the
          observed quark-sector CP violation carried by the CKM
          sector [premise P2: theta_QCD ~ 0 measured; no flavor
          structure beyond the frame's Yukawa sector; datum
          J ~ 3.1e-5 != 0, imported]  =>  N_g >= 3.
          This bound does NOT use H1/H2.
  CEILING: the level-9 fold's address capacity (v15.461/467/474)
          + H2 (a sector reads the digit)  =>  N_g <= 3.
  TOGETHER: N_g = 3, conditional on H2 for the ceiling only.
  Door II update: the integer is no longer unbounded on both
  sides -- it is floored by completed-frame physics + data and
  ceilinged by the fold premise the m_tau experiment tests.
  NOT selected here: the bit itself (supplied, as nature
  supplies it), any Door III value. Falsifiers: a 4th mixing
  generation with new-valued labels kills the ceiling's premise
  (H2/fold, as filed v15.468); J = 0 in nature would have killed
  the floor's datum -- it is measured nonzero.""")
