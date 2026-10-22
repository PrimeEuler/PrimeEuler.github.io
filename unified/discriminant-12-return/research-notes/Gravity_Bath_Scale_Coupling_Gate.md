# Gravity bath gate: orbital scale is not slow relative to eccentricity

**2026-10-22.** Parents v14.710 (both competing files), v14.711 audit, v14.712, EFT v3.4. Source-exact high-speed isotropic velocity noise, \(D=D_0 I\) in the half-covariance convention.

## Coupled-generator test [D]

Let \(h=v^2/2-\mu/r\), \(T=-\mu/(2h)\) for bound energy h<0. With \({\cal L}h=3D_0\), \(\frac{d}{dt}[h]_t=2D_0v^2\), \(T_h=2T^2/\mu\), \(T_{hh}=8T^3/\mu^2\), and the exact Kepler orbit average \(\langle v^2\rangle=\mu/T\),

\[
\langle{\cal L}T\rangle
=\frac{2T^2}{\mu}(3D_0)
 +\frac12\frac{8T^3}{\mu^2}\biggl(2D_0\frac{\mu}{T}\biggr)
=\frac{14D_0T^2}{\mu}.
\]

\[
\biggl\langle\frac{d[T]_t}{dt}\biggr\rangle
=(T_h)^2\langle2D_0v^2\rangle
=\frac{8D_0T^3}{\mu}.
\]

The same source's shape rate is \(C=10D_0T/\mu\) in
\(A_\varepsilon=C(1-2\varepsilon)\) and \(D_\varepsilon=2C\varepsilon(1-\varepsilon)\). Therefore

\[
\boxed{\langle{\cal L}T\rangle/T=(7/5)C,\quad
\langle d[T]_t/dt\rangle/T^2=(4/5)C.}
\]

Both fractional drift and fractional quadratic-variation rates are order C, not parametrically smaller. **The required separation \(T\)-relaxation much slower than eccentricity relaxation is absent.** This closes the specific v14.711 audit gap in the negative for the hot high-speed model.

## What this does and does not invalidate

- The high-speed shape *instantaneous local and secular generator* and its drift zero e²=2/3 remain derivable, as in sandbox v14.710 and external audit v14.711.
- The one-dimensional Jacobi diffusion with fixed C has uniform stationary density p(e²)=1 and mean Gram functional (8 ln2−4)/3, exactly as in gravity v14.710. That is a **conditional idealization**, not an established long-time equilibrium of the full joint (T,e²) dynamics.
- Even though a generator C(T) times the same z-differential operator might preserve a uniform z marginal under some special cross-covariance structures, the actual joint generator includes shared velocity-noise cross terms and the bound/unbound boundary. One cannot infer or rule out a joint stationary law without determining those terms and boundary conditions.
- The positive local drift \({\cal L}T\) represents an Ito/convexity effect of T=-μ/(2h). T diverges on approach h=0−, so a global unconditional mean over escape trajectories need not exist. Do not extrapolate these bound-orbit averages past unbinding.
- The hot-limit ratio is independent of D0 and measured G, but is a **comparison of bath timescales**, not a novel gravitational field law or a predicted shift in Xi. No coupling from orbital bath noise to rotor field-slope response is supplied.

## Producer and next gate

Producer: research-notes/gravity_bath_scale_coupling_gate.py. Derive the full orbit-averaged two-dimensional generator including mixed \(T,\varepsilon\) covariance and the absorbing flux at h=0. Test whether conditional-on-survival distributions exhibit a distinct quasi-stationary shape law, with no assumption of a universal \(2/3\) stationary shape. Separate the finite-temperature Maxwellian corrections and the BPS bound-preserving and killed interpretations; source computations rather than invent coefficients.

## Ledger collision note

External audit v14.711 independently documented simultaneous v14.710 use: gravity Jacobi entry landed first and retains chronological title; sandbox drift-coefficients v14.710 landed one second later and requires an additive alias/erratum by its owner. Neither predecessor is rewritten here, and all references distinguish by full file name. This is a known version-number collision, not a missing result.
