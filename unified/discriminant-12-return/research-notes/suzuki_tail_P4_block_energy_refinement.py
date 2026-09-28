#!/usr/bin/env python3
"""Block-energy refinement of the v13.824 numerical P4 basis certificate.

v13.824 bounded the transformed residual by the global smooth-bulk floor.
That is safe but pessimistic because the residual is split between:

  F = tail modes 5..3999 (even) or 6..4000 (odd),
  R = the remaining tail.

On this decomposition the already-certified smooth bulk satisfies

    B_FF >= b I,
    B_RR >= g I,
    ||B_FR|| <= c,

with public constants

    even: b=0.0415-1e-10,
    odd : b=0.2400-1e-10,
    c<0.417,
    g>5.33.

For any residual r=(r_F,r_R),

    <r,B^{-1}r>
      = sup_x [2 Re<r,x> - <x,Bx>]

is therefore bounded by the inverse of the scalar 2x2 majorant

    M = [[b,-c],[-c,g]]

evaluated on (||r_F||,||r_R||).

The low-part residual is bounded by the audited finite-support residual from
v13.824.  The remote-part norm is bounded conservatively by the full
v13.824 Euclidean residual cap, so no cancellation is used.

This produces a substantially sharper transformed-residual / subspace-angle
certificate without changing the numerical basis or any frozen data.
"""
from __future__ import annotations

import math
import numpy as np

import suzuki_tail_P4_residual_basis_certificate as P
from suzuki_grouped_residue_error_certificate import COUPLING_SQUARED_CAP


LOW_RESIDUAL_CAP = {
    "even-v": 2.60e-4,
    "odd-v":  1.31e-3,
}

FINITE_B_FLOOR = {
    "even-v": 0.0415 - 1.0e-10,
    "odd-v":  0.2400 - 1.0e-10,
}

CROSS_CAP = 0.417
REMOTE_B_FLOOR = 5.33

ENERGY_RESIDUAL_CAP = {
    "even-v": 0.00580,
    "odd-v":  0.00880,
}

SIN_THETA_CAP = {
    "even-v": 0.0582,
    "odd-v":  0.0984,
}

ANGLE_DEG_CAP = {
    "even-v": 3.34,
    "odd-v":  5.65,
}

GROUPED_RESIDUE_ERROR_CAP = {
    "even-v": 0.00150,
    "odd-v":  0.00410,
}


def scalar_energy_cap(sector):
    b=FINITE_B_FLOOR[sector]
    c=CROSS_CAP
    g=REMOTE_B_FLOOR

    M=np.array([[b,-c],[-c,g]],dtype=float)
    ev=np.linalg.eigvalsh(M)
    if ev[0] <= 0:
        raise RuntimeError(("scalar bulk majorant not positive",sector,ev))

    v=np.array([
        LOW_RESIDUAL_CAP[sector],
        P.TOTAL_EUCLIDEAN_RESIDUAL_CAP[sector],
    ])

    return math.sqrt(float(v@np.linalg.inv(M)@v)),ev


def certify_sector(sector):
    # Re-run the complete v13.824 basis construction/certificate unchanged.
    row=P.certify_sector(sector)

    if row["finite_residual_operator"] >= LOW_RESIDUAL_CAP[sector]:
        raise RuntimeError((
            "low residual cap failed",
            sector,row["finite_residual_operator"],
        ))

    # Re-check the exact block constants rather than trusting only the
    # hard-coded public majorants.
    start=5 if sector=="even-v" else 6
    stop=3999 if sector=="even-v" else 4000
    modes=np.arange(start,stop+1,2,dtype=int)

    cross=P.cross_hilbert_hs_upper(modes,stop+2)
    if cross >= CROSS_CAP:
        raise RuntimeError(("cross cap failed",sector,cross))

    remote=math.log((stop+2)/4.0)-math.pi/2.0
    if remote <= REMOTE_B_FLOOR:
        raise RuntimeError(("remote B floor failed",sector,remote))

    energy,Meigs=scalar_energy_cap(sector)
    if energy >= ENERGY_RESIDUAL_CAP[sector]:
        raise RuntimeError(("energy residual cap failed",sector,energy))

    sep=0.10-P.RITZ_ABS_CAP[sector]
    sintheta=energy/sep
    angle=math.degrees(math.asin(sintheta))

    if sintheta >= SIN_THETA_CAP[sector]:
        raise RuntimeError(("sin theta cap failed",sector,sintheta))
    if angle >= ANGLE_DEG_CAP[sector]:
        raise RuntimeError(("angle cap failed",sector,angle))

    residue_error=sintheta*COUPLING_SQUARED_CAP[sector]
    if residue_error >= GROUPED_RESIDUE_ERROR_CAP[sector]:
        raise RuntimeError((
            "grouped residue cap failed",sector,residue_error
        ))

    return {
        "sector":sector,
        "finite_residual_actual":row["finite_residual_operator"],
        "low_residual_cap":LOW_RESIDUAL_CAP[sector],
        "full_euclidean_residual_cap":P.TOTAL_EUCLIDEAN_RESIDUAL_CAP[sector],
        "bulk_scalar_eigenvalues":Meigs,
        "cross_actual":cross,
        "remote_floor_actual":remote,
        "energy_residual":energy,
        "energy_residual_cap":ENERGY_RESIDUAL_CAP[sector],
        "separation":sep,
        "sin_theta":sintheta,
        "sin_theta_cap":SIN_THETA_CAP[sector],
        "angle_deg":angle,
        "angle_deg_cap":ANGLE_DEG_CAP[sector],
        "grouped_residue_error":residue_error,
        "grouped_residue_error_cap":GROUPED_RESIDUE_ERROR_CAP[sector],
    }


def main():
    rows=[
        certify_sector("even-v"),
        certify_sector("odd-v"),
    ]

    for row in rows:
        print("\nsector =",row["sector"])
        for k,v in row.items():
            if k!="sector":
                print(k,"=",v)

    print("\nPASS block-energy refinement of numerical P4 basis")
    print(
        "The numerical basis is unchanged; only the transformed-residual "
        "bound is sharpened by respecting the certified B_sm block geometry."
    )


if __name__=="__main__":
    main()
