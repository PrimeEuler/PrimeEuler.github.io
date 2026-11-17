# Cone Derivation Ledger v15.1110 — Compact Maxwell stream function on the projected cone ellipse: rest offset, TT quadrupole and rate-of-change obstruction

**Date:** 2026-11-17 Eastern. **Gravity/Cone lane.** **Status:** [D] exact compactly supported vector potential whose divergence-free magnetic circulation follows the XY-projected cone ellipse, full source/charge continuity identities for general time-dependent shape, integrated magnetic stress/energy with an analytic G-free ratio; [N] no ellipse eccentricity, phase, acceleration/sech clock, metric action coupling or novel gravity coefficient dynamically selected; [O] self-consistent current/actuator constitutive action and boundary response and a matched K4 tidal test. **Immediately prewrite live HEAD:** 6752403c06b4b74eb794750584478d03ba69e93c. v15.1109 belongs to **External Audit Round 595** commit cd4196eaf8b1a450f6fdc2386f49754842c4edc6 (confirmed and checked). v15.1110 unique. Additive only; all prior certified, Suzuki, Audit, Sandbox and Muse objects preserved.

## Audit and prior-art control
Round 595/v15.1109 independently derived and re-executed v15.1105–1108, PASS, including the **physically nonsolenoidal** first prototype v15.1107 and its fully disclosed, valid, additive solenoidal correction. Gravity v15.1108, based on unmodified archived foundation PaperA Conic Theorem, proved the projected tilted-plane ellipse from T+e X=C and T²=X²+Y² has center d=-Ce/(1-e²), semiaxes A=C/(1-e²), B=C/sqrt(1-e²), focal relation d²=A²-B², and the exact `cosφ=tanh u, sinφ=sech u` trace. Its Kepler-style radial acceleration is **conditional on an externally given areal clock**. Gravity v15.1107 proved the *generic* azimuthal magnetic ellipse allows an m=2 tidal stress while the circular case cancels. This gate is new specifically because it uses **the archived cone's exact offset ellipse**, makes the magnetic field **compact in all three spatial dimensions and solenoidal**, computes its complete spatial TT stress and field energy, and checks a genuine shape-to-stress ratio without claiming the shape is a field equation.

## Gate 977 — exact compact Maxwell curl following the true cone-projected ellipse
Take x as the longitudinal axis of an incident plus-TT gravitational wave, and identify the projected cone cutting-plane coordinates X,Y with the transverse spatial y,z axes of a *candidate physical embedding*. That identification is an **additional correspondence assumption**, not a theorem of Maxwell or the Cone.

For 0≤e<1, C>0, define
d=-Ce/(1-e²), A=C/(1-e²), B=C/sqrt(1-e²).
Then the ellipse is q(y,z)=((y-d)/A)²+(z/B)²=1. Choose a compact real axial profile f(x) with ∫f(x)²dx=1; a concrete choice is
f(x)=[1-(x/L)²]^4 /sqrt(L*(65536/109395)) for |x|<L, zero outside.
Let F(q)=(1-q)^4 when q<1 and zero for q≥1. Define the vector potential (temporal gauge)
**A_EM=(ψ,0,0), ψ=ψ0 f(x)F(q)**,
where ψ0 is a **freely specified physical flux amplitude**, not a cone number. The magnetic field B=curl A=(0,∂zψ,-∂yψ) is exactly divergence-free and supported in a bounded elliptical cylinder of finite x extent (smoothed on its face by f). Its lines at fixed x follow level sets q=const: **concentric ellipses with the identical focus/center relation and shape ratio of the archived cone section**, scaled by sqrt(q). No magnetic monopole; the vector potential and actual source currents are necessary. Note that the nested scaled ellipses share center d, *not* the common absolute focus at the original cone origin: only the outer q=1 contour has focus precisely at that origin. This limitation matters if one demands every magnetic field line be a distinct cone section with the **same** origin focus; that stronger requirement is not established by this field.

For a time-dependent ψ(x,y,z,t), choose the same vector potential and scalar potential zero so E=(-∂tψ,0,0). In conventional units c_light=ε0=μ0=1, define
ρ=div E=-∂x∂tψ,
J_x=(curl B)_x-∂t E_x=-(∂y²+∂z²)ψ+∂t²ψ,
J_y=∂x∂yψ, J_z=∂x∂zψ.
These obey Faraday, div B=0, Gauss, Ampere and continuity ∂tρ+div J=0 **identically**. Thus any smooth imposed shape e(t) is kinematically compatible with a conserved electromagnetic 4-current; however J,ρ are **defined by the prescribed field** rather than predicted by a physical material equation. One cannot infer a realizable passive amplifier or source energy without an actuator/charge dynamics model. A static ψ has E=ρ=0 and nonzero compact J=curl B supporting magnetic circulation.

