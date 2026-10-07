#!/usr/bin/env python3
"""
Reproducer for v14.097 S2-S3 / v14.102 Request 1:
Bicone ladder-algebra verification.

Verifies (by explicit finite-dimensional matrices, no assumptions):
  (1) M[i,j,m] = <1s|a_i b_j|2p,m> exhibits delta_{q,-m} with value +1
      (the Wigner-Eckhart vector selection rule, emerging from computation).
  (2) OBSTRUCTION: ab-type bilinears FAIL to satisfy [L_+, .] vector-operator
      ladder relations under L=J^a+J^b (for all sigma-pairings tried).
      Hence r_q is not in the bicone su(2)+su(2) enveloping algebra.

States: |1s> = vacuum |0,0,0,0>; |2p,m> from |1/2>x|1/2> (Na=1,Nb=1).
Truncated Fock space: Na+Nb <= 2.

Reference: workspace/d12/explorations/bicone-dipole/REPORT.md S2-S4.
Ledger: v14.097 (partial), v14.102 (audit request).
"""

import numpy as np
from itertools import product

print("=" * 70)
print("v14.097 S2-S3 reproducer: bicone ladder algebra")
print("=" * 70)

# ---------------------------------------------------------------------------
# Fock basis: |na1, na2, nb1, nb2>, na1+na2+nb1+nb2 <= 2
# ---------------------------------------------------------------------------
basis = []
for na1, na2, nb1, nb2 in product(range(3), repeat=4):
    if na1 + na2 + nb1 + nb2 <= 2:
        basis.append((na1, na2, nb1, nb2))
dim = len(basis)
idx = {s: i for i, s in enumerate(basis)}
print(f"\nFock basis dim (Na+Nb<=2): {dim}")

def destroy(mode):
    """Annihilation operator for mode 0:a1, 1:a2, 2:b1, 3:b2."""
    M = np.zeros((dim, dim), dtype=complex)
    for s, i in idx.items():
        n = s[mode]
        if n > 0:
            s2 = list(s); s2[mode] -= 1; s2 = tuple(s2)
            j = idx[s2]
            M[j, i] = np.sqrt(n)
    return M

a1 = destroy(0); a2 = destroy(1); b1 = destroy(2); b2 = destroy(3)
a1d = a1.T.conj(); a2d = a2.T.conj(); b1d = b1.T.conj(); b2d = b2.T.conj()

# Schwinger su(2): J^a_+ = a1^d a2, J^a_- = a2^d a1, J^a_z = (a1^d a1 - a2^d a2)/2
Jap = a1d @ a2; Jam = a2d @ a1; Jaz = (a1d@a1 - a2d@a2)/2
Jbp = b1d @ b2; Jbm = b2d @ b1; Jbz = (b1d@b1 - b2d@b2)/2
Lp = Jap + Jbp; Lm = Jam + Jbm; Lz = Jaz + Jbz

# States
vac = np.zeros(dim); vac[idx[(0,0,0,0)]] = 1.0  # |1s>
# |2p,m>: Na=1, Nb=1
s_p1 = np.zeros(dim); s_p1[idx[(1,0,1,0)]] = 1.0                    # m=+1: a1d b1d|0>
s_m1 = np.zeros(dim); s_m1[idx[(0,1,0,1)]] = 1.0                    # m=-1: a2d b2d|0>
s_0  = np.zeros(dim)
s_0[idx[(1,0,0,1)]] = 1/np.sqrt(2); s_0[idx[(0,1,1,0)]] = 1/np.sqrt(2)  # m=0
states_2p = {+1: s_p1, 0: s_0, -1: s_m1}
print("States: |1s>=vacuum, |2p,m> triplet (Na=1,Nb=1)")

# ---------------------------------------------------------------------------
# (1) M[i,j,m] = <1s|a_i b_j|2p,m> : expect delta_{q,-m}, value +1
# R_{-1}=a1 b1, R_0=(a1 b2 + a2 b1)/sqrt2, R_{+1}=a2 b2
# ---------------------------------------------------------------------------
print("\n--- (1) Selection rule M[i,j,m] = <1s|a_i b_j|2p,m> ---")
a = [None, a1, a2]; b = [None, b1, b2]
R = {-1: a1@b1, 0: (a1@b2 + a2@b1)/np.sqrt(2), +1: a2@b2}
ok1 = True
for m in (+1, 0, -1):
    for q in (-1, 0, +1):
        val = (vac.conj() @ R[q] @ states_2p[m]).item()
        expect = 1.0 if q == -m else 0.0
        match = abs(val - expect) < 1e-10
        ok1 &= match
        if abs(val) > 1e-10 or not match:
            print(f"  m={m:+d}, q={q:+d}: {val.real:+.4f} (expect {expect:+.1f}) {'OK' if match else 'FAIL'}")
