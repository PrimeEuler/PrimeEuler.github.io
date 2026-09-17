#!/usr/bin/env python3
"""Exact-rational certificate for the frozen M16001 low-coordinate basis.

Reconstruct Q and L0 from the canonical binary64 hexadecimal payloads, solve
P L0^T = Q exactly over Fraction, construct a deterministic exact null basis
N of ker(Q^T) using pivot rows 0..5 and free rows 6..9, and certify
B=[P,N] is nonsingular.  No floating linear algebra is used.
"""
from fractions import Fraction
import hashlib

Q_HEX = [
['0x1.a9b0106ac01e8p-4','0x1.50e85227b79f2p-5','0x1.110e340c239ffp-7','-0x1.26a56146f4c61p-9','-0x1.c3bc320065106p-12','-0x1.3ddf24d66961ap-9'],
['0x1.31614dcd93fadp-2','0x1.f5ac98952c139p-4','0x1.a3f768a3f4820p-6','-0x1.d238dc60d4bc0p-8','-0x1.5b42f56f67900p-10','-0x1.f257751033980p-8'],
['0x1.ce789977291cdp-2','0x1.9b6445cd32180p-3','0x1.710376b61e89ep-5','-0x1.b443abef4fc9cp-7','-0x1.30a7867c4bda8p-9','-0x1.c82d01295d99ep-7'],
['0x1.12868d5f20568p-1','0x1.17dbd9766c281p-2','0x1.1a23c7dfb9336p-4','-0x1.75e2ce9fbf67cp-6','-0x1.c8458b60c3edep-9','-0x1.75967d178eb3ep-6'],
['0x1.fe7099bce9880p-12','-0x1.6029608f09120p-12','-0x1.0b6cac294ebf3p-4','0x1.e3081403468f4p-3','-0x1.de674a31d9b83p-1','-0x1.092202100922cp-2'],
['0x1.78ae806502bb8p-2','0x1.73a4763af9621p-2','0x1.3eb502e4eff0dp-3','-0x1.7fefb6818df0cp-4','-0x1.ecb9b14c73288p-7','-0x1.2bf87ac4484d6p-4'],
['-0x1.ae668ca1cd0f0p-3','0x1.596694f849d90p-4','0x1.5de702d2aa8f2p-2','-0x1.a2b41e5441d46p-1','-0x1.0cbaa50837aebp-3','-0x1.6e2e1c3e46549p-2'],
['-0x1.5706bcc587e32p-2','0x1.ab01142a9e1b8p-2','0x1.49a79c77f13f3p-1','0x1.ec9bd6cef6483p-2','0x1.09f8afc5c94a0p-3','-0x1.8c7426ec776aep-3'],
['-0x1.5886f59dbcaa3p-2','0x1.70067d3c53b3dp-1','-0x1.900a8aa8bfe82p-2','-0x1.36755ea389b2ep-3','-0x1.030b5f2af21c4p-3','0x1.a98d4a3cfb6f8p-2'],
['0x1.ffa22a56bf28ep-5','-0x1.93cc3126d01fep-3','0x1.0ef7cb0da9f59p-1','-0x1.ba679d6129a27p-4','-0x1.1b6a2e159d855p-2','0x1.88dcec0ac34b7p-1']]
L0_HEX = [
['0x1.9be6472ce844cp-13','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['0x1.1bc7b425ec472p-43','0x1.e1d13acd74362p-7','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.0334f3068864cp-42','-0x1.bebb714d496d0p-50','0x1.c1a4c3504ca1fp-1','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.8f493ba5ca6eep-42','0x1.1aa47eb676025p-48','0x1.86ea932041c6ap-52','0x1.4dfa151bb0094p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.d4b7b575bf7d5p-44','0x1.a231497eb8b46p-48','0x1.80e1a99ec70cfp-52','0x1.670073992bbbdp-56','0x1.6b6c07a0eec9ap+0','0x0.0p+0'],
['0x1.e1711cbdb3146p-42','0x1.d0b5ccbc83ab6p-50','-0x1.452798c7f5298p-50','0x1.6dad86e75f51ap-53','0x1.a00d12034cd1fp-54','0x1.883bd6fde0ad5p+0']]

def fhex(s): return Fraction.from_float(float.fromhex(s))
def lower_solve(L,b):
    x=[]
    for i in range(len(L)):
        x.append((b[i]-sum(L[i][j]*x[j] for j in range(i)))/L[i][i])
    return x

def solve(A,b):
    M=[r[:] + [v] for r,v in zip(A,b)]; n=len(A)
    for c in range(n):
        p=next(r for r in range(c,n) if M[r][c])
        M[c],M[p]=M[p],M[c]
        z=M[c][c]; M[c]=[v/z for v in M[c]]
        for r in range(n):
            if r!=c and M[r][c]:
                z=M[r][c]; M[r]=[M[r][j]-z*M[c][j] for j in range(n+1)]
    return [M[i][-1] for i in range(n)]

def det(A):
    M=[r[:] for r in A]; out=Fraction(1); n=len(M)
    for c in range(n):
        p=next((r for r in range(c,n) if M[r][c]),None)
        if p is None: return Fraction(0)
        if p!=c: M[c],M[p]=M[p],M[c]; out=-out
        z=M[c][c]; out*=z
        for r in range(c+1,n):
            f=M[r][c]/z
            for j in range(c+1,n): M[r][j]-=f*M[c][j]
    return out

def payload(name,M):
    lines=['M16001-RATIONAL-MATRIX-v1',f'name={name}',f'rows={len(M)}',f'cols={len(M[0])}']
    lines += [','.join(f'{x.numerator}/{x.denominator}' for x in row) for row in M]
    return '\n'.join(lines)+'\n'
def digest(name,M): return hashlib.sha256(payload(name,M).encode('ascii')).hexdigest()

def main():
    Q=[[fhex(x) for x in r] for r in Q_HEX]; L=[[fhex(x) for x in r] for r in L0_HEX]
    assert all(L[i][j]==0 for i in range(6) for j in range(i+1,6))
    assert all(L[i][i] for i in range(6))
    P=[lower_solve(L,r) for r in Q]
    assert all(sum(P[r][k]*L[c][k] for k in range(6))==Q[r][c] for r in range(10) for c in range(6))
    A=[[Q[col][row] for col in range(6)] for row in range(6)]
    C=[[Q[col][row] for col in range(6,10)] for row in range(6)]
    assert det(A)!=0
    N=[[Fraction(0) for _ in range(4)] for _ in range(10)]
    for t in range(4):
        x=solve(A,[-C[r][t] for r in range(6)])
        for r in range(6): N[r][t]=x[r]
        N[6+t][t]=1
    assert all(sum(Q[r][c]*N[r][t] for r in range(10))==0 for c in range(6) for t in range(4))
    assert all(N[6+r][c] == (1 if r==c else 0) for r in range(4) for c in range(4))
    B=[P[r]+N[r] for r in range(10)]; db=det(B); assert db!=0
    print('M16001 exact basis certificate')
    for name,M in [('Q',Q),('L0',L),('P',P),('N',N),('B',B)]: print(f'{name:2s} SHA-256 = {digest(name,M)}')
    print('L0 triangular/nonzero diagonal PASS')
    print('P L0^T - Q == 0             PASS')
    print('pivot rows 0..5 nonsingular PASS')
    print('Q^T N == 0                  PASS')
    print('free block == I4            PASS')
    print('rank(N) == 4                PASS')
    print('det(B) != 0                 PASS')
    print('det(B) =',f'{db.numerator}/{db.denominator}')
    print('CERTIFICATE: PASS')
if __name__=='__main__': main()
