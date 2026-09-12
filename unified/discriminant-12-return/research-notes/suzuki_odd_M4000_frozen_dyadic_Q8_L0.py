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
    ['0x1.b68a6558f161ap-2', '-0x1.f65994010ab67p-3', '0x1.b8268f1544621p-4', '-0x1.0ae21b85f2595p-2', '0x1.967abf5148437p-4', '-0x1.1c9b43df6e740p-3', '-0x1.9da443564ec2fp-5', '-0x1.d771c2537bcb6p-5'],
    ['0x1.b471b5b72ff5bp-5', '-0x1.b486f28fe9488p-2', '0x1.7d1e4f4fec45dp-2', '-0x1.4ca92a6bda0a0p-3', '0x1.05916fdded3d9p-2', '-0x1.04c7907274b62p-1', '-0x1.26defb6c529b0p-3', '-0x1.75a8fdb7d03e8p-3'],
    ['0x1.c06ee18a917cep-2', '-0x1.45d845a0fa579p-2', '0x1.3d31399d877b4p-6', '-0x1.d5d3762340557p-3', '-0x1.2229b6d16d56ap-3', '0x1.579ad8c3a98f9p-1', '0x1.42b2aced9c1c1p-4', '0x1.e0985abf176b4p-4'],
    ['-0x1.4befffc4e9bc3p-1', '-0x1.79a7cadedac64p-2', '0x1.70f0c5aa6df4dp-2', '-0x1.6b6a267fdb42ap-3', '0x1.29f2562b29828p-3', '0x1.9f3e44f9ad1d6p-2', '-0x1.0f81d1d59ff99p-4', '-0x1.a18f79eadaef3p-4'],
    ['-0x1.7bffe760c5e3ap-3', '-0x1.5af72a60aef74p-2', '0x1.33df2080b7b15p-8', '-0x1.1b3023778a89ep-3', '-0x1.62042d752f3edp-1', '-0x1.3adce64050292p-2', '0x1.96825d709937dp-3', '0x1.dd0f13a804289p-2'],
    ['-0x1.054ea69010c26p-6', '-0x1.a72881dbff11dp-5', '-0x1.1fd2ce5264304p-5', '0x1.c1fec7903b244p-5', '0x1.2c15ba0baa62cp-1', '-0x1.1553a94f3665bp-6', '0x1.0f65e8587038bp-4', '0x1.9b139d99eb326p-1'],
    ['0x1.c74fe002b8348p-4', '0x1.1544983a19b68p-1', '0x1.7d31dd6804c9cp-1', '-0x1.3857603b13baep-3', '-0x1.6e9e04422a7b8p-3', '0x1.702ad4c6da111p-5', '-0x1.6a35be7835eb5p-3', '0x1.cf8ca43f4690ep-3'],
    ['0x1.e761345475a39p-7', '0x1.9c9c57d03c154p-4', '0x1.c7a5c544dc8e3p-3', '-0x1.b69c002f22252p-5', '0x1.1dfc3f7dc9a06p-3', '-0x1.4e6290fdfb586p-5', '0x1.e31cc29e77455p-1', '-0x1.48ad8ea275619p-3'],
]

L0_HEX = [
    ['0x1.b17b78106c211p-17', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
    ['-0x1.48210a3aea17ap-40', '0x1.df41e21c98021p-10', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
    ['-0x1.6fe9349f3a544p-39', '0x1.8311f8cc751d0p-45', '0x1.73632603845e5p-4', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
    ['0x1.a234ec4edcee9p-39', '-0x1.850d87670df5bp-44', '0x1.c411e0be02898p-50', '0x1.9d3974904c1d2p-1', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
    ['-0x1.2065ceace0752p-37', '0x1.decc42dd97f24p-45', '0x1.cdc3e8347ea65p-50', '0x1.1245966f64862p-50', '0x1.3adeb0416beabp+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
    ['-0x1.ee324389117b6p-36', '0x1.4310f471af42fp-45', '0x1.ccc1af26d9d52p-49', '0x1.ee61dfd36a27cp-51', '0x1.34ccf694a7ec4p-50', '0x1.58fa855d11b19p+0', '0x0.0p+0', '0x0.0p+0'],
    ['0x1.0b877f1755accp-36', '-0x1.e78be5dd24d79p-45', '-0x1.58eff6b106fcbp-48', '0x1.24e330c07b94ap-52', '0x1.928bbc2cf89f4p-53', '0x1.ab58a81e200aap-53', '0x1.803e1ecc80394p+0', '0x0.0p+0'],
    ['0x1.2fb66047f0b19p-37', '-0x1.fd92aa101c371p-44', '-0x1.718b1e9ce9287p-50', '0x1.85989d4fa05cbp-56', '-0x1.9ad785167a0ffp-53', '-0x1.2b92458212fccp-52', '-0x1.62009274c0048p-53', '0x1.987817b6a6167p+0'],
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
