#!/usr/bin/env python3
"""Leading micromotion coefficient for the resonant linear magnetic driver."""
import math
for n in (1,2,3,4,5,6):
    j=n/2
    p=1/(2*n)
    C=math.sqrt(n)/(4*math.sqrt(2))*(1-1/(2*n))**(n-.5)
    print(f"j={j:g}  C_j={C:.15g}  p*={p:.15g}")
print("Predicted E_pop^max = C_j * epsilon + O(epsilon^2) for fixed j.")
