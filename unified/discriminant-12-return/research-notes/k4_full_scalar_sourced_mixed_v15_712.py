#!/usr/bin/env python3
"""v15.712: source-before-constraint mixed K4 scalar couplings.

Re-executes frozen v14.935 scalar matter and EH payloads in a temporary
directory, then reconstructs their original E=0-gauge Fourier Lagrangian.
Extracts exact sourced ADM lapse/shift mixed interactions on the tau=1
K4 background. This is NOT a sourced scalar pole or tidal readout;
time-dependent coefficients must be differentiated before freezing.
"""
import pickle
import subprocess
import sys
import tempfile
from pathlib import Path
import sympy as s

payload=Path(__file__).resolve().parent.parent/"payloads"/"k4_full_svt_v14_935"
with tempfile.TemporaryDirectory() as tmp:
    for name in ("matter_sector.py","eh_scalar.py"):
        subprocess.run([sys.executable,str(payload/name)],cwd=tmp,
                       capture_output=True,text=True,check=True)
    with open(Path(tmp)/"matter_scalar.pkl","rb") as fp:
        Lm=s.sympify(pickle.load(fp)["L2"])
    with open(Path(tmp)/"eh_scalar.pkl","rb") as fp:
        Le=s.sympify(pickle.load(fp)["L2"])

a,adot,kappa,C,eta,k=s.symbols("a adot kappa C eta k")
Phi,B,psi,E,P=s.symbols("Phi B psi E P")
psi_t,E_t,P_t=s.symbols("psi_t E_t P_t")
replacements={
 "Phi":Phi,"psi":psi,"Ezz":-k*k*E,"Bz":-k*B,"Bzz":-k*k*B,
 "psi_z":-k*psi,"psi_zz":-k*k*psi,"psi_t":psi_t,
 "E_zzz":k**3*E,"E_zzzz":k**4*E,"E_zzt":-k*k*E_t,
 "Pzz":-k*k*P,"Pzt":-k*P_t}
def fourier(expr):
    for name,val in replacements.items():
        expr=expr.subs(s.Symbol(name),val)
    return s.expand(expr)

L=s.expand((fourier(Lm)+fourier(Le)).subs({E:0,E_t:0}))
H=s.hessian(L,(Phi,B))
d=s.Matrix([s.diff(L,Phi),s.diff(L,B)]).subs({Phi:0,B:0})
H_expected=s.Matrix([
 [a*(kappa*C-9*adot**2)/kappa,2*a*adot*k*k/kappa],
 [2*a*adot*k*k/kappa,a*k*k*(9*adot**2-kappa*C)/(3*kappa)]])
assert (H-H_expected).applyfunc(s.simplify)==s.zeros(2)
on={a:1/s.sqrt(3),adot:1/s.sqrt(3),C:1,kappa:1}
Hon=H.subs(on)
don=d.subs(on)
assert s.simplify(Hon.det()+4*k*k*(1+k*k)/9)==0
d_expected=s.Matrix([
 2*s.sqrt(3)*(P*k*k-3*k*k*psi-3*psi-3*psi_t)/9,
 -2*k*k*(P_t-3*psi_t)/9])
assert (don-d_expected).applyfunc(s.simplify)==s.zeros(2,1)
Jp,Jb=s.symbols("J_Phi J_B")
J=s.Matrix([Jp,Jb])
linear=-(J.T*Hon.inv()*don)[0]
Fphi=(P*k*k+P_t*k*k-3*k*k*psi-3*k*k*psi_t-3*psi-3*psi_t)/(3*(k*k+1))
Fb=-s.sqrt(3)*(P*k*k-P_t-3*k*k*psi-3*psi)/(3*(k*k+1))
assert s.simplify(linear-Jp*Fphi-Jb*Fb)==0
L00=L.subs({Phi:0,B:0}).subs(on)
Lred=s.expand(L00-s.Rational(1,2)*(don.T*Hon.inv()*don)[0])
assert s.simplify(Lred.coeff(psi_t,2))==0
assert s.simplify(s.diff(Lred,psi_t,P_t))==0
assert s.simplify(Lred.coeff(P_t,2)-s.sqrt(3)*k**4/(27*(k*k+1)))==0
print("PASS: full frozen K4 scalar quadratic action independently reconstructed")
print("PASS: exact sourced scalar mixed couplings before scalar constraint reduction")
print("F_Phi=",s.factor(Fphi))
print("F_B=",s.factor(Fb))
print("WARNING: freezing tau=1 BEFORE sourced EOM does not determine scalar pole")
