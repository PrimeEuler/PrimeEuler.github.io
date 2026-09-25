#!/usr/bin/env python3
"""Frozen exact-dyadic six-direction endpoint verifier inputs.

These payloads are the fresh positive eigendirections and midpoint Cholesky
preconditioners from the rho=0.10 endpoint effective cores in v13.806.

Sign convention for each eigenvector column:
the component of largest absolute value is chosen positive.

Every hexadecimal literal is an exact IEEE-754 binary64 dyadic.  The verifier
must treat these values as fixed mathematical inputs and must not regenerate
eigenvectors or Cholesky factors during an outward replay.

Payload hashes use JSON serialization with keys Q,L0, compact separators, and
sort_keys=True.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import numpy as np


EVEN_Q_HEX = [
['0x1.119fbf33644c9p-1','0x1.109235977ddc8p-5','0x1.ea63d63b39210p-7','0x1.cfcfbb731f5d8p-9','-0x1.4e20f7f0b9374p-7','-0x1.2a796189c9b4ap-6'],
['0x1.59ed68b328e52p-2','0x1.6f958cd880b38p-5','0x1.78c0fd035d300p-6','0x1.a5d22e9893a00p-10','-0x1.093f89fdd3fa0p-6','-0x1.de3d17e554c20p-6'],
['-0x1.14fa9097f2bbdp-6','-0x1.046d1768d7811p-4','-0x1.8a4d4d5dc8f55p-3','0x1.e068e7a02daf2p-1','-0x1.54c99e26395d4p-3','-0x1.cc07599765d6dp-3'],
['0x1.f3403ee8bd41cp-3','0x1.74e0c89c8c571p-4','0x1.69435aa8af864p-4','-0x1.0e6d418c64244p-10','-0x1.b08df5ab8550bp-5','-0x1.6b372e86fec3fp-4'],
['0x1.2e5e1b655dd20p-3','0x1.3c977f7444a79p-3','0x1.936c4ac1a0c88p-1','0x1.fd9dadb7fcc1fp-6','-0x1.1392415a08acfp-2','-0x1.a00c912f2885ep-2'],
['0x1.6cd11398a06c6p-2','0x1.f33c6884022b5p-2','-0x1.009c27f8b98aap-1','-0x1.1b689b2951fa1p-3','-0x1.316293bcc051bp-3','-0x1.af0899ae80d42p-3'],
['0x1.4fd0dab545943p-3','-0x1.44437783962ccp-2','0x1.7a5ae430d7680p-3','0x1.4747f7d8e0f34p-3','0x1.69b10d2a9f54dp-2','0x1.4ee0e082453e4p-2'],
['0x1.c116eb37c423ep-5','0x1.21b0ba90cfb83p-1','0x1.43745170368f9p-3','0x1.bfcde207336a0p-3','0x1.76371e5babf10p-1','0x1.17b9e9b4d4cb2p-4'],
['-0x1.f0e83cf246c23p-5','0x1.b7b055ced1cd0p-2','0x1.3757ea6f65374p-3','0x1.3b223fe35af79p-3','-0x1.daf0efb7b44c3p-2','0x1.7b0f957c71c64p-1'],
['0x1.32755c7aed9dcp-1','-0x1.6007fbb7ad939p-2','-0x1.b753b5755bb3cp-7','0x1.942d3dd873d48p-5','-0x1.5048feb97f033p-6','0x1.119907ce857fdp-2'],
]

EVEN_L0_HEX = [
['0x1.6f4cd80a2c6c2p-3','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.ec013a2d193fcp-50','0x1.ecb0b31448a75p-1','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['0x1.96dabf8bb9ae7p-51','0x1.3304e79f13161p-54','0x1.41a60d5ac9accp+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['0x1.3d41c1599cf9bp-52','0x1.5b2fadf3cea7ep-58','0x1.440badeae11cbp-52','0x1.62c09d41d71eep+0','0x0.0p+0','0x0.0p+0'],
['-0x1.2d239d763be35p-50','0x1.3cc2338f31b77p-51','-0x1.5d93768fe4520p-52','-0x1.7f21e59cf9eebp-52','0x1.84e5c09249111p+0','0x0.0p+0'],
['-0x1.7bf07a13d6a60p-51','0x1.8a1188b3b5b90p-53','-0x1.7376ee7d71f7bp-53','-0x1.0623eb6ae7bb6p-53','0x1.6a849b678e75dp-53','0x1.9168452936ad9p+0'],
]

ODD_Q_HEX = [
['-0x1.6cdb1b3e93534p-4','-0x1.7ee06ef5d397dp-4','-0x1.08cee53dddeb2p-3','-0x1.2ffefa315c90cp-5','0x1.a2259d5423ec8p-7','-0x1.e524b3f321989p-5'],
['-0x1.7d9434189956ap-3','-0x1.180436f6aae05p-2','-0x1.fea2cbaf08fbcp-2','-0x1.98e8211186e7ap-4','0x1.24d4a2b0e8828p-5','-0x1.7b92c861c7840p-3'],
['0x1.364f73667cee7p-7','0x1.629e72b9a0b79p-3','0x1.58fad3ea6d77dp-1','0x1.8564f15ba3706p-5','-0x1.a97d2bc4e34cdp-7','0x1.09eb7092353a1p-3'],
['-0x1.2110caaa89242p-3','-0x1.18460d19c1af0p-3','0x1.a8ac7233c455bp-2','-0x1.96833a2bff09cp-5','0x1.5576439d540e0p-5','-0x1.552101cfce26dp-4'],
['0x1.8e2e46b39f57ap-5','0x1.681ae111adf9bp-1','-0x1.49c0eb1b9cdd6p-2','0x1.06c5e28651574p-3','-0x1.4bfe48e42c032p-3','0x1.c070b406d4159p-2'],
['0x1.09bdadd2fee6bp-3','-0x1.2568d5a78147ep-1','-0x1.22832c5fbf4a1p-7','0x1.1e6b2683fae38p-5','-0x1.a8df4c6ee8bacp-2','0x1.61dfab8660d47p-1'],
['-0x1.c44fd7983220cp-2','0x1.4f42d21105ecap-3','0x1.9d84f0e38103bp-5','-0x1.66c1c17100705p-4','-0x1.98c8f835c0c28p-3','0x1.5e4340c90fe45p-3'],
['0x1.aba1483d417cbp-4','-0x1.8b583fb727346p-4','-0x1.74affa38cc1f2p-5','0x1.d2c12fa80c452p-3','0x1.ae94578c75313p-1','0x1.a2547a38003bep-2'],
['0x1.a6c3b139c1b84p-1','0x1.0e5a0f951fbfcp-5','-0x1.8d938ac4adf16p-7','0x1.36f8589cc2784p-4','-0x1.3fcb55041af2fp-3','-0x1.94020cfdc97e0p-3'],
['-0x1.64ae891f43065p-3','-0x1.62950eb52f9cdp-4','-0x1.2bfe69438dbcep-7','0x1.e5f612b6517f8p-1','-0x1.4f01bd4287511p-3','-0x1.788b5adafc207p-3'],
]

ODD_L0_HEX = [
['0x1.9fe45e21e9611p-1','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['0x1.c39e1be206301p-52','0x1.2b9f784434e88p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.bb61cd6d3de5cp-56','0x1.7dc86a5469165p-51','0x1.4ec5257f48c9dp+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.277629a63a58ap-52','0x1.04c9c7c43e9c3p-51','0x1.ad7e27ce1d6a1p-54','0x1.62b4018f62515p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.bd3acc17bb9edp-54','-0x1.119d153e1681ap-53','-0x1.0d5e02cbb474bp-53','0x1.0b44acd2b9530p-51','0x1.8515cc2c9a818p+0','0x0.0p+0'],
['0x1.28a7381c63846p-53','0x1.b449e75d0f56ap-51','-0x1.70f31f4cb6da5p-52','0x1.6ce6cd4d11b7ap-51','-0x1.5baf26f387c44p-52','0x1.94007dc27411fp+0'],
]

EVEN_PAYLOAD_SHA256 = "af158c4f87c4d90e7c23b0f0ef2adb4dbb8f27cd88d96efa1563cb6fd546d5b0"
ODD_PAYLOAD_SHA256 = "c983603a88bbdc9d9a217cb8c6936fb5b05ae56d84f9c85e5baf8bf1924ec9eb"

EVEN_FIRST6_DET_DIAGNOSTIC = -3.96645702505283e-06
ODD_FIRST6_DET_DIAGNOSTIC = -2.638188240960451e-07

EVEN_Q_GRAM_ERROR_2NORM = 1.2151125699310343e-15
ODD_Q_GRAM_ERROR_2NORM = 1.4838711512320212e-15


def floats(hex_rows):
    return np.array([[float.fromhex(x) for x in row] for row in hex_rows])


def exact_det_first6(qhex):
    a = [
        [Fraction.from_float(float.fromhex(x)) for x in row]
        for row in qhex[:6]
    ]
    det = Fraction(1)
    sign = 1
    n = 6
    for k in range(n):
        pivot = next((i for i in range(k,n) if a[i][k] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        p = a[k][k]
        det *= p
        for i in range(k+1,n):
            if a[i][k] == 0:
                continue
            f = a[i][k]/p
            for j in range(k+1,n):
                a[i][j] -= f*a[k][j]
    return sign*det


def payload_hash(qhex,lhex):
    raw = json.dumps(
        {"Q":qhex,"L0":lhex},
        separators=(",",":"),
        sort_keys=True,
    ).encode()
    return hashlib.sha256(raw).hexdigest()


def verify_one(qhex,lhex,expected_hash):
    Q=floats(qhex)
    L=floats(lhex)
    det=exact_det_first6(qhex)
    assert det != 0
    assert all(L[i,i] != 0 for i in range(6))
    assert payload_hash(qhex,lhex) == expected_hash
    return Q,L,det


if __name__ == "__main__":
    for name,q,l,h in (
        ("even-v",EVEN_Q_HEX,EVEN_L0_HEX,EVEN_PAYLOAD_SHA256),
        ("odd-v",ODD_Q_HEX,ODD_L0_HEX,ODD_PAYLOAD_SHA256),
    ):
        Q,L,det=verify_one(q,l,h)
        print(name)
        print(" payload sha256 =",h)
        print(" exact first-six determinant nonzero =",det != 0)
        print(" determinant diagnostic =",float(det))
        print(" Q Gram error 2-norm =",np.linalg.norm(Q.T@Q-np.eye(6),2))
        print(" L0 diagonal =",[L[i,i].hex() for i in range(6)])
