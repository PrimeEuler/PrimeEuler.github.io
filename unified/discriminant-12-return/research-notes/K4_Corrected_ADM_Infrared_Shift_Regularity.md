# Gate v15.001: Infrared ADM shift regularity from corrected SVT payload
Date 2026-10-27. Parents gravity v14.996 reconciliation, v14.998, v15.000. Source payload am3scalar_svt_reconciliation_v14_996/RECONCILIATION_NOTE.md read directly, live HEAD checked. Additive research-only; Suzuki physical weld parked; protected other lanes untouched.

Corrected reduced action kinetic coefficients (variables and Fourier normalizations as in v14.996):
A_S(k,τ)=√3 τ³/[54(k²+1)], A_V(k,τ)=√3 τ³/[18(3k²+4)]. Their k→0 limits are √3 τ³/54 and √3 τ³/72, strictly positive and finite at τ>0, so the reduced quadratic physical modes show NO kinetic coefficient IR pole for this normalization (in contrast erroneous v14.993). Mode k=0 remains a special global/homogeneous gauge/relabeling problem, not necessarily physical.

Vector auxiliary shift explicitly V(k)=4√3 τ dotπ_T/[9k³+12k]. Although V itself behaves like 1/k for a nonzero fixed dotπ_T as k→0, the derivative kV=4√3 τ dotπ_T/[9k²+12] is bounded uniformly for k≥0, with limit √3 τ dotπ_T/3. Geometric ADM extrinsic curvature features derivatives of shift, so this demonstrates a concrete cancellation for a physical derivative; NOT proof every ADM component is IR-controlled. On R³, bounded multiplier k/(9k³+12k) avoids an IR singular in differentiated vector shift, under appropriate Fourier norms; on T³, zero mode treated separately.

No exact second-order nonlinear Hamiltonian/momentum source has been computed. Quadratic mode convolution of k1 and k2 can produce k=k1+k2→0 even when each input is nonzero; first-order bounded kV does not automatically imply quadratic sources vanish O(k²), nor uniform estimate for undifferentiated shift. Full nonlinear constraint inversion and energy bootstrap remain OPEN. Distinguish τ-dependent prefactors from uniform logarithmic-time energy estimates.

NEXT: extract or derive explicit second-order ADM scalar/vector constraint source in fixed regular gauge, examine convolution zero-mode and whether Ward identities force derivative factors; retain the exact corrected unreduced action as reference, don't resurrect v14.993 ghost band.
