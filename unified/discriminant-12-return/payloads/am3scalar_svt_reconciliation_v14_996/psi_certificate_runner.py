"""Independent reconstruction certificate runner for corrected v14.996 scalar ADM build.
Run in payloads/am3scalar_svt_reconciliation_v14_996/:
  python psi_certificate_runner.py
Outputs psi_certificate.txt; fail closed if oscillator or constraint residual mismatches.
"""
import sympy as s
exec(open("scalar_adm2.py").read())
L = s.expand(L2b.subs(s.diff(a,t),1/s.sqrt(3)).subs(a,t/s.sqrt(3)).subs({C:1,kap:1}))
D=lambda f:s.diff(f,t)
EL=lambda expr,v:s.expand(s.diff(expr,v)-s.diff(s.diff(expr,D(v)),t))
EB,EP=EL(L,B),EL(L,Phi)
phi_aux=s.solve(EB,Phi)[0]
b_aux=s.solve(s.expand(EP.subs(Phi,phi_aux)),B)[0]
phi_aux=s.expand(phi_aux.subs(B,b_aux))
R=s.expand(L.subs({Phi:phi_aux,B:b_aux}))
Epsi,Epi=EL(R,psi),EL(R,pi)
psi_sol=s.factor(s.solve(Epsi,psi)[0])
# Compute reconstruction with derivatives eliminated using the certified reduced EOM.
pdd=s.diff(pi,(t,2))
osc=-(3/t)*D(pi)-(3*k**2+4)/t**2*pi
def on_shell(x):
    x=s.expand(x.subs(psi,psi_sol).doit())
    x=x.subs(pdd,osc)
    return s.factor(x)
psid_sol=s.factor(s.diff(psi_sol,t).doit().subs(pdd,osc))
# The source reduction can contain other Euler constraints; compare Epi after elimination.
scalar_residual=s.factor(Epi.subs(psi,psi_sol).subs(D(psi),psid_sol).subs(pdd,osc).doit())
def coeff(x,field):
    return s.factor(s.diff(x,field))
A=coeff(psi_sol,pi)
Bcoef=coeff(psi_sol,D(pi))
remainder=s.simplify(psi_sol-A*pi-Bcoef*D(pi))
with open("psi_certificate.txt","w") as out:
    for name,val in [
        ("psi_sol",psi_sol),("psi_pi_coeff",A),("psi_dotpi_coeff",Bcoef),
        ("reconstruction_remainder",remainder),("psi_dot_sol",psid_sol),
        ("psi_pi_k0",s.limit(A,k,0,dir="+")),
        ("psi_dotpi_k0",s.limit(Bcoef,k,0,dir="+")),
        ("scalar_EL_residual_on_oscillator",scalar_residual)]:
        out.write(f"{name} = {val}\n")
assert remainder==0, "Reconstruction contains other field structures"
assert s.simplify(scalar_residual)==0, "Scalar EL residual: needs further constraints"
print("Reconstruction coefficient file and on-shell scalar residual verified")
