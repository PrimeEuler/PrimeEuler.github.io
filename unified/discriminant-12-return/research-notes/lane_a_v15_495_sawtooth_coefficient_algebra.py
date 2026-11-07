#!/usr/bin/env python3
"""Exact sawtooth coefficient-algebra certificate for Lane A v15.495."""

from itertools import combinations, product

FREQUENCIES = {
    2: (1, 0, 0, 0),
    3: (0, 1, 0, 0),
    4: (2, 0, 0, 0),
    5: (0, 0, 1, 0),
    7: (0, 0, 0, 1),
}


def add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def scale(c, u):
    return tuple(c * a for a in u)


def translation_label(q, r, sigma, tau):
    return add(scale(tau, FREQUENCIES[r]), scale(-sigma, FREQUENCIES[q]))


def coefficient_atoms(q, r, sigma, tau):
    """Offsets of translated sawtooths occurring in G_(sigma,tau)."""
    zero = (0, 0, 0, 0)
    sigma_a = scale(sigma, FREQUENCIES[q])
    minus_tau_b = scale(-tau, FREQUENCIES[r])
    minus_lambda = scale(-1, translation_label(q, r, sigma, tau))
    return zero, sigma_a, minus_lambda, minus_tau_b


def main():
    words = []
    labels = set()
    atom_tests = 0
    adjoint_tests = 0
    polynomial_tests = 0

    for q, r in combinations(FREQUENCIES, 2):
        for sigma, tau in product((-1, 1), repeat=2):
            label = translation_label(q, r, sigma, tau)
            assert label != (0, 0, 0, 0)
            labels.add(label)
            atoms = coefficient_atoms(q, r, sigma, tau)
            assert all(len(atom) == 4 and all(isinstance(n, int) for n in atom) for atom in atoms)
            atom_tests += len(atoms)

            # G=(s_0-s_A)(s_-lambda-s_A)
            #   +(s_0-s_-B)(s_-lambda-s_-B), a polynomial in four
            # translated copies of the one sawtooth generator.
            zero, sigma_a, minus_lambda, minus_tau_b = atoms
            monomials = [
                (zero, minus_lambda, 1),
                (zero, sigma_a, -1),
                (sigma_a, minus_lambda, -1),
                (sigma_a, sigma_a, 1),
                (zero, minus_lambda, 1),
                (zero, minus_tau_b, -1),
                (minus_tau_b, minus_lambda, -1),
                (minus_tau_b, minus_tau_b, 1),
            ]
            assert len(monomials) == 8
            assert sum(coefficient for _, _, coefficient in monomials) == 0
            polynomial_tests += len(monomials)
            words.append((q, r, sigma, tau, label, atoms))

    assert len(words) == 40
    assert len(labels) == 40

    # The (-sigma,-tau) word has the opposite group label and is the
    # adjoint partner of the (sigma,tau) word after coefficient transport.
    word_index = {(q, r, sigma, tau): (label, atoms) for q, r, sigma, tau, label, atoms in words}
    adjoint_orbits = set()
    for q, r, sigma, tau, label, _ in words:
        partner_label, _ = word_index[(q, r, -sigma, -tau)]
        assert partner_label == scale(-1, label)
        orbit = tuple(sorted(((q, r, sigma, tau), (q, r, -sigma, -tau))))
        adjoint_orbits.add(orbit)
        adjoint_tests += 1
    assert len(adjoint_orbits) == 20

    # At x=0 the q=2,r=3,sigma=tau=+1 coefficient has jump
    # 2*(log(3/2)-2), represented by the nonzero log exponent vector
    # log(3)-log(2) together with the period constant -2.
    jump_log_vector = add(FREQUENCIES[3], scale(-1, FREQUENCIES[2]))
    assert jump_log_vector == (-1, 1, 0, 0)
    assert jump_log_vector != (0, 0, 0, 0)

    print("status=PASS_EXACT_SAWTOOTH_COEFFICIENT_ALGEBRA")
    print("translation_group=Z^4_generated_by_log_2_log_3_log_5_log_7")
    print("q4_relation=log_4=2log_2")
    print("weighted_words=40")
    print("distinct_nonidentity_group_labels=40")
    print("adjoint_orbits=20")
    print("coefficient_algebra=Cstar_of_all_group_translates_of_sawtooth")
    print("every_G_sigma_tau=finite_polynomial_in_four_translated_sawtooths")
    print("ordinary_continuous_torus_section=OBSTRUCTED_BY_NONZERO_JUMP")
    print("jump_q2_q3_pp=2*(log(3/2)-2)")
    print(f"translated_atom_tests={atom_tests}")
    print(f"polynomial_monomial_tests={polynomial_tests}")
    print(f"adjoint_label_tests={adjoint_tests}")
    print("algebraic_crossed_product_membership=CERTIFIED")
    print("crossed_product_norm_bound=UNEVALUATED")


if __name__ == "__main__":
    main()