## Gate 978 — integrated Maxwell TT stress is set by projected eccentricity, not position
For an initial static field, the magnetic energy is
U_B=(1/(2μ0))∫(B_y²+B_z²)d³x.
Use ellipse coordinates y=d+A r cosφ, z=B r sinφ with 0≤r<1, Jacobian A B r. Since ∫f²dx=1,
B_y=ψ0 f(x) (2r/B)F'(r²)sinφ,
B_z=-ψ0 f(x)(2r/A)F'(r²)cosφ.
The angular integrals are ∫cos²φ=∫sin²φ=π, the radial integral for F(q)=(1-q)^4 is
**∫_0^1 r³[F'(r²)]² dr=1/7**.
The integrated spatial momentum-flux stress difference (Maxwell convention T_ij=u δ_ij - B_i B_j/μ0) is
**I_plus=∫(T_yy-T_zz)d³x=-(4π ψ0²/(7μ0)) e²/sqrt(1-e²).**
The integrated magnetic energy is
**U_B=(2π ψ0²/(7μ0)) (2-e²)/sqrt(1-e²).**
Therefore the exact dimensionless ratio in this *particular specified source family* is
**I_plus/U_B= -2e²/(2-e²)**,
and the aligned cross overlap is ∫T_yz=0 by angular reflection. A rotation of the elliptical field's principal axes rotates the plus and cross response through 2 times that angle. For the circular limit e=0 the complete co-axial TT overlap vanishes. The axial width L, center offset d, scale C, overall ψ0 and μ0 cancel **in the ratio**, because of the deliberately L2-normalized axial source amplitude and self-similar F profile. This ratio is **not claimed universal for all divergenceless fields on the same boundary**: a different radial stream profile, additional electric fields, physical current support, or a different embedding can alter the relative stress distribution.

The physical *translation* of an otherwise identical field does not change integrated stress at all: d drops out by change of variables. Within the cone-cut family the **ellipticity** is algebraically tied to the offset d/C=-e/(1-e²), so the geometry supplies a reexpression of the eccentricity ratio in dimensionless cone-offset coordinates. The geometry alone supplies **no value of e**. In particular the arithmetic EM ±1/2 and gravity ±1/4 grid offsets are not themselves e, d/C or a physical spatial ellipse axis; setting e to 1/2 or 1/4 is only illustrative, NOT a derivation or selection law.

## Gate 979 — small-e analysis and rate-of-change
At fixed ψ0 and the normalized f, expand:
I_plus= -(4πψ0²/(7μ0)) [e²+(1/2)e⁴+O(e⁶)],
U_B=(4πψ0²/(7μ0)) + (πψ0²/(14μ0)) e⁴+O(e⁶).
Thus quadrupolar stress responds at order e² while the *total* magnetic stored energy shifts only at order e⁴ for this chosen profile and normalization. The exact shape derivatives are
dU_B/de = (2πψ0²/(7μ0)) e³/(1-e²)^(3/2),
dI_plus/de = -(4πψ0²/(7μ0)) e(2-e²)/(1-e²)^(3/2).
This does not mean shape can change without energy or actuator force: a time-dependent e(t) creates E_x=-ψdot, field electric energy, J·E work, electromagnetic momentum and possibly moving-support stresses, which are absent from the frozen-magnetic U_B(e) alone.

For a weak, externally specified plus-polarized tidal strain h(t) propagating along x, with the fixed lab axes above, the first-order **external metric work** corresponding to the Maxwell stress is
P_tidal=-(1/2) hdot(t) I_plus(e)
=+[2π ψ0²/(7μ0)] hdot e²/sqrt(1-e²),
subject to the fixed-coordinate and support bookkeeping already stated in v15.1105–1107. For time-varying e(t), the coefficient I_plus(e(t)) also changes, but that variation needs an independent source dynamical equation and a total energy budget; it does not follow from the tanh/sech parameterization of the ellipse or the row/column acceleration parabolas. A constant e with a finite h pulse returning to zero and with the currents rigidly externally held gives zero **integrated first-order work** ∫P_tidal dt ∝ h_final-h_initial=0; genuine net pumping requires a changing, phase-correlated field stress or dissipative/boundary dynamics. This guards against interpreting a nonzero instantaneous power density as indefinite energy gain.

## Gate 980 — status, reproducibility and next decision
Locally executed full derivation script in container prior to GitHub transcription: **PASS** focal geometry, analytic radial integral, stress, energy and ratio, compact axial normalization 65536/109395, Maxwell solenoidal and continuity differential identities, and illustrative eccentricity evaluations. Additive source `research-notes/k4_compact_cone_ellipse_maxwell_tt_v15_1110.py`, commit **6752403c06b4b74eb794750584478d03ba69e93c**, contains the same exact calculation and checks. Independent committed-byte Audit pending.

**Positive:** an exact, normalized *Cone-ellipse-shaped* compact Maxwell current exists; the associated nonzero tidal TT work coefficient has a computable dimensionless eccentricity dependence. The rest offset is mathematically associated to eccentricity but not separately read by total stress. **Negative:** the coefficient is already a conventional Maxwell anisotropic stress; no Cone-specific electromagnetic current, absolute physical acceleration timing, phase locking, K4 metric source or experimentally distinguishable gravitational observable has been derived.

**Next gate:** give e(t) and the associated acceleration/deceleration parabolas a source-consistent dynamics (possibly a finite elastic/inductive circuit under a tidal h(t)) and compute the *complete* electromechanical + metric energy ledger; compare to matched standard Einstein–Maxwell+elastic solid. Independently test whether the cone's sech speed/angle law can fix a physical time evolution without postulating an areal clock. A null result is acceptable and must be ledgered.

**Audit handoff:** verify projected versus intrinsic cone ellipse eccentricity, field line focus limitation for interior q<1, magnetic curl sign/normalization, compact axial support, full charge/current continuity for time-varying ψ, angular/radial integrals and dimensionless -2e²/(2-e²) ratio, and the e² versus e⁴ small-e asymptotics. Verify that tidal work and source work are not double-counted and that a static e and returning h pulse produces zero integrated first-order work.
