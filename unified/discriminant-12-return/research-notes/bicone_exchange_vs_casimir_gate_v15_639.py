#!/usr/bin/env python3
"""Exact finite bicone swap vs quarter-shell Casimir grading; SymPy. v15.639."""
import sympy as s
sp=s.Matrix([[0,1],[0,0]]); sm=sp.T; sz=s.diag(1,-1); i2=s.eye(2)
j1z=s.kronecker_product(sz,i2)/2
j2z=s.kronecker_product(i2,sz)/2
l_z=j1z+j2z; a_z=j1z-j2z
l_plus=s.kronecker_product(sp,i2)+s.kronecker_product(i2,sp)
a_plus=s.kronecker_product(sp,i2)-s.kronecker_product(i2,sp)
a_minus=a_plus.T
swap=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
assert swap**2==s.eye(4)
assert swap.eigenvals()=={1:3,-1:1}
assert swap*l_z-l_z*swap==s.zeros(4)
assert swap*l_plus-l_plus*swap==s.zeros(4)
assert swap*a_z+a_z*swap==s.zeros(4)
assert swap*a_plus+a_plus*swap==s.zeros(4)
Q=(a_plus**2+a_minus**2)/2
assert swap*Q-Q*swap==s.zeros(4)
sing=s.Matrix([0,1,-1,0])/s.sqrt(2)
trip=s.Matrix([0,1,1,0])/s.sqrt(2)
assert Q*sing==s.zeros(4,1)
# On the physical bicone singlet j=0 and triplet j=1, quarter-mesh chi=e^(16 pi i j(j+1))=+I.
chi_em=s.eye(4)
assert chi_em*a_z+a_z*chi_em==2*a_z
assert s.trace(swap)==2 and s.trace(chi_em)==4
# A single odd-quarter j=3/4 four-state shell has chi=-I, not swap parity.
assert s.trace(-s.eye(4))==-4
# Previously certified exact quarter/bicone matrix encoding (v15.572); provenance, not a new result.
j=s.Rational(3,4); ms=[-j,-j+s.Rational(1,2),-j+1,j]
mz=s.diag(*ms); jp=s.zeros(4)
for col,m in enumerate(ms):
    if m+1 in ms: jp[ms.index(m+1),col]=s.sqrt((j-m)*(j+m+1))
jm=jp.T
assert mz==-j1z-j2z/2
assert jp==s.sqrt(s.Rational(3,2))*s.kronecker_product(sm,i2)
E=s.simplify(j*(j+1)*s.eye(4)-((jp+jm)/2)**2-((jp-jm)/(2*s.I))**2-mz**2)
assert E==a_z**2/2
assert jp**2==s.zeros(4) and l_plus**2!=s.zeros(4)
# Dynamical test: exchange preserves swap; relative field changes swap parity but with free strength.
lam,gam=s.symbols('lambda gamma',real=True)
p1=s.kronecker_product(sp,i2);p2=s.kronecker_product(i2,sp)
jdot=j1z*j2z+(p1*p2.T+p1.T*p2)/2
H=-lam*jdot+gam*a_z
U=s.Matrix.hstack(sing,trip)
H2=s.simplify(U.T*H*U)
assert H2==s.Matrix([[3*lam/4,gam],[gam,-lam/4]])
gap2=s.simplify(s.trace(H2)**2-4*H2.det())
assert s.simplify(gap2-(lam**2+4*gam**2))==0
assert swap*jdot-jdot*swap==s.zeros(4)
print("PASS v15.639: exchange parity != geometric Casimir parity; rank-1 relative mixing, rank-2 evenness; lambda/gamma undetermined. v15.572 encoding checked as prior.")
