#!/usr/bin/env python3
"""Deterministic structural witness for the v15.018 provenance obstruction."""

import json
from fractions import Fraction


def adjoint_entry(k_nm: Fraction, w_n: Fraction, w_m: Fraction) -> Fraction:
    # Real-rational specialization of (K*_w)[m,n]=(w_n/w_m)conj(K[n,m]).
    return (w_n / w_m) * k_nm


payload = {
    "formal_adjoint_weight_dependence": {
        "kernel_entry_K_n_m": "2",
        "weights_equal_adjoint_entry": str(adjoint_entry(Fraction(2), Fraction(1), Fraction(1))),
        "weights_3_to_1_adjoint_entry": str(adjoint_entry(Fraction(2), Fraction(3), Fraction(1))),
        "formula": "(K*_w)[m,n]=(w_n/w_m) conjugate(K[n,m])",
    },
    "certified_spike_tail": {
        "source": "v14.967/v14.969 exact-floor repair",
        "limit": "N*K[N,m1] -> -c*z_m1 != 0",
        "unweighted_series_exponent": -2,
        "unweighted_verdict": "convergent",
        "weight_N_series_exponent": -1,
        "weight_N_verdict": "divergent",
        "H_a_threshold": "column square-summable only for a<1/2",
    },
    "scope": "frozen data underdetermine Hilbert realization; no universal nonexistence claim",
}

assert payload["formal_adjoint_weight_dependence"]["weights_equal_adjoint_entry"] == "2"
assert payload["formal_adjoint_weight_dependence"]["weights_3_to_1_adjoint_entry"] == "6"

print(json.dumps(payload, indent=2, sort_keys=True))

