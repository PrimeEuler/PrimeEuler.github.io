#!/usr/bin/env python3
"""Frozen exact-dyadic four-negative-direction endpoint verifier inputs.

These are the sign-canonicalized four negative eigendirections of the fresh
rho=0.10 M=3999/4000 effective cores.  Lneg is the midpoint Cholesky factor
of the positive matrix

    - Qneg^T S_mid Qneg.

Every hexadecimal literal is an exact IEEE-754 binary64 dyadic.  A verifier
must consume these payloads as fixed inputs and must not regenerate the
eigenspaces.

Payload hashes use JSON serialization with keys Q and Lneg, compact
separators, and sort_keys=True.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import numpy as np


EVEN_QNEG_HEX = [
["0x1.04085fbfa8d2cp-6","0x1.19c80a6f616f3p-7","0x1.17c0e29b805f8p-4","0x1.aeb2370691082p-1"],
["0x1.031a2a48474dcp-5","0x1.020166dcfcdccp-5","0x1.c8ac931e5821ep-1","-0x1.29f57cc1bd789p-2"],
["0x1.f0287b11953e5p-10","0x1.706504c6f3626p-11","0x1.12cbb207fb84ep-8","0x1.665e2f7ffa516p-8"],
["0x1.719413b97f41dp-4","0x1.d67f9300e8704p-1","-0x1.85c219b3de27dp-3","-0x1.44148300a68aap-3"],
["0x1.47a304c7c3f5ap-4","-0x1.eb88e3b7f57dcp-3","-0x1.1238b5a1ce41fp-3","-0x1.d431dd5f53605p-4"],
["0x1.72433e4261455p-2","-0x1.f9d13c730f0d6p-3","-0x1.dfd270acad9fep-3","-0x1.d275e009c2f4ap-3"],
["0x1.7ea264c231cbep-1","-0x1.5b65c2221cc42p-4","-0x1.64ccb24a0583ep-4","-0x1.724a8737e60f4p-4"],
["-0x1.f93b2695c96f3p-3","-0x1.d65eaabe8ebe8p-6","-0x1.59be3d5ad57b0p-5","-0x1.59e5c1001c107p-5"],
["0x1.b55d9c8215bafp-6","0x1.4934bc0876ccap-7","0x1.4c529680a32d7p-6","0x1.afdbadbd3e805p-6"],
["-0x1.eeb1512b4b644p-2","-0x1.55355f666e206p-3","-0x1.2353768205d42p-2","-0x1.4f08684ed979fp-2"],
]

EVEN_LNEG_HEX = [
["0x1.94ba1725b3a2cp-2","0x0.0p+0","0x0.0p+0","0x0.0p+0"],
["-0x1.429058a69e9e7p-50","0x1.4b0e62910c872p-2","0x0.0p+0","0x0.0p+0"],
["0x1.4659558fc1f53p-52","0x1.d9aa070fbde33p-52","0x1.f95ad3bba2aabp-3","0x0.0p+0"],
["0x1.459dd433832bep-53","-0x1.59a135fd05596p-52","0x1.96bdba2283f1ap-53","0x1.5e42110764727p-3"],
]

ODD_QNEG_HEX = [
["-0x1.862064287a464p-6","-0x1.746ebb16dae31p-5","-0x1.1e4fc517a0ceap-2","0x1.e080e7bbdd6f9p-1"],
["-0x1.e8cd8d56162a7p-8","-0x1.58c26c519ac0ap-6","0x1.880aa1d7f12d7p-1","0x1.8dfa2fae9a0bdp-4"],
["-0x1.a755cf64082dcp-4","-0x1.aff91c026231dp-2","0x1.fd4225438250ep-2","0x1.f87f0f8fab40bp-3"],
["-0x1.73be8dc0dc4a8p-4","0x1.b566412aac5d2p-1","0x1.5596240ba85c5p-3","0x1.c710e2fb77f34p-4"],
["-0x1.d0246d4be9175p-3","0x1.0b72b338ad7c3p-2","0x1.620772f2dfa7fp-3","0x1.fa54f410ef2adp-4"],
["-0x1.d0744e4a95387p-5","0x1.d899462ac3cf8p-7","0x1.71d530955dfbdp-7","0x1.dce493c547e45p-8"],
["0x1.ab4cde9fa1d95p-1","0x1.ec9e2e6260563p-6","0x1.decfed6adb9b4p-6","0x1.742f1e016a586p-6"],
["0x1.b612e36b1f7b0p-3","0x1.67f3444b25faep-5","0x1.90c1cf4dc7427p-5","0x1.43b3b1151540dp-5"],
["0x1.b62ab240b723cp-2","0x1.15d09299a2e30p-3","0x1.50dec56677d43p-3","0x1.1cdf8e967a406p-3"],
["0x1.76a2677364cfbp-6","0x1.e0b8b159727e9p-8","0x1.e6cf342a0d131p-8","0x1.404102d331f05p-8"],
]

ODD_LNEG_HEX = [
["0x1.8a9dc946809a0p-2","0x0.0p+0","0x0.0p+0","0x0.0p+0"],
["-0x1.6f8d5cd1f9a67p-51","0x1.4d19904b38fc6p-2","0x0.0p+0","0x0.0p+0"],
["-0x1.5cefbcc0c24a1p-52","-0x1.af63bac8f74a2p-52","0x1.079e8db70a4cap-2","0x0.0p+0"],
["-0x1.8e16ad34044a3p-54","-0x1.5720e8df8aaf0p-54","0x1.834758d0dab6fp-51","0x1.62db56e6a6728p-3"],
]

EVEN_PAYLOAD_SHA256 = "40e43622bce7044f9e5bc39a682399d39acaccab2835a68ca2eec892af2cf309"
ODD_PAYLOAD_SHA256 = "798cbbcd88c2c035854d5b67432e5b12cf1c04dedac7399873a1bd27211a2395"


def floats(rows):
    return np.array([[float.fromhex(x) for x in row] for row in rows])


def payload_hash(qhex, lhex):
    raw = json.dumps(
        {"Q": qhex, "Lneg": lhex},
        separators=(",", ":"),
        sort_keys=True,
    ).encode()
    return hashlib.sha256(raw).hexdigest()


def exact_first4_det(qhex):
    a = [
        [Fraction.from_float(float.fromhex(x)) for x in row]
        for row in qhex[:4]
    ]
    det = Fraction(1)
    sign = 1
    for k in range(4):
        pivot = next((i for i in range(k, 4) if a[i][k] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        p = a[k][k]
        det *= p
        for i in range(k + 1, 4):
            if a[i][k] == 0:
                continue
            f = a[i][k] / p
            for j in range(k + 1, 4):
                a[i][j] -= f * a[k][j]
    return sign * det


def verify_one(name, qhex, lhex, expected_hash):
    Q = floats(qhex)
    L = floats(lhex)

    det = exact_first4_det(qhex)
    assert det != 0
    assert all(L[i, i] != 0 for i in range(4))
    assert payload_hash(qhex, lhex) == expected_hash

    gram_error = np.linalg.norm(Q.T @ Q - np.eye(4), 2)

    print(name)
    print(" payload sha256 =", expected_hash)
    print(" exact first-four determinant nonzero =", det != 0)
    print(" determinant diagnostic =", float(det))
    print(" Q Gram error 2-norm =", gram_error)
    print(" Lneg diagonal =", [L[i, i].hex() for i in range(4)])


if __name__ == "__main__":
    verify_one(
        "even-v",
        EVEN_QNEG_HEX,
        EVEN_LNEG_HEX,
        EVEN_PAYLOAD_SHA256,
    )
    verify_one(
        "odd-v",
        ODD_QNEG_HEX,
        ODD_LNEG_HEX,
        ODD_PAYLOAD_SHA256,
    )
