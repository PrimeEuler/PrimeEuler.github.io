"""
Door anatomy II (2026-11-05, sandbox): the generation door,
measured. Same method as door anatomy I (chirality): enumerate
what the frame actually says about the replica tower
c -> c + 3g and split every quantity into
  OUTPUTS  -- things a physical computation reads, and
  ADDRESSES -- labels of where a replica sits.
If every output is g-invariant, no frame computation can output
the generation count, and the door's content can be stated
exactly.

Frame table (minimal embedding of close_the_gap.py, v15.388):
field: (N_A, c at g=0, Y). Replicas: c_g = c_0 + 3g, shell
N_g = N_A + c_g, z_g = N_A - 2 c_g, ambient (N,0) shell dim
(N+1)(N+2)/2. Checks per g in 0..4:
 (a) slot existence: pair modes carry N_A quanta -> slot size
     N_A + 1 = 2j + 1, constant in g;
 (b) output invariance: n2 = N_A mod 2; tau = c_g mod 3;
     Y mod 2 recomputed from the Z6 congruence
     Y/2 + tau/3 + n2/2 in Z (exact Fractions) and matched
     against the field's closed Y (constant in g by (b) if the
     congruence value is);
 (c) the per-generation anomaly sums with the closed Y table
     and kappa = 3: identical (and zero) for every g.
Also recorded: which quantities DO vary with g (the addresses),
the tower's base (g = 0 is the minimal embedding) and ordering
(g is shell height), and the absence of any upper bound.
"""
from fractions import Fraction as F

# field: (N_A, c0, Y as Fraction, color multiplicity note)
FIELDS = {
    "L_L": (1, 0, F(-1)), "Q_L": (1, 1, F(1, 3)), "H": (1, 0, F(1)),
    "e_R": (0, 0, F(-2)), "u_R": (0, 1, F(4, 3)), "d_R": (0, 1, F(-2, 3)),
    "nu_R": (0, 0, F(0)), "W": (2, 0, F(0)),
}
KAPPA = 3  # imported color multiplicity (v15.388), same for all g

def y_mod2(n2, tau):
    """Y mod 2 from the Z6 congruence Y/2 = -tau/3 - n2/2 (mod 1)."""
    return (-2 * F(tau, 3) - n2) % 2

def anomaly_sums():
    """Per-generation anomaly coefficients from the closed table."""
    Y = {k: v[2] for k, v in FIELDS.items()}
    # [SU(2)]^2 U(1): sum over doublets of Y (x color mult for Q_L)
    a_su2 = Y["L_L"] + KAPPA * Y["Q_L"]
    # [SU(3)]^2 U(1): quarks only: 2*Y_Q (doublet, 2 weak comps)
    #   - Y_u - Y_d (right-handed, as left-handed conjugates)
    a_su3 = 2 * Y["Q_L"] - Y["u_R"] - Y["d_R"]
    # [grav]^2 U(1): sum over all Weyl fermions of Y (LH counting:
    # doublets x weak dim x color, singlets as conjugates with -Y)
    a_grav = (2 * Y["L_L"] + 2 * KAPPA * Y["Q_L"]
              - Y["e_R"] - KAPPA * Y["u_R"] - KAPPA * Y["d_R"] - Y["nu_R"])
    # U(1)^3: same counting with Y^3
    a_cube = (2 * Y["L_L"] ** 3 + 2 * KAPPA * Y["Q_L"] ** 3
              - Y["e_R"] ** 3 - KAPPA * Y["u_R"] ** 3
              - KAPPA * Y["d_R"] ** 3 - Y["nu_R"] ** 3)
    return a_su2, a_su3, a_grav, a_cube

print("=" * 76)
print("REPLICA TOWER: outputs vs addresses, g = 0..4")
print("=" * 76)
all_invariant = True
for name, (na, c0, Y) in FIELDS.items():
    rows = []
    for g in range(5):
        c = c0 + 3 * g
        N = na + c
        z = na - 2 * c
        slot = na + 1
        n2 = na % 2
        tau = c % 3
        ym2 = y_mod2(n2, tau)
        ok = (ym2 == Y % 2)
        all_invariant &= ok and (slot == na + 1)
        rows.append((g, c, N, z, (N + 1) * (N + 2) // 2, slot, tau, str(ym2), ok))
    print(f"  {name:>5}: (g, c, shell N, z, ambient dim, slot, tau, Y mod 2, match)")
    for r in rows:
        print(f"         {r}")
print(f"  slot sizes constant, tau constant, Y mod 2 matched for all g: {all_invariant}")

print()
a = anomaly_sums()
print(f"  per-generation anomaly sums (SU2^2 U1, SU3^2 U1, grav^2 U1, U1^3):")
print(f"    {a}  -- functions of the closed Y table only, hence")
print(f"    identical for every g: anomalies give ZERO information about g.")

print()
print("=" * 76)
print("VERDICT")
print("=" * 76)
print("g-VARIANT (addresses only): c, shell N, z, ambient shell dim.")
print("g-INVARIANT (every physical output): slot size 2j+1, n2, tau,")
print("Y mod 2 (hence the closed Y), the anomaly coefficients, and")
print("every loop weight pattern built from them. The tower has a")
print("canonical BASE (g=0 = the minimal embedding) and an ORDER")
print("(g is shell height), but no LENGTH: slots exist for all")
print("g >= 0 with no obstruction at any g, and no frame output is")
print("a function of g. The generation door's content is therefore")
print("NOT a bit (contrast door I): it is one unbounded positive")
print("integer -- the count, N_g = 3 in nature -- plus the mass /")
print("mixing sector, which the frame cannot even phrase (it has")
print("no masses; CKM-weighted generation sums enter only as")
print("imports, loop step 4). No internal computation outputs the")
print("count; unlike the chiral bit, there is not even a symmetry")
print("whose breaking would fix it -- the replica direction is a")
print("half-line of identical-output slots, and nature's choice")
print("of 3 is an external datum of integer species.")
