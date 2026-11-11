#!/usr/bin/env python3
"""v15.719: source-driven gauge-invariant scalar metric potentials and Weyl tide.

Rebuilds the original v14.935 scalar quadratic EH+solid action using the
additive v15.712 reproducer. Uses the exact v15.717 coasting conserved
source, the *particular* P solution, and solves the original ADM
lapse/shift algebraic constraints before evaluating Bardeen potentials.
The electric Weyl scalar STF formula is separately checked using the
linearized 4D Weyl tensor. This is a prescribed conserved Fourier stress,
not a physically selected matter action, nor complete cosmological detector.
"""
from pathlib import Path
import runpy
import sympy as s

archive=runpy.run_path(str(Path(__file__).with_name(
    "k4_full_scalar_sourced_mixed_v15_712.py")))
H,d=[archive[n] for n in ("H","d")]
a,adot,C,kappa,eta,k=[archive[n] for n in
   ("a","adot","C","kappa","eta","k")]
psi,P,psi_t,P_t=[archive[n] for n in ("psi","P","psi_t","P_t")]
t,sigma,rho0=s.symbols("tau sigma rho0",positive=True,real=True)
b=1+(8*eta-3)*(1+k*k)/3
D=8*eta*(1+k*k)-3*k*k
assert s.simplify(D-3*b)==0
p=sigma/(4*k*k*b)
ps=s.Function("psi")(t)
a_t=t/s.sqrt(3)
JP=s.sqrt(3)*(k*k*sigma*t+4*rho0)/36
JB=-k*k*sigma*t/36
subs={a:a_t,adot:1/s.sqrt(3),C:1,kappa:1,
      P:p,P_t:0,psi:ps,psi_t:s.diff(ps,t)}
q=(-H.subs(subs).inv()*(d.subs(subs)+s.Matrix([JP,JB])))
q=q.applyfunc(s.factor)
phi=q[0];shift=q[1]
# E=0 spatial gauge: Phi_B = Phi + d(a B)/dt,
# Psi_B = psi - H a B, H=1/tau, with g_0z=-a partial_z B.
PhiN=s.factor(phi+s.diff(a_t*shift,t))
PsiN=s.factor(ps-shift/s.sqrt(3))
expectPhi=sigma/24+rho0/(6*t*(1+k*k))
expectPsi=expectPhi-sigma*(8*eta-3)/(12*D)
assert s.simplify(PhiN-expectPhi)==0
assert s.simplify(PsiN-expectPsi)==0
assert s.simplify(s.diff(PhiN,ps))==0
assert s.simplify(s.diff(PsiN,ps))==0
# Source-free arbitrary time-slicing psi cancels from both metric potentials.
slip=s.factor(PhiN-PsiN)
assert s.simplify(slip-sigma*(8*eta-3)/(12*D))==0

# Independent 4D linearized Weyl check in local Minkowski signature (+---).
w=s.symbols("omega",real=True,nonzero=True)
F,S=s.symbols("F S")
q4=s.Matrix([-w,0,0,k])
g=s.diag(1,-1,-1,-1)
h=s.diag(2*F,2*S,2*S,2*S)
def R(a,b,c,d):
    return s.expand((-q4[b]*q4[c]*h[a,d]-q4[a]*q4[d]*h[b,c]
                    +q4[a]*q4[c]*h[b,d]+q4[b]*q4[d]*h[a,c])/2)
Ric=s.Matrix(4,4,lambda i,j:s.expand(sum(
    g[m,m]*R(m,i,m,j) for m in range(4))))
curv=s.expand(sum(g[m,m]*Ric[m,m] for m in range(4)))
def Weyl(a,b,c,d):
    return s.expand(R(a,b,c,d)-s.Rational(1,2)*(
        g[a,c]*Ric[d,b]-g[a,d]*Ric[c,b]-g[b,c]*Ric[d,a]
        +g[b,d]*Ric[c,a])+curv/6*(
            g[a,c]*g[b,d]-g[a,d]*g[b,c]))
E0=s.Matrix(3,3,lambda i,j:Weyl(0,i+1,0,j+1))
Q=s.diag(-s.Rational(1,3),-s.Rational(1,3),s.Rational(2,3))
assert (E0-k*k*(F+S)*Q/2).applyfunc(s.simplify)==s.zeros(3)
# Conformal invariance of 4D Weyl; physical orthonormal tide scales a^-2.
physical=s.factor(k*k*(PhiN+PsiN)/(2*a_t**2))
E=physical*Q
assert s.simplify(s.trace(E))==0
assert s.simplify(s.trace(E*E)-s.Rational(2,3)*physical**2)==0
assert s.simplify(s.trace(Q*Q)-s.Rational(2,3))==0
print("PASS: source-driven Bardeen potentials independent of scalar gauge psi")
print("PASS: four-dimensional electric Weyl STF form and 2/3 norm")
print("PHI_NEWTON=",s.factor(PhiN))
print("PSI_NEWTON=",s.factor(PsiN))
print("WEYL_AMPLITUDE=",physical)
print("WARNING: no selected sigma, no localized matter action, no complete T/V readout")
