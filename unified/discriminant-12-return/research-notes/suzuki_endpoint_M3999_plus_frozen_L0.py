#!/usr/bin/env python3
"""Frozen Cholesky preconditioners for the rho=0.10 plus endpoint.

The positive endpoint uses the standard ten-coordinate core in each parity;
there is no frozen eigenspace.  Only the midpoint Cholesky factor L0 of the
fresh M=3999/4000 ten-dimensional effective core is frozen.

Every hexadecimal literal is an exact IEEE-754 binary64 dyadic.
Payload hashes use JSON serialization with key L0, compact separators, and
sort_keys=True.
"""
from __future__ import annotations

import hashlib
import json
import numpy as np


EVEN_L0_HEX = [
['0x1.e8d9a52e97963p-4','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.58620c9ae99edp-5','0x1.d606993ff01c5p-3','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.2cfa71d285ea2p-6','0x1.f7d0a1c3e59fcp-9','0x1.722a4cc4faeaep+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['0x1.02c07a0141ca6p-5','0x1.c2729d1f5958ap-5','0x1.1c12f6344f400p-6','0x1.85c5251da3439p-2','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['0x1.5235781fe4c2ap-2','0x1.7c00d97e8f86ep-2','0x1.763db74daf808p-4','0x1.35f174123d300p-1','0x1.18e0571ab4c3fp+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['0x1.e148458fcbbeep-4','0x1.118f116214a50p-3','0x1.decce38e42a15p-6','0x1.ab7d074bccff6p-4','-0x1.7b2c472ecc48ap-2','0x1.e23a4db03f693p-1','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.13ae515c8b06fp-2','-0x1.0dcd63b75c804p-2','-0x1.c37a7d2840e5dp-5','-0x1.1cf8d0c895220p-2','-0x1.98c13c9448f8ap-6','-0x1.46606a75199c6p-1','0x1.22c00fc19dd8ep-1','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.9cff4c79479bdp-5','-0x1.467aa2ca32febp-5','-0x1.0e62ef4d9fbc2p-7','-0x1.1252803e5f336p-4','-0x1.ff5c952c4cea0p-4','-0x1.cacf81b27aca0p-3','0x1.779381337f74cp-1','0x1.2cd46e767d798p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.0365d9fa0a17ap-3','-0x1.dc70c5e60fc88p-4','-0x1.792c1f03e15edp-6','-0x1.d0f12e03a516ap-4','-0x1.02f25fbd3dee5p-5','-0x1.5b3af1788b565p-3','-0x1.03d56af469307p-4','-0x1.29409ff623d0ap-2','0x1.81537d5a7c0a6p+0','0x0.0p+0'],
['-0x1.e464abfd5de92p-4','-0x1.a0058a96f8700p-4','-0x1.464d2cf70d7d5p-6','-0x1.d0fc2dc924d9bp-4','-0x1.83687fade9aa7p-4','-0x1.b35da199de48dp-3','0x1.475c4740927ccp-3','-0x1.0836db4828994p-2','0x1.5c5b581328f8ap-3','0x1.8633dd30a1739p-1'],
]

ODD_L0_HEX = [
['0x1.3161fcf01c86ap-2','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['0x1.43bf30b5d6852p-1','0x1.30651ed9bad76p-1','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.67f2e2ef9b073p-1','-0x1.10e012fe8c722p-1','0x1.eed6576e534d6p-2','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.89ff5ae9acf2ap-3','-0x1.c0220118fb3b9p-3','0x1.7dedb495159dcp-2','0x1.076ca146e981ep-1','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.839360ab853f4p-2','-0x1.a3e59db17ce03p-5','-0x1.5abb968b0c44bp-1','-0x1.5eb406644e6c5p-1','0x1.8e685210eba60p-1','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.9bdf28b608728p-3','-0x1.25dac29e67167p-4','-0x1.7311961a2ebf5p-3','-0x1.784061489e32bp-3','0x1.efc5f390a26c4p-5','0x1.7c7da1e87bc6cp+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.ffd9bcbbc6defp-4','-0x1.7ee3ff3145452p-4','0x1.67517a491ec2dp-6','-0x1.9da3c04d95995p-4','0x1.5a45f009c6931p-2','0x1.50da6c3e709d3p-3','0x1.35ebb1e10a516p-1','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.3053fb7fa4375p-3','-0x1.514d7e0b944d4p-5','-0x1.2204b391be68dp-3','-0x1.53d3905476d7cp-4','-0x1.9637a380ef6c1p-4','-0x1.7b81ef4fdd77cp-5','-0x1.16218f84178c8p-1','0x1.75badf4f664d4p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.1302e0570146ap-3','0x1.7ba52f5c8409bp-7','-0x1.e2bc9728be51ep-3','-0x1.76d6022de2cc9p-5','-0x1.663116d01953dp-2','-0x1.f7f217213aa61p-4','-0x1.5830a7adb4a33p-2','-0x1.e9513d9d4c51bp-2','0x1.4e8e2322e4175p-1','0x0.0p+0'],
['-0x1.ab65555ba6d12p-4','-0x1.4a880e584959dp-7','-0x1.14873bfecdfe6p-3','-0x1.413aa41b0ec1ep-5','-0x1.48a3ae5dd69cdp-3','-0x1.b9bf55ce17ee2p-5','-0x1.4694d5106b8b5p-3','-0x1.39327c2432569p-3','-0x1.dadbcdb3fe7ffp-7','0x1.7a819b0c17002p+0'],
]

EVEN_SHA256 = "488ed62ca2d6d4ba6eea4bd12bf80c10156a93cff6075fd32d34a6f3b9621742"
ODD_SHA256 = "638f8e97a051aa97b17f9c2f147ab49810f1c5166600fef64fd3bca56015140d"


def floats(rows):
    return np.array([[float.fromhex(x) for x in row] for row in rows])


def payload_hash(rows):
    raw = json.dumps(
        {"L0": rows},
        separators=(",", ":"),
        sort_keys=True,
    ).encode()
    return hashlib.sha256(raw).hexdigest()


if __name__ == "__main__":
    for name, rows, expected in (
        ("even-v", EVEN_L0_HEX, EVEN_SHA256),
        ("odd-v", ODD_L0_HEX, ODD_SHA256),
    ):
        L = floats(rows)
        assert payload_hash(rows) == expected
        assert all(L[i, i] > 0 for i in range(10))
        print(name)
        print(" sha256 =", expected)
        print(" ||L0^-1||_2 =", np.linalg.norm(np.linalg.inv(L), 2))
        print(" lambda_min(L0 L0^T) =", np.linalg.eigvalsh(L @ L.T)[0])
