import numpy as np
from math import sqrt

def w(j):  # rank-1 axial weights (v14.626)
    return (j+1)/sqrt((2*j+1)*(2*j+3))
def v(j):  # rank-2 up-weight <j+2,0|P2|j,0> = (3/2) w_j w_{j+1}
    return 1.5*(j+1)*(j+2)/((2*j+3)*sqrt((2*j+1)*(2*j+5)))
def d2(j): # rank-2 diagonal <j,0|P2|j,0> = (3(w_j^2 + w_{j-1}^2) - 1)/2, w_{-1}:=0
    wm = w(j-1) if j >= 1 else 0.0
    return (3*(w(j)**2 + wm**2) - 1)/2

# --- verify against explicit matrix: P2 = (3 cos^2 - 1)/2 in the |j,0> basis
J = 60
C = np.zeros((J, J))
for j in range(J-1):
    C[j, j+1] = C[j+1, j] = w(j)
P2 = (3*C@C - np.eye(J))/2
mask = np.ones((J, J), bool)
for j in range(J):
    for k in range(J):
        if abs(j-k) in (0, 2): mask[j, k] = False
print(f"selection rule: max |P2| entry with |dj| not in {{0,2}}: {np.abs(P2[mask]).max():.2e}  (machine zero)")
print(f"up-weight check:  max |P2[j,j+2] - v(j)| = {max(abs(P2[j, j+2]-v(j)) for j in range(J-2)):.2e}")
print(f"diagonal check:   max |P2[j,j] - d2(j)|  = {max(abs(P2[j, j]-d2(j)) for j in range(J)):.2e}")
print("\nrank-2 weights v_j -> 3/8 from above:")
for j in (0, 1, 2, 5, 10, 50):
    print(f"  v_{j} = {v(j):.10f}   diag d2_{j} = {d2(j):+.10f}")

print("\nclimb products (rank-2 preserves parity -> two independent chains):")
for name, start in (("even", 0), ("odd", 1)):
    for N in (5, 10, 20):
        P = np.prod([v(start+2*k) for k in range(N)])
        print(f"  {name} chain, {N:2d} steps: Prod = {P:.4e}   Prod/(3/8)^N = {P/(3/8)**N:.6f}")

print("\n=== tidal coupling beta2 = 2 G M_s I^2 / (hbar^2 R^3);  well depth U = G M_s I / R^3 ===")
hbar = 1.054571817e-34; G = 6.67430e-11; gE = 9.81
def budget(tag, I, Mtot, Ms, R):
    U = G*Ms*I/R**3
    b2 = 2*G*Ms*I**2/(hbar**2 * R**3)
    wlib = sqrt(2*U/I)
    earth_tide = I * 2*gE/6.371e6            # Earth's own gravity-gradient well depth (2g/R_E)
    l_tol = U/(Mtot*gE)                     # CM-balance tolerance: rank-1 Earth leakage = signal
    print(f"{tag}: U={U:.2e} J, beta2={b2:.2e}, libration f={wlib/2/np.pi:.2e} Hz")
    print(f"    Earth tidal background well = {earth_tide:.2e} J  ({earth_tide/U:.1f}x signal, static/known)")
    print(f"    CM balance tolerance (rank-1 leakage = signal): l << {l_tol:.1e} m")
budget("nano (I=1.92e-31), 1 mg at 1 mm ", 1.92e-31, 7.78e-18, 1e-3, 1e-3)
budget("bench (I=1e-4), 10 kg at 10 cm  ", 1e-4, 0.1, 10.0, 0.10)
