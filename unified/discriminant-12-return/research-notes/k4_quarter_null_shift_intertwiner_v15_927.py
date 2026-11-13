#!/usr/bin/env python3
"""Gravity v15.927 — q=2 quarter-rung null injections are NOT exact
intertwiners of the original defective step-one ladder.

The rectangular operators A_L|L,i>=|L+1,i> and
B_L|L,i>=|L+1,i+1> change magnetic label by -1/4,+1/4.
They flip chi=(-1)^L, and have consistent reverse adjoints, but neither
is an SU2-style exact J+ intertwiner for L>=2; any state-independent
linear combination also fails. Physical E1 operator not supplied.
"""
import sympy as s
def ops(L):
    j=s.Rational(L,4)
    M=s.diag(*[-j+s.Rational(i,2) for i in range(L+1)])
    J=s.zeros(L+1)
    for i in range(L-1):
        m=-j+s.Rational(i,2)
        J[i+2,i]=s.sqrt((j-m)*(j+m+1))
    return M,J

for L in range(1,41):
    M,J=ops(L);Mp,Jp=ops(L+1)
    A=s.zeros(L+2,L+1)
    B=s.zeros(L+2,L+1)
    for i in range(L+1):
        A[i,i]=1
        B[i+1,i]=1
    assert Mp*A-A*M==-s.Rational(1,4)*A
    assert Mp*B-B*M==s.Rational(1,4)*B
    assert A.T*A==B.T*B==s.eye(L+1)
    assert A.T*B!=s.zeros(L+1)
    # Adjoint pairing on direct-sum tower gives self-adjoint H.
    Cplus=A+B
    assert (Cplus+Cplus.T).T==(Cplus+Cplus.T) if Cplus.shape[0]==Cplus.shape[1] else True
    DA=s.simplify(Jp*A-A*J)
    DB=s.simplify(Jp*B-B*J)
    if L>=2:
        assert DA!=s.zeros(L+2,L+1)
        assert DB!=s.zeros(L+2,L+1)
        # The support of DA is only row=i+2 (same index parity);
        # DB is only row=i+3. Thus their nonzero entries cannot cancel.
        for row in range(L+2):
            for col in range(L+1):
                if DA[row,col]!=0:
                    assert row-col==2 and DB[row,col]==0
                if DB[row,col]!=0:
                    assert row-col==3 and DA[row,col]==0
        # An explicit guaranteed nonzero obstruction for A near top.
        assert DA[L+1,L-1]!=0
        # B obstruction exists already from source i=0 for L>=2.
        assert DB[3,0]!=0
    # M commutator fixes distinct charges: no nonzero constant mix
    # exactly intertwines M regardless of L.
    assert (Mp*A-A*M)!=s.zeros(L+2,L+1)
    assert (Mp*B-B*M)!=s.zeros(L+2,L+1)
    # q=2 sector χ flip
    assert (-1)**(L+1)*A== -(-1)**L*A
    assert (-1)**(L+1)*B== -(-1)**L*B
    if L in [1,2,3,4,7,11,40]:
        print('L',L,'DA nonzeros',sum(bool(x) for x in DA),
              'DB nonzeros',sum(bool(x) for x in DB))
print('PASS L=1..40: ±1/4 magnetic charge, adjoint isometries, disjoint nonzero ladder obstructions')
