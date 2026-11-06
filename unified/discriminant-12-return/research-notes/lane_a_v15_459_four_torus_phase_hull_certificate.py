#!/usr/bin/env python3
"""Exact exponent-lattice certificate for the Lane A v15.459 phase hull."""

from fractions import Fraction


VECTORS = {
    2: (1, 0, 0, 0),
    3: (0, 1, 0, 0),
    4: (2, 0, 0, 0),
    5: (0, 0, 1, 0),
    7: (0, 0, 0, 1),
}


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        q = a[rank][col]
        a[rank] = [x / q for x in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][col]:
                q = a[i][col]
                a[i] = [x - q * y for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def main():
    assert VECTORS[4] == tuple(2 * x for x in VECTORS[2])
    assert rank(list(VECTORS.values())) == 4
    assert rank([VECTORS[p] for p in (2, 3, 5, 7)]) == 4
    print("status=PASS_EXACT_FOUR_TORUS_PHASE_HULL")
    print("independent_prime_phases=2,3,5,7")
    print("q4_phase_relation=zeta_4=zeta_2^2")
    print("phase_hull_dimension=4")
    print("joint_operator_norm_gate=UNEVALUATED")


if __name__ == "__main__":
    main()
