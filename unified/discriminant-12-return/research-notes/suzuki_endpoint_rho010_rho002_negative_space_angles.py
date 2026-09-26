#!/usr/bin/env python3
"""Cross-radius diagnostic for frozen four-negative endpoint trial spaces.

This is a guardrail, not a theorem ingredient.  It compares the exact-dyadic
four-negative trial spaces frozen at rho=0.10 and rho=0.02 in ordinary
coefficient-space geometry.

The endpoint trial spaces certify inertia, but they need not be the canonical
spectral subspace of the generalized tail operator.  A substantial principal
angle therefore warns against treating the endpoint Ritz vectors themselves
as invariant "resonance modes."

The canonical object for the next Feshbach gate is the basis-free spectral
projector P4 of J_tail onto |delta|<0.02.
"""
from __future__ import annotations

import numpy as np

from suzuki_endpoint_M3999_frozen_four_negative_inputs import (
    EVEN_QNEG_HEX as EVEN_Q010_HEX,
    ODD_QNEG_HEX as ODD_Q010_HEX,
    EVEN_LNEG_HEX as EVEN_LNEG010_HEX,
    ODD_LNEG_HEX as ODD_LNEG010_HEX,
    EVEN_PAYLOAD_SHA256 as EVEN_SHA010,
    ODD_PAYLOAD_SHA256 as ODD_SHA010,
    verify_one as verify_010,
    floats as floats_010,
)
from suzuki_endpoint_M3999_rho002_minus_frozen_inputs import (
    EVEN_QNEG_HEX as EVEN_Q002_HEX,
    EVEN_LNEG_HEX as EVEN_LNEG002_HEX,
    EVEN_QPOS_HEX,
    EVEN_LPOS_HEX,
    EVEN_PAYLOAD_SHA256 as EVEN_SHA002,
    ODD_QNEG_HEX as ODD_Q002_HEX,
    ODD_LNEG_HEX as ODD_LNEG002_HEX,
    ODD_QPOS_HEX,
    ODD_LPOS_HEX,
    ODD_PAYLOAD_SHA256 as ODD_SHA002,
    verify_one as verify_002,
    floats as floats_002,
)


def principal_angles_deg(q1, q2):
    u1, _ = np.linalg.qr(q1)
    u2, _ = np.linalg.qr(q2)
    s = np.linalg.svd(u1.T @ u2, compute_uv=False)
    s = np.clip(s, -1.0, 1.0)
    return np.degrees(np.arccos(s))


def verify_payloads():
    verify_010("even-v", EVEN_Q010_HEX, EVEN_LNEG010_HEX, EVEN_SHA010)
    verify_010("odd-v", ODD_Q010_HEX, ODD_LNEG010_HEX, ODD_SHA010)
    verify_002(
        "even-v",
        EVEN_Q002_HEX, EVEN_LNEG002_HEX,
        EVEN_QPOS_HEX, EVEN_LPOS_HEX,
        EVEN_SHA002,
    )
    verify_002(
        "odd-v",
        ODD_Q002_HEX, ODD_LNEG002_HEX,
        ODD_QPOS_HEX, ODD_LPOS_HEX,
        ODD_SHA002,
    )


def report():
    verify_payloads()

    rows = {}
    for sector, q010h, q002h in (
        ("even-v", EVEN_Q010_HEX, EVEN_Q002_HEX),
        ("odd-v", ODD_Q010_HEX, ODD_Q002_HEX),
    ):
        q010 = floats_010(q010h)
        q002 = floats_002(q002h)
        angles = principal_angles_deg(q010, q002)
        rows[sector] = angles

        print("\nsector =", sector)
        print("principal angles deg =", angles)
        print("max angle deg =", float(np.max(angles)))

    # Loose, platform-stable diagnostic guards.
    assert rows["even-v"][2] < 0.5
    assert 30.0 < rows["even-v"][3] < 45.0
    assert rows["odd-v"][2] < 0.2
    assert rows["odd-v"][3] < 3.0

    print("\nPASS cross-radius endpoint-trial-space diagnostic")
    print(
        "Guardrail: endpoint negative trial bases are inertia certificates, "
        "not canonical resonance coordinates. Use the spectral projector P4 "
        "of J_tail for the four-channel Feshbach reduction."
    )


if __name__ == "__main__":
    report()
