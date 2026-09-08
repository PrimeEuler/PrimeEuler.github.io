#!/usr/bin/env python3
"""Coarse certificate targets for the fixed rational 77x6 witness W.

The v13.345 midpoint margins are so large that the final proof does not need
high-precision interval eigenvalues or coupling norms.  It is enough to certify
four deliberately rounded inequalities:

    W^T A0_FF W >= 0.18 I_6,
    ||W^T A0_F,[155,3001]||_F < 0.009,
    beta_{n>=3003} < 1.5e-4,
    alpha_155 > 0.0249.

Then beta_total < 0.00915 and the full adverse Schur correction is below

    0.00915^2 / 0.0249 < 0.00337,

leaving >0.1766 positive margin on the six-dimensional pole-free subspace.
Adding the PSD pole preserves positivity.

These coarse targets drastically reduce interval precision requirements.
"""
from __future__ import annotations
import math

FINITE_FORM_LOWER=0.18
FINITE_TAIL_FRO_UPPER=0.009
REMOTE_TAIL_UPPER=1.5e-4
TAIL_GAP_LOWER=0.0249

MID_FINITE_MIN=0.187445591522
MID_FINITE_TAIL_FRO=8.730696686245e-3
TAIL_COLUMNS=1424
PROJECTED_ROWS=6


def report():
    beta=FINITE_TAIL_FRO_UPPER+REMOTE_TAIL_UPPER
    penalty=beta*beta/TAIL_GAP_LOWER
    final=FINITE_FORM_LOWER-penalty
    fro_slack=FINITE_TAIL_FRO_UPPER-MID_FINITE_TAIL_FRO
    per_projected_entry_radius=fro_slack/math.sqrt(PROJECTED_ROWS*TAIL_COLUMNS)
    projected_form_entry_radius=(MID_FINITE_MIN-FINITE_FORM_LOWER)/PROJECTED_ROWS
    print('beta_total target =',beta)
    print('Schur penalty target =',penalty)
    print('final six-plane margin =',final)
    print('allowed projected finite-tail entry radius ~',per_projected_entry_radius)
    print('allowed projected 6x6 form entry radius ~',projected_form_entry_radius)


if __name__=='__main__': report()
