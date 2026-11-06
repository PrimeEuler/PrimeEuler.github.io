#!/usr/bin/env python3
"""Exact integer-exponent certificate for Lane A v15.462."""

N = 256001
PRIME_VECTORS = {
    2: (1, 0, 0, 0),
    3: (0, 1, 0, 0),
    5: (0, 0, 1, 0),
    7: (0, 0, 0, 1),
}


def start(a):
    return (2**a - 1) * N


def scale(v, k):
    return tuple(k * x for x in v)


def add(u, v):
    return tuple(x + y for x, y in zip(u, v))


def main():
    for a in range(32):
        assert start(a + 1) == 2 * start(a) + N
        for v in PRIME_VECTORS.values():
            lhs = scale(v, start(a + 1))
            rhs = add(scale(v, 2 * start(a)), scale(v, N))
            assert lhs == rhs
    q2 = PRIME_VECTORS[2]
    q4 = scale(q2, 2)
    assert scale(q4, start(17)) == scale(scale(q2, start(17)), 2)
    print("status=PASS_EXACT_ANNULUS_PHASE_DOUBLING")
    print("annulus_start_j_a=(2^a-1)N")
    print("anchor_recurrence=eta_(a+1)=rho*eta_a^2")
    print("rho_p=exp(i*pi*N*log(p)),p=2,3,5,7")
    print("q4_anchor=q2_anchor^2")
    print("joint_scale_fiber_norm_gate=UNEVALUATED")


if __name__ == "__main__":
    main()
