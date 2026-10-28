"""Additive exact psi certificate runner; execute inside v14.996 payload directory.
python psi_certificate_runner.py
Requires sympy and the existing scalar_adm2.py. Fails closed on residual.
"""
import sympy as s
exec(open("scalar_adm2.py").read())
L=s.expand(L2b.subs(s.diff(a,t),1/s.sqrt(3)).subs(a,t/s.sqrt(3)).subs({C:1,kap:1}))
D=lambda f:s.diff(f,t)
EL=lambda expr,v:s.expand(s.diff(expr,v)-s.diff(s.diff(expr,D(v)),t))
EB,EP=EL(L,B),EL(L,Phi)
phi_aux=s.solve(EB,Phi)[0]
b_aux=s.solve(s.expand(EP.subs(Phi,phi_aux)),B)[0]
phi_aux=s.expand(phi_aux.subs(B,b_aux))
R=s.expand(L.subs({Phi:phi_aux,B:b_aux}))
Epsi,Epi=EL(R,psi),EL(R,pi)
psi_sol=s.factor(s.solve(Epsi,psi)[0])
# Match source-faithful v14.996 elimination of Epsi and its time derivative.
epsi_dt=s.expand(s.diff(Epsi,t))
psi_dot_sol=s.expand(s.solve(epsi_dt,D(psi))[0].subs(psi,psi_sol))
Epi_red=s.expand(Epi.subs({psi:psi_sol,D(psi):psi_dot_sol}))
pdd=s.diff(pi,(t,2)); pd=D(pi)
c2=s.factor(Epi_red.coeff(pdd))
remain=s.expand(Epi_red-c2*pdd)
c1=s.factor(remain.coeff(pd))
remain2=s.expand(remain-c1*pd)
c0=s.factor(s.simplify(remain2/pi))
assert s.simplify(remain2-c0*pi)==0, "Unresolved reduced scalar terms"
P=s.factor(c1/c2); Q=s.factor(c0/c2)
assert s.simplify(P-3/t)==0 and s.simplify(Q-(3*k*k+4)/t**2)==0, "Oscillator mismatch"
A=s.factor(s.diff(psi_sol,pi)); Bcoef=s.factor(s.diff(psi_sol,pd))
rest=s.simplify(psi_sol-A*pi-Bcoef*pd)
with open("psi_certificate.txt","w") as f:
    for name,val in [("psi_sol",psi_sol),("psi_pi_coeff",A),("psi_dotpi_coeff",Bcoef),
       ("other_reconstruction_terms",rest),("psi_dot_sol",psi_dot_sol),
       ("pi_ode_P",P),("pi_ode_Q",Q),
       ("psi_pi_coeff_low_k",s.limit(A,k,0,dir="+")),
       ("psi_dotpi_coeff_low_k",s.limit(Bcoef,k,0,dir="+"))]:
        f.write(f"{name} = {val}\n")
assert rest==0, "Reconstruction uses derivatives beyond pi and dotpi"
print("psi_certificate.txt generated; reduced scalar oscillator matches corrected v14.996")
