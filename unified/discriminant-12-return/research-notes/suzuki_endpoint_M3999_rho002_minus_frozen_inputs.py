#!/usr/bin/env python3
"""Frozen exact-dyadic rho=0.02 MINUS endpoint verifier inputs.

For each parity this module freezes:
  * Qneg: the four negative midpoint eigendirections;
  * Lneg: Cholesky factor of -Qneg^T S^- Qneg;
  * Qpos: the six positive midpoint eigendirections;
  * Lpos: Cholesky factor of  Qpos^T S^- Qpos.

Column signs are canonicalized so the largest-magnitude entry is positive.
Every hexadecimal literal is an exact IEEE-754 binary64 dyadic.
Runtime verification fails closed on payload hash mismatch, exact rank-minor
vanishing, or a nonpositive Cholesky diagonal.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import numpy as np

EVEN_QNEG_HEX = [['-0x1.961664068c425p-6', '-0x1.1de8c9694fedfp-5', '-0x1.48be66758af6ep-3', '0x1.f76d3576e861ap-1'],
 ['-0x1.79cd4ae858c25p-6', '-0x1.691ab7bc6f194p-5', '0x1.f6c50cfd115bcp-1', '0x1.33dd0ba9ab67ep-3'],
 ['-0x1.dc7d2daceac5ep-12', '-0x1.c637b073efc60p-11', '0x1.c54f90d8c772cp-12', '-0x1.382dd13afba9fp-16'],
 ['0x1.3c5ae952f204ap-7', '0x1.f36f26104ffe4p-1', '0x1.32e0b6ac657e2p-6', '0x1.7117c3a7cf124p-6'],
 ['0x1.7c59d9b4499cfp-3', '-0x1.57a51f6519703p-3', '-0x1.b8c3cc70a870cp-5', '-0x1.8be1fd71ef4eap-5'],
 ['0x1.08e7a62371224p-1', '-0x1.692f1d3117ae0p-4', '-0x1.37a4a2bbc0ad3p-5', '-0x1.14b657994e683p-5'],
 ['0x1.8c3b8ed50b860p-1', '0x1.ae9d5a39b6a73p-5', '0x1.386094b4b6183p-5', '0x1.603de998255b5p-5'],
 ['-0x1.9b1877f366102p-3', '-0x1.3058e5a39709ap-5', '-0x1.ab342f908b4c0p-6', '-0x1.d0d145b118fc6p-6'],
 ['0x1.80cb903633b28p-7', '0x1.909891df511a3p-9', '0x1.2a20f0a9dcdbcp-9', '0x1.49ed2b47bb4e7p-9'],
 ['-0x1.e9f6107b43b77p-3', '-0x1.286d0d21f88e6p-4', '-0x1.ca76040da270ep-5', '-0x1.0206588f93c98p-4']]

EVEN_LNEG_HEX = [['0x1.58d9bcdd02bb9p-3', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['0x1.311d687a374c8p-49', '0x1.22ee3efd25ed4p-3', '0x0.0p+0', '0x0.0p+0'],
 ['-0x1.3bff81bd1110ep-49', '-0x1.3c4b56c86e78dp-50', '0x1.a332e2646d91cp-4', '0x0.0p+0'],
 ['-0x1.4af991559497ap-52', '-0x1.23bb860149dbbp-53', '-0x1.5e8228029202ap-50', '0x1.a6a5978f31c97p-5']]

EVEN_QPOS_HEX = [['0x1.110d30108b0bep-4', '0x1.996d6ba95009ep-6', '0x1.9bed82203da35p-7', '0x1.6aa60fcba07e0p-11', '-0x1.55d25a3de43d4p-7', '-0x1.0f9c00cee8a2dp-6'],
 ['0x1.68b108bfd06a0p-4', '0x1.35b0d87aa3448p-5', '0x1.5bb4570cac7c0p-6', '0x1.70042c1bdc900p-14', '-0x1.1a33fb20aeef0p-6', '-0x1.ba0f4a68c5ba0p-6'],
 ['-0x1.272247f9544f8p-6', '-0x1.09c4eecc55147p-4', '-0x1.b384cfa374902p-3', '0x1.e22491908bcd0p-1', '-0x1.4a9db160a0289p-3', '-0x1.8c1df8b2707ebp-3'],
 ['0x1.2f7ee3b03654bp-3', '0x1.63f1324587969p-4', '0x1.69a48091f9c68p-4', '0x1.6457f29616fdfp-9', '-0x1.d87859078ac75p-5', '-0x1.53fe00f58bd95p-4'],
 ['0x1.ba77cc2870533p-3', '0x1.3ec375a22adf1p-3', '0x1.95c72be3c5269p-1', '0x1.0e0a95b88def7p-4', '-0x1.2aec9a9d41377p-2', '-0x1.83f79127d0669p-2'],
 ['0x1.8c00b00d7f9e0p-2', '0x1.f6e6f573c799ep-2', '-0x1.f8b151a42c15bp-2', '-0x1.1eb2e7d08913fp-3', '-0x1.54a6b0cf25734p-3', '-0x1.9ec34d2ec3b66p-3'],
 ['-0x1.c3561607cc808p-9', '-0x1.4f0680d6288b8p-2', '0x1.63fc7e7ed3fd8p-3', '0x1.287ff41a4bf52p-3', '0x1.834c85269a7d4p-2', '0x1.39871443f90c7p-2'],
 ['0x1.1f8550a4a188cp-3', '0x1.2291960068223p-1', '0x1.3cd06664c1086p-3', '0x1.aca0e63c8130dp-3', '0x1.7a7e3f859bea8p-1', '0x1.db53549084296p-6'],
 ['-0x1.5d2a3dadea650p-4', '0x1.b31b7febc819dp-2', '0x1.297231740659cp-3', '0x1.320c839eac470p-3', '-0x1.a371ff767250ep-2', '0x1.8cdd0171292b8p-1'],
 ['0x1.b91f4f02a56d3p-1', '-0x1.5550686f159dap-2', '-0x1.55bbd958b92d7p-7', '0x1.7ec000aa649fbp-5', '-0x1.47bbc3e006639p-9', '0x1.17ef1bd6ffe16p-2']]

EVEN_LPOS_HEX = [['0x1.fbdd033218676p-2', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['0x1.39a7a99e5a44ap-51', '0x1.064ca39882f93p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['-0x1.c54d5043ad113p-52', '0x1.611ce1da00ce1p-51', '0x1.4b9827a36c91ep+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['0x1.2cd88c635d011p-55', '0x1.c45f88ac8cfcep-55', '0x1.3213176fd1693p-52', '0x1.68bda995bac92p+0', '0x0.0p+0', '0x0.0p+0'],
 ['0x1.3a177033558aep-52', '-0x1.3b308fb111a1bp-52', '-0x1.bc6922770630fp-56', '0x1.44ffb56d18ba4p-51', '0x1.8eec3b560a2bbp+0', '0x0.0p+0'],
 ['0x1.8e7f2aa6f20aap-52', '0x1.df4448752f023p-51', '0x1.42df22d4e73b4p-52', '0x1.c5deca1fce31cp-52', '-0x1.c954261fb38a7p-51', '0x1.9b482df4c4f16p+0']]

EVEN_PAYLOAD_SHA256 = "f42f62b50fbd8ebd8e40a692450915ed4f6b4bcb9b5a2822f55f103c6f4bb5b3"

ODD_QNEG_HEX = [['-0x1.562842b1c551fp-5', '-0x1.10469ad9a6302p-4', '-0x1.0b231c1ba5254p-1', '0x1.a8863c674ebabp-1'],
 ['-0x1.8e3af43637655p-4', '-0x1.494c15432b77cp-3', '0x1.6731413a989b0p-1', '0x1.259da0fdf69a7p-2'],
 ['-0x1.75a6270477021p-4', '-0x1.10a889a79a6aep-1', '0x1.56558514e5b0bp-2', '0x1.319110266a353p-2'],
 ['-0x1.24f49fc3802fcp-2', '0x1.8bc4ba2ee668ap-1', '0x1.d75360eabeb1cp-3', '0x1.c73afa7ad5530p-3'],
 ['-0x1.35f4b9cb7b324p-2', '0x1.5ef6cbb29f52cp-3', '0x1.0eecd89c77980p-3', '0x1.374fc7ef78cd1p-3'],
 ['-0x1.ed30faf6b3df5p-5', '0x1.6ee722a1108cfp-10', '0x1.fdd2b6be16cb4p-9', '0x1.778f216e541aap-8'],
 ['0x1.9a350e617186ap-1', '0x1.5d20ca8f9d675p-3', '0x1.151c53eb868f5p-3', '0x1.1c5ca0df74d11p-3'],
 ['0x1.83c87786cd754p-3', '0x1.13bc3b5c4511bp-4', '0x1.100becb24b81dp-4', '0x1.36e3cfe1bf2eap-4'],
 ['0x1.6a7347880118ep-2', '0x1.478ab688ee0a1p-3', '0x1.65e201935c7dcp-3', '0x1.ab384b2f2361dp-3'],
 ['0x1.3348682cf3a0ap-6', '0x1.3158571edd064p-7', '0x1.51e3456e23cefp-7', '0x1.8ce7f1f23d9b3p-7']]

ODD_LNEG_HEX = [['0x1.52cd2d8451014p-3', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['0x1.033c39ae05fb2p-51', '0x1.232eb96f1b4e8p-3', '0x0.0p+0', '0x0.0p+0'],
 ['0x1.c69ac16d41fe0p-52', '-0x1.6c928dac784edp-50', '0x1.b6741c7ddbb3fp-4', '0x0.0p+0'],
 ['0x1.504717e27df7bp-51', '-0x1.b7e17fb310844p-51', '-0x1.610dae8f465a9p-50', '0x1.02972ca2830d5p-4']]

ODD_QPOS_HEX = [['-0x1.21080a35ff505p-4', '-0x1.749510b2a6dd7p-4', '-0x1.00402fa03fce6p-3', '-0x1.3e958cc17235cp-5', '0x1.0e834a7bbcd81p-6', '-0x1.dfb3300f23755p-5'],
 ['-0x1.474fe2b3d6b59p-3', '-0x1.1b68fa6aa4521p-2', '-0x1.f6b86352155a6p-2', '-0x1.bb3a873117718p-4', '0x1.874e6e314b304p-5', '-0x1.74e8a4b3fd028p-3'],
 ['0x1.ce72a8becc2d1p-7', '0x1.7fc45b57e94e1p-3', '0x1.5844cf4d8c64ep-1', '0x1.e000696c9a2d1p-5', '-0x1.6902289c81ef7p-6', '0x1.026b1e397d33cp-3'],
 ['-0x1.fd4b0008e5e97p-4', '-0x1.02ef4d57a5961p-3', '0x1.ad4e81ff9e6e7p-2', '-0x1.6edcf42666c0dp-5', '0x1.741ddc47e48b6p-5', '-0x1.56877487e42dbp-4'],
 ['0x1.5668b652cb144p-5', '0x1.65fc837355488p-1', '-0x1.5498d060910d5p-2', '0x1.0689ca922ea1dp-3', '-0x1.794e2f23cc43ap-3', '0x1.ba8dc782dff1dp-2'],
 ['0x1.106266e11f4a1p-3', '-0x1.24d4b0d26bdadp-1', '0x1.453f1fbe3225ep-9', '0x1.15587a9626a81p-6', '-0x1.c58c4deddd176p-2', '0x1.59627cb9635c1p-1'],
 ['-0x1.b9387ff70eecfp-2', '0x1.4e3f4a89c1c8bp-3', '0x1.9890c04cfb8bfp-5', '-0x1.8939f7715fd6dp-4', '-0x1.a19e995722277p-3', '0x1.496d47acb1fc9p-3'],
 ['0x1.ba1fe1e7e6f10p-4', '-0x1.8355f105bfa0fp-4', '-0x1.55d68fd6b27eep-5', '0x1.f60f50d656a02p-3', '0x1.a2b5ceccbe514p-1', '0x1.c7e94e4bb06fbp-2'],
 ['0x1.ac879f2fa0ad6p-1', '0x1.7d3a8b33778f8p-5', '-0x1.65eea20eeac06p-7', '0x1.7e710cc94bc7bp-4', '-0x1.3a1c60260a802p-3', '-0x1.99c8d09b36cfcp-3'],
 ['-0x1.878c1469b385ap-3', '-0x1.9fc00b786dd4dp-4', '-0x1.5ba80cdca7b5fp-6', '0x1.e217da6393d96p-1', '-0x1.67ef92c40a3adp-3', '-0x1.7c8cc801ccac1p-3']]

ODD_LPOS_HEX = [['0x1.ce9c5aa735a3ep-1', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['-0x1.83fb7b1ebb550p-50', '0x1.370135f6ae37bp+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['0x1.8a6df5b4f2fa6p-52', '0x1.80ab4774ee24fp-51', '0x1.562304fa04b4ep+0', '0x0.0p+0', '0x0.0p+0', '0x0.0p+0'],
 ['-0x1.2d9bff04a21b1p-53', '0x1.7f75483a3a368p-51', '0x1.24dd032a23e4bp-50', '0x1.7241ae3283a9dp+0', '0x0.0p+0', '0x0.0p+0'],
 ['0x1.844229b999b80p-58', '0x1.8a5f773da9332p-53', '0x1.7f997e28d3149p-51', '-0x1.4cd20eeb53842p-52', '0x1.8f92beb3d6a7fp+0', '0x0.0p+0'],
 ['0x1.4e2073f43b389p-52', '0x1.d8e59b4d03de3p-54', '-0x1.8bf2df68f6f4bp-53', '0x1.bbcfa02b3994ap-52', '-0x1.490bb0dc81f2ap-53', '0x1.9d2107087aeefp+0']]

ODD_PAYLOAD_SHA256 = "550fc794249e79ebb943ac1771542f7c2940827bfe8dfe71c84acc9d477fed9f"


def floats(rows):
    return np.array([[float.fromhex(x) for x in row] for row in rows])


def payload_hash(qneg, lneg, qpos, lpos):
    raw = json.dumps(
        {"Qneg": qneg, "Lneg": lneg, "Qpos": qpos, "Lpos": lpos},
        separators=(",", ":"),
        sort_keys=True,
    ).encode()
    return hashlib.sha256(raw).hexdigest()


def exact_first_minor_det(qhex, k):
    a = [
        [Fraction.from_float(float.fromhex(x)) for x in row]
        for row in qhex[:k]
    ]
    det = Fraction(1)
    sign = 1
    for j in range(k):
        pivot = next((i for i in range(j, k) if a[i][j] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            sign *= -1
        p = a[j][j]
        det *= p
        for i in range(j + 1, k):
            if a[i][j] == 0:
                continue
            f = a[i][j] / p
            for m in range(j + 1, k):
                a[i][m] -= f * a[j][m]
    return sign * det


def verify_one(name, qneg, lneg, qpos, lpos, expected_hash):
    if payload_hash(qneg, lneg, qpos, lpos) != expected_hash:
        raise RuntimeError(f"{name}: frozen rho0.02 minus payload hash mismatch")

    dneg = exact_first_minor_det(qneg, 4)
    dpos = exact_first_minor_det(qpos, 6)
    if dneg == 0:
        raise RuntimeError(f"{name}: exact negative four-plane rank test failed")
    if dpos == 0:
        raise RuntimeError(f"{name}: exact positive six-plane rank test failed")

    Ln = floats(lneg)
    Lp = floats(lpos)
    if not all(Ln[i, i] > 0 for i in range(4)):
        raise RuntimeError(f"{name}: negative preconditioner diagonal failed")
    if not all(Lp[i, i] > 0 for i in range(6)):
        raise RuntimeError(f"{name}: positive preconditioner diagonal failed")

    Qn = floats(qneg)
    Qp = floats(qpos)
    return {
        "negative_exact_minor_nonzero": True,
        "positive_exact_minor_nonzero": True,
        "negative_minor_decimal": float(dneg),
        "positive_minor_decimal": float(dpos),
        "negative_gram_error_2norm": float(np.linalg.norm(Qn.T @ Qn - np.eye(4), 2)),
        "positive_gram_error_2norm": float(np.linalg.norm(Qp.T @ Qp - np.eye(6), 2)),
    }


if __name__ == "__main__":
    for args in (
        ("even-v", EVEN_QNEG_HEX, EVEN_LNEG_HEX, EVEN_QPOS_HEX, EVEN_LPOS_HEX, EVEN_PAYLOAD_SHA256),
        ("odd-v", ODD_QNEG_HEX, ODD_LNEG_HEX, ODD_QPOS_HEX, ODD_LPOS_HEX, ODD_PAYLOAD_SHA256),
    ):
        name = args[0]
        out = verify_one(*args)
        print(name)
        print(" sha256 =", args[-1])
        for k, v in out.items():
            print(" ", k, "=", v)
