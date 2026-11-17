# Cone Derivation Ledger v15.1100 — Acceleration worldline as confocal moving-secant trace and hyperbolic-secant circle

**Date:** 2026-11-17 Eastern. **Track:** Gravity/Cone. **Status:** [D] exact matching of uniformly accelerated Minkowski worldline to existing confocal-parabola/moving-secant cone map; [D] exact proper-time to compactified circle-angle derivative sech; [N] mesh half-steps do not imply equidistant proper time, equal circle angle or an action frequency; [O] new action-derived selector/curl-circle physical weld. **Live HEAD immediately before ledger write:** abf0f7ab3598c666a4b238a909b38bdd43f4191c (new reproducer), collision search performed; v15.1099 belongs to External Audit Round 593. Strict additive-only, no earlier certified, Suzuki, Sandbox, Muse or Audit objects modified.

## Ledger synchronization and priority
External Audit Round 593/v15.1099, commit 232b5900a66075575db14d93f37bee4e48813838, independently verified the six recent Gravity v15.1093–1098 results and their corrected scripts, finding no remaining mathematical error. Critically, **the raw parabola/secant to hyperbolic circle equations and the sech Jacobian are NOT new**. The ledger already contains the normalized rapidity circle and (d\theta=\operatorname{sech}u\,du) in v13.196/v13.691, and exactly the moving confocal-parabola secant map and unit-circle projection in v15.1053. User had proposed moving parallel secant through half-step confocal acceleration vertices with (v_k=(n-k^2)/(2k)). New focus of this gate is the previously-uncombined **physical proper-time identification** of that exact secant parameter with a uniformly accelerating worldline, plus its implications for lattice samples and time. No novel gravity force or selector is implied.

## Gate 945 — confocal parabola/secant equals accelerated worldline coordinate chart
Let physical proper acceleration be (a>0), speed of light (c), Rindler length (R=c^2/a), and define positive parameter (k) of dimension length. The family of Euclidean confocal parabolas on coordinates (X,Y) is
(Y^2=k^2-2kX); vertex at ((k/2,0)) and focus at (0,0). Intersect each with the moving-secant height (Y=R), giving
(X_k=(k^2-R^2)/(2k)).
Complete the cone shell with
(T_k=(k^2+R^2)/(2k)), hence (T_k^2-X_k^2=R^2), (T_k+X_k=k), (T_k-X_k=R^2/k).
The user's earlier sign convention for displacement is (v_k=-X_k=(R^2-k^2)/(2k)), which is identical after reversing the X axis.

Define rapidity (u=\log(k/R)) so (k=Re^u). Algebra gives
(T_k=R\cosh u,quad X_k=R\sinh u).
The uniformly accelerated Minkowski trajectory initially at rest in the inertial frame is
(ct=R\sinh(a\tau/c)), (x=R[\cosh(a\tau/c)-1]).
Thus **the exact secant family matches the trajectory** under (u=a\tau/c), (ct=X_k), (x=T_k-R). The sign/orientation of proper-time and displacement may be reversed; the identity is valid for all real rapidity, and the parabola's (k>0) samples all (u\in\mathbb R).

Important: the family of *confocal mesh parabolas* (Y^2=k^2-2kX) is not the same as the **local osculating parabola of the worldline** (v15.1096), which lives in the inertial ((x,ct)) plot and has focus at (x=R/2). The confocal parabolas all have focus 0 in an auxiliary ((X,Y)) plane; the worldline is the trajectory of their moving-secant intersection after the stated algebraic identification, not the path of a single mesh parabola. The physical acceleration is specified through (R=c^2/a): no dynamics or acceleration value is derived by this reparameterization.

## Gate 946 — hyperbolic-secant tracing law becomes proper-time angular law
The same shell's projective circle map is
(x_c/R=X_k/T_k=\tanh u),
(y_c/R=R/T_k=\operatorname{sech}u),
with (x_c^2+y_c^2=R^2); use unit coordinates if desired. Equivalently choose angle (θ\in(-\pi/2,\pi/2)) with (θ=\arctan\sinh u), (\sin\u03b8=\tanh u), (\cos\u03b8=\operatorname{sech}u). Exactly
(d\u03b8/du=\operatorname{sech}u),
(d\u03b8/d\tau=(a/c)\operatorname{sech}(a\tau/c)).
In terms of the positive parabola label,
(\u03b8(k)=2\arctan(k/R)-\pi/2), (d\u03b8/dk=2R/(k^2+R^2)). This is a real projective *compactification*, not a Wick-rotated periodic circle nor a real charged orbital trajectory. An accelerated worldline running through all rapidities traverses the **open upper semicircle** in this convention, from (-\pi/2) to (+\pi/2): its total unbounded-time angular advance is only \pi, not recurring rotations; no frequency selected.

## Gate 947 — half-step parabola lattice is nonuniform in proper time or circle angle
For a chosen external unit (h>0) (the arithmetic half-step (h=1/2) requires fixing physical units in length coordinate (k)), consecutive labels (k\to k+h) correspond to
(Δ\tau=(c/a)\log[(k+h)/k])
and
(Δ\u03b8=2[\arctan((k+h)/R)-\arctan(k/R)]).
Both vary with k and diminish as k grows, so a uniform lattice on the null label k is **not** a uniform proper-time clock or uniform circle-angle lattice. The involution (k\leftrightarrow R^2/k) mirrors (X\to-X) while leaving T unchanged; in general it does not map a fixed-additive k half-step lattice to itself. These exact results close off interpreting equally spaced confocal vertices as a selected physical rotation rate without extra dynamical boundary or sampling rules.

## Gate 948 — physical interpretation, existing curl and next action gate
A Maxwell current around an accelerated charge can have azimuthal magnetic circles in transverse **spatial** planes (Sandbox v15.1091). The auxiliary circle here is instead a **projective representation of longitudinal Minkowski hyperbolic rapidity**. Equal diagram radii or circle language do not imply a common physical orbit, action ∮ p·dx, current loop or acceleration-selected Compton radius. Likewise setting (R=\hbar/(mc)) remains the old v15.886 free-scale choice (ρ=1), not a consequence of (\operatorname{sech}u) tracing; all (ρ>0) are possible after choosing a different a for fixed m. The matched Einstein+same K4 solid and standard Dirac-Maxwell source remains unchanged, so no new gravitational or tidal operator has been found.

**Reproducer:** `research-notes/k4_acceleration_hyperbolic_secant_trace_v15_1100.py`, additive commit abf0f7ab3598c666a4b238a909b38bdd43f4191c. Independent local preliminary SymPy calculation passed for core parabola/secant/hyperbola/time and sech circle identities; full committed reproducer pending independent Audit re-execution. This entry does not claim that the full script has already been re-executed independently.

**AUDIT HANDOFF:** check complete script and distinct parabola families; ensure k=T+X, physical ct=X and x=T-R proper-time signs/dimensions; verify circle is *nonperiodic upper semicircle* and k-half-step sampling is not constant proper time; verify 90-degree orientation conventions and no Compton/Rindler scale selector. **NEXT:** formulate a physically grounded discrete time-node selection mechanism or worldline coupling to a transverse spin-current field, then test whether it selects a specific real k-lattice increment or ρ without importing it.
