#!/usr/bin/env python3
"""Frozen exact-dyadic rho=0.02 PLUS endpoint ten-core Cholesky factors.

The plus endpoint uses the standard ten-coordinate core in each parity.
Only the midpoint Cholesky factor L0 is frozen. Every hexadecimal literal
is an exact IEEE-754 binary64 dyadic. Runtime verification fails closed on
payload hash mismatch, nonpositive diagonal, or exact triangular-rank failure.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import numpy as np

EVEN_L0_HEX = [['0x1.1c91c6da343ccp-4', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['0x1.f5053c61fbf99p-6', '0x1.f44c3c77ff435p-4', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['0x1.de54c6679d3afp-5', '0x1.660557f29a95cp-5', '0x1.6c5d8d1d064a8p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['0x1.15ccc3e62b578p-3', '0x1.94e7cfe2eca32p-4', '0x1.8163f73912916p-7', '0x1.ab599d6cbeca0p-3', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['0x1.4cd7df6fe04fcp-1', '0x1.d5f715247eb5dp-2', '0x1.a3b8572e651d8p-5', '0x1.4017f25097ce8p-1', '0x1.ac2dd31f8b500p-1', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['0x1.1b1fbd3aef627p-2', '0x1.685061bff0db1p-3', '0x1.cb4994b206c9fp-7', '-0x1.4fa5b941e092ep-7', '-0x1.3913dd2b6f5dap-1', '0x1.614aec77ecf4bp-1', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['-0x1.a5f21176f6259p-2', '-0x1.14bbf0eb1aa14p-2', '-0x1.a02b4e015207cp-6', '-0x1.a2b2aa22d56b4p-3', '0x1.5a69a7f2da53cp-3', '-0x1.363d8333d39a7p-1', '0x1.927111b909db5p-2', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['-0x1.7a0c4d5a4b5afp-6', '-0x1.70aec2e213a52p-6', '-0x1.1e43ad7ee5f7cp-8', '-0x1.c0a816a8fdc73p-4', '-0x1.2736c235322e6p-3', '-0x1.8b9470037fbb8p-2', '0x1.db33486e831bep-1', '0x1.cf7e70b10828ap-1', '0x0.0p+0', '0x0.0p+0'],
 ['-0x1.545132f08114ap-3', '-0x1.b7e52e053e895p-4', '-0x1.48214d3ca454ep-7', '-0x1.6b0efdfb7d4e5p-4', '0x1.c81eee608e33ap-6', '-0x1.447d2e774b197p-3', '-0x1.be88a443549e5p-4', '-0x1.5202ab0495564p-2', '0x1.731895cd24ce2p+0', '0x0.0p+0'],
 ['-0x1.0d649be80ebbcp-3', '-0x1.71016ca7dca23p-4', '-0x1.45b41f6e59896p-7', '-0x1.14bc02d26844cp-3', '-0x1.17dab68271f99p-4', '-0x1.3b41d5948b8abp-2', '0x1.14667aeb31ffcp-3', '-0x1.c4563b35c44a0p-2', '0x1.eef2d47cf8e53p-4', '0x1.e9da9cd2f7027p-2']]

EVEN_SHA256 = "d2bb5e790023af852e349e001876369e5d9fd43a56a85f7fb3edc687d7d3ef5c"

ODD_L0_HEX = [['0x1.025cb5d909951p-2', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['0x1.8ad582198a21ep-1', '0x1.4d7ed3c8cabc4p-2', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['-0x1.9dc3d7a1321f7p-1', '-0x1.98dbb89210591p-2', '0x1.6bf8bba8a058bp-2', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['-0x1.a9aee0544d0adp-3', '-0x1.1177c1f284157p-2', '0x1.d1684ec9fc078p-2', '0x1.27d69aa7dd739p-2', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['-0x1.b67863b03b2c0p-2', '0x1.b1a4af49ddb47p-3', '-0x1.ac3fe8b99d152p-1', '-0x1.2d011cd4b7674p-1', '0x1.18d51d802b8f7p-1', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['-0x1.c455ac549676ep-3', '0x1.2c0a410113ff1p-6', '-0x1.c0458bbd08e6ap-3', '-0x1.46839a5b1ff8fp-3', '0x1.315a26650a1a4p-12', '0x1.725ff4ce9f716p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['-0x1.100f743abe7abp-3', '-0x1.7545623fc026fp-4', '0x1.a384cf18cbba5p-6', '-0x1.a89b033e807c2p-3', '0x1.b8cc4446c6bf2p-2', '0x1.6f0e5df04bea4p-3', '0x1.7b5201d431a05p-2', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['-0x1.498b4775b99c2p-3', '0x1.123b511a7405ap-5', '-0x1.4f65b01fa6fbcp-3', '-0x1.28a968192916fp-6', '-0x1.527911d5eb2d3p-3', '-0x1.a883565b178e4p-5', '-0x1.7eba3897e3e9bp-1', '0x1.4f8190a45308fp+0', '0x0.0p+0', '0x0.0p+0'],
 ['-0x1.26b8174157b31p-3', '0x1.0a723954fc3e4p-3', '-0x1.1302fa687a953p-2', '0x1.24b2c1b7fcfd7p-3', '-0x1.f7c8d7575a68ap-2', '-0x1.19892c6786b9ap-3', '-0x1.373556d4a0869p-3', '-0x1.0e6ffdcd1ab31p-1', '0x1.79b8fae4d450dp-2', '0x0.0p+0'],
 ['-0x1.c1b475be84c3bp-4', '0x1.f45f16b5eb8f5p-5', '-0x1.3661432ebbbe4p-3', '0x1.d2a985c0993e1p-5', '-0x1.d4811a30ea2cap-3', '-0x1.ec482fe404967p-5', '-0x1.168625b3abf52p-4', '-0x1.53bea21671f4bp-3', '-0x1.a04b331250766p-3', '0x1.67723e897a8d4p+0']]

ODD_SHA256 = "7eb101a7138b27a92412c9f381a12d53aacd70af437d86ed478f4dc44a86f8df"


def floats(rows):
    return np.array([[float.fromhex(x) for x in row] for row in rows])


def payload_hash(rows):
    raw = json.dumps(
        {"L0": rows},
        separators=(",", ":"),
        sort_keys=True,
    ).encode()
    return hashlib.sha256(raw).hexdigest()


def exact_triangular_det(rows):
    det = Fraction(1)
    for i, row in enumerate(rows):
        det *= Fraction.from_float(float.fromhex(row[i]))
    return det


def verify_one(name, rows, expected_hash):
    if payload_hash(rows) != expected_hash:
        raise RuntimeError(f"{name}: frozen rho0.02 plus L0 hash mismatch")
    det = exact_triangular_det(rows)
    if det == 0:
        raise RuntimeError(f"{name}: exact plus L0 rank test failed")
    L = floats(rows)
    if not all(L[i, i] > 0 for i in range(10)):
        raise RuntimeError(f"{name}: plus L0 positive diagonal failed")
    return {
        "exact_rank": 10,
        "determinant_nonzero": True,
        "determinant_decimal": float(det),
        "inverse_2norm": float(np.linalg.norm(np.linalg.inv(L), 2)),
        "lambda_min_reference": float(np.linalg.eigvalsh(L @ L.T)[0]),
    }


if __name__ == "__main__":
    for name, rows, expected in (
        ("even-v", EVEN_L0_HEX, EVEN_SHA256),
        ("odd-v", ODD_L0_HEX, ODD_SHA256),
    ):
        out = verify_one(name, rows, expected)
        print(name)
        print(" sha256 =", expected)
        for k, v in out.items():
            print(" ", k, "=", v)
