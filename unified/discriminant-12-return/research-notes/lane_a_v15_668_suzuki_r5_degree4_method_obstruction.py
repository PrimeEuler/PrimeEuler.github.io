#!/usr/bin/env python3
"""Certified one-arc obstruction to the direct R=5 B^4 Schur method.

This imports the independently audited v15.664 interval/error machinery,
certifies the full R=5 cut ordering, selects the R=5 arc containing the R=4
maximizer, and proves a lower bound on ||B_F5(x)^4||_infinity above 4.10^4.

That only obstructs this positive-polynomial/absolute-row certificate.  It is
not a lower bound on ||B_F5(x)|| and is not evidence against C5 or C16.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import time
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product

import numpy as np

BASE = (
    "unified/discriminant-12-return/research-notes/"
    "lane_a_v15_664_suzuki_r3_outward_degree4_certificate.py"
)
spec = spec_from_file_location("base", BASE)
base = module_from_spec(spec)
spec.loader.exec_module(base)

R = 5
TARGET_X = 0.05145728861651011
TARGET4 = F(41, 10) ** 4


def cut_interval(k):
    value = (F(), F())
    for ki, q in zip(k, (2, 3, 5, 7)):
        value = base.add(value, base.scale(base.LS[q], -ki))
    return base.mod2(value)


exact_cuts = []
for k0 in range(-R - 1, R + 2):
    for k1, k2, k3 in product(range(-R, R + 1), repeat=3):
        exact_cuts.append(cut_interval((k0, k1, k2, k3)))
exact_cuts.sort(key=lambda z: z[0])
for left, right in zip(exact_cuts, exact_cuts[1:]):
    assert left[1] < right[0]

float_cuts = base.producer.cuts(R)
assert len(exact_cuts) == len(float_cuts) == 17303
for interval, cut in zip(exact_cuts, float_cuts):
    cut_fraction = F.from_float(float(cut))
    assert interval[0] - base.TOL < cut_fraction < interval[1] + base.TOL

index = int(np.searchsorted(float_cuts, TARGET_X) - 1) % len(float_cuts)
wrap = index + 1 == len(float_cuts)
right = float(float_cuts[(index + 1) % len(float_cuts)]) + (2 if wrap else 0)
unwrapped_midpoint = (float(float_cuts[index]) + right) / 2
midpoint = unwrapped_midpoint % 2
midpoint_fraction = F.from_float(unwrapped_midpoint)
right_low = exact_cuts[(index + 1) % len(exact_cuts)][0] + (2 if wrap else 0)
assert midpoint_fraction > exact_cuts[index][1] + base.MARGIN
assert midpoint_fraction < right_low - base.MARGIN


def observed_row_sum(matrix):
    k = int(np.diff(matrix.indptr).max())
    value = float(np.asarray(abs(matrix).sum(axis=1)).ravel().max())
    return F.from_float(value), k


started = time.time()
b = base.producer.assemble(R, midpoint)
b2 = b @ b
b4 = b2 @ b2
obs1, k1 = observed_row_sum(b)
obs2, k2 = observed_row_sum(b2)
obs4, k4 = observed_row_sum(b4)

# Upper enclosures used in the audited v15.664 forward-error formulas.
m = obs1 / (1 - base.gamma(k1))
c2 = obs2 / (1 - base.gamma(k2))
r2 = base.gamma(2 * k1) * m * m
r4 = r2 * (m * m + c2) + base.gamma(2 * k2) * c2 * c2
perturb = (m + base.E) ** 4 - m ** 4

# If s=fl(sum_j |B4_ij|) on the maximizing computed row, then the exact
# row sum of the stored float matrix is at least s/(1+gamma(k4)).  Subtract
# the certified infinity-norm arithmetic and coefficient perturbations.
lower_stored_row = obs4 / (1 + base.gamma(k4))
certified_lower = lower_stored_row - r4 - perturb
certified_upper = obs4 / (1 - base.gamma(k4)) + r4 + perturb

print("R5_CUTS", len(float_cuts), "ARC_INDEX", index, "MIDPOINT", midpoint)
print("MAX_EXACT_WORD_STATE_ERROR", float(base.max_state_error))
print("NNZ", b.nnz, b2.nnz, b4.nnz, "ROW_LENGTHS", k1, k2, k4)
print("OBSERVED_B4_ROW", float(obs4), "OBSERVED_ROOT", float(obs4) ** 0.25)
print("ARITHMETIC_R4_ERROR", float(r4), "COEFFICIENT_PERTURBATION", float(perturb))
print("CERTIFIED_B4_ROW_INTERVAL", float(certified_lower), float(certified_upper))
print("TARGET4", float(TARGET4), "METHOD_OBSTRUCTION", certified_lower > TARGET4)
print("SECONDS", time.time() - started)
print("NO_SPECTRAL_NORM_LOWER_BOUND")
print("NO_C5_OR_C16_CONCLUSION")
