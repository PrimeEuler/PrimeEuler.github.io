#!/usr/bin/env python3
"""Sharp no-go for combining ten separate row maxima without location data."""
import contextlib
import io

with contextlib.redirect_stdout(io.StringIO()):
    import lane_a_v15_405_cross_pair_cancellation_budget_certificate as base

F = base.F

# Information model: nonnegative row-bound functions f_qr on one common
# index set X, with only the ten separate facts sup_X f_qr <= B_qr retained.
# This is already a simultaneous commutative model, but the maxima have lost
# all common-location information.  The universal estimate
#
#     sup_X sum_qr f_qr <= sum_qr B_qr
#
# is sharp on the singleton X={*}, taking every f_qr(*)=B_qr.
separate_max_sum = base.pair_sum
allowed_cross = base.allowed_cross
unavoidable_excess = separate_max_sum - allowed_cross

assert separate_max_sum.lo > allowed_cross.hi
assert F(6181, 1000) < separate_max_sum.lo
assert separate_max_sum.hi < F(6182, 1000)
assert F(1932, 1000) < unavoidable_excess.lo
assert unavoidable_excess.hi < F(1933, 1000)

print("information_model", "one common row domain X and only the ten separate bounds sup_X f_qr <= B_qr")
print("sharp_commutative_realization", "X={*} and f_qr(*)=B_qr for every pair")
print("sharp_joint_row_max", float(separate_max_sum.lo), float(separate_max_sum.hi))
print("required_joint_budget", float(allowed_cross.lo), float(allowed_cross.hi))
print("certified_excess", float(unavoidable_excess.lo), float(unavoidable_excess.hi))
print("certified", "6.181 < sharp separate-maxima universal bound < 6.182")
print("certified", "separate row maxima exceed the required joint budget by more than 1.932")
print("conclusion", "no theorem retaining only the ten separate row maxima can certify the 4.249030150... budget")
print("next_data", "must retain the signed pair row functions on a shared translation/torus domain, including where their extrema occur")
print("scope", "information-model no-go only; not a physical lower bound, cancellation certificate, complete tail, or stationary/infinite-capacity closure")
