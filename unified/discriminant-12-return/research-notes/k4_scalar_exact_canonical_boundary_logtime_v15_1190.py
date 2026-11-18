#!/usr/bin/env python3
"""Reproduce exact K4 scalar canonical mode and removable metric-scalar boundary.
Regenerate archived v14.935 matter, EH and lapse/shift-assembled scalar action.
Copy three original source scripts to a temporary directory; never change
archived files or create new pickle artifacts inside the repository.

Optional K4_PAYLOAD_DIR points at the original archived payload directory.
"""
import os, pickle, shutil, subprocess, sys, tempfile
from pathlib import Path
import sympy as s

payload=Path(os.environ.get('K4_PAYLOAD_DIR',Path(__file__).resolve().parent.parent/'payloads'/'k4_full_svt_v14_935'))
assert all((payload/x).exists() for x in ('matter_sector.py','eh_scalar.py','assemble.py'))
with tempfile.TemporaryDirectory() as td:
    dest=Path(td)
    for filename in ('matter_sector.py','eh_scalar.py','assemble.py'):
        shutil.copy2(payload/filename,dest/filename)
        subprocess.run([sys.executable,filename],cwd=dest,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,timeout=160)
    L=s.sympify(pickle.loads((dest/'scalar_reduced.pkl').read_bytes())['Lred'])
a,ad,C,kap,k,eta=s.symbols('a adot C kappa k eta')
P,psi,Pt,psit=s.symbols('P psi P_t psi_t')
t=s.symbols('tau',positive=True)
p=s.Function('P')(t);z=s.Function('psi')(t)
Lbg=s.factor(L.subs({a:t/s.sqrt(3),ad:1/s.sqrt(3),C:1,kap:1}))
Lf=s.expand(Lbg.subs({P:p,psi:z,Pt:s.diff(p,t),psit:s.diff(z,t)}))
EL=lambda X,f:s.factor(s.diff(s.diff(X,s.diff(f,t)),t)-s.diff(X,f))
assert s.simplify(EL(Lf,z))==0
c=2*s.sqrt(3)*k*k/9
F=-c*t*t*(z*p-s.Rational(3,2)*z*z)
Lclean=s.factor(Lf-s.diff(F,t))
assert not Lclean.has(z) and not Lclean.has(s.diff(z,t))
K=s.factor(s.diff(Lclean,s.diff(p,t),2))
M=s.factor(s.diff(Lclean,s.diff(p,t),p))
V=s.factor(-s.diff(Lclean,p,2))
Kexpect=2*s.sqrt(3)*k**4*t**3/(27*(1+k*k))
Mexpect=2*s.sqrt(3)*k**4*t*t/(27*(1+k*k))
Vexpect=2*s.sqrt(3)*k**4*t*(8*eta*(1+k*k)-3*k*k-6)/(81*(1+k*k))
assert s.simplify(K-Kexpect)==0
assert s.simplify(M-Mexpect)==0
assert s.simplify(V-Vexpect)==0
assert s.simplify(s.diff(K,t)/K-3/t)==0
freq2=s.factor((V+s.diff(M,t))/K)
expected=(8*eta*(1+k*k)-3*k*k)/(3*t*t)
assert s.simplify(freq2-expected)==0
Om2=s.factor(freq2-s.diff(s.diff(K,t)/K,t)/2-(s.diff(K,t)/K)**2/4)
nu2=s.factor(t*t*Om2-s.Rational(1,4))
assert s.simplify(nu2-(8*eta*(1+k*k)/3-k*k-1))==0
assert s.simplify(nu2-((8*eta-3)*(1+k*k)/3))==0
for ee in [s.Rational(2,5),s.Rational(3,4),s.Integer(1),s.Rational(3,2)]:
    for kk in [s.Rational(1,10),s.Integer(1),s.Integer(10)]:
        assert nu2.subs({eta:ee,k:kk})>0
Om=s.sqrt(nu2+s.Rational(1,4))/t
assert s.simplify(s.diff(Om,t)/(2*Om)+1/(2*t))==0
print('PASS original archived scalar ADM reconstruction, exact psi total boundary, positive K∝a³')
print('K_PP =',K)
print('M_PdotP =',M)
print('V_PP =',V)
print('omega² =',freq2)
print('nu² =',s.factor(nu2))
print('sigma=-H/2; scalar stable in log-time; no q2-specific physical boost')