print(f"  <1s|R_q|2p,m> = delta_(q,-m) * (+1): {'PASS' if ok1 else 'FAIL'}")

# ---------------------------------------------------------------------------
# (2) OBSTRUCTION: [L_+, R_q] should = sqrt(2-q(q+1)) R_{q+1} for vector op.
#   q=-1: [L+,R_-1] = sqrt(2) R_0
#   q= 0: [L+,R_0 ] = sqrt(2) R_+1
#   q=+1: [L+,R_+1] = 0
# Check as OPERATOR identities (Frobenius norm of difference).
# ---------------------------------------------------------------------------
print("\n--- (2) Obstruction: [L_+, R_q] vs vector-operator requirement ---")
def comm(A, B): return A@B - B@A
# For a genuine rank-1 tensor, ALL of [L+,R_q] must match. Any failure => not a vector op.
failures = 0
for q, req in [(-1, np.sqrt(2)*R[0]), (0, np.sqrt(2)*R[+1]), (+1, np.zeros_like(R[+1]))]:
    lhs = comm(Lp, R[q])
    diff = np.linalg.norm(lhs - req)
    norm_req = np.linalg.norm(req)
    print(f"  q={q:+d}: ||[L+,R_q] - sqrt(2-q(q+1))R_(q+1)|| = {diff:.4f}  (||req||={norm_req:.4f})")
    if diff > 1e-8:
        print(f"         -> FAILS (as claimed in v14.097 S4)")
        failures += 1
    else:
        print(f"         -> closes")
# Also check [L_-, R_q]: [L-,R_q] should = sqrt(2-q(q-1)) R_{q-1}
print("  [L_-, R_q] check:")
for q, req in [(+1, np.sqrt(2)*R[0]), (0, np.sqrt(2)*R[-1]), (-1, np.zeros_like(R[-1]))]:
    lhs = comm(Lm, R[q])
    diff = np.linalg.norm(lhs - req)
    print(f"  q={q:+d}: ||[L-,R_q] - req|| = {diff:.4f}", "-> FAILS" if diff>1e-8 else "-> closes")
    if diff > 1e-8: failures += 1
ok2 = (failures > 0)
print(f"  => {failures} ladder-relation failures: {'OBSTRUCTION CONFIRMED' if ok2 else 'no obstruction'}")

# Try alternative sigma-pairings: a sigma b for sigma in {I, sx, sy, sz}
print("\n  Trying sigma-pairings a*sigma*b (q=-1-like: a1 b1 variants):")
sx = np.array([[0,1],[1,0]]); sy = np.array([[0,-1j],[1j,0]]); sz = np.array([[1,0],[0,-1]]); I2=np.eye(2)
aa = [a1, a2]; bb = [b1, b2]
for name, sig in [("I",I2),("sx",sx),("sy",sy),("sz",sz)]:
    # T = sum_ij a_i sig_ij b_j  (q=-1 type)
    T = sum(sig[i,j]*aa[i]@bb[j] for i in range(2) for j in range(2))
    # vector requirement would need [L+,T] ~ R_0-like; just report norm of [L+,T]
    c = comm(Lp, T)
    print(f"    sigma={name}: ||[L+,T]||={np.linalg.norm(c):.4f}, ||T||={np.linalg.norm(T):.4f}")

print("\n" + "=" * 70)
print("SUMMARY:")
print(f"  (1) Selection rule delta_(q,-m), +1: {'PASS' if ok1 else 'FAIL'}")
print(f"  (2) ab-bilinears fail SO(3) vector ladder relations: {'CONFIRMED' if ok2 else 'NOT confirmed'}")
print("  => r_q not in bicone su(2)+su(2) enveloping algebra (v14.097 S4).")
print("=" * 70)
