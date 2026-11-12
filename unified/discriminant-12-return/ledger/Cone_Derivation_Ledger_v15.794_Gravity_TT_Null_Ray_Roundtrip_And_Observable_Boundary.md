# Cone Derivation Ledger v15.794 — Gravity: first-order tensor null-ray round-trip detector benchmark and limits of spatial arm averaging

**Date:** 2026-11-12 US Eastern. **Parents:** original K4 EH+solid action v14.928/935; conventional elasticity comparator v15.706/760; v15.787 full local Fermi Riemann; v15.788 full scalar/vector/tensor compact-source local tidal readings; additive repair v15.792; finite-arm fixed-time *spatial proxy* v15.793. **Prewrite live HEAD:** 496e77ed799486741c4cab4d3b1affde97196275; target file absent; all changes additive, Suzuki frozen objects untouched.

**Categories:** [D] first-order null-geodesic outbound and return photon travel-time integral for a conventional transverse-traceless plane Fourier metric perturbation in local Minkowski spacetime; [D] exact local, stationary-spatial and orthogonal-arm limits and temporal response zeros; [N] new Cone operator, novel tidal coupling or source-independent detector response; [O] full FLRW/source-driven K4 scalar/vector/tensor photon propagation with freely moving mirrors and finite source-to-detector distance.

## Gate 410 — standard flat-local TT photon travel time from null paths

In a local Minkowski region choose metric signature (−+++) and linear perturbation

**ds²=−dt²+[δ_ij+h_ij(t,x)]dx^i dx^j**,

**h_ij=H_ij exp[−iωt+i k·x]**,

with H transverse/traceless for the conventional GR tensor-wave physical comparator. Two freely falling test mirrors can be at fixed spatial coordinates in TT gauge to first order in the usual plane-wave setting; for other metric sectors this gauge simplification need not hold.

A laser pulse emitted from the beam splitter at coordinate t_e travels along arm unit vector u to an end mirror at spatial distance L and returns. To first order evaluate the metric perturbation on the **unperturbed** outbound path (t,x)=(t_e+s,su) and inbound path (t,x)=(t_e+L+s,(L−s)u), 0≤s≤L. The first-order travel-time correction is

**δT_RT = (L/2) H_uu exp(−iω t_e) 𝒯(x,y)**,

where **H_uu=u_i u_j H_ij**, x=ωL, y=(k·u)L and

**𝒯(x,y)=F(y−x)+exp[i(y−x)]F(−y−x)**,

**F(v)=[exp(iv)−1]/(iv)=exp(iv/2) sinc(v/2)**, with F(0)=1.

This directly includes the **different time phase** along outbound and inbound light rays. A fixed-time spatial arm average, as in v15.793, does not capture this causal phase sampling. The expression is the standard linearized local TT response of a simple round-trip light path, not a finished detector model for an expanding K4 background.

## Gate 411 — exact limiting checks and real transfer zeros

At long wavelength and low frequency x→0,y→0,

**𝒯→2**, so **δT_RT→L H_uu exp(−iωt_e)**, matching the first-order round-trip metric-length change.

For a static spatial grating x=0 (formal transfer control),

**𝒯(0,y)=2F(y)**,

which is twice the spatial-phase transfer of the fixed-time averaging proxy. This static grating is not an on-shell vacuum massless TT gravitational wave at nonzero k; it is solely a mathematical check on the propagation integral.

For an arm perpendicular to wavevector (y=0),

**𝒯(x,0)=F(−x)[1+exp(−ix)]**.

At x=2πm (integer m≠0), the response of that arm has an exact temporal transfer zero despite a nonzero TT metric polarization overlap. Such frequency-dependent nulls are ordinary interferometer light-travel sampling, not an absent gravitational mode.

For general oblique arm direction, source frequency and arm length, the round-trip light travel is a complex frequency response. The real measured time delay is the real part after ±k and ±ω conjugate pairing. Geometry and frequency can suppress an otherwise nonzero conventional physical response.

## Gate 412 — the originality and detector boundary

Our K4 solid tensor sector has the usual metric tensor graviton and, at the level explicitly derived, standard Einstein–Hilbert kinetic propagation. The physical tensor transfer of a finite detector is not determined by a local electric-Riemann coefficient alone: finite-frequency light propagation, source/mirror motion, cosmological metric changes and signal emission/reception synchronization matter.

The derivation in this gate does **not** yet apply to the coasting-FLRW K4 scalar and vector metric sectors, because mirror acceleration and gauge constraints modify the null-ray signal; nor does it propagate the compact physical canonical source from v15.750–788 to a remote detector. A proper calculation must simultaneously include emitter worldline, mirror worldlines, constrained metric, null geodesics and finite light travel.

Under an identical *matched* GR+relativistic-solid action, same background, source and detector, the final full photon observable would again be identical as established by v15.760: no new Cone-specific operator has appeared. This is an important **negative originality gate**, even while detector modeling becomes more physical.

**Reproducer:** research-notes/k4_minkowski_tt_roundtrip_nullray_v15_794.py, additive commit **dc49135554481f3cc7dcf8691948cc367225e34d**. Independently run local SymPy calculations verified the outgoing/return transfer, both low-frequency and spatial limits, the perpendicular-arm frequency null and nontrivial oblique transfer values. External audit of the committed script remains pending.

**HANDOFF — external audit:** independently rederive first-order roundtrip photon travel time from the stated Fourier metric, including the outgoing/return phases and the factor L/2, compare with standard TT gauge mirror worldlines and check the long-wave and temporal-null limits. Do not confuse the finite-arm spatial-sampling proxy from v15.793 with a physical photon/timing signal. Audit v15.792 additive ShapeError repair against the original archived v15.787 reproducer.

**NEXT:** construct the full FLRW laser-ranging/gradiometer observable with appropriate free-fall mirror boundary conditions for the physical three-sector compact canonical source, and explicitly subtract the exactly matched GR+solid prediction. If no independent Cone operator/selector is derived, that full matched-response residual must remain zero.
