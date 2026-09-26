#!/usr/bin/env python3
"""Final rho=0.02 parity-tail inertia certificate.

This theorem wrapper consumes the v13.818 frozen payloads unchanged and the
v13.820 widened audit caps unchanged.  It does not regenerate any frozen
eigenspace or Cholesky factor.

Certified conclusions, sector by sector:

    ind_-(F^-_{0.02,tail}) = 4,  ker F^-_{0.02,tail} = {0},
    ind_-(F^+_{0.02,tail}) = 0,  ker F^+_{0.02,tail} = {0},

hence, by the generalized-pencill inertia-difference identity,

    N_tail(0.02)
      = ind_-(F^-_{0.02,tail}) - ind_-(F^+_{0.02,tail})
      = 4.

Equivalently, for the compact relative tail operator K, exactly four
generalized eigenvalues lie in the sector-wise resonance window

    (-1.02, -0.98).

No direct-sum multiplicity claim across parity sectors is made here.
"""
from __future__ import annotations

import numpy as np

import suzuki_endpoint_M3999_rho002_adversarial_audit as A
from suzuki_endpoint_M3999_rho002_minus_frozen_inputs import (
    EVEN_QNEG_HEX, EVEN_LNEG_HEX, EVEN_QPOS_HEX, EVEN_LPOS_HEX,
    EVEN_PAYLOAD_SHA256, ODD_QNEG_HEX, ODD_LNEG_HEX,
    ODD_QPOS_HEX, ODD_LPOS_HEX, ODD_PAYLOAD_SHA256,
    floats as minus_floats, verify_one as verify_minus_payload,
)
from suzuki_endpoint_M3999_rho002_plus_frozen_L0 import (
    EVEN_L0_HEX, EVEN_SHA256, ODD_L0_HEX, ODD_SHA256,
    floats as plus_floats, verify_one as verify_plus_payload,
)


# Public fail-closed theorem margins.  These are deliberately the widened,
# audited v13.820 lower bounds, not best midpoint values.
NEGATIVE_RAW_LOWER = {
    "even-v": 0.00266179948027,
    "odd-v":  0.00398570593918,
}
NEGATIVE_NORMALIZED_LOWER = {
    "even-v": 0.99999991429,
    "odd-v":  0.99999984934,
}
MINUS_POSITIVE_TERMINAL_LOWER = {
    "even-v": 3.13191084098,
    "odd-v":  3.17134400520,
}
MINUS_POSITIVE_NORMALIZED_LOWER = {
    "even-v": 0.9848679786,
    "odd-v":  0.9972258994,
}
PLUS_TERMINAL_LOWER = {
    "even-v": 3.34990486435,
    "odd-v":  3.35907757792,
}
PLUS_NORMALIZED_LOWER = {
    "even-v": 0.9871476699,
    "odd-v":  0.9898083969,
}


def frozen_payloads():
    # Fail closed before any theorem arithmetic.
    verify_minus_payload(
        "even-v",
        EVEN_QNEG_HEX, EVEN_LNEG_HEX,
        EVEN_QPOS_HEX, EVEN_LPOS_HEX,
        EVEN_PAYLOAD_SHA256,
    )
    verify_minus_payload(
        "odd-v",
        ODD_QNEG_HEX, ODD_LNEG_HEX,
        ODD_QPOS_HEX, ODD_LPOS_HEX,
        ODD_PAYLOAD_SHA256,
    )
    verify_plus_payload("even-v", EVEN_L0_HEX, EVEN_SHA256)
    verify_plus_payload("odd-v", ODD_L0_HEX, ODD_SHA256)

    minus = {
        "even-v": (
            minus_floats(EVEN_QNEG_HEX),
            minus_floats(EVEN_LNEG_HEX),
            minus_floats(EVEN_QPOS_HEX),
            minus_floats(EVEN_LPOS_HEX),
        ),
        "odd-v": (
            minus_floats(ODD_QNEG_HEX),
            minus_floats(ODD_LNEG_HEX),
            minus_floats(ODD_QPOS_HEX),
            minus_floats(ODD_LPOS_HEX),
        ),
    }
    plus = {
        "even-v": plus_floats(EVEN_L0_HEX),
        "odd-v": plus_floats(ODD_L0_HEX),
    }
    return minus, plus


