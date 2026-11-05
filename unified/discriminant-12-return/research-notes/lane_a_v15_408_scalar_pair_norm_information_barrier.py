#!/usr/bin/env python3
"""Sharp no-go for any cross-pair route retaining only ten scalar norms."""
import contextlib
import io

with contextlib.redirect_stdout(io.StringIO()):
    import lane_a_v15_405_cross_pair_cancellation_budget_certificate as base

F = base.F

# Information model: ten arbitrary self-adjoint operators A_i satisfying
# ||A_i|| <= B_i, where B_i are exactly the audited pair constants.
# The universal triangle estimate is sharp: on H=C choose A_i=B_i I.
# Then every individual constraint is saturated and ||sum A_i||=sum B_i.
aligned_sum = base.pair_sum
allowed_cross = base.allowed_cross
unavoidable_excess = aligned_sum - allowed_cross

assert aligned_sum.lo > allowed_cross.hi
assert F(6181, 1000) < aligned_sum.lo
assert aligned_sum.hi < F(6182, 1000)
assert F(1932, 1000) < unavoidable_excess.lo
assert unavoidable_excess.hi < F(1933, 1000)

print("information_model", "only self-adjointness and the ten individual bounds ||A_qr|| <= B_qr")
print("sharp_scalar_realization", "H=C and A_qr=B_qr*I for every pair")
print("aligned_joint_norm", float(aligned_sum.lo), float(aligned_sum.hi))
print("required_joint_budget", float(allowed_cross.lo), float(allowed_cross.hi))
print("certified_excess", float(unavoidable_excess.lo), float(unavoidable_excess.hi))
print("certified", "6.181 < sharp scalar-only universal bound < 6.182")
print("certified", "sharp scalar-only bound exceeds the required joint budget by more than 1.932")
print("conclusion", "no theorem using only the ten scalar pair norms and self-adjointness can certify the 4.249030150... budget")
print("next_data", "must retain shared translations, signed coefficient functions, or other simultaneous operator structure across distinct pairs")
print("scope", "information-model no-go only; not a lower bound for the physical cross sum or complete tail")
