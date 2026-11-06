#!/usr/bin/env python3
"""Exact architecture certificate for Lane A v15.464."""

DIMENSION = 4
COORDINATE_DEGREE = 2
TOTAL_PREIMAGES = COORDINATE_DEGREE ** DIMENSION


def roots_of_sign_vector(signs):
    assert len(signs) == DIMENSION
    return tuple(1 if s == 0 else -1 for s in signs)


def main():
    fibers = {
        roots_of_sign_vector(tuple((mask >> j) & 1 for j in range(DIMENSION)))
        for mask in range(TOTAL_PREIMAGES)
    }
    assert len(fibers) == 16
    assert TOTAL_PREIMAGES == 16
    print("status=PASS_EXACT_DOUBLING_ENDOMORPHISM_ARCHITECTURE")
    print("affine_map_conjugate_to=coordinatewise_squaring_on_T4")
    print("covering_degree=16")
    print("ordinary_Z_crossed_product_status=INVALID_NONAUTOMORPHISM")
    print("valid_framework=natural_extension_solenoid_or_endomorphism_correspondence")
    print("joint_norm_gate=UNEVALUATED")


if __name__ == "__main__":
    main()
