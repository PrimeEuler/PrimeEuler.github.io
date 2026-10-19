import numpy as np
from math import sqrt, pi

# SHAPE/READ channel (axial field, cos th): w_j = (j+1)/sqrt((2j+1)(2j+3))     [v14.626]
def w(j): return (j+1) / sqrt((2*j+1)*(2*j+3))
# DRIVE channel (transverse tipping field, sin th * e^{i phi}): the NMR/Rabi coupling.
# <j+1, m+1| sin th e^{i phi} |j, m> = -sqrt((j+m+1)(j+m+2)/((2j+1)(2j+3)));  at m=0:
def u(j): return sqrt((j+1)*(j+2) / ((2*j+1)*(2*j+3)))

print("drive weights u_j (m=0 -> m=1):")
for j in (0, 1, 2, 5, 10, 50):
    print(f"  u_{j} = {u(j):.10f}   axial w_{j} = {w(j):.10f}   ratio u/w = {u(j)/w(j):.10f}  sqrt((j+2)/(j+1)) = {sqrt((j+2)/(j+1)):.10f}")

print("\nclimb products: is  Prod u_j  =  Prod w_j * sqrt(J+1)  exact?")
for J in (1, 2, 3, 5, 10, 30, 100):
    Pw = np.prod([w(j) for j in range(J)])
    Pu = np.prod([u(j) for j in range(J)])
    print(f"  J={J:4d}: Prod u = {Pu:.6e}   Prod w * sqrt(J+1) = {Pw*sqrt(J+1):.6e}   ratio = {Pu/(Pw*sqrt(J+1)):.15f}")
print("\n=> drive climb ~ sqrt(pi/2)*sqrt(J+1)*2^-J : same Wallis skeleton as the axial channel,")
print("   related by the exact factor sqrt(J+1) -- zero free parameters in the map.")
