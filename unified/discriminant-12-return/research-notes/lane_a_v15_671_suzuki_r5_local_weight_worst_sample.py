#!/usr/bin/env python3
"""Outward local-weight R5 certificate at v15.670's worst fixed sample.

Recomputes a positive 40-step weight at x=1 and applies the same outward
weighted-B^4 Collatz enclosure.  This certifies one arc only, not C5 or C16.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import hashlib
import time
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location

import numpy as np

BASE = (
    "unified/discriminant-12-return/research-notes/"
    "lane_a_v15_664_suzuki_r3_outward_degree4_certificate.py"
)
spec = spec_from_file_location("base", BASE)
base = module_from_spec(spec)
spec.loader.exec_module(base)

R = 5
INDEX = 8651
POWER_STEPS = 40
CUTS = base.producer.cuts(R)
assert len(CUTS) == 17303
X = float((CUTS[INDEX] + CUTS[INDEX + 1]) / 2)
assert X == 1.0


def observed_row_sum(matrix):
    k = int(np.diff(matrix.indptr).max())
    value = float(np.asarray(abs(matrix).sum(axis=1)).ravel().max())
    return F.from_float(value), k


started = time.time()
b = base.producer.assemble(R, X)
b2 = b @ b
b4 = b2 @ b2
absolute_b4 = abs(b4)

weight = np.ones(b.shape[0], dtype=np.float64)
for _ in range(POWER_STEPS):
    weight = np.asarray(absolute_b4 @ weight).ravel()
    weight /= weight.max()
assert np.all(weight > 0)
weight_condition = F.from_float(float(weight.max())) / F.from_float(float(weight.min()))
weight_sha256 = hashlib.sha256(weight.tobytes(order="C")).hexdigest()

obs1, k1 = observed_row_sum(b)
obs2, k2 = observed_row_sum(b2)
k4 = int(np.diff(b4.indptr).max())
m = obs1 / (1 - base.gamma(k1))
c2 = obs2 / (1 - base.gamma(k2))
r2 = base.gamma(2 * k1) * m * m
r4 = r2 * (m * m + c2) + base.gamma(2 * k2) * c2 * c2
perturb = (m + base.E) ** 4 - m ** 4

ratios = np.asarray(absolute_b4 @ weight).ravel() / weight
observed = F.from_float(float(ratios.max()))
stored_upper = observed / (1 - base.gamma(2 * k4 + 1))
true_upper = stored_upper + weight_condition * (r4 + perturb)

print("R5_ARC_INDEX", INDEX, "MIDPOINT", X)
print("POWER_STEPS", POWER_STEPS, "WEIGHT_MIN", weight.min(),
      "WEIGHT_MAX", weight.max(), "WEIGHT_CONDITION", float(weight_condition))
print("WEIGHT_SHA256", weight_sha256)
print("NNZ", b.nnz, b2.nnz, b4.nnz, "ROW_LENGTHS", k1, k2, k4)
print("OBSERVED_WEIGHTED_B4", float(observed))
print("OUTWARD_WEIGHTED_B4", float(true_upper),
      "OUTWARD_FOURTH_ROOT", float(true_upper) ** 0.25)
print("TARGET4", float(F(41, 10) ** 4),
      "LOCAL_ARC_PASS", true_upper < F(41, 10) ** 4)
print("SECONDS", time.time() - started)
print("ONE_ARC_ONLY_NO_C5_OR_C16_CERTIFICATE")
