#!/usr/bin/env python3
"""Frozen rho=0.02 full-parity endpoint theorem carriers.

Minus endpoint:
  frozen eight-dimensional positive core planes after finite-buffer
  elimination, with Cholesky preconditioners.

Plus endpoint:
  compactly supported two-dimensional negative trial planes.

Every payload scalar is an exact binary64 hexadecimal dyadic.
Runtime checks fail closed on hash mismatch, exact-rank failure, or
nonpositive Cholesky diagonal.
"""
from __future__ import annotations
from fractions import Fraction
import hashlib, json
import numpy as np

EVEN_MINUS_QPOS_HEX = [['-0x1.705ebc15e8670p-3', '0x1.f60d1ec97b001p-1', '0x1.0e70834d8231bp-5', '0x1.a2561987330cap-8', '0x1.6bcdd717d023dp-9', '0x1.600d5380178f9p-10', '-0x1.054570b35c081p-9', '-0x1.898bc13bb39e2p-9'], ['0x1.efdb4700ac7cdp-1', '0x1.4dda48e2927c4p-3', '0x1.908f3501a2820p-5', '0x1.ecf5abd731620p-7', '0x1.ce85ba4578040p-8', '0x1.0faf02e117c80p-10', '-0x1.78b2b88c0dfc0p-8', '-0x1.2b97cc693d400p-7'], ['0x1.2287bcb7021c3p-3', '0x1.41c75165533b1p-4', '0x1.13ba98b6d3566p-4', '0x1.9a4b7e4e741e4p-6', '0x1.9c86c5c3da7e4p-7', '0x1.6cb217e3084c0p-11', '-0x1.55b5e90472d14p-7', '-0x1.1010bd9e6c1e4p-6'], ['0x1.1001f05eb07aep-4', '0x1.751aa895c746ap-5', '0x1.6a168ea6ff0eep-4', '0x1.35fd58c52f506p-5', '0x1.5bf3b0b96f7d6p-6', '0x1.7d565d0b03f00p-14', '-0x1.19fc723d76804p-6', '-0x1.ba9eb627ebde0p-6'], ['-0x1.a72502e6d0c00p-13', '-0x1.40dced35fcdc0p-11', '-0x1.2821973e841a0p-6', '-0x1.09fc6dc17e75fp-4', '-0x1.b3cd7139d45c2p-3', '0x1.e2200576ff698p-1', '-0x1.4a3d11927391fp-3', '-0x1.8c6a5e5a04482p-3'], ['0x1.c38cce1f16fa0p-7', '0x1.84159ca1f9112p-7', '0x1.2f0f8b7df4ed3p-3', '0x1.63e087039f794p-4', '0x1.69a92614df678p-4', '0x1.64b7cf595eaf8p-9', '-0x1.d7fc7c4f3df4cp-5', '-0x1.545465595cce3p-4'], ['-0x1.ffa6069f4afe0p-6', '-0x1.6822d1cd51f80p-6', '0x1.b7a746c2965a3p-3', '0x1.3dfc482a1c3d0p-3', '0x1.95b99d3ed795ap-1', '0x1.0e1d20eb74d48p-4', '-0x1.2aa45a8de1555p-2', '-0x1.845d6207eace5p-2'], ['-0x1.724150d00f020p-6', '-0x1.108aa99c2c40ep-6', '0x1.8ad96ca242b35p-2', '0x1.f708bbf035d28p-2', '-0x1.f89ad779315fbp-2', '-0x1.1ec2fa4142cb1p-3', '-0x1.543a64cb07466p-3', '-0x1.9f0faa7ea359ap-3'], ['0x1.e831220238f70p-6', '0x1.82a5d4f4a5f64p-6', '-0x1.4d5c2b9f9bf20p-9', '-0x1.4ee14a384d5fcp-2', '0x1.6412af33c0542p-3', '0x1.2893e1dbdbd1dp-3', '0x1.82fb5b6186649p-2', '0x1.39df3afb21b54p-2'], ['-0x1.4a23a5ba181ccp-6', '-0x1.12ff688dede12p-6', '0x1.1dd0915ce27f0p-3', '0x1.22958ad8b651cp-1', '0x1.3d43cc1b53fcdp-3', '0x1.acc12d921e789p-3', '0x1.7a6f7aa7270a1p-1', '0x1.e4ebbddbfbdd6p-6'], ['0x1.ea0dbad9a33a0p-10', '0x1.d218e51e64cccp-10', '-0x1.5dbf65c4d54d5p-4', '0x1.b31aed29c78d4p-2', '0x1.29c9045c7a461p-3', '0x1.3223c3dc374f2p-3', '-0x1.a44484d4e8d5ap-2', '0x1.8c9de8b50c5eep-1'], ['-0x1.80c28c1704178p-5', '-0x1.673b668a19907p-5', '0x1.b88f54df37bf7p-1', '-0x1.54f80da1790a8p-2', '-0x1.545a9a434d0e2p-7', '0x1.7ee151e31e994p-5', '-0x1.6bac71073f30cp-9', '0x1.17e8c298b8deep-2']]
EVEN_MINUS_LPOS_HEX = [['0x1.767e00002389dp-4', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'], ['0x1.5647fad8bc3a4p-50', '0x1.92fd366cd2f10p-3', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'], ['0x1.27ec9dc91c7b4p-49', '0x1.10d2f214630d3p-49', '0x1.fcab825bc2598p-2', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'], ['0x1.47f3617c6b1f6p-48', '0x1.ad23e0e0eb46ep-52', '0x1.28fdaf3c7b250p-55', '0x1.06557605ff6a3p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'], ['0x1.3c0ab3c67c288p-50', '0x1.d2ec2a5cede4dp-53', '0x1.8543b71be24abp-51', '0x1.0c371a6c4cf1dp-53', '0x1.4b9a9254fb2a9p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'], ['-0x1.15e544cca6f6bp-48', '-0x1.a7dffca26660ep-52', '0x1.fee19ebed3ea2p-52', '-0x1.5a864b63755fbp-54', '0x1.3739d967a02abp-51', '0x1.68bdcb0cb673cp+0', '0x0.0p+0', '0x0.0p+0'], ['-0x1.c91fa845110d9p-49', '-0x1.a302e650ced47p-51', '0x1.5a4715f8b5f2bp-51', '0x1.82e8c297f2c83p-51', '0x1.6e7c760a38bd7p-51', '0x1.63144f76beb86p-53', '0x1.8eee1ca7270a4p+0', '0x0.0p+0'], ['-0x1.938489603f753p-50', '-0x1.060aaa1b05ffap-49', '-0x1.358d5630cf158p-55', '0x1.82f8b0473ae56p-52', '0x1.112bbaa41811bp-51', '0x1.76a2bbfd35168p-53', '-0x1.a60e920930b85p-51', '0x1.9b4d05ad939dcp+0']]
EVEN_MINUS_SHA256 = "99d84bde14147780b80d5b2de4b9b9c71778e7a9b8ec508cc819be8875b61ce6"

ODD_MINUS_QPOS_HEX = [['-0x1.217cfb01b3e29p-2', '0x1.e71aae21b1f2dp-1', '-0x1.43198ba082cc6p-6', '-0x1.44d0fc141c39bp-6', '-0x1.76b195f76bcd4p-6', '-0x1.2e98fea4b1658p-7', '0x1.dc4c671bf83a3p-9', '-0x1.92d04da85912fp-7'], ['0x1.cce732996dfe0p-1', '0x1.c1d6775cf1d9fp-3', '-0x1.470b6dda62480p-5', '-0x1.6a01fa0847230p-5', '-0x1.c26b4421db490p-5', '-0x1.51eff6e18b220p-6', '0x1.0fb0068bc2200p-7', '-0x1.d7a564174f830p-6'], ['0x1.a91aa6861874dp-3', '0x1.ec91edb7b2b38p-4', '-0x1.1c562ab19bf35p-4', '-0x1.6b408b977c976p-4', '-0x1.0153c29562ec6p-3', '-0x1.472f9335656c3p-5', '0x1.0f93b57faf307p-6', '-0x1.e72db76686360p-5'], ['0x1.8941372253b74p-4', '0x1.03020533d50fcp-4', '-0x1.3e7d422c1a118p-3', '-0x1.12190a93ebc05p-2', '-0x1.f7e0ccc0f43eep-2', '-0x1.cb5d81a2f9030p-4', '0x1.89ba8cf0793b3p-5', '-0x1.7b32533555345p-3'], ['0x1.2cdb4fce72a2ep-3', '0x1.a65d5061c4503p-4', '0x1.3611554105550p-7', '0x1.66e9a00f2ac0dp-3', '0x1.58397b4997f18p-1', '0x1.055d124a4da88p-4', '-0x1.736f46d32936ep-6', '0x1.0916dce86b7b4p-3'], ['0x1.adb84254ddf10p-4', '0x1.28185b4f9efb5p-4', '-0x1.00f5925d94e66p-3', '-0x1.10ac797729ad1p-3', '0x1.ab5e6cfe8cb86p-2', '-0x1.54b8f57a2b85fp-5', '0x1.6d85e018a5569p-5', '-0x1.522debedca25cp-4'], ['0x1.4cc1cc287eafcp-4', '0x1.e785522eb8e4cp-5', '0x1.3cedfb9e97e3fp-5', '0x1.67470e1b8d434p-1', '-0x1.4e4438785c162p-2', '0x1.01573de6f1e1cp-3', '-0x1.75c5a1ea25775p-3', '0x1.bb8a3efcd903cp-2'], ['0x1.d219f85f9fac0p-9', '0x1.56e8174892470p-9', '0x1.127cdd3b44d1cp-3', '-0x1.25c17804c9e40p-1', '-0x1.4a0d1de166280p-7', '0x1.98d5fbd806fccp-7', '-0x1.c23105209c0d9p-2', '0x1.599a682de78ffp-1'], ['0x1.0b34ed6752b6cp-4', '0x1.4e4667dbb5b7dp-5', '-0x1.ba39a27ef0baep-2', '0x1.48c26e675849cp-3', '0x1.9ddce2596d243p-5', '-0x1.8a7d7a9a05496p-4', '-0x1.a01fb50ada0d3p-3', '0x1.4adea9f619741p-3'], ['0x1.411a506696420p-5', '0x1.bb2ae7abffd49p-6', '0x1.b9049d32bb7a3p-4', '-0x1.851ebb2e63f52p-4', '-0x1.783e4936908a2p-5', '0x1.f40c63336eb71p-3', '0x1.a393580fd1d40p-1', '0x1.c4b4ea3965483p-2'], ['0x1.c7c4574ef1b70p-4', '0x1.469d1b53d55dfp-4', '0x1.ac0862f4090bep-1', '0x1.917e6a0b384e8p-5', '-0x1.14f47059354e8p-7', '0x1.829ebe0fa463ap-4', '-0x1.3c76e75157ca6p-3', '-0x1.969f99b67f23ap-3'], ['0x1.9f1f19ea5fef0p-8', '0x1.1161a00a21e34p-8', '-0x1.887cd991ca004p-3', '-0x1.ac148adc3290dp-4', '-0x1.fa0df7db23b78p-6', '0x1.e1decbaa1b654p-1', '-0x1.6b9b94f22933fp-3', '-0x1.765a6659ec50ap-3']]
ODD_MINUS_LPOS_HEX = [['0x1.bcd8cd590305cp-5', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'], ['0x1.13bc715787455p-49', '0x1.261b0ae6408ffp-3', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'], ['-0x1.45d970dd0e27ep-47', '-0x1.54c1803d167d0p-49', '0x1.cf1261f01893dp-1', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'], ['0x1.e071ba07053ddp-50', '0x1.45e3971d57a2dp-56', '0x1.852e616e22b9fp-52', '0x1.376056c91543ap+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'], ['-0x1.d83d37ac21f78p-47', '-0x1.190afafd249c4p-50', '0x1.83959056e4dafp-51', '0x1.1923eaac66f84p-50', '0x1.56bd2a15ef384p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'], ['0x1.c2890d640a654p-55', '0x1.06556bbe71579p-50', '-0x1.f7286f44ad31bp-53', '0x1.f3da22624006fp-54', '-0x1.5032d74058b23p-54', '0x1.725945e911984p+0', '0x0.0p+0', '0x0.0p+0'], ['-0x1.e9af360f6e1e0p-49', '0x1.11389434e5041p-50', '0x1.ac733ad9b2324p-57', '-0x1.2d0a30c17662fp-56', '0x1.70ed4dc653450p-53', '0x1.dd691f2ee502cp-53', '0x1.8f96e9a07494dp+0', '0x0.0p+0'], ['-0x1.f4e045dc4be1cp-51', '-0x1.072a12b7f649cp-49', '-0x1.14bfca99b6f00p-51', '0x1.65564eb4f9dbap-54', '0x1.8802fab0b5e8bp-53', '-0x1.e5a9d1f4b35f8p-55', '0x1.6717920d99865p-53', '0x1.9d53f6c2cf845p+0']]
ODD_MINUS_SHA256 = "2b252375df5805127acb66dcfd9bdb21bb9530c95f062c8bb8fc11bbcec7b224"

EVEN_PLUS_MODES = [1,3]
EVEN_PLUS_QNEG_HEX = [['0x1.0000000000000p+0', '0x0.0p+0'], ['0x0.0p+0', '0x1.0000000000000p+0']]
EVEN_PLUS_LNEG_HEX = [['0x1.8d1ff27dad998p-3', '0x0.0p+0'], ['0x1.85c3255cf21bcp-6', '0x1.5e92fa6d55361p-4']]
EVEN_PLUS_SHA256 = "eb8ddbe867b8bd63a582111adee047ff59ef3103c373d6c23553e0df43ee92d3"

ODD_PLUS_MODES = [2,4,6,8]
ODD_PLUS_QNEG_HEX = [['0x1.fa7b432fe063ep-1', '-0x1.0d0890f1b876fp-3'], ['0x1.0026acd23e31ap-3', '0x1.f7e5a84f7fdb5p-1'], ['0x1.44b325410b993p-6', '-0x1.a6de5c3a54980p-5'], ['-0x1.2d1cde5788328p-4', '-0x1.b6df6332e21a0p-4']]
ODD_PLUS_LNEG_HEX = [['0x1.1781574dc0b83p-3', '0x0.0p+0'], ['0x1.abeb5159ca93ap-53', '0x1.96da7539e1c5cp-6']]
ODD_PLUS_SHA256 = "8dc6e0eb24b62fb553d179fd5796d1c7de5acbc936d7d8f6311c673151a46039"

def floats(rows):
    return np.array([[float.fromhex(x) for x in row] for row in rows])

def exact_first_minor_det(qhex,k):
    a=[[Fraction.from_float(float.fromhex(x)) for x in row] for row in qhex[:k]]
    det=Fraction(1); sign=1
    for j in range(k):
        pivot=next((i for i in range(j,k) if a[i][j]!=0),None)
        if pivot is None: return Fraction(0)
        if pivot!=j: a[j],a[pivot]=a[pivot],a[j]; sign*=-1
        p=a[j][j]; det*=p
        for i in range(j+1,k):
            if a[i][j]==0: continue
            f=a[i][j]/p
            for m in range(j+1,k): a[i][m]-=f*a[j][m]
    return sign*det

def minus_hash(q,l):
    return hashlib.sha256(json.dumps({"Qpos":q,"Lpos":l},sort_keys=True,separators=(",",":")).encode()).hexdigest()

def plus_hash(modes,q,l):
    return hashlib.sha256(json.dumps({"modes":modes,"Qneg":q,"Lneg":l},sort_keys=True,separators=(",",":")).encode()).hexdigest()

def verify():
    for name,q,l,h in (
        ("even-minus",EVEN_MINUS_QPOS_HEX,EVEN_MINUS_LPOS_HEX,EVEN_MINUS_SHA256),
        ("odd-minus",ODD_MINUS_QPOS_HEX,ODD_MINUS_LPOS_HEX,ODD_MINUS_SHA256),
    ):
        if minus_hash(q,l)!=h: raise RuntimeError(name+" hash")
        if exact_first_minor_det(q,8)==0: raise RuntimeError(name+" rank")
        if not np.all(np.diag(floats(l))>0): raise RuntimeError(name+" diagonal")
    for name,m,q,l,h in (
        ("even-plus",EVEN_PLUS_MODES,EVEN_PLUS_QNEG_HEX,EVEN_PLUS_LNEG_HEX,EVEN_PLUS_SHA256),
        ("odd-plus",ODD_PLUS_MODES,ODD_PLUS_QNEG_HEX,ODD_PLUS_LNEG_HEX,ODD_PLUS_SHA256),
    ):
        if plus_hash(m,q,l)!=h: raise RuntimeError(name+" hash")
        if exact_first_minor_det(q,2)==0: raise RuntimeError(name+" rank")
        if not np.all(np.diag(floats(l))>0): raise RuntimeError(name+" diagonal")

if __name__=="__main__":
    verify()
    print("PASS frozen full-endpoint theorem carriers")
