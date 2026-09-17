# M16001 Q/N formation transcript contract

Status: audit scaffold; fail closed; no theorem promotion.

This contract closes the ambiguity identified in ledger v13.505/v13.510 about how the normalized Q/N block's floating-point radius is to be produced.

The *actual M16001 replay* must emit an `.npz` containing:

- `qn_mid[m,n]`: the long-double midpoint of every normalized Q/N entry used by the seven-plane Schur calculation;
- `qn_absprod[m,n]`: for that same entry, the reduction majorant `sum_i abs(x_i*y_i)` from the actual operands entering the dot product;
- `qn_k`: either a scalar common dot length or an integer array matching `qn_mid`.

The checker `suzuki_M16001_QN_formation_transcript.py` derives, without an accepted radius literal,

`rad_ij = gamma_{k_ij} * qn_absprod_ij`,

with `gamma_k = k*u/(1-k*u)` and `u=2^-p`, where `p` is the detected `longdouble` significand precision. It fails if `p<64`.

The first conservative block enclosure is

`||B_QN||_2 <= ||B_QN_mid||_F + ||Rad_QN||_F`.

This deliberately uses a Frobenius midpoint majorant so that the checker does not silently rely on an uncertified spectral-norm routine. If this is too loose for the final margin, a later helper may add a separately outward-certified spectral midpoint bound while retaining the same entrywise radii.

## Producer requirements

The producer must instrument the code path that forms the Q/N block used by the final M16001 replay. Recomputing a mathematically similar block in a separate convenience path is not sufficient. The emitted `qn_mid`, `qn_absprod`, and `qn_k` must correspond entry-for-entry.

If an entry is formed by more than one rounded stage (for example a dot product followed by scaling/normalization or subtraction), the producer must emit the intermediate magnitudes and operation counts too, and the checker must be extended to charge those stages before this gate can be marked closed. A dot-product-only transcript is accepted only when the inspected producer shows that this is the complete rounded formation path.

No empirical binary64/long-double difference and no hand-selected safety multiplier may substitute for the emitted magnitude accounting.