def certify_sector(sector, frozen_minus, frozen_plus):
    qneg, lneg, qpos, lpos = frozen_minus[sector]

    minus_block = A.build_blocks(sector, -1)
    plus_block = A.build_blocks(sector, +1)

    neg = A.audit_subspace(
        "minus-neg",
        minus_block,
        qneg,
        lneg,
        negative=True,
    )
    pos = A.audit_subspace(
        "minus-pos",
        minus_block,
        qpos,
        lpos,
        negative=False,
    )
    plus = A.audit_subspace(
        "plus",
        plus_block,
        np.eye(10),
        frozen_plus[sector],
        negative=False,
    )

    pos_remote = A.audit_remote(pos)
    plus_remote = A.audit_remote(plus)

    # Four independent strict negative directions.
    if not neg["raw_margin"] > NEGATIVE_RAW_LOWER[sector]:
        raise RuntimeError(("negative raw theorem margin failed", sector))
    if not neg["normalized_lower"] > NEGATIVE_NORMALIZED_LOWER[sector]:
        raise RuntimeError(("negative normalized theorem margin failed", sector))

    # Infinite remote-corrected codimension-four positive side.
    if not pos_remote["margin"] > MINUS_POSITIVE_TERMINAL_LOWER[sector]:
        raise RuntimeError(("minus positive terminal theorem margin failed", sector))
    if not pos_remote["normalized"] > MINUS_POSITIVE_NORMALIZED_LOWER[sector]:
        raise RuntimeError(("minus positive normalized theorem margin failed", sector))

    # Full plus-endpoint positivity.
    if not plus_remote["margin"] > PLUS_TERMINAL_LOWER[sector]:
        raise RuntimeError(("plus terminal theorem margin failed", sector))
    if not plus_remote["normalized"] > PLUS_NORMALIZED_LOWER[sector]:
        raise RuntimeError(("plus normalized theorem margin failed", sector))

    # The inertia conclusions are now exact integer consequences:
    #
    # minus:
    #   four-dimensional negative graph trial space  => ind_- >= 4,
    #   codimension-four positive complement         => ind_<=0 <= 4,
    #   therefore ind_- = 4 and ker = 0.
    #
    # plus:
    #   positive finite Schur core + positive eliminated blocks => F^+ > 0,
    #   therefore ind_- = 0 and ker = 0.
    minus_index = 4
    plus_index = 0
    count = minus_index - plus_index

    return {
        "sector": sector,
        "negative_raw_margin": neg["raw_margin"],
        "negative_normalized_margin": neg["normalized_lower"],
        "minus_positive_terminal_margin": pos_remote["margin"],
        "minus_positive_normalized_margin": pos_remote["normalized"],
        "plus_terminal_margin": plus_remote["margin"],
        "plus_normalized_margin": plus_remote["normalized"],
        "minus_index": minus_index,
        "plus_index": plus_index,
        "minus_kernel_dimension": 0,
        "plus_kernel_dimension": 0,
        "N_tail_0p02": count,
    }


def main():
    frozen_minus, frozen_plus = frozen_payloads()

    # Re-prove the two shared analytic audit assumptions before promotion.
    zbound = A.prove_far_generator()
    cross = A.common_cross_cap_check()
    print("far endpoint-generator upper interval =", zbound)
    print("remote cross component totals =", cross)

    rows = [
        certify_sector("even-v", frozen_minus, frozen_plus),
        certify_sector("odd-v", frozen_minus, frozen_plus),
    ]

    for row in rows:
        print("\nsector =", row["sector"])
        for key, value in row.items():
            if key != "sector":
                print(key, "=", value)

        assert row["minus_index"] == 4
        assert row["plus_index"] == 0
        assert row["minus_kernel_dimension"] == 0
        assert row["plus_kernel_dimension"] == 0
        assert row["N_tail_0p02"] == 4

    print("\nPASS: rho=0.02 parity-tail inertia theorem")
    print(
        "For each parity sector: ind_-(F^-_0.02,tail)=4, "
        "ind_-(F^+_0.02,tail)=0, both endpoint kernels are zero, "
        "and N_tail(0.02)=4."
    )
    print(
        "Equivalent compact-relative statement: exactly four sector-wise "
        "tail eigenvalues of K lie in (-1.02,-0.98)."
    )
    print(
        "Guardrail: no parity-direct-sum multiplicity claim and no statement "
        "about the separate two-mode low-core Feshbach problem."
    )


if __name__ == "__main__":
    main()
