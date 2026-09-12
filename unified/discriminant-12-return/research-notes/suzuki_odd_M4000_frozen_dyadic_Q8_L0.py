#!/usr/bin/env python3
"""Frozen exact-dyadic odd-sector verifier inputs at M=4000.

Q is the 10x8 midpoint candidate-positive basis (Schur directions 3..10),
frozen as exact IEEE-754 dyadics. L0 is the frozen 8x8 lower-triangular
preconditioner. The verifier must not regenerate either object.

An exact Fraction determinant check on rows (0,3,4,5,6,7,8,9) proves rank(Q)=8.
All nonzero diagonal entries of L0 prove exact invertibility.
"""
from fractions import Fraction

Q_HEX = [
    ['-0x1.14e7a8a982ed0p-2', '0x1.40788673e3addp-2', '-0x1.558aca3873c01p-2', '-0x1.9189e16456320p-1', '0x1.36ebee434c857p-4', '-0x1.b268b0182d3c1p-5', '-0x1.2b210a8115a72p-7', '-0x1.0a1de1bceac8fp-10'],
    ['0x1.23f01ef166402p-2', '-0x1.6e68ca3a80470p-5', '-0x1.dfbff3966ce78p-5', '-0x1.975bbe48f696ep-2', '0x1.1a6a970374b6ap-4', '-0x1.24fc4886a1536p-4', '-0x1.9a2a8d4cdfc26p-6', '-0x1.8cff9eb3ac762p-6'],
    ['0x1.88e1011e90de8p-1', '0x1.55730d7580d69p-2', '-0x1.a1c59365c6d56p-4', '0x1.c4b20887c2d21p-4', '-0x1.103604ad4ea44p-4', '0x1.12a078ac63b17p-4', '0x1.9be220965fa04p-5', '0x1.895dcf7b1536bp-5'],
    ['-0x1.6bd31ba660646p-2', '0x1.14a809019f600p-1', '-0x1.a3e059f18d811p-3', '0x1.15a9624374b7dp-3', '-0x1.34c74aad49ae2p-4', '0x1.3119c40a40a02p-4', '0x1.c79aa0ea68caap-5', '0x1.9626100a98961p-5'],
    ['0x1.16f286b02496ep-3', '-0x1.8c3d36a0c7d20p-2', '-0x1.7f94fa8d3ab4bp-3', '0x1.02bbc9552c1c4p-3', '-0x1.2d7726d7831acp-4', '0x1.28d667fd55a1ap-4', '0x1.c8da69a181c5ep-5', '0x1.9a9a7fb37354bp-5'],
    ['0x1.0105d18e3d05ep-4', '-0x1.64e90eefdb388p-4', '0x1.f575d0ae2970bp-1', '0x1.a186f6525dd9dp-3', '-0x1.d4192db0b8e79p-4', '0x1.ce8af20b470dep-4', '0x1.60b84386ad0f0p-4', '0x1.35d72dc266a7ap-4'],
    ['-0x1.2131e761fce8fp-3', '0x1.06df4ddb558b6p-3', '0x1.53728de361f82p-4', '-0x1.22b5b9ac34338p-4', '-0x1.f810536ad0967p-4', '0x1.e983b6c1de3b2p-4', '0x1.80574e2e888c7p-4', '0x1.5802c4ce99d36p-4'],
    ['0x1.01480572f12cap-3', '-0x1.d500572333acbp-4', '-0x1.81271b89c4272p-4', '0x1.43eb2fce19a85p-4', '0x1.f2dc178221056p-1', '0x1.abc467210319fp-4', '0x1.4a22365f2dd36p-4', '0x1.26d36bec00d1ap-4'],
    ['-0x1.083fca9d65f4cp-3', '0x1.e7d8eff255992p-4', '0x1.7225eec577659p-4', '-0x1.3642685e06cbfp-4', '0x1.f74a34cf0d45dp-4', '0x1.f962d511328fcp-1', '-0x1.a06881bb81f55p-4', '-0x1.7290e4990f62ap-4'],
    ['0x1.31458cfd4f0fbp-3', '-0x1.1bf8794e27876p-3', '-0x1.b89e73a2e4214p-4', '0x1.729deae87aef8p-4', '-0x1.c976aa22af291p-4', '0x1.d4bda2ff992a5p-4', '-0x1.f03f37c42af79p-1', '-0x1.c450683371ecdp-4'],
]

L0_HEX = [
    ['0x1.b17b78106c211p-17', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
    ['-0x1.26163028480b8p-39', '0x1.d37a7e752c400p-10', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
    ['-0x1.5e1a5da71e1dap-38', '0x1.691427f822c86p-42', '0x1.75989167a7720p-4', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
    ['0x1.beb2c9ca3be24p-38', '-0x1.eccacbf3360a4p-42', '-0x1.3bcf4f19dbd00p-46', '0x1.4dfeadf9431acp-1', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
    ['-0x1.d094bf6783a10p-39', '0x1.d4b136bf63d0cp-43', '0x1.6dba37632fc60p-47', '0x1.8cb69a7792730p-50', '0x1.5dc69fb9c65d2p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
    ['0x1.ce599756bbf0cp-39', '-0x1.bdba613ecb3e8p-43', '-0x1.8d241189d1f00p-47', '0x1.41fd7aaa8fd44p-49', '0x1.7dca09bc63848p-53', '0x1.7e4553298bd62p+0', '0x0.0p+0', '0x0.0p+0'],
    ['0x1.57ec22f677bf0p-39', '-0x1.5d50f36dd2548p-43', '-0x1.3104518cf6af0p-47', '0x1.52e177d779480p-50', '0x1.00d1344499100p-53', '-0x1.f761f70a5b800p-56', '0x1.8f2e8c6e3c3e4p+0', '0x0.0p+0'],
    ['0x1.30352050946d0p-39', '-0x1.344499ec92850p-43', '-0x1.130336e41ec00p-47', '0x1.3eab860a2c940p-50', '0x1.ea0e23a9eac00p-54', '-0x1.4fef927164c00p-56', '0x1.7e48a39c57800p-58', '0x1.95afca314381ep+0'],
]

ROWS = (0,3,4,5,6,7,8,9)

def F(x):
    n,d = float.fromhex(x).as_integer_ratio()
    return Fraction(n,d)

def det_exact(M):
    A=[[F(x) for x in row] for row in M]
    n=len(A); det=Fraction(1)
    for i in range(n):
        p=next(r for r in range(i,n) if A[r][i])
        if p!=i:
            A[i],A[p]=A[p],A[i]; det=-det
        piv=A[i][i]; det*=piv
        for r in range(i+1,n):
            if A[r][i]:
                q=A[r][i]/piv
                for c in range(i+1,n):
                    A[r][c]-=q*A[i][c]
                A[r][i]=Fraction(0)
    return det

if __name__ == "__main__":
    minor=[[Q_HEX[r][c] for c in range(8)] for r in ROWS]
    d=det_exact(minor)
    assert d != 0
    assert all(float.fromhex(L0_HEX[i][i]) != 0.0 for i in range(8))
    print("exact rank(Q)=8")
    print("minor determinant =", d)
    print("L0 exactly invertible")
