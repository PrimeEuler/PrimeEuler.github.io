# Cone Derivation Ledger v15.1319 — Negative tensor sign gate: archived Maxwell TT source versus stated spatial-metric plus convention

**Date:** 2026-11-22 Eastern. **Gravity/Cone lane. Status:** [NEGATIVE] the previously archived sourced tensor equation and archived TT spatial metric sign do not simultaneously satisfy the linearized Einstein TT spatial equation when the source `PiTT` is the actual positive Maxwell spatial-stress projection `Tij=rho deltaij−EiEj−BiBj`; [D] independent Christoffel-to-Einstein tensor plus-projection, independent original solid anisotropic pressure, concrete dealiased original compact-Maxwell nonzero oblique source; [OPEN] determine whether the physical tensor variable `gamma` was intended as negative of the metric strain, repair all uses additively if needed, full SVT numerical metric and optical readout. **Immediately pre-ledger HEAD:** c4b4306c50d1d3b3ec1e13274bc65f7b21066e1c. Proposed v15.1319 path checked absent, no overwrite. Preserve prior TT output as *historical* rather than silently altering it, preserve all Audit/Suzuki/Muse/Sandbox and K4 action.

## Gate 1251 — independent four-metric tensor Einstein operator

For one TT plus polarization, k along z, signature (-+++), coasting `a=τ/sqrt3`, declare the **spatial metric** `gxx=a²(1+gamma e^(ikz)), gyy=a²(1−gamma e^(ikz)), gzz=a²`. This is the same explicit metric convention stated in v15.787, not an inferred source-sign convention. A fresh local SymPy full connection/Ricci/Einstein computation linearized about FLRW, including perturbation of the inverse metric in mixed indices, gives

`delta G^x_x=+ (gamma''+3gamma'/τ+3k²gamma/τ²)/2`,
`delta G^y_y=− (gamma''+3gamma'/τ+3k²gamma/τ²)/2`,
`delta G^0_0=delta G^z_z=0` in the pure TT sector.

This is independent of the earlier electric-Riemann formula. In particular, the gravitational tensor source sign must be checked at the **spatial Einstein equation** rather than extrapolated from the tidal contact expression.

## Gate 1252 — independently varied Maxwell and original K4 material plus pressure

With the original relativistic solid `F=C(det B)^(1/3)[1+eta_s(tr B²/(tr B)²−1/3)]`, a TT spatial strain `gamma_xx=gamma, gamma_yy=−gamma` corresponds to infinitesimal material principal shear `beta_x=gamma/2, beta_y=−gamma/2`. The independently derived homogeneous tensor-shear constitutive law from v15.1264, verified by Audit Round 620, gives `delta p_s,x−delta p_s,y=−8eta_s C gamma/(9a²)`. Thus for eta_s=3/4,kappa C=1,a=τ/sqrt3, the x-type TT stress is `delta T^x_x,solid,plus=−gamma/τ²` (and opposite y). This agrees with direct first variation of the same F(B) at diagonal strain.

For Maxwell the literal source in v15.1262 is `Tij=rho δij−EiEj−BiBj`, and its TT plus coefficient is `Pi_plus=(Txx−Tyy)/2`, or equivalently `(Tee−Tbb)/2` in an orthonormal oblique polarization basis. Physical Maxwell plus pressure equals `9Pi_plus/τ⁴`.

The independently reconstructed plus Einstein equation is therefore
`[gamma''+3gamma'/τ+3k²gamma/τ²]/2 = 9Pi_plus/τ⁴ −gamma/τ²`,
or
`gamma''+3gamma'/τ+(3k²+2)gamma/τ²= +18Pi_plus/τ⁴`.

