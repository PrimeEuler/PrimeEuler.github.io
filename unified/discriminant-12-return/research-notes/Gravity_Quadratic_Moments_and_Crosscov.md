# Gravity follow-on: quadratic 2/3, dimensional test, and orbit-averaged scale–shape noise orthogonality

Date 2026-10-22. Parents v14.592 §3 (Archimedes/Airy), v14.700–704, v14.708–713. Reproducer gravity_quadratic_moment_crosscov.py.

### Geometric factor [D]

For the cap y=h(1−x²/a²) on −a≤x≤a, the parabolic segment area is 4ah/3, and the chord–tangent circumscribing parallelogram has area 2ah. Their ratio is exactly 2/3. Thus the normalized average (1/2)∫_{−1}^1(1−x²)dx is the identical elementary integral. A previous conversational claim that the relevant bounding rectangle had area 4 for y=1−x² was mistaken; its width is 2 and height is 1, so its area is 2.

On S^{d−1} the isotropic coordinate moments satisfy E[x_i²]=1/d and E[1−x_i²]=(d−1)/d: the 2/3 is specifically d=3 in this general identity. The Airy bouncer's 2/3 exponent, by contrast, is the inverse action-scaling exponent 1/(3/2), and the hot-bath e²=2/3 is the coefficient-dependent stochastic drift zero. Numeric agreement does not identify all these mechanisms.

### Exact cross-covariance [D]

For high-speed isotropic diffusion D_0 I (half-covariance convention), frozen-orbit local primitive covariances are d[h]_t/dt=2D_0 v² and d[h,L]_t/dt=2D_0 L. With T=−μ/(2h), q=L√(−2h)/μ, the partial derivatives are
T_h=2T²/μ, q_h=q/(2h)=−qT/μ, q_L=q/L.
The local quadratic cross-variation rate is
\[
\frac{d[T,q]_t}{dt}=\frac{4D_0T^2q}{\mu}\left(1-\frac{Tv^2}{\mu}\right).
\]
The Kepler orbit average uses <v²>=μ/T and therefore **vanishes identically**, <d[T,q]/dt>=0, and likewise <d[T,e²]/dt>=0 because e²=1−q². The exact cancellation is **after secular averaging**, not pointwise.

This refines v14.713: the scale noise and eccentricity noise are instantaneously orthogonal in the orbit-averaged diffusion approximation, even though scale drift and scale variance remain of order the eccentricity rate C=10D_0T/μ. No timescale separation follows. Zero cross-covariance does NOT imply stochastic independence of T and eccentricity, because their marginal coefficients depend on T, the full process admits escape, and the averaging itself has a timescale-assumption boundary.

### Next gate

Construct the joint orbit-averaged generator explicitly in (T,z=e²), including the coefficients already known, and test whether a harmonic/conditional uniform z distribution survives T-dependent time-change and killing at h=0. Keep bound-preserving, cemetery/killed and surviving-conditioned laws distinct. The bath's drift-zero and its full population distribution are distinct; \(\Xi\) remains standard radial-gradiometry, with no derived bath-to-rotor coupling. No new G or physical apex/separatrix selection asserted.