**Collision with archived sign:** v15.750/v15.1234/v15.1235/v15.1262 explicitly evolved `gamma''+3gamma'/τ+(3k²+2)gamma/τ²=−18Pi_plus/τ⁴` with the tensor field subsequently interpreted by v15.787's `gxx=a²(1+gamma)` and full electric Riemann `Eplus=−(gamma''+2gamma'/τ)/2`. If both `gamma` variables denote the same spatial metric strain and `Pi_plus` denotes the same Maxwell stress projector, these are incompatible. The gap in the x-type plus Einstein spatial residual is **−18 Pi_plus/τ⁴**, and the x−y difference is **−36 Pi_plus/τ⁴**. At the initial slice gamma=gamma'=0 the discrepancy cannot be attributed to preexisting shear data.

A possible resolution is a historical *variable sign* `gamma_evolution=−gamma_spatial_metric`; then the archived negative source could consistently drive a reversed physical strain, **provided every source/metric/curvature identification and vector/tensor comparison is changed consistently**. An alternative is a historical source projector definition `Pi_evolution=−Pi_physical`. The frozen source code's literal `PiTT` appears to use the standard physical Tij projection, so a hand-waved source sign is not sufficient. Audit must trace signs from the unexpanded Einstein+solid+Maxwell action.

## Gate 1253 — concrete falsification against unchanged compact Maxwell E0

Using the original v15.1078 compact initial E0, shared Nyquist-clean transverse Fourier projection of v15.1267, and 2N³ zero-padding before quadratic stress formation (v15.1274 scheme), compute `Pi_plus` at initial tau=1 for oblique k=(1,0,1), polarization `e=(1,0,-1)/sqrt2`, `b=(0,1,0)`. Fourier bin is (2,0,2) on L=4pi. The dealiased source is nonzero:

| N³ | Pi_plus(k,1) real | archived x-type TT Einstein residual at gamma=gamma'=0 |
|---|---:|---:|
| 24³ | +0.00048158021257934346 | −0.008668443826428182 |
| 32³ | +0.0004546200702725532 | −0.008183161264905958 |
| 48³ | +0.0004612348231110169 | −0.008302226815998303 |

Imaginary parts are <=3e-20 from conjugate/parity pairing. The residual is vastly larger than numerical roundoff. This is **not a new physical effect**: it is a sign mismatch between a sourced TT evolution convention and a declared spatial metric/sign convention in the existing Einstein–Maxwell+same-K4 calculation.

**Execution classification:** independent local SymPy geometric tensor calculation actually printed `Gxx=+(3k² gamma+τ²gamma''+3τgamma')/(2τ²)`, `Gyy=−Gxx`, `G00=Gzz=0`; independently varied K4 solid shears are inherited from audited v15.1264. A separate local NumPy calculation on the actual Maxwell compact source at 24³/32³/48³ executed and printed the table. Newly committed additive self-contained NumPy falsification reproducer `research-notes/k4_tt_source_sign_obstruction_v15_1319.py`, SHA c4b4306c50d1d3b3ec1e13274bc65f7b21066e1c, remains to be replayed from exact committed bytes by External Audit. It measures the initial-slice TT source residual, while the independent geometric derivation is documented here and available for Audit to rederive.

## Gate 1254 — hold the full spacetime claim and request independent correction

Do **not** promote v15.1267 full electric tidal trace or earlier tensor Weyl/full-Riemann amplitude to a fully physically sourced Einstein metric until this sign is resolved. The tidal *trace* cannot detect a purely TT sign fault, because TT trace is identically zero. Similarly v15.1314–1317 scalar closure and v15.1318 vector identity do not constrain TT source sign. They can remain provisionally valid on their own terms while this separate TT obstruction is audited.

**AUDIT HANDOFF (priority):** independently derive `δG^i_j,TT` directly from `gij=a²(δij+gammaij)` in the same metric signature; derive solid TT stress from original frozen F(B), and confirm `Tij_Maxwell=rhoδij−EiEj−BiBj` is the **physical** spatial mixed stress coefficient. Inspect v14.928/v14.935 tensor quadratic action for whether its tensor variable is defined with `gij=a²(δij−gammaij)`, then trace through v15.750, v15.787, v15.1234–1235, v15.1262 and downstream tides. Independently replay the concrete plus Maxwell 3-grid residual. If necessary, commit a **new additive, fully convention-reconciled TT equation and corrected physical metric/readout**, leaving all earlier historical certification records intact.

**Next physics:** after a satisfactory tensor sign reconciliation, close both TT polarizations, re-evolve metric from *one* dealiased Maxwell stress prescription, check the full coupled Einstein spatial/ADM residuals and only then calculate a finite-baseline causal photon–mirror–emitter-clock observable. With identical Einstein–Maxwell+K4 action on both sides, matched GR comparison remains null; no quarter-grid physical selector/G-free gravitational novelty established.
